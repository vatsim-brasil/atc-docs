# Mapas de SBBR (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {}
SEM_ROTULO = {None, 'M1', 'M2', 'L5A', 'L5B'}
_best = {}
for ref, pts in TWY:
    if ref in SEM_ROTULO:
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
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 50, a[1] + (b[1] - a[1]) * k - 34))))
            break
        acc += d


def on_rwy(name, t0, t1, off=0):
    """Trecho sobre o eixo da pista, deslocado para o lado (off em metros) para não cobrir outra rota."""
    (ux, uy), _ = unit(*RWY[name])
    return [(x - uy * off, y + ux * off) for x, y in (rwy_pt(name, t0), rwy_pt(name, t1))]


N, S = '11L/29R', '11R/29L'
LN, LS = math.dist(*RWY[N]), math.dist(*RWY[S])
tN = lambda p: rwy_dist(N, p)[1]
tS = lambda p: rwy_dist(S, p)[1]

A11L = node_on('A', (-754, -896))
C11L = node_on('C', (-144, -896))
F29R = node_on('F', (1042, -898))
G29R = node_on('G', (742, -897))
B29R = node_on('B', (2227, -895))
Y11R = node_on('Y', (-2280, 904))
BB11R = node_on('BB', (-1349, 906))
EE29L = node_on('EE', (-233, 901))
Z29L = node_on('Z', (870, 903))
AP1N = node_on('L2', (92, -600))     # saída do pátio 1 para a H
AP1W = node_on('L1', (-100, -548))
AP1S = node_on('R', (190, -150))     # frente leste do pátio 1, para a U
AP1K = node_on('K', (289, -150))
HS = {'HS1': (-505, -682), 'HS2': (232, 702)}


def hotspots(s):
    for t, (x, y) in HS.items():
        s.append(f'<circle cx="{x}" cy="{y}" r="80" fill="#e5484d" opacity="0.35"/>')
        s.append(f'<text x="{x + 95}" y="{y + 110}" font-size="50" font-weight="700" fill="#c62a2f">{t}</text>')


# ======================================================== 1. visão geral
s = svg_open('SBBR: visão geral, pátios e pontos de decolagem')
base_layers(s)
hotspots(s)
pts = [
    (A11L, (-1500, -1200), ['11L · A', 'TORA 3050 m']),
    (C11L, (-450, -1200), ['11L · C (cód. A/B)', 'TORA 2193 m']),
    (F29R, (900, -1200), ['29R · F (cód. A/B)', 'TORA 1956 m']),
    (B29R, (2050, -1200), ['29R · B', 'TORA 3200 m']),
    (Y11R, (-2050, 1020), ['11R · Y', 'TORA 3150 m']),
    (BB11R, (-1100, 1020), ['11R · BB (cód. A/B)', 'TORA 2188 m']),
    (EE29L, (0, 1020), ['29L · EE (cód. A/B)', 'TORA 2161 m']),
    (Z29L, (1100, 1020), ['29L · Z', 'TORA 3300 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="40" fill="{PAL["tora"]}" stroke="#fff" stroke-width="9"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbbr-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


s = svg_open('SBBR: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="40" fill="{PAL["gnd"]}" opacity="0.12"/>')
for name in RWY:
    s.append(f'<path d="{strip(name, 107)}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
for name in RWY:
    s.append(f'<path d="{strip(name, 107)}" fill="none" stroke="{PAL["twr"]}" stroke-width="9" stroke-dasharray="40 24"/>')
twy_labels(s)
apron_labels(s)
callout(s, 300, -1200, ['TWR (N quando dividida)', 'pista 11L/29R e TWY até o ponto de espera'], PAL['twr'])
callout(s, -700, 1020, ['TWR (S quando dividida)', 'pista 11R/29L e TWY até o ponto de espera'], PAL['twr'])
callout(s, 1950, 150, ['GND', 'pátios e TWY', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbbr-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos


def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 12, y - 12) for x, y in pts], 'alt', dashed=True, width=20)
    for pts in deps:
        flow(s, pts, 'dep', width=30)
    for pts in arrs:
        flow(s, pts, 'arr', width=24)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y), PAL[col])
        callout(s, x, y, ls, PAL[col])
    frame(s)
    save(fname, s)


# --- pistas 11L e 11R
dep11L = chain(AP1W, TW('L1', 'H', 'A'), A11L)
dep11R = chain(AP1S, TW('R', 'U', 'Y'), Y11R)
alt11L = chain(AP1W, TW('L1', 'C'), C11L)
alt11R = chain(AP1S, TW('R', 'U', 'BB'), BB11R)
arr11L = on_rwy(N, 700, tN(F29R)) + chain(F29R, TW('F', 'H', 'L2'), AP1N)
arr11R = on_rwy(S, 800, tS(EE29L)) + chain(EE29L, TW('EE', 'K'), AP1K)
flow_map('sbbr-fluxo-11.svg', 'SBBR: fluxo de solo, pistas 11L e 11R',
         [dep11L, dep11R], [arr11L, arr11R], [alt11L, alt11R],
         [((-1500, -1200), ['Decolagem 11L (N/NE):', 'L1, H e A'], 'dep', node_on('H', (-800, -684))),
          ((-450, -1200), ['Código A/B: 11L', 'pela C'], 'alt', C11L),
          ((1200, -1200), ['Pouso 11L: livram pela F', '(ou G) e seguem pela H'], 'arr', F29R),
          ((-2050, 1020), ['Decolagem 11R (S/SE):', 'R, U e Y'], 'dep', node_on('U', (-2000, 705))),
          ((-1000, 1020), ['Código A/B: 11R', 'pela BB'], 'alt', BB11R),
          ((300, 1020), ['Pouso 11R: livram pela EE', 'e seguem pela K'], 'arr', EE29L)])

# --- pistas 29R e 29L
dep29R = chain(AP1N, TW('L2', 'H', 'B'), B29R)
dep29L = chain(AP1K, TW('K', 'U', 'Z'), Z29L)
alt29R = chain(AP1N, TW('L2', 'H', 'F'), F29R)
alt29L = chain(AP1K, TW('K', 'U', 'EE'), EE29L)
arr29R = on_rwy(N, LN - 700, tN(G29R)) + chain(G29R, TW('G', 'H', 'L2'), AP1N)
arr29L = on_rwy(S, LS - 800, tS(BB11R)) + chain(BB11R, TW('BB', 'U', 'R'), AP1S)
flow_map('sbbr-fluxo-29.svg', 'SBBR: fluxo de solo, pistas 29R e 29L',
         [dep29R, dep29L], [arr29R, arr29L], [alt29R, alt29L],
         [((2050, -1200), ['Decolagem 29R (N/NE):', 'L2, H e B'], 'dep', node_on('H', (1900, -690))),
          ((950, -1200), ['Código A/B: 29R', 'pela F'], 'alt', F29R),
          ((-300, -1200), ['Pouso 29R: livram pela G', '(ou C) e seguem pela H'], 'arr', G29R),
          ((1600, 1020), ['Decolagem 29L (S/SE):', 'K, U e Z'], 'dep', Z29L),
          ((400, 1020), ['Código A/B: 29L', 'pela EE'], 'alt', EE29L),
          ((-1300, 1020), ['Pouso 29L: livram pela BB', 'e seguem pela U'], 'arr', BB11R)])
