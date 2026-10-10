"""Gera os diagramas SVG de SBCT a partir da geometria de solo da divisão.

Uso: python3 -I gen.py <pasta_de_saida>
"""
import sys, os, math, heapq, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base import *

OUT = sys.argv[1]

# ---------------------------------------------------------------- dados
APRONS = [p for f in load('3_PATIO') for p in polys(f['geometry'])]
BUILD = [p for f in load('4_PRÉDIOS') for p in polys(f['geometry'])]
# TWY sem ref no OSM, nomeadas pela carta ADC (índice da feição em 9A_TAXIWAY)
UNNAMED = {7: 'PAD', 16: 'C', 33: 'C', 22: 'HG', 23: 'HG', 39: 'J', 40: 'J', 42: 'J',
           8: 'HG', 9: 'HG', 10: 'HG', 24: 'HG', 25: 'HG', 29: 'HG', 30: 'HG'}
TWY = []
for i, f in enumerate(load('9A_TAXIWAY')):
    p = f['properties']
    if p.get('aeroway') != 'taxiway':
        continue
    ref = UNNAMED.get(i) or p.get('ref')
    if ref and ref.startswith('Via'):
        ref = 'HG'
    for ln in lines(f['geometry']):
        TWY.append((ref, [xy(*q[:2]) for q in ln]))
STAND_LINES = [[xy(*q[:2]) for q in ln] for f in load('9A2_TAXIWAY_PONTILHADA') for ln in lines(f['geometry'])]
HOLD = [[xy(*q[:2]) for q in ln] for f in load('9A4_HOLDING') for ln in lines(f['geometry'])]
GATES = {f['properties'].get('ref'): xy(*f['geometry']['coordinates'][:2]) for f in load('9B_GATES')}

RWY = {'15/33': (thr('15'), thr('33')), '11/29': (thr('11'), thr('29'))}


def unit(a, b):
    L = math.dist(a, b)
    return ((b[0] - a[0]) / L, (b[1] - a[1]) / L), L


def rwy_dist(name, p):
    """Distância (com sinal) do ponto ao eixo da pista e posição ao longo dela."""
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    vx, vy = p[0] - a[0], p[1] - a[1]
    return vx * uy - vy * ux, vx * ux + vy * uy


def rwy_pt(name, t):
    a, b = RWY[name]
    (ux, uy), _ = unit(a, b)
    return (a[0] + ux * t, a[1] + uy * t)


# cruzamento das pistas
_d1, _t = rwy_dist('15/33', thr('11'))
(ux, uy), _ = unit(*RWY['11/29'])
_k = -_d1 / (ux * unit(*RWY['15/33'])[0][1] - uy * unit(*RWY['15/33'])[0][0])
XING = (thr('11')[0] + ux * _k, thr('11')[1] + uy * _k)

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
    on.append((rwy_dist(name, XING)[1], key(XING)))
    on.append((0, key(a)))
    on.append((L, key(b)))
    on = sorted(set(on))
    for (_, p), (_, q) in zip(on, on[1:]):
        w = math.dist(p, q) * 3
        G[p].append((q, 'RWY' + name, w))
        G[q].append((p, 'RWY' + name, w))


def refs_at(n):
    return {r for _, r, _ in G[n]}


def node_at(r1, r2, near=None):
    c = [n for n in G if r1 in refs_at(n) and r2 in refs_at(n)]
    if not c:
        raise SystemExit(f'sem interseção {r1}/{r2}')
    return c[0] if near is None else min(c, key=lambda n: math.dist(n, near))


def node_on(r, near):
    return min((n for n in G if r in refs_at(n)), key=lambda n: math.dist(n, near))


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
    'gnd': '#2f7fd0', 'twr': '#e0a100', 'tora': '#7b2fbf',
}

X0 = thr('15')[0] - 280
X1 = max(x for _, pts in TWY for x, _ in pts) + 260
Y0 = thr('29')[1] - 170
Y1 = max(y for p in BUILD for r in p for _, y in [xy(*q[:2]) for q in r]) + 150


def pl(pts):
    return 'M' + ' L'.join(f'{x:.0f},{y:.0f}' for x, y in pts)


