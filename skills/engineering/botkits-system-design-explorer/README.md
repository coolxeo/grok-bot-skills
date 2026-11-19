# botkits-system-design-explorer

Explain a system design on one page you can present with the keyboard and hand over as a link.

For engineers who present a design to a review panel, an interview or a new team.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-system-design-explorer
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Takes a brief, a time budget and your decisions (one line plus why each), and asks about the decisions you have not made yet.
- Builds one self-contained HTML page: the one rule the design hangs on, decision cards with a switch trigger, an animated architecture diagram with named flows, the capacity math, stepped walkthroughs, and a glossary.
- Adds an animated event demo (records and messages move through the real components, chapter by chapter) and an isometric layer stack with a table beside it.
- Every box, number and decision opens a side sheet with a "Say it" line and five fixed headings: what it is, how it works, why this choice, the numbers, what can go wrong.
- Works as a talk (↓ moves one section, → moves one step) and as a page people read alone. Light and dark, phone width, reduced motion.
- Ends with a review loop: screenshots in both themes and at 390 px, every number checked across page and notes, every decided component present in the diagram.
- It does not decide your architecture for you. It asks, records your answer, and draws it.

## Before / after (example)

The skill's examples use a made-up concert ticket on-sale that sells 50,000 seats in a few minutes without selling one twice. The product, the numbers and the costs are invented.

Before, the design lived in a doc with eight decisions buried in paragraphs, one static box diagram, and capacity numbers that differ between the doc and the slides.

After, it is one page. It opens with the system running. Fans join the queue, two holds race for one seat, and the second one loses on screen. The decisions sit in lanes, each with its pick, a key number and how hard it is to reverse. The diagram lights one flow at a time at 0.5x. A layer stack follows one order from the queue to the read side. Each hard part gets a walk you step through with →, and cost is one bar that adds up to 100%, one line item per step. Every box opens a sheet with the line to say and the long answer.

## Use it in

- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-system-design-explorer/` or `~/.claude/skills/botkits-system-design-explorer/` |
| Codex | `.agents/skills/botkits-system-design-explorer/` or `~/.agents/skills/botkits-system-design-explorer/` |
| Cursor | `.agents/skills/botkits-system-design-explorer/` or `.cursor/skills/botkits-system-design-explorer/` |
| Gemini CLI | `.gemini/skills/botkits-system-design-explorer/` or `.agents/skills/botkits-system-design-explorer/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-system-design-explorer/` or `.agents/skills/botkits-system-design-explorer/` |
| Grok Build | `.grok/skills/botkits-system-design-explorer/` or `~/.grok/skills/botkits-system-design-explorer/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Premium

The free skill works by itself and gives the full method, page structure, rules and review loop. BotKits Premium adds a working example page to copy from, the code for each component (event demo engine, isometric layer stack, walks, keyboard model, cost bar), screenshots, a reading-mode section for pages people read alone, and plugin packaging for Claude Code and Agent Plugins clients.

## Links

- [botkits.dev](https://botkits.dev)
- Inspired by: Dani Acosta's own system design explorer, Ben Shneiderman's "overview first, details on demand" and the C4 model's labelling rules. Details in [SKILL.md](SKILL.md#inspired-by).

## License

MIT.
