"""Gera os diagramas SVG de SBNF a partir da geometria do GND_DRAW
(pátios, prédios e taxiways com ref).

Uso: python3 -I gen.py <pasta_de_saida>
"""
import sys, os, math, heapq, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1]

# ---------------------------------------------------------------- dados
# pátios, prédios e taxiways do GND_DRAW (as taxiways já vêm com ref)
APRONS = [p for f in load('4_PATIOS') for p in polys(f['geometry'])]
BUILD = [p for f in load('5_PREDIOS') for p in polys(f['geometry'])]


def _rect(x0, y0, x1, y1):
    """Retângulo em coordenadas do desenho, convertido de volta para lon/lat (path_d reprojeta)."""
    def inv(x, y):
        y = -y
        px, py = x * COS + y * SIN, -x * SIN + y * COS
        return (px / KX + LON0, py / KY + LAT0)
    return [[inv(x0, y0), inv(x1, y0), inv(x1, y1), inv(x0, y1), inv(x0, y0)]]


# o GND_DRAW só tem o pavimento do pátio 1 e pedaços dos pátios 2 e 3:
# completa os dois em volta das posições da PDC (pátio 2: 1-4, pátio 3: 6A, 6B, 7, 8)
APRONS += [_rect(-232, 180, -116, 270), _rect(160, 150, 272, 275)]

# índices das feições de 9A_TAXIWAY (ver debug.py): 3, 4 e 6 são a pista de táxi do pátio (APN no AIP);
# 22 e 23 são as áreas de giro das cabeceiras 08 e 26
REMAP = {3: 'APN', 4: 'APN', 6: 'APN', 22: 'GIRO08', 23: 'GIRO26', 21: 'A', 7: 'B'}
_raw = [(REMAP.get(i, ref), [xy(*q) for q in ln]) for i, (ref, ln) in enumerate(taxiways())]
# linhas de posição sem ref (pontas soltas curtas) saem; as demais ligações sem ref ficam livres na rota
_ends = collections.Counter(key2 for _, pts in _raw for key2 in
                            [(round(p[0]), round(p[1])) for p in pts])
TWY = []
for ref, pts in _raw:
    L_ = sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))
    loose = any(_ends[(round(p[0]), round(p[1]))] == 1 for p in (pts[0], pts[-1]))
    if ref is None and loose and L_ < 130:
        continue
    TWY.append((ref, pts))

RWY = {'08/26': (thr('08'), thr('26'))}


def unit(a, b):
    L = math.dist(a, b)
    return ((b[0] - a[0]) / L, (b[1] - a[1]) / L), L


def rwy_dist(name, p):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    vx, vy = p[0] - a[0], p[1] - a[1]
    return vx * uy - vy * ux, vx * ux + vy * uy


def rwy_pt(name, t):
    a, b = RWY[name]
    (ux, uy), _ = unit(a, b)
    return (a[0] + ux * t, a[1] + uy * t)


# ---------------------------------------------------------------- grafo
def key(p):
    return (round(p[0], 1), round(p[1], 1))


G = collections.defaultdict(list)
for ref, pts in TWY:
    for a, b in zip(pts, pts[1:]):
        ka, kb = key(a), key(b)
        w = math.dist(a, b)
        G[ka].append((kb, ref, w))
        G[kb].append((ka, ref, w))

for name in RWY:
    a, b = RWY[name]
    L = math.dist(a, b)
    on = []
    for n in list(G):
        d, t = rwy_dist(name, n)
        if -30 <= t <= L + 30 and abs(d) < 40:
            p = key(rwy_pt(name, t))
            if p != n:
                G[n].append((p, None, abs(d)))
                G[p].append((n, None, abs(d)))
            on.append((t, p))
    on = sorted(set(on))
    for (_, p), (_, q) in zip(on, on[1:]):
        w = math.dist(p, q) * 3
        G[p].append((q, 'RWY' + name, w))
        G[q].append((p, 'RWY' + name, w))


def refs_at(n):
    return {r for _, r, _ in G[n]}


def node_on(r, near):
    return min((n for n in G if r in refs_at(n)), key=lambda n: math.dist(n, near))


def node_at(r1, r2, near):
    c = [n for n in G if r1 in refs_at(n) and r2 in refs_at(n)]
    if not c:
        raise SystemExit(f'sem interseção {r1}/{r2}')
    return min(c, key=lambda n: math.dist(n, near))


def rwy_node(name, t):
    """Nó do eixo da pista mais próximo da distância t (a partir da cabeceira 08)."""
    p = rwy_pt(name, t)
    return min((n for n in G if 'RWY' + name in refs_at(n)), key=lambda n: math.dist(n, p))


