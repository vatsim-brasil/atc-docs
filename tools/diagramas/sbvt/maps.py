# Mapas de SBVT (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)

# a M começa logo depois da cabeceira 24, sem ligação no OSM: liga a ponta da pista à M
_r, _l = rwy_node('06/24', math.dist(*RWY['06/24'])), node_on('M', (469, -838))
G[_r].append((_l, 'M', math.dist(_r, _l)))
G[_l].append((_r, 'M', math.dist(_r, _l)))

AP1 = node_on('N', (560, 760))
G02 = node_on('G', (783, 874))
J_RWY = node_on('J', (725, 157))
K02 = node_on('K', (618, -605))
K20 = node_on('K', (600, -733))
M20 = node_on('M', (562, -1007))
T02 = rwy_dist('02/20', thr('02'))[1]
T20 = rwy_dist('02/20', thr('20'))[1]

# ======================================================== 1. visão geral
s = svg_open('SBVT: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (G02, (-150, 960), ['02 · G ou H', 'TORA 2058 m']),
    (M20, (850, -1200), ['20 · M', 'TORA 2058 m']),
    (thr('06'), (-450, 950), ['06', 'TORA 1750 m']),
    (thr('24'), (150, -900), ['24 · F', 'TORA 1750 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="26" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbvt-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=50):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip('02/20', 90) + ' ' + strip('06/24', 90)
s = svg_open('SBVT: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="40" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="6" stroke-dasharray="26 16"/>')
twy_labels(s)
apron_labels(s)
callout(s, -250, -760, ['TWR', 'pistas 02/20 e 06/24', 'e TWY até o ponto de espera'], PAL['twr'])
callout(s, 150, 450, ['GND', 'pátios, A, F, N', 'e ligações até o', 'ponto de espera'], PAL['gnd'])
frame(s)
save('sbvt-responsabilidade.svg', s)

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


# --- pista 02
dep02 = chain(AP1, TW('N', 'F', 'G'), G02)
arr02k = [rwy_pt('02/20', T02 + 350)] + chain(K02, TW('K', 'F', 'N'), AP1)
arr02j = [rwy_pt('02/20', T02 + 150)] + chain(J_RWY, TW('J', 'F', 'N'), AP1)
flow_map('sbvt-fluxo-02.svg', 'SBVT: fluxo de solo, pista 02',
         [dep02], [arr02k], [arr02j],
         [((-150, 960), ['Decolagem 02:', 'N, F e G (ou H)'], 'dep', G02),
          ((150, -1000), ['Pouso 02: livram pela K', 'e seguem pela F até o', 'pátio 1. Evitar a M (HS 7)'], 'arr', K02),
          ((150, 500), ['Turboélices:', 'livram pela J'], 'alt', J_RWY)])

# --- pista 20
dep20 = chain(AP1, TW('N', 'F', 'RWY06/24', 'M'), M20)
arr20j = [rwy_pt('02/20', T20 - 350)] + chain(J_RWY, TW('J', 'F', 'N'), AP1)
flow_map('sbvt-fluxo-20.svg', 'SBVT: fluxo de solo, pista 20',
         [dep20], [arr20j], [],
         [((150, -1050), ['Decolagem 20: F, passa pela', 'cabeceira 24, e M'], 'dep', node_on('M', (520, -920))),
          ((150, 500), ['Pouso 20: livram pela J', 'e seguem pela F'], 'arr', J_RWY)])
