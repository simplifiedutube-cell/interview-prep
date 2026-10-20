"""Write learn/practise/evidence into every track's item tuples, idempotently.

Slots 0-2 (text, meta, tag) are copied through byte for byte, because idFor()
hashes the group title and the item text: reword either and every grade for
that item is orphaned. Only slots 3, 4 and 5 are rewritten.

Matching is by item text, never by index. The first version of this script
matched by position and silently mis-assigned 225 sources when one item line
failed to parse, so: every item must either match a key or be reported.

Data lives in tables/<track-id>.py, one module per track, each exposing
DATA = {item-text-substring: (learn, practise, evidence)}.

  python3 -I build/sources/apply_table.py            # every track with a table
  python3 -I build/sources/apply_table.py t04 t05    # just these
"""
import importlib, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
HTML = HERE.parents[1] / "master-tracker.html"
sys.path.insert(0, str(HERE))


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


def track_bounds(src, tid):
    """The slice of the file holding one track's definition."""
    start = src.index('{id:"%s"' % tid)
    nxt = src.find('\n{id:"t', start + 1)
    end = nxt if nxt != -1 else src.index("\n];", start)
    return start, end


def validate(tid, data):
    bad = []
    for k, v in data.items():
        if len(v) != 3:
            bad.append("%s: expected 3 fields, got %d" % (k[:40], len(v)))
        for f in v:
            if f is None:
                continue
            if '"' in f:
                bad.append("%s: a double quote would break the JS literal" % k[:40])
            if f.count("|") > 1:
                bad.append("%s: more than one | in %r" % (k[:40], f[:50]))
    if bad:
        raise SystemExit("%s data is invalid:\n  " % tid + "\n  ".join(bad))


def apply_track(src, tid, data):
    validate(tid, data)
    start, end = track_bounds(src, tid)
    lines = src[start:end].split("\n")
    matched, unmatched, used = 0, [], set()

    for n, line in enumerate(lines):
        if not line.lstrip().startswith('["'):
            continue
        i = line.index("[")
        j = find_close(line, i)
        parts = split_top(line[i + 1:j])

        key = next((k for k in data if k in parts[0]), None)
        if not key:
            unmatched.append(parts[0][:70])
            continue
        used.add(key)
        learn, prac, ev = data[key]
        keep = [p if p else "null" for p in (parts + ["null"] * 3)[:3]]
        lines[n] = line[:i] + "[" + ",".join(keep + [lit(learn), lit(prac), lit(ev)]) + "]" + line[j + 1:]
        matched += 1

    return src[:start] + "\n".join(lines) + src[end:], matched, sorted(set(data) - used), unmatched


def syntax_check():
    """Parse the file's inline script with node.

    The data in tables/ is validated field by field, but a hand edit to an item's
    meta is not — and a raw double quote there ends the JS string literal, blanks
    the whole page, and still passes every check that only looks at the data. So
    the last thing this script does is parse what it just wrote.
    """
    import re, shutil, subprocess, tempfile, os
    if not shutil.which("node"):
        print("note: node not found, skipping the syntax check")
        return
    body = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", HTML.read_text(encoding="utf-8"), re.S)[0]
    f = tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8")
    f.write(body); f.close()
    try:
        r = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
    finally:
        os.unlink(f.name)
    if r.returncode:
        raise SystemExit("master-tracker.html no longer parses:\n" + r.stderr[:1500])
    print("syntax check: the inline script parses")


def main():
    want = sys.argv[1:]
    mods = sorted(p.stem for p in (HERE / "tables").glob("t*.py"))
    if want:
        missing = [t for t in want if t not in mods]
        if missing:
            raise SystemExit("no table for: %s (have %s)" % (", ".join(missing), ", ".join(mods)))
        mods = want

    src = HTML.read_text(encoding="utf-8")
    total, problems = 0, False
    for tid in mods:
        data = importlib.import_module("tables." + tid).DATA
        src, n, unused, unmatched = apply_track(src, tid, data)
        total += n
        print("%s  %3d/%d items written" % (tid, n, len(data)))
        if unused:
            problems = True
            print("     keys that matched nothing: %s" % unused)
        if unmatched:
            print("     items left without a resource: %d" % len(unmatched))
            for u in unmatched:
                print("       - %s" % u)

    HTML.write_text(src, encoding="utf-8")
    syntax_check()
    print("\n%d items written across %d track(s)" % (total, len(mods)))
    if problems:
        raise SystemExit("some keys matched nothing — fix them before shipping")


if __name__ == "__main__":
    main()
