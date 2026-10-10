"""Gera os diagramas SVG de SBGR a partir da geometria de solo da divisão.

Uso: python3 -I gen.py <pasta_de_saida>
"""
import sys, os, math, heapq, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1]

# ---------------------------------------------------------------- dados
APRONS = [p for f in load('SBGR_6_APRON') for p in polys(f['geometry'])]
BUILD = [p for f in load('SBGR_8_PREDIOS') for p in polys(f['geometry'])]
TWY = []  # (ref, [(x,y),...])
for f in load('SBGR_10_TAXIWAY'):
    ref = f['properties'].get('ref')
    if ref and (ref[0].isdigit() or ref.startswith('B1')):
        continue  # linhas de acesso a estandes
    for ln in lines(f['geometry']):
        TWY.append((ref, [xy(*p[:2]) for p in ln]))
STAND_LINES = []
for f in load('SBGR_10_TAXIWAY'):
    ref = f['properties'].get('ref')
    if ref and (ref[0].isdigit() or ref.startswith('B1')):
        for ln in lines(f['geometry']):
            STAND_LINES.append([xy(*p[:2]) for p in ln])
HOLD = [[xy(*p[:2]) for p in ln] for f in load('SBGR_11C_HOLDING_LINES') for ln in lines(f['geometry'])]
GATES = {f['properties'].get('ref'): xy(*f['geometry']['coordinates'][:2]) for f in load('SBGR_GATES')}

RWY = {
    '10L': runway_ends('10L', '28R', 90, 60),
    '10R': runway_ends('10R', '28L', 0, 0),
}
Y10L = (RWY['10L'][0][1] + RWY['10L'][1][1]) / 2
Y10R = (RWY['10R'][0][1] + RWY['10R'][1][1]) / 2


def rwy_y(name, x):
    (x1, y1), (x2, y2) = RWY[name]
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)


# ---------------------------------------------------------------- grafo
def key(p):
    return (round(p[0], 1), round(p[1], 1))


G = collections.defaultdict(list)  # node -> [(node, ref, w)]
for ref, pts in TWY:
    for a, b in zip(pts, pts[1:]):
        ka, kb = key(a), key(b)
        w = math.dist(a, b)
        G[ka].append((kb, ref, w))
        G[kb].append((ka, ref, w))

for name in RWY:
    (x1, _), (x2, _) = RWY[name]
    on = []
    for n in list(G):
        if len(G[n]) == 1 and x1 - 20 <= n[0] <= x2 + 20 and abs(n[1] - rwy_y(name, n[0])) < 45:
            p = key((n[0], rwy_y(name, n[0])))
            G[n].append((p, None, abs(n[1] - p[1])))
            G[p].append((n, None, abs(n[1] - p[1])))
            on.append(p)
    on = sorted(set(on))
    for a, b in zip(on, on[1:]):
        w = math.dist(a, b) * 3
        G[a].append((b, 'RWY' + name, w))
        G[b].append((a, 'RWY' + name, w))


def refs_at(n):
    return {r for _, r, _ in G[n]}


def node_at(r1, r2, near=None):
    c = [n for n in G if r1 in refs_at(n) and r2 in refs_at(n)]
    if not c:
        raise SystemExit(f'sem interseção {r1}/{r2}')
    if near is None:
        return c[0]
    return min(c, key=lambda n: math.dist(n, near))


def node_on(r, near):
    return min((n for n in G if r in refs_at(n)), key=lambda n: math.dist(n, near))


def end_near(r, rwy, side):
    """Extremidade da TWY r junto à pista rwy, do lado norte (-1) ou sul (+1)."""
    c = [n for n in G if r in refs_at(n) and side * (n[1] - rwy_y(rwy, n[0])) > 0]
    return min(c, key=lambda n: abs(n[1] - rwy_y(rwy, n[0])))


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
    """legs: (nó, refs-permitidas-até-o-próximo, nó, refs, nó...)."""
    pts = []
    for i in range(0, len(legs) - 2, 2):
        seg = route(legs[i], legs[i + 2], legs[i + 1])
        pts += seg if not pts else seg[1:]
    return pts


