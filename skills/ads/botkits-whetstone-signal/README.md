# botkits-whetstone-signal

Pick, score, and send back the conversion event that automated ad campaigns optimize for.

Use this when Meta Advantage+, Google Performance Max, Google Demand Gen, or a similar campaign brings cheap leads that rarely turn into revenue. Also use it when you set up a new automated campaign and must choose what to optimize for.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-whetstone-signal
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it. Copy the skill folder itself, not the category folder.

## What it does

- Asks for your funnel counts from your own backend for the last 4 to 8 weeks, your tracking and your consent setup before it recommends anything.
- Runs a volume check. The platform needs about 50 optimization events a week per campaign (or per ad set on Meta). It picks the deepest stage that clears that bar, or attaches a value to a shallower one.
- Writes one qualified event as a rule that sales and engineering read the same way. It can add one self-qualify question to the form and build a first-party engagement score.
- Sends the qualified result back through the Meta Conversions API or Google offline conversions and enhanced conversions. It changes one campaign first and keeps a holdout.
- Compares platform counts with backend counts each week and judges success on backend numbers only.
- Never uses broker data, sensitive traits, or personal data on content made for children. Includes a [qualified event spec](qualified-event-spec.md) template.

## Before / after (example)

### Before

A plumber runs Meta Advantage+ lead ads. Many leads live outside the service area or want a job the business does not do. The campaign optimizes for every lead, with no value attached.

### After

The form asks for the postcode. A qualified lead is inside the service area and asks for a job on the list. That is about 40 a week, under the bar of 50, so the campaign still optimizes for all leads. Each lead goes back through the Conversions API with a value: 0 out of area, 50 in area, 150 in area with a booked visit. Existing customers are excluded with a consented list. Booked jobs in the job system are compared with the Meta lead count each week. This is the local services example from [SKILL.md](SKILL.md).

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-whetstone-signal/` or `~/.claude/skills/botkits-whetstone-signal/` |
| Codex | `.agents/skills/botkits-whetstone-signal/` or `~/.agents/skills/botkits-whetstone-signal/` |
| Cursor | `.agents/skills/botkits-whetstone-signal/` or `.cursor/skills/botkits-whetstone-signal/` |
| Gemini CLI | `.gemini/skills/botkits-whetstone-signal/` or `.agents/skills/botkits-whetstone-signal/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-whetstone-signal/` or `.agents/skills/botkits-whetstone-signal/` |
| Grok Build | `.grok/skills/botkits-whetstone-signal/` or `~/.grok/skills/botkits-whetstone-signal/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Template: [qualified-event-spec.md](qualified-event-spec.md)
- Inspired by: the origin of this skill is unresolved. See the [credits table](../../../docs/credits.md).

License: MIT
