"""Gera os diagramas SVG de SBVT a partir da geometria de solo da divisão (GND_DRAW)
e das taxiways do OpenStreetMap (com ref).

Uso: python3 -I gen.py <pasta_de_saida>
"""
import sys, os, math, heapq, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1]

# ---------------------------------------------------------------- dados
APRONS = [p for f in load('5-PATIO') for p in polys(f['geometry'])]
BUILD = [p for f in load('6-PREDIOS') for p in polys(f['geometry'])]
# taxiways do OSM sem ref, identificadas pela posição na carta ADC
REF = {61: 'H', 47: 'G', 42: 'N', 64: 'F', 66: 'F', 67: 'F', 59: 'D', 38: 'D', 39: 'J', 34: 'J', 48: 'J',
       72: 'K', 18: 'K', 19: 'K', 69: 'K', 71: 'K', 14: 'K', 73: 'M', 15: 'M', 12: 'E', 32: 'E', 33: 'E',
       54: 'C', 51: 'D', 52: 'D', 24: 'B', 25: 'B', 26: 'B', 49: 'B', 50: 'A', 20: 'PP', 21: 'PP'}
SKIP = set()
TWY = []
for i, e in enumerate(osm()):
    if e['tags'].get('aeroway') != 'taxiway' or i in SKIP:
        continue
    TWY.append((REF.get(i, e['tags'].get('ref')), [xy(g['lon'], g['lat']) for g in e['geometry']]))

RWY = {'02/20': (thr('02'), thr('20')), '06/24': (thr('06'), thr('24'))}


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
    """Nó do eixo da pista mais próximo da distância t (a partir de 10 ou da extremidade 15)."""
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

X0 = -760
X1 = 1060
Y0 = -1290
Y1 = 1130
SC = 2.1


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
            f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{W:.0f}" height="{H:.0f}" rx="50" fill="{PAL["bg"]}"/>']


def badge(x, y, t, fill=None, fg='#fff', size=64):
    fill = fill or PAL['rwy']
    w = size * 0.62 * len(t) + 30
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.72:.0f}" width="{w:.0f}" height="{size*1.44:.0f}" rx="10" fill="{fill}"/>'
            f'<text x="{x:.0f}" y="{y+size*0.36:.0f}" font-size="{size}" font-weight="700" fill="{fg}" text-anchor="middle">{t}</text></g>')


def tag(x, y, t, size=30):
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
        s.append(f'<path d="{pl(pts)}" fill="none" stroke="{PAL["twy"]}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>')
    for name, (a, b) in RWY.items():
        (ux, uy), L = unit(a, b)
        s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{PAL["rwy"]}" stroke-width="46"/>')
        s.append(f'<line x1="{a[0]+ux*60:.1f}" y1="{a[1]+uy*60:.1f}" x2="{b[0]-ux*60:.1f}" y2="{b[1]-uy*60:.1f}" '
                 f'stroke="#fff" stroke-width="3" stroke-dasharray="44 34"/>')
    for ln in HOLD:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="{PAL["hold"]}" stroke-width="13"/>')
    s.append('</g>')
    for name in RWY:
        n1, n2 = name.split('/')
        a, b = RWY[name]
        (ux, uy), _ = unit(a, b)
        s.append(badge(a[0] - ux * 85, a[1] - uy * 85, n1, size=44))
        s.append(badge(b[0] + ux * 85, b[1] + uy * 85, n2, size=44))
    if labels:
        twy_labels(s)
        apron_labels(s)


LABELS = [  # posições escolhidas à mão
    ('A', (-420, 400)), ('B', (-280, 240)), ('C', (-110, -110)), ('D', (60, 50)), ('D', (280, 125)),
    ('E', (300, -150)), ('F', (515, -100)), ('F', (610, 380)), ('J', (640, 165)), ('K', (530, -545)),
    ('L', (575, -790)), ('M', (575, -960)), ('N', (600, 760)), ('G', (700, 1010)), ('H', (720, 935)),
    ('PP', (-60, -235)),
]


def twy_labels(s):
    for ref, (x, y) in LABELS:
        s.append(tag(x, y, ref))


def circle_num(s, x, y, t, r=40):
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" stroke="{PAL["text"]}" stroke-width="7"/>'
             f'<text x="{x:.0f}" y="{y+15:.0f}" font-size="44" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">{t}</text></g>')