def svg_open(title):
    W, H = X1 - X0, Y1 - Y0
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{X0:.0f} {Y0:.0f} {W:.0f} {H:.0f}" '
            f'width="{W/2.6:.0f}" height="{H/2.6:.0f}" role="img" aria-label="{title}" '
            f'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif">',
            f'<title>{title}</title>',
            '<defs>'
            + ''.join(f'<marker id="ar-{k}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3" orient="auto-start-reverse">'
                      f'<path d="M0,0 L10,5 L0,10 z" fill="{PAL[k]}"/></marker>' for k in ('dep', 'arr', 'alt'))
            + '</defs>',
            f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{W:.0f}" height="{H:.0f}" rx="40" fill="{PAL["bg"]}"/>']


def badge(x, y, t, fill=None, fg='#fff', size=48):
    fill = fill or PAL['rwy']
    w = size * 0.62 * len(t) + 24
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.72:.0f}" width="{w:.0f}" height="{size*1.44:.0f}" rx="8" fill="{fill}"/>'
            f'<text x="{x:.0f}" y="{y+size*0.36:.0f}" font-size="{size}" font-weight="700" fill="{fg}" text-anchor="middle">{t}</text></g>')


def tag(x, y, t, size=34):
    w = size * 0.66 * len(t) + 14
    return (f'<g><rect x="{x-w/2:.0f}" y="{y-size*0.68:.0f}" width="{w:.0f}" height="{size*1.36:.0f}" rx="5" fill="#1d1d1d"/>'
            f'<text x="{x:.0f}" y="{y+size*0.35:.0f}" font-size="{size}" font-weight="700" fill="#ffd400" text-anchor="middle">{t}</text></g>')


def base_layers(s, labels=True):
    s.append('<g>')
    for p in APRONS:
        s.append(f'<path d="{path_d(p)}" fill="{PAL["apron"]}" fill-rule="evenodd"/>')
    for ln in STAND_LINES:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="#bcc1c8" stroke-width="2"/>')
    for p in BUILD:
        s.append(f'<path d="{path_d(p)}" fill="{PAL["build"]}" fill-rule="evenodd"/>')
    for ref, pts in TWY:
        w = 6 if ref == 'HG' else 8
        s.append(f'<path d="{pl(pts)}" fill="none" stroke="{PAL["twy"]}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
    for name, (a, b) in RWY.items():
        (ux, uy), L = unit(a, b)
        s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{PAL["rwy"]}" stroke-width="45"/>')
        s.append(f'<line x1="{a[0]+ux*40:.1f}" y1="{a[1]+uy*40:.1f}" x2="{b[0]-ux*40:.1f}" y2="{b[1]-uy*40:.1f}" '
                 f'stroke="#fff" stroke-width="2.5" stroke-dasharray="36 28"/>')
    for ln in HOLD:
        s.append(f'<path d="{pl(ln)}" fill="none" stroke="{PAL["hold"]}" stroke-width="10"/>')
    s.append('</g>')
    for n1, n2 in (('15', '33'), ('11', '29')):
        a, b = thr(n1), thr(n2)
        (ux, uy), _ = unit(a, b)
        s.append(badge(a[0] - ux * 95, a[1] - uy * 95, n1))
        s.append(badge(b[0] + ux * 95, b[1] + uy * 95, n2))
    if labels:
        twy_labels(s)
        apron_labels(s)


def pt_on(ref, frac=0.5):
    best = max((pts for r, pts in TWY if r == ref), key=lambda p: sum(math.dist(a, b) for a, b in zip(p, p[1:])))
    L = [0]
    for a, b in zip(best, best[1:]):
        L.append(L[-1] + math.dist(a, b))
    t = L[-1] * frac
    for i in range(1, len(L)):
        if L[i] >= t:
            k = (t - L[i - 1]) / max(L[i] - L[i - 1], 1e-9)
            a, b = best[i - 1], best[i]
            return (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)


LABELS = [  # (ref, posição) ajustadas à mão para não sobrepor
    ('A', (-300, 20)), ('A', (-170, -55)), ('B', (60, -150)), ('B', (680, -170)),
    ('C', (-610, -125)), ('D', (262, -470)), ('E', (250, -215)), ('F', (950, -200)),
    ('G', (445, -90)), ('H', (630, -88)), ('J', (345, -95)), ('M', (745, -18)), ('N', (840, -95)),
    ('L', (1000, 30)), ('L', (1300, 200)),
]


def twy_labels(s):
    for ref, (x, y) in LABELS:
        s.append(tag(x, y, ref))


def centroid(refs):
    pts = [GATES[r] for r in refs if r in GATES]
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


def circle_num(s, x, y, t):
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="44" fill="#fff" stroke="{PAL["text"]}" stroke-width="6"/>'
             f'<text x="{x:.0f}" y="{y+16:.0f}" font-size="46" font-weight="700" fill="{PAL["text"]}" text-anchor="middle">{t}</text></g>')


