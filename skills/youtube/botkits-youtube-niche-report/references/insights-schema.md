# insights.json

You write this file after reading the tables from `analyze.py`. Every key is
optional; the page leaves out what is missing. Text fields accept `**bold**`
and nothing else.

The values below are a made-up example (the home espresso niche from
`config.example.json`), not real results. Replace them with your own.

```json
{
  "title": "What wins in home espresso, and the next five videos",
  "page_title": "Espresso Niche Report",
  "eyebrow": "Niche report · pulled 2026-11-13",
  "lede": "Two sentences that answer the user's question.",

  "answer": {
    "heading": "The next five videos",
    "intro": "Ordered by strength of evidence.",
    "rules": ["One rule per line that every video in the batch follows."],
    "batch": [
      {"slot": 1, "idea": 3, "title": "Lead title", "why": "The evidence, with numbers.",
       "hook": "The opening line.", "short": "How the Short version opens.",
       "logline": "One sentence on what happens.", "tags": ["milk_art", "before_after"]}
    ]
  },

  "own": {
    "heading": "Your Shorts beat the small channels. Your long videos don't.",
    "paragraphs": ["Only when own_channel is set."],
    "sheets": [{"id": "YOUR_VIDEO_ID", "note": "What your opening does."}]
  },

  "channels": {"heading": "Who is in the niche", "paragraphs": [], "bullets": []},
  "compare": {"heading": "Whose old videos still earn", "paragraphs": [], "bullets": []},

  "sections": [
    {"id": "verdict", "place": "first", "nav": "The verdict", "eyebrow": "What is happening",
     "heading": "One sentence", "paragraphs": ["..."],
     "kpis": [{"value": "7 weeks", "label": "what the number is"}],
     "bullets": ["..."],
     "cards": [{"title": "The data shows", "paragraphs": [], "bullets": ["..."]}],
     "table": {"head": ["Measure", "You", "Leaders"], "right": [1, 2], "rows": [["Length", "46 s", "15 s"]]},
     "note": "A small-print line.", "sheets": [{"id": "VIDEO_ID", "note": "..."}], "after": ["..."]}
  ],

  "findings": {
    "cluster": ["**Milk art leads**: median 120K, 2.4× channel among established recent uploads (n=14)."],
    "format": [], "hook": [], "structure": [], "title_shape": [], "voice": []
  },

  "hookdefs": [
    {"k": "result_first", "what": "The finished drink in the first second, then the steps.",
     "ex": ["Example opening line that worked"]}
  ],

  "sheets": [{"id": "VIDEO_ID", "note": "What this opening does in one sentence."}],

  "ideas_heading": "Twenty ideas, torn down and converted",
  "ideas_intro": "How to read each card.",
  "ideas": [
    {"n": 1, "src": ["VIDEO_ID", "VIDEO_ID_2"],
     "lesson": "Why the source video worked, in one paragraph.",
     "adaptation": "The user's own version, in one paragraph.",
     "titles": ["Lead title", "Option 2", "Option 3"],
     "thumbs": ["Thumbnail concept A", "Thumbnail concept B"],
     "hook": "The opening line.",
     "tags": ["optional", "labels"]}
  ],

  "screen_note": "The keep rule, in one paragraph, and what was dropped most.",
  "caveats": ["Each caveat as one sentence."]
}
```

`src` ids must be screened-in videos (they appear in `data.json` videos);
the first one supplies the idea's thumbnail and teardown fields. `sheets`
ids must have a `thumbs/hook-<id>.jpg`. Keys of `findings` match the table
names. `hookdefs[].k` should match the hook names in the tables.

`page_title` is the short name for the browser tab (two to four words);
without it the tab shows `title`. `sections` are free blocks you write
yourself: every part is optional and they render in the order paragraphs,
kpis, bullets, cards, table, note, sheets, after. `place` is `first` (above
the answer), `top` (after the answer, the default) or `end` (after the
ideas). `channels` and `compare` add text to the channels table and to the
then-and-now table (`analyze.py --prev`).
