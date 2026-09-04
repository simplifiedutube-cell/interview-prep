"""Pure-stdlib PNG icon generation. No imaging library, no second dependency.

The mark: a teal field with three white horizontal bars at 62% / 44% / 78% width,
left-aligned and evenly spaced — reads as a progress stack, on-brand for a tracker,
and still legible at 32px.

Antialiasing is exact-horizontal-coverage per row with SS vertical subsamples, which
is both better looking and far faster than brute-force NxN supersampling.
"""
import math
import struct
import zlib

TEAL = (0x0E, 0x6B, 0x5C)
WHITE = (0xFF, 0xFF, 0xFF)
SS = 16                       # vertical subsamples per output row

BARS = (0.62, 0.44, 0.78)     # widths as a fraction of the content box


def _span(x0, y0, x1, y1, r, y):
    """Horizontal extent of a rounded rect at scanline y, or None."""
    if y < y0 or y > y1:
        return None
    if y < y0 + r:
        dy = y0 + r - y
    elif y > y1 - r:
        dy = y - (y1 - r)
    else:
        dy = 0.0
    if dy > 0:
        if dy >= r:
            return None
        dx = r - math.sqrt(r * r - dy * dy)
    else:
        dx = 0.0
    a, b = x0 + dx, x1 - dx
    return (a, b) if b > a else None


def _accumulate(cov, span, n, w):
    """Add horizontal coverage of `span` into the float row `cov`, weighted by w."""
    if span is None:
        return
    a, b = span
    i0 = max(0, int(math.floor(a)))
    i1 = min(n - 1, int(math.ceil(b)) - 1)
    for i in range(i0, i1 + 1):
        o = min(b, i + 1.0) - max(a, float(i))
        if o > 0:
            cov[i] += o * w


def _shapes(n, radius_frac, inset_frac):
    """Return (bg_rect, [bar_rects]) in output-pixel float coordinates."""
    r = radius_frac * n
    bg = (0.0, 0.0, float(n), float(n), r)

    pad = inset_frac * n
    cx0, cy0 = pad, pad
    cw, ch = n - 2 * pad, n - 2 * pad

    # 3 bars, gap = 0.55 * bar height  ->  3h + 2(0.55h) = ch
    h = ch / 4.1
    gap = 0.55 * h
    br = h * 0.35

    bars = []
    for k, frac in enumerate(BARS):
        y0 = cy0 + k * (h + gap)
        bars.append((cx0, y0, cx0 + cw * frac, y0 + h, br))
    return bg, bars


def render(n, radius_frac=0.0, inset_frac=0.20, bg_color=TEAL, fg_color=WHITE):
    """Return (rows_rgb, rows_alpha) — each a list of n rows of n floats/tuples."""
    bg, bars = _shapes(n, radius_frac, inset_frac)
    rgb_rows, a_rows = [], []
    w = 1.0 / SS

    for j in range(n):
        cov_bg = [0.0] * n
        cov_fg = [0.0] * n
        for k in range(SS):
            y = j + (k + 0.5) / SS
            _accumulate(cov_bg, _span(*bg, y), n, w)
            for b in bars:
                _accumulate(cov_fg, _span(*b, y), n, w)

        row_rgb, row_a = [], []
        for i in range(n):
            ab = min(1.0, cov_bg[i])
            af = min(ab, cov_fg[i])
            if ab <= 0:
                row_rgb.append((0, 0, 0))
                row_a.append(0)
                continue
            px = tuple(
                int(round((bg_color[c] * (ab - af) + fg_color[c] * af) / ab))
                for c in range(3)
            )
            row_rgb.append(px)
            row_a.append(int(round(ab * 255)))
        rgb_rows.append(row_rgb)
        a_rows.append(row_a)
    return rgb_rows, a_rows


def _chunk(tag, data):
    return (struct.pack(">I", len(data)) + tag + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))


def write_png(path, rgb_rows, a_rows=None):
    """Write RGBA (colour type 6) when a_rows is given, else RGB (type 2)."""
    n = len(rgb_rows)
    ctype = 6 if a_rows else 2
    raw = bytearray()
    for j, row in enumerate(rgb_rows):
        raw.append(0)                              # filter: none
        for i, px in enumerate(row):
            raw += bytes(px)
            if a_rows:
                raw.append(a_rows[j][i])
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + _chunk(b"IHDR", struct.pack(">IIBBBBB", n, n, 8, ctype, 0, 0, 0))
        + _chunk(b"IDAT", zlib.compress(bytes(raw), 9))
        + _chunk(b"IEND", b"")
    )


SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
<rect width="512" height="512" rx="61" fill="#0E6B5C"/>
<rect x="102" y="102" width="192" height="75" rx="26" fill="#fff"/>
<rect x="102" y="218" width="137" height="75" rx="26" fill="#fff"/>
<rect x="102" y="334" width="242" height="75" rx="26" fill="#fff"/>
</svg>
"""


def build(assets):
    """Emit the full icon set into `assets` (a pathlib.Path). Returns filenames."""
    out = []

    # PWA "any" — rounded corners, transparent outside
    for n in (192, 512):
        rgb, a = render(n, radius_frac=0.12, inset_frac=0.20)
        write_png(assets / f"icon-{n}.png", rgb, a)
        out.append(f"icon-{n}.png")

    # PWA "maskable" — full bleed, glyph inside the central safe area
    for n in (192, 512):
        rgb, a = render(n, radius_frac=0.0, inset_frac=0.27)
        write_png(assets / f"icon-{n}-maskable.png", rgb, a)
        out.append(f"icon-{n}-maskable.png")

    # apple-touch-icon — NO alpha and NO pre-rounded corners.
    # iOS applies its own mask; a pre-rounded icon gets double-rounded.
    rgb, _ = render(180, radius_frac=0.0, inset_frac=0.21)
    write_png(assets / "apple-touch-icon.png", rgb)
    out.append("apple-touch-icon.png")

    rgb, a = render(32, radius_frac=0.14, inset_frac=0.17)
    write_png(assets / "favicon-32.png", rgb, a)
    out.append("favicon-32.png")

    (assets / "icon.svg").write_text(SVG, encoding="utf-8")
    out.append("icon.svg")
    return out


if __name__ == "__main__":
    import pathlib
    import sys
    d = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    d.mkdir(parents=True, exist_ok=True)
    print("\n".join(build(d)))
