---
name: diagram-design
description: >-
  use this when creating explainer diagrams (architecture, sequence, process,
  cards for posts) as HTML/SVG/PNG so they are branded and not ranking-dashboard
  slop
---
# Diagram design

Make one diagram that teaches one thing: architecture, a sequence, a process, a loop, a layer stack, or a still card for a post. Output is a self-contained HTML file with inline SVG, exported to PNG when it's going on social or into an ad. Works on its own; if Cathryn Lavery's diagram pack is installed, use its type references for layout detail.

## Should this be a diagram?

Draw only when space carries meaning: order, flow, containment, or connection. If a short paragraph or a small table says it as well, write that instead. Never draw a one-box "diagram".

## Plan before drawing

1. Write the caption first: one sentence the diagram proves. If you can't, you don't know what to draw yet.
2. Pick the type that matches the relationship: flow (process, pipeline), time (sequence, timeline), structure (layers, nesting, tree), or cycle (loop). One level of detail per diagram; zoom levels go in separate diagrams.
3. List the nodes. Merge any two that always appear together. Past about nine nodes or twelve arrows, split into an overview and a detail.
4. Get the brand: colors, fonts, and spacing from the live site or the user's saved profile. Ask once if neither exists. Never ship a default palette into a branded project.

## Drawing rules

- Every box gets a short label and, if needed, a few words on what it does. Every arrow has a direction; label it when the relationship isn't obvious.
- One accent color for the one or two nodes the caption is about. Everything else stays neutral.
- Borders, not shadows. Flat fills. Text large enough to read on a phone at post size.
- Align to a grid. Even spacing. Lines don't cross unless they must.
- A title that says what and what scope. A legend only when shapes or colors carry meaning, as a single strip at the bottom.
- Remove anything that adds ink but no information: background textures, 3D, icons that repeat the label, gradients.

## Never ship

- Ranking dashboards, two-column scorecards, or three equal summary cards as the default answer.
- Dark background with neon cyan or purple glow.
- An accent on every "important" node.
- Identical boxes for things that are different kinds (a person, a service, a database).
- Mermaid's auto-layout pasted as a final design. Mermaid is fine for drafts and inside PRs.

## Social and ad stills

1200×675 (16:9) unless the platform asks for something else. One idea, big type, no legend. Run the caption through no-ai-slop.

## Output

- A single HTML file with inline SVG and CSS, no external requests.
- SVG has a `<title>` and `<desc>` for screen readers.
- PNG export at 2x for posts and ads. Open the PNG and look at it before handing it over.

## Inspired by

- [Cathryn Lavery, diagram-design](https://github.com/cathrynlavery/diagram-design) (MIT). Does well: "deletion is the best move", one or two focal accents, a per-type complexity budget, and a style-guide gate before drawing. Missing: about 580 lines plus a required reference pack, so the skill cannot run without installing it first.
- [C4 model, Notation](https://c4model.com/diagrams/notation) (CC BY 4.0). Does well: every diagram gets a title with type and scope, a key, and labeled elements and relationships, so it stands alone. Missing: covers software architecture only and leaves visual style open.
- [Edward Tufte's chartjunk idea, via Wikipedia](https://en.wikipedia.org/wiki/Chartjunk). Does well: names decoration that adds ink without information. Missing: written about data graphics, with no steps for building a schematic.

## What this version adds

- Standalone: works without the upstream pack, and uses it when present.
- Caption-first planning and a "should this be a diagram?" test.
- Dani's never-ship list, social still sizes, and accessible SVG plus a look-at-the-PNG check.