def route(a, b, allowed):
    allowed = set(allowed) | {None}
    dist, prev = {a: 0}, {}
    pq = [(0, a)]
    while pq:
        d, n = heapq.heappop(pq)
        if n == b:
            break
        if d > dist[n]:
            continue
        for m, r, w in G[n]:
            if r not in allowed:
                continue
            nd = d + w
            if nd < dist.get(m, 1e18):
                dist[m], prev[m] = nd, n
                heapq.heappush(pq, (nd, m))
    if b not in dist:
        raise SystemExit(f'sem rota {a}->{b} por {allowed}')
    path = [b]
    while path[-1] != a:
        path.append(prev[path[-1]])
    return path[::-1]


def chain(*legs):
    pts = []
    for i in range(0, len(legs) - 2, 2):
        seg = route(legs[i], legs[i + 2], legs[i + 1])
        pts += seg if not pts else seg[1:]
    return pts


# ---------------------------------------------------------------- desenho
PAL = {
    'bg': '#f5f6f8', 'apron': '#cfd3d9', 'build': '#3d4452',
    'twy': '#a9afb8', 'rwy': '#262b33', 'text': '#1f2430', 'muted': '#5b6372',
    'dep': '#12a150', 'arr': '#3d7fd6', 'alt': '#c26a00', 'hold': '#d42a2a',
    'gnd': '#2f7fd0', 'twr': '#e0a100', 'tora': '#7b2fbf', 'rmp': '#0f9d8a',
}

X0 = thr('08')[0] - 200
X1 = thr('26')[0] + 160
Y0 = -330
Y1 = 420
SC = 1.6


def pl(pts):
    return 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)


def svg_open(title):
    W, H = X1 - X0, Y1 - Y0
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{X0:.0f} {Y0:.0f} {W:.0f} {H:.0f}" '
            f'width="{W/SC:.0f}" height="{H/SC:.0f}" role="img" aria-label="{title}" '
            f'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif">',
            f'<title>{title}</title>',
            '<defs>'
            + ''.join(f'<marker id="ar-{k}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3" orient="auto-start-reverse">'
                      f'<path d="M0,0 L10,5 L0,10 z" fill="{PAL[k]}"/></marker>' for k in ('dep', 'arr', 'alt'))
            + '</defs>',
            f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{W:.0f}" height="{H:.0f}" rx="30" fill="{PAL["bg"]}"/>']


def badge(x, y, t, fill=None, fg='#fff', size=40):
    fill = fill or PAL['rwy']
    w = size * 0.62 * len(t) + 30
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.72:.0f}" width="{w:.0f}" height="{size*1.44:.0f}" rx="10" fill="{fill}"/>'
            f'<text x="{x:.0f}" y="{y+size*0.36:.0f}" font-size="{size}" font-weight="700" fill="{fg}" text-anchor="middle">{t}</text></g>')


def tag(x, y, t, size=24):
    w = size * 0.66 * len(t) + 16
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.68:.0f}" width="{w:.0f}" height="{size*1.36:.0f}" rx="6" fill="#1d1d1d"/>'
            f'<text x="{x:.0f}" y="{y+size*0.35:.0f}" font-size="{size}" font-weight="700" fill="#ffd400" text-anchor="middle">{t}</text></g>')


def base_layers(s, labels=True):
    s.append('<g>')
    for p in APRONS:
        s.append(f'<path d="{path_d(p)}" fill="{PAL["apron"]}" fill-rule="evenodd"/>')
    for p in BUILD:
        s.append(f'<path d="{path_d(p)}" fill="{PAL["build"]}" fill-rule="evenodd"/>')
    for ref, pts in TWY:
        s.append(f'<path d="{pl(pts)}" fill="none" stroke="{PAL["twy"]}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>')
    for name, (a, b) in RWY.items():
        (ux, uy), L = unit(a, b)
        s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{PAL["rwy"]}" stroke-width="45"/>')
        s.append(f'<line x1="{a[0]+ux*60:.1f}" y1="{a[1]+uy*60:.1f}" x2="{b[0]-ux*60:.1f}" y2="{b[1]-uy*60:.1f}" '
                 f'stroke="#fff" stroke-width="2" stroke-dasharray="30 24"/>')
    for ln in HOLD:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="{PAL["hold"]}" stroke-width="8"/>')
    s.append('</g>')
    a, b = RWY['08/26']
    s.append(badge(a[0] - 110, a[1], '08', size=40))
    s.append(badge(b[0] + 110, b[1], '26', size=40))
    if labels:
        twy_labels(s)
        apron_labels(s)


LABELS = []  # preenchido por maps.py


def twy_labels(s):
    for ref, (x, y) in LABELS:
        s.append(tag(x, y, ref))


def circle_num(s, x, y, t, r=26):
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" stroke="{PAL["text"]}" stroke-width="5"/>'
             f'<text x="{x:.0f}" y="{y+11:.0f}" font-size="32" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">{t}</text></g>')


