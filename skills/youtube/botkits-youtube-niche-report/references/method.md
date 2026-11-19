# Method reference

## Metrics

| Field | Meaning |
| --- | --- |
| `views` | View count at pull time. |
| `out` (× channel) | `views` / median views of the same channel's same tab (videos or Shorts) across its whole catalogue. 1.0× is ordinary for that channel. |
| hit | A video at 3× channel or more. |
| `vpd` | Views per day since upload. Useful for recent videos that haven't peaked. |
| `heat` | YouTube's "most replayed" curve, resampled to 20 buckets (peak per bucket, 0 to 1). Only on videos where YouTube shows it. |
| `era` | `since <date>` when uploaded on or after `wave_start` (default: 90 days before the pull), else `older`. |
| `tier` | `established` at `established_subs` subscribers or more, else `small`. |

Tables report, per group: `n`, median views, median × channel, hits, total
views and the top video. The four scopes on the page:

- **Established, recent**: established channels' uploads in the current era. Plan from this one.
- **Established, all time**: shows durable topics, dominated by old evergreen hits.
- **All screened**: every kept video.
- **Small channels**: what copies and newcomers do. Mostly shows what fails.

The catalogue medians come from yt-dlp's flat listing (rounded view counts),
which is close enough for a ratio. Catalogue size is capped by `tab_cap`.

## Derived fields

- **Format**: Shorts by length (30 s or less, 33 to 60 s, over 60 s); videos
  by `film_buckets` in seconds (default under 2:30, 2:30 to 4:00, over 4:00);
  "Series episode" when the title says Part N, Episode N or #N.
- **Hook**: the model's `hook_type`. Optional `hook_rules` in `config.json`,
  a list of `[name, regex]` pairs, override it when they match the first
  on-screen line, the first spoken line, the model's hook text or the title,
  in that order. Use rules once you know the niche's recurring openings.
- **Title shape**: fixed rules: Series / Part N, ONE-WORD CAPS, Number first,
  Question, First person, Second person / command, Versus, Two-beat
  sentence, How to, Plain statement.

## Files in the work folder

| File | Written by | One row is |
| --- | --- | --- |
| `config.json` | you | settings (see `config.example.json`) |
| `discovery.jsonl` | pull | one search result |
| `channels.json` | pull | one channel: `key`, `url`, `channel_id`, `name`, `why` (seed, own, or discovered with hit count) |
| `catalog.jsonl` | pull | one listed video: `chan`, `tab`, `id`, `title`, `view_count`, `duration` |
| `videos.jsonl` | pull | full metadata of one top video, with `rank`, `heatmap20` |
| `hooks.jsonl` | pull | `id`, `has_subs`, `source`, `first60`: `[{t, text}]` |
| `thumbs/<id>.jpg` | pull | 320 px thumbnail |
| `tags.jsonl` | tag | `id`, `keep`, `why_out`, `topic`, `cluster`, `structure`, `hook_type`, `hook_text`, `voice` |
| `thumbs/hook-<id>.jpg`, `hook-picks.json` | hookframes | 3×3 sheet of the first 45 s; `hook-picks.json` lists each id with the frame times it used |
| `hook-frames.jsonl` | you | see below |
| `data.json` | analyze | everything the page needs |
| `insights.json` | you | see insights-schema.md |
| `report.html` | build_report | the page |

## hook-frames.jsonl

One line per sheet you read. Frames are at 0.5, 2, 4, 7, 10, 15, 22, 30 and
45 s, left to right, top to bottom. A clip shorter than 46 s (most Shorts)
gets its 9 frames spread evenly over its real length instead: take the times
from `stamps` in `hook-picks.json` (the script also prints them). Shorts use
tall 9:16 cells and videos wide 16:9 cells.

```json
{"id": "VIDEO_ID",
 "onscreen": [{"t": 0.5, "text": "Exact words on screen"}, {"t": 4, "text": "Next line"}],
 "first_visual": "What the first frame shows, in one sentence",
 "cut_count_first15": 3,
 "character_on_screen_by_s": 4}
```

Leave out logos and "subscribe" overlays from `onscreen`. Put a description
of what's written in brackets after the words if it matters, for example
`"DUE IN 100 DAYS (on a sticky note)"`. Use `null` when the subject never
appears in the first 45 s.

## What to look for in the tables

1. Which cluster has the highest × channel in the recent established
   scope, and is it carried by one channel? Check the top video column.
2. Which formats and lengths win, and whether Shorts in this niche are
   native or re-cuts of long videos.
3. Which hook types win, and what the winning openings share in the frame
   sheets: text on screen in the first second, when the subject appears,
   how many cuts in the first 15 s.
4. Which structure is the niche default (largest n) and whether it beats
   1.0×. A default that sits at 1.0× is room for a different shape.
5. Which title shapes the leaders use and which ones only the small
   channels use.
6. If the user's channel is in the pull: where its videos sit against the
   small-channel median and the established medians.
