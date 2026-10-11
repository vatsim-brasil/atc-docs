# Mapas de SBBE (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)

# rótulos: ponto médio do trecho mais longo de cada TWY (ajustes à mão em LBL_FIX)
LBL_FIX = {}
_best = {}
for ref, pts in TWY:
    if ref in (None, APN, 'GIRO', 'TAG'):
        continue
    L_ = sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))
    if L_ > _best.get(ref, (0, None))[0]:
        _best[ref] = (L_, pts)
for ref, (L_, pts) in _best.items():
    acc, half = 0, L_ / 2
    for a, b in zip(pts, pts[1:]):
        d = math.dist(a, b)
        if acc + d >= half:
            k = (half - acc) / d
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 34, a[1] + (b[1] - a[1]) * k - 20))))
            break
        acc += d


def inter(p1, p2, p3, p4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def on_rwy(name, t0, t1, off=0):
    """Trecho sobre o eixo da pista, deslocado para o lado (off em metros) para não cobrir outra rota."""
    (ux, uy), _ = unit(*RWY[name])
    return [(x - uy * off, y + ux * off) for x, y in (rwy_pt(name, t0), rwy_pt(name, t1))]


X = inter(*RWY['07/25'], *RWY['03/21'])
L07, L03 = math.dist(*RWY['07/25']), math.dist(*RWY['03/21'])
AP3 = node_on(APN, (-130, 205))
AP4 = node_on(APN, (85, 450))
AP5 = node_on(APN, (450, -100))
C07 = node_on('C', rwy_pt('07/25', 262))
D07 = node_on('D', rwy_pt('07/25', 40))
B03 = node_on('B', rwy_pt('03/21', 60))
A03 = node_on('A', rwy_pt('03/21', 470))
H03 = node_on('H', rwy_pt('03/21', 740))

# ======================================================== 1. visão geral
s = svg_open('SBBE: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (C07, (-560, 620), ['07 · C', 'TORA 2475 m']),
    (thr('07'), (-760, 60), ['07 · D (cabeceira)', 'TORA 2800 m']),
    (B03, (800, 560), ['03 · B', 'TORA 1830 m']),
    (thr('25'), (800, -1450), ['25 (cabeceira)', 'TORA 2800 m']),
    (thr('21'), (650, -1250), ['21 (cabeceira)', 'TORA 1830 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="26" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbbe-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=50):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip('07/25', 90) + ' ' + strip('03/21', 90)
s = svg_open('SBBE: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="40" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="6" stroke-dasharray="26 16"/>')
twy_labels(s)
apron_labels(s)
callout(s, 900, -900, ['TWR', 'pistas 07/25 e 03/21', 'e TWY até o ponto de espera'], PAL['twr'])
callout(s, -550, -1000, ['GND', 'pátios e TWY', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbbe-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos


def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 8, y - 8) for x, y in pts], 'alt', dashed=True, width=12)
    for pts in deps:
        flow(s, pts, 'dep', width=17)
    for pts in arrs:
        flow(s, pts, 'arr', width=13)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y), PAL[col])
        callout(s, x, y, ls, PAL[col])
    frame(s)
    save(fname, s)


# --- pistas 07 e 03
T_X07 = rwy_dist('07/25', X)[1]
T_X03 = rwy_dist('03/21', X)[1]
dep07 = chain(AP3, TW(APN, 'C'), C07)
dep03 = chain(AP4, TW(APN, 'B'), B03)
alt07 = chain(AP3, TW(APN, 'D'), D07)
arr07 = on_rwy('07/25', 700, T_X07) + on_rwy('03/21', T_X03, 470, 14) + chain(A03, TW('A', APN), AP3)
arr03 = on_rwy('03/21', 300, 740, -14) + chain(H03, TW('H', APN), AP5)
flow_map('sbbe-fluxo-07-03.svg', 'SBBE: fluxo de solo, pistas 07 e 03',
         [dep07, dep03], [arr07, arr03], [alt07],
         [((-560, 600), ['Jatos: 07 pela C', '(TORA 2475 m)'], 'dep', C07),
          ((800, 560), ['Turboélices e pistão:', '03 pela B'], 'dep', B03),
          ((950, -900), ['Pouso 07: livrar na', 'interseção e seguir', 'pela 03/21 até a A'], 'arr', X),
          ((1000, -330), ['Pouso 03: A (pátios', '3 e 4) ou H (pátio 5)'], 'arr', H03)])

# --- pistas 25 e 21
dep25 = chain(AP3, TW(APN, 'C'), C07) + on_rwy('07/25', 262, L07, 16)
dep21 = chain(AP4, TW(APN, 'A'), A03) + on_rwy('03/21', 470, L03, -16)
arr25 = on_rwy('07/25', 1900, 262, -16) + chain(C07, TW('C', APN), AP3)
arr21 = on_rwy('03/21', 1450, 470, 16) + chain(A03, TW('A', APN), AP3)
flow_map('sbbe-fluxo-25-21.svg', 'SBBE: fluxo de solo, pistas 25 e 21',
         [dep25, dep21], [arr25, arr21], [],
         [((1000, -1100), ['Decolagem 25: C e', 'backtrack até a cabeceira'], 'dep', rwy_pt('07/25', 2250)),
          ((-550, -1250), ['Decolagem 21: A e', 'backtrack até a cabeceira'], 'dep', rwy_pt('03/21', 1650)),
          ((-560, 600), ['Pouso 25: livram', 'pela C'], 'arr', C07),
          ((800, 560), ['Pouso 21: livram', 'pela A'], 'arr', A03)])
