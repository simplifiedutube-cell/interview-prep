"""Assemble dist/index.html and dist/questions.html from the two hand-written pages.

Both carry <!--BUILD:*--> markers so this is pure mechanical substitution — the
sources stay readable, git-tracked, and openable on their own.

index.html keeps its own complete stylesheet (it is the most-visited page; an extra
CSS request buys nothing) and pulls in site.js only, for the service worker and the
update pill. questions.html additionally links site.css, for the shared shell.
"""
import html
import re
import shutil
from pathlib import Path

MERMAID_TITLES = {
    1: "the pipeline you must be able to draw in 3 minutes",
    2: "the agent loop with your guard mechanisms",
    3: "the latency budget you must recite",
    4: "hybrid retrieval with hard tenant isolation",
}


def _mermaid_html(n, have_svg, src_text):
    """A scrollable, fit-toggleable diagram — or an honest fallback. Never a blank box."""
    if have_svg:
        inner = (f'<img src="/assets/flow-{n:02d}.svg" '
                 f'alt="{html.escape(MERMAID_TITLES.get(n, "Flow diagram"))}" loading="lazy">')
    else:
        inner = f'<pre class="mmd-src">{html.escape(src_text)}</pre>'
    return (
        f'<div class="dg-bar"><button class="btn" data-fit="mmd{n}">⤢ actual size</button>'
        f'<span class="dg-hint">pinch to zoom</span></div>'
        f'<div class="mermaid fit" id="mmd{n}" tabindex="0" role="region" '
        f'aria-label="{html.escape(MERMAID_TITLES.get(n, "Flow diagram"))}">{inner}</div>'
    )


def build(root, dist, head, js_name, css_name, warn, shell, sync_name):
    site = Path(__file__).resolve().parent / "site"

    # ---------------- index.html : the tracker ----------------
    s = (root / "master-tracker.html").read_text(encoding="utf-8")
    if "<!--BUILD:HEAD-->" not in s:
        warn("master-tracker.html is missing <!--BUILD:HEAD-->; PWA tags not injected")
    # the tracker is self-contained: strip the stylesheet link out of the shared head
    head_no_css = re.sub(r'<link rel="stylesheet"[^>]*>\n?', "", head)
    s = s.replace("<!--BUILD:HEAD-->", head_no_css)
    # sync.js goes on the tracker only — it is the one page with state to sync, and
    # it must load BEFORE the inline script's PrepSync.start() call runs.
    s = s.replace("<!--BUILD:SYNC-->", f'<script src="/assets/{sync_name}"></script>')
    s = s.replace("<!--BUILD:JS-->", f'<script src="/assets/{js_name}"></script>')
    (dist / "index.html").write_text(s, encoding="utf-8")

    # ---------------- questions.html : the resume question bank ----------------
    q = (root / "resume-question-bank.html").read_text(encoding="utf-8")
    q = q.replace("<!--BUILD:HEAD-->", head)
    q = q.replace("<!--BUILD:JS-->", f'<script src="/assets/{js_name}"></script>')

    mm = site / "mermaid"
    ok = 0
    for n in range(1, 5):
        svg = mm / f"flow-{n:02d}.svg"
        src = mm / f"flow-{n:02d}.mmd"
        have = svg.exists() and svg.stat().st_size > 500
        if have:
            shutil.copy(svg, dist / "assets" / f"flow-{n:02d}.svg")
            ok += 1
        marker = f"<!--BUILD:MERMAID:{n}-->"
        if marker not in q:
            warn(f"questions.html missing {marker}")
            continue
        q = q.replace(marker, _mermaid_html(
            n, have, src.read_text(encoding="utf-8") if src.exists() else ""))
    if ok < 4:
        warn(f"only {ok}/4 mermaid diagrams pre-rendered; the rest fall back to source text. "
             f"Re-run: build/site/mermaid/render.sh")

    # the shared shell, so the question bank is navigable like every other page
    q = q.replace("<body>", "<body>\n" + shell("Resume Question Bank", "questions.html"), 1)
    (dist / "questions.html").write_text(q, encoding="utf-8")
    return ok
