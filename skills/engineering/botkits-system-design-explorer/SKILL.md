---
name: botkits-system-design-explorer
description: >-
  Use this when you must explain a system design to a review panel, an
  interview or a team. It builds one self-contained HTML page with decision
  cards, an animated architecture diagram, stepped walkthroughs and a
  drill-down sheet for every box. It works as a keyboard talk and as a page people read
  alone. For one static diagram, use botkits-diagram-design.
compatibility: Writes one static HTML file. Uses a headless browser (Playwright) for the screenshot check when one is available.
---

# System design explorer

One HTML page that explains a system the way an architect does at a whiteboard. The rule the design hangs on comes first, then the decisions, then the moving picture, then one walkthrough per hard part. Every box, number and decision opens a sheet with the long explanation. The presenter walks it with the keyboard, one section per key press. A reviewer can read it alone afterwards.

The examples below use a made-up concert ticket on-sale system, where two million fans compete for 50,000 seats and no seat may be sold twice.

## When to use

- A design review, a system design interview, an architecture committee, or a hand-over to a new team.
- The talk has a time budget and named sections to cover.
- People will ask "why not X?" and you want the answer one click away.

Skip it for a single diagram in a post or a PR. Use [botkits-diagram-design](../../design/botkits-diagram-design/SKILL.md) for that.

## 1. Before you build

1. **Get the brief and the time budget.** Write down the sections the presenter must cover and the minutes for each. If the brief asks the presenter to pick one option per section, ask them to pick. Recommend one and start on it while you wait.
2. **Lock the decisions with the person before you draw.** Ask a few questions per round (eventing, storage, cache, compute, regions, payments, whatever the system needs). Give the facts they need to answer. Record each answer as **one line plus why** in a study notes file. Those notes are speaker notes. They never go on the page as paragraphs.
3. **Find the one rule.** One sentence that explains most decisions, for example "the waiting room takes the crowd; only admitted users touch the database." Put it at the top. If a decision card cannot be explained through it, either the card or the rule is wrong.
4. **Write the capacity math once.** Users, then per day, then per second, then peak. Reuse the exact same numbers on the page, in the deck and in the notes. Mark every invented figure as an assumption on the page.
5. **Get the brand.** Colours, fonts and spacing from the person's site or design file. Ask once if neither exists. Otherwise use neutral tokens, with a quiet ground, white sheets and one accent.

## 2. Page structure

Each part is a full-height `section.block`. Keep this order unless the brief forces another:

1. **Masthead and agenda.** A title that says what the system does and under which constraint. The one rule in a card. The talk's parts with minutes for each (minutes are helper text, see section 6).
2. **Demo.** An animated run of system events: fake records travel as pills and dots through the real components, chapter by chapter. See "Event demo".
3. **Decisions.** Cards grouped into lanes by stage of the flow (for example Enter, Hold, Pay, Run). See "Decision cards".
4. **Architecture diagram.** Animated, with named flows the viewer can switch between. Click a node to open its sheet.
5. **Layers.** An isometric stack of at most five layers with a property table beside it. It follows one item from arrival to storage to the read side. See "Layer stack".
6. **Numbers.** The capacity math as clickable figures, each with its worked sum.
7. **Walks.** One stepped walkthrough per hard part. The ticket system gets a correctness walk (how a seat is never sold twice) and a cost walk.
8. **Terms.** Every short form on the page, spelled out.

A **Talk** section with a keyboard slide deck can sit above the masthead when the page is also the slides (see "Embedding a deck").

## 3. Copy rules

- **Titles say what the section shows and the decision behind it.** "Holding a seat so two fans can never buy it", not "Seat holds". No one-word section titles.
- **Few short forms.** Spell each one out the first time, add a hover `title` (or `abbr`), and list it in Terms. Drop a short form when the plain words are short enough.
- **Decisions are one line plus why.** "Kafka-compatible log: tickets, email and the warehouse each read at their own pace." Add the switch trigger: the condition that would make you change the decision.
- **Cues on screen, explanation in the presenter's mouth.** Walk steps show two to four short cue chips. A faded one or two sentence description sits under the selected step only.
- **Helper text is hidden by default** behind a notes toggle next to the theme switch (section 6). Hide lead lines, minute labels, legend notes and step descriptions. Keep titles, picks, numbers, colours and cue chips.
- **Remove labels that carry no information.** If every card says "1 of 3", drop it.
- **Name nodes by what they are.** "Postgres, seats and orders", not "Storage". Label edges with verbs: "hold", "refresh 1 s", "release expired".
- **Label fakes.** Made-up records, numbers and generated images say so on the page.
- **No AI filler.** Run every title and caption through [botkits-no-ai-slop](../../writing/botkits-no-ai-slop/SKILL.md). Read each line aloud. If you would not say it to the panel, rewrite it.

