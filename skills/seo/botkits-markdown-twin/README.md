# botkits-markdown-twin

For one HTML page, publish a clean markdown copy that an agent can read instead of scraping the rendered page. The twin must carry the same facts as the HTML.

Use this when adding a clean markdown twin for one HTML page: a `.md` copy at the same path, a `rel=alternate` type=text/markdown link, and one line for it in /llms.txt.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-markdown-twin
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Writes a clean `.md` copy at the same path, using a form from the [llms.txt v2 spec](https://llmstxt.org/): append `.md` (`page.html.md`) or replace the extension (`page.md`). For a URL with no filename, use `index.html.md` or `index.md`.
- Advertises the twin from the HTML page with `<link rel="alternate" type="text/markdown" href="...">`.
- Adds one line for that twin in `/llms.txt` (creates the file if needed): a markdown link, optionally a colon, and a short note. The link points at the twin, not the HTML page.
- Covers only the one page it was asked to cover. It does not invent a site-wide crawl, a Worker router, or content negotiation unless that work is already in scope.
- The markdown has the same facts as the HTML, without navigation or other chrome. Do not cloak.

## Before / after (example)

This example, from the skill itself, starts with an HTML page at `/docs/install/` (or `/docs/install.html`). The page explains how to install: run `npm install example`, then start the app with `npm start`. There is no markdown twin, no `rel=alternate` link, and no line in `/llms.txt`.

After the three steps, a twin lives at `/docs/install.md` (or `/docs/install/index.md`) with the same facts and no chrome. The HTML page points to it with `rel="alternate" type="text/markdown"`. `/llms.txt` has one new line that links to the twin, not the HTML page.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-markdown-twin/` or `~/.claude/skills/botkits-markdown-twin/` |
| Codex | `.agents/skills/botkits-markdown-twin/` or `~/.agents/skills/botkits-markdown-twin/` |
| Cursor | `.agents/skills/botkits-markdown-twin/` or `.cursor/skills/botkits-markdown-twin/` |
| Gemini CLI | `.gemini/skills/botkits-markdown-twin/` or `.agents/skills/botkits-markdown-twin/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-markdown-twin/` or `.agents/skills/botkits-markdown-twin/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Premium

The free skill works by itself. The [AEO Kit (Markdown Twins + YouTube Watch Pages)](https://daniacostaai.gumroad.com/l/wzalwo) adds the Cloudflare Worker router (content negotiation) and the YouTube watch page builder. Price: $24.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Jeremy Howard's /llms.txt v2 proposal](https://llmstxt.org/). This skill adds a per-page sequence (a markdown twin, a rel=alternate link, and one line in /llms.txt) and a tiny worked example.

License: MIT
