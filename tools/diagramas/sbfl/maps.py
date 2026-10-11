# Mapas de SBFL (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
MAIN, AUX = '14/32', '03/21'

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'D': (1500, -280), 'C': (-420, 500), 'B': (215, -640)}
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
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 30, a[1] + (b[1] - a[1]) * k - 20))))
            break
        acc += d

LM = math.dist(*RWY[MAIN])
AP1 = node_on('Y2', (720, -200))
AP3 = node_on('A', (0, -770))
F14 = node_on('F', thr('14'))
D32 = node_on('D', thr('32'))
G_M = node_on('G', rwy_pt(MAIN, 760))
B_M = node_on('B', rwy_pt(MAIN, 335))
A21 = node_on('A', rwy_pt(AUX, 1265))
HS = {'HS1': ((-255, -610), (-420, -600)), 'HS2': ((-150, -497), (-80, -560)), 'HS3': ((-185, -345), (-330, -300)), 'HS4': ((-45, 40), (-190, 50))}


def hotspots(s):
    for t, ((x, y), (lx, ly)) in HS.items():
        s.append(f'<circle cx="{x}" cy="{y}" r="36" fill="#e5484d" opacity="0.35"/>')
        s.append(f'<text x="{lx}" y="{ly}" font-size="30" font-weight="700" fill="#c62a2f">{t}</text>')


# ======================================================== 1. visão geral
s = svg_open('SBFL: visão geral, pátios e pontos de decolagem')
base_layers(s)
hotspots(s)
pts = [
    (thr('14'), (300, -680), ['14 · F (cabeceira)', 'TORA 2400 m']),
    (thr('32'), (2100, -700), ['32 · D (cabeceira)', 'TORA 2400 m']),
    (end('21'), (-450, -900), ['21 · A', 'TORA 1320 m']),
    (thr('03'), (550, 600), ['03', 'TORA 1180 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="26" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbfl-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=50):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(MAIN, 90) + ' ' + strip(AUX, 50)
s = svg_open('SBFL: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="40" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="6" stroke-dasharray="26 16"/>')
twy_labels(s)
apron_labels(s)
callout(s, 1600, -760, ['TWR', 'as duas pistas e TWY', 'até o ponto de espera'], PAL['twr'])
callout(s, 1600, 200, ['GND', 'pátios e TWY', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbfl-responsabilidade.svg', s)

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


# --- pista 14
dep14 = chain(AP1, TW('Y2', 'G', 'D', 'F'), F14)
arr14 = [rwy_pt(MAIN, 500)] + chain(D32, TW('D', 'G', 'Y2'), AP1)
alt14 = chain(AP3, TW('A', 'B'), B_M)
flow_map('sbfl-fluxo-14.svg', 'SBFL: fluxo de solo, pista 14',
         [dep14], [arr14], [alt14],
         [((300, -680), ['Decolagem 14:', 'G, D e F'], 'dep', node_on('F', (-60, -400))),
          ((1800, 200), ['Pouso 14: rolam até o fim', 'e voltam pela D'], 'arr', node_on('D', (2000, -360))),
          ((900, -760), ['Pátios 3 e 4: B,', 'cruzando a pista'], 'alt', B_M)])

# --- pista 32
dep32 = chain(AP1, TW('Y2', 'G', 'D'), D32)
arr32 = [rwy_pt(MAIN, LM - 500)] + chain(G_M, TW('G', 'Y2'), AP1)
alt32 = chain(AP3, TW('A', 'B'), B_M)
flow_map('sbfl-fluxo-32.svg', 'SBFL: fluxo de solo, pista 32',
         [dep32], [arr32], [alt32],
         [((2050, 200), ['Decolagem 32:', 'G e D até a cabeceira'], 'dep', node_on('D', (2100, -360))),
          ((1000, -760), ['Pouso 32: livram pela G', 'até o pátio 1'], 'arr', G_M),
          ((300, -760), ['Pátios 3 e 4: B,', 'cruzando a pista'], 'alt', B_M)])
