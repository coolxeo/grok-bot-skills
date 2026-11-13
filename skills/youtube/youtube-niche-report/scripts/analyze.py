"""Step 4: turn the pull and the tags into data.json (every kept video with derived fields, and all tables).

usage:  python3 -I analyze.py --dir <work>        (no network; prints the tables for you to read)

Reads channels.json, catalog.jsonl, videos.jsonl, hooks.jsonl, tags.jsonl and, if present, hook-frames.jsonl.
"x channel" (out) = a video's views / the median views of its own channel's same tab in the full catalogue, so a big
channel's ordinary upload doesn't drown out a small channel's hit. 1.0 is an ordinary video for that channel.
"""
import datetime as dt
import json
import re
import statistics as st
import sys
from collections import Counter, defaultdict

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))  # works under python3 -I
from common import jl_read, load, workdir_arg

SCOPES = {"est_recent": "Established, recent", "est": "Established, all time", "all": "All screened",
          "small": "Small channels"}
DIMENSIONS = ["cluster", "format", "hook", "structure", "title_shape", "voice", "era", "tier"]


def first_screen(frames, vid):
    for o in (frames.get(vid) or {}).get("onscreen") or []:
        t = re.sub(r"\([^)]*\)", "", o.get("text") or "").strip()
        if t and not re.search(r"studio|presents|watermark|subscribe", t, re.I):
            return t
    return ""


def spoken_first(hooks, vid):
    for line in (hooks.get(vid) or {}).get("first60") or []:
        t = re.sub(r"&gt;|>>", "", line["text"]).strip()
        if t and not re.match(r"^\W*\[", t):
            return t
    return ""


def hook_of(cfg, tag, frames, hooks, vid, title):
    """The hook text is the first line on screen, else the first spoken line, else the title.
    Its class is the model's hook_type, unless config hook_rules ([[name, regex], ...]) match the text first."""
    cands = [first_screen(frames, vid), spoken_first(hooks, vid), tag.get("hook_text") or "", title]
    text = next((c for c in cands if c), title)
    for c in cands:
        for name, rx in cfg.get("hook_rules") or []:
            if c and re.search(rx, c, re.I):
                return name, c
    return tag.get("hook_type") or "other", text


def fmt(cfg, r):
    d = r.get("duration") or 0
    if r["tab"] == "shorts":
        return "Short, 30 s or less" if d <= 32 else ("Short, 33-60 s" if d <= 60 else "Short, over 60 s")
    if re.search(r"\bpart \d|\bep(isode)?\.? ?\d|#\d+\b", r["title"], re.I):
        return "Series episode"
    a, b = cfg["film_buckets"]
    mm = lambda s: f"{s // 60}:{s % 60:02d}"
    if d < a:
        return f"Video under {mm(a)}"
    if d <= b:
        return f"Video {mm(a)}-{mm(b)}"
    return f"Video over {mm(b)}"


def title_shape(title):
    t = re.split(r"\s[|(\[]|#", title)[0].strip()
    if re.search(r"\bpart \d|\bep(isode)?\.? ?\d", title, re.I):
        return "Series / Part N"
    if re.fullmatch(r"[A-Z0-9 ,'&!.-]{2,24}", t) and len(t.split()) <= 3:
        return "ONE-WORD CAPS"
    if re.match(r"^\d[\d,.]*\s?\$?\s?(minute|hour|day|second|week|month|year|step|way|tip|thing|mistake)s?\b", t, re.I) \
            or re.match(r"^(top )?\d+ ", t, re.I):
        return "Number first (7 tips)"
    if re.search(r"\?\s*$", t):
        return "Question"
    if re.match(r"^(i|i'm|i've|i'll|my|we)\b", t, re.I) or t.startswith(("\"", "'", "“")):
        return "First person"
    if re.match(r"^(you|your|you're|stop|don't|never|why you)\b", t, re.I):
        return "Second person / command"
    if re.search(r"\bvs\.?\b|\bversus\b", t, re.I):
        return "Versus"
    if re.search(r"\. \S", t) or re.search(r"\.\.\.|…", t):
        return "Two-beat sentence"
    if re.match(r"^how (to|i)\b", t, re.I):
        return "How to"
    return "Plain statement"


def table(rs, key):
    g = defaultdict(list)
    for r in rs:
        g[r[key]].append(r)
    out = []
    for k, x in g.items():
        v = [r["views"] for r in x]
        out.append({"k": k, "n": len(x), "med": st.median(v), "sum": sum(v),
                    "out": round(st.median([r["out"] for r in x]), 2), "hit": sum(1 for r in x if r["out"] >= 3),
                    "top": max(x, key=lambda r: r["views"])["id"]})
    return sorted(out, key=lambda o: -o["out"])


