# storytelling-hooks

Write a hook from a fact you already have, or build a swipe-file carousel people can save and reuse.

For writers and operators who need a first line that names a real story, or a reference carousel that readers bookmark.

## Install

```sh
npx skills add botkitsdev/botkits --skill storytelling-hooks
```

To list the 32 skills in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Picks a hook family from a fact you already have (a date, a cost, a client question, a rule you follow).
- Drafts 3 hooks from 2 or 3 families, keeps 1, and checks that the rest of the post can pay off that line.
- Fills every blank with a real fact. If a fact is missing, it changes family instead of inventing one.
- When the job is a swipe-file carousel: plans a one-line post that ends in a colon, a cover slide, and content slides with one named group, a "use when" line, and 6 to 8 numbered templates.
- Uses BotKits visual tokens for any carousel artwork, and our own templates rather than another writer's lines.

## Before and after (example)

This example starts with a topic and no fact in the first line: "Some notes on how my writing process improved this year." The reader cannot tell what changed, or whether the post will pay off.

After the pass, the chosen hook (Lesson family) is:

```text
2 years of weekly posts left me with one rule: finish the outline before any sentence.
```

The two unused options came from Transformation and Mistake. The body then has to deliver that one rule. For a carousel job, the post text would be a headline plus a colon, and each slide would keep the same row count.

## Works with

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Pattern library: [references/patterns.md](references/patterns.md)
- Source table: [references/swipe-file-carousel-analysis.md](references/swipe-file-carousel-analysis.md)
- Inspired by: [Chase Dimond's 80 Storytelling Hooks](https://x.com/ecomchasedimond/status/2122793870669062451) and the 11 other save-first posts listed in [SKILL.md](SKILL.md#inspired-by). This skill adds why each family works, our own templates, a fact rule for every blank, a check that the body pays off the hook, and a carousel procedure that uses BotKits visual tokens.

License: MIT