def apron_labels(s):
    a1 = [r for r in GATES if r and int(''.join(c for c in r if c.isdigit())) <= 23]
    a2 = [r for r in GATES if r and r not in a1]
    x, y = centroid(a1)
    circle_num(s, x, y + 5, '1')
    x, y = centroid(a2)
    circle_num(s, x + 40, y + 10, '2')
    for t, (x, y) in (('TPS', (720, 180)), ('TECA', (-40, 110)), ('HANGARES', (-480, 200))):
        s.append(badge(x, y, t, fill='#fff', fg=PAL['build'], size=40))


def flow(s, pts, kind, dashed=False, width=18, arrow=True):
    da = ' stroke-dasharray="34 22"' if dashed else ''
    me = f' marker-end="url(#ar-{kind})"' if arrow else ''
    if not dashed:
        s.append(f'<path d="{pl(pts)}" fill="none" stroke="#fff" stroke-width="{width+10}" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append(f'<path d="{pl(pts)}" fill="none" stroke="{PAL[kind]}" stroke-width="{width}" stroke-linecap="round" '
             f'stroke-linejoin="round"{da}{me}/>')
    if not arrow:
        return
    segs = list(zip(pts, pts[1:]))
    total = sum(math.dist(a, b) for a, b in segs)
    step, acc, nxt = 330, 0, 330
    for a, b in segs:
        d = math.dist(a, b)
        while d and acc + d >= nxt and nxt < total - 120:
            k = (nxt - acc) / d
            x, y = a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k
            ang = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
            s.append(f'<path d="M-11,-10 L11,0 L-11,10 z" fill="#fff" transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})"/>')
            nxt += step
        acc += d


def north_arrow(s, x, y):
    nx, ny = math.sin(THETA), -math.cos(THETA)
    ang = math.degrees(math.atan2(ny, nx)) + 90
    s.append(f'<g transform="translate({x:.0f},{y:.0f}) rotate({ang:.1f})">'
             f'<path d="M0,-100 L28,34 L0,12 L-28,34 z" fill="{PAL["text"]}"/>'
             f'<text x="0" y="-118" font-size="38" font-weight="700" text-anchor="middle" fill="{PAL["text"]}">N</text></g>')


def scale_bar(s, x, y):
    s.append(f'<g fill="{PAL["text"]}"><rect x="{x}" y="{y}" width="200" height="12"/><rect x="{x+200}" y="{y}" width="200" height="12" fill="none" stroke="{PAL["text"]}" stroke-width="4"/>'
             f'<text x="{x}" y="{y-12}" font-size="28">0</text><text x="{x+400}" y="{y-12}" font-size="28" text-anchor="middle">400 m</text></g>')


def credit(s):
    s.append(f'<text x="{X1-30:.0f}" y="{Y1-28:.0f}" font-size="28" fill="{PAL["muted"]}" text-anchor="end">'
             f'Base: © OpenStreetMap contributors (ODbL) · ADC SBCT / AIP AD 2 SBCT · fora de escala para navegação</text>')


def callout(s, x, y, lines_, color, size=38):
    w = max(len(l) for l in lines_) * size * 0.56 + 28
    h = len(lines_) * size * 1.25 + 16
    rx = x - w / 2
    s.append(f'<rect x="{rx:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" rx="10" fill="#fff" stroke="{color}" stroke-width="5"/>')
    for i, l in enumerate(lines_):
        s.append(f'<text x="{x:.0f}" y="{y + 10 + size*1.05 + i*size*1.25:.0f}" font-size="{size}" font-weight="{700 if i == 0 else 400}" '
                 f'fill="{PAL["text"]}" text-anchor="middle">{l}</text>')


def leader(s, p, q, color):
    s.append(f'<line x1="{p[0]:.0f}" y1="{p[1]:.0f}" x2="{q[0]:.0f}" y2="{q[1]:.0f}" stroke="{color}" stroke-width="4"/>')


def frame(s):
    north_arrow(s, X1 - 140, Y0 + 180)
    scale_bar(s, X1 - 560, Y1 - 110)
    credit(s)


