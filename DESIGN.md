# BotKits design

How to make BotKits visuals. Follow [BRAND.md](BRAND.md) for the name, voice and claims. Colour, type and logo rules are in [Visual tokens and logo](#visual-tokens-and-logo) below. This file covers grid, type scale, image sizes, alt text, file names, and the check you run before shipping.

## Where this applies

README cards, demo GIFs, dividers, badges, headers, and social images. The logo mark is locked; do not redraw it.

## Visual tokens and logo

Moved here from Designer's brand sheet. Colour, type and logo rules live in this section.

### Colour

Brand blue is the default colour. Orange is a spark used at most once, and only sometimes.

| Token | Light | Dark | Use |
|---|---|---|---|
| bg | `#f1f2ee` | `#111418` | Page / artboard |
| surface | `#fafaf7` | `#171b20` | Cards, panels |
| text / ink | `#14181b` | `#e7e9e3` | Body and headlines |
| muted | `#535b61` | `#9ea7ad` | Secondary text |
| rule | `#d2d6ce` | `#2b3138` | Dividers, hairlines |
| blue | `#2340c4` | `#a3b4ff` | Brand colour: titles, frames, links, bars |
| on-ink | `#f6f7f3` | `#111418` | Type or icon sitting on ink |
| spark | `#F2762E` | `#FF9A5C` | One small accent, only sometimes |

Do not use lime `#C8FF3D` or the old ink `#0D0A1F`.

### Type

- Newsreader (display) for headlines and the BotKits wordmark.
- Hanken Grotesk for body.
- DM Mono for code, the install line, skill slugs, and terminal demos.
- All are SIL OFL. Outline type to paths in shipped SVGs; ship no `<text>` and no font dependency.

### Logo

Files live in `assets/`:

- `mark-512.png`: square mark on `#2340c4`. Also ship `mark.svg` and `mark-1024.png` when you can.
- `logo-wide.png` / `logo-wide@2x.png`: 1280×320 light header (wordmark + install line). This is the light root header in README.md.
- `header-dark.png` / `header-dark@2x.png`: 1280×320 dark header. This is the dark root header in README.md.

There is no `header-light.png`. The light header is `logo-wide.png`.

The mark is a closed isometric kit with pill eyes, on the blue tile. Do not recolour it, add a spark, or change its geometry.

Clear space: keep a margin around the mark of at least the lid lip (~10% of the tile). The 40 px GitHub avatar must still read as a box with two eyes, with the blue circle edge visible on `#ffffff` and `#0d1117`. Do not use the mark below 40 px.

## Grid and spacing

- Design on an 8 px grid.
- README headers are 1280×320. Mark is 192 px, 72 px from the left, 56 px from the wordmark. Keep 60 px between the end of the word and the dot grid.
- Top-3 cards are 800×460. 9 px brand-blue bar at the top. Title starts at x=38, cap height near y=35. Content inset 76 px on article-style cards; diagrams sit in the middle band (about y=130 to 310).
- Terminal demos are 960×520. 9 px blue bar, 17 px window dot at (36, 28), a rule under the title, code inset 50 px. Body text after a `you`/`bot` label starts at x=122.
- Give the mark clear space of at least 10% of the tile. Do not crop into the lid lip.

## Type scale

Minimums are for 1×. Never ship text smaller than this.

| Role | Face | Size | Tracking | Min |
|---|---|---|---|---|
| Wordmark | Newsreader | 168 px on the 1280 header | −0.025 em | 80 px |
| Card title (skill slug) | Newsreader | 40 px | −0.02 em | 24 px |
| Article title | Hanken Grotesk 700 | 30 px | −0.02 em | 18 px |
| Body / hook | Hanken Grotesk | 18 to 20 px | 0 | 14 px |
| Caption / label | Hanken Grotesk or DM Mono | 16 px | 0 | 13 px |
| Code, install line, diagrams | DM Mono | 13 to 26 px | 0 | 12 px |
| Hero number | Newsreader | ~88 px | −0.03 em | 40 px |

Outline all type to paths in SVGs. No `<text>` in shipped SVGs.

## Light and dark

- Use one token set per image. Light: bg `#f1f2ee`, surface `#fafaf7`, text `#14181b`, muted `#535b61`, rule `#d2d6ce`, blue `#2340c4`. Dark: bg `#111418`, surface `#171b20`, text `#e7e9e3`, muted `#9ea7ad`, rule `#2b3138`, blue `#a3b4ff`.
- For drop-in README cards that replace the current files, use the **light** set so the blue is `#2340c4`. Also ship `-light` and `-dark` (and `@2x`) pairs.
- A dark terminal demo stays dark: bg `#111418`, type `#e7e9e3`, typed code `#a3b4ff`, filled chrome `#2340c4`.

## Spark (orange)

- Light `#F2762E`, dark `#FF9A5C`.
- At most one small element per image (cursor, one arrow, one short label, one key number).
- Never in the logo, headers, or body text.
- Keep spark under about 5% of the pixels. If it is not clearly one highlight, drop it.

## Image sizes

| Asset | 1× | 2× |
|---|---|---|
| `logo-wide.png`, `header-dark.png` | 1280×320 | 2560×640 |
| `mark-512.png` | 512×512 | none (`mark-1024.png` is 1024×1024) |
| GitHub avatar | 40×40 circle | none |
| Top-3 cards | 800×460 | 1600×920 |
| `demo.gif` | 960×520 | none |

Match these sizes when you replace a repo file.

## Alt text

Write a short, factual description of what the image shows. Name the skill and any number that is in the picture. Do not start with "image of". Example: `aeo-geo-site: botkits.dev is-agentic score, 79 to 81 to 100, is-agentic.com, 17 Nov 2026`.

## File names

- Logo: `mark-512.png`, `mark-1024.png`, `mark.svg`, `logo-wide.png`, `logo-wide@2x.png`, `header-dark.png`, `header-dark@2x.png`, plus `@2x` and `.svg` where they exist.
- Cards: `top3-{skill}-light.png`, `top3-{skill}-dark.png`, and `@2x`. Drop-in repo copies use the unsuffixed names (`top3-shorts-reframe.png`, `top3-x-article.png`, `top3-aeo-geo-site.png`) and are the light artwork.
- Demo: `demo.gif`.
- Put drop-in files in `assets/` with those exact repo names so the README needs no edits.

## Before you ship an image

1. The prose name and the wordmark are BotKits; the slug is botkitsdev/botkits. No "botskills".
2. Tokens are a single light or dark set from [Visual tokens and logo](#visual-tokens-and-logo). No lime `#C8FF3D`. No mixed palettes.
3. Logo and headers are blue and white only. Pixel-check that they contain no spark and no lime.
4. If the image uses a spark, there is only one, it is small (under ~5% of pixels), and it is not body text.
5. Type meets the minimum sizes. SVG type is outlined; no `<text>`.
6. The file name and pixel size match the table above.
7. Alt text is written and describes the content, including any number on the card.
8. Open the render at 1× and at the 40 px mark (for logos). Check spelling, contrast, and that a dark or light GitHub page is not assumed unless you shipped both.

## README section order

DESIGN.md has no README template. For the section order of a skill README, follow [BRAND.md](BRAND.md) section 8.
