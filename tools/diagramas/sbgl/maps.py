# Mapas de SBGL (executado por gen.py, que define a geometria e as funções de desenho)

# J termina dentro do pátio 5 e H começa nele: o táxi entre as duas é pelo pátio (sem eixo no OSM)
_j, _h = node_on('J', (375, 2356)), node_on('H', (436, 2431))
G[_j].append((_h, 'J', math.dist(_j, _h)))
G[_h].append((_j, 'J', math.dist(_j, _h)))

AP1 = node_on('L1', (-292, -128))
AP2 = node_on('Y', (-120, 472))
AP2_L3 = node_on('L3', (-188, 580))
AP3_L4 = node_on('L4', (112, 1180))

# ======================================================== 1. visão geral
s = svg_open('SBGL: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (P_RWY, (-600, -1230), ['10 · P (cabeceira)', 'TORA 4000 m']),
    (Z_RWY, (3500, -1230), ['28 · Z (cabeceira)', 'TORA 4000 m']),
    (A_RWY, (-1050, -560), ['15 · A', 'TORA 3060 m']),
    (G_RWY, (1200, 2560), ['33 · G ou H', 'TORA 3050 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy + 50), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="40" fill="{PAL["tora"]}" stroke="#fff" stroke-width="8"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbgl-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=80):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


def hold_half(name):
    ds = [abs(rwy_dist(name, p)[0]) for ln in HOLD for p in ln]
    ds = [d for d in ds if 60 < d < 260]
    return sum(ds) / len(ds)


H1, H2 = hold_half('10/28'), hold_half('15/33')
STRIPS = f'{strip("10/28", H1)} {strip("15/33", H2)}'
RMP = [p for r, p in APRONS if r not in ('6', '7', '8', 'Líder Aviação e Aerorio')]

s = svg_open('SBGL: áreas de responsabilidade do Solo, da Torre e do Pátio')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
for p in RMP:
    s.append(f'<path d="{path_d(p)}" fill="{PAL["rmp"]}" opacity="0.35" stroke="{PAL["rmp"]}" stroke-width="8"/>')
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="8" stroke-dasharray="34 20"/>')
twy_labels(s)
apron_labels(s)
callout(s, 1250, -470, ['TWR', 'as duas pistas e as TWY', 'até o ponto de espera'], PAL['twr'])
callout(s, 2300, 600, ['GND', 'TWY B, K, N, M e ligações', 'até o ponto de espera;', 'pátios 6, 7 e 8'], PAL['gnd'])
callout(s, 2300, 1300, ['APRON (eventos)', 'pátios 1, 2, 3 e 5.', 'Sem APRON, o Solo assume'], PAL['rmp'])
frame(s)
save('sbgl-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos
BARS = []


def draw_bars(s):
    for (x, y), pts in BARS:
        i = min(range(len(pts) - 1), key=lambda i: math.dist(pts[i], (x, y)))
        a, b = pts[i], pts[i + 1]
        (ux, uy), _ = unit(a, b) if a != b else ((1, 0), 1)
        nx, ny = -uy * 70, ux * 70
        s.append(f'<g><line x1="{x-nx:.0f}" y1="{y-ny:.0f}" x2="{x+nx:.0f}" y2="{y+ny:.0f}" stroke="#fff" stroke-width="38" stroke-linecap="round"/>'
                 f'<line x1="{x-nx:.0f}" y1="{y-ny:.0f}" x2="{x+nx:.0f}" y2="{y+ny:.0f}" stroke="{PAL["hold"]}" stroke-width="24" stroke-linecap="round"/></g>')


def flow_map(fname, title, deps, arrs, heavy=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in deps:
        flow(s, pts, 'dep', width=26)
    for pts in arrs:
        flow(s, pts, 'arr', width=20)
    for pts in heavy:
        flow(s, [(x + 18, y - 18) for x, y in pts], 'alt', dashed=True, width=18)
    draw_bars(s)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y + 40), PAL[col])
        callout(s, x, y, ls, PAL[col])
    frame(s)
    save(fname, s)


TW = lambda *r: set(r)

# --- operação segregada: pousos 15, decolagens 10
BARS.clear()
dep10 = chain(AP2, TW('Y', 'Y1', 'Y2', 'L1'), AP1, TW('L1', 'N'), node_at('N', 'P', P_RWY), TW('P'), P_RWY)
dep10w = chain(AP2_L3, TW('L3', 'K'), node_on('K', (-700, -330)), TW('K', 'L1', 'N', 'M'), node_at('N', 'P', P_RWY), TW('P'), P_RWY)
arr15d = [rwy_pt('15/33', 1250)] + chain(D_RWY, TW('D', 'B', 'L3'), AP2_L3)
arr15e = [rwy_pt('15/33', 1750)] + chain(E_RWY, TW('E', 'B', 'L4'), AP3_L4)
flow_map('sbgl-fluxo-15-10.svg', 'SBGL: fluxo de solo, operação segregada (pousos 15, decolagens 10)',
         [dep10], [arr15d, arr15e], [dep10w],
         [((-1000, -1240), ['Decolagem 10:', 'L1, N e P'], 'dep', node_on('N', (-500, -600))),
          ((-1250, 900), ['Envergadura > 36 m:', 'L3, K, N e P'], 'alt', node_on('K', (-560, 160))),
          ((-900, 1560), ['Pouso 15: livram', 'pela D ou pela E'], 'arr', D_RWY)])

# --- operação convergente: pousos 28, decolagens 33
BARS.clear()
dep33 = chain(AP3_L4, TW('L4', 'B', 'G'), G_RWY)
dep33w = chain(AP3_L4, TW('L4', 'B', 'F'), F_RWY, TW('RWY15/33', 'F', 'J'), J_RWY, TW('J', 'H'), H_RWY)
BARS.append((node_on('F', rwy_pt('15/33', 2640)), dep33w))
arr28dd = [rwy_pt('10/28', 3150)] + chain(DD_RWY, TW('DD', 'N'), node_on('N', (-100, -740)))
arr28bb = [rwy_pt('10/28', 2250)] + chain(BB_RWY, TW('BB'), node_on('N', (860, -740)))
arr28m = chain(node_on('N', (-100, -740)), TW('N', 'L1'), AP1)
flow_map('sbgl-fluxo-28-33.svg', 'SBGL: fluxo de solo, operação convergente (pousos 28, decolagens 33)',
         [dep33], [arr28dd, arr28bb, arr28m], [dep33w],
         [((1350, 2230), ['Decolagem 33:', 'B até a G'], 'dep', G_RWY),
          ((-350, 2450), ['Envergadura > 36 m: F, cruza', 'a 15/33, J e H'], 'alt', J_RWY),
          ((2400, -1240), ['Pouso 28: livram', 'pela DD ou pela BB'], 'arr', DD_RWY)])
