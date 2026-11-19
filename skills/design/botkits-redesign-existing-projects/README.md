# botkits-redesign-existing-projects

Improve the design of a site or app that already exists, without starting over.

Use this when you want a better-looking, easier-to-use site and must keep the stack, the features, and what users already rely on.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-redesign-existing-projects
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it. Copy the skill folder itself, not the category folder.

## What it does

- Asks, or infers and states, what the page must make people do and what must not change. Then it reads the code and takes "before" screenshots at mobile and desktop widths.
- Audits each page for hierarchy, type, color, layout and spacing, states, feedback, accessibility, template tells and code smells, with a screenshot or line reference for each problem.
- Ranks the problems by user impact and effort. Problems that block the main action or fail accessibility come first.
- Fixes in small steps, one theme per commit or PR, inside the current stack. It runs the app and its tests after each step.
- Hands over "after" screenshots at the same widths, paired with the "before" set. It lists what changed, what it left alone, and what needs the user's decision.

## Before / after (example)

### Before

An existing site has too many type sizes, an accent used everywhere, gray text that fails contrast, and missing focus states. The usual fix is a framework migration or one large rewrite.

### After

The problems are listed with screenshots and ranked by impact and effort. Contrast and focus come first. Each fix lands as its own commit on the current stack, and nothing that worked before breaks. Before and after screenshots at the same widths show the difference.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-redesign-existing-projects/` or `~/.claude/skills/botkits-redesign-existing-projects/` |
| Codex | `.agents/skills/botkits-redesign-existing-projects/` or `~/.agents/skills/botkits-redesign-existing-projects/` |
| Cursor | `.agents/skills/botkits-redesign-existing-projects/` or `.cursor/skills/botkits-redesign-existing-projects/` |
| Gemini CLI | `.gemini/skills/botkits-redesign-existing-projects/` or `.agents/skills/botkits-redesign-existing-projects/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-redesign-existing-projects/` or `.agents/skills/botkits-redesign-existing-projects/` |
| Grok Build | `.grok/skills/botkits-redesign-existing-projects/` or `~/.grok/skills/botkits-redesign-existing-projects/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Leon Lin's Taste Skill redesign-skill](https://github.com/Leonxlnx/taste-skill/tree/main/skills/redesign-skill), [Nielsen Norman Group's 10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) and [Vercel's Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines). This skill adds goal questions before the audit, before and after screenshots, impact-by-effort ranking, and one theme per commit.

License: MIT
