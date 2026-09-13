# grok-bot-skills

Portable **Grok Bot** skills (`SKILL.md`) for public use.

> Not affiliated with Cursor or xAI.

This pack is clean of personal-project specifics (no private brands, accounts, or personal ops).

## What a Grok Bot skill is

A skill is a folder with a `SKILL.md` file:

1. **YAML frontmatter** — at least `name` and `description` (the when-to-use line agents match against).
2. **Markdown body** — standing instructions the bot follows when the skill is invoked.

Skills are grouped under `skills/<category>/<slug>/` for browsing. The **slug** (leaf kebab folder name) is the durable id — invoke with `/` or `@` plus that slug, and cross-link with `sand-workflow:<slug>`.

## Install

1. Copy the skill folders you want into your Grok Bot workflows directory (typically under the agent workflows / skills path your bot already uses). You can copy a whole category or individual `<slug>` folders.
2. Invoke with `/` or `@` plus the skill slug (for example `/no-ai-slop` or `@design-a-grok-bot`), depending on your Grok Bot UI.
3. Prefer **one job per skill**. Do not merge unrelated playbooks into a single file.

## Ethos

- **One job.** Each skill does one thing and refuses adjacent work.
- **Anti-slop.** Prefer concrete, short, verified prose over generic AI filler. Start publishing text with `no-ai-slop`.
- **Portable.** Skills here stay general and reusable.

## Skill index

### Writing — `skills/writing/`

| Slug | When to use |
|------|-------------|
| `coach` | Structural read of a draft before line-edit (thesis, arc, teach test) |
| `draft` | Writing or expanding an article section by section (never one-shot the whole piece) |
| `outline` | Turning a seed, interview, or facts into a writing plan |
| `source-check` | After draft, before publish — verify factual claims |
| `top-edit` | Last mechanical pass for AI tells and house-style misses |
| `no-ai-slop` | First pass on any text headed for publish — strip AI tells without flattening voice |
| `social-copywriting` | Writing or adapting copy for X or LinkedIn |
| `x-article` | Writing or rewriting an X Article (long-form) with section images |

### Engineering — `skills/engineering/`

| Slug | When to use |
|------|-------------|
| `engineering-playbook` | Delegating code to cloud agents and supervising PRs with a design-first bar |
| `show-me` | Opening or rewriting a PR description, or explaining code shape visually |

### SEO — `skills/seo/`

| Slug | When to use |
|------|-------------|
| `aeo-geo-site` | Building or updating a site for SEO plus AEO/GEO so assistants can cite it cleanly |
| `exact-match-intent-seo` | Choosing domains, URL slugs, titles, or H1s for exact-match intent SEO |

### Design — `skills/design/`

| Slug | When to use |
|------|-------------|
| `design-taste-frontend` | Anti-slop frontend for landings, portfolios, and redesigns (brief inference first) |
| `redesign-existing-projects` | Auditing and upgrading an existing site/app away from generic AI patterns |
| `diagram-design` | Explainer diagrams (architecture, sequence, process) as HTML/SVG/PNG |

### Bots — `skills/bots/`

| Slug | When to use |
|------|-------------|
| `design-a-grok-bot` | Designing or creating a new Grok Bot (persona, CreateAgent, verify live profile) |
| `make-bot-ui` | Custom UI that wakes a Grok Bot over a webhook with tap/approve cards |
| `routine-healthcheck` | Auditing scheduled routines for token waste and noisy empty wakes |
| `transcript-healthcheck` | Mining bot transcripts for friction and evidence-backed automation proposals |
| `overheard` | Weekday third-party mention digest voice, sources, and anti-jobs |
| `overheard-setup` | First-run / reconfigure interview for watch list and sources |

### Images — `skills/images/`

| Slug | When to use |
|------|-------------|
| `chatgpt-images-browser-playbook` | Generating stills on chatgpt.com via signed-in Images 2.5 UI (session-only; one still per dispatch) |

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

## Changelog

### v0.2.0 — 2026-09-13

- Removed `CONTRIBUTING.md` and scrub / contributor-process language from the README.
- Reorganized skills into category folders (`writing`, `engineering`, `seo`, `design`, `bots`, `images`) while keeping leaf kebab slugs.
- Updated the README skill index for category browsing; `sand-workflow:<slug>` still targets leaf slugs.

### v0.1.0 — 2026-09-13

- Initial public release of scrubbed portable Grok Bot skills.
- 21 core skills plus generalized `chatgpt-images-browser-playbook`.
- README, MIT license, and contributor scrub checklist.