# ---------------------------------------------------------------- desenho
PAL = {
    'bg': '#f5f6f8', 'grass': '#e3e8e1', 'apron': '#cfd3d9', 'build': '#3d4452',
    'twy': '#a9afb8', 'rwy': '#262b33', 'text': '#1f2430', 'muted': '#5b6372',
    'dep': '#12a150', 'arr': '#3d7fd6', 'alt': '#c26a00', 'hold': '#d42a2a',
    'gnd': '#2f7fd0', 'twr': '#e0a100', 'tora': '#7b2fbf',
}

allx = [x for p in APRONS for r in p for x, _ in [xy(*q[:2]) for q in r]]
ally = [y for p in APRONS for r in p for _, y in [xy(*q[:2]) for q in r]]
X0 = min(min(allx), RWY['10R'][0][0]) - 270
X1 = max(max(allx), RWY['10L'][1][0]) + 300
Y0 = min(min(ally), min(xy(*q[:2])[1] for p in BUILD for r in p for q in r)) - 70
Y1 = max(ally) + 60


def pl(pts):
    return 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)


def svg_open(title, y0=Y0, y1=Y1, extra_h=0):
    W, H = X1 - X0, y1 - y0 + extra_h
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{X0:.0f} {y0:.0f} {W:.0f} {H:.0f}" '
         f'width="{W/3.4:.0f}" height="{H/3.4:.0f}" role="img" aria-label="{title}" '
         f'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif">',
         f'<title>{title}</title>',
         '<defs>'
         + ''.join(f'<marker id="ar-{k}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3" orient="auto-start-reverse">'
                   f'<path d="M0,0 L10,5 L0,10 z" fill="{PAL[k]}"/></marker>' for k in ('dep', 'arr', 'alt'))
         + '</defs>',
         f'<rect x="{X0:.0f}" y="{y0:.0f}" width="{W:.0f}" height="{H:.0f}" rx="40" fill="{PAL["bg"]}"/>']
    return s


def base_layers(s, labels=True, faded=False):
    op = ' opacity="0.55"' if faded else ''
    s.append(f'<g{op}>')
    for p in APRONS:
        s.append(f'<path d="{path_d(p)}" fill="{PAL["apron"]}" fill-rule="evenodd"/>')
    for ln in STAND_LINES:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="#bcc1c8" stroke-width="2"/>')
    for p in BUILD:
        s.append(f'<path d="{path_d(p)}" fill="{PAL["build"]}" fill-rule="evenodd"/>')
    for ref, pts in TWY:
        s.append(f'<path d="{pl(pts)}" fill="none" stroke="{PAL["twy"]}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>')
    for name, ((x1, y1), (x2, y2)) in RWY.items():
        s.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{PAL["rwy"]}" stroke-width="45"/>')
        s.append(f'<line x1="{x1+40:.1f}" y1="{y1:.1f}" x2="{x2-40:.1f}" y2="{y2:.1f}" stroke="#fff" stroke-width="2.5" stroke-dasharray="36 28"/>')
    for ln in HOLD:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="{PAL["hold"]}" stroke-width="12"/>')
    s.append('</g>')
    # identificação das cabeceiras
    for a, b in (('10L', '28R'), ('10R', '28L')):
        (x1, y1), (x2, y2) = RWY[a]
        s.append(badge(x1 - 110, y1, a))
        s.append(badge(x2 + 110, y2, b))
    if labels:
        twy_labels(s)
        apron_labels(s)


def badge(x, y, t, fill=None, fg='#fff', size=56):
    fill = fill or PAL['rwy']
    w = size * 0.62 * len(t) + 26
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.72:.0f}" width="{w:.0f}" height="{size*1.44:.0f}" rx="8" fill="{fill}"/>'
            f'<text x="{x:.0f}" y="{y+size*0.36:.0f}" font-size="{size}" font-weight="700" fill="{fg}" text-anchor="middle">{t}</text></g>')