## 4. Visual and motion rules

- **Light and dark for everything.** Tokens on `:root`. Dark values under `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {...} }` and again under `:root[data-theme="dark"]`. A theme button cycles system, light, dark and remembers the choice (`localStorage` inside try/catch).
- **Quiet ground, light sheets, soft lifts.** Three or four shadow tokens for lift. One accent for "chosen, in flow". One signal colour for "edge case, cost, warning".
- **One channel per meaning.** If colour means category, it cannot also mean risk. The reversibility ring is neutral grey; its letter (L, M, H) and arc length carry the meaning.
- **Motion tokens, no overshoot:** `--ease-out: cubic-bezier(.16,1,.3,1)` for arrivals, `--ease-in: cubic-bezier(.7,0,.84,0)` for exits, `--ease-in-out: cubic-bezier(.65,0,.35,1)` for toggles. Durations 120, 220 and 420 ms.
- A pill slides under the active nav item and tab. A marker follows the current walk step. Cue chips arrive about 70 ms apart. Big numbers count to their new value. All of it turns off under `prefers-reduced-motion`.
- **Diagram edges** are dotted paths with a moving dash offset, an arrowhead, and a packet that travels along the lit flow. The diagram must show real control flow. If a queue triggers a worker, draw source, then queue, then worker, not two arrows into the worker.
- **Icons:** one set, inlined as SVG paths (Lucide, ISC licence, is a good fit; credit it on the page). One icon per decision card, in a small tile.
- **Phone check at 390 px:** the page never scrolls sideways. A wide diagram, table or tab strip may scroll inside its own container.

## 5. Components

### Decision cards

- Lanes look like board columns: a plain heading with a count ("Hold 3") and the cards on a shaded lane.
- A card shows an icon tile, the decision title, the pick, a category dot, one key number and a reversibility ring (L, M, H). No hover effects inside cards.
- Click opens the sheet: all options (the pick first, marked chosen, each with a one-line why), the switch trigger, and a button to the node in the diagram.
- A ledger bar above the lanes shows every decision as one segment, **grouped by category colour**, with filter chips in the same order.
- Data model per decision: `[id, lane, title, icon, pick, pickWhy, category, number, reversibility 1-3, switchIf, nodeId, [[option, why] x3]]`. The first option is always the pick. Assert it in code.

### Drill-down sheet ("Learn it")

Every node, number and decision opens the same side sheet. It has a **Say it** line (the sentence the presenter says), likely questions, and a **Learn it** block with five fixed headings: **What it is**, **How it works**, **Why this choice**, **The numbers** (worked, for example 2,000,000 ÷ 600 s ≈ 3,300 a second), **What can go wrong**. Keep all of it in one `LEARN = { id: { say, what, how, why, nums, risk, q } }` object. Write the same text to a speaker notes markdown file in talk order, so the page and the notes never drift. The sheet is deep-linkable (`#x-<kind>-<id>`), closes with Escape, and returns focus.

### Walks

A walk is a stage plus an ordered list of steps. Each step has a title, two to four cue chips, a faded description and a link to one node. The stage gets the classes `at-N` and `ge-0` to `ge-N`, and elements tagged `data-act="2 3"` light up on those steps, so CSS does the animation. "Play the steps" auto-advances. Clicking a step or the stage moves one step.

**Charts in walks stay simple.** A cost walk is one fixed bar that adds up to 100%. Each step highlights one line item, biggest first, and shows its share. No regrouping, no bars that change size. Assert the sum in code.

### Diagram playback

- Default speed **0.5x**, with a 0.5x / 1x toggle. Fast animation is hard to narrate.
- Flow tabs light one path at a time ("Join the queue", "Hold a seat", "Pay", "Everything"). Nodes off the path fade.

### Event demo (animated system events)

The demo shows what the system does when real traffic arrives.

- Four or five chapters of about 7 seconds, one per stage of the flow, with a chapter list and a progress bar per chapter.
- One clock drives everything. Every position, counter and node state is computed from time `t`, so scrubbing, seeking and reduced motion work and nothing gets stuck between two states.
- Records (an order, a request) are labelled pills that move between nodes. Messages on a log or queue are dots that travel along the real diagram edge. A fan out sends one dot per consumer at the same moment.
- Nodes react: they pulse when an event lands, show a count, and change state (held, paid, released).
- Lay the stage out on a fixed canvas and scale it to the container, so coordinates never change per screen size.
- Default speed 0.5x. **Play step** plays one chapter and stops on its last frame. **Play all** runs to the end.
- Show at least one edge case being handled on screen: a duplicate merged, a hold expiring, a retry.
- Label it: "Made-up orders, timings slowed down."

### Layer stack (isometric layers plus table)

