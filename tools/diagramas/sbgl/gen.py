"""Gera os diagramas SVG de SBGL a partir da geometria de solo da divisão (GND_DRAW)
e das taxiways do OpenStreetMap (com ref).

Uso: python3 -I gen.py <pasta_de_saida>
"""
import sys, os, math, heapq, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1]

# ---------------------------------------------------------------- dados
APRONS = [(f['properties'].get('ref') or f['properties'].get('name'), p) for f in load('4_APRON') for p in polys(f['geometry'])]
BUILD = [p for f in load('5_PREDIOS') for p in polys(f['geometry'])]
TWY = []
for e in osm():
    if e['tags'].get('aeroway') != 'taxiway':
        continue
    TWY.append((e['tags'].get('ref'), [xy(g['lon'], g['lat']) for g in e['geometry']]))
STAND_LINES = [[xy(*q[:2]) for q in ln] for f in load('9D_TAXIWAY_TRACEJADA') for ln in lines(f['geometry'])]
HOLD = [[xy(*q[:2]) for q in ln] for f in load('9E_HOLDING_POINTS') for ln in lines(f['geometry'])]

RWY = {'10/28': (thr('10'), thr('28')), '15/33': (end('15'), end('33'))}


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

X0 = end('15')[0] - 260
X1 = thr('28')[0] + 260
Y0 = thr('10')[1] - 330
Y1 = end('33')[1] + 380
SC = 4.2


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


def tag(x, y, t, size=46):
    w = size * 0.66 * len(t) + 16
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.68:.0f}" width="{w:.0f}" height="{size*1.36:.0f}" rx="6" fill="#1d1d1d"/>'
            f'<text x="{x:.0f}" y="{y+size*0.35:.0f}" font-size="{size}" font-weight="700" fill="#ffd400" text-anchor="middle">{t}</text></g>')


def base_layers(s, labels=True):
    s.append('<g>')
    for _, p in APRONS:
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
    # cabeceiras deslocadas da 15/33
    (ux, uy), _ = unit(*RWY['15/33'])
    for n in ('15', '33'):
        x, y = thr(n)
        s.append(f'<line x1="{x-uy*26:.0f}" y1="{y+ux*26:.0f}" x2="{x+uy*26:.0f}" y2="{y-ux*26:.0f}" stroke="#fff" stroke-width="7"/>')
    for ln in HOLD:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="{PAL["hold"]}" stroke-width="13"/>')
    s.append('</g>')
    for n1, n2, a, b in (('10', '28', thr('10'), thr('28')), ('15', '33', end('15'), end('33'))):
        (ux, uy), _ = unit(a, b)
        s.append(badge(a[0] - ux * 120, a[1] - uy * 120, n1))
        s.append(badge(b[0] + ux * 120, b[1] + uy * 120, n2))
    if labels:
        twy_labels(s)
        apron_labels(s)


LABELS = [  # posições escolhidas à mão
    ('N', (700, -740)), ('M', (500, -620)), ('N', (3000, -740)), ('M', (3200, -620)),
    ('P', (-430, -820)), ('Q', (-280, -760)), ('R', (-100, -900)),
    ('AA', (1180, -935)), ('BB', (1530, -935)), ('CC', (2300, -935)), ('DD', (2700, -935)), ('Z', (3720, -800)),
    ('L1', (-420, -360)), ('K', (-660, -280)), ('B', (-930, 120)), ('B', (60, 1380)),
    ('C', (-930, 520)), ('D', (-330, 1140)), ('E', (40, 1640)), ('F', (330, 1935)), ('J', (230, 2160)),
    ('G', (690, 2390)), ('H', (520, 2470)), ('A', (-1190, -300)),
    ('L2', (-310, 600)), ('L3', (-150, 610)), ('L4', (170, 1200)), ('L5', (290, 1520)),
    ('L6', (1950, -620)), ('L7', (2780, -620)),
]


def twy_labels(s):
    for ref, (x, y) in LABELS:
        s.append(tag(x, y, ref))


def circle_num(s, x, y, t, r=62):
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#fff" stroke="{PAL["text"]}" stroke-width="8"/>'
             f'<text x="{x:.0f}" y="{y+22:.0f}" font-size="64" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">{t}</text></g>')


APRON_POS = {'1': (-560, 90), '2': (40, 760), '3': (440, 1150), '5': (120, 2330), '6': (2720, -330),
             '7': (720, 1820), '8': (560, 2610)}


def apron_labels(s):
    for t, (x, y) in APRON_POS.items():
        circle_num(s, x, y, t)
    for t, (x, y) in (('T1', (-180, 190)), ('T2', (520, 640)), ('PÍER SUL', (950, 1060)), ('MIL', (900, 1950))):
        s.append(badge(x, y, t, fill='#fff', fg=PAL['build'], size=52))


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
    s.append(f'<text x="{X1-40:.0f}" y="{Y1-36:.0f}" font-size="36" fill="{PAL["muted"]}" text-anchor="end">'
             f'Base: © OpenStreetMap contributors (ODbL) · ADC SBGL / AIP AD 2 SBGL · fora de escala para navegação</text>')


def callout(s, x, y, lines_, color, size=50):
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
    north_arrow(s, X1 - 200, Y0 + 260)
    scale_bar(s, X1 - 700, Y1 - 150)
    credit(s)


def save(name, s):
    s.append('</svg>')
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\n'.join(s))
    print('ok', name)


# nós de referência --------------------------------------------------------
L15 = math.dist(*RWY['15/33'])
T15 = rwy_dist('15/33', thr('15'))[1]     # cabeceira 15 a partir da extremidade
T33 = rwy_dist('15/33', thr('33'))[1]

P_RWY = node_on('P', thr('10'))
R_RWY = node_on('R', rwy_pt('10/28', 44))
Z_RWY = node_on('Z', thr('28'))
A_RWY = node_on('A', rwy_pt('15/33', 92))
G_RWY = node_on('G', rwy_pt('15/33', 3166))
H_RWY = node_on('H', rwy_pt('15/33', 3166))
D_RWY = node_on('D', rwy_pt('15/33', 1518))
E_RWY = node_on('E', rwy_pt('15/33', 2021))
DD_RWY = node_on('DD', rwy_pt('10/28', 2834))
BB_RWY = node_on('BB', rwy_pt('10/28', 1923))
F_RWY = node_on('F', rwy_pt('15/33', 2700))
J_RWY = node_on('J', rwy_pt('15/33', 2627))

if __name__ == '__main__' and len(sys.argv) > 2:
    # modo debug: imprime nós
    for n in ('P_RWY', 'Z_RWY', 'A_RWY', 'G_RWY', 'H_RWY', 'D_RWY', 'E_RWY', 'DD_RWY', 'BB_RWY', 'F_RWY', 'J_RWY'):
        print(n, globals()[n])
    raise SystemExit

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'maps.py')).read())
