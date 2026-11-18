# botkits-outline

Turn a seed, interview notes, or a pile of facts into a writing plan the writer can approve. No prose yet.

Use this when turning a seed, interview, or set of facts into a writing plan before drafting an article.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-outline
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Starts with one sentence: the claim the piece makes and the one thing a reader will learn. If that sentence is missing, it asks the writer.
- Picks a shape that fits the material and says why: Story to mechanism, Answer first, Teardown, or Changed my mind. Heavy sections get more beats than light ones.
- For each section it records a working heading, the job it does in one line, the facts or examples it will use, and its rough length.
- Adds two or three openings built from something real in the material (a moment, a number, a quote), gaps marked `[GAP: ...]` (never filled by guessing), and a cut list of material that is true but off the point.
- Presents the plan and waits for a yes. After sign-off the chain is draft, source-check, no-ai-slop. The plan can still move once drafting starts.

## Before / after (example)

This example starts with a seed, interview notes, or a pile of facts. There is no claim sentence yet. No shape has been chosen. Missing numbers or quotes are still unmarked, so they could be guessed later. Off-point material has nowhere to go.

After the plan you have a one-sentence claim, a named shape with a reason, a section list with jobs, facts and rough lengths, two or three openings taken from the material, gaps marked `[GAP: ...]`, and a cut list. The plan waits for a yes. Nothing is drafted yet.

## Works with

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Nadiem Mahmoud's outline](https://github.com/nadiem99/claude-writing-skills/blob/5b52111e1bd30e93643929f17155e82aa26f771f/skills/pipeline/outline/SKILL.md) (MIT), [Paul Graham's Writing, Briefly](https://www.paulgraham.com/writing44.html), and [Google's Technical Writing Two on large documents](https://developers.google.com/tech-writing/two/large-docs). This skill adds a one-sentence claim first, four named shapes, a cut list, and a note that the plan will change during drafting.

License: MIT
