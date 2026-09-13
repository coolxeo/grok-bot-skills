# grok-bot-skills

Portable **Grok Bot** skills (`SKILL.md`) — scrubbed for public use.

> Not affiliated with Cursor or xAI.

## What a Grok Bot skill is

A skill is a folder with a `SKILL.md` file:

1. **YAML frontmatter** — at least `name` and `description` (the when-to-use line agents match against).
2. **Markdown body** — standing instructions the bot follows when the skill is invoked.

In Grok Bot / sand workflows, skills are identified by slug (folder name). Cross-links often use `sand-workflow:<slug>`.

## Install

1. Copy the skill folders you want into your Grok Bot workflows directory (typically under the agent workflows / skills path your bot already uses).
2. Invoke with `/` or `@` plus the skill name / slug (for example `/no-ai-slop` or `@design-a-grok-bot`), depending on your Grok Bot UI.
3. Prefer **one job per skill**. Do not merge unrelated playbooks into a single file.

## Ethos

- **One job.** Each skill does one thing and refuses adjacent work.
- **Anti-slop.** Prefer concrete, short, verified prose over generic AI filler. Start publishing text with `no-ai-slop`.
- **Portable.** No personal names, emails, account IDs, product cast locks, or live calendars in this repo.

## Privacy

This tree is scrubbed for public release:

- No personal names or family references
- No personal or employer emails
- No account IDs, cookies, or API keys
- No product-specific cast boards / character locks in general playbooks
- No live personal calendars or home-timezone schedules tied to a private identity

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contributor scrub checklist.

## Skill index

| Slug | When to use |
|------|-------------|
| `aeo-geo-site` | Building or updating a site for SEO plus AEO/GEO so assistants can cite it cleanly |
| `chatgpt-images-browser-playbook` | Generating stills on chatgpt.com via signed-in Images 2.5 UI (session-only; one still per dispatch) |
| `coach` | Structural read of a draft before line-edit (thesis, arc, teach test) |
| `design-a-grok-bot` | Designing or creating a new Grok Bot (persona, CreateAgent, verify live profile) |
| `design-taste-frontend` | Anti-slop frontend for landings, portfolios, and redesigns (brief inference first) |
| `diagram-design` | Explainer diagrams (architecture, sequence, process) as HTML/SVG/PNG |
| `draft` | Writing or expanding an article section by section (never one-shot the whole piece) |
| `engineering-playbook` | Delegating code to cloud agents and supervising PRs with a design-first bar |
| `exact-match-intent-seo` | Choosing domains, URL slugs, titles, or H1s for exact-match intent SEO |
| `make-bot-ui` | Custom UI that wakes a Grok Bot over a webhook with tap/approve cards |
| `no-ai-slop` | First pass on any text headed for publish — strip AI tells without flattening voice |
| `outline` | Turning a seed, interview, or facts into a writing plan |
| `overheard` | Weekday third-party mention digest voice, sources, and anti-jobs |
| `overheard-setup` | First-run / reconfigure interview for watch list and sources |
| `redesign-existing-projects` | Auditing and upgrading an existing site/app away from generic AI patterns |
| `routine-healthcheck` | Auditing scheduled routines for token waste and noisy empty wakes |
| `show-me` | Opening or rewriting a PR description, or explaining code shape visually |
| `social-copywriting` | Writing or adapting copy for X or LinkedIn |
| `source-check` | After draft, before publish — verify factual claims |
| `top-edit` | Last mechanical pass for AI tells and house-style misses |
| `transcript-healthcheck` | Mining bot transcripts for friction and evidence-backed automation proposals |
| `x-article` | Writing or rewriting an X Article (long-form) with section images |

**Skill count: 22**

## Intentionally excluded

These local skills are **not** published here (personal, employer-locked, or too product-specific):

| Excluded slug | Why |
|---------------|-----|
| `linkedin-post-from-a-source` | Personal / account-tied posting path |
| `gemini-omni-storyboard-commercial` | Product / cast-locked commercial pipeline |
| `sunny-work-account-only-google` | Employer / work-account only |
| `google-chat-work-path` | Employer chat path |
| `executive-visual-overview` | Internal / non-portable briefing format |
| `reddit-morning-paste-expiry` | Personal schedule / paste workflow |
| `taste-skill-frontend` | Superseded / overlapping with `design-taste-frontend` |
| `chatgpt-images-2-5-consistency` | Product cast / consistency locks unsuitable for a public general playbook |

`chatgpt-images-browser-playbook` **is** included, but only as a **generalized session-only** rewrite (no product cast boards).

## License and attributions

- Licensed under the [MIT License](LICENSE) — Copyright 2026 coolxeo.
- Upstream credits kept in skill bodies where applicable, including:
  - **tasteskill** lineage in `design-taste-frontend` / redesign guidance
  - **humanlayer** `show-me`
  - **cathrynlavery** `diagram-design`
  - **Microsoft AEO** PDF guidance referenced by AEO/GEO site work
  - Writing-skill adaptations noted in coach / draft / outline / source-check / top-edit sources

## Scrub checklist for contributors

```bash
P=$(python3 -c "print('|'.join([
  'Dan'+'i','Dan'+'iel Garcia','coolxeo'+'@','devo'+'team',
  'Little '+'Acorn','Soft '+'Explorer','Chest'+'nut','Count '+'To Ten',
  'little'+'acornnest','Torre'+'molinos','Aco'+'sta']))")
rg -n -i "$P" .
```

Expect **zero** hits. Also avoid employer domains, private repo names, and personal calendar slots. Full list in [CONTRIBUTING.md](CONTRIBUTING.md).

## Changelog

### v0.1.0 — 2026-09-13

- Initial public release of scrubbed portable Grok Bot skills.
- 21 core skills plus generalized `chatgpt-images-browser-playbook`.
- README, MIT license, and contributor scrub checklist.
