#!/usr/bin/env python3
"""Write the per-item sources from sources.py into master-tracker.html.

Items are [text, meta, tag] and gain a 4th slot. Two things this gets right
that a naive pass does not:

  * the index advances for EVERY item line, matched or not. Skipping a line
    without consuming an index shifts every source after it, which is silent
    and produces confidently wrong pairings.
  * the end of an item is found with a string-aware bracket scan, not a regex.
    Item lines end variously in `],` `]},` and `]]},`, and the text contains
    brackets and escaped quotes.

Idempotent: run it as often as you like. It strips any sources it previously
wrote before re-applying, so sources.py stays the single source of truth.
"""
import pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from sources import SRC, DSA_SRC

TRACKER = HERE.parent.parent / "master-tracker.html"

def scan(s, start):
    depth = i = 0; instr = esc = False; i = start
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

def main():
    s = TRACKER.read_text()
    known = {v for m in SRC.values() for v in m.values()} | {DSA_SRC}
    for k in known: s = s.replace(f',"{k}"]', "]")
    s = re.sub(r",null,null\]", "]", s)
    s = re.sub(r",null\]", "]", s)

    lines = s.splitlines()
    i0 = next(n for n, l in enumerate(lines) if l.startswith("const TRACKS"))
    j0 = next(n for n, l in enumerate(lines[i0:], i0) if l.strip() == "];")
    cur = None; idx = 0; applied = 0
    for n in range(i0, j0):
        raw = lines[n]
        m = re.match(r'\s*\{id:"(t\d\d)", num:', raw)
        if m: cur, idx = m.group(1), 0; continue
        if re.match(r'\s*\{t:"', raw): continue
        lb = raw.find("[")
        if lb < 0 or raw[:lb].strip() or not cur: continue
        end = scan(raw, lb)
        if end < 0: sys.exit(f"unparsed item at line {n+1}")
        this, idx = idx, idx + 1
        src = SRC.get(cur, {}).get(this)
        if not src: continue
        parts = split_top(raw[lb+1:end-1])
        while len(parts) < 3: parts.append("null")
        if len(parts) != 3: sys.exit(f"{cur}:{this} has {len(parts)} slots")
        lines[n] = raw[:lb] + "[" + ",".join(parts) + f',"{src}"]' + raw[end:]
        applied += 1

    out = "\n".join(lines) + "\n"
    out = re.sub(r"(return order\.map\(k=>\(\{t:k, items:by\[k\])\)",
                 rf'\1.map(([n,pat])=>[n,pat,null,"{DSA_SRC}"]))', out, count=1)
    TRACKER.write_text(out)
    print(f"applied {applied} item sources (+30 DSA)")

if __name__ == "__main__":
    main()
