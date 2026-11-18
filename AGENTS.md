# AGENTS.md

Instructions for any coding agent (Grok Bot, Claude Code, Codex, Cursor, Gemini CLI, Muse Code and others) working in this repo.

## Read first

1. [BRAND.md](BRAND.md): the name (always **BotKits** in prose), what we may claim, voice and links.
2. [DESIGN.md](DESIGN.md): palette, fonts, logo use, image sizes and the per-skill README template.

Both are required. If a task conflicts with them, stop and ask the owner instead of guessing.

## Repo layout

```
skills/<category>/<skill-name>/SKILL.md   instructions the bot loads
skills/<category>/<skill-name>/README.md  optional, for humans (template in DESIGN.md)
skills/<category>/<skill-name>/...        optional scripts, templates, references
assets/                                   shared README images
docs/credits.md                           source credits
THIRD_PARTY_NOTICES.md                    license notices
```

Categories today: ads, bots, design, engineering, images, seo, video, writing, youtube.

## Skill format

Every skill follows the open [Agent Skills spec](https://agentskills.io/specification):

- `SKILL.md` starts with YAML frontmatter on line 1. Nothing (not a title, not a blank line) comes before the opening `---`.
- `name`: lowercase letters, digits and single hyphens, at most 64 characters, and the same as the folder name.
- `description`: at most 1024 characters. Say what the skill does and when to use it. Put the trigger words first, because some bots shorten long descriptions.
- Keep `SKILL.md` under 500 lines. Move long reference material to files next to it and link them with relative paths, one level deep.
- One skill, one job.

When you add a skill, also add it to the skill list and the count in `README.md`.

## Portable skills

A skill should run on any bot that reads the format. To keep it portable:

- Use only `name` and `description` in frontmatter, plus the optional spec fields (`license`, `compatibility`, `metadata`). Bot-specific fields such as Claude Code's `disable-model-invocation` are ignored or rejected elsewhere.
- Write steps in plain words ("search the web", "run this command"), not one bot's tool names. If a step needs a specific bot or tool, say so in a `## Needs` section and in `compatibility`.
- Scripts must state their dependencies and fail with a clear message.
- No secrets, tokens or personal account IDs in any file.
- Do not claim a skill works on a bot unless it was run there. See the table in BRAND.md.

## Use a skill in other bots

Install with the [Skills CLI](https://github.com/vercel-labs/skills), which copies folders to the right place per agent:

```sh
npx skills add botkitsdev/botkits --skill <skill-name>
```

Or copy one skill folder by hand. Copy the skill folder itself (`skills/<category>/<skill-name>/`), not the category folder, because some bots only look one folder deep.

| Bot | Where the folder goes | Source |
| --- | --- | --- |
| Claude Code | `.claude/skills/<skill-name>/` or `~/.claude/skills/` | [docs](https://code.claude.com/docs/en/skills) |
| Claude apps | ZIP the folder, upload in Customize > Skills | [help](https://support.claude.com/en/articles/12512180-use-skills-in-claude) |
| Codex | `.agents/skills/<skill-name>/` | [docs](https://learn.chatgpt.com/docs/build-skills) |
| ChatGPT (Business, Enterprise, Edu, Healthcare) | Skills > Create > Upload from your computer | [help](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) |
| Cursor | `.agents/skills/` or `.cursor/skills/` (also reads `.claude/skills/`) | [docs](https://cursor.com/docs/skills) |
| Gemini CLI | `.gemini/skills/<skill-name>/` or `.agents/skills/`, one level deep only | [docs](https://geminicli.com/docs/cli/tutorials/skills-getting-started/) |
| Muse Code | `.agents/skills/<skill-name>/` | [docs](https://meta-models.github.io/muse-code-sdk/next/guides/extend/skills/) |
| Grok Bot | Paste the `SKILL.md` in chat and ask the Bot to save it as a skill | [docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) |
| Muse (Meta app), ChatGPT dots | No documented skill install. Paste the instructions into chat or custom instructions. | not verified |

`.agents/skills/` is the shared folder that Codex, Cursor, Gemini CLI and Muse Code all read.

## Outside sources

- Rewrite outside skills in our own words. Do not copy any run of 8 or more words from the source.
- End the skill (or its README) with an `## Inspired by` section that names and links each source.
- Add the source to `docs/credits.md`. If its license needs a notice, add it to `THIRD_PARTY_NOTICES.md`.
- Do not copy from sources that have no reuse license, such as marketplace templates.

## Git and pull requests

- Branch from `main`. Bot branches start with the bot's prefix, for example `grok-<topic>`.
- One topic per PR. For README upgrades, about 5 skills per PR.
- Never force-push and never rebase a shared branch. Add a new commit instead.
- Do not merge your own PR. A reviewer merges.
- Do not change `assets/` or `README.md` in a PR whose topic is something else.
- PR body: what changed, why, and links to any sources.

## Before you open a PR

- [ ] Prose says BotKits, never botskills or Botkits.
- [ ] No lime `#C8FF3D` in new images or badges.
- [ ] Every image has real alt text.
- [ ] Every number has a source.
- [ ] `name` matches the folder and frontmatter is on line 1.
- [ ] New outside ideas are credited.
- [ ] Public text passed [no-ai-slop](skills/writing/no-ai-slop/).
