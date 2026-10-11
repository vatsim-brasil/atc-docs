# Mapas de SBRJ (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
MAIN, AUX = '02R/20L', '02L/20R'

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {}
_best = {}
for ref, pts in TWY:
    if ref is None:
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
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 22, a[1] + (b[1] - a[1]) * k - 16))))
            break
        acc += d

LM = math.dist(*RWY[MAIN])
AP1 = node_on('J', (-300, -288))
AP2 = node_on('B', (219, -230))
A20 = node_on('A', rwy_pt(MAIN, 1260))
E02 = node_on('E', rwy_pt(MAIN, 80))
H_M = node_on('H', rwy_pt(MAIN, 940))
G_M = node_on('G', rwy_pt(MAIN, 340))
A20R = node_on('A', rwy_pt(AUX, 1215))
D02L = node_on('D', rwy_pt(AUX, 19))

# ======================================================== 1. visão geral
s = svg_open('SBRJ: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('02R'), (-700, 180), ['02R · E', 'TORA 1323 m']),
    (thr('20L'), (600, 180), ['20L · A', 'TORA 1323 m']),
    (thr('02L'), (-750, -560), ['02L · D', 'TORA 1260 m']),
    (thr('20R'), (330, -560), ['20R · A', 'TORA 1260 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="18" fill="{PAL["tora"]}" stroke="#fff" stroke-width="5"/>')
    callout(s, cx, cy, ls, PAL['tora'], size=20)
frame(s)
save('sbrj-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, h1, h2, e=40):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * h1, a[1] - uy * e + ny * h1), (b[0] + ux * e + nx * h1, b[1] + uy * e + ny * h1),
         (b[0] + ux * e - nx * h2, b[1] + uy * e - ny * h2), (a[0] - ux * e - nx * h2, a[1] - uy * e - ny * h2)]
    return pl(p) + ' Z'


ya, ym = thr('02L')[1], thr('02R')[1]
x0, x1 = min(thr('02R')[0], thr('02L')[0]) - 40, thr('20L')[0] + 40
y0, y1 = min(ya, ym) - 60, max(ya, ym) + 45
STRIPS = f'M{x0:.0f},{y0:.0f} L{x1:.0f},{y0:.0f} L{x1:.0f},{y1:.0f} L{x0:.0f},{y1:.0f} Z'
s = svg_open('SBRJ: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="30" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="5" stroke-dasharray="20 12"/>')
twy_labels(s)
apron_labels(s)
callout(s, 450, 120, ['TWR', 'as duas pistas, o espaço entre elas', 'e as TWY até o ponto de espera'], PAL['twr'], size=20)
callout(s, -650, -560, ['GND', 'pátios e TWY', 'até o ponto de espera'], PAL['gnd'], size=20)
frame(s)
save('sbrj-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos


def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 6, y - 6) for x, y in pts], 'alt', dashed=True, width=9)
    for pts in deps:
        flow(s, pts, 'dep', width=13)
    for pts in arrs:
        flow(s, pts, 'arr', width=10)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y), PAL[col])
        callout(s, x, y, ls, PAL[col], size=20)
    frame(s)
    save(fname, s)


# --- pistas 20
dep20 = chain(AP1, TW('J', 'A'), A20)
arr20 = [rwy_pt(MAIN, LM - 300)] + chain(G_M, TW('G', 'C', 'K', 'J'), AP1)
alt20 = chain(AP2, TW('B', 'J', 'A'), A20R)
flow_map('sbrj-fluxo-20.svg', 'SBRJ: fluxo de solo, pistas 20L e 20R',
         [dep20], [arr20], [alt20],
         [((600, 170), ['Decolagem 20L: J e A,', 'cruzando a 20R'], 'dep', A20),
          ((-650, 170), ['Pouso 20L: livram pela G', 'e cruzam a 02L/20R pela C'], 'arr', G_M),
          ((300, -560), ['Pista auxiliar 20R:', 'aviação geral pela A'], 'alt', A20R)])

# --- pistas 02
dep02 = chain(AP1, TW('J', 'K', 'D', 'E'), E02)
arr02 = [rwy_pt(MAIN, 300)] + chain(H_M, TW('H', 'B', 'J'), AP1)
alt02 = chain(AP2, TW('B', 'J', 'K', 'D'), D02L)
flow_map('sbrj-fluxo-02.svg', 'SBRJ: fluxo de solo, pistas 02R e 02L',
         [dep02], [arr02], [alt02],
         [((-650, 170), ['Decolagem 02R: J, K, D e E,', 'cruzando a 02L'], 'dep', E02),
          ((550, 170), ['Pouso 02R: livram pela H', 'e cruzam a 02L/20R pela B'], 'arr', H_M),
          ((-700, -560), ['Pista auxiliar 02L:', 'aviação geral pela D'], 'alt', D02L)])
