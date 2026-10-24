# Mapas de SBCY (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '17/35'
R = 'RWY' + RW
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'A': (60, 135), 'B': (240, 135), 'C': (560, 135), 'D': (1480, 150),
           'E': (1000, 150), 'F': (1000, 345), 'G': (1520, 300)}
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

AP1 = node_on('E', (-250, 196))   # pátio 1 (terminal)
AP2 = node_on('E', (414, 196))    # pátio 2
# pontos do eixo onde cada TWY encontra a pista (distância da cabeceira 17, medida no GND_DRAW)
A_R = rwy_node(RW, 837)
B_R = rwy_node(RW, 1008)
C_R = rwy_node(RW, 1324)
D_R = rwy_node(RW, 2257)
T17 = rwy_node(RW, 0)
T35 = rwy_node(RW, L)

# ======================================================== 1. visão geral
s = svg_open('SBCY: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('17'), (-700, -230), ['17 · cabeceira (backtrack pela A)', 'TORA 2300 m']),
    (thr('35'), (1150, -230), ['35 · D (cabeceira)', 'TORA 2300 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
callout(s, 240, -330, ['C: só aeronaves leves (código A)', 'giro de 180° só nas áreas de giro das cabeceiras'], PAL['hold'])
frame(s)
save('sbcy-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 105, e=120)
s = svg_open('SBCY: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 240, -310, ['TWR', 'pista 17/35, áreas de giro e TWY até o ponto de espera'], PAL['twr'])
callout(s, -480, 510, ['GND', 'pátios 1 e 2, E, F, G e ligações até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbcy-responsabilidade.svg', s)

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


def on_rwy(pts, off=-14):
    """Trecho na pista desenhado um pouco ao lado do eixo, para não cobrir o pouso."""
    return [(x, y + off) if abs(rwy_dist(RW, (x, y))[0]) < 5 else (x, y) for x, y in pts]


# --- pista 17: sem TWY até a cabeceira 17; decolagens entram pela A e fazem backtrack
dep17 = on_rwy(chain(AP1, TW('E', 'A'), A_R, TW(R), T17))
arr17 = [rwy_pt(RW, 350)] + chain(rwy_node(RW, 400), TW(R), D_R, TW('D', 'E'), AP2)
arr17c = [rwy_pt(RW, 900)] + chain(rwy_node(RW, 950), TW(R), C_R, TW('C', 'E'), AP2)
flow_map('sbcy-fluxo-17.svg', 'SBCY: fluxo de solo, pista 17',
         [dep17], [arr17], [arr17c],
         [((-500, -260), ['Decolagem 17: E até a A,', 'backtrack e giro na cabeceira'], 'dep', rwy_pt(RW, 400)),
          ((420, -300), ['Leves (código A): livram pela C'], 'alt', C_R),
          ((1150, -260), ['Pouso 17: livram pela D', 'e voltam pela E'], 'arr', D_R)])

# --- pista 35
dep35 = chain(AP1, TW('E', 'D'), D_R) + [thr('35')]
arr35 = [rwy_pt(RW, L - 350)] + chain(rwy_node(RW, L - 400), TW(R), B_R, TW('B', 'E'), AP2)
alt35 = [rwy_pt(RW, L - 400)] + chain(rwy_node(RW, L - 450), TW(R), A_R, TW('A', 'E'), AP1)
arr35c = [rwy_pt(RW, L - 600)] + chain(rwy_node(RW, L - 650), TW(R), C_R, TW('C', 'E'), AP2)
flow_map('sbcy-fluxo-35.svg', 'SBCY: fluxo de solo, pista 35',
         [dep35], [arr35], [alt35, arr35c],
         [((1150, 520), ['Decolagem 35: E até a D', '(cabeceira)'], 'dep', node_on('E', (1150, 196))),
          ((-250, -280), ['Pouso 35: livram pela B', 'ou, mais adiante, pela A'], 'arr', B_R),
          ((700, -300), ['Leves (código A): C'], 'alt', C_R)])