def save(name, s):
    s.append('</svg>')
    with open(os.path.join(OUT, name), 'w') as f:
        f.write('\n'.join(s))
    print('ok', name)


# nós de referência --------------------------------------------------------
R15 = lambda x: key(rwy_pt('15/33', x - thr('15')[0]))  # ponto no eixo da 15/33 pela coordenada x
THR11 = key(thr('11'))
C_A = node_on('C', (-535, 5))             # junção C/A na cabeceira 11
C_RWY_E = node_on('C', (-719, -275))      # C entrando na pista alinhado para leste (decolagem 15)
C_RWY_W = node_on('C', (-847, -274))      # C saindo da pista (pouso 33)
A_B = node_at('A', 'B')
A_HG = node_on('A', (-349, 30))
E_B = node_on('E', (181, -118))
E_RWY = node_on('E', (217, -274))
F_RWY = node_on('F', (975, -275))
F_B = node_on('F', (851, -147))
B_G = node_at('B', 'G')
B_H = node_on('B', (602, -118))
L_H = node_on('H', (570, -37))
L_G = node_on('G', (426, -42))
L_N = node_on('N', (839, -34))
L_J = node_on('J', (305, -65))
B_J = node_on('J', (247, -118))
D_RWY = node_on('D', (243, -715))
B_APN2 = node_on('B', (60, -125))

TORA_C = math.dist(C_RWY_E, thr('33'))

