# botkits-diagram-design

Make one explainer diagram that teaches one thing, branded and not dashboard slop.

Use this when you need an architecture, sequence, process, loop or layer diagram, or a still card for a post, as HTML, SVG or PNG.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-diagram-design
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it. Copy the skill folder itself, not the category folder.

## What it does

- Checks first if the idea needs a diagram. It draws only when order, flow, containment or connection carries meaning.
- Writes the caption first: one sentence the diagram proves. Then it picks the type, lists the nodes, and splits into an overview and a detail past about nine nodes or twelve arrows.
- Takes colors, fonts and spacing from the live site or the user's saved profile, and asks once if neither exists.
- Uses one accent for the one or two nodes the caption is about, borders instead of shadows, and labeled arrows. It never ships ranking dashboards, neon glow, or Mermaid auto-layout as a final design.
- Outputs one self-contained HTML file with inline SVG and a `<title>` and `<desc>`, plus a 2x PNG for posts and ads. Social stills are 1200×675 unless the platform asks for another size.
- Can add an optional line-draw clip timed by the [botkits-motion-picker](../botkits-motion-picker/) presets. The PNG stays the default, and rendered files stay out of git.

## Before / after (example)

### Before

A post needs a picture of a pipeline. The usual result is three equal summary cards on a dark background with a neon glow, an accent on every node, and no caption.

### After

The caption is written first. The flow has labeled boxes and directed arrows on a grid. One accent marks the node the caption is about. The file is one HTML page with inline SVG, and the 2x PNG is opened and checked before handover.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-diagram-design/` or `~/.claude/skills/botkits-diagram-design/` |
| Codex | `.agents/skills/botkits-diagram-design/` or `~/.agents/skills/botkits-diagram-design/` |
| Cursor | `.agents/skills/botkits-diagram-design/` or `.cursor/skills/botkits-diagram-design/` |
| Gemini CLI | `.gemini/skills/botkits-diagram-design/` or `.agents/skills/botkits-diagram-design/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-diagram-design/` or `.agents/skills/botkits-diagram-design/` |
| Grok Build | `.grok/skills/botkits-diagram-design/` or `~/.grok/skills/botkits-diagram-design/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Cathryn Lavery's diagram-design](https://github.com/cathrynlavery/diagram-design), the [C4 model notation guide](https://c4model.com/diagrams/notation) and [Edward Tufte's idea of chartjunk](https://en.wikipedia.org/wiki/Chartjunk). This skill works without the upstream pack, adds caption-first planning and a "should this be a diagram?" test, and adds an optional line-draw clip.

License: MIT
