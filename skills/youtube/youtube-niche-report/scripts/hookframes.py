"""Step 3: frame sheets of the openings that beat their channel most, for reading hooks frame by frame.

usage:  python3 hookframes.py --dir <work>        (after tag.py; resumable; read-only on YouTube)

Needs yt-dlp and ffmpeg. Picks the hook_sheets kept videos with the highest views / channel median (same tab), at most
hook_sheets_per_channel per channel, about hook_sheet_shorts of them Shorts, plus your own channel's hook_sheets_own
newest uploads (when own_channel is set). --ids a,b,c sheets just those videos. For each it downloads only the first 60 s
at 480p into .hooks/ (not for sharing) and writes:

  thumbs/hook-<id>.jpg   9 frames at 0.5, 2, 4, 7, 10, 15, 22, 30 and 45 s in a 3x3 sheet, read left to right, top to bottom;
                         a clip shorter than 46 s gets its 9 frames spread evenly over its real length instead. Shorts
                         use 9:16 cells (180x320), so vertical text stays readable; videos use 16:9 cells (320x180).
  hook-picks.json        the ids picked, best first, each with the frame times (s) its sheet used

Then look at each sheet yourself and write hook-frames.jsonl (one line per sheet, see references/method.md):
  {"id": "...", "onscreen": [{"t": 0.5, "text": "first line on screen"}], "first_visual": "...",
   "cut_count_first15": 3, "character_on_screen_by_s": 4}
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from statistics import median

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))  # works under python3 -I
from common import jl_read, load, workdir_arg

STAMPS = [0.5, 2, 4, 7, 10, 15, 22, 30, 45]


def clip_length(clip):
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(clip)],
                       capture_output=True, text=True)
    try:
        return float(p.stdout.strip())
    except ValueError:
        return None


def stamps_for(length):
    """The fixed times when the clip is long enough, else 9 times spread from 0.5 s to just before the end."""
    if not length or length > STAMPS[-1] + 1:
        return STAMPS
    end = max(length - 0.6, 1.0)
    return [round(0.5 + (end - 0.5) * i / 8, 1) for i in range(9)]


def pick(root, cfg):
    own = {c["key"] for c in json.load(open(root / "channels.json", encoding="utf-8")) if c.get("why") == "own"}
    meds = {}
    for r in jl_read(root / "catalog.jsonl"):
        if r.get("view_count") is not None:
            meds.setdefault((r["chan"], r["tab"]), []).append(r["view_count"])
    meds = {k: median(v) for k, v in meds.items()}
    views = {v["id"]: v.get("view_count") or 0 for v in jl_read(root / "videos.jsonl")}
    kept = [t for t in jl_read(root / "tags.jsonl") if t.get("keep") and t["chan"] not in own]
    for t in kept:
        t["lift"] = views.get(t["id"], 0) / max(1, meds.get((t["chan"], t["tab"]), 1))
    kept.sort(key=lambda t: -t["lift"])
    out, per = [], {}

    def take(rows, n):
        got = 0
        for t in rows:
            if got >= n:
                break
            if per.get(t["chan"], 0) < cfg["hook_sheets_per_channel"] and t["id"] not in out:
                out.append(t["id"])
                per[t["chan"]] = per.get(t["chan"], 0) + 1
                got += 1

    take([t for t in kept if t["tab"] == "shorts"], cfg["hook_sheet_shorts"])
    take([t for t in kept if t["tab"] == "videos"], cfg["hook_sheets"] - len(out))
    # your own channel: its newest uploads, so its openings can be read the same way as the leaders'
    if own and cfg["hook_sheets_own"]:
        mine = [v for v in jl_read(root / "videos.jsonl") if v["chan"] in own]
        mine.sort(key=lambda v: v.get("upload_date") or "", reverse=True)
        out += [v["id"] for v in mine if v["id"] not in out][:cfg["hook_sheets_own"]]
    return out


def sheet(root, vid, tab):
    """Returns the frame times used, or None when no sheet could be made."""
    dest = root / "thumbs" / f"hook-{vid}.jpg"
    times = root / "thumbs" / f"hook-{vid}.times.json"
    if dest.exists():
        return json.load(open(times)) if times.exists() else STAMPS
    clips = root / ".hooks"
    clips.mkdir(exist_ok=True)
    clip = clips / f"{vid}.mp4"
    if not clip.exists():
        subprocess.run(["yt-dlp", "--no-warnings", "-q", "--download-sections", "*0-60",
                        "-f", "bv*[height<=480]+ba/b[height<=480]", "--merge-output-format", "mp4", "-o", str(clip),
                        f"https://www.youtube.com/watch?v={vid}"], capture_output=True, text=True, timeout=300)
    if not clip.exists():
        print(f"clip failed {vid}", file=sys.stderr)
        return None
    w, h = (180, 320) if tab == "shorts" else (320, 180)
    fit = f"scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2"
    frames = clips / vid
    frames.mkdir(exist_ok=True)
    for old in frames.glob("*.png"):
        old.unlink()
    ts = stamps_for(clip_length(clip))
    for i, t in enumerate(ts):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", str(clip), "-frames:v", "1",
                        "-vf", fit, str(frames / f"{i:02d}.png")])
    if not list(frames.glob("*.png")):
        return None
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "1", "-pattern_type", "glob",
                    "-i", str(frames / "*.png"), "-vf", "tile=3x3", "-frames:v", "1", "-q:v", "4", str(dest)])
    if not dest.exists():
        return None
    times.write_text(json.dumps(ts))
    return ts


def main():
    ap = workdir_arg(__doc__.splitlines()[0])
    ap.add_argument("--ids", help="comma-separated video ids to sheet instead of the automatic pick")
    a = ap.parse_args()
    root, cfg = load(a.dir)
    (root / "thumbs").mkdir(exist_ok=True)
    ids = [i.strip() for i in a.ids.split(",") if i.strip()] if a.ids else pick(root, cfg)
    tabs = {v["id"]: v["tab"] for v in jl_read(root / "videos.jsonl")}
    tabs.update({t["id"]: t["tab"] for t in jl_read(root / "tags.jsonl")})
    with ThreadPoolExecutor(3) as ex:
        got = list(ex.map(lambda v: sheet(root, v, tabs.get(v, "videos")), ids))
    picks = root / "hook-picks.json"
    old = [p for p in (json.load(open(picks)) if picks.exists() else []) if p["id"] not in ids] if a.ids else []
    json.dump(old + [{"id": v, "stamps": ts} for v, ts in zip(ids, got)], open(picks, "w"))
    for v, ts in zip(ids, got):
        if ts and ts != STAMPS:
            print(f"  {v}: short clip, frames at {', '.join(map(str, ts))} s", file=sys.stderr)
    print(f"hook sheets: {sum(ts is not None for ts in got)}/{len(ids)} in {root / 'thumbs'}", file=sys.stderr)


if __name__ == "__main__":
    main()