APRON_POS = {'1': (40, 210), '2': (-175, 150), '3': (305, 190)}


def apron_labels(s):
    for t, (x, y) in APRON_POS.items():
        circle_num(s, x, y, t)
    for t, (x, y) in (('TPS', (20, 330)),):
        s.append(badge(x, y, t, fill='#fff', fg=PAL['build'], size=26))


def flow(s, pts, kind, dashed=False, width=24, arrow=True):
    da = ' stroke-dasharray="44 28"' if dashed else ''
    me = f' marker-end="url(#ar-{kind})"' if arrow else ''
    if not dashed:
        s.append(f'<path d="{pl(pts)}" fill="none" stroke="#fff" stroke-width="{width+12}" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<path d="{pl(pts)}" fill="none" stroke="{PAL[kind]}" stroke-width="{width}" stroke-linecap="round" '
             f'stroke-linejoin="round"{da}{me}/>')
    if not arrow:
        return
    segs = list(zip(pts, pts[1:]))
    total = sum(math.dist(a, b) for a, b in segs)
    step, acc, nxt = 300, 0, 300
    for a, b in segs:
        d = math.dist(a, b)
        while d and acc + d >= nxt and nxt < total - 100:
            k = (nxt - acc) / d
            x, y = a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
            s.append(f'<path d="M-9,-8 L9,0 L-9,8 z" fill="#fff" transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})"/>')
            nxt += step
        acc += d


def north_arrow(s, x, y):
    nx, ny = math.sin(THETA), -math.cos(THETA)
    ang = math.degrees(math.atan2(ny, nx)) + 90
    s.append(f'<g transform="translate({x:.0f},{y:.0f}) rotate({ang:.1f})">'
             f'<path d="M0,-80 L22,27 L0,10 L-22,27 z" fill="{PAL["text"]}"/>'
             f'<text x="0" y="-94" font-size="32" font-weight="700" text-anchor="middle" fill="{PAL["text"]}">N</text></g>')


def scale_bar(s, x, y):
    s.append(f'<g fill="{PAL["text"]}"><rect x="{x}" y="{y}" width="100" height="10"/><rect x="{x+100}" y="{y}" width="100" height="10" fill="none" stroke="{PAL["text"]}" stroke-width="3"/>'
             f'<text x="{x}" y="{y-10}" font-size="24">0</text><text x="{x+200}" y="{y-10}" font-size="24" text-anchor="middle">200 m</text></g>')


def credit(s):
    s.append(f'<text x="{X1-40:.0f}" y="{Y1-18:.0f}" font-size="18" fill="{PAL["muted"]}" text-anchor="end">'
             f'Base: © OpenStreetMap contributors (ODbL) · GND_DRAW · ADC/PDC SBNF / AIP AD 2 SBNF · fora de escala para navegação</text>')


def callout(s, x, y, lines_, color, size=24):
    w = max(len(l) for l in lines_) * size * 0.56 + 36
    h = len(lines_) * size * 1.25 + 14
    rx = x - w / 2
    s.append(f'<rect x="{rx:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="8" fill="#fff" stroke="{color}" stroke-width="4"/>')
    for i, l in enumerate(lines_):
        s.append(f'<text x="{x:.0f}" y="{y + 7 + size*1.05 + i*size*1.25:.0f}" font-size="{size}" font-weight="{700 if i == 0 else 400}" '
                 f'fill="{PAL["text"]}" text-anchor="middle">{l}</text>')


def leader(s, p, q, color):
    s.append(f'<line x1="{p[0]:.0f}" y1="{p[1]:.0f}" x2="{q[0]:.0f}" y2="{q[1]:.0f}" stroke="{color}" stroke-width="3"/>')


def frame(s):
    north_arrow(s, X0 + 90, Y0 + 130)
    scale_bar(s, X1 - 300, Y0 + 60)
    credit(s)


def save(name, s):
    s.append('</svg>')
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\n'.join(s))
    print('ok', name)


# pontos de espera: onde cada TWY cruza a distância de 90 m do eixo (pista de não precisão, código 4)
HOLD = []
L_RWY = math.dist(*RWY['08/26'])
for ref, pts in TWY:
    for a, b in zip(pts, pts[1:]):
        (da, ta), (db, tb) = rwy_dist('08/26', a), rwy_dist('08/26', b)
        for side in (1, -1):
            fa, fb = da * side - 90, db * side - 90
            if fa * fb < 0:
                k = fa / (fa - fb)
                p = (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
                if -250 < ta + (tb - ta) * k < L_RWY + 60:
                    (ux, uy), _ = unit(a, b)
                    HOLD.append([(p[0] - uy * 14, p[1] + ux * 14), (p[0] + uy * 14, p[1] - ux * 14)])

if __name__ == '__main__' and len(sys.argv) > 2:
    raise SystemExit

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maps.py')).read())
