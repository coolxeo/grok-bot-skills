#!/usr/bin/env bash
# Stops paid kit files from landing in this public repo.
# Paid sources live in a private store, never here. See BRAND.md section 9.
set -euo pipefail
fail=0

# 1. The 4 lite skills hold only SKILL.md and README.md.
for d in skills/writing/x-article skills/seo/aeo-geo-site skills/video/shorts-reframe skills/seo/markdown-twin; do
  [ -d "$d" ] || continue
  extra=$(find "$d" -type f ! -name SKILL.md ! -name README.md)
  if [ -n "$extra" ]; then echo "Paid guard: $d is a lite skill. Only SKILL.md and README.md may live here:"; echo "$extra"; fail=1; fi
done

# 2. File names that exist only in the paid kits.
hits=$(git ls-files | grep -E '(^|/)(aeo_check\.py|shortkit\.py|negotiate\.mjs|make-watch-page\.mjs|watch\.json|wrangler\.example\.jsonc|scoring-rubric\.md|audit-checklist\.md|article-skeleton\.md|prepublish-checklist\.md|TEST-RESULTS\.md|worked-audit\.md|worked-example\.md|ai-crawlers\.md|audit-report\.md|page-brief\.md|image-plan\.md|promo-post\.md|sample-contact-sheet\.png|sample-frame-[^/]*)$|(^|/)(fixture-site|jsonld|router|watch-page|shorts-builder|aeo-kit|shorts-kit|paid-sources)/' || true)
if [ -n "$hits" ]; then echo "Paid guard: these paths match paid kit files:"; echo "$hits"; fail=1; fi

# 3. No Gumroad link in any SKILL.md.
g=$(git ls-files '*SKILL.md' | xargs grep -l -i 'gumroad' || true)
if [ -n "$g" ]; then echo "Paid guard: Gumroad link in SKILL.md:"; echo "$g"; fail=1; fi

[ "$fail" -eq 0 ] && echo "Paid guard: clean."
exit "$fail"
