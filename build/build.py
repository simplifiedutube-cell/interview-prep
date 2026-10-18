#!/usr/bin/env python3
"""Build the deployable prep site into dist/.

One dependency: pandoc (already installed). Everything else is stdlib.

    python3 build/build.py [--strict] [--no-autolink]

Drag the resulting dist/ folder onto app.netlify.com/drop.
"""
import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DIST = ROOT / "public"          # Vercel serves this directory with no build step
SITE = HERE / "site"
TPL = HERE / "templates"

sys.path.insert(0, str(HERE))
import icons                      # noqa: E402
import excalidraw_svg             # noqa: E402
import manifest                    # noqa: E402
from manifest import (            # noqa: E402
    SECTION_ORDER, APP_PAGES, DIAGRAMS, UNPUBLISHED,
)

# Archived docs stay in the repo and in git; they are simply not built. Links
# pointing at one degrade to plain text, exactly like a never-published file —
# a dangling href to a page that no longer exists is worse than no link.
DOCS = [d for d in manifest.DOCS if d[4] != "archived"]
ARCHIVED = {(ROOT / d[0]).resolve() for d in manifest.DOCS if d[4] == "archived"}
ARCHIVED_NAMES = {Path(d[0]).name for d in manifest.DOCS if d[4] == "archived"}

WARN = []
NOTE = []


def warn(m):
    WARN.append(m)
    print("WARN: " + m)


def note(m):
    NOTE.append(m)
    print("note: " + m)


# ---------------------------------------------------------------- pandoc

def find_pandoc():
    p = shutil.which("pandoc")
    if not p:
        sys.exit(
            "build: pandoc not found.\n"
            "  Install it:  brew install pandoc\n"
            "  It is the only dependency this build has. Nothing else to install."
        )
    v = subprocess.run([p, "--version"], capture_output=True, text=True).stdout.split()[1]
    if int(v.split(".")[0]) < 3:
        sys.exit(f"build: pandoc {v} is too old; need 3.x. Run: brew upgrade pandoc")
    return p, v


PANDOC, PANDOC_V = find_pandoc()


def render_md(src):
    r = subprocess.run(
        # -tex_math_dollars: GFM enables it, so prose like "$0.0210/query … $0.0147"
        # gets swallowed as inline TeX and re-emitted as a run of italic letters.
        # These documents are full of dollar figures and contain no maths.
        [PANDOC, "-f", "gfm+smart-tex_math_dollars", "-t", "html5", "--wrap=none",
         "--no-highlight", "--email-obfuscation=none", str(src)],
        capture_output=True, text=True,
    )
    if r.returncode:
        sys.exit(f"build: pandoc failed on {src}\n{r.stderr}")
    return r.stdout


# ---------------------------------------------------------------- html bits

SRC_INDEX = {(ROOT / s).resolve(): out for s, out, *_ in DOCS}
DIAG_INDEX = {(ROOT / d[0]).resolve(): Path(d[0]).stem for d in DIAGRAMS}
BASENAMES = {}
for _s, _o, *_ in DOCS:
    BASENAMES.setdefault(Path(_s).name, []).append((ROOT / _s).resolve())


def resolve_ref(target, src):
    """Map a .md/.excalidraw reference to a site URL, or None."""
    raw = target.split("#", 1)
    frag = "#" + raw[1] if len(raw) > 1 else ""
    t = urllib.parse.unquote(raw[0])
    if not t or t.startswith(("http://", "https://", "mailto:", "#")):
        return None
    for base in (src.parent, ROOT):
        cand = (base / t).resolve()
        if cand in ARCHIVED:
            return "ARCHIVED", False
        if cand in SRC_INDEX:
            return "/" + SRC_INDEX[cand] + frag, (base is ROOT)
        if cand in DIAG_INDEX:
            return "/diagrams/index.html#" + DIAG_INDEX[cand], (base is ROOT)
    return None


A_RE = re.compile(r'<a\s+href="([^"]+)"([^>]*)>(.*?)</a>', re.S)


def rewrite_links(body, src):
    def sub(m):
        href, rest, inner = m.group(1), m.group(2), m.group(3)
        name = Path(urllib.parse.unquote(href.split("#")[0])).name
        if name in UNPUBLISHED or name in ARCHIVED_NAMES:
            return (f'<a class="unpublished" title="kept in the repo, not published to this site">'
                    f'{inner}</a>')
        r = resolve_ref(href, src)
        if r and r[0] == "ARCHIVED":
            return (f'<a class="unpublished" title="archived \u2014 kept in the repo, '
                    f'not published to this site">{inner}</a>')
        if r:
            url, via_root = r
            if via_root:
                note(f"fixed root-relative link in {src.relative_to(ROOT)}: {href} -> {url}")
            return f'<a href="{url}"{rest}>{inner}</a>'
        if href.startswith(("http://", "https://")):
            return f'<a href="{href}" target="_blank" rel="noopener"{rest}>{inner}</a>'
        if href.startswith("#") or href.startswith("mailto:"):
            return m.group(0)
        warn(f"unresolved link in {src.relative_to(ROOT)}: {href}")
        return m.group(0)
    return A_RE.sub(sub, body)