def tag(x, y, t, size=46):
    """Rótulo de TWY no estilo de placa de localização (amarelo sobre preto)."""
    w = size * 0.66 * len(t) + 16
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.68:.0f}" width="{w:.0f}" height="{size*1.36:.0f}" rx="5" fill="#1d1d1d"/>'
            f'<text x="{x:.0f}" y="{y+size*0.35:.0f}" font-size="{size}" font-weight="700" fill="#ffd400" text-anchor="middle">{t}</text></g>')


def pt_on(ref, frac=0.5, near=None):
    best = None
    for r, pts in TWY:
        if r != ref:
            continue
        if near is not None:
            for p in pts:
                if best is None or math.dist(p, near) < math.dist(best, near):
                    best = p
        else:
            L = [0]
            for a, b in zip(pts, pts[1:]):
                L.append(L[-1] + math.dist(a, b))
            t = L[-1] * frac
            for i in range(1, len(L)):
                if L[i] >= t:
                    k = (t - L[i - 1]) / max(L[i] - L[i - 1], 1e-9)
                    a, b = pts[i - 1], pts[i]
                    return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
    return best


def twy_labels(s):
    # posições escolhidas à mão a partir da carta ADC (x aproximado) para evitar sobreposição
    yA = A_L[1]
    yB = B_L[1]
    for x in (-700, 400, 1500):
        s.append(tag(x, yA - 1, 'A'))
        s.append(tag(x + 120, yB - 1, 'B'))
    for ref, near in (('G', (A_G[0], (yB + Y10L) / 2)),
                      ('H', (node_at('H', 'B')[0], (yB + Y10L) / 2)),
                      ('L', (node_at('L', 'B')[0], (yB + Y10L) / 2)),
                      ('N', (node_at('N', 'B')[0], (yB + Y10L) / 2)),
                      ('O', (node_at('O', 'B')[0], (yB + Y10L) / 2)),
                      ('P', None), ('Q', None), ('DD', None), ('FF', None),
                      ('BB', None), ('CC', None), ('C', None), ('D', None), ('E', None),
                      ('S', None), ('T', None), ('U', None), ('K', None), ('J', None), ('I', None),
                      ('M', None), ('V', None)):
        p = pt_on(ref, 0.5, near)
        if p:
            s.append(tag(p[0] + 48, p[1], ref, 40))


def centroid(refs):
    pts = [GATES[r] for r in refs if r in GATES]
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


def apron_labels(s):
    groups = collections.defaultdict(list)
    for r in GATES:
        if r and r[0].isdigit() and len(r.rstrip('LRA')) == 3:
            groups[r[0]].append(r)
        elif r:
            groups['12'].append(r)
    for g, refs in groups.items():
        x, y = centroid(refs)
        s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="54" fill="#fff" stroke="{PAL["text"]}" stroke-width="6"/>'
                 f'<text x="{x:.0f}" y="{y+19:.0f}" font-size="56" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">{g}</text></g>')
    # pátio 13 (BASP) e pátio 10 (Sideral), sem estandes no arquivo
    for x, y, t in ((2552, -960, '10'),):
        s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="54" fill="#fff" stroke="{PAL["text"]}" stroke-width="6"/>'
                 f'<text x="{x:.0f}" y="{y+19:.0f}" font-size="56" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">{t}</text></g>')
    x, y = 185, 225
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="54" fill="#fff" stroke="{PAL["text"]}" stroke-width="6"/>'
             f'<text x="{x:.0f}" y="{y+19:.0f}" font-size="56" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">13</text></g>')
    for t, (x, y) in (('T1', (-1390, -1150)), ('T2', (-540, -1290)), ('T3', (60, -1300)), ('CARGO', (-1080, -1540))):
        s.append(badge(x, y, t, fill='#fff', fg=PAL['build'], size=50))


