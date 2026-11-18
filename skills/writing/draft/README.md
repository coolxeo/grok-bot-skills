# draft

Write from an approved outline, one section at a time. Never produce the whole article in one go.

Use this when writing or expanding an article one section at a time, with the writer's approval between sections.

## Install

```sh
npx skills add botkitsdev/botkits --skill draft
```

To list the 31 skills in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Writes from an approved outline, one section at a time. The writer approves each section before the next. Never produces the whole article in one go.
- Before each section, restates the thesis in one sentence, names the section and why it comes next, and names two habits of the writer's voice to keep.
- Every paragraph moves the piece with a new fact, step, or turn. Uses plain words. Opens each section on something concrete. Leaves `[GAP: what is needed]` instead of inventing numbers, quotes, or sources. Follows no-ai-slop house rules while writing.
- After each section, offers two versions of any heavy line (the hook, a key claim, the last line), rereads from the top, and proposes an outline change if the section is fighting the plan. Then stops and waits for approval unless the writer asked for more than one section.
- When every section is in: source-check, then no-ai-slop.

## Before / after (example)

This example starts with an approved outline. The missing facts are still unmarked. The risk is writing the whole article at once, inventing a number or quote, or polishing a section that fights the outline.

After the pass, each section is written and approved before the next. The thesis is restated first. Voice habits are named. Gaps stay as `[GAP: ...]`. Heavy lines come in two versions for the writer to pick. If a section fights the outline, an outline change is proposed and the work waits. When every section is in, the next steps are source-check, then no-ai-slop.

## Works with

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Nadiem Mahmoud's draft](https://github.com/nadiem99/claude-writing-skills/blob/5b52111e1bd30e93643929f17155e82aa26f771f/skills/pipeline/draft/SKILL.md) (MIT), [Paul Graham's Write Simply](https://www.paulgraham.com/simply.html) and [Writing, Briefly](https://www.paulgraham.com/writing44.html), and [George Orwell's Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/). Mahmoud drafts section by section and checks the thesis first, but bans "But" and "And" openers and leans on vault files. This skill adds gap markers, anti-slop rules during drafting, and permission for natural "But" and "And" openers.

License: MIT
