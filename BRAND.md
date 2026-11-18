# BotKits brand rules

This file is the standard for every word we publish about BotKits: README, skill pages, botkits.dev, posts, PRs, and kit listings. AGENTS.md must follow it. For colors, type, logo and images, follow [DESIGN.md](DESIGN.md).

Last updated: 18 Nov 2026. Owner: Dani Acosta.

## 1. Name

- In prose, always write **BotKits**. One word, capital B, capital K.
- The logo wordmark is also **BotKits** (Dani, 18 Nov 2026). Lowercase "botkits" appears only in the repo slug, the domain and the install command.
- Repo slug: `botkitsdev/botkits`. Site: `botkits.dev`. Write these exactly, in code format when they are commands or paths.
- Never write: "botskills", "Bot Kits", "Botkits", "BOTKITS", "Grok Bot skills", "Grok skills".
- The owner is **Dani Acosta**. Use that exact name. X handle: @DaniAcostaAI.
- Paid products use their exact listing names (see section 9).

## 2. Positioning

Options (one line each):

1. Skills your bots can run today. Open SKILL.md folders for Claude, ChatGPT, Codex, Cursor, Gemini, Copilot and Grok Bot.
2. Plain, tested processes for the jobs your bots do every day. One SKILL.md each. MIT.
3. Open skills for any agent that reads SKILL.md. Built and used daily by a real bot team.

**Pick: option 1.** It keeps the current H1, names the agents a reader already uses, and says what the thing is (a folder with a SKILL.md). Use the short form "Skills your bots can run today" as the H1 and the full line as the subhead.

BotKits is not a Grok Bot project. Grok Bot is where we run the skills every day. That is proof, not the audience.

## 3. Who it is for

- Solo founders and small teams who run AI agents for real work: writing, SEO, video, ads, bot operations.
- People who already use one of the agents in section 7 and want a clear process, not a prompt pack.
- Not for: people who want a hosted app, a course, or a promise of growth.

## 4. Promise and proof

- Promise: a clear process your agent can follow for one job, in a file you can read in five minutes.
- Every number needs a source you can open: a file, a commit, a dashboard, a public URL. Put the source and the date next to it, or in a linked note.
- No invented numbers. No "10x", "hours saved", "thousands of users" unless we measured it and can show where.
- Skill count: say the real count from the repo on the day you write it. Update the badge, the README and the site together.
- "Used daily by my own bots" is true for Grok Bot only. Do not extend it to other agents.
- Screenshots and examples must come from real runs. Mark mockups as mockups.

## 5. Voice and tone

- Short. Concrete. Verbs first. One idea per sentence.
- Plain English in the spirit of ASD-STE100: common words, active voice, present tense, sentences under about 20 words.
- First person singular for Dani ("I", "my bots"). Second person for the reader ("your bot").
- Say what the skill does, what goes in, what comes out, and what it will not do.
- Calm. No hype, no exclamation marks, no emoji in prose.
- No em dashes. Use a period, a comma, a colon or parentheses.

## 6. Skill names and descriptions

- Folder name = `name` in frontmatter. Lowercase, digits and hyphens, max 64 characters (Agent Skills spec).
- Name the job or the output: `x-article`, `shorts-reframe`, `source-check`. Not the tool or the brand.
- New skills must not carry one agent's name (no `*-grok-bot`, `*-claude`) unless the skill only works there. If so, add a `compatibility` line in the frontmatter and say it in the first line of the page.
- `description` starts with the trigger: "Use this when ..." or "Use to ...". Then the output. Then one key limit. Max 1024 characters; aim for under 300.
- Front-load trigger words. Some agents cut long descriptions.

## 7. Compatibility wording

Only claim what we checked. Source: `2026-11-18-agent-compat-research.md`. Recheck before each release.

| Wording to use | Agents |
| --- | --- |
| "Used daily" | Grok Bot |
| "Installs with `npx skills add`" (tested 18 Nov 2026) | Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, Grok Build |
| "Supports the SKILL.md format (vendor docs)" | Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at agentskills.io |
| "No direct install yet. Paste the instructions into a chat." | ChatGPT dots, Meta Muse |

Rules:

- Say "Other agents that support the Agent Skills format can load it. We have not run it there." for agents we have not run. Never say "works everywhere".
- Do not say a skill "works in X" until someone ran it there. Install tested is not run tested.
- Skills that use Grok Bot tools (routines, cards, agent folders) must say so on the first line of their page: "Needs Grok Bot. Uses routines and approval cards."
- Do not write "compatible with Muse" or "works with dots".

## 8. README and skill page shape

Every skill page (README or botkits.dev) uses this order:

1. One-line promise. What job it does, in plain words.
2. Who it is for. One line.
3. Install: `npx skills add botkitsdev/botkits --skill <name>`, plus the manual folder copy for agents the CLI does not cover.
4. What it does. 3 to 6 bullets. Inputs, steps, output, limits.
5. Before and after. A short real example. Mark it as an example.
6. Works with. Use section 7 wording.
7. Links: botkits.dev page, the paid kit if one exists (section 9), Inspired by.
8. License: MIT.

## 9. Links and calls to action

- Main link everywhere: the repo `https://github.com/botkitsdev/botkits` or `https://botkits.dev`.
- One call to action per piece. Default: "Install with `npx skills add botkitsdev/botkits`" or "Browse on botkits.dev".
- Gumroad links appear only in a section titled **Paid kits** (README, site kits page, a skill page's paid kit line). Never in posts, Reddit comments, PR descriptions or a skill's `SKILL.md`.
- Paid kits (exact names and prices): X Article Writer, $7. AEO/GEO Site Audit & Build Kit, $9. Shorts Builder Kit, $14. AEO Kit (Markdown Twins + YouTube Watch Pages), $24. Check the listing before you quote a price.
- Free skills stay free and complete. A paid kit is the tested, ready-to-run version, not the missing half.
- Paid kit files (scripts, templates, examples, tests) never go in this repo. The lite skills `x-article`, `aeo-geo-site`, `shorts-reframe` and `markdown-twin` hold only `SKILL.md` and `README.md`. The `paid-guard` check stops any PR that breaks this.

## 10. Words to avoid

Do not use: unlock, unleash, supercharge, game-changer, revolutionize, seamless, effortless, powerful, robust, cutting-edge, next-level, elevate, empower, leverage (as a verb), harness, delve, dive in, deep dive, journey, landscape, realm, tapestry, testament, in today's fast-paced world, it's not just X it's Y, the best part?, here's the thing, let that sink in, magic, secret sauce, 10x, insane, crushing it, AI-powered (as a selling point), "simply", "just" (as in "just run").

Also avoid: rhetorical questions as hooks, lists of three adjectives, closing slogans, and claims about other people's results.

## 11. Credit

- Every skill written from outside ideas ends with an **Inspired by** section.
- Write it in our own words. Name the source with a link, say what it does well, what it misses, and what our version adds.
- Keep upstream license notices where they apply. Full list: `docs/credits.md` and `THIRD_PARTY_NOTICES.md`.
- Never copy text from a source into a skill.

## 12. Visuals

See [DESIGN.md](DESIGN.md). In short: botkits.dev blue, `#2340c4` on light and `#a3b4ff` on dark. Lime is retired; do not use it in new work.