def flow(s, pts, kind, dashed=False, width=20, arrow=True):
    da = ' stroke-dasharray="40 26"' if dashed else ''
    me = f' marker-end="url(#ar-{kind})"' if arrow else ''
    if not dashed:
        s.append(f'<path d="{pl(pts)}" fill="none" stroke="#fff" stroke-width="{width+12}" stroke-linecap="round" '
                 f'stroke-linejoin="round"/>')
    s.append(f'<path d="{pl(pts)}" fill="none" stroke="{PAL[kind]}" stroke-width="{width}" stroke-linecap="round" '
             f'stroke-linejoin="round"{da}{me}/>')
    if not arrow:
        return
    # setas intermediárias
    L, acc = 0, 0
    segs = list(zip(pts, pts[1:]))
    total = sum(math.dist(a, b) for a, b in segs)
    step = 420
    nxt = step
    for a, b in segs:
        d = math.dist(a, b)
        while acc + d >= nxt and nxt < total - 150:
            k = (nxt - acc) / d
            x, y = a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
            s.append(f'<path d="M-14,-13 L14,0 L-14,13 z" fill="#fff" transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})"/>')
            nxt += step
        acc += d


def north_arrow(s, x, y):
    # norte verdadeiro no referencial girado
    nx, ny = math.sin(THETA), -math.cos(THETA)
    x2, y2 = x + nx * 110, y + ny * 110
    ang = math.degrees(math.atan2(ny, nx)) + 90
    s.append(f'<g transform="translate({x:.0f},{y:.0f}) rotate({ang:.1f})">'
             f'<path d="M0,-120 L34,40 L0,14 L-34,40 z" fill="{PAL["text"]}"/>'
             f'<text x="0" y="-140" font-size="44" font-weight="700" text-anchor="middle" fill="{PAL["text"]}">N</text></g>')


def scale_bar(s, x, y):
    s.append(f'<g fill="{PAL["text"]}"><rect x="{x}" y="{y}" width="250" height="14"/><rect x="{x+250}" y="{y}" width="250" height="14" fill="none" stroke="{PAL["text"]}" stroke-width="4"/>'
             f'<text x="{x}" y="{y-14}" font-size="32">0</text><text x="{x+500}" y="{y-14}" font-size="32" text-anchor="middle">500 m</text></g>')


def credit(s, y):
    s.append(f'<text x="{X1-40:.0f}" y="{y:.0f}" font-size="34" fill="{PAL["muted"]}" text-anchor="end">'
             f'Base: © OpenStreetMap contributors (ODbL) · ADC SBGR / AIP AD 2 SBGR · fora de escala para navegação</text>')


def callout(s, x, y, lines_, color, anchor='middle', size=46):
    w = max(len(l) for l in lines_) * size * 0.56 + 30
    h = len(lines_) * size * 1.25 + 18
    rx = x - w / 2 if anchor == 'middle' else (x if anchor == 'start' else x - w)
    s.append(f'<rect x="{rx:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="10" fill="#fff" stroke="{color}" stroke-width="5"/>')
    for i, l in enumerate(lines_):
        s.append(f'<text x="{rx + w/2:.0f}" y="{y + 12 + size*1.05 + i*size*1.25:.0f}" font-size="{size}" font-weight="{700 if i == 0 else 400}" '
                 f'fill="{PAL["text"]}" text-anchor="middle">{l}</text>')


def save(name, s):
    s.append('</svg>')
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\n'.join(s))
    print('ok', name)


# nós de referência --------------------------------------------------------
A_G = node_at('A', 'G')
A_H = node_at('A', 'H')
B_H = node_at('B', 'H')
B_L = node_at('B', 'L')
B_N = node_at('B', 'N')
B_O = node_at('B', 'O')
B_P = node_at('B', 'P')
B_Q = node_at('B', 'Q')
A_Q = node_at('A', 'Q')
A_L = node_on('A', B_L)
A_N = node_on('A', B_N)
A_O = node_on('A', B_O)
A_P = node_on('A', B_P)
B_G = node_on('B', A_G)
A_Y9 = node_at('A', 'Y9')
A_EAST = A_Y9
A_WEST = A_G

G_10L_N = end_near('G', '10L', -1)
H_10L_N = end_near('H', '10L', -1)
Q_10L_N = end_near('Q', '10L', -1)
P_10L_N = end_near('P', '10L', -1)
O_10L_N = end_near('O', '10L', -1)
G_10R_N = end_near('G', '10R', -1)
G_10L_S = end_near('G', '10L', +1)
BB_10R = end_near('BB', '10R', -1)
CC_10R = end_near('CC', '10R', -1)
L_10L = end_near('L', '10L', -1)
N_10L = end_near('N', '10L', -1)
T_10R = end_near('T', '10R', +1)
U_10R = end_near('U', '10R', +1)