CODE_RE = re.compile(r"<code>([^<>]{3,80}?\.md)</code>")


def autolink_code_refs(body, src):
    """Turn bare `resources.md` mentions into taps. Exact filename match against a
    19-entry table, so false positives are effectively impossible."""
    # never touch a <code> already inside an <a>
    spans = [(m.start(), m.end()) for m in A_RE.finditer(body)]

    def inside(i):
        return any(a <= i < b for a, b in spans)

    def sub(m):
        if inside(m.start()):
            return m.group(0)
        r = resolve_ref(m.group(1), src)
        if not r or r[0] == "ARCHIVED":
            return m.group(0)
        return f'<a class="xref" href="{r[0]}">{m.group(0)}</a>'
    return CODE_RE.sub(sub, body)


def wrap_tables(body):
    return re.sub(
        r"<table>",
        '<div class="tw" tabindex="0" role="region" aria-label="Table, scrolls horizontally"><table>',
        body,
    ).replace("</table>", "</table></div>")


def staticise_tasklists(body):
    """Markdown task lists render read-only.

    Wiring 360 of these to localStorage would reintroduce the dated 28-day axis and
    create a second progress store that disagrees with the tracker. It would also put
    360 focusable-but-useless controls in the tab order."""
    body = re.sub(r'<input\s+type="checkbox"\s+checked=""\s*/?>',
                  '<span class="tick on" aria-hidden="true"></span>', body)
    body = re.sub(r'<input\s+type="checkbox"\s*/?>',
                  '<span class="tick" aria-hidden="true"></span>', body)
    body = re.sub(r'\bdisabled=""\s*', "", body)
    return body


H1_RE = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.S)
H2_RE = re.compile(r'<h2\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', re.S)
TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(s):
    return html.unescape(TAG_RE.sub("", s)).strip()


def pull_h1(body):
    m = H1_RE.search(body)
    if not m:
        return body, None
    return body[:m.start()] + body[m.end():], strip_tags(m.group(1))


def collect_h2(body):
    return [(i, strip_tags(t)) for i, t in H2_RE.findall(body)]


def first_sentence(body):
    for m in re.finditer(r"<p>(.*?)</p>", body, re.S):
        t = strip_tags(m.group(1))
        if len(t) > 25:
            t = re.split(r"(?<=[.!?])\s+", t)[0]
            return (t[:150] + "…") if len(t) > 150 else t
    return ""


# ---------------------------------------------------------------- shell

