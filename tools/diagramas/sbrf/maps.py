# Mapas de SBRF (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)

AP1 = node_on('N', (-62, -207))
AP2 = node_on('M', (800, -115))
AP3 = node_on('K', (260, 202))
AP4 = node_on('K', (-182, 202))
HGR = node_on('W', (-753, 427))

M18 = node_on('M', (-1356, 43))      # entrada da M no início da pista
B18 = node_on('B', (-130, 44))
B36 = node_on('B', (-130, 44))
G18 = node_on('G', (-227, 44))
G36 = node_on('G', (-227, 44))
J18 = node_on('J', (-734, 44))
L18 = node_on('L', (599, 43))
C36 = node_on('C', (1464, 43))
D36 = node_on('D', (1452, 43))
T18 = rwy_dist('18/36', thr('18'))[1]
T36 = rwy_dist('18/36', thr('36'))[1]

# ======================================================== 1. visão geral
s = svg_open('SBRF: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (M18, (-1150, -470), ['18 · M (início da pista)', 'TORA 2937 m']),
    (B18, (-420, -470), ['18 · B', 'TORA 1609 m']),
    (G18, (-380, 400), ['18 · G', 'TORA 1703 m']),
    (J18, (-1180, 300), ['18 · J', 'TORA 2186 m']),
    (C36, (1350, 330), ['36 · C ou D', 'TORA 2751 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy + (0 if cy < 0 else 0)), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbrf-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip('18/36', 105)
s = svg_open('SBRF: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, -1000, -470, ['TWR', 'pista 18/36 e TWY', 'até o ponto de espera'], PAL['twr'])
callout(s, 1250, 330, ['GND', 'pátios, M, K, D e ligações', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbrf-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos


def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 12, y - 12) for x, y in pts], 'alt', dashed=True, width=14)
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


# --- pista 18
dep18 = chain(AP2, TW('M'), M18)
alt18b = chain(AP2, TW('M', 'B'), B18)
alt18g = chain(AP4, TW('K', 'G'), G18)
arr18l = [rwy_pt('18/36', T18 + 450)] + chain(L18, TW('L', 'M'), AP2)
arr18e = [rwy_pt('18/36', T18 + 1500)] + chain(L18, TW('E', 'K'), AP3)
flow_map('sbrf-fluxo-18.svg', 'SBRF: fluxo de solo, pista 18',
         [dep18], [arr18l, arr18e], [alt18b, alt18g],
         [((-1050, -470), ['Decolagem 18: M até', 'o início da pista'], 'dep', node_on('M', (-1100, -40))),
          ((-450, -470), ['Turboélices e cód. A/B:', 'interseção B, G ou J'], 'alt', B18),
          ((1250, 330), ['Pouso 18: livram', 'pela L (pátio 2) ou E'], 'arr', L18)])

# --- pista 36
dep36 = chain(AP2, TW('M', 'C'), C36)
alt36 = chain(AP4, TW('K', 'D'), D36)
arr36b = [rwy_pt('18/36', T36 - 450)] + chain(B36, TW('B', 'M'), AP2)
arr36g = [rwy_pt('18/36', T36 - 1400)] + chain(G36, TW('G', 'K'), AP4)
flow_map('sbrf-fluxo-36.svg', 'SBRF: fluxo de solo, pista 36',
         [dep36], [arr36b, arr36g], [alt36],
         [((1380, -330), ['Decolagem 36:', 'M e C'], 'dep', node_on('C', (1480, -20))),
          ((1150, 380), ['Pátios oeste:', 'K e D'], 'alt', node_on('D', (1200, 200))),
          ((-700, -470), ['Pouso 36: livram', 'pela B (pátio 2) ou G'], 'arr', B36)])
