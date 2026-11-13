"""Step 2: screen and tag every pulled video with a language model: keep or out, topic, cluster, structure, hook.

usage:
  python3 tag.py --dir <work> export              write tag-batches/prompt-<name>.md (about 120 videos each)
  python3 tag.py --dir <work> import              read tag-batches/answer-<name>.json into tags.jsonl
  python3 tag.py --dir <work> run --cmd "<cmd>"   run <cmd> per batch and read its stdout as the answer

Pick the way your agent works:
  - The agent itself: run export, read each prompt file, write the JSON answer next to it as answer-<name>.json
    (same <name> as the prompt), run import. Rows that fail validation stay untagged; export again to retry them.
  - A model CLI: run with --cmd, where {prompt} is replaced by the prompt file path and {schema} by the schema file path,
    e.g. --cmd "grok -m <model> --output-format json --json-schema {schema} --prompt-file {prompt}".
    The answer can be the bare {"rows": [...]} object or any JSON that holds it (a "structuredOutput" or "result" key).

Resumable: ids already in tags.jsonl are skipped. Channels found only by search get shorter rows (no description, a
shorter first60; they are often off-niche). Your own channel's videos are tagged too, so they can be compared, but never screened out.
"""
import hashlib
import json
import re
import shlex
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))  # works under python3 -I
from common import jl_append, jl_read, load, workdir_arg

BATCH = 120


def schema(cfg):
    def enum(vals):
        return {"type": "string", "enum": list(vals)}

    row = {"type": "object", "properties": {
        "id": {"type": "string"}, "keep": {"type": "boolean"}, "why_out": {"type": "string"},
        "topic": {"type": "string"}, "cluster": enum(cfg["clusters"]), "structure": enum(cfg["structures"]),
        "hook_type": enum(cfg["hook_types"]), "hook_text": {"type": "string"},
        "voice": enum(["narrator", "on_camera_talk", "dialogue", "text_only", "music_only", "unknown"])}}
    row["required"] = list(row["properties"])
    return {"type": "object", "properties": {"rows": {"type": "array", "items": row}}, "required": ["rows"]}


def prompt(cfg):
    cl = "\n".join(f"  {k}: {v}" for k, v in cfg["clusters"].items())
    return f"""You are screening YouTube videos for a niche study. The niche: {cfg['niche']}

For each row decide:
keep: {cfg['keep_rule'] or 'true only if the video is squarely in the niche above.'} Rows marked "own": true are always keep: true.
why_out: a short reason when keep is false, else "".
topic: a 2-5 word label of the specific subject.
cluster: one of
{cl}
structure: one of {' | '.join(cfg['structures'])}. How the video is built from start to end.
hook_type: one of {' | '.join(cfg['hook_types'])}. How the first seconds grab the viewer; judge from first60 (the first 60 s of captions) and the title.
hook_text: the opening line from first60, or the title if there is none.
voice: narrator | on_camera_talk | dialogue | text_only | music_only | unknown. Empty first60 or only [Music] means text_only, music_only or unknown.
Return exactly one entry per input row, with the same ids, as JSON: {{"rows": [...]}}. Do not use any tools; answer from the rows below.

ROWS (JSON lines):
"""


def build_rows(root):
    chans = json.load(open(root / "channels.json", encoding="utf-8"))
    broad = {c["key"] for c in chans if c.get("why", "").startswith("discovered")}
    own = {c["key"] for c in chans if c.get("why") == "own"}
    hooks = {r["id"]: r for r in jl_read(root / "hooks.jsonl")}
    seen, rows = set(), []
    for v in jl_read(root / "videos.jsonl"):
        if not v.get("id") or v["id"] in seen:
            continue
        seen.add(v["id"])
        first60 = " / ".join(x["text"] for x in hooks.get(v["id"], {}).get("first60", []))[:400]
        row = {"id": v["id"], "chan": v["chan"], "channel": v.get("channel"), "tab": v["tab"], "title": v.get("title"),
               "duration": v.get("duration"), "view_count": v.get("view_count"), "upload_date": v.get("upload_date")}
        if v["chan"] in own:
            row["own"] = True
        if v["chan"] in broad:  # title-first rows: keep the opening line short, skip the description
            row.update(first60=first60[:160])
        else:
            row.update(description=(v.get("description") or "")[:300], first60=first60)
        rows.append((v["chan"] in broad, row))
    return rows


def batches(root):
    done = {r["id"] for r in jl_read(root / "tags.jsonl")}
    rows = [(b, r) for b, r in build_rows(root) if r["id"] not in done]
    out = []
    for broad in (False, True):
        part = [r for b, r in rows if b == broad]
        size = BATCH * 2 if broad else BATCH
        out += [part[i:i + size] for i in range(0, len(part), size)]
    return out


def find_rows(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("rows"), list):
            return obj["rows"]
        for k in ("structuredOutput", "structured_output", "result", "output", "content"):
            if k in obj:
                got = find_rows(obj[k])
                if got is not None:
                    return got
    if isinstance(obj, list) and obj and isinstance(obj[0], dict) and "id" in obj[0]:
        return obj
    if isinstance(obj, str):
        m = re.search(r"\{.*\}", obj, re.S)
        if m:
            try:
                return find_rows(json.loads(m.group(0)))
            except Exception:
                return None
    return None


VOICES = ["narrator", "on_camera_talk", "dialogue", "text_only", "music_only", "unknown"]


