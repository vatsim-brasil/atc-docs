# Mapas de SBMO (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '12/30'
L = math.dist(*RWY[RW])
T12 = rwy_dist(RW, thr('12'))[1]
T30 = rwy_dist(RW, thr('30'))[1]

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'A': (-1200, 90), 'B': (-520, 110), 'C': (250, 110), 'D': (1290, 140), 'E': (750, 220),
           'F': (250, 260), 'G': (-330, 250), 'K': (920, -100)}
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

AP1 = node_on('G', (-250, 240))      # entrada oeste do pátio 1
AP1E = node_on('F', (200, 238))      # entrada leste do pátio 1
AP2 = node_on('E', (-1030, 175))     # frente do pátio 2
A12 = node_on('A', thr('12'))
D30 = node_on('D', end('30'))
C_R = rwy_node(RW, 87 - end('12')[0])   # saída rápida C (pouso 12)
B_R = rwy_node(RW, -271 - end('12')[0])  # saída rápida B (pouso 30)


# ======================================================== 1. visão geral
s = svg_open('SBMO: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('12'), (-1100, -330), ['12 · A (cabeceira)', 'TORA 2490 m']),
    (end('30'), (1100, -330), ['30 · D (início da pista)', 'TORA 2602 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbmo-visao-geral.svg', s)


# ======================================================== 2/3. fluxos
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
dep12 = chain(AP1, TW('G', 'E', 'A'), A12)
dep12b = chain(AP2, TW('E', 'A'), A12)
arr12 = [rwy_pt(RW, T12 + 500)] + chain(C_R, TW('C', 'E', 'F'), AP1E)
alt12 = [rwy_pt(RW, T12 + 1500), rwy_pt(RW, L - 120)] + chain(D30, TW('D', 'E', 'F'), AP1E)
flow_map('sbmo-fluxo-12.svg', 'SBMO: fluxo de solo, pista 12',
         [dep12, dep12b], [arr12], [alt12],
         [((-800, -330), ['Decolagem 12:', 'E até a A (cabeceira)'], 'dep', node_on('E', (-900, 175))),
          ((100, -330), ['Pouso 12: livram pela C', '(saída rápida, ~1400 m)'], 'arr', C_R),
          ((1050, -330), ['Se passar da C:', 'D no fim e volta pela E'], 'alt', D30)])

# --- pista 30
dep30 = chain(AP1E, TW('F', 'E', 'D'), D30)
dep30b = chain(AP2, TW('E', 'D'), D30)
arr30 = [rwy_pt(RW, T30 - 500)] + chain(B_R, TW('B', 'E'), AP2)
arr30b = chain(node_at('B', 'E', (-790, 175)), TW('E', 'G'), AP1)
alt30 = [rwy_pt(RW, T30 - 1500), rwy_pt(RW, 100)] + chain(A12, TW('A', 'E'), AP2)
flow_map('sbmo-fluxo-30.svg', 'SBMO: fluxo de solo, pista 30',
         [dep30, dep30b], [arr30, arr30b], [alt30],
         [((1000, -330), ['Decolagem 30: E até a D', '(início da pista)'], 'dep', node_on('E', (900, 174))),
          ((-450, -330), ['Pouso 30: livram pela B', '(saída rápida, ~1460 m)'], 'arr', B_R),
          ((-1150, -330), ['Se passar da B:', 'A no fim'], 'alt', A12)])
