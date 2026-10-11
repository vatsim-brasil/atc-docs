# Mapas de SBPA (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '11/29'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {}
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

AP1 = node_on('M3', (-300, -316))
A11 = node_on('A', thr('11'))
C_R = node_on('C', rwy_pt(RW, 573))
F_R = node_on('F', rwy_pt(RW, 1502))
E_R = node_on('E', rwy_pt(RW, 1994))
HS = {'HS1': (-1100, -90)}


def hotspots(s):
    for t, (x, y) in HS.items():
        s.append(f'<circle cx="{x}" cy="{y}" r="60" fill="#e5484d" opacity="0.35"/>')
        s.append(f'<text x="{x + 66}" y="{y - 40}" font-size="40" font-weight="700" fill="#c62a2f">{t}</text>')


# ======================================================== 1. visão geral
s = svg_open('SBPA: visão geral, pátios e pontos de decolagem')
base_layers(s)
hotspots(s)
pts = [
    (thr('11'), (-1250, -860), ['11 · A ou J', 'TORA 3200 m']),
    (C_R, (-800, 450), ['11 · C (HIRO)', 'TORA 2627 m']),
    (F_R, (350, 450), ['29 · F', 'TORA 1507 m']),
    (E_R, (1150, 450), ['29 · E', 'TORA 1994 m']),
    (rwy_pt(RW, 2400), (1650, -400), ['29 · 1ª área de giro', 'TORA 2280 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbpa-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 105)
s = svg_open('SBPA: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 1200, 360, ['TWR', 'pista 11/29 e TWY até o ponto de espera'], PAL['twr'])
callout(s, 1250, -500, ['GND', 'pátios e TWY', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbpa-responsabilidade.svg', s)

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


# --- pista 11
dep11 = chain(AP1, TW('M3', 'B', 'J'), node_on('J', thr('11')))
alt11 = chain(AP1, TW('M3', 'C'), C_R)
arr11 = [rwy_pt(RW, 500)] + chain(F_R, TW('F', 'D', 'M4', 'M3'), AP1)
arr11e = [rwy_pt(RW, 1600)] + chain(E_R, TW('E', 'D'), node_on('D', (300, -222)))
flow_map('sbpa-fluxo-11.svg', 'SBPA: fluxo de solo, pista 11',
         [dep11], [arr11], [alt11, arr11e],
         [((-1250, -860), ['Decolagem 11: M3, B', 'e J (ou A)'], 'dep', node_on('B', (-750, -200))),
          ((-800, 450), ['C: só em HIRO,', 'coordenado com o Solo'], 'alt', C_R),
          ((450, 450), ['Pouso 11: livram pela', 'F (1502 m) ou E (1994 m)'], 'arr', F_R)])

# --- pista 29
dep29 = chain(AP1, TW('M3', 'M4', 'D', 'E'), E_R)
alt29 = chain(AP1, TW('M3', 'M4', 'D', 'F'), F_R)
arr29 = [rwy_pt(RW, L - 600)] + chain(C_R, TW('C', 'M3'), AP1)
flow_map('sbpa-fluxo-29.svg', 'SBPA: fluxo de solo, pista 29',
         [dep29], [arr29], [alt29],
         [((1150, 450), ['Decolagem 29: D até', 'a E (TORA 1994 m)'], 'dep', E_R),
          ((350, 450), ['Se combinado:', 'pela F (TORA 1507 m)'], 'alt', F_R),
          ((-800, 450), ['Pouso 29: livram', 'pela C (2627 m)'], 'arr', C_R)])