def valid(g, cfg):
    """Coerce one answer row to the schema; return None when it can't be trusted."""
    if not isinstance(g, dict) or not isinstance(g.get("id"), str):
        return None
    keep = g.get("keep")
    if isinstance(keep, str) and keep.lower() in ("true", "false"):
        keep = keep.lower() == "true"
    if not isinstance(keep, bool):
        return None
    out = {"id": g["id"], "keep": keep}
    for k in ("why_out", "topic", "hook_text"):
        out[k] = g.get(k) if isinstance(g.get(k), str) else ""
    for k, allowed, fallback in (("cluster", cfg["clusters"], "other"), ("structure", cfg["structures"], "other"),
                                 ("hook_type", cfg["hook_types"], "other"), ("voice", VOICES, "unknown")):
        out[k] = g.get(k) if g.get(k) in allowed else fallback
    return out


def merge(batch, got, cfg):
    """Valid rows for ids in this batch, one per id. Ids left out are retried by the next export or run."""
    want = {r["id"]: r for r in batch}
    out, seen, bad = [], set(), 0
    for g in got or []:
        g = valid(g, cfg)
        if not g or g["id"] not in want or g["id"] in seen:
            bad += 1
            continue
        seen.add(g["id"])
        w = want[g["id"]]
        if w.get("own"):
            g["keep"], g["why_out"] = True, ""
        out.append({"chan": w["chan"], "tab": w["tab"], **g})
    missing = len(want) - len(seen)
    if bad or missing:
        print(f"  {bad} invalid or duplicate rows dropped, {missing} ids without a valid answer (they stay untagged)",
              file=sys.stderr)
    return out


def batch_name(b):
    """A name tied to the ids in the batch, so an answer can never be paired with different rows."""
    return hashlib.sha1(" ".join(r["id"] for r in b).encode()).hexdigest()[:10]


def export(root, cfg):
    d = root / "tag-batches"
    d.mkdir(exist_ok=True)
    for old in list(d.glob("prompt-*.md")) + list(d.glob("batch-*.json")):  # stale batches from an earlier export
        old.unlink()
    (d / "schema.json").write_text(json.dumps(schema(cfg)), encoding="utf-8")
    bs = batches(root)
    for b in bs:
        name = batch_name(b)
        (d / f"prompt-{name}.md").write_text(prompt(cfg) + "\n".join(json.dumps(r, ensure_ascii=False) for r in b),
                                             encoding="utf-8")
        (d / f"batch-{name}.json").write_text(json.dumps(b, ensure_ascii=False), encoding="utf-8")
    print(f"{sum(map(len, bs))} rows in {len(bs)} prompt files in {d}", file=sys.stderr)


def import_(root, cfg):
    d = root / "tag-batches"
    n = 0
    for bf in sorted(d.glob("batch-*.json")):
        af = d / bf.name.replace("batch-", "answer-")
        if not af.exists():
            print(f"missing {af.name}", file=sys.stderr)
            continue
        print(af.name, file=sys.stderr)
        try:
            answer = json.load(open(af, encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"  not valid JSON ({e}); fix it and import again", file=sys.stderr)
            continue
        rows = merge(json.load(open(bf, encoding="utf-8")), find_rows(answer), cfg)
        jl_append(root / "tags.jsonl", rows)
        n += len(rows)
        bf.rename(bf.with_suffix(".done"))
    print(f"imported {n} rows", file=sys.stderr)


def run(root, cfg, cmd, workers):
    d = root / "tag-batches"
    d.mkdir(exist_ok=True)
    sf = d / "schema.json"
    sf.write_text(json.dumps(schema(cfg)), encoding="utf-8")

    def one(item):
        i, b = item
        pf = d / f"run-{i:03d}.md"
        pf.write_text(prompt(cfg) + "\n".join(json.dumps(r, ensure_ascii=False) for r in b), encoding="utf-8")
        args = [a.replace("{prompt}", str(pf)).replace("{schema}", str(sf)) for a in shlex.split(cmd)]
        for attempt in range(2):
            try:
                p = subprocess.run(args, capture_output=True, text=True, timeout=1800)
            except subprocess.TimeoutExpired:
                print(f"batch {i} timed out (try {attempt + 1})", file=sys.stderr)
                continue
            try:
                got = find_rows(json.loads(p.stdout))
            except Exception:
                got = find_rows(p.stdout)
            if got:
                out = merge(b, got, cfg)
                print(f"batch {i}: {len(out)}/{len(b)}", file=sys.stderr)
                return out
            print(f"batch {i} failed (try {attempt + 1}): {p.stderr.strip()[-300:]}", file=sys.stderr)
        return []

    bs = batches(root)
    print(f"{sum(map(len, bs))} rows in {len(bs)} batches", file=sys.stderr)
    with ThreadPoolExecutor(workers) as ex:
        for out in ex.map(one, enumerate(bs)):
            jl_append(root / "tags.jsonl", out)


def main():
    p = workdir_arg(__doc__.splitlines()[0])
    p.add_argument("mode", choices=["export", "import", "run"])
    p.add_argument("--cmd", help="model command for run mode; {prompt} and {schema} are replaced by file paths")
    p.add_argument("--workers", type=int, default=3)
    a = p.parse_args()
    root, cfg = load(a.dir)
    if a.mode == "export":
        export(root, cfg)
    elif a.mode == "import":
        import_(root, cfg)
    else:
        if not a.cmd:
            raise SystemExit("run needs --cmd")
        run(root, cfg, a.cmd, a.workers)
    tags = jl_read(root / "tags.jsonl")
    print(f"tags.jsonl: {len(tags)} tagged, {sum(bool(t.get('keep')) for t in tags)} kept", file=sys.stderr)


if __name__ == "__main__":
    main()
