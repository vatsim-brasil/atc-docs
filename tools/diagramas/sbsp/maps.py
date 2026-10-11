# Mapas de SBSP (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
MAIN, AUX = '17R/35L', '17L/35R'

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'M': (0, 108), 'N': (0, 200), 'S': (130, -290), 'L': (900, 140), 'C': (390, -90), 'H': (395, 95),
           'A': (-820, -60), 'E': (-860, 85), 'F': (-560, 95), 'B': (-500, -110), 'O': (-470, -230)}
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
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 30, a[1] + (b[1] - a[1]) * k - 18))))
            break
        acc += d

LM = math.dist(*RWY[MAIN])
LA = math.dist(*RWY[AUX])
AP3 = node_on('N', (100, 170))
AP2 = node_on('S', (300, -258))
E17 = node_on('E', end('17R'))
K35 = node_on('K', end('35L'))
H_M = node_on('H', rwy_pt(MAIN, 1160))
I_M = node_on('I', rwy_pt(MAIN, 1395))
F_M = node_on('F', rwy_pt(MAIN, 215))
O17 = node_on('O', rwy_pt(AUX, 155))
R35 = node_on('R', rwy_pt(AUX, 1440))
Q_A = node_on('Q', rwy_pt(AUX, 995))
HS = {'HS1': (-780, 60), 'HS2': (-600, 75), 'HS3': (370, 140)}


def hotspots(s):
    for t, (x, y) in HS.items():
        s.append(f'<circle cx="{x}" cy="{y}" r="38" fill="#e5484d" opacity="0.35"/>')
        s.append(f'<text x="{x + 40}" y="{y + 56}" font-size="28" font-weight="700" fill="#c62a2f">{t}</text>')


# ======================================================== 1. visão geral
s = svg_open('SBSP: visão geral, pátios e pontos de decolagem')
base_layers(s)
hotspots(s)
pts = [
    (thr('17R'), (-850, 560), ['17R · E', 'TORA 1760 m']),
    (thr('35L'), (1150, 560), ['35L · K', 'TORA 1760 m']),
    (thr('17L'), (-750, -560), ['17L · O', 'TORA 1345 m']),
    (thr('35R'), (1050, -560), ['35R · R', 'TORA 1345 m']),
]
for n, (cx, cy), ls in pts:
    leader(s, n, (cx, cy), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="24" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbsp-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=50):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(MAIN, 90) + ' ' + strip(AUX, 75)
s = svg_open('SBSP: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="40" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="6" stroke-dasharray="26 16"/>')
twy_labels(s)
apron_labels(s)
callout(s, 1000, -560, ['TWR', 'as duas pistas e TWY', 'até o ponto de espera'], PAL['twr'])
callout(s, -700, 560, ['GND', 'pátios e TWY', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbsp-responsabilidade.svg', s)

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


# --- pistas 17
dep17 = chain(AP3, TW('N', 'M', 'E'), E17)
arr17 = [rwy_pt(MAIN, 500)] + chain(I_M, TW('I', 'L', 'H', 'N'), AP3)
alt17 = chain(AP2, TW('S', 'O'), O17)
flow_map('sbsp-fluxo-17.svg', 'SBSP: fluxo de solo, pistas 17R e 17L',
         [dep17], [arr17], [alt17],
         [((-850, 560), ['Decolagem 17R:', 'N ou M e E'], 'dep', node_on('M', (-500, 130))),
          ((900, 560), ['Pouso 17R: livram pela I', 'e voltam pela L e H'], 'arr', I_M),
          ((-750, -560), ['Pista auxiliar 17L:', 'S e O (pátios 1 e 2)'], 'alt', O17)])

# --- pistas 35
dep35 = chain(AP3, TW('N', 'H', 'L', 'J', 'K'), K35)
arr35 = [rwy_pt(MAIN, LM - 400)] + chain(F_M, TW('F', 'M', 'N'), AP3)
alt35 = chain(AP2, TW('S', 'R'), R35)
flow_map('sbsp-fluxo-35.svg', 'SBSP: fluxo de solo, pistas 35L e 35R',
         [dep35], [arr35], [alt35],
         [((1150, 560), ['Decolagem 35L:', 'N, H, L e K'], 'dep', node_on('L', (900, 160))),
          ((-850, 560), ['Pouso 35L: livram pela F', '(ou H) e voltam pela M'], 'arr', F_M),
          ((1050, -560), ['Pista auxiliar 35R:', 'S e R (pátios 1 e 2)'], 'alt', R35)])