TAKEOFF = [  # (twy, nó junto à pista, rótulo, cor)
    ('10L', G_10L_N, 'G', '10L · TORA 3700 m'),
    ('10L', H_10L_N, 'H', '10L · TORA 3400 m'),
    ('28R', Q_10L_N, 'Q', '28R · TORA 3700 m'),
    ('28R', P_10L_N, 'P', '28R · TORA 3460 m'),
    ('28R', O_10L_N, 'O', '28R · TORA 2397 m'),
    ('10R', G_10R_N, 'G', '10R · TORA 2487 m'),
]

# ======================================================== 1. visão geral
s = svg_open('SBGR: visão geral, pátios e pontos de decolagem', extra_h=0)
base_layers(s)
for rw, n, t, lab in TAKEOFF:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="34" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
callout(s, G_10R_N[0] + 330, G_10R_N[1] + 90, ['10R · G', 'TORA 2487 m'], PAL['tora'], size=44)
s.append(f'<line x1="{G_10R_N[0]:.0f}" y1="{G_10R_N[1]:.0f}" x2="{G_10R_N[0]+330:.0f}" y2="{G_10R_N[1]+90:.0f}" stroke="{PAL["tora"]}" stroke-width="4"/>')
callout_specs = [
    (G_10L_N, -260, ['10L · G', 'TORA 3700 m']),
    (H_10L_N, 260, ['10L · H', 'TORA 3400 m']),
    (O_10L_N, -230, ['28R · O', 'TORA 2397 m']),
    (P_10L_N, -230, ['28R · P', 'TORA 3460 m']),
    (Q_10L_N, 110, ['28R · Q', 'TORA 3700 m']),
]
for n, dx, ls in callout_specs:
    callout(s, n[0] + dx, n[1] - 300, ls, PAL['tora'], size=44)
    s.append(f'<line x1="{n[0]:.0f}" y1="{n[1]-26:.0f}" x2="{n[0]+dx:.0f}" y2="{n[1]-300+90:.0f}" stroke="{PAL["tora"]}" stroke-width="4"/>')
north_arrow(s, X1 - 160, Y0 + 220)
scale_bar(s, X1 - 700, Y1 - 120)
credit(s, Y1 - 30)
save('sbgr-visao-geral.svg', s)

# ======================================================== 2. responsabilidade GND x TWR
hold_n = [p for ln in HOLD for p in ln if p[1] < Y10L and Y10L - p[1] < 160]
hold_s = [p for ln in HOLD for p in ln if p[1] > Y10R and p[1] - Y10R < 160]
yt = Y10L - (sum(Y10L - p[1] for p in hold_n) / len(hold_n))
yb = Y10R + (sum(p[1] - Y10R for p in hold_s) / len(hold_s))
s = svg_open('SBGR: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="40" fill="{PAL["gnd"]}" opacity="0.13"/>')
base_layers(s, labels=True)
s.append(f'<rect x="{X0+20:.0f}" y="{yt:.0f}" width="{X1-X0-40:.0f}" height="{yb-yt:.0f}" fill="{PAL["twr"]}" opacity="0.22"/>')
for yy in (yt, yb):
    s.append(f'<line x1="{X0+20:.0f}" y1="{yy:.0f}" x2="{X1-20:.0f}" y2="{yy:.0f}" stroke="{PAL["twr"]}" stroke-width="8" stroke-dasharray="30 18"/>')
callout(s, 2350, (Y10L + Y10R) / 2 - 75, ['TWR', 'pistas, cruzamentos e', 'TWY entre as pistas'], PAL['twr'], size=48)
callout(s, 2350, Y0 + 520, ['GND', 'pátios, TWY A e B e', 'ligações até o ponto de espera'], PAL['gnd'], size=48)
callout(s, 1450, yb + 60, ['GND', 'pátios 12 e 13, TWY S, T e U'], PAL['gnd'], size=44)
# pontos de transferência
for n, txt in ((L_10L, '1'), (N_10L, '1'), (G_10L_N, '2'), (H_10L_N, '2'), (O_10L_N, '2')):
    pass
