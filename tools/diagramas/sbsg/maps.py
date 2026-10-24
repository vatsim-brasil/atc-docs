# Mapas de SBSG (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '12/30'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'B': (-1100, -86), 'B1': (-1560, -40), 'B4': (1560, -40), 'A': (-490, -183), 'APN': (-1000, -285),
           'F': (-719, -205), 'E': (-262, -205), 'DD': (60, 0), 'CC': (530, 0)}
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
            LABELS.append(('APN 1' if ref == 'APN' else ref,
                           LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 40, a[1] + (b[1] - a[1]) * k - 24))))
            break
        acc += d


def near(p):
    return min(G, key=lambda n: math.dist(n, p))


AP1 = node_on('APN', (-160, -285))   # pátio 1
AP2 = node_on('APN', (-700, -285))   # pátio 2
B1_12 = node_on('B1', (-1421, 104))  # B1 na pista (cabeceira 12)
B4_30 = node_on('B4', (1415, 105))   # B4 na pista (cabeceira 30)
DD12 = node_on('DD', (-112, 104))    # DD (saída rápida da 12)
CC12 = node_on('CC', (359, 104))
DD30 = near((181, 104))              # ligação da pista à DD para quem pousa na 30
CC30 = near((651, 104))

T_DD12 = rwy_dist(RW, DD12)[1]
T_CC12 = rwy_dist(RW, CC12)[1]
T_DD30 = L - rwy_dist(RW, DD30)[1]
T_CC30 = L - rwy_dist(RW, CC30)[1]
print(f'saídas: 12 DD {T_DD12:.0f} CC {T_CC12:.0f} | 30 CC {T_CC30:.0f} DD {T_DD30:.0f}')

# ======================================================== 1. visão geral
s = svg_open('SBSG: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('12'), (-1150, 200), ['12 · B1 (cabeceira)', 'TORA 3000 m']),
    (thr('30'), (1150, 200), ['30 · B4 (cabeceira)', 'TORA 3000 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbsg-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 105)
s = svg_open('SBSG: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 0, 220, ['TWR', 'pista 12/30 e TWY até o ponto de espera'], PAL['twr'])
callout(s, 800, -520, ['GND', 'pátios, APN 1, A, B, E, F e ligações', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbsg-responsabilidade.svg', s)

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


# --- pista 12
dep12 = chain(AP2, TW('APN', 'F', 'B', 'B1'), B1_12)
arr12 = [rwy_pt(RW, 600)] + chain(DD12, TW('DD', 'B', 'E', 'APN'), AP1)
flow_map('sbsg-fluxo-12.svg', 'SBSG: fluxo de solo, pista 12',
         [dep12], [arr12], [],
         [((-850, 190), ['Decolagem 12:', 'F ou E, B até a B1'], 'dep', node_on('B', (-1000, -86))),
          ((350, 190), ['Pouso 12: livram pela DD', f'(~{T_DD12:.0f} m) ou CC (~{T_CC12:.0f} m)'], 'arr', DD12)])

# --- pista 30
dep30 = chain(AP1, TW('APN', 'E', 'B', 'B4'), B4_30)
arr30 = [rwy_pt(RW, L - 500)] + chain(DD30, TW('DD', 'B', 'F', 'APN'), AP2)
flow_map('sbsg-fluxo-30.svg', 'SBSG: fluxo de solo, pista 30',
         [dep30], [arr30], [],
         [((1050, 190), ['Decolagem 30:', 'E ou F, B até a B4'], 'dep', node_on('B', (1100, -86))),
          ((-300, 330), [f'Pouso 30: livram pela DD', f'(~{T_DD30:.0f} m) ou no fim pela B1'], 'arr', DD30)])
