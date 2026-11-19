<picture><source media="(prefers-color-scheme: dark)" srcset="../../../assets/skills/header-botkits-source-check-dark.png 1x, ../../../assets/skills/header-botkits-source-check-dark@2x.png 2x"><img src="../../../assets/skills/header-botkits-source-check-light.png" srcset="../../../assets/skills/header-botkits-source-check-light.png 1x, ../../../assets/skills/header-botkits-source-check-light@2x.png 2x" width="800" alt="BotKits botkits-source-check skill header"></picture>

# botkits-source-check

Check every factual claim in a draft before it goes out. Report only, except for adding or updating a Sources section.

Use this after drafting an article, before publish, to verify every factual claim and statistic against a named source.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-source-check
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Logs each checkable statement with its line: numbers, dates, quotes, "X said", "X caused Y", rankings, comparisons, and claims about a named person or company. Skips clearly marked opinions and first-hand experience.
- Checks in this order: a source named in the draft, the writer's notes and files, then the open web. Follows quotes and numbers back to where they first appeared.
- Gives each claim one status: OK, Stretched, Open, or Wrong. When two good sources give different numbers, uses the primary one and tells the writer about the conflict.
- Looks at the whole draft for over-reliance on one source, old numbers, numbers without context, vague attribution ("studies show", "experts agree"), and social posts or press releases standing in for evidence.
- Adds or updates a Sources section at the end, numbered and grouped by section, each with author or outlet, title, date, URL, and the date it was checked. Reports counts, each non-OK claim with a fix, and a verdict: Ready, Small fixes, Needs sourcing, or Not reliable.
- Never rewrites the prose. Never papers over an open claim with a source that does not say it.

## Before / after (example)

This example starts with a drafted article. Some numbers, quotes and "X said" lines have no named source. A later article is cited instead of the place the figure first appeared. Vague attribution such as "studies show" is still in the text.

After the check, every checkable claim has a status (OK, Stretched, Open, or Wrong). Each non-OK claim has its line, what the source actually says, and a fix. A Sources section is added or updated, with access dates. The verdict is Ready, Small fixes, Needs sourcing, or Not reliable. The prose is not rewritten.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-source-check/` or `~/.claude/skills/botkits-source-check/` |
| Codex | `.agents/skills/botkits-source-check/` or `~/.agents/skills/botkits-source-check/` |
| Cursor | `.agents/skills/botkits-source-check/` or `.cursor/skills/botkits-source-check/` |
| Gemini CLI | `.gemini/skills/botkits-source-check/` or `.agents/skills/botkits-source-check/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-source-check/` or `.agents/skills/botkits-source-check/` |
| Grok Build | `.grok/skills/botkits-source-check/` or `~/.grok/skills/botkits-source-check/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Nadiem Mahmoud's source-check](https://github.com/nadiem99/claude-writing-skills/blob/5b52111e1bd30e93643929f17155e82aa26f771f/skills/pipeline/source-check/SKILL.md) (MIT), [Mike Caulfield's SIFT](https://hapgood.us/2019/06/19/sift-the-four-moves/), and [Wikipedia's Verifiability policy](https://en.wikipedia.org/wiki/Wikipedia:Verifiability) (CC BY-SA 4.0). This skill adds a check of who is behind a source, a rule for conflicting numbers, and access dates and archive links.

License: MIT
