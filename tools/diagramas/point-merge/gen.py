"""Generates the two conceptual point-merge SVGs (structure and sequencing)."""
import math
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "docs/MOP/terminais/sbcw-curitiba/img"
M = (400.0, 380.0)          # merge point
R_OUT, R_IN = 290.0, 235.0  # sequencing legs (outer higher, inner lower)
A0, A1 = 32.0, 148.0        # arc span in degrees

BLUE, GREEN, ORANGE, INK, MUTED = "#2f7fd1", "#12a150", "#e8590c", "#1e293b", "#64748b"
FONT = 'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif"'


def pt(r, deg):
    a = math.radians(deg)
    return (M[0] + r * math.cos(a), M[1] - r * math.sin(a))


def arc(r, a_from, a_to):
    """SVG arc path from angle a_from to a_to (degrees, counter-clockwise positive)."""
    x0, y0 = pt(r, a_from)
    x1, y1 = pt(r, a_to)
    sweep = 1 if a_to < a_from else 0
    large = 1 if abs(a_to - a_from) > 180 else 0
    return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {large},{sweep} {x1:.1f},{y1:.1f}"


def plane(x, y, heading, color):
    """Aircraft glyph; heading 0 = up, clockwise positive."""
    return (f'<g transform="translate({x:.1f},{y:.1f}) rotate({heading:.1f})">'
            f'<path d="M0,-13 L3,-4 L13,2 L13,5 L3,2 L2,9 L6,12 L6,14 L0,12 L-6,14 L-6,12 L-2,9 L-3,2 L-13,5 L-13,2 L-3,-4 Z" '
            f'fill="{color}" stroke="#fff" stroke-width="1.2"/></g>')


def on_arc_cw(r, deg, color):      # moving left to right over the top (angle decreasing)
    x, y = pt(r, deg)
    return plane(x, y, 180 - deg, color)


def on_arc_ccw(r, deg, color):     # moving right to left (angle increasing)
    x, y = pt(r, deg)
    return plane(x, y, -deg, color)


def badge(x, y, n):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{INK}"/>'
            f'<text x="{x:.1f}" y="{y + 5:.1f}" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">{n}</text>')


