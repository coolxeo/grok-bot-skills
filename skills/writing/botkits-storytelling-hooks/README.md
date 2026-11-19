# botkits-storytelling-hooks

Write a hook from a fact you already have.

For writers and operators who need a first line that names a real story.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-storytelling-hooks
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Picks a hook family from a fact you already have (a date, a cost, a client question, a rule you follow).
- Drafts 3 hooks from 2 or 3 families, keeps 1, and checks that the rest of the post can pay off that line.
- Fills every blank with a real fact. If a fact is missing, it changes family instead of inventing one.
- Uses our own templates rather than another writer's lines.

## Before / after (example)

This example starts with a topic and no fact in the first line: "Some notes on how my writing process improved this year." The reader cannot tell what changed, or whether the post will pay off.

After the pass, the chosen hook (Lesson family) is:

```text
2 years of weekly posts left me with one rule: finish the outline before any sentence.
```

The two unused options came from Transformation and Mistake. The body then has to deliver that one rule.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-storytelling-hooks/` or `~/.claude/skills/botkits-storytelling-hooks/` |
| Codex | `.agents/skills/botkits-storytelling-hooks/` or `~/.agents/skills/botkits-storytelling-hooks/` |
| Cursor | `.agents/skills/botkits-storytelling-hooks/` or `.cursor/skills/botkits-storytelling-hooks/` |
| Gemini CLI | `.gemini/skills/botkits-storytelling-hooks/` or `.agents/skills/botkits-storytelling-hooks/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-storytelling-hooks/` or `.agents/skills/botkits-storytelling-hooks/` |
| Grok Build | `.grok/skills/botkits-storytelling-hooks/` or `~/.grok/skills/botkits-storytelling-hooks/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Pattern library: [references/patterns.md](references/patterns.md)
- Inspired by: [Chase Dimond's 80 Storytelling Hooks](https://x.com/ecomchasedimond/status/2122793870669062451) and the 11 other save-first posts listed in [SKILL.md](SKILL.md#inspired-by). This skill adds why each family works, our own templates, a fact rule for every blank, and a check that the body pays off the hook.

License: MIT
