"""Step 1: pull a niche from YouTube, read-only, with yt-dlp.

usage:  python3 pull.py --dir <work folder> [--discover-only]     (resumable: finished steps and rows are skipped)

Needs yt-dlp and curl on a network that reaches YouTube. Nothing on YouTube is changed and nothing is downloaded
except captions and 320 px thumbnails. A niche of about 30 channels takes 30-60 minutes.

Writes into the work folder:
  discovery.jsonl   flat results of the search queries (finds channels the seed list missed)
  channels.json     the channels pulled: seeds, your own channel if set, and up to max_discovered found ones, with why
  catalog.jsonl     every video and Short listed on each channel (flat, rounded views): the base for channel medians
  videos.jsonl      full metadata of each channel's top_per_tab videos and top_per_tab Shorts by views, plus its
                    recent_per_tab newest uploads per tab (marked "sample": "recent"),
                    with YouTube's "most replayed" curve in 20 buckets when it exists
  hooks.jsonl       the first 60 s of captions (manual or auto) for each channel's top hooks_per_tab per tab;
                    falls back to youtube-transcript-api when it is installed and yt-dlp finds none
  thumbs/<id>.jpg   320 px thumbnail of each channel's top thumbs_per_channel videos
"""
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))  # works under python3 -I
from common import channel_url, handle_key, jl_append, jl_read, jl_write, load, workdir_arg


MISSING = re.compile(r"does not have a|this channel has no|no videos? (found|available)", re.I)
FAILED = []  # (what, why) for every request that failed, reported at the end of each stage


