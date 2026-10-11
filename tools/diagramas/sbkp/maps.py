# Mapas de SBKP (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '15/33'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'C': (300, 210), 'G': (-500, 310)}
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
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 40, a[1] + (b[1] - a[1]) * k - 24))))
            break
        acc += d

T = lambda p: rwy_dist(RW, p)[1]
AP4 = node_on('N1', (-1100, 537))
AP3 = node_on('G', (-800, 350))
D15 = node_on('D', thr('15'))
H15 = node_on('H', rwy_pt(RW, T((-1350, 44))))
A15 = node_on('A', rwy_pt(RW, 1250))
B15 = node_on('B', rwy_pt(RW, T((214, 44))))
F15 = node_on('F', rwy_pt(RW, T((624, 44))))
E33 = node_on('E', thr('33'))

HS = {'HS1': (-1600, 340), 'HS3': (-160, 210), 'HS5': (-900, 345), 'HS6': (930, 140)}


def hotspots(s):
    for t, (x, y) in HS.items():
        s.append(f'<circle cx="{x}" cy="{y}" r="60" fill="#e5484d" opacity="0.35"/>')
        s.append(f'<text x="{x + 66}" y="{y + 80}" font-size="40" font-weight="700" fill="#c62a2f">{t}</text>')


# ======================================================== 1. visão geral
s = svg_open('SBKP: visão geral, pátios e pontos de decolagem')
base_layers(s)
hotspots(s)
pts = [
    (D15, (-1500, -320), ['15 · D (cabeceira)', 'TORA 3150 m']),
    (H15, (-700, -320), ['15 · H (cód. A/B/C)', 'TORA 2910 m']),
    (F15, (600, -320), ['33 · F (cód. A/B)', 'TORA 2208 m']),
    (thr('33'), (1450, -320), ['33 · E (cabeceira)', 'TORA 3240 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbkp-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 105)
s = svg_open('SBKP: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 0, -320, ['TWR', 'pista 15/33 e TWY até o ponto de espera'], PAL['twr'])
callout(s, 800, 900, ['GND', 'pátios, C, G e ligações', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbkp-responsabilidade.svg', s)

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


# --- pista 15
dep15 = chain(AP4, TW('N1', 'K1', 'K2', 'G', 'C', 'H'), H15)
alt15 = chain(AP4, TW('N1', 'L1', 'M', 'D'), D15)
arr15 = [rwy_pt(RW, 500)] + chain(B15, TW('B', 'A', 'C', 'G', 'K2', 'K1', 'N2'), node_on('N2', (-1100, 581)))
arr15f = [rwy_pt(RW, 1700)] + chain(F15, TW('F', 'C', 'J', 'J1', 'K'), node_on('K', (-150, 470)))
flow_map('sbkp-fluxo-15.svg', 'SBKP: fluxo de solo, pista 15',
         [dep15], [arr15], [alt15, arr15f],
         [((-700, -320), ['Cód. A/B/C: 15 pela H', '(TORA 2910 m)'], 'dep', H15),
          ((-1500, -320), ['Cód. D/E: pista inteira', 'pela D'], 'alt', D15),
          ((300, -320), ['Pouso 15: livram pela', 'A ou B (cód. A-D)'], 'arr', B15),
          ((1300, -320), ['Cód. C/D: também', 'pela F (2200 m)'], 'alt', F15)])

# --- pista 33
dep33 = chain(AP4, TW('N1', 'K1', 'K2', 'G', 'C', 'E'), E33)
alt33 = chain(AP4, TW('N1', 'K1', 'K2', 'G', 'C', 'F'), F15)
arr33 = [rwy_pt(RW, L - 300)] + chain(B15, TW('B', 'C', 'J', 'J1', 'K'), node_on('K', (-150, 470)))
flow_map('sbkp-fluxo-33.svg', 'SBKP: fluxo de solo, pista 33',
         [dep33], [arr33], [alt33],
         [((1450, -320), ['Decolagem 33:', 'C até a E (cabeceira)'], 'dep', node_on('C', (1500, 250))),
          ((650, -320), ['Cód. A/B: 33 pela F', '(TORA 2208 m)'], 'alt', F15),
          ((-300, -320), ['Pouso 33: livram pela B', '(1350 m)'], 'arr', B15)])
