#!/usr/bin/env python3
"""Write per-item learning sources into master-tracker.html.

Two sources of truth, by track:
  * curriculum.py — tracks t03..t11 (the syllabus the user asked to be researched).
    Produced by a 37-agent research + adversarial-verification workflow; carries a
    chapter/lecture/timestamp locator per item.
  * sources.py    — tracks t01 and t12, which that pass did not cover.

Matching is by ITEM TEXT, not by index. An earlier index-based applier skipped
unparsed lines without consuming an index and silently shifted every source after
it, so each one looked plausible and was wrong. Text matching cannot do that: an
unmatched item is reported, not mis-assigned.

Idempotent — strips what it previously wrote before re-applying.
"""
import pathlib, re, sys, html as H
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from curriculum import CURRICULUM
from sources import SRC, DSA_SRC

TRACKER = HERE.parent.parent / "master-tracker.html"
CURRICULUM_TRACKS = set(CURRICULUM)

def scan(s, start):
    depth = 0; i = start; instr = esc = False
    while i < len(s):
        c = s[i]
        if instr:
            if esc: esc = False
            elif c == "\\": esc = True
            elif c == '"': instr = False
        else:
            if c == '"': instr = True
            elif c in "[{(": depth += 1
            elif c in "]})":
                depth -= 1
                if depth == 0: return i + 1
        i += 1
    return -1

def split_top(body):
    out = []; depth = i = start = 0; instr = esc = False
    while i < len(body):
        c = body[i]
        if instr:
            if esc: esc = False
            elif c == "\\": esc = True
            elif c == '"': instr = False
        else:
            if c == '"': instr = True
            elif c in "[{(": depth += 1
            elif c in "]})": depth -= 1
            elif c == "," and depth == 0: out.append(body[start:i]); start = i + 1
        i += 1
    return out + [body[start:]]

def clean(v):
    """Make a source string safe inside a double-quoted JS literal."""
    return v.replace('"', "'").replace("\\", "/")

QUOTES = str.maketrans({"\u201c": '"', "\u201d": '"', "\u2018": "'", "\u2019": "'",
                        "\u2013": "-", "\u2014": "-"})
def norm(s):
    s = H.unescape(re.sub(r"<[^>]+>", "", s)).translate(QUOTES)
    return re.sub(r"\s+", " ", s).strip().lower()

def main():
    s = TRACKER.read_text()
    # Labels are embedded in a double-quoted JS string literal, so a double quote
    # inside one ends the string and breaks the file. Normalise to single quotes
    # in ONE place, used by both the strip and the write, so they always agree.
    raw_known = {v for m in SRC.values() for v in m.values()} | {DSA_SRC}
    raw_known |= {f'{r["label"]}|{r["url"]}' for rows in CURRICULUM.values() for r in rows}
    known = raw_known | {clean(k) for k in raw_known}
    for k in sorted(known, key=len, reverse=True): s = s.replace(f',"{k}"]', "]")
    s = re.sub(r",null,null\]", "]", s); s = re.sub(r",null\]", "]", s)

    lookup = {tid: {norm(r["item"]): f'{r["label"]}|{r["url"]}' for r in rows}
              for tid, rows in CURRICULUM.items()}

    lines = s.splitlines()
    i0 = next(n for n, l in enumerate(lines) if l.startswith("const TRACKS"))
    j0 = next(n for n, l in enumerate(lines[i0:], i0) if l.strip() == "];")
    cur = None; idx = 0; applied = 0; missed = []
    for n in range(i0, j0):
        raw = lines[n]
        m = re.match(r'\s*\{id:"(t\d\d)", num:', raw)
        if m: cur, idx = m.group(1), 0; continue
        if re.match(r'\s*\{t:"', raw): continue
        lb = raw.find("[")
        if lb < 0 or raw[:lb].strip() or not cur: continue
        end = scan(raw, lb)
        if end < 0: sys.exit(f"unparsed item at line {n+1}")
        parts = split_top(raw[lb+1:end-1])
        this, idx = idx, idx + 1
        text = parts[0].strip()
        if text.startswith('"') and text.endswith('"'): text = text[1:-1]

        if cur in CURRICULUM_TRACKS:
            src = lookup[cur].get(norm(text))
            if not src: missed.append((cur, norm(text)[:60])); continue
        else:
            src = SRC.get(cur, {}).get(this)
            if not src: continue

        while len(parts) < 3: parts.append("null")
        if len(parts) != 3: sys.exit(f"{cur}:{this} has {len(parts)} slots")
        lines[n] = raw[:lb] + "[" + ",".join(parts) + f',"{clean(src)}"]' + raw[end:]
        applied += 1

    out = "\n".join(lines) + "\n"
    dsa = {norm(r["item"]): f'{r["label"]}|{r["url"]}' for r in CURRICULUM.get("t11", [])}
    if dsa:
        import json as J
        table = ",".join(f"{J.dumps(k)}:{J.dumps(clean(v))}" for k, v in dsa.items())
        # match `items:by[k]` with or without an existing .map(...) tail
        out, n_sub = re.subn(
            r"items:by\[k\](?:\.map\(\(\[n,pat\]\)=>\[n,pat[^\]]*\]\))?",
            "items:by[k].map(([n,pat])=>[n,pat,null,DSA_SRC[n.toLowerCase()]||null])",
            out, count=1)
        if not n_sub: sys.exit("could not wire DSA_SRC into dsaGroups()")
        if "const DSA_SRC" not in out:
            out = out.replace("function dsaGroups(){",
                              "const DSA_SRC={" + table + "};\nfunction dsaGroups(){", 1)
    TRACKER.write_text(out)
    print(f"  applied {applied} item sources" + (f"  ·  DSA table {len(dsa)}" if dsa else ""))
    if missed:
        print(f"  UNMATCHED {len(missed)} (fix curriculum.py or the item text):")
        for t, x in missed[:15]: print(f"    {t}  {x}")

if __name__ == "__main__":
    main()