def ytdlp_ok(args, timeout=900):
    """Run yt-dlp; return (stdout, ok). ok is False when the request failed (not when a tab simply doesn't exist)."""
    err = ""
    for attempt in range(3):
        try:
            p = subprocess.run(["yt-dlp", "--no-warnings", *args], capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            err = f"timed out after {timeout} s"
            continue
        if p.returncode == 0 or p.stdout.strip():
            return p.stdout, True
        err = p.stderr.strip()[-300:]
        if MISSING.search(err):
            return "", True
        if "429" in err or "rate" in err.lower():
            time.sleep(30 * (attempt + 1))
            continue
        break
    FAILED.append((args[-1], err))
    print("yt-dlp failed:", args[-1], err, file=sys.stderr)
    return "", False


def ytdlp(args, timeout=900):
    return ytdlp_ok(args, timeout)[0]


def report_failures(stage):
    if FAILED:
        print(f"{stage}: {len(FAILED)} requests failed; run again to retry them", file=sys.stderr)
        for what, why in FAILED[:10]:
            print(f"  {what}: {why}", file=sys.stderr)
        FAILED.clear()


def as_json(out):
    try:
        d = json.loads(out)
    except Exception:
        return None
    return d if isinstance(d, dict) else None  # yt-dlp prints null for a missing tab


# 1. discovery -----------------------------------------------------------------------------------------------
def discover(root, cfg):
    path = root / "discovery.jsonl"
    if path.exists():
        return jl_read(path)

    def one(q):
        out, ok = ytdlp_ok(["--flat-playlist", "-J", f"ytsearch{cfg['search_depth']}:{q}"])
        if not ok:
            return None
        d = as_json(out) or {}
        return [{"query": q, "id": e.get("id"), "title": e.get("title"), "channel": e.get("channel"),
                 "channel_id": e.get("channel_id"), "channel_url": e.get("channel_url"),
                 "view_count": e.get("view_count"), "duration": e.get("duration")}
                for e in d.get("entries") or [] if e]

    rows, failed = [], 0
    with ThreadPoolExecutor(cfg["workers"]) as ex:
        for r in ex.map(one, cfg["queries"]):
            if r is None:
                failed += 1
            else:
                rows += r
    if failed:  # don't cache a partial search: the next run retries every query
        report_failures("discovery")
        raise SystemExit(f"{failed} of {len(cfg['queries'])} searches failed; nothing saved. Run again.")
    jl_write(path, rows)
    return rows


def pick_channels(root, cfg, disc):
    path = root / "channels.json"
    if path.exists():
        return json.load(open(path, encoding="utf-8"))
    chans = [{"key": handle_key(h), "url": channel_url(h), "why": "seed"} for h in cfg["seed_channels"]]
    if cfg["own_channel"]:
        chans.append({"key": handle_key(cfg["own_channel"]), "url": channel_url(cfg["own_channel"]), "why": "own"})
    known = set()
    for c in chans:  # resolve channel ids so a seed found again by search isn't added twice
        d = as_json(ytdlp(["--flat-playlist", "--playlist-end", "1", "-J", c["url"] + "/videos"], timeout=120)) or {}
        c["channel_id"] = d.get("channel_id") or d.get("id")
        c["name"] = d.get("channel") or d.get("uploader") or c["key"]
        known.add(c["channel_id"])
    by = defaultdict(list)
    for r in disc:
        if r.get("channel_id"):
            by[r["channel_id"]].append(r)
    cand = []
    for cid, rs in by.items():
        hits = len({r["query"] for r in rs})  # distinct searches, not videos
        top = max((r.get("view_count") or 0) for r in rs)
        if cid not in known and hits >= cfg["discover_min_hits"] and top >= cfg["discover_min_views"]:
            cand.append((hits, top, cid, rs[0].get("channel"), rs[0].get("channel_url")))
    cand.sort(key=lambda c: (-c[0], -c[1]))
    for hits, top, cid, name, url in cand[:cfg["max_discovered"]]:
        chans.append({"key": cid, "url": url or f"https://www.youtube.com/channel/{cid}", "channel_id": cid,
                      "name": name, "why": f"discovered: {hits} search hits, top {top:,} views"})
    json.dump(chans, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return chans


# 2. catalogue -----------------------------------------------------------------------------------------------
def catalog(root, cfg, chans):
    path = root / "catalog.jsonl"
    if path.exists():
        return jl_read(path)

    def one(c):
        rows = []
        for tab in ("videos", "shorts"):
            out, ok = ytdlp_ok(["--flat-playlist", "--playlist-end", str(cfg["tab_cap"]), "-J", f"{c['url']}/{tab}"])
            if not ok:
                return None
            d = as_json(out)
            if not d:  # the channel has no such tab
                continue
            for e in d.get("entries") or []:
                if e:
                    rows.append({"chan": c["key"], "channel": d.get("channel") or d.get("uploader"), "tab": tab,
                                 "id": e.get("id"), "title": e.get("title"), "view_count": e.get("view_count"),
                                 "duration": e.get("duration")})
        print(f"catalog {c['key']}: {len(rows)}", file=sys.stderr)
        return rows

    rows, failed = [], 0
    with ThreadPoolExecutor(cfg["workers"]) as ex:
        for r in ex.map(one, chans):
            if r is None:
                failed += 1
            else:
                rows += r
    if failed:  # a missing channel would skew every median, so don't cache a partial catalogue
        report_failures("catalog")
        raise SystemExit(f"{failed} of {len(chans)} channels failed to list; nothing saved. Run again.")
    jl_write(path, rows)
    return rows


def top_ids(cat, n, recent=0):
    """Per (channel, tab): the n most viewed ids, then the `recent` newest ids not already in (the flat listing is
    newest first). The newest ones are an unbiased sample of what a channel uploads now, so 'recent' tables and
    cadence aren't built only from the winners."""
    by = defaultdict(list)
    for r in cat:
        if r.get("id"):
            by[(r["chan"], r["tab"])].append(r)
    out = {}
    for k, rs in by.items():
        top = [r["id"] for r in sorted(rs, key=lambda r: -(r.get("view_count") or 0))[:n]]
        new = [r["id"] for r in rs[:recent] if r["id"] not in top]
        out[k] = top + new
    return out


# 3. full metadata -------------------------------------------------------------------------------------------
KEEP = ["id", "title", "channel", "channel_id", "uploader_id", "channel_follower_count", "view_count", "like_count",
        "comment_count", "duration", "upload_date", "tags", "categories", "chapters", "language"]


def slim(d, chan, tab, rank, top_n=None):
    r = {k: d.get(k) for k in KEEP}
    r.update(chan=chan, tab=tab, rank=rank, description=(d.get("description") or "")[:800])
    if top_n is not None and rank > top_n:
        r["sample"] = "recent"  # pulled because it is new, not because it is a top video
    hm = d.get("heatmap") or []
    if hm:
        b = [0.0] * 20
        dur = d.get("duration") or hm[-1]["end_time"]
        for h in hm:
            i = min(19, int(h["start_time"] / dur * 20)) if dur else 0
            b[i] = max(b[i], round(h["value"], 3))
        r["heatmap20"] = b
    return r


def fetch_full(root, cfg, cat):
    path = root / "videos.jsonl"
    done = {(r["chan"], r["id"]) for r in jl_read(path)}

    def one(item):
        (chan, tab), ids = item
        rows = []
        for rank, vid in enumerate(ids, 1):
            if (chan, vid) in done:
                continue
            out = ytdlp(["--skip-download", "-j", f"https://www.youtube.com/watch?v={vid}"], timeout=120)
            try:
                rows.append(slim(json.loads(out.splitlines()[0]), chan, tab, rank, cfg["top_per_tab"]))
            except Exception:
                pass
        print(f"full {chan}/{tab}: {len(rows)} new", file=sys.stderr)
        return rows

    with ThreadPoolExecutor(cfg["workers"]) as ex:
        for rows in ex.map(one, top_ids(cat, cfg["top_per_tab"], cfg["recent_per_tab"]).items()):
            jl_append(path, rows)


# 4. hooks: first 60 s of captions ---------------------------------------------------------------------------
def vtt_head(text, secs=60):
    out, last = [], None
    for block in text.split("\n\n"):
        m = re.search(r"(\d+):(\d+):(\d+)\.\d+ -->", block)
        if not m:
            continue
        t = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
        if t > secs:
            break
        for line in block.splitlines()[1:]:
            line = re.sub(r"<[^>]+>", "", line).strip()
            if line and "-->" not in line and line != last:
                out.append((t, line))
                last = line
    return out


def transcript_head(vid, langs, secs=60):
    """Fallback when yt-dlp finds no captions. Optional: needs youtube-transcript-api."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return []
    want = [l for base in langs for l in (base, f"{base}-US", f"{base}-GB")]
    try:
        try:
            items = YouTubeTranscriptApi().fetch(vid, languages=want).to_raw_data()
        except AttributeError:  # versions before 1.0
            items = YouTubeTranscriptApi.get_transcript(vid, languages=want)
    except Exception:
        return []
    return [(int(x["start"]), x["text"]) for x in items if x["start"] <= secs]


def hooks(root, cfg, cat):
    path = root / "hooks.jsonl"
    done = {r["id"] for r in jl_read(path)}
    subdir = root / ".subs"
    subdir.mkdir(exist_ok=True)
    langs = ",".join(f"{l}.*,{l}" for l in cfg["caption_langs"])

    def one(item):
        (chan, tab), ids = item
        rows = []
        for vid in ids:
            if vid in done:
                continue
            _, ok = ytdlp_ok(["--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", langs,
                              "--sub-format", "vtt", "--sleep-subtitles", "1", "-o", str(subdir / "%(id)s"),
                              f"https://www.youtube.com/watch?v={vid}"], timeout=120)
            if not ok:  # leave it out so the next run retries it
                continue
            files = sorted(subdir.glob(f"{vid}*.vtt"), key=lambda p: ("orig" in p.name, len(p.name)))
            lines = vtt_head(files[0].read_text(encoding="utf-8", errors="ignore")) if files else []
            src = "yt-dlp" if files else ""
            if not files:
                lines = transcript_head(vid, cfg["caption_langs"])
                src = "youtube-transcript-api" if lines else ""
            rows.append({"chan": chan, "tab": tab, "id": vid, "has_subs": bool(lines), "source": src,
                         "first60": [{"t": t, "text": x} for t, x in lines]})
        return rows

    with ThreadPoolExecutor(cfg["workers"]) as ex:
        for rows in ex.map(one, top_ids(cat, cfg["hooks_per_tab"]).items()):
            jl_append(path, rows)


# 5. thumbnails ----------------------------------------------------------------------------------------------
def thumbs(root, cfg, cat):
    d = root / "thumbs"
    d.mkdir(exist_ok=True)
    for (chan, tab), ids in top_ids(cat, cfg["thumbs_per_channel"]).items():
        if tab != "videos":
            continue
        for vid in ids:
            dest = d / f"{vid}.jpg"
            if not dest.exists():
                subprocess.run(["curl", "-sfL", "-o", str(dest), f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg"])


def main():
    ap = workdir_arg(__doc__.splitlines()[0])
    ap.add_argument("--discover-only", action="store_true",
                    help="stop after writing channels.json, so you can review it before the long pull")
    args = ap.parse_args()
    root, cfg = load(args.dir)
    if not cfg["queries"] and not cfg["seed_channels"]:
        raise SystemExit("config.json needs at least one of queries or seed_channels")
    disc = discover(root, cfg)
    print("discovery rows", len(disc), file=sys.stderr)
    chans = pick_channels(root, cfg, disc)
    print("channels", len(chans), [c.get("name") or c["key"] for c in chans], file=sys.stderr)
    if args.discover_only:
        print(f"review {root / 'channels.json'}, drop off-niche channels, then run again without --discover-only",
              file=sys.stderr)
        return
    cat = catalog(root, cfg, chans)
    print("catalog rows", len(cat), file=sys.stderr)
    fetch_full(root, cfg, cat)
    report_failures("full metadata")
    hooks(root, cfg, cat)
    report_failures("captions")
    thumbs(root, cfg, cat)
    print("done", file=sys.stderr)


if __name__ == "__main__":
    main()
