"""Excalidraw -> SVG, stdlib only.

The corpus is a small, uniform subset (verified across all 6 scenes):
  * only text / rectangle / arrow, every angle 0, opacity always 100
  * every arrow is exactly 2 points with an end arrowhead and no start head
  * every rectangle is roundness type 3, fillStyle solid or hachure
  * 6 colour families, strokeWidth 2 (one 3)

Two things that are NOT obvious from the schema and will produce wrong output
if taken at face value:

  1. A container-bound label's stored `height` is STALE — it is the single-line
     height even for a 3-line label. The block height must be recomputed from the
     line count, or every multi-line label sits too low in its box.
  2. 97 of 129 texts are bound labels (verticalAlign:middle, textAlign:center).
     Their position must be derived from the CONTAINER, not from their own x/y.
"""
import html
import json
import math

PAD = 10                # Excalidraw BOUND_TEXT_PADDING (measured: uniformly 10 in this corpus)
ASCENT = 0.80           # baseline as a fraction of font size, from the line-box text top
FONT = ("ui-sans-serif,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif")


def _esc(s):
    return html.escape(s, quote=False)


def _dash(e):
    st = e.get("strokeStyle")
    if st == "dashed":
        return ' stroke-dasharray="8 6"'
    if st == "dotted":
        return ' stroke-dasharray="2 5"'
    return ""


def _text_geom(e, containers):
    """Return (anchor, x, block_top, lines, font_size, line_h)."""
    fs = e.get("fontSize", 16)
    lh = e.get("lineHeight", 1.25)
    line_h = fs * lh
    lines = e.get("text", "").split("\n")
    block_h = len(lines) * line_h

    c = containers.get(e.get("containerId"))
    if c:
        # Position from the container. The element's own x/y/height are unreliable.
        if e.get("textAlign") == "center":
            anchor, x = "middle", c["x"] + c["width"] / 2
        elif e.get("textAlign") == "right":
            anchor, x = "end", c["x"] + c["width"] - PAD
        else:
            anchor, x = "start", c["x"] + PAD
        va = e.get("verticalAlign", "middle")
        if va == "middle":
            top = c["y"] + (c["height"] - block_h) / 2
        elif va == "bottom":
            top = c["y"] + c["height"] - PAD - block_h
        else:
            top = c["y"] + PAD
    else:
        w = e.get("width", 0)
        if e.get("textAlign") == "center":
            anchor, x = "middle", e["x"] + w / 2
        elif e.get("textAlign") == "right":
            anchor, x = "end", e["x"] + w
        else:
            anchor, x = "start", e["x"]
        top = e["y"]
    return anchor, x, top, lines, fs, line_h


def _bbox(els, containers):
    xs, ys = [], []
    for e in els:
        t = e["type"]
        if t == "rectangle":
            xs += [e["x"], e["x"] + e["width"]]
            ys += [e["y"], e["y"] + e["height"]]
        elif t == "arrow":
            for px, py in e.get("points", []):
                xs.append(e["x"] + px)
                ys.append(e["y"] + py)
        elif t == "text":
            anchor, x, top, lines, fs, line_h = _text_geom(e, containers)
            w = e.get("width", 0)
            # anchor-aware, or the bbox grows a full text width to the left of every
            # left-anchored label and the scene ends up padded with dead space
            if anchor == "middle":
                xs += [x - w / 2, x + w / 2]
            elif anchor == "end":
                xs += [x - w, x]
            else:
                xs += [x, x + w]
            ys += [top, top + len(lines) * line_h]
    if not xs:
        return 0, 0, 100, 100
    return min(xs), min(ys), max(xs), max(ys)


def to_svg(path, title=""):
    data = json.loads(path.read_text(encoding="utf-8"))
    els = [e for e in data.get("elements", []) if not e.get("isDeleted")]
    containers = {e["id"]: e for e in els if e["type"] == "rectangle"}

    minx, miny, maxx, maxy = _bbox(els, containers)
    m = 24
    minx, miny, maxx, maxy = minx - m, miny - m, maxx + m, maxy + m
    w, h = maxx - minx, maxy - miny

    body, markers = [], {}

    # rectangles first, then arrows, then text — so labels are never occluded
    order = {"rectangle": 0, "arrow": 1, "text": 2}
    for e in sorted(els, key=lambda x: order.get(x["type"], 9)):
        t = e["type"]
        sw = e.get("strokeWidth", 2)

        if t == "rectangle":
            rw, rh = e["width"], e["height"]
            rx = min(32.0, rw * 0.25, rh * 0.25)
            bg = e.get("backgroundColor", "transparent")
            fill = "none" if bg == "transparent" else bg
            body.append(
                f'<rect x="{e["x"]:.1f}" y="{e["y"]:.1f}" width="{rw:.1f}" height="{rh:.1f}" '
                f'rx="{rx:.1f}" fill="{fill}" stroke="{e["strokeColor"]}" '
                f'stroke-width="{sw}"{_dash(e)}/>'
            )

        elif t == "arrow":
            pts = e.get("points", [])
            if len(pts) < 2:
                continue
            col = e["strokeColor"]
            mid = markers.setdefault(col, "m%d" % len(markers))
            x0, y0 = e["x"] + pts[0][0], e["y"] + pts[0][1]
            x1, y1 = e["x"] + pts[-1][0], e["y"] + pts[-1][1]
            # pull the line back so the marker tip lands on the intended point
            dx, dy = x1 - x0, y1 - y0
            d = math.hypot(dx, dy) or 1.0
            x1 -= dx / d * sw * 2.2
            y1 -= dy / d * sw * 2.2
            body.append(
                f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" '
                f'stroke="{col}" stroke-width="{sw}" stroke-linecap="round"'
                f'{_dash(e)} marker-end="url(#{mid})"/>'
            )

        elif t == "text":
            anchor, x, top, lines, fs, line_h = _text_geom(e, containers)
            base = top + (line_h - fs) / 2 + fs * ASCENT
            spans = "".join(
                f'<tspan x="{x:.1f}" y="{base + i * line_h:.1f}">{_esc(ln)}</tspan>'
                for i, ln in enumerate(lines) if ln.strip()
            )
            if not spans:
                continue
            body.append(
                f'<text font-size="{fs}" text-anchor="{anchor}" fill="{e["strokeColor"]}" '
                f'font-family="{FONT}">{spans}</text>'
            )

    # Per-colour markers rather than fill="context-stroke", which is too new for older iOS.
    defs = "".join(
        f'<marker id="{i}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5.5" '
        f'markerHeight="5.5" orient="auto-start-reverse">'
        f'<path d="M0.5,1 L9,5 L0.5,9 z" fill="{c}"/></marker>'
        for c, i in markers.items()
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{minx:.1f} {miny:.1f} {w:.1f} {h:.1f}" '
        f'width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{_esc(title)}">'
        f'<title>{_esc(title)}</title><defs>{defs}</defs>'
        f'<rect x="{minx:.1f}" y="{miny:.1f}" width="{w:.1f}" height="{h:.1f}" fill="#ffffff"/>'
        f'{"".join(body)}</svg>'
    )


if __name__ == "__main__":
    import pathlib
    import sys
    for p in sys.argv[1:]:
        p = pathlib.Path(p)
        out = p.with_suffix(".svg")
        out.write_text(to_svg(p, p.stem), encoding="utf-8")
        print(out, out.stat().st_size, "bytes")
