# botkits-ship-post

Turn real work into one honest post. The repo is the source, not a blank page. Drafts only.

Use this when something has shipped (a merged PR, a release, a deploy, a week of commits) and you want one build-in-public post for X, plus a Reddit draft if asked.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-ship-post
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Collects what shipped from git (the given ref, or the last 7 days if none), then asks the owner one question and waits: what got in users' way before, and what is different now. It does not write that sentence for them.
- Picks the one change a user would notice. Opens on the before and after, not the method. Writes three openings and keeps one.
- Drafts one X post, a reply that carries the link if there is one, and a Reddit draft only if asked. Then runs botkits-no-ai-slop and lists every number next to the commit, file, or owner message it came from. Hands the drafts over and stops. Never posts, schedules, or publishes.
- Every number traces to the commits, the diff, or the owner's answer. No claims about what users did or felt unless the owner reported it. If the owner's sentence and the code disagree, it says so and describes what the code does.
- A week of only refactors, dependency bumps, CI, and lint is a quiet week. It says that, and offers to skip or to post about the problem being worked on, in the owner's words.

## Before / after (example)

This example starts with a commit such as `fix: retry failed webhook deliveries`. A method-first draft would say "Added exponential backoff to the webhook worker."

After the skill, the opening is the before and after, as in the skill's own example: "A failed webhook used to mean a lost order notice. Now it retries for an hour before giving up." The output has the picked change, the owner's sentence, the X post, an optional link reply, and a number ledger. Nothing is posted.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-ship-post/` or `~/.claude/skills/botkits-ship-post/` |
| Codex | `.agents/skills/botkits-ship-post/` or `~/.agents/skills/botkits-ship-post/` |
| Cursor | `.agents/skills/botkits-ship-post/` or `.cursor/skills/botkits-ship-post/` |
| Gemini CLI | `.gemini/skills/botkits-ship-post/` or `.agents/skills/botkits-ship-post/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-ship-post/` or `.agents/skills/botkits-ship-post/` |
| Grok Build | `.grok/skills/botkits-ship-post/` or `~/.grok/skills/botkits-ship-post/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Corey Haines's ship-post reference in marketingskills](https://github.com/coreyhaines31/marketingskills/blob/main/skills/social/references/ship-post.md) (MIT, skills/social v2.5.2) and [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) (Apache 2.0). This skill adds a standalone workflow for this repo, a number ledger in the output, an opening step (three options, keep one), a link-carrying reply, and an optional Reddit draft.

License: MIT
