# BotKits brand

This file sets the name, the claims and the voice for BotKits. Every README, skill, image caption, PR body and post about this repo follows it. Visual rules live in [DESIGN.md](DESIGN.md).

## Name

- In prose, the name is always **BotKits**: capital B, capital K, one word.
- Never write "botskills" (the old name), "Botkits", "Bot Kits" or "BOTKITS" in prose.
- Lowercase `botkits` is only for URLs, the repo slug, package and folder names, and code: `botkits.dev`, `botkitsdev/botkits`, `npx skills add botkitsdev/botkits`.
- The logo wordmark is drawn as lowercase "botkits" for now. That is artwork, not prose. Dani decides if it changes.
- The author is **Dani Acosta**. On X: [@DaniAcostaAI](https://x.com/DaniAcostaAI).

## What BotKits is

BotKits is a set of open skill folders for AI bots and coding agents. Each skill is one job, written as a `SKILL.md` file. Paid kits on [botkits.dev](https://botkits.dev/kits/) are the tested, ready-to-run versions of some free skills.

One-line positioning: **Skills your bots can run today.**

## Which bots

BotKits is not Grok-only. Skills use the open [Agent Skills](https://agentskills.io/specification) format (a folder with a `SKILL.md` that starts with `name` and `description`), and that format is read by many bots. Say only what each bot can do today:

| Bot | What we can say | Source |
| --- | --- | --- |
| Claude Code | Loads skill folders from `.claude/skills/`. | [Claude Code docs](https://code.claude.com/docs/en/skills) |
| Claude apps | Custom skills upload as a ZIP in Customize > Skills, with code execution on. | [Claude Help Center](https://support.claude.com/en/articles/12512180-use-skills-in-claude) |
| Codex | Loads skill folders from `.agents/skills/`. | [ChatGPT Learn: Build skills](https://learn.chatgpt.com/docs/build-skills) |
| ChatGPT | Skills can be uploaded on Business, Enterprise, Edu and Healthcare workspaces. | [OpenAI Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) |
| Cursor | Loads skill folders from `.agents/skills/` and `.cursor/skills/`, and also reads `.claude/skills/` and `.codex/skills/`. | [Cursor docs](https://cursor.com/docs/skills) |
| Gemini CLI | Loads skill folders from `.gemini/skills/` or `.agents/skills/`. | [Gemini CLI docs](https://geminicli.com/docs/cli/creating-skills/) |
| Muse Code | Loads skill folders from `.agents/skills/`. | [Muse Code docs](https://meta-models.github.io/muse-code-sdk/next/guides/extend/skills/) |
| Grok Bot | Saves a skill from chat into your private skill library, shared by all your Bots. | [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) |
| Muse (Meta app), ChatGPT dots | No skill install found in official docs. You can paste a skill's text into chat or into custom instructions. | See AGENTS.md research notes |

Rules for claims:

- Do not say "works with every bot" or "tested on X" unless someone ran it there and kept the proof.
- Some skills use one bot's tools (Grok Bot routines, a signed-in browser, ffmpeg). Say so in that skill's README.
- When a bot adds or drops support, update this table first, with the source link.

## Voice

- Plain, short and concrete. Say what the skill does and what you get.
- Use numbers only from a source you can link or a run you can show. No invented numbers, no made-up users, no fake reviews.
- No hype words: "revolutionary", "game-changer", "supercharge", "unlock", "seamless", "effortless", "10x", "magic".
- No AI tells. Run [no-ai-slop](skills/writing/no-ai-slop/) on any public text.
- First person is Dani's voice ("my bot team", "I use this daily") only when it is true.
- Nothing about ads results, revenue or sponsors unless Dani signs off on the exact claim.

## Links

- Site: [botkits.dev](https://botkits.dev)
- Repo: [github.com/botkitsdev/botkits](https://github.com/botkitsdev/botkits)
- Paid kits: [botkits.dev/kits](https://botkits.dev/kits/)
- Install line: `npx skills add botkitsdev/botkits`

Link to the repo or botkits.dev first. Gumroad links go only in the paid-kit line of a skill README or on botkits.dev.

## Credits

Skills inspired by outside work are rewritten in our own words and end with an "Inspired by" section. See [docs/credits.md](docs/credits.md) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). BotKits is a community project and is not affiliated with xAI, Cursor, Anthropic, OpenAI, Google or Meta.
