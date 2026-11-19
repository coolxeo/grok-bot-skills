#!/usr/bin/env bash
# Rebuilds the flat skill links that other agents read, from skills/<category>/<name>/.
#   .agents/skills/<name> -> ../../skills/<category>/<name>   (Codex, Cursor, Gemini CLI, GitHub Copilot, Muse Code)
#   .claude/skills        -> ../.agents/skills                (Claude Code)
# Run with --check in CI: it fails if a link is missing, broken or stale.
set -euo pipefail
cd "$(dirname "$0")/../.."
check=0; [ "${1:-}" = "--check" ] && check=1
want=$(mktemp); trap 'rm -f "$want"' EXIT
for f in skills/*/*/SKILL.md; do d=$(dirname "$f"); echo "$(basename "$d") ../../$d"; done | sort > "$want"
dups=$(cut -d' ' -f1 "$want" | uniq -d)
[ -z "$dups" ] || { echo "Skill links: two skills share a folder name: $dups"; exit 1; }
if [ "$check" -eq 1 ]; then
  have=$(for l in .agents/skills/*; do [ -L "$l" ] && echo "$(basename "$l") $(readlink "$l")"; done | sort)
  [ "$have" = "$(cat "$want")" ] || { echo "Skill links are out of date. Run .github/scripts/skill-links.sh"; diff <(echo "$have") "$want" || true; exit 1; }
  for l in .agents/skills/*; do [ -f "$l/SKILL.md" ] || { echo "Skill links: broken link $l"; exit 1; }; done
  [ "$(readlink .claude/skills)" = "../.agents/skills" ] || { echo "Skill links: .claude/skills must link to ../.agents/skills"; exit 1; }
  echo "Skill links: in sync ($(wc -l < "$want") skills)."; exit 0
fi
rm -rf .agents/skills; mkdir -p .agents/skills .claude
while read -r name target; do ln -s "$target" ".agents/skills/$name"; done < "$want"
ln -sfn ../.agents/skills .claude/skills
echo "Skill links: wrote $(wc -l < "$want") links."
