# botkits-no-ai-slop

Edit out AI-writing tells with the smallest change that works, or flag them without rewriting. Never adds facts.

Load first for any text that will be published (X posts and replies, Reddit comments, LinkedIn, ads, site, PRs).

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-no-ai-slop
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Load it before writing anything public, and as the last edit inside botkits-x-article, botkits-social-copywriting, botkits-ship-post, botkits-draft, and diagram captions. The goal is copy that sounds like the person who wrote it, minus the habits a model leaves behind.
- Four modes: Edit (default; lightest touch, then show what changed), Detect (list each tell with the quoted line, the pattern name, and a fix; do not rewrite and do not give an AI-probability score), Embedded (cleaned text only, for other skills), and Batch (run Edit or Detect on each piece, then compare first and last lines for shared templates).
- Before editing, gets the writer's real voice from two or three published pieces in the same place when it can. The sample outranks the general tells. House rules still apply.
- Fixes the shape, not the symptom. Leaves quotations, titles, names, code, URLs, and mentioned phrases alone. Never adds a number, name, date, quote, or experience the writer did not give. Runs a fact lock on names, numbers, links, negations, conditions, and certainty.
- Optional `python3 scripts/lint.py draft.md`, run from this folder, quotes mechanical tells. House rules for publishing: no em dashes in short copy, no trailing period on social posts, no hyphens on LinkedIn, real units only, and posts in a code block.

## Before / after (example)

This example starts with a draft that will be published. It has a staged contrast, a slogan closer, and an em dash in short copy. There is no check yet that names, numbers, links, and negations survived an edit.

In Edit mode, those tells are removed with a light touch, the writer's voice is kept, and the output shows what changed plus a fact-lock line. In Detect mode the same tells are listed with a quoted line and a fix; the draft is not rewritten. Nothing new is added.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-no-ai-slop/` or `~/.claude/skills/botkits-no-ai-slop/` |
| Codex | `.agents/skills/botkits-no-ai-slop/` or `~/.agents/skills/botkits-no-ai-slop/` |
| Cursor | `.agents/skills/botkits-no-ai-slop/` or `.cursor/skills/botkits-no-ai-slop/` |
| Gemini CLI | `.gemini/skills/botkits-no-ai-slop/` or `.agents/skills/botkits-no-ai-slop/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-no-ai-slop/` or `.agents/skills/botkits-no-ai-slop/` |
| Grok Build | `.grok/skills/botkits-no-ai-slop/` or `~/.grok/skills/botkits-no-ai-slop/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Peter Yang's no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT), [Wikipedia's Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (CC BY-SA 4.0), [blader/humanizer](https://github.com/blader/humanizer) (MIT), [Hardik Pandya's stop-slop](https://github.com/hardikpandya/stop-slop) (MIT), [Conor Bronsdon's avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) (MIT), [Lauren Tan's pstack unslop](https://github.com/cursor/plugins/tree/main/pstack/skills/unslop) (MIT), and posts by [@moinerus](https://x.com/moinerus/status/2100301069070872984) and [@sloporific](https://x.com/sloporific/status/2101360288851247255). This skill adds four modes (including Embedded and Batch), a voice step from the writer's published pieces, a fact lock, an optional `scripts/lint.py`, a Never add list, and house rules for short copy.

License: MIT
