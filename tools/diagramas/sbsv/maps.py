# Mapas de SBSV (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)

AP1 = node_on('J1', (-1216, 206))
AP2 = node_on('H', (-348, -205))
C10 = node_on('C', (-1262, -6))
B10 = node_on('B', (-1450, -6))
D10 = node_on('D', (-349, -6))
G28 = node_on('G', (1419, -7))
F10 = node_on('F', (485, -6))
F28 = node_on('F', (686, -7))
E10 = node_on('E', (0, -6))
T10 = rwy_dist('10/28', thr('10'))[1]
T28 = rwy_dist('10/28', thr('28'))[1]
N17 = node_on('N', (-2205, -476))
L35 = node_on('L', (-1633, 769))

# ======================================================== 1. visão geral
s = svg_open('SBSV: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (C10, (-1250, -560), ['10 · C', 'TORA 2776 m']),
    (D10, (-620, -560), ['10 · D ou H (turboélices)', 'TORA 1848 m']),
    (G28, (1250, -420), ['28 · G', 'TORA 2883 m']),
    (thr('17'), (-1750, -560), ['17', 'TORA 1518 m']),
    (thr('35'), (-2200, 800), ['35', 'TORA 1518 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="34" fill="{PAL["tora"]}" stroke="#fff" stroke-width="7"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbsv-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip('10/28', 105) + ' ' + strip('17/35', 75)
s = svg_open('SBSV: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 700, -480, ['TWR', 'pistas 10/28 e 17/35 e TWY', 'até o ponto de espera'], PAL['twr'])
callout(s, 800, 500, ['GND', 'pátios, A, K, M e ligações', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbsv-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos


def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 12, y - 12) for x, y in pts], 'alt', dashed=True, width=16)
    for pts in deps:
        flow(s, pts, 'dep', width=22)
    for pts in arrs:
        flow(s, pts, 'arr', width=17)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y), PAL[col])
        callout(s, x, y, ls, PAL[col])
    frame(s)
    save(fname, s)


# --- pista 10
dep10 = chain(AP1, TW('J1', 'A', 'C'), C10)
alt10 = chain(AP1, TW('J1', 'A', 'D'), D10)
arr10f = [rwy_pt('10/28', T10 + 500)] + chain(F10, TW('F', 'A', 'J1'), AP1)
flow_map('sbsv-fluxo-10.svg', 'SBSV: fluxo de solo, pista 10',
         [dep10], [arr10f], [alt10],
         [((-1250, -560), ['Decolagem 10:', 'J1, A e C'], 'dep', C10),
          ((-500, -560), ['Turboélices:', 'interseção D'], 'alt', D10),
          ((900, 480), ['Pouso 10: livram pela F', '(turboélices: D) e seguem pela A'], 'arr', F10)])

# --- pista 28
dep28 = chain(AP1, TW('J1', 'A', 'G'), G28)
arr28d = [rwy_pt('10/28', T28 - 500)] + chain(D10, TW('D', 'K', 'J2', 'J1'), AP1)
flow_map('sbsv-fluxo-28.svg', 'SBSV: fluxo de solo, pista 28',
         [dep28], [arr28d], [],
         [((1150, 480), ['Decolagem 28:', 'A até a G'], 'dep', node_on('G', (1460, 120))),
          ((-700, -560), ['Pouso 28: livram', 'pela D, K até o pátio 1'], 'arr', D10)])