# ======================================================== 1. visão geral
s = svg_open('SBCT: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (C_RWY_E, (-560, -560), ['15 · C', 'TORA 1740 m']),
    (key(thr('15')), (-1150, -560), ['15 · cabeceira', 'TORA 2218 m', 'backtrack desde a C', '(HEAVY: desde a E)']),
    (F_RWY, (1000, -520), ['33 · F (cabeceira)', 'TORA 2218 m']),
    (C_A, (-1000, -150), ['11 · A (cabeceira)', 'TORA 1798 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy + 40), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbct-visao-geral.svg', s)

# ======================================================== 2. responsabilidade
def strip(name, half):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    e = 60
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


s = svg_open('SBCT: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="40" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{strip("15/33", 125)} {strip("11/29", 100)}" fill="{PAL["twr"]}" opacity="0.28" fill-rule="nonzero"/>')
base_layers(s)
s.append(f'<path d="{strip("15/33", 125)} {strip("11/29", 100)}" fill="none" stroke="{PAL["twr"]}" stroke-width="6" stroke-dasharray="26 16"/>')
callout(s, -50, -900, ['TWR', 'as duas pistas, os cruzamentos', 'e a TWY até o ponto de espera'], PAL['twr'], size=40)
callout(s, 1200, -760, ['GND', 'pátios 1 e 2, hangares,', 'TWY A, B, L, G, H, J, M, N', 'até o ponto de espera'], PAL['gnd'], size=40)


def num(x, y, t, col):
    s.append(f'<g><circle cx="{x:.0f}" cy="{y:.0f}" r="36" fill="{col}" stroke="#fff" stroke-width="6"/>'
             f'<text x="{x:.0f}" y="{y+15:.0f}" font-size="42" font-weight="700" fill="#fff" text-anchor="middle">{t}</text></g>')


num(-480, 85, '1', PAL['dep'])
num(900, -110, '1', PAL['dep'])
num(-380, 85, '2', PAL['arr'])
num(140, -200, '2', PAL['arr'])
num(800, -190, '2', PAL['arr'])
num(-460, -110, '3', PAL['twr'])
num(285, -330, '3', PAL['twr'])
frame(s)
save('sbct-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos
BARS = []


def stop_bar(pts, p):
    """Barra vermelha no ponto p (espera obrigatória antes de cruzar pista)."""
    BARS.append((p, pts))


def draw_bars(s):
    for (x, y), pts in BARS:
        i = min(range(len(pts) - 1), key=lambda i: math.dist(pts[i], (x, y)))
        a, b = pts[i], pts[i + 1]
        (ux, uy), _ = unit(a, b) if a != b else ((1, 0), 1)
        nx, ny = -uy * 55, ux * 55
        s.append(f'<g><line x1="{x-nx:.0f}" y1="{y-ny:.0f}" x2="{x+nx:.0f}" y2="{y+ny:.0f}" stroke="#fff" stroke-width="30" stroke-linecap="round"/>'
                 f'<line x1="{x-nx:.0f}" y1="{y-ny:.0f}" x2="{x+nx:.0f}" y2="{y+ny:.0f}" stroke="{PAL["hold"]}" stroke-width="18" stroke-linecap="round"/></g>')


def flow_map(fname, title, deps, arrs, exits=(), alts=(), notes=(), heavy=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, pts, 'dep', dashed=True, width=12)
    for pts in exits:
        flow(s, pts, 'dep', width=11, arrow=False)
    for pts in deps:
        flow(s, pts, 'dep', width=20)
    for pts in arrs:
        flow(s, pts, 'arr', width=15)
    for pts in heavy:
        flow(s, [(x, y - 16) for x, y in pts], 'alt', dashed=True, width=13)
    draw_bars(s)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y + 30), PAL[col])
        callout(s, x, y, ls, PAL[col])
    frame(s)
    save(fname, s)


TW = lambda *r: set(r)
EXITS = [
    route(L_G, B_G, {'G'}),
    route(L_H, B_H, {'H'}),
    route(L_J, B_J, {'J'}),
    route(L_N, F_B, {'N'}),
]

# --- sistema 11/15
BARS.clear()
HOLD_C15 = (-702 + 16, -146)
HOLD_A11 = (-418, 28)
dep15 = chain(B_H, TW('B'), A_B, TW('A'), A_HG, TW('A'), C_A, TW('C', 'A'), C_RWY_E)
dep11 = chain(A_HG, TW('A'), C_A)
back15 = [C_RWY_W, R15(thr('15')[0] + 60)]
arr15e = [R15(E_RWY[0] - 220)] + chain(E_RWY, TW('E'), E_B, TW('B', 'J'), B_J)
arr15f = [R15(thr('33')[0] - 260)] + chain(F_RWY, TW('F'), F_B, TW('N'), L_N)
stop_bar(dep15, (-418, 28))
HEAVY15 = chain(B_G, TW('B'), E_B, TW('E'), E_RWY, TW('RWY15/33'), key(thr('15')))
flow_map('sbct-fluxo-15.svg', 'SBCT: fluxo de solo, sistema 11/15',
         [dep15, dep11], [arr15e, arr15f], EXITS, [back15],
         [((-1000, -620), ['Jatos:', 'backtrack até a 15'], 'dep', (-1050, -275)),
          ((-430, -620), ['Leves e ATR:', 'decolam da C'], 'dep', C_RWY_E),
          ((330, -640), ['Pouso 15, leves:', 'livram pela E'], 'arr', E_RWY),
          ((-80, -860), ['HEAVY ou > 36 m:', 'entra pela E e', 'backtrack até a 15'], 'alt', R15(-60)),
          ((1050, -560), ['Pouso 15, ATR e jatos:', 'livram pela F'], 'arr', F_RWY)], heavy=[HEAVY15])

# --- sistema 29/33
BARS.clear()
dep33 = chain(B_APN2, TW('B'), F_B, TW('F'), F_RWY)
arr33c = [R15(C_RWY_W[0] + 220)] + chain(C_RWY_W, TW('C'), C_A, TW('A', 'C'), A_HG, TW('A'), A_B)
arr33r = [R15(XING[0] + 200)] + chain(key(XING), TW('RWY11/29'), C_A, TW('A'), A_HG)
stop_bar(arr33c, (-605 + 5, -62 + 4))
HEAVY33 = chain(C_RWY_W, TW('C'), C_A, TW('RWY11/29'), key(XING), TW('RWY15/33'), E_RWY, TW('E'), E_B)
flow_map('sbct-fluxo-33.svg', 'SBCT: fluxo de solo, sistema 29/33',
         [dep33], [arr33c, arr33r], EXITS, [],
         [((1050, -560), ['Decolagem 33:', 'pela F, TORA 2218 m'], 'dep', F_RWY),
          ((-900, -640), ['Pouso 33, ATR e jatos:', 'livram pela C'], 'arr', C_RWY_W),
          ((560, -640), ['HEAVY ou > 36 m: C, backtrack', 'na 29 e na 33, livra pela E'], 'alt', R15(90)),
          ((-140, -700), ['Pouso 33, leves:', 'livram pela pista 29', 'no sentido da A'], 'arr', key(rwy_pt('11/29', 300)))], heavy=[HEAVY33])
print('TORA C (geom.)', round(TORA_C))
