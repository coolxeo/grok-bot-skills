# Contributing

Thanks for improving portable Grok Bot skills.

## What belongs here

- One job per skill. Short `SKILL.md` with YAML frontmatter (`name`, `description`) and a body an agent can follow.
- Portable guidance: no personal names, emails, account IDs, live calendars, employer internals, or product cast locks.
- Keep upstream credits when you adapt someone else's work.

## Scrub checklist (required before PR)

Run from the repo root. Build the pattern from parts so this file does not contain the forbidden tokens as contiguous text, then expect **zero** hits:

```bash
P=$(python3 -c "print('|'.join([
  'Dan'+'i','Dan'+'iel Garcia','coolxeo'+'@','devo'+'team',
  'Little '+'Acorn','Soft '+'Explorer','Chest'+'nut','Count '+'To Ten',
  'little'+'acornnest','Torre'+'molinos','Aco'+'sta','Costa '+'Garden',
  'fleet '+'rule']))")
rg -n -i "$P" .
```

Also manually scan for:

- Personal emails and phone numbers
- Employer / client names and private repo names
- Family names
- Personal timezone slots or home addresses
- Product-specific character sheets, cast boards, or material locks baked into a general playbook
- Duplicate YAML frontmatter blocks at the top of a `SKILL.md`

## Skill shape

```markdown
---
name: Short Title
description: >-
  Use when … (when-to-use line agents match against)
---
# Short Title

Body…
```

- Prefer one leading frontmatter block only (no duplicated `---` / `name:` pairs).
- Cross-link other skills with `sand-workflow:<slug>` when helpful.
- Do not paste secrets, cookies, or API keys into skills.

## PR tips

- Say which skill(s) changed and why.
- Note any upstream attribution updates.
- Keep the README skill index in sync when adding or removing a slug.