def main():
    root, cfg = load(workdir_arg(__doc__.splitlines()[0]).parse_args().dir)
    tags = {r["id"]: r for r in jl_read(root / "tags.jsonl")}
    vids = {r["id"]: r for r in jl_read(root / "videos.jsonl")}
    hooks = {r["id"]: r for r in jl_read(root / "hooks.jsonl")}
    frames = {r["id"]: r for r in jl_read(root / "hook-frames.jsonl")}
    cat = jl_read(root / "catalog.jsonl")
    chans = json.load(open(root / "channels.json", encoding="utf-8"))
    own_keys = {c["key"] for c in chans if c.get("why") == "own"}
    if not tags:
        raise SystemExit("tags.jsonl is empty: run tag.py first")

    pulled = cfg.get("pulled_at") or dt.date.fromtimestamp((root / "videos.jsonl").stat().st_mtime).isoformat()
    pull_day = dt.date.fromisoformat(pulled)
    wave = (cfg["wave_start"] or (pull_day - dt.timedelta(days=90)).isoformat()).replace("-", "")
    wave_label = f"since {wave[:4]}-{wave[4:6]}-{wave[6:]}"

    g = defaultdict(list)
    for r in cat:
        if r.get("view_count") is not None:
            g[(r["chan"], r["tab"])].append(r["view_count"])
    med = {k: st.median(v) for k, v in g.items()}
    cat_n = {k: len(v) for k, v in g.items()}

    rows = []
    for vid, t in tags.items():
        r = vids.get(vid)
        if not r:
            continue
        m = med.get((r["chan"], r["tab"])) or 1
        d = r.get("upload_date") or ""
        age = (pull_day - dt.date(int(d[:4]), int(d[4:6]), int(d[6:]))).days if d else None
        hc, htxt = hook_of(cfg, t, frames, hooks, vid, r["title"])
        f = frames.get(vid, {})
        rows.append({
            "id": vid, "keep": bool(t.get("keep")), "why_out": t.get("why_out", ""), "own": r["chan"] in own_keys,
            "chan": r["chan"], "channel": r.get("channel") or r["chan"], "subs": r.get("channel_follower_count"),
            "tab": r["tab"], "title": r["title"], "views": r.get("view_count") or 0, "likes": r.get("like_count"),
            "comments": r.get("comment_count"), "dur": r.get("duration"), "date": d, "age": age,
            "vpd": round((r.get("view_count") or 0) / max(age or 1, 1)),
            "out": round((r.get("view_count") or 0) / max(m, 1), 2), "chan_med": m,
            "era": wave_label if d >= wave else "older",
            "tier": f"established ({cfg['established_subs']:,}+ subs)" if (r.get("channel_follower_count") or 0) >= cfg["established_subs"]
            else f"small (<{cfg['established_subs']:,} subs)",
            "cluster": t.get("cluster") if t.get("cluster") in cfg["clusters"] else "other",
            "topic": t.get("topic", ""), "format": fmt(cfg, r), "voice": t.get("voice", "unknown"),
            "hook": hc, "hook_text": htxt[:140], "structure": t.get("structure") or "other",
            "title_shape": title_shape(r["title"]), "heat": r.get("heatmap20"), "frames": vid in frames,
            "cuts15": f.get("cut_count_first15"), "char_s": f.get("character_on_screen_by_s"),
        })

    keep = [r for r in rows if r["keep"] and not r["own"]]
    own = [r for r in rows if r["own"]]
    est = [r for r in keep if r["tier"].startswith("established")]
    tables = {}
    for key in DIMENSIONS:
        tables[key] = {"est_recent": table([r for r in est if r["era"] != "older"], key), "est": table(est, key),
                       "all": table(keep, key), "small": table([r for r in keep if not r["tier"].startswith("established")], key)}

    screen = []
    for c in chans:
        rs = [r for r in rows if r["chan"] == c["key"]]
        if not rs:
            continue
        reasons = Counter(r["why_out"].split(",")[0][:40] for r in rs if not r["keep"])
        screen.append({"chan": c["key"], "channel": rs[0]["channel"], "subs": rs[0]["subs"], "why": c.get("why", ""),
                       "pulled": len(rs), "kept": sum(r["keep"] for r in rs),
                       "catalog": cat_n.get((c["key"], "videos"), 0) + cat_n.get((c["key"], "shorts"), 0),
                       "reasons": reasons.most_common(3)})

    out = {"niche": cfg["niche"], "pulled_at": pulled, "era_label": wave_label, "scopes": SCOPES,
           "established_subs": cfg["established_subs"], "n_channels": len(chans), "n_catalog": len(cat),
           "n_pulled": len(rows), "n_kept": len(keep), "n_own": len(own), "clusters": cfg["clusters"],
           "tables": tables, "screen": screen, "videos": [r for r in rows if r["keep"]],
           "out_sample": sorted([{"id": r["id"], "channel": r["channel"], "title": r["title"], "views": r["views"],
                                  "why": r["why_out"]} for r in rows if not r["keep"]], key=lambda r: -r["views"])[:60]}
    json.dump(out, open(root / "data.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))

    print(f"kept {len(keep)} (+{len(own)} own) of {len(rows)} tagged; established {len(est)}; recent = {wave_label}")
    for key, tb in tables.items():
        print("==", key, "(all screened | established recent)")
        for o in tb["all"]:
            w = next((x for x in tb["est_recent"] if x["k"] == o["k"]), None) or {"n": 0, "out": 0, "med": 0}
            print(f"  {str(o['k'])[:34]:34} n={o['n']:4} med={o['med']:>11,.0f} x={o['out']:6.2f} hits={o['hit']:3}"
                  f"  | recent n={w['n']:3} x={w['out']:5.2f} med={w['med']:>10,.0f}")
    print("data.json written", file=sys.stderr)


if __name__ == "__main__":
    main()