def head_block(css, extra=""):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#F5F6F2">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex,nofollow">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="icon" type="image/svg+xml" href="/assets/icon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Prep">
<link rel="stylesheet" href="/assets/{css}">{extra}"""


def nav_html(current):
    out = ['<aside id="s-side"><div class="s-head"><div class="s">Interview prep</div>'
           '<div class="t">Library</div></div><nav>']
    out.append('<div class="navsep">App</div>')
    for url, label, _ in APP_PAGES:
        out.append(f'<a href="/{url}">{html.escape(label)}</a>')
    out.append('<a href="/library.html"%s>All documents</a>'
               % (' class="here"' if current == "library.html" else ""))
    for sec in SECTION_ORDER:
        rows = [(o, t) for s, o, se, t, v in DOCS if se == sec]
        if not rows:
            continue
        out.append(f'<div class="navsep">{html.escape(sec)}</div>')
        for out_path, title in rows:
            cls = ' class="here"' if out_path == current else ""
            out.append(f'<a href="/{out_path}"{cls}>{html.escape(title)}</a>')
    out.append("</nav></aside>")
    return "".join(out)


def shell(title, current):
    return (
        '<header class="topbar">'
        '<button class="tb-btn" id="s-menu" aria-label="Open library navigation" '
        'aria-expanded="false" aria-controls="s-side">☰</button>'
        '<button class="tb-btn tb-back" id="s-back" aria-label="Back" hidden>‹</button>'
        f'<span class="tb-title">{html.escape(title)}</span>'
        '<a class="tb-btn tb-home" href="/index.html">Tracker</a>'
        "</header>"
        + nav_html(current)
        + '<div id="s-scrim"></div>'
    )


def fill(tpl, **kw):
    s = (TPL / tpl).read_text(encoding="utf-8")
    for k, v in kw.items():
        s = s.replace("{{%s}}" % k, v)
    left = re.findall(r"\{\{([A-Z_]+)\}\}", s)
    if left:
        warn(f"template {tpl} left unfilled: {sorted(set(left))}")
    return s


def write(rel, text):
    p = DIST / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero if any link is unresolved")
    ap.add_argument("--no-autolink", action="store_true")
    args = ap.parse_args()

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    assets = DIST / "assets"
    assets.mkdir()

    # ---- assets, content-hashed
    css_txt = (SITE / "site.css").read_text(encoding="utf-8")
    js_txt = (SITE / "site.js").read_text(encoding="utf-8")
    sync_txt = (SITE / "sync.js").read_text(encoding="utf-8")
    css_name = "site.%s.css" % hashlib.sha256(css_txt.encode()).hexdigest()[:8]
    js_name = "site.%s.js" % hashlib.sha256(js_txt.encode()).hexdigest()[:8]
    sync_name = "sync.%s.js" % hashlib.sha256(sync_txt.encode()).hexdigest()[:8]
    (assets / css_name).write_text(css_txt, encoding="utf-8")
    (assets / js_name).write_text(js_txt, encoding="utf-8")
    (assets / sync_name).write_text(sync_txt, encoding="utf-8")
    icon_files = icons.build(assets)

    HEAD = head_block(css_name)

    # ---- markdown documents
    order = [(s, o, se, t, v) for s, o, se, t, v in DOCS]
    rendered = {}
    for i, (s, out, sec, title, vis) in enumerate(order):
        src = (ROOT / s).resolve()
        body = render_md(src)
        body, h1 = pull_h1(body)
        body = rewrite_links(body, src)
        if not args.no_autolink:
            body = autolink_code_refs(body, src)
        body = staticise_tasklists(body)
        body = wrap_tables(body)
        toc = collect_h2(body)
        words = len(re.findall(r"[A-Za-z0-9’'-]+", strip_tags(body)))
        rendered[out] = dict(
            body=body, h1=h1 or title, title=title or h1, sec=sec,
            words=words, src=s, vis=vis, toc=toc,
            desc=getattr(manifest, "DESCRIPTIONS", {}).get(out) or first_sentence(body),
        )

    # diagrams page body comes from diagrams/README.md but renders as a gallery
    diag_out = "diagrams/index.html"

    for i, (s, out, sec, title, vis) in enumerate(order):
        r = rendered[out]
        prev_n = order[i - 1][1] if i else None
        next_n = order[i + 1][1] if i + 1 < len(order) else None
        pn = []
        if prev_n:
            pn.append(f'<a class="pv" href="/{prev_n}"><div class="k">Previous</div>'
                      f'<div class="l">{html.escape(rendered[prev_n]["title"])}</div></a>')
        if next_n:
            pn.append(f'<a class="nx" href="/{next_n}"><div class="k">Next</div>'
                      f'<div class="l">{html.escape(rendered[next_n]["title"])}</div></a>')
        prevnext = '<nav class="pn">%s</nav>' % "".join(pn) if pn else ""

        toc_html = ""
        if len(r["toc"]) >= 3:
            items = "".join(f'<li><a href="#{i2}">{html.escape(t)}</a></li>'
                            for i2, t in r["toc"])
            toc_html = (f'<details class="toc"><summary>On this page — '
                        f'{len(r["toc"])} sections</summary><ol>{items}</ol></details>')

        banner = ""
        if "DAILY-CHECKLIST" in r["src"]:
            banner = ('<div class="refbar"><b>Reference, not state.</b> Ticking happens in the '
                      '<a href="/index.html">tracker</a> — Today (00) for the routine, tracks '
                      '01–13 for the syllabus. This page is the plan behind them.</div>')

        mins = max(1, round(r["words"] / 220))
        if out == diag_out:
            continue      # rendered by the gallery builder below
        write(out, fill(
            "doc.html", HEAD=HEAD, TITLE=html.escape(r["title"]),
            SHELL=shell(r["title"], out), SECTION=html.escape(r["sec"]),
            H1=html.escape(r["h1"]), READING=f'{r["words"]:,} words · ~{mins} min read',
            BANNER=banner, TOC=toc_html, BODY=r["body"], PREVNEXT=prevnext,
            SRC=html.escape(r["src"]), JS=js_name,
        ))

    # ---- diagrams gallery
    gallery = []
    for j, (dsrc, dtitle, ddesc) in enumerate(DIAGRAMS):
        p = (ROOT / dsrc).resolve()
        stem = p.stem
        svg = excalidraw_svg.to_svg(p, dtitle)
        (DIST / "diagrams" / f"{stem}.svg").parent.mkdir(parents=True, exist_ok=True)
        (DIST / "diagrams" / f"{stem}.svg").write_text(svg, encoding="utf-8")
        bid = f"dg{j}"
        gallery.append(
            f'<section class="dg" id="{html.escape(stem)}">'
            f'<h2>{html.escape(dtitle)}</h2><div class="d">{html.escape(ddesc)}</div>'
            f'<div class="dg-bar">'
            f'<button class="btn" data-fit="{bid}">⤢ actual size</button>'
            f'<span class="dg-hint">pinch to zoom</span></div>'
            f'<div class="diagram fit" id="{bid}" tabindex="0" role="region" '
            f'aria-label="{html.escape(dtitle)} diagram">'
            f'<img src="/diagrams/{stem}.svg" alt="{html.escape(dtitle)}" '
            f'width="100%" loading="lazy"></div></section>'
        )
    dr = rendered[diag_out]
    write(diag_out, fill(
        "diagrams.html", HEAD=HEAD, SHELL=shell("Architecture Diagrams", diag_out),
        COUNT=f"{len(DIAGRAMS)} diagrams", INTRO=dr["body"],
        GALLERY="".join(gallery), JS=js_name,
    ))

    # ---- library index
    secs = []
    for sec in SECTION_ORDER:
        rows = [(o, rendered[o]) for _s, o, se, _t, _v in DOCS if se == sec]
        if not rows:
            continue
        cards = []
        for out, r in rows:
            mins = max(1, round(r["words"] / 220))
            cards.append(
                f'<a class="card" href="/{out}"><div class="t">{html.escape(r["title"])}</div>'
                + (f'<div class="d">{html.escape(r["desc"])}</div>' if r["desc"] else "")
                + f'<div class="m">{r["words"]:,} words · ~{mins} min</div></a>'
            )
        secs.append(f'<section class="lib-sec"><h2>{html.escape(sec)}</h2>{"".join(cards)}</section>')

    app_cards = "".join(
        f'<a class="card" href="/{u}"><div class="t">{html.escape(lbl)}</div>'
        f'<div class="d">{html.escape(d)}</div></a>' for u, lbl, d in APP_PAGES
    )
    secs.insert(0, f'<section class="lib-sec"><h2>App</h2>{app_cards}</section>')
    total_words = sum(r["words"] for r in rendered.values())
    write("library.html", fill(
        "library.html", HEAD=HEAD, SHELL=shell("Library", "library.html"),
        COUNT=f"{len(DOCS)} documents · {total_words:,} words", SECTIONS="".join(secs),
        JS=js_name,
    ))

    # ---- the two app pages
    import apppages
    apppages.build(ROOT, DIST, HEAD, js_name, css_name, warn, shell, sync_name)

    # ---- login page: reachable while logged out, so it links only /assets/*
    write("login.html", fill("login.html", HEAD=HEAD))

    # ---- offline + 404
    for name, kicker, h1, msg in [
        ("offline.html", "Offline", "You're offline",
         "<p>This page isn't in the cache yet. The tracker and the library index always are.</p>"),
        ("404.html", "Not found", "No such page",
         "<p>That URL doesn't exist on this site.</p>"),
    ]:
        write(name, fill("simple.html", HEAD=HEAD, TITLE=h1, KICKER=kicker, H1=h1,
                         BODY=msg + '<p><a href="/index.html">Tracker</a> · '
                                    '<a href="/library.html">Library</a></p>'))

    # ---- static site files
    # NB: no _headers file — that is Netlify syntax and does nothing on Vercel.
    # Its cache-control and noindex rules live in vercel.json "headers".
    shutil.copy(SITE / "robots.txt", DIST / "robots.txt")
    shutil.copy(SITE / "manifest.webmanifest.tmpl", DIST / "manifest.webmanifest")

    # ---- service worker: precache everything, versioned by content
    files = sorted(
        "/" + str(p.relative_to(DIST)).replace(os.sep, "/")
        for p in DIST.rglob("*") if p.is_file()
    )
    h = hashlib.sha256()
    for f in files:
        h.update(f.encode())
        h.update(hashlib.sha256((DIST / f.lstrip("/")).read_bytes()).digest())
    build_id = f"{date.today():%Y%m%d}-{h.hexdigest()[:8]}"
    precache = sorted(set(files + ["/"]))
    sw = (SITE / "sw.js.tmpl").read_text(encoding="utf-8")
    sw = sw.replace("{{BUILD}}", build_id).replace(
        "{{PRECACHE}}", json.dumps(precache, indent=2))
    write("sw.js", sw)

    # ---- report
    nbytes = sum(p.stat().st_size for p in DIST.rglob("*") if p.is_file())
    pages = len(list(DIST.rglob("*.html")))
    print()
    print(f"wrote {pages} pages · {len(DIAGRAMS)} diagrams · {len(icon_files)} icons "
          f"· fixed {len(NOTE)} root-relative links · {len(WARN)} warnings")
    print(f"build {build_id} · {len(precache)} precached files · {nbytes/1024:.0f} KB")
    print(f"pandoc {PANDOC_V} · dist at {DIST}")
    if WARN and args.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
