<picture><source media="(prefers-color-scheme: dark)" srcset="../../../assets/skills/header-botkits-draft-dark.png 1x, ../../../assets/skills/header-botkits-draft-dark@2x.png 2x"><img src="../../../assets/skills/header-botkits-draft-light.png" srcset="../../../assets/skills/header-botkits-draft-light.png 1x, ../../../assets/skills/header-botkits-draft-light@2x.png 2x" width="800" alt="BotKits botkits-draft skill header"></picture>

# botkits-draft

Write from an approved outline, one section at a time. Never produce the whole article in one go.

Use this when writing or expanding an article one section at a time, with the writer's approval between sections.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-draft
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Writes from an approved outline, one section at a time. The writer approves each section before the next. Never produces the whole article in one go.
- Before each section, restates the thesis in one sentence, names the section and why it comes next, and names two habits of the writer's voice to keep.
- Every paragraph moves the piece with a new fact, step, or turn. Uses plain words. Opens each section on something concrete. Leaves `[GAP: what is needed]` instead of inventing numbers, quotes, or sources. Follows botkits-no-ai-slop house rules while writing.
- After each section, offers two versions of any heavy line (the hook, a key claim, the last line), rereads from the top, and proposes an outline change if the section is fighting the plan. Then stops and waits for approval unless the writer asked for more than one section.
- When every section is in: botkits-source-check, then botkits-no-ai-slop.

## Before / after (example)

This example starts with an approved outline. The missing facts are still unmarked. The risk is writing the whole article at once, inventing a number or quote, or polishing a section that fights the outline.

After the pass, each section is written and approved before the next. The thesis is restated first. Voice habits are named. Gaps stay as `[GAP: ...]`. Heavy lines come in two versions for the writer to pick. If a section fights the outline, an outline change is proposed and the work waits. When every section is in, the next steps are botkits-source-check, then botkits-no-ai-slop.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-draft/` or `~/.claude/skills/botkits-draft/` |
| Codex | `.agents/skills/botkits-draft/` or `~/.agents/skills/botkits-draft/` |
| Cursor | `.agents/skills/botkits-draft/` or `.cursor/skills/botkits-draft/` |
| Gemini CLI | `.gemini/skills/botkits-draft/` or `.agents/skills/botkits-draft/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-draft/` or `.agents/skills/botkits-draft/` |
| Grok Build | `.grok/skills/botkits-draft/` or `~/.grok/skills/botkits-draft/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Nadiem Mahmoud's draft](https://github.com/nadiem99/claude-writing-skills/blob/5b52111e1bd30e93643929f17155e82aa26f771f/skills/pipeline/draft/SKILL.md) (MIT), [Paul Graham's Write Simply](https://www.paulgraham.com/simply.html) and [Writing, Briefly](https://www.paulgraham.com/writing44.html), and [George Orwell's Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/). This skill adds gap markers, anti-slop rules during drafting, and permission for natural "But" and "And" openers.

License: MIT