def label(x, y, text, color=INK, size=15, anchor="middle", weight="700"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" paint-order="stroke" stroke="#f8fafc" stroke-width="4">{text}</text>')


def frame(title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 520" width="800" height="520" role="img" '
            f'aria-label="{title}" {FONT}>\n<title>{title}</title>\n'
            '<defs><marker id="ar" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{INK}"/></marker>'
            '<marker id="ar-o" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{ORANGE}"/></marker></defs>\n'
            '<rect width="800" height="520" rx="12" fill="#f8fafc"/>\n' + body + '\n</svg>\n')


def common():
    """Arcs, entries, merge point and the common leg to the runway."""
    s = []
    # range rings hint
    s.append(f'<circle cx="{M[0]}" cy="{M[1]}" r="{R_OUT}" fill="none" stroke="#cbd5e1" stroke-dasharray="2 6"/>')
    s.append(f'<circle cx="{M[0]}" cy="{M[1]}" r="{R_IN}" fill="none" stroke="#cbd5e1" stroke-dasharray="2 6"/>')
    # entry legs
    ox, oy = pt(R_OUT, A1)
    ix, iy = pt(R_IN, A0)
    s.append(f'<path d="M30,60 L{ox:.1f},{oy:.1f}" stroke="{BLUE}" stroke-width="5" fill="none" marker-end="url(#ar)"/>')
    s.append(f'<path d="M770,90 L{ix:.1f},{iy:.1f}" stroke="{GREEN}" stroke-width="5" fill="none" marker-end="url(#ar)"/>')
    # sequencing legs
    s.append(f'<path d="{arc(R_OUT, A1, A0)}" stroke="{BLUE}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    s.append(f'<path d="{arc(R_IN, A0, A1)}" stroke="{GREEN}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    # flow direction along each leg
    for deg in (128, 90, 52):
        x, y = pt(R_OUT, deg)
        s.append(f'<path d="M-7,-6 L7,0 L-7,6 z" fill="#fff" stroke="{BLUE}" stroke-width="2" '
                 f'transform="translate({x:.1f},{y:.1f}) rotate({90 - deg:.1f})"/>')
        x, y = pt(R_IN, deg)
        s.append(f'<path d="M-7,-6 L7,0 L-7,6 z" fill="#fff" stroke="{GREEN}" stroke-width="2" '
                 f'transform="translate({x:.1f},{y:.1f}) rotate({270 - deg:.1f})"/>')
    # common leg: merge point -> IAF -> runway
    s.append(f'<path d="M{M[0]},{M[1]} L{M[0]},455" stroke="{INK}" stroke-width="5" marker-end="url(#ar)"/>')
    s.append(f'<rect x="{M[0] - 7}" y="470" width="14" height="42" rx="2" fill="{INK}"/>')
    s.append(f'<path d="M{M[0] - 4},476 V506" stroke="#fff" stroke-width="1.5" stroke-dasharray="4 4"/>')
    s.append(f'<circle cx="{M[0]}" cy="{M[1]}" r="11" fill="#fff" stroke="{INK}" stroke-width="4"/>')
    s.append(label(M[0] + 20, M[1] + 6, "M", anchor="start", size=20))
    s.append(label(M[0] + 16, 452, "IAF", anchor="start", size=13, color=MUTED))
    return s


def structure():
    s = common()
    # equal distance to M from any point of the arc
    for deg in (125, 65):
        x, y = pt(R_OUT, deg)
        s.append(f'<path d="M{M[0]},{M[1]} L{x:.1f},{y:.1f}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="6 5"/>')
        lx, ly = pt(R_OUT * 0.55, deg)
        s.append(label(lx + (-12 if deg > 90 else 12), ly, "d", color=MUTED, size=17, anchor="middle"))
    x, y = pt(R_OUT, 90)
    s.append(label(x, y - 14, "FL150", color=BLUE))
    x, y = pt(R_IN, 90)
    s.append(label(x, y + 26, "FL140", color=GREEN))
    s.append(label(40, 46, "A", color=BLUE, size=20, anchor="start"))
    s.append(label(760, 76, "B", color=GREEN, size=20, anchor="end"))
    return frame("Point merge: estrutura", "\n".join(s))


def sequencing():
    s = common()
    # aircraft still on the legs
    s.append(on_arc_cw(R_OUT, 140, BLUE))
    s.append(on_arc_cw(R_OUT, 118, BLUE))
    s.append(on_arc_ccw(R_IN, 44, GREEN))
    s.append(on_arc_ccw(R_IN, 66, GREEN))
    # aircraft turning direct to M from the outer leg
    deg = 108
    x, y = pt(R_OUT, deg)
    s.append(f'<path d="M{x:.1f},{y:.1f} L{M[0] - 1},{M[1] - 18}" stroke="{ORANGE}" stroke-width="3.5" '
             f'stroke-dasharray="9 6" marker-end="url(#ar-o)"/>')
    s.append(plane(x, y, 270 - deg, ORANGE))
    # aircraft ahead, already direct to M on the same track, spaced
    def along(t):
        return (x + (M[0] - x) * t, y + (M[1] - y) * t)
    hd = math.degrees(math.atan2(M[0] - x, -(M[1] - y)))
    p1, p2 = along(0.42), along(0.78)
    s.append(plane(p1[0], p1[1], hd, INK))
    s.append(plane(p2[0], p2[1], hd, INK))
    q1, q2 = along(0.47), along(0.73)
    s.append(f'<path d="M{q1[0] + 26:.1f},{q1[1]:.1f} L{q2[0] + 26:.1f},{q2[1]:.1f}" stroke="{MUTED}" stroke-width="1.5" '
             'marker-start="url(#ar)" marker-end="url(#ar)"/>')
    mid = along(0.6)
    s.append(label(mid[0] + 40, mid[1] + 5, "≥ x NM", color=MUTED, size=14, anchor="start", weight="600"))
    # step badges
    bx, by = pt(R_OUT, 150)
    s.append(badge(bx - 26, by - 24, 1))
    s.append(badge(x - 30, y - 22, 2))
    b3 = along(0.6)
    s.append(badge(b3[0] - 34, b3[1], 3))
    s.append(badge(M[0] - 30, 440, 4))
    return frame("Point merge: sequenciamento", "\n".join(s))


open(f"{OUT}/point-merge-estrutura.svg", "w").write(structure())
open(f"{OUT}/point-merge-sequencia.svg", "w").write(sequencing())
