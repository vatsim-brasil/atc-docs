# Mapas de SBEG (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)

AP1 = node_on('APN', (450, -750))
AP2 = node_on('APN', (1250, -1000))
A11 = node_on('A', (-1189, -278))    # A chega à pista junto da cabeceira 11
B29 = node_on('B', (1359, -278))     # B chega à pista junto da cabeceira 29
L = math.dist(*RWY['11/29'])

# ======================================================== 1. visão geral
s = svg_open('SBEG: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (A11, (-1000, -900), ['11 · A (cabeceira)', 'TORA 2700 m']),
    (B29, (600, -560), ['29 · B (cabeceira)', 'TORA 2700 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbeg-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip('11/29', 105)
s = svg_open('SBEG: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 150, -520, ['TWR', 'pista 11/29 e TWY', 'até o ponto de espera'], PAL['twr'])
callout(s, -500, -1000, ['GND', 'pátios 1 a 5, A e B', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbeg-responsabilidade.svg', s)

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


# --- pista 11
dep11 = chain(AP1, TW('APN', 'A'), A11)
alt11 = chain(AP2, TW('APN'), AP1)
arr11 = [rwy_pt('11/29', 900)] + chain(B29, TW('B', 'APN'), AP2)
flow_map('sbeg-fluxo-11.svg', 'SBEG: fluxo de solo, pista 11',
         [dep11], [arr11], [alt11],
         [((-850, -900), ['Decolagem 11: A até', 'a cabeceira 11'], 'dep', node_on('A', (-700, -480))),
          ((-250, -1200), ['Pátios 2 a 5: pela', 'pista de táxi do pátio'], 'alt', node_on('APN', (900, -900))),
          ((350, -560), ['Pouso 11: rolar até', 'o fim e livrar pela B'], 'arr', node_on('B', (1300, -430)))])

# --- pista 29
dep29 = chain(AP2, TW('APN', 'B'), B29)
alt29 = chain(AP1, TW('APN'), node_on('APN', (742, -839)))
arr29 = [rwy_pt('11/29', L - 900)] + chain(A11, TW('A', 'APN'), AP1)
flow_map('sbeg-fluxo-29.svg', 'SBEG: fluxo de solo, pista 29',
         [dep29], [arr29], [alt29],
         [((450, -560), ['Decolagem 29: B até', 'a cabeceira 29'], 'dep', node_on('B', (1300, -430))),
          ((-850, -900), ['Pouso 29: rolar até', 'o fim e livrar pela A'], 'arr', node_on('A', (-700, -480)))])
