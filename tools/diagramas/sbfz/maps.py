# Mapas de SBFZ (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '13/31'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'A': (0, 205), 'J': (-850, -140), 'K': (-1290, 320), 'P': (-1395, 170), 'B': (-1240, 150),
           'L': (-560, 290), 'ZA': (-590, 345), 'ZB': (-960, 330)}
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

AP1 = node_on('J', (-300, -108))    # pátio 1 (aviação geral)
AP2 = node_on('L', (-659, 344))     # pátio 2 (terminal)
AP4 = node_on('G', (730, -107))     # acesso ao pátio 4 (militar)
P13 = node_on('P', (-1386, 63))
B13 = node_on('B', (-1237, 62))
C13 = node_on('C', (-322, 62))
H31 = node_on('H', (1189, 62))
Q31 = node_on('Q', (1261, 62))
D_X = node_on('D', (681, 62))
G_X = node_on('G', (681, 62))
C_X = node_on('C', (-428, 62))
E_X = node_on('E', (-428, 62))

# ======================================================== 1. visão geral
s = svg_open('SBFZ: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('13'), (-1390, -440), ['13 · P (cabeceira)', 'TORA 2755 m']),
    (B13, (-800, -440), ['13 · B ou J', 'TORA 2613 m']),
    (C13, (-150, -440), ['13 · C ou E (cód. A/B)', 'TORA 1668 m']),
    (H31, (900, 560), ['31 · H', 'TORA 2665 m']),
    (thr('31'), (1250, -440), ['31 · Q (cabeceira)', 'TORA 2755 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="30" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
frame(s)
save('sbfz-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def strip(name, half, e=60):
    a, b = RWY[name]
    (ux, uy), L = unit(a, b)
    nx, ny = -uy, ux
    p = [(a[0] - ux * e + nx * half, a[1] - uy * e + ny * half), (b[0] + ux * e + nx * half, b[1] + uy * e + ny * half),
         (b[0] + ux * e - nx * half, b[1] + uy * e - ny * half), (a[0] - ux * e - nx * half, a[1] - uy * e - ny * half)]
    return pl(p) + ' Z'


STRIPS = strip(RW, 90)
s = svg_open('SBFZ: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{STRIPS}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{STRIPS}" fill="none" stroke="{PAL["twr"]}" stroke-width="7" stroke-dasharray="30 18"/>')
twy_labels(s)
apron_labels(s)
callout(s, 300, 560, ['TWR', 'pista 13/31 e TWY até o ponto de espera'], PAL['twr'])
callout(s, 300, -470, ['GND', 'pátios, A, J e ligações até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbfz-responsabilidade.svg', s)

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


# --- pista 13
dep13 = chain(AP2, TW('L', 'A', 'P'), P13)
alt13 = chain(AP2, TW('L', 'A', 'B'), B13)
arr13 = [rwy_pt(RW, 1500)] + chain(D_X, TW('D', 'A', 'L'), AP2)
flow_map('sbfz-fluxo-13.svg', 'SBFZ: fluxo de solo, pista 13',
         [dep13], [arr13], [alt13],
         [((-1390, -440), ['Decolagem 13:', 'A até a P (cabeceira)'], 'dep', node_on('P', (-1350, 150))),
          ((-800, -440), ['Com HIRO: pela B', '(TORA 2613 m)'], 'alt', B13),
          ((500, 560), ['Pouso 13: livram pela D', '(2242 m) e seguem pela A'], 'arr', node_on('D', (709, 129)))])

# --- pista 31
dep31 = chain(AP2, TW('L', 'A', 'D'), D_X) + chain(G_X, TW('G', 'J', 'Q'), Q31)[1:]
alt31 = chain(AP2, TW('L', 'A', 'D'), D_X) + chain(G_X, TW('G', 'J', 'H'), H31)[1:]
arr31 = [rwy_pt(RW, L - 900)] + chain(node_on('C', (-322, 62)), TW('C', 'A', 'L'), AP2)
flow_map('sbfz-fluxo-31.svg', 'SBFZ: fluxo de solo, pista 31',
         [dep31], [arr31], [alt31],
         [((1240, -470), ['Decolagem 31: A, D, cruza', 'a pista, G e J até a Q'], 'dep', node_on('J', (1050, -100))),
          ((850, 560), ['Interseção H', '(TORA 2665 m)'], 'alt', H31),
          ((-500, 560), ['Pouso 31: livram pela C', '(1668 m) e seguem pela A'], 'arr', node_on('C', (-303, 172)))])
