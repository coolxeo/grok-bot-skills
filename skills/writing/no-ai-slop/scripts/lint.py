#!/usr/bin/env python3
"""lint.py: flag AI-writing tells in a draft. Detect only. It never edits.

Part of the no-ai-slop skill (github.com/coolxeo/grok-bot-skills). MIT.
No dependencies beyond Python 3.

Usage:
  python3 scripts/lint.py FILE [--blocks] [--x] [--linkedin] [--skill PATH] [--json]

  --blocks  lint only fenced ``` blocks (each block = one post or comment).
            Use it on draft files that mix notes and copy.
  --x       X post checks too: 280-char limit (links count 23), link in the
            block, hashtag count, and the house rule of no trailing period.
  --linkedin  LinkedIn house rules: no hyphens in the body, no trailing period.
  --skill   SKILL.md to read the word lists from (default: ../SKILL.md).

Levels: HARD = fix before publishing. SOFT = look again; may be fine.
Exit code 1 if any HARD flag. A flag is evidence to check, not proof that AI
wrote the text. Quoted examples inside "..." are not exempt, so expect hits
when you lint a file that talks about slop.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_PATHS = [os.path.join(HERE, "..", "SKILL.md"), os.path.join(HERE, "SKILL.md")]

ADVERBS_EMPTY_FALLBACK = "just, literally, honestly, simply, actually, truly"

# Fallback watch list; the "Watch list" line in SKILL.md wins when present.
CLUSTER_WORDS = ["quietly", "steady", "practical", "dependable", "clearer",
                 "prioritize", "universally", "echoed", "matters", "crucial",
                 "key", "landscape", "highlight", "highlighting", "underscore",
                 "underscores", "showcase", "showcasing", "enhance", "valuable",
                 "align with", "additionally", "real", "actual", "genuine",
                 "honest", "honestly"]

LAZY_EXTREMES = ["never", "always", "every", "everyone", "nobody", "everything"]

CHAT_RESIDUE = ["i hope this helps", "great question", "you're absolutely right",
                "let me know if", "would you like", "happy to help", "certainly!",
                "of course!", "fair point", "good question", "great point"]

STAGED = [r"here'?s (the thing|what|why|how)", r"let'?s (dive|break|explore)",
          r"the (real|uncomfortable) truth", r"let that sink in", r"read that again",
          r"plot twist", r"think about it", r"what nobody tells you",
          r"the part (most people|everyone) (skip|miss)", r"to be clear",
          r"don'?t get me wrong", r"i'?m not saying", r"real talk"]

QUALIFIED = set()  # words listed with a qualifier, e.g. "landscape (abstract)"

def _items(s):
    s = re.sub(r"\([^)]*\)", "", s)
    return [t.strip().strip(".").lower() for t in s.split(",") if t.strip().strip(".")]

def load_lists(skill):
    """Read word lists from SKILL.md. Returns (banned, phrases, adverbs, watch, path)."""
    paths = [skill] if skill else SKILL_PATHS
    for p in paths:
        if p and os.path.isfile(p):
            body = open(p, encoding="utf-8").read()
            fav = re.search(r"Model favorites:\s*(.+?)\.\s*$", body, re.M)
            fil = re.search(r"Filler phrases:\s*(.+?)\.\s*(?:Shorten|Cut)", body)
            adv = re.search(r"Empty intensifiers \(([^)]*)\)", body)
            wat = re.search(r"Watch list[^:]*:\s*(.+?)\.\s", body)
            if fav:
                QUALIFIED.update(m.strip().lower() for m in re.findall(r"([\w -]+?)\s*\(", fav.group(1)))
                watch = []
                if wat:
                    watch = [w.replace("and the newer set seen in 2026 model output:", "").strip()
                             for w in _items(wat.group(1).replace(":", ","))]
                    watch = [w.replace("and ", "", 1) if w.startswith("and ") else w for w in watch]
                    watch = [w for w in watch if w and len(w.split()) <= 2]
                return (_items(fav.group(1)), _items(fil.group(1)) if fil else [],
                        _items(adv.group(1)) if adv else _items(ADVERBS_EMPTY_FALLBACK),
                        watch or CLUSTER_WORDS, p)
    return [], [], _items(ADVERBS_EMPTY_FALLBACK), CLUSTER_WORDS, "none"

def norm(s):
    return s.replace("\u2019", "'").replace("\u2018", "'").lower()

def has(text, phrase):
    return re.search(r"(?<![a-z])" + re.escape(phrase) + r"(?![a-z])", text) is not None

def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]

def words(s):
    return re.findall(r"[A-Za-z0-9€$%'./<>=\"-]+", s)

URL = re.compile(r"https?://\S+")

def units_from(text, blocks):
    lines = text.splitlines()
    if not blocks:
        return [(1, text)]
    out, cur, start, inside = [], [], 0, False
    for i, l in enumerate(lines, 1):
        if l.strip().startswith("```"):
            if inside:
                out.append((start, "\n".join(cur)))
                cur, inside = [], False
            else:
                inside, start = True, i + 1
            continue
        if inside:
            cur.append(l)
    return out

def lint_unit(start, text, lists, xmode, lmode=False):
    banned, phrases, adverbs, watch, _ = lists
    flags = []
    def add(level, check, ln, quote, fix):
        flags.append(dict(level=level, check=check, line=ln, quote=quote.strip()[:120], fix=fix))
    lines = text.splitlines()
    for off, raw in enumerate(lines):
        ln = start + off
        l = URL.sub("", raw)
        if not l.strip() or l.lstrip().startswith("#"):
            continue
        n = norm(l)
        if "\u2014" in l or "\u2013" in l or re.search(r"\s--\s", l):
            add("HARD", "em-dash", ln, raw, "use a period, comma or line break")
        for b in banned:
            if has(n, b):
                lvl = "SOFT" if b in QUALIFIED else "HARD"
                add(lvl, "model-favorite", ln, raw, f"cut or replace '{b}'")
        for p in phrases:
            if has(n, p):
                add("SOFT", "empty-phrase", ln, raw, f"cut '{p}' unless it is the writer's voice")
        for a in adverbs:
            if has(n, a):
                add("SOFT", "empty-adverb", ln, raw, f"'{a}': keep only if it carries meaning")
        for c in CHAT_RESIDUE:
            if has(n, c.rstrip("!")):
                add("HARD", "chat-residue", ln, raw, "remove the chatbot wrapper")
        for s in STAGED:
            if re.search(r"(?<![a-z])" + s, n):
                add("HARD", "staged-opener", ln, raw, "cut the run-up, state the point")
        # Binary contrast family.
        if re.search(r"\b(is|was|it's|that's|isn't|wasn't)\s+not\b[^.?!\n]{0,50}[.,;]\s*(it's|it is|it was|but|that's)\b", n) \
           or re.search(r"\bnot (just|only|merely)\b[^.?!\n]{0,60}\bbut\b", n) \
           or re.search(r"\b(isn't|aren't|wasn't)\b[^.?!\n]{0,40}[.,]\s*(it's|they're|it was)\b", n) \
           or re.search(r"\bthe (question|answer|problem|point|issue) isn't\b", n):
            add("HARD", "binary-contrast", ln, raw, "state the positive claim directly")
        if re.search(r"\bwould rather\b[^.?!\n]*\bthan\b", n):
            add("SOFT", "rather-moral", ln, raw, "'I would rather X than Y' moral; often a kicker, keep only if it is the point")
        if re.search(r"\b(does not|doesn't|did not|didn't|do not|don't|is not|isn't|never) [^.,;\n]{1,40}, (it|they|we|i|the \w+) (just )?\w+", n):
            add("SOFT", "contrast-splice", ln, raw, "'does not X, it Y' splice; say what it does")
        if re.search(r"\brather than\b", n):
            add("SOFT", "rather-than", ln, raw, "Y-rather-than-X contrast; keep only if X is a real belief")
        if re.search(r"[a-z0-9], (never|not|no) [a-z]+[^,.]{0,30}($|[.])", n):
            add("SOFT", "clipped-negative-tail", ln, raw, "', never X' tail; say what happens instead")
        if re.search(r"\b(the|my|our|your) [a-z ]{0,30}(is|are|was) where\b", n) or re.search(r"\bthat'?s where\b", n):
            add("SOFT", "faux-insight-frame", ln, raw, "'X is where Y' framing; state Y")
        if re.search(r"\b(two|three|four|2|3|4) (things|lessons|rules|ways|steps|mistakes)\b", n):
            add("SOFT", "announced-count", ln, raw, "count announced before the list; just give the items")
        # Colon reveal: short lead-in, colon, lowercase clause (not a label list, time or URL).
        for m in re.finditer(r"(^|[.!?]\s+)([A-Za-z][^:\n]{2,45}):\s+([a-z][^\n]{3,})", l):
            lead = m.group(2)
            if re.search(r"\d$", lead) or len(lead.split()) > 8 or len(m.group(3).split()) < 2:
                continue
            add("HARD", "colon-reveal", ln, raw, "rewrite as one plain sentence")
            break
        if re.match(r"\s*(this|that) (is|was)\b", n):
            add("SOFT", "demonstrative-opener", ln, raw, "'This/That is' with no noun; name the thing")
        for w in LAZY_EXTREMES:
            if has(n, w) and not re.search(r"\bevery \d", n):
                add("SOFT", "lazy-extreme", ln, raw, f"'{w}': true? else give the number")
        if re.search(r"\b(honest|honestly|real|actual|genuine) (shape|answer|number|work|value|reason)\b", n):
            add("SOFT", "moral-or-real-adjective", ln, raw, "drop 'honest/real/actual' before the noun")
        if re.search(r"[“”‘’]", raw):
            add("SOFT", "curly-quotes", ln, raw, "use straight quotes if the target uses them (weak alone)")
        if re.search(r"\?\s+[A-Z0-9][^?]{0,60}[.!]", l) and len(words(l)) < 30:
            add("SOFT", "self-answered-question", ln, raw, "drop the question, keep the answer as a claim")
    # Unit-level checks.
    body = URL.sub("", text)
    sents = [s for s in sentences(body) if not s.startswith("#")]
    lens = [len(words(s)) for s in sents]
    run = 0
    for i, k in enumerate(lens):
        run = run + 1 if 0 < k <= 4 else 0
        if run == 3:
            add("SOFT", "staccato-run", start, " / ".join(sents[i-2:i+1]), "3+ fragments in a row; merge into a sentence")
    if len(sents) >= 2 and 0 < lens[-1] <= 5:
        add("SOFT", "short-closer", start, sents[-1], "short last line; cut if it restates or is a mic-drop")
    if len(sents) >= 2:
        last2 = sents[-2:]
        if all(len(words(s)) <= 5 for s in last2) and len(last2) == 2:
            a, b = [words(s) for s in last2]
            if a and b and (a[0].lower() in ("you", "your", "i", "we", "it") or b[0].lower() in ("you", "your", "i", "we")):
                add("HARD", "parallel-kicker", start, " ".join(last2), "'Your agent X. You Y.' mic-drop; end on the concrete line before it")
    tri = re.findall(r"\b\w+(?: \w+){0,3}, \w+(?: \w+){0,3},? (?:and|or) \w+", norm(body))
    if len(tri) >= 2:
        add("SOFT", "triads", start, "; ".join(tri[:3]), f"{len(tri)} lists of three; keep one, cut or merge the rest")
    nb = norm(body)
    hits = [w for w in watch if has(nb, w)]
    if len(hits) >= 3:
        add("SOFT", "ai-vocab-cluster", start, ", ".join(hits), "3+ watch words in one piece; replace the weakest")
    if len(lens) >= 4 and max(lens) - min(lens) <= 3:
        add("SOFT", "flat-rhythm", start, f"sentence lengths {lens}", "vary sentence length")
    last = [l for l in text.strip().splitlines() if l.strip() and not re.match(r"\s*(#\w+\s*)+$", l)]
    if (xmode or lmode) and last and URL.sub("", last[-1]).rstrip().endswith("."):
        tl = text.splitlines()
        idx = max(i for i, l in enumerate(tl) if l.strip() == last[-1].strip())
        add("HARD", "trailing-period", start + idx, last[-1], "house rule: no period on the last line of a social post")
    if lmode:
        for off, raw in enumerate(text.splitlines()):
            if re.search(r"[A-Za-z]-[A-Za-z]", URL.sub("", raw)):
                add("HARD", "linkedin-hyphen", start + off, raw, "house rule: no hyphens in LinkedIn body")
    if xmode:
        xlen = len(URL.sub("x" * 23, text))
        if xlen > 280:
            add("HARD", "x-length", start, f"{xlen} chars", "cut to 280 (links count 23)")
        if URL.search(text):
            add("SOFT", "x-link", start, URL.search(text).group(0), "link in this block; fine if it is the reply that carries the link")
        if len(re.findall(r"(?<!\w)#\w+", text)) > 2:
            add("SOFT", "x-hashtags", start, "", "0-2 hashtags")
    return flags

def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    path = args[0]
    skill = args[args.index("--skill") + 1] if "--skill" in args else None
    lists = load_lists(skill)
    text = open(path, encoding="utf-8").read()
    allf = []
    for start, unit in units_from(text, "--blocks" in args):
        for f in lint_unit(start, unit, lists, "--x" in args, "--linkedin" in args):
            allf.append(f)
    if "--json" in args:
        print(json.dumps(dict(file=path, lists=lists[4], flags=allf), indent=1))
    else:
        print(f"# lint {path} (lists from {lists[4]})")
        for f in allf:
            print(f"{f['level']:4} L{f['line']:<4} {f['check']:24} \"{f['quote']}\" -> {f['fix']}")
        h = sum(f['level'] == 'HARD' for f in allf)
        print(f"# {h} HARD, {len(allf) - h} SOFT")
    sys.exit(1 if any(f['level'] == 'HARD' for f in allf) else 0)

if __name__ == "__main__":
    main()