A tilted stack of at most five plates that follows one item from arrival (bottom plate) to where people read it (top plate). Each plate names the real components on it, and a table beside the stack gives one row per layer: what happens to the item there and where it is stored. Selecting a plate highlights its row and the other way round. On a phone the stack flattens to a column. If a layer does not hold or move the item, cut it.

### Keyboard model

- ↓ / ↑, Page Down / Page Up and Space glide exactly one section with an eased scroll (cubic in-out, 420 to 900 ms). A section taller than the screen pages through itself (85% of the viewport per press) before moving on.
- ← / → go to whichever stepped thing is on screen: a walk, the demo, the embedded deck. Keep a registry `window.walks = [{ sec, next, prev }]`. The arrow handler picks the entry whose section crosses the middle of the screen.
- Ignore keys with modifiers, inside inputs, and while the sheet is open. Never take Space from a focused button.

### Embedding a deck

Put the slide deck in a shadow root inside a Talk section, so its CSS cannot leak, scale its 16:9 stage to the container, and register it with the arrow keys. Regenerate the embed from the deck source. Do not hand-edit the copy.

## 6. Notes toggle

```css
:root:not(.notes) :is(.sec-lead, .hint, .sdesc, .ag-time, .legend-note) { display: none !important; }
```

```js
function applyNotes(on) {
  document.documentElement.classList.toggle("notes", on);
  const b = document.getElementById("notesBtn");   // keep the button in sync, also when restored from storage
  b.innerHTML = icon(on ? "captions" : "captions-off");
  b.setAttribute("aria-pressed", on);
  b.title = on ? "Hide notes" : "Show notes"; b.setAttribute("aria-label", b.title);
}
try { applyNotes(localStorage.getItem("notes") === "on"); } catch (e) { applyNotes(false); }
```

## 7. Review loop (every round)

1. Screenshot light, dark and a 390 px phone with a headless browser. The console has no errors, and `document.documentElement.scrollWidth <= innerWidth`.
2. Press ↓ through the whole page and → through every walk. Nothing is skipped.
3. Every decided component appears in the overview diagram. A cache or queue that is in the decisions but missing from the diagram is the most common miss.
4. Search for every number across the page, the deck, the study notes and the speaker notes. They must agree. Rates, latency budgets and retention days drift first.
5. Read every title and caption aloud against the copy rules.
6. Publish to the same URL as last time, so links people already have keep working.

## 8. Pitfalls

- **Too much interaction.** Hover effects inside cards that rewrite their text. Keep cards still; the sheet holds the detail.
- **Two people editing the page.** Always start from the latest published version, never an older local copy.
- **Secrets.** A key pasted in chat never lands in a file, a commit or a script. Read keys from an environment variable and tell the person to rotate a pasted key.
- **Data flow drawn as control flow.** Edges that show where data ends up, not what calls what. Node labels that name a stage instead of a system.
- **Animation too fast to narrate.** Hence 0.5x by default and step-by-step playback.
- **Numbers that change between sections.** One source object for figures, rendered everywhere.

## Checklist

- [ ] The one rule is at the top, and each decision card can be explained through it
- [ ] Every decision has a pick, two rejected options with a why, and a switch trigger
- [ ] Every component in the decisions appears in the diagram
- [ ] Every node, number and decision opens a sheet with the five Learn it headings
- [ ] Numbers match across page, deck and notes; invented ones are marked
- [ ] Light, dark and 390 px screenshots checked; no console errors; no sideways scroll
- [ ] ↓ and → walk the whole talk; reduced motion turns animation off
- [ ] The demo has 4 or 5 chapters, one clock, and at least one edge case handled on screen
- [ ] The layer stack has at most 5 plates, bottom plate first, a matching table and a flat phone view
- [ ] Copy passed botkits-no-ai-slop

## Inspired by

- Dani Acosta's own system design explorer (private). The rules were tied to one page and its data, with no example anyone else could open.
- [Ben Shneiderman, "The Eyes Have It" (1996)](https://doi.org/10.1109/VL.1996.545307). Does well: names the order "overview first, zoom and filter, then details on demand". Missing: written for data browsers, with no advice on presenting a design live.
- [C4 model, Notation](https://c4model.com/diagrams/notation). Does well: every element and relationship is labelled, so a diagram stands alone. Missing: static diagrams only, no walkthroughs or decisions.

## What this version adds

- One data object per kind of fact (decisions, nodes, numbers, steps, bill), with asserts for "pick comes first" and "bill adds up to 100".
- Decision cards with a switch trigger and a reversibility ring, grouped by category in one ledger.
- The five-heading Learn it sheet for every box, shared with the speaker notes.
- A keyboard model that serves both the talk and the solo reader.
- A review loop that catches drifting numbers and components missing from the diagram.
