# coach

Review a draft's argument and structure before line edits. The writer keeps the pen.

Use this when a draft needs a structural read before line-edit: thesis, arc, and teach test first, style second.

## Install

```sh
npx skills add botkitsdev/botkits --skill coach
```

To list the 31 skills in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it.

## What it does

- Asks only the questions the draft and chat do not already answer: who the reader is and what they know, where the piece will run, and what the reader should do or believe afterwards. The answers set the bar.
- Writes a reverse outline (one line per paragraph). Then answers three gate questions: can you say the thesis in one sentence, does each paragraph need the one before it, and is every load-bearing claim backed. Any "no" ends the review, reports the failures, and sends the writer back to outline or draft.
- If the gate passes, scores seven axes from 1 to 5 (Entry, Build, Voice, Evidence, Takeaway, Reach, Pace). 3 is fine and 5 is ready to publish. The total is out of 35.
- The report has the gate result, the score, what already works (quoted), the top three problems with a quoted line and a before/after sketch, and one question for the writer.
- Does not edit the file. Does not rewrite whole sections.

## Before / after (example)

This example starts with a draft that is about to be line-edited. The thesis is hard to state in one sentence. A paragraph does not need the one before it. A load-bearing claim has no fact, example, or source behind it.

After the read you get a reverse outline and a gate result. If any gate question is "no", the review stops there and the writer goes back to outline or draft. The file is not edited. If the gate passes, you get a score out of 35, quoted lines that already work, the top three structural problems with a before/after sketch, and one question for the writer.

## Works with

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [Nadiem Mahmoud's coach](https://github.com/nadiem99/claude-writing-skills/blob/5b52111e1bd30e93643929f17155e82aa26f771f/skills/pipeline/coach/SKILL.md) (MIT, which credits Every's Eleanor Warnock), [Paul Graham's Writing, Briefly](https://www.paulgraham.com/writing44.html), and [George Orwell's Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/). Mahmoud has a structure-first gate and a seven-axis rubric, but is tied to vault folders and judges every piece by an essay arc. This skill adds reader, venue and goal questions, a reverse outline as gate evidence, a "what works" section, and one question for the writer.

License: MIT
