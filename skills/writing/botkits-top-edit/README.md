# botkits-top-edit

The final screen before publishing. Run it after botkits-no-ai-slop. It is a checklist, not a critique: it flags issues and does not edit.

Use this as the last mechanical pass before publishing, to screen AI tells and house-style misses that a slop word-list can skip.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-top-edit
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Flags only. Each flag gets a line number, the quoted text, and a fix. It does not edit the file.
- Pass 1 looks for leftover tells that survive a slop word-list: "This" or "That" with no noun, decorative paired constructions, stacked connectors, hedges, even-handed paragraphs that never land, signposting, consultant phrases, repeated section endings, restated points, contrast reframes more than twice in a long piece, and stale metaphors.
- Pass 2 is house style: a concrete opening, a findable takeaway, named sources for big claims, the writer's own detail, destination rules from botkits-no-ai-slop, and a headline that does not repeat the first line.
- Pass 3 is prose: the same word three times in a few lines, three or more passive sentences in a row, five sentences of about the same length, and links that must resolve with honest anchor text. If breaking a rule makes the sentence better, it leaves the line and says so.
- Verdict: Clean (0 to 2 small flags), Quick fixes (3 to 5), or Needs work (6 or more, or anything structural), plus one sentence of advice. After the writer reads the report, it can offer a voice bank and a one-line retro.

## Before / after (example)

This example starts with a draft that already had a slop pass. A sentence still opens with "This" and no noun. An "on the other hand" paragraph never lands. The headline and the first line say the same thing.

After the screen, those issues are flagged with line numbers, quoted text, and a fix. The file is unchanged. The verdict is Clean, Quick fixes, or Needs work, with one sentence of advice.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-top-edit/` or `~/.claude/skills/botkits-top-edit/` |
| Codex | `.agents/skills/botkits-top-edit/` or `~/.agents/skills/botkits-top-edit/` |
| Cursor | `.agents/skills/botkits-top-edit/` or `.cursor/skills/botkits-top-edit/` |
| Gemini CLI | `.gemini/skills/botkits-top-edit/` or `.agents/skills/botkits-top-edit/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-top-edit/` or `.agents/skills/botkits-top-edit/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Nadiem Mahmoud's top-edit](https://github.com/nadiem99/claude-writing-skills/blob/5b52111e1bd30e93643929f17155e82aa26f771f/skills/pipeline/top-edit/SKILL.md) and its [AI tells checklist](https://github.com/nadiem99/claude-writing-skills/blob/5b52111e1bd30e93643929f17155e82aa26f771f/context/ai-tells-checklist.md) (MIT, which credit Every's Kate Lee), [George Orwell's Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/), and [Hardik Pandya's stop-slop](https://github.com/hardikpandya/stop-slop) (MIT). This skill adds a focus on tells that survive a word-list pass, destination and link checks, and an explicit "broken on purpose" exception.

License: MIT
