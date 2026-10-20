"""Write learn/practise/evidence into track t03's item tuples, idempotently.

Slots 0-2 (text, meta, tag) are copied through byte for byte, because idFor()
hashes the group title and the item text: reword either and every grade for
that item is orphaned. Only slots 3, 4 and 5 are rewritten.

Matching is by item text, never by index. The first version of this script
matched by position and silently mis-assigned 225 sources when one item line
failed to parse, so: every item must either match a key or be reported.
"""
import re, sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from python_table import DATA

HTML = pathlib.Path(__file__).resolve().parents[2] / "master-tracker.html"


def find_close(s, i):
    """Index of the ] closing the [ at s[i], skipping bracket chars in strings."""
    depth, j, q = 0, i, None
    while j < len(s):
        c = s[j]
        if q:
            if c == "\\":
                j += 2
                continue
            if c == q:
                q = None
        elif c in "\"'":
            q = c
        elif c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    raise ValueError("unbalanced [ at %d" % i)


def split_top(s):
    """Split a tuple body on top-level commas, string-aware."""
    out, buf, depth, q = [], "", 0, None
    for c in s:
        if q:
            buf += c
            if c == q:
                q = None
            continue
        if c in "\"'":
            q = c; buf += c; continue
        if c in "[{(":
            depth += 1
        elif c in "]})":
            depth -= 1
        if c == "," and depth == 0:
            out.append(buf); buf = ""
        else:
            buf += c
    if buf.strip():
        out.append(buf)
    return [x.strip() for x in out]


def lit(v):
    return "null" if v is None else '"' + v + '"'


def main():
    src = HTML.read_text(encoding="utf-8")

    start = src.index('{id:"t03"')
    end = src.index('/* ================= 03 ================= */', start)
    block = src[start:end]

    lines = block.split("\n")
    matched, unmatched, used = 0, [], set()

    for n, line in enumerate(lines):
        stripped = line.lstrip()
        if not stripped.startswith('["'):
            continue
        i = line.index("[")
        j = find_close(line, i)
        parts = split_top(line[i + 1:j])
        text = parts[0]

        key = next((k for k in DATA if k in text), None)
        if not key:
            unmatched.append(text[:70])
            continue
        used.add(key)
        learn, prac, ev = DATA[key]

        keep = (parts + ["null", "null", "null"])[:3]
        keep = [p if p else "null" for p in keep]
        body = ",".join(keep + [lit(learn), lit(prac), lit(ev)])
        lines[n] = line[:i] + "[" + body + "]" + line[j + 1:]
        matched += 1

    out = src[:start] + "\n".join(lines) + src[end:]
    HTML.write_text(out, encoding="utf-8")

    print("items rewritten: %d" % matched)
    print("keys unused    : %s" % sorted(set(DATA) - used))
    print("items unmatched: %s" % unmatched)


if __name__ == "__main__":
    main()
