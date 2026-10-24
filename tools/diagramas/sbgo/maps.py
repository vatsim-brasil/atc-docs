# Mapas de SBGO (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '14/32'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'A': (-100, 154), 'J': (300, -215), 'B': (-1180, 70), 'F': (-1130, -150), 'E': (1150, 70),
           'T': (1240, -160), 'H': (600, -140), 'G': (-720, -140), 'K': (0, -420), 'L': (900, -400),
           'C': (-150, 80), 'D': (800, 60), 'A1': (-280, 230)}
_best = {}
for ref, pts in TWY:
    if ref in (None, 'HANGARES 1', 'HANGARES 2'):
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

AP1 = node_on('A', (-520, 154))     # pátio 1 (aviação geral)
AP2 = node_on(None, (420, -520))    # pátio 2 (terminal)
F14 = node_on('F', (-1076, -53))
B14 = rwy_node(RW, 0)
T32 = node_on('T', (1169, -53))
E32 = node_on('E', (1169, -53))
H14 = node_on('H', (469, -53))
G32 = node_on('G', (-479, -53))
HS1 = (200, -205)

# ======================================================== 1. visão geral
s = svg_open('SBGO: visão geral, pátios e pontos de decolagem')
base_layers(s)
s.append(f'<ellipse cx="{HS1[0]}" cy="{HS1[1]}" rx="760" ry="48" fill="none" stroke="{PAL["hold"]}" stroke-width="7" stroke-dasharray="26 16"/>')
s.append(tag(HS1[0] - 620, HS1[1] - 70, 'HS1'))
pts = [
    (thr('14'), (-1050, -520), ['14 · F ou B (cabeceira)', 'TORA 2286 m']),
    (thr('32'), (1000, 330), ['32 · T ou E (cabeceira)', 'TORA 2286 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
callout(s, -420, -600, ['HS1: a J é paralela à pista', 'não confundir na final'], PAL['hold'])
frame(s)
save('sbgo-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 105, e=200)
s = svg_open('SBGO: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 1000, 330, ['TWR', 'pista 14/32 e TWY até o ponto de espera'], PAL['twr'])
callout(s, -350, -700, ['GND', 'pátios, A, J e ligações até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbgo-responsabilidade.svg', s)

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


# --- pista 14
dep14 = chain(AP2, TW('K', 'J', 'F'), F14)
alt14 = chain(AP1, TW('A', 'B'), B14)
arr14 = [rwy_pt(RW, 400)] + chain(H14, TW('H', 'J', 'L'), AP2)
flow_map('sbgo-fluxo-14.svg', 'SBGO: fluxo de solo, pista 14',
         [dep14], [arr14], [alt14],
         [((-1000, -560), ['Decolagem 14 (pátio 2):', 'K e J até a F'], 'dep', node_on('J', (-700, -225))),
          ((-900, 340), ['Pátio 1 (aviação geral):', 'A até a B'], 'alt', node_on('A', (-900, 154))),
          ((850, 330), ['Pouso 14: livram pela H', 'e seguem pela J e pela L'], 'arr', H14)])

# --- pista 32
dep32 = chain(AP2, TW('L', 'T'), T32)
alt32 = chain(AP1, TW('A', 'E'), E32)
arr32 = [rwy_pt(RW, L - 400)] + chain(G32, TW('G', 'J', 'K'), AP2)
flow_map('sbgo-fluxo-32.svg', 'SBGO: fluxo de solo, pista 32',
         [dep32], [arr32], [alt32],
         [((1000, -560), ['Decolagem 32 (pátio 2):', 'L até a T'], 'dep', node_on('L', (1000, -320))),
          ((900, 340), ['Pátio 1 (aviação geral):', 'A até a E'], 'alt', node_on('A', (800, 154))),
          ((-950, 340), ['Pouso 32: livram pela G', 'e seguem pela J e pela K'], 'arr', G32)])
