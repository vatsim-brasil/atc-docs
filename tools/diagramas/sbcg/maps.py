# Mapas de SBCG (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '06/24'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'A': (1150, -680), 'B': (950, -110)}
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

AP1 = node_on('A', (900, -760))
AP2 = node_on('F', (683, -770))
D06 = node_on('D', thr('06'))
A24 = node_on('A', (847, -246))
E_R = node_on('E', rwy_pt(RW, 1300))

# ======================================================== 1. visão geral
s = svg_open('SBCG: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('06'), (-1300, 120), ['06 · D (cabeceira)', 'TORA 2600 m']),
    (thr('24'), (300, 120), ['24 · A (cabeceira)', 'TORA 2600 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbcg-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 105)
s = svg_open('SBCG: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, -300, 120, ['TWR', 'pista 06/24 e TWY até o ponto de espera'], PAL['twr'])
callout(s, -700, -900, ['GND', 'pátios, C e ligações', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbcg-responsabilidade.svg', s)

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


# --- pista 06
dep06 = chain(AP2, TW('F', 'C', 'D'), D06)
arr06 = [rwy_pt(RW, 500)] + chain(A24, TW('A'), AP1)
alt06 = [rwy_pt(RW, 400), rwy_pt(RW, 1300)] + chain(E_R, TW('E', 'C', 'F'), AP2)
flow_map('sbcg-fluxo-06.svg', 'SBCG: fluxo de solo, pista 06',
         [dep06], [arr06], [alt06],
         [((-1300, -900), ['Decolagem 06:', 'C até a D (cabeceira)'], 'dep', node_on('C', (-1200, -446))),
          ((300, 60), ['Pouso 06: rolam até o fim', 'e livram pela A'], 'arr', A24),
          ((-500, 120), ['Leves: livram', 'pela E (~1300 m)'], 'alt', E_R)])

# --- pista 24
dep24 = chain(AP1, TW('A'), A24)
arr24 = [rwy_pt(RW, L - 500)] + chain(D06, TW('D', 'C', 'F'), AP2)
alt24 = [rwy_pt(RW, L - 400), rwy_pt(RW, 1300)] + chain(E_R, TW('E', 'C', 'F'), AP2)
flow_map('sbcg-fluxo-24.svg', 'SBCG: fluxo de solo, pista 24',
         [dep24], [arr24], [alt24],
         [((300, 60), ['Decolagem 24:', 'A até a cabeceira'], 'dep', A24),
          ((-1000, 120), ['Pouso 24: rolam até o fim,', 'livram pela D e voltam pela C'], 'arr', D06),
          ((-500, -900), ['Leves: livram', 'pela E (~1300 m)'], 'alt', E_R)])
