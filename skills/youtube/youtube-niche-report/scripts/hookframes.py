"""Step 3: frame sheets of the openings that beat their channel most, for reading hooks frame by frame.

usage:  python3 hookframes.py --dir <work>        (after tag.py; resumable; read-only on YouTube)

Needs yt-dlp and ffmpeg. Picks the hook_sheets kept videos with the highest views / channel median (same tab), at most
hook_sheets_per_channel per channel, about hook_sheet_shorts of them Shorts. For each it downloads only the first 60 s
at 480p into .hooks/ (not for sharing) and writes:

  thumbs/hook-<id>.jpg   9 frames at 0.5, 2, 4, 7, 10, 15, 22, 30 and 45 s in a 3x3 sheet, read left to right, top to bottom
  hook-picks.json        the ids picked, best first

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


def pick(root, cfg):
    own = {c["key"] for c in json.load(open(root / "channels.json")) if c.get("why") == "own"}
    meds = {}
    for r in jl_read(root / "catalog.jsonl"):
        if r.get("view_count"):
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
    return out


def sheet(root, vid):
    dest = root / "thumbs" / f"hook-{vid}.jpg"
    if dest.exists():
        return True
    clips = root / ".hooks"
    clips.mkdir(exist_ok=True)
    clip = clips / f"{vid}.mp4"
    if not clip.exists():
        subprocess.run(["yt-dlp", "--no-warnings", "-q", "--download-sections", "*0-60",
                        "-f", "bv*[height<=480]+ba/b[height<=480]", "--merge-output-format", "mp4", "-o", str(clip),
                        f"https://www.youtube.com/watch?v={vid}"], capture_output=True, text=True, timeout=300)
    if not clip.exists():
        print(f"clip failed {vid}", file=sys.stderr)
        return False
    frames = clips / vid
    frames.mkdir(exist_ok=True)
    for i, t in enumerate(STAMPS):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", str(clip), "-frames:v", "1",
                        "-vf", "scale=320:320:force_original_aspect_ratio=decrease,pad=320:320:(ow-iw)/2:(oh-ih)/2",
                        str(frames / f"{i:02d}.png")])
    if not list(frames.glob("*.png")):
        return False
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "1", "-pattern_type", "glob",
                    "-i", str(frames / "*.png"), "-vf", "tile=3x3", "-frames:v", "1", "-q:v", "4", str(dest)])
    return dest.exists()


def main():
    root, cfg = load(workdir_arg(__doc__.splitlines()[0]).parse_args().dir)
    (root / "thumbs").mkdir(exist_ok=True)
    ids = pick(root, cfg)
    json.dump(ids, open(root / "hook-picks.json", "w"))
    with ThreadPoolExecutor(3) as ex:
        ok = sum(ex.map(lambda v: sheet(root, v), ids))
    print(f"hook sheets: {ok}/{len(ids)} in {root / 'thumbs'}", file=sys.stderr)


if __name__ == "__main__":
    main()
