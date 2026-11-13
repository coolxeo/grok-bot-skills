# insights.json

You write this file after reading the tables from `analyze.py`. Every key is
optional; the page leaves out what is missing. Text fields accept `**bold**`
and nothing else.

```json
{
  "title": "What wins in home espresso, and the next five videos",
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
    "paragraphs": ["Only when own_channel is set."]
  },

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
