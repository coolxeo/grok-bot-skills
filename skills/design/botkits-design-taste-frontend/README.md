# botkits-design-taste-frontend

Build a landing page, portfolio, or marketing site that looks chosen for its subject, not like a template.

Use this when you build a page from a brief and want the result to fit this subject and this audience.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-design-taste-frontend
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it. Copy the skill folder itself, not the category folder.

## What it does

- Writes a one-line design read before any code: what the page is for, who it is for, the one action it drives, and the mood in three words.
- Plans tokens first: 4 to 6 named colors with roles, one or two type families, a one-line idea per section, and one bold element. Then checks if the plan would fit any similar page, and changes that part if so.
- Avoids common generated-page defaults, such as cream and terracotta, neon on near-black, identical cards, fake screenshots and invented logos or metrics.
- Builds with real copy for the end user and real images, or labeled image slots. It checks each dependency before it imports it, and keeps a floor for responsive layout, keyboard focus, reduced motion and WCAG AA contrast.
- Opens the page in a browser at mobile and desktop widths, fixes what looks off, and hands over the screenshots with the code.

## Before / after (example)

### Before

A brief asks for a product landing page. The usual result is a centered hero, three feature cards, a logo strip and a testimonial carousel. Every section fades in. The quotes come from a stock "Jane Doe".

### After

The page starts from a written design read and a token plan with one bold element. Copy is written for the end user, with buttons that say what happens. Missing images are labeled slots, listed at the end. There is one motion moment, or none. Screenshots at mobile and desktop widths come with the code.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-design-taste-frontend/` or `~/.claude/skills/botkits-design-taste-frontend/` |
| Codex | `.agents/skills/botkits-design-taste-frontend/` or `~/.agents/skills/botkits-design-taste-frontend/` |
| Cursor | `.agents/skills/botkits-design-taste-frontend/` or `.cursor/skills/botkits-design-taste-frontend/` |
| Gemini CLI | `.gemini/skills/botkits-design-taste-frontend/` or `.agents/skills/botkits-design-taste-frontend/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-design-taste-frontend/` or `.agents/skills/botkits-design-taste-frontend/` |
| Grok Build | `.grok/skills/botkits-design-taste-frontend/` or `~/.grok/skills/botkits-design-taste-frontend/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Leon Lin's Taste Skill](https://github.com/Leonxlnx/taste-skill), [Anthropic's frontend-design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design) and [Vercel's Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines). This skill adds a short loadable process, a screenshot check at two widths, copy rules tied to botkits-no-ai-slop, and an accessibility floor.

License: MIT
