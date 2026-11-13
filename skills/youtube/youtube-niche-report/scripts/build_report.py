"""Step 6: build the report page, one self-contained HTML file, from data.json, insights.json and the thumbnails.

usage:  python3 -I build_report.py --dir <work> [--out report.html]        (run analyze.py first; needs Pillow)

insights.json is what you write after reading the tables (shape in references/insights-schema.md). Everything the page
needs is embedded: data, the idea thumbnails and the hook sheets as base64 JPEG. Third-party thumbnails are embedded
small (320 px) for review; don't republish the page as your own artwork.
"""
import sys
import base64
import io
import json
from pathlib import Path

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))  # works under python3 -I
from common import load, workdir_arg

HERE = Path(__file__).resolve().parent
KEEP = ["id", "title", "channel", "tab", "views", "out", "vpd", "date", "dur", "cluster", "topic", "format", "hook",
        "hook_text", "structure", "title_shape", "voice", "era", "tier", "own", "subs", "heat"]


def b64(path, width):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=72)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def fetch_thumb(vid, dest):
    """Ideas can cite videos outside the top thumbnails pulled per channel; fetch those (best effort)."""
    import urllib.request
    dest.parent.mkdir(exist_ok=True)
    try:
        with urllib.request.urlopen(f"https://i.ytimg.com/vi/{vid}/mqdefault.jpg", timeout=20) as r:
            dest.write_bytes(r.read())
    except Exception as e:
        print(f"no thumbnail for {vid}: {type(e).__name__}", file=sys.stderr)


def main():
    p = workdir_arg(__doc__.splitlines()[0])
    p.add_argument("--out", default="report.html")
    a = p.parse_args()
    root, cfg = load(a.dir)
    data = json.load(open(root / "data.json", encoding="utf-8"))
    ins_path = root / "insights.json"
    ins = json.load(open(ins_path, encoding="utf-8")) if ins_path.exists() else {}
    data["videos"] = [{k: v.get(k) for k in KEEP} for v in data["videos"]]
    data.pop("out_sample", None)
    ins.setdefault("title", cfg["report_title"] or f"What wins in {cfg['niche']}")
    data["ins"] = ins

    data["thumbs"] = {}
    for i in ins.get("ideas", []):
        for vid in i.get("src", []):
            f = root / "thumbs" / f"{vid}.jpg"
            if not f.exists():
                fetch_thumb(vid, f)
            if f.exists() and vid not in data["thumbs"]:
                data["thumbs"][vid] = b64(f, 320)
    data["sheets"] = []
    for s in ins.get("sheets", []):
        f = root / "thumbs" / f"hook-{s['id']}.jpg"
        if f.exists():
            data["sheets"].append({"id": s["id"], "note": s.get("note", ""), "src": b64(f, 520)})

    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")  # no tag can close the data block
    title = ins["title"].replace("<", "&lt;")
    html = (HERE / "template.html").read_text(encoding="utf-8").replace("/*DATA*/", blob).replace("<!--TITLE-->", title)
    out = Path(a.out)
    out = out if out.is_absolute() else root / out
    out.write_text(html, encoding="utf-8")
    print(out, f"{len(html) / 1e6:.2f} MB")


if __name__ == "__main__":
    main()
