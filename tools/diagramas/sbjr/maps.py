# Mapas de SBJR (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '03/21'
L = math.dist(*RWY[RW])

# rótulos das TWY, posicionados à mão a partir da ADC
LABELS += [('A', (330, -120)), ('B', (-400, -178)), ('C', (-95, -168)), ('D', (232, -168)), ('E', (535, -178))]

AP1 = node_on('A', (60, -135))      # pátio 1, em frente ao TPS
AP2 = node_on('A', (-280, -118))    # pátio 2 (helicópteros)
B03 = rwy_node(RW, 0)
E21 = rwy_node(RW, L)
C_R = node_on('C', (25, -229))      # C no eixo da pista (~490 m da cabeceira 21)
D_R = node_on('D', (105, -229))     # D no eixo da pista (~490 m da cabeceira 03)
HS1 = (-195, -95)

# ======================================================== 1. visão geral
s = svg_open('SBJR: visão geral, pátios e pontos de decolagem')
base_layers(s)
s.append(f'<circle cx="{HS1[0]}" cy="{HS1[1]}" r="34" fill="{PAL["hold"]}" fill-opacity="0.25" stroke="{PAL["hold"]}" stroke-width="4" stroke-dasharray="10 6"/>')
s.append(tag(HS1[0], HS1[1] - 48, 'HS1'))
pts = [
    (thr('03'), (-330, -410), ['03 · B (cabeceira)', 'TORA 900 m']),
    (thr('21'), (470, -410), ['21 · E (cabeceira)', 'TORA 900 m']),
]
for n, c, ls in pts:
    leader(s, n, (c[0], c[1] + 30), PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="16" fill="{PAL["tora"]}" stroke="#fff" stroke-width="4"/>')
    callout(s, cx, cy, ls, PAL['tora'])
callout(s, 140, 120, ['HS1: cruzamento intenso de', 'aeronaves e veículos'], PAL['hold'])
leader(s, (HS1[0] + 25, HS1[1] + 25), (60, 120), PAL['hold'])
frame(s)
save('sbjr-visao-geral.svg', s)


# ======================================================== 2. responsabilidade
def box(a, b, c, d):
    return pl([a, b, c, d]) + ' Z'


ya = thr('03')[1]
TWR = (box((-420, ya - 48), (560, ya - 48), (560, ya + 48), (-420, ya + 48)) + ' '
       + box((-420, ya + 48), (-340, ya + 48), (-340, ya + 82), (-420, ya + 82)) + ' '
       + box((470, ya + 48), (560, ya + 48), (560, ya + 90), (470, ya + 90)))
s = svg_open('SBJR: áreas de responsabilidade do Solo e da Torre')
s.append(f'<rect x="{X0:.0f}" y="{Y0:.0f}" width="{X1-X0:.0f}" height="{Y1-Y0:.0f}" rx="50" fill="{PAL["gnd"]}" opacity="0.12"/>')
s.append(f'<path d="{TWR}" fill="{PAL["twr"]}" opacity="0.28"/>')
base_layers(s, labels=False)
s.append(f'<path d="{TWR}" fill="none" stroke="{PAL["twr"]}" stroke-width="4" stroke-dasharray="16 10"/>')
twy_labels(s)
apron_labels(s)
callout(s, 70, -400, ['TWR', 'pista 03/21 e TWY até o ponto de espera'], PAL['twr'])
callout(s, 330, 60, ['GND', 'pátios 1 e 2, A e ligações', 'até o ponto de espera'], PAL['gnd'])
frame(s)
save('sbjr-responsabilidade.svg', s)

# ======================================================== 3/4. fluxos


def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 5, y - 5) for x, y in pts], 'alt', dashed=True, width=8)
    for pts in deps:
        flow(s, pts, 'dep', width=12)
    for pts in arrs:
        flow(s, pts, 'arr', width=9)
    twy_labels(s)
    apron_labels(s)
    for (x, y), ls, col, anchor in notes:
        if anchor:
            leader(s, anchor, (x, y), PAL[col])
        callout(s, x, y, ls, PAL[col])
    frame(s)
    save(fname, s)


# --- pista 03
dep03 = chain(AP1, TW('A', 'B'), B03)
arr03 = [rwy_pt(RW, 150)] + chain(D_R, TW('D', 'A'), node_on('A', (300, -140)), TW('A'), AP1)
alt03 = [rwy_pt(RW, 520), rwy_pt(RW, L - 20)] + chain(E21, TW('E', 'A'), AP1)
flow_map('sbjr-fluxo-03.svg', 'SBJR: fluxo de solo, pista 03',
         [dep03], [arr03], [alt03],
         [((-300, -400), ['Decolagem 03:', 'A e B até a cabeceira'], 'dep', node_on('B', (-375, -180))),
          ((200, -400), ['Pouso 03: livram pela D', '(~490 m) e voltam pela A'], 'arr', D_R),
          ((470, 50), ['Sem livrar na D: rolam até', 'o fim e livram pela E'], 'alt', node_on('E', (500, -180)))])

# --- pista 21
dep21 = chain(AP1, TW('A', 'E'), E21)
arr21 = [rwy_pt(RW, L - 150)] + chain(C_R, TW('C', 'A'), node_on('A', (-180, -125)), TW('A'), AP1)
alt21 = [rwy_pt(RW, 380), rwy_pt(RW, 20)] + chain(B03, TW('B', 'A'), AP1)
flow_map('sbjr-fluxo-21.svg', 'SBJR: fluxo de solo, pista 21',
         [dep21], [arr21], [alt21],
         [((440, -400), ['Decolagem 21:', 'A e E até a cabeceira'], 'dep', node_on('E', (500, -180))),
          ((-80, -400), ['Pouso 21: livram pela C', '(~490 m) e voltam pela A'], 'arr', C_R),
          ((-330, 50), ['Sem livrar na C: rolam até', 'o fim e livram pela B'], 'alt', node_on('B', (-375, -180)))])