APRON_POS = {'1': (420, 770), '2': (-150, -60), '3': (-310, 70), '4': (-150, -350)}


def apron_labels(s):
    for t, (x, y) in APRON_POS.items():
        circle_num(s, x, y, t)
    for t, (x, y) in (('TPS', (330, 900)), ('CARGA', (-560, 160))):
        s.append(badge(x, y, t, fill='#fff', fg=PAL['build'], size=32))


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
    step, acc, nxt = 450, 0, 450
    for a, b in segs:
        d = math.dist(a, b)
        while d and acc + d >= nxt and nxt < total - 150:
            k = (nxt - acc) / d
            x, y = a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
            s.append(f'<path d="M-14,-13 L14,0 L-14,13 z" fill="#fff" transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})"/>')
            nxt += step
        acc += d


def north_arrow(s, x, y):
    nx, ny = math.sin(THETA), -math.cos(THETA)
    ang = math.degrees(math.atan2(ny, nx)) + 90
    s.append(f'<g transform="translate({x:.0f},{y:.0f}) rotate({ang:.1f})">'
             f'<path d="M0,-130 L36,44 L0,16 L-36,44 z" fill="{PAL["text"]}"/>'
             f'<text x="0" y="-152" font-size="50" font-weight="700" text-anchor="middle" fill="{PAL["text"]}">N</text></g>')


def scale_bar(s, x, y):
    s.append(f'<g fill="{PAL["text"]}"><rect x="{x}" y="{y}" width="250" height="16"/><rect x="{x+250}" y="{y}" width="250" height="16" fill="none" stroke="{PAL["text"]}" stroke-width="5"/>'
             f'<text x="{x}" y="{y-16}" font-size="38">0</text><text x="{x+500}" y="{y-16}" font-size="38" text-anchor="middle">500 m</text></g>')


def credit(s):
    s.append(f'<text x="{X1-30:.0f}" y="{Y1-26:.0f}" font-size="21" fill="{PAL["muted"]}" text-anchor="end">'
             f'Base: © OpenStreetMap contributors (ODbL) · ADC SBVT / AIP AD 2 SBVT · fora de escala para navegação</text>')


def callout(s, x, y, lines_, color, size=31):
    w = max(len(l) for l in lines_) * size * 0.56 + 36
    h = len(lines_) * size * 1.25 + 22
    rx = x - w / 2
    s.append(f'<rect x="{rx:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="12" fill="#fff" stroke="{color}" stroke-width="6"/>')
    for i, l in enumerate(lines_):
        s.append(f'<text x="{x:.0f}" y="{y + 12 + size*1.05 + i*size*1.25:.0f}" font-size="{size}" font-weight="{700 if i == 0 else 400}" '
                 f'fill="{PAL["text"]}" text-anchor="middle">{l}</text>')


def leader(s, p, q, color):
    s.append(f'<line x1="{p[0]:.0f}" y1="{p[1]:.0f}" x2="{q[0]:.0f}" y2="{q[1]:.0f}" stroke="{color}" stroke-width="5"/>')


def frame(s):
    north_arrow(s, X0 + 130, Y0 + 230)
    scale_bar(s, X0 + 80, Y0 + 380)
    credit(s)


def save(name, s):
    s.append('</svg>')
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\n'.join(s))
    print('ok', name)


# pontos de espera: onde cada TWY cruza 90 m do eixo da pista
HOLD = []
for name, H in (('02/20', 90), ('06/24', 90)):
    L_RWY = math.dist(*RWY[name])
    for ref, pts in TWY:
        for a, b in zip(pts, pts[1:]):
            (da, ta), (db, tb) = rwy_dist(name, a), rwy_dist(name, b)
            for side in (1, -1):
                fa, fb = da * side - H, db * side - H
                if fa * fb < 0:
                    k = fa / (fa - fb)
                    p = (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
                    if -60 < ta + (tb - ta) * k < L_RWY + 60:
                        (ux, uy), _ = unit(a, b)
                        HOLD.append([(p[0] - uy * 26, p[1] + ux * 26), (p[0] + uy * 26, p[1] - ux * 26)])

if __name__ == '__main__' and len(sys.argv) > 2:
    raise SystemExit

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maps.py')).read())