def num(x, y, t, col):
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="{col}" stroke="#fff" stroke-width="7"/>'
             f'<text x="{x:.0f}" y="{y+17:.0f}" font-size="48" font-weight="700" fill="#fff" text-anchor="middle">{t}</text></g>')
for b in (B_L, B_N):
    num(b[0] + 70, b[1] + 40, '1', PAL['arr'])
for n in (G_10L_N, H_10L_N, P_10L_N, Q_10L_N):
    num(n[0] - 60, n[1] - 70, '2', PAL['dep'])
num(node_at('S', 'T')[0] - 70, node_at('S', 'T')[1] - 60, '3', PAL['arr'])
north_arrow(s, X1 - 160, Y0 + 220)
scale_bar(s, X1 - 700, Y1 - 120)
credit(s, Y1 - 30)
save('sbgr-responsabilidade.svg', s)


# ======================================================== 3/4. fluxos de solo
Y_HOLD_10L_S = Y10L + (Y10R - Y10L) * 0.35
Y_HOLD_10R_S = Y10R + (Y10R - Y10L) * 0.33


BARS = []


def stop_bar(s, pts, ylim=Y_HOLD_10L_S):
    """Barra vermelha onde a rota encontra o ponto de espera (por padrão, ao sul da 10L)."""
    for a, b in zip(pts, pts[1:]):
        if (a[1] - ylim) * (b[1] - ylim) <= 0 and a[1] != b[1]:
            k = (ylim - a[1]) / (b[1] - a[1])
            x = a[0] + (b[0] - a[0]) * k
            if any(abs(x - px) < 150 and abs(ylim - py) < 30 for px, py in BARS):
                return
            BARS.append((x, ylim))
            return


def draw_bars(s):
    for x, y in BARS:
        crowded = any(0 < px - x < 450 and abs(py - y) < 30 for px, py in BARS)
        sx = x - 125 if crowded else x + 125
        s.append(f'<g><line x1="{x-70:.0f}" y1="{y:.0f}" x2="{x+70:.0f}" y2="{y:.0f}" stroke="#fff" stroke-width="34" stroke-linecap="round"/>'
                 f'<line x1="{x-62:.0f}" y1="{y:.0f}" x2="{x+62:.0f}" y2="{y:.0f}" stroke="{PAL['hold']}" stroke-width="22" stroke-linecap="round"/>'
                 f'<circle cx="{sx:.0f}" cy="{y:.0f}" r="40" fill="{PAL['hold']}" stroke="#fff" stroke-width="6"/>'
                 f'<rect x="{sx-24:.0f}" y="{y-8:.0f}" width="48" height="16" fill="#fff"/></g>')


def flow_map(fname, title, deps, arrs, alts, notes, exits, south=(), arr_alts=()):
    s = svg_open(title)
    BARS.clear()
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, pts, 'alt', dashed=True, width=13)
    for pts in exits:
        flow(s, pts, 'dep', width=14)
    for pts in deps:
        flow(s, pts, 'dep', width=24)
    for pts in arrs:
        flow(s, pts, 'arr', width=17)
    for pts in south:
        flow(s, pts, 'dep', width=24)
    for pts in arr_alts:
        flow(s, pts, "arr", width=17)
    for pts in list(arrs) + list(arr_alts):
        stop_bar(s, pts)
    for pts in south:
        stop_bar(s, pts, Y_HOLD_10R_S)
        stop_bar(s, pts)
    draw_bars(s)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col in notes:
        callout(s, x, y, ls, PAL[col], size=44)
    north_arrow(s, X1 - 160, Y0 + 220)
    scale_bar(s, X1 - 700, Y1 - 120)
    credit(s, Y1 - 30)
    save(fname, s)


TW = lambda *r: set(r)


