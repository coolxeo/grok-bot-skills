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
    "hooks_per_tab": 20,
    "thumbs_per_channel": 20,
    "hook_sheets": 60,
    "hook_sheet_shorts": 20,
    "hook_sheets_per_channel": 6,
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
    cfg = {**DEFAULTS, **{k: v for k, v in json.load(open(cfg_path)).items() if not k.startswith("_")}}
    if "other" not in cfg["clusters"]:
        cfg["clusters"]["other"] = "Other"
    return root, cfg


def handle_key(h):
    """'@Some.Channel' or a channel URL -> a short key used in every file."""
    h = h.strip().rstrip("/")
    if "/channel/" in h:
        return h.split("/channel/")[-1]
    if "/@" in h:
        h = h.split("/@")[-1]
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
    for line in open(path):
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:  # a half-written line from an interrupted run
                bad += 1
    if bad:
        print(f"{path.name}: skipped {bad} unreadable lines", file=sys.stderr)
    return rows


def jl_write(path, rows):
    with open(path, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def jl_append(path, rows):
    with open(path, "a") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
