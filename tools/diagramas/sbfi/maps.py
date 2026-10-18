# Mapas de SBFI (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '15/33'
L = math.dist(*RWY[RW])
T15 = rwy_dist(RW, thr('15'))[1]
T33 = rwy_dist(RW, thr('33'))[1]

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'D': (-900, -140), 'A': (-735, -140), 'B': (-452, -140), 'C': (-108, -150), 'E': (-560, -150),
           'F': (418, -120)}
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


def on_rwy(t0, t1, off=0):
    """Trecho sobre a pista (backtrack), da distância t0 à t1 a partir da cabeceira 15, deslocado do eixo."""
    a, b = rwy_pt(RW, t0), rwy_pt(RW, t1)
    return [(a[0], a[1] + off), (b[0], b[1] + off)]


AP1 = node_on('E', (-760, -75))      # frente do pátio 1
AP2 = node_on('E', (-260, -80))      # frente do pátio 2
AP3 = node_on(None, (365, 10))       # pátio 3 (via de táxi do pátio, sem designador)
EXIT = {r: rwy_node(RW, rwy_dist(RW, node_on(r, (x, -200)))[1]) for r, x in
        (('D', -850), ('A', -684), ('B', -401), ('C', -157), ('F', 368))}
DIST15 = {r: rwy_dist(RW, n)[1] - T15 for r, n in EXIT.items()}
for r in EXIT:
    print(f'{r}: {DIST15[r]:.0f} m da THR 15, {T33 - rwy_dist(RW, EXIT[r])[1]:.0f} m da THR 33')


def tq(r):
    return rwy_dist(RW, EXIT[r])[1]


# ======================================================== 1. visão geral
s = svg_open('SBFI: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('15'), (-1850, -470), ['15 · cabeceira (backtrack)', 'TORA 2705 m']),
    (thr('33'), (180, -470), ['33 · cabeceira (backtrack)', 'TORA 2705 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
# áreas de giro (AIP 2.20 item 6)
for t, lbl in ((T15 + 668, 'giro'), (T15 + 2240, 'giro')):
    p = rwy_pt(RW, t)
    s.append(f'<text x="{p[0]:.0f}" y="{p[1] + (-70 if t < T15 + 1000 else 95):.0f}" font-size="34" font-style="italic" '
             f'fill="{PAL["muted"]}" text-anchor="middle">{lbl}</text>')
frame(s)
save('sbfi-visao-geral.svg', s)


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


# --- pista 15: entra pela D e regressa até a cabeceira 15
dep15 = chain(AP2, TW('E', 'D'), EXIT['D']) + on_rwy(tq('D'), T15 + 30, off=-12)
dep15b = chain(AP1, TW('E', 'D'), EXIT['D'])
arr15 = on_rwy(T15 + 1500, tq('C')) + chain(EXIT['C'], TW('C', 'E'), AP2)
alt15 = on_rwy(tq('C'), tq('F')) + chain(EXIT['F'], TW('F'), AP3)
flow_map('sbfi-fluxo-15.svg', 'SBFI: fluxo de solo, pista 15',
         [dep15, dep15b], [arr15], [alt15],
         [((-1850, -470), ['Decolagem 15: E até a D,', 'backtrack até a cabeceira 15'], 'dep', rwy_pt(RW, T15 + 500)),
          ((-420, -470), ['Pouso 15: livram pela C', f'(~{DIST15["C"]:.0f} m) ou pela B'], 'arr', EXIT['C']),
          ((440, -470), ['Pátio 3: livram pela F', f'(~{DIST15["F"]:.0f} m)'], 'alt', EXIT['F'])])

# --- pista 33: entra pela C e regressa até a cabeceira 33
dep33 = chain(AP1, TW('E', 'C'), EXIT['C']) + on_rwy(tq('C'), T33 - 30, off=-12)
dep33b = chain(AP3, TW('F'), EXIT['F'])
arr33 = on_rwy(T33 - 500, tq('A')) + chain(EXIT['A'], TW('A', 'E'), AP1)
alt33 = on_rwy(tq('A'), T15 + 668) + on_rwy(T15 + 668, tq('D'), off=-40) + chain(EXIT['D'], TW('D', 'E'), AP1)
flow_map('sbfi-fluxo-33.svg', 'SBFI: fluxo de solo, pista 33',
         [dep33, dep33b], [arr33], [alt33],
         [((250, -470), ['Decolagem 33: E até a C,', 'backtrack até a cabeceira 33'], 'dep', rwy_pt(RW, T33 - 300)),
          ((-700, -470), ['Pouso 33: livram pela A', f'(~{T33 - tq("A"):.0f} m) ou pela B'], 'arr', EXIT['A']),
          ((-1750, -470), ['Se passar da D: giro', 'na área de giro e volta'], 'alt', rwy_pt(RW, T15 + 668))])
