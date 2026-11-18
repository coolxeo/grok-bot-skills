"""Shared helpers for the youtube-niche-report scripts: the work folder, its config.json and JSON Lines files."""
import argparse
import json
import sys
from pathlib import Path

DEFAULTS = {
    "niche": "",
    "report_title": "",
    "own_channel": "",
    "seed_channels": [],
    "queries": [],
    "search_depth": 40,
    "max_discovered": 12,
    "discover_min_hits": 2,
    "discover_min_views": 50000,
    "top_per_tab": 50,
    "recent_per_tab": 20,
    "hooks_per_tab": 20,
    "thumbs_per_channel": 20,
    "hook_sheets": 60,
    "hook_sheet_shorts": 20,
    "hook_sheets_per_channel": 6,
    "hook_sheets_own": 12,
    "tab_cap": 1500,
    "workers": 4,
    "caption_langs": ["en"],
    "wave_start": "",
    "established_subs": 5000,
    "film_buckets": [150, 240],
    "keep_rule": "",
    "clusters": {"other": "Other"},
    "structures": ["other"],
    "hook_types": ["visual_only", "other"],
}


def workdir_arg(description):
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--dir", default=".", help="work folder that holds config.json (default: current folder)")
    return p


def load(workdir):
    root = Path(workdir).resolve()
    cfg_path = root / "config.json"
    if not cfg_path.exists():
        raise SystemExit(f"no config.json in {root}; copy config.example.json there and edit it")
    cfg = {**DEFAULTS, **{k: v for k, v in json.load(open(cfg_path, encoding="utf-8")).items() if not k.startswith("_")}}
    if "other" not in cfg["clusters"]:
        cfg["clusters"]["other"] = "Other"
    return root, cfg


def handle_key(h):
    """'@Some.Channel', a channel id or a channel URL (/@x, /channel/UC…, /c/x, /user/x) -> a short key for every file."""
    h = h.strip().rstrip("/")
    if h.startswith("http"):
        from urllib.parse import urlparse
        parts = [p for p in urlparse(h).path.split("/") if p]
        if not parts:
            raise SystemExit(f"can't read a channel from {h}")
        if parts[0] in ("channel", "c", "user") and len(parts) > 1:
            return parts[1] if parts[0] == "channel" else f"{parts[0]}-{parts[1]}"
        return parts[0].lstrip("@")
    return h.lstrip("@").split("/")[0]


def channel_url(h):
    h = h.strip().rstrip("/")
    if h.startswith("http"):
        return h
    if h.startswith("UC") and len(h) == 24:
        return f"https://www.youtube.com/channel/{h}"
    return f"https://www.youtube.com/@{h.lstrip('@')}"


def jl_read(path):
    path = Path(path)
    if not path.exists():
        return []
    rows, bad = [], 0
    for line in open(path, encoding="utf-8"):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:  # a half-written line from an interrupted run
                bad += 1
    if bad:
        print(f"{path.name}: skipped {bad} unreadable lines", file=sys.stderr)
    return rows


def jl_write(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def jl_append(path, rows):
    path = Path(path)
    if path.exists() and path.stat().st_size:  # an interrupted run can leave a half line: cut it off first
        data = path.read_bytes()
        if not data.endswith(b"\n"):
            cut = data.rfind(b"\n") + 1
            with open(path, "r+b") as f:
                f.truncate(cut)
            print(f"{path.name}: dropped an incomplete last line", file=sys.stderr)
    with open(path, "a", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