def apron_exit(ref, ytop=-200):
    """Rota da borda do pátio até a TWY A pela ligação ref."""
    yA = A_G[1]
    c = [n for n in G if ref in refs_at(n) and yA + ytop <= n[1] < yA - 20]
    top = min(c, key=lambda n: n[1])
    best = None
    for a in (n for n in G if 'A' in refs_at(n) and abs(n[0] - top[0]) < 150):
        try:
            p = route(top, a, {ref})
        except SystemExit:
            continue
        L = sum(math.dist(u, v) for u, v in zip(p, p[1:]))
        if best is None or L < best[0]:
            best = (L, p)
    return best[1]


G_10R_N_ = end_near('G', '10R', -1)
EXITS = [apron_exit(r) for r in ('I', 'J', 'K', 'M', 'Y9')]
EXITS.append(chain(node_on('Y1', (-1237, -1045)), {'Y1'}, node_at('A', 'Y1'), {'A'}, A_G))
A_10 = min((n for n in G if 'A' in refs_at(n) and 2480 < n[0] < 2600), key=lambda n: abs(n[0] - 2531))
EXITS.append(route((2531.0, -866.0), A_10, {None, 'A'}))

# pátios 12 e 13: saída pela S até a G, ao sul da 10R
S_G = node_at('S', 'G')
G_10R_S = end_near('G', '10R', +1)
EXITS.append([(-953, 185), S_G])
EXITS.append([(31, 200)] + chain(node_at('S', 'T'), {'S'}, S_G))
SOUTH_TO_10L = chain(S_G, {'G'}, G_10R_S, {'G', 'RWY10R'}, G_10R_N_, {'G', 'C'}, end_near('G', '10L', +1))
EXITS.append(route(node_on('G', (A_G[0], A_G[1] - 190)), A_G, {'G'}))
EXITS.append(route(node_on('H', (A_H[0], A_H[1] - 140)), A_H, {'H'}))
# --- configuração 10: pousos 10R, decolagens 10L
dep10 = [
    chain(A_10, TW('A'), A_G, TW('G'), G_10L_N),
    chain(A_H, TW('H', 'B'), H_10L_N),
]
arr10 = [
    chain(BB_10R, TW('BB', 'L', 'RWY10L'), B_L) + [A_L],
    chain(CC_10R, TW('CC', 'N', 'RWY10L'), B_N) + [A_N],
    chain(T_10R, TW('T'), node_at('S', 'T')),
    chain(U_10R, TW('U'), node_at('S', 'U')),
]
alt10 = [chain(B_Q, TW('B'), B_H)]
O_10R = end_near('O', '10R', -1)
OSCAR = [O_10R] + chain(end_near('O', '10L', +1), {'O', None}, end_near('O', '10L', -1), {'O'}, node_at('B', 'O'), {'O', None}, A_O)
flow_map('sbgr-fluxo-10.svg', 'SBGR: fluxo de solo, pousos 10R e decolagens 10L', dep10, arr10, alt10, [], EXITS, [SOUTH_TO_10L], [OSCAR])

# --- configuração 28: pousos 28L, decolagens 28R
dep28 = [
    chain(A_G, TW('A'), A_Q, TW('Q'), Q_10L_N),
    [A_P] + chain(B_P, TW('P'), P_10L_N),
]
G_10R_S = end_near('G', '10R', +1)
G_C = node_at('G', 'C')
arr28 = [
    chain(G_10R_N, TW('G', 'C'), G_10L_S, TW('G', 'RWY10L'), G_10L_N, TW('G'), A_G),
    chain(T_10R, TW('T'), node_at('S', 'T')),
    chain(U_10R, TW('U'), node_at('S', 'U')),
]
alt28 = [chain(B_H, TW('B'), B_Q)]
flow_map('sbgr-fluxo-28.svg', 'SBGR: fluxo de solo, pousos 28L e decolagens 28R', dep28, arr28, alt28, [], EXITS,
         [[(x - 45, y) for x, y in SOUTH_TO_10L + chain(end_near('G', '10L', +1), {'G', 'RWY10L'}, G_10L_N, {'G'}, A_G)[1:]]])
