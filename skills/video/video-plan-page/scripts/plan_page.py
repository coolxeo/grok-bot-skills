#!/usr/bin/env python3
"""Turn a video script into one explorable HTML plan page, before any shot is made.

    python3 plan_page.py example/script.json --plan example/plan.json --out plan.html

The page holds a playable animatic (captions on time, HUD, key frames where they exist, a
"to paint" card where they don't), a scrubbable timeline, the goal and checks, hook versions,
the shot list, title and thumbnail options, the order of work, and the open choices with a
reply the viewer can copy.

script.json
    title, series, episode, of, moral, notes, titles [str], thumbs [{id, words, brief, note}],
    checks [{name, ok, info}], quest {goal, stakes, enemy, hud, opening, cast [str],
    hooks [{text, checks: "MHSNB" letters passed, pick}]}, lines [{who, text, level, beat,
    loop, see, hud, knows [name], t, dur, min}].
    `text` may hold one "|" to split a caption into two rows. A line with `see` is a shot.
    Lines without `t`/`dur` are timed from their word count (2.6 words a second, at least
    2.4 s, `min` raises the floor).

plan.json (every field optional)
    page_title, eyebrow, lede, chips [str], levels {n: name}, hud_label, speakers {who: label},
    colours {name: css colour} for the `knows` dots, enemy_colour, keys {"S03" or "12.5": image},
    thumb_images {thumb id: image}, shots_note, steps [{title, detail, time}],
    gantt [{name, start, end, kind: "cpu"|"you"}] in hours, gantt_span, gantt_note,
    cards [{tab, tab_label, title, rows [[k, v]]}], decisions [{question, options
    [{label, detail, reply, rec}]}], approve_what.

Images are relative to the plan file, shrunk to 960 px JPEG (with Pillow) and embedded, so the
page is a single file. A missing image prints a warning and the shot stays "to paint".
Web fonts load from Google Fonts when online; --no-webfonts drops that request and the page
uses system fonts.
"""
import argparse
import base64
import html as htmllib
import io
import json
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent / "template.html"
WORDS_PER_S = 2.6
MIN_LINE_S = 2.4
MAX_PAGE_BYTES = 15 * 1024 * 1024


def warn(msg):
    print(f"plan_page: warning: {msg}", file=sys.stderr)


def timed(lines):
    """Return copies of the lines with `t` and `dur`; given values win, the rest are estimated."""
    out, t = [], 0.0
    for line in lines:
        words = len(str(line.get("text", "")).replace("|", " ").split())
        dur = line.get("dur")
        if dur is None:
            dur = max(line.get("min", 0), MIN_LINE_S, words / WORDS_PER_S)
        start = line.get("t", t)
        out.append({**line, "t": round(start, 2), "dur": round(dur, 2)})
        t = start + dur
    return out


def image_uri(path, width=960):
    """Return the image as a data URI, or None (with a warning) when the file is missing."""
    p = Path(path).expanduser()
    if not p.is_file():
        warn(f"image not found, left as 'to paint': {p}")
        return None
    try:
        from PIL import Image
    except ImportError:
        data = p.read_bytes()
        mime = "image/png" if p.suffix.lower() == ".png" else "image/jpeg"
    else:
        im = Image.open(p).convert("RGB")
        im.thumbnail((width, width * 2))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=72)
        data, mime = buf.getvalue(), "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(data).decode()


def attach_keys(lines, keys, base):
    """Attach key images to shots, by shot id (S01 = first line with `see`) or by start time."""
    by_shot, by_time = {}, {}
    for k, v in (keys or {}).items():
        if k.upper().startswith("S"):
            by_shot[k.upper()] = v
        else:
            try:
                by_time[round(float(k), 1)] = v
            except ValueError:
                warn(f"key '{k}' is neither a shot id nor a time; skipped")
    out, n = [], 0
    for line in lines:
        new = dict(line)
        if line.get("see"):
            n += 1
            src = by_shot.get(f"S{n:02d}") or by_time.get(round(line["t"], 1))
            uri = image_uri(base / src) if src else None
            if uri:
                new["key"] = uri
        out.append(new)
    return out


def build(script, plan, plan_dir, webfonts=True):
    if not script.get("lines"):
        raise ValueError("script has no lines")
    lines = attach_keys(timed(script["lines"]), plan.get("keys"), plan_dir)
    last = lines[-1]
    thumbs = []
    for th in script.get("thumbs", []):
        src = (plan.get("thumb_images") or {}).get(th.get("id"))
        uri = image_uri(plan_dir / src) if src else None
        thumbs.append({**th, **({"image": uri} if uri else {})})
    data = {
        "title": script.get("title", "Untitled"), "series": script.get("series"),
        "episode": script.get("episode"), "of": script.get("of"), "quest": script.get("quest", {}),
        "moral": script.get("moral"), "notes": script.get("notes"), "titles": script.get("titles", []),
        "thumbs": thumbs, "checks": script.get("checks", []), "lines": lines,
        "total": round(last["t"] + last["dur"], 1), "colours": plan.get("colours", {}),
        "enemy_colour": plan.get("enemy_colour"), "speakers": plan.get("speakers", {}),
        "plan": {k: v for k, v in plan.items()
                 if k not in ("keys", "thumb_images", "colours", "speakers", "enemy_colour")},
    }
    page = TEMPLATE.read_text(encoding="utf-8")
    if not webfonts:
        head, _, rest = page.partition("<!--WEBFONTS-->")
        page = head + rest.partition("<!--/WEBFONTS-->")[2]
    title = htmllib.escape(plan.get("page_title") or data["title"])
    # Escape every "<" so script text can never close the <script> tag or open a comment.
    payload = json.dumps(data).replace("<", "\\u003c")
    return page.replace("/*TITLE*/", title, 1).replace("/*DATA*/null", payload, 1)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Build an explorable video plan page.")
    ap.add_argument("script", type=Path)
    ap.add_argument("--plan", type=Path)
    ap.add_argument("--out", type=Path, default=Path("plan.html"))
    ap.add_argument("--no-webfonts", action="store_true", help="system fonts only, no outside request")
    a = ap.parse_args(argv)
    try:
        script = json.loads(a.script.read_text(encoding="utf-8"))
        plan = json.loads(a.plan.read_text(encoding="utf-8")) if a.plan else {}
        page = build(script, plan, (a.plan or a.script).parent, webfonts=not a.no_webfonts)
    except (OSError, ValueError, KeyError) as e:
        print(f"plan_page: {e}", file=sys.stderr)
        return 1
    size = len(page.encode("utf-8"))
    if size > MAX_PAGE_BYTES:
        print(f"plan_page: page is {size // 1024} KB, over the 15 MB limit; use fewer or smaller keys",
              file=sys.stderr)
        return 1
    a.out.write_text(page, encoding="utf-8")
    print(f"wrote {a.out} ({size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
