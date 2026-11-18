# BotKits design

Visual rules for every image, card, diagram and README in this repo. The palette and fonts come from [botkits.dev](https://botkits.dev) (`site/assets/site.css`). Name and voice rules are in [BRAND.md](BRAND.md).

## Palette

BotKits is white and blue. Blue is the one brand accent.

| Token | Light | Dark |
| --- | --- | --- |
| bg | `#f1f2ee` | `#111418` |
| surface | `#fafaf7` | `#171b20` |
| text | `#14181b` | `#e7e9e3` |
| muted | `#535b61` | `#9ea7ad` |
| rules | `#d2d6ce` | `#2b3138` |
| accent | `#2340c4` | `#a3b4ff` |
| soft accent | `#2340c414` | n/a |
| on-ink | `#f6f7f3` | `#111418` |

**Spark** (optional): `#F2762E` light, `#FF9A5C` dark. At most one small element per image or post, such as a cursor or one highlighted number. Never in the logo mark, never in body text.

**Retired:** lime `#C8FF3D`. Do not use it in new work. Replace it when you touch an old asset.

Badges use `labelColor=14181B` with `color=2340C4` or `F6F7F3`.

## Type

- **Newsreader** (serif) for display: headlines and card titles, weight 400 to 600, letter-spacing about -0.02em.
- **Hanken Grotesk** (sans) for body text, weight 400 to 700.
- **DM Mono** for code, labels, the `botkits.dev` label and the install line, weight 400 or 500.

All three are SIL OFL 1.1. In images, convert text to paths so the file has no font dependency.

## Shape

- Editorial and technical: a big serif headline, a mono command line in a thin ruled box, and a dot grid (24 px grid, 1.1 px dots at about 13%).
- Small corners (2 to 6 px radius). Flat fills and rules. No gradients, no drop shadows, no glow.

## Logo

- **Mark** (`assets/mark-512.png`): a closed box with two eyes on a blue rounded square. Solid fills only, no hairlines, so it reads at 40 px and 20 px. Use it for avatars, favicons and small spots.
- **Wide logo** (`assets/logo-wide.png`, `@2x`): the mark, the "botkits" wordmark in Newsreader and the install line in DM Mono, on the light bg with the dot grid on the right. `assets/header-dark.png` (`@2x`) is the dark version.
- The wordmark is lowercase "botkits" until Dani picks otherwise. Prose still says BotKits (see BRAND.md).
- Do not recolour, stretch, rotate, outline or add effects to the mark or wordmark. Do not put the spark colour in either.
- Source files belong to Designer. Ask Designer for changes; do not redraw the logo in a PR.

## README and card images

| Use | Size | Files |
| --- | --- | --- |
| Repo header | 1280×320 (and 2560×640 @2x) | `logo-wide.png`, `header-dark.png` |
| Mark | 512×512 | `mark-512.png` |
| Terminal demo | 960×520 GIF | `demo.gif` |
| Skill card (Top 3 and per-skill) | 800×460 (and 1600×920 @2x) | `top3-<skill>.png` |

Rules:

- White and blue only, plus at most one spark element.
- Ship light and dark versions where the README uses a `<picture>` switch.
- Every image needs alt text that says what it shows, including any number on it and its source. Not "image" or "screenshot".
- Show the real result of the skill (a frame, a score, a page), not decoration. Numbers on a card need a source and a date.
- Keep PNGs small: export at 1x and 2x, no larger. Do not commit video captures or rendered test output.
- Put shared images in `assets/`. Put images used by one skill in that skill's folder.

## Per-skill README layout

Each skill folder can have a `README.md` for humans. `SKILL.md` stays the instructions for the bot. The section order is set in [BRAND.md](BRAND.md) section 8. Layout rules:

- Put the skill card (800×460, light and dark) right under the one-line promise, with alt text.
- Install line in a code block: `npx skills add botkitsdev/botkits --skill <skill-name>`.
- Before and after as a two-column table, marked as an example.
- "Works with" uses the BRAND.md section 7 wording only.
- The paid kit link sits in a line titled **Paid kits**, only if a kit exists.
- No other images, badges or colours beyond this file.

Copy comes from Marketer. Layout and images follow this file.
