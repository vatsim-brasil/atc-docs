"""Gera os diagramas SVG de SBRF a partir da geometria de solo da divisão (GND_DRAW)
e das taxiways do OpenStreetMap (com ref).

Uso: python3 -I gen.py <pasta_de_saida>
"""
import sys, os, math, heapq, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1]

# ---------------------------------------------------------------- dados
APRONS = [p for f in load('4_PATIO') for p in polys(f['geometry'])]
BUILD = [p for f in load('5_PREDIOS') for p in polys(f['geometry'])]
# taxiways do OSM sem ref, identificadas pela posição na carta ADC
REF = {4: 'L', 63: 'L', 65: 'L', 8: 'C', 52: 'E', 53: 'E', 54: 'E', 55: 'E', 56: 'E', 57: 'E', 35: 'M',
       114: 'B', 72: 'B', 59: 'B', 60: 'B', 71: 'G', 119: 'G', 64: 'G', 80: 'G', 40: 'G',
       70: 'J', 118: 'J', 36: 'J', 38: 'J', 37: 'K', 122: 'K', 124: 'K', 47: 'K',
       13: 'W', 79: 'W', 117: 'W', 73: 'F', 113: 'F', 46: 'F', 112: 'F',
       11: 'N', 76: 'N', 61: 'P', 77: 'P', 74: 'D'}
SKIP = {7, 62}  # TWY A do OSM: não existe na ADC atual
TWY = []
for i, e in enumerate(osm()):
    if e['tags'].get('aeroway') != 'taxiway' or i in SKIP:
        continue
    TWY.append((REF.get(i, e['tags'].get('ref')), [xy(g['lon'], g['lat']) for g in e['geometry']]))

RWY = {'18/36': (end('18'), thr('36'))}


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

X0 = end('18')[0] - 230
X1 = thr('36')[0] + 230
Y0 = -560
Y1 = 600
SC = 3.6


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


def tag(x, y, t, size=38):
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
    # cabeceira 18 deslocada (186 m)
    (ux, uy), _ = unit(*RWY['18/36'])
    x, y = thr('18')
    s.append(f'<line x1="{x-uy*26:.0f}" y1="{y+ux*26:.0f}" x2="{x+uy*26:.0f}" y2="{y-ux*26:.0f}" stroke="#fff" stroke-width="7"/>')
    for ln in HOLD:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="{PAL["hold"]}" stroke-width="13"/>')
    s.append('</g>')
    a, b = RWY['18/36']
    s.append(badge(a[0] - 110, a[1], '18', size=54))
    s.append(badge(b[0] + 110, b[1], '36', size=54))
    if labels:
        twy_labels(s)
        apron_labels(s)


LABELS = [  # posições escolhidas à mão
    ('M', (-1000, -60)), ('M', (300, -60)), ('M', (1200, -90)), ('C', (1530, 0)),
    ('B', (-200, -60)), ('L', (690, -10)), ('P', (-175, -165)), ('N', (-10, -190)),
    ('J', (-700, 160)), ('W', (-660, 300)), ('G', (-385, 120)), ('K', (-80, 240)), ('K', (480, 240)),
    ('F', (160, 120)), ('E', (760, 90)), ('D', (1150, 240)), ('D', (1470, 110)),
]


def twy_labels(s):
    for ref, (x, y) in LABELS:
        s.append(tag(x, y, ref))


def circle_num(s, x, y, t, r=48):
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" stroke="{PAL["text"]}" stroke-width="7"/>'
             f'<text x="{x:.0f}" y="{y+18:.0f}" font-size="52" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">{t}</text></g>')


APRON_POS = {'1': (-120, -260), '2': (820, -250), '3': (330, 350), '4': (-120, 330)}


def apron_labels(s):
    for t, (x, y) in APRON_POS.items():
        circle_num(s, x, y, t)
    for t, (x, y) in (('TPS', (850, -400)), ('CARGA', (420, -470)), ('MIL', (230, 470)), ('HANGARES', (-1000, 470))):
        s.append(badge(x, y, t, fill='#fff', fg=PAL['build'], size=40))


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
    s.append(f'<text x="{X1-40:.0f}" y="{Y1-30:.0f}" font-size="30" fill="{PAL["muted"]}" text-anchor="end">'
             f'Base: © OpenStreetMap contributors (ODbL) · ADC SBRF / AIP AD 2 SBRF · fora de escala para navegação</text>')


def callout(s, x, y, lines_, color, size=40):
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
    north_arrow(s, X0 + 300, Y0 + 170)
    scale_bar(s, X1 - 600, Y0 + 110)
    credit(s)


def save(name, s):
    s.append('</svg>')
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\n'.join(s))
    print('ok', name)


# pontos de espera: onde cada TWY cruza a distância de 105 m do eixo
HOLD = []
L_RWY = math.dist(*RWY['18/36'])
for ref, pts in TWY:
    for a, b in zip(pts, pts[1:]):
        (da, ta), (db, tb) = rwy_dist('18/36', a), rwy_dist('18/36', b)
        for side in (1, -1):
            fa, fb = da * side - 105, db * side - 105
            if fa * fb < 0:
                k = fa / (fa - fb)
                p = (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
                if -60 < ta + (tb - ta) * k < L_RWY + 60:
                    (ux, uy), _ = unit(a, b)
                    HOLD.append([(p[0] - uy * 24, p[1] + ux * 24), (p[0] + uy * 24, p[1] - ux * 24)])

if __name__ == '__main__' and len(sys.argv) > 2:
    raise SystemExit

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maps.py')).read())
