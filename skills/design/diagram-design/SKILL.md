---
name: Diagram design
description: >-
  use this when creating explainer diagrams (architecture, sequence, process,
  cards for posts) as HTML/SVG/PNG so they are branded and not ranking-dashboard
  slop
---
# Diagram design

Based on [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) (skills.sh). This skill requires the upstream pack and its reference files. Locate its installed directory in your environment. If it is missing, ask the user to install it before continuing. Read its `SKILL.md` and the matching `references/type-*.md` before drawing. Resolve all reference paths below from that directory.

Use this for explainer diagrams (architecture, sequence, process, layer stack, loop, and the other types in that pack) as standalone HTML/SVG/PNG. Not for a paragraph that already does the job, not for a 3-column table, not for one-shape "diagrams."

## Philosophy

The highest-quality move is deletion. Every node is a distinct idea. Target density 4/10. Above 9 nodes, split into two diagrams. One focal accent, not a traffic light.

## Do not ship these

- Ranking dashboards, two-column scorecards, or three equal summary cards as the default
- Dark mode + cyan/purple glow
- Tiny type
- Shadows; borders instead
- Accent on every "important" node (1–2 max)
- Identical boxes for every node
- Reproducing Mermaid's automatic layout

## Before you draw

1. Ask whether a well-written paragraph would teach more. If yes, don't draw.
2. Name the visual type and load `references/type-<name>.md`.
3. Skin from `references/style-guide.md`. Do not silently ship the default tangerine skin into a branded project. Pull tokens from the live brand or a saved profile first.
4. For a 16:9 social or ad still (1200×675), one idea, large type, no legend soup.

## Output

Self-contained HTML with inline SVG/CSS, then export PNG when the destination is a post or ad. Follow `references/export.md` and `references/output-spec.md`.

License: the upstream diagram pack uses MIT. See [third-party notices](../../../THIRD_PARTY_NOTICES.md) and the [source audit](../../../docs/credits.md).
