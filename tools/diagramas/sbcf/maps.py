# Mapas de SBCF (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '16/34'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'A': (1800, 290), 'R': (820, 128), 'S': (820, 60), 'T': (820, 20), 'Q': (2000, 120),
           'P': (3150, 300), 'B': (-420, 330)}
_best = {}
for ref, pts in TWY:
    if ref in (None, 'APN'):
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
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 40, a[1] + (b[1] - a[1]) * k - 24))))
            break
        acc += d

AP1 = node_on('R', (1200, 104))     # pátio 1
AP2 = node_on('R', (700, 105))      # pátio 2
B16 = node_on('B', (-471, 422))
C116 = node_on('C1', (470, 424))
F116 = node_on('F1', (1159, 423))
H34 = node_on('H', (2437, 423))
P34 = node_on('P', (3039, 422))

# ======================================================== 1. visão geral
s = svg_open('SBCF: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('16'), (-300, -330), ['16 · B (cabeceira)', 'TORA 3600 m']),
    (C116, (520, -330), ['16 · C1 (cód. A/B)', 'TORA 2720 m']),
    (H34, (2100, 480), ['34 · H (cód. A/B)', 'TORA 2987 m']),
    (thr('34'), (3000, 480), ['34 · P (cabeceira)', 'TORA 3600 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbcf-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 105)
s = svg_open('SBCF: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 1500, 540, ['TWR', 'pista 16/34 e TWY até o ponto de espera'], PAL['twr'])
callout(s, 1900, -360, ['GND', 'pátios, A e ligações até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbcf-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos


def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 10, y - 10) for x, y in pts], 'alt', dashed=True, width=14)
    for pts in deps:
        flow(s, pts, 'dep', width=20)
    for pts in arrs:
        flow(s, pts, 'arr', width=15)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y), PAL[col])
        callout(s, x, y, ls, PAL[col])
    frame(s)
    save(fname, s)


# --- pista 16
dep16 = chain(AP2, TW('R', 'APN', 'C2', 'A', 'B'), B16)
alt16 = chain(AP2, TW('R', 'APN', 'C2', 'C1'), C116)
arr16 = [rwy_pt(RW, 500)] + chain(F116, TW('F1', 'F2', 'R'), AP1)
flow_map('sbcf-fluxo-16.svg', 'SBCF: fluxo de solo, pista 16',
         [dep16], [arr16], [alt16],
         [((-300, -330), ['Decolagem 16:', 'A até a B (cabeceira)'], 'dep', node_on('A', (-200, 243))),
          ((520, -330), ['Código A/B: 16', 'pela C1 (TORA 2720 m)'], 'alt', C116),
          ((1300, 480), ['Pouso 16: livram pela F1', '(1765 m) e seguem pela F2'], 'arr', F116)])

# --- pista 34
dep34 = chain(AP1, TW('R', 'F2', 'A', 'P'), P34)
alt34 = chain(AP1, TW('R', 'F2', 'A', 'H'), H34)
arr34 = [rwy_pt(RW, L - 600)] + chain(C116, TW('C1', 'C2', 'APN', 'R'), AP2)
flow_map('sbcf-fluxo-34.svg', 'SBCF: fluxo de solo, pista 34',
         [dep34], [arr34], [alt34],
         [((3000, 480), ['Decolagem 34:', 'A até a P (cabeceira)'], 'dep', node_on('A', (2900, 220))),
          ((2100, 480), ['Código A/B: 34', 'pela H (TORA 2987 m)'], 'alt', H34),
          ((400, 480), ['Pouso 34: livram pela C1', '(2700 m) e seguem pela C2'], 'arr', C116)])
