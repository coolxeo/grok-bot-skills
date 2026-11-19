# botkits-motion-picker

Pick one animation library for one motion moment, with its license and a calm, snappy, or playful preset.

Use this when you choose an animation library for a page, a diagram or a short clip, or when you need the preset timing numbers.

## Install

```sh
npx skills add botkitsdev/botkits --skill botkits-motion-picker
```

To list every skill in the repo: `npx skills add botkitsdev/botkits --list`.

No CLI? Copy this folder into the skills folder your agent uses, and keep `SKILL.md` inside it. Copy the skill folder itself, not the category folder.

## What it does

- Allows one motion moment per page, or none. It always respects `prefers-reduced-motion`.
- Uses three fixed presets. calm is the default: 420 ms, cubic-bezier(0.33, 0, 0.2, 1), spring stiffness 140 and damping 24. snappy and playful are used only when the user asks.
- Maps one need to one library from a table of 20, with the license read from each repo's LICENSE file on 14 Nov 2026, or `unverified` when that file is absent.
- Flags license traps for GSAP, Remotion, Theatre.js, p5.js and Typed.js.
- Marks Lenis "avoid by default" (no scroll hijacking). It keeps video to short clips joined with fades, with no zoom-in or push-in, and keeps gif, mp4, webm and rendered png files out of git.

## Before / after (example)

### Before

A page fades and slides every section in. Two animation libraries are installed for the same job, and nobody checked their licenses. The motion still runs when the visitor asks for reduced motion.

### After

The answer names the need, one library, the calm preset and that library's license, with any trap that applies. Only one moment on the page moves. With reduced motion on, the page shows the end state.

## Use it in

- Used daily: Grok Bot.
- Installs with `npx skills add` (tested 18 Nov 2026): Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and Grok Build.
- Supports the SKILL.md format (vendor docs): Claude apps (upload), ChatGPT (Business, Enterprise, Edu, Healthcare upload), and the other clients listed at [agentskills.io](https://agentskills.io/clients).
- Other agents that support the Agent Skills format can load it. We have not run it there.
- No direct install yet in ChatGPT dots or Meta Muse. Paste the instructions from [SKILL.md](SKILL.md) into a chat.

| Agent | Put this folder here |
| --- | --- |
| Grok Bot | Paste [SKILL.md](SKILL.md) in a 1:1 chat and ask the Bot to save it as a skill. |
| Claude Code | `.claude/skills/botkits-motion-picker/` or `~/.claude/skills/botkits-motion-picker/` |
| Codex | `.agents/skills/botkits-motion-picker/` or `~/.agents/skills/botkits-motion-picker/` |
| Cursor | `.agents/skills/botkits-motion-picker/` or `.cursor/skills/botkits-motion-picker/` |
| Gemini CLI | `.gemini/skills/botkits-motion-picker/` or `.agents/skills/botkits-motion-picker/` (one folder deep only) |
| GitHub Copilot | `.github/skills/botkits-motion-picker/` or `.agents/skills/botkits-motion-picker/` |
| Grok Build | `.grok/skills/botkits-motion-picker/` or `~/.grok/skills/botkits-motion-picker/` |
| Claude apps | Turn on code execution. ZIP this folder and upload it in Customize, Skills. |

Install tested is not run tested.

## Links

- [botkits.dev](https://botkits.dev)
- Instructions: [SKILL.md](SKILL.md)
- Inspired by: [N01ennn's post](https://x.com/N01ennn/status/2121695892738629808) naming 20 animation libraries, and the LICENSE file in each of those repos. The links are in [SKILL.md](SKILL.md#inspired-by). This skill adds one need to one library, fixed preset numbers, and the license traps.

License: MIT
