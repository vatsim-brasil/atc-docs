# Mapas de SBSL (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '06/24'
L = math.dist(*RWY[RW])

LABELS += [('A', (395, -5)), ('B', (-470, -470))]
_ap2 = [xy(g['lon'], g['lat']) for e in json.load(open(os.path.join(HERE, 'osm_apron.json')))['elements']
        if e['tags'].get('name') == 'Pátio 2' for g in e['geometry']]
APRON_POS.update({'1': (-20, -250), '2': (max(p[0] for p in _ap2) + 70, sum(p[1] for p in _ap2) / len(_ap2))})

AP1 = node_on('APN', (60, -205))          # meio do pátio 1
A_IN = node_on('A', (332, -32))           # A no fim da pista de rolamento do pátio 1
A_R = rwy_node(RW, rwy_dist(RW, (333, 68))[1])  # A na pista
T_A = rwy_dist(RW, A_R)[1]                # distância da cabeceira 06 até a A
T06 = rwy_node(RW, 0)
T24 = rwy_node(RW, L)
print(f'A a {T_A:.0f} m da THR 06 e {L - T_A:.0f} m da THR 24')


def on_rwy(pts, off):
    """Desloca para o lado um trecho sobre a pista (backtrack desenhado ao lado do eixo)."""
    return [(x, y + off) for x, y in pts]


# ======================================================== 1. visão geral
s = svg_open('SBSL: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (thr('06'), (-1050, 260), ['06 · cabeceira (backtrack)', 'TORA 2385 m']),
    (thr('24'), (760, 260), ['24 · cabeceira (backtrack)', 'TORA 2385 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="28" fill="{PAL["tora"]}" stroke="#fff" stroke-width="6"/>')
    callout(s, cx, cy, ls, PAL['tora'])
_o = (OLDRWY[0][0] * 0.8 + OLDRWY[1][0] * 0.2, OLDRWY[0][1] * 0.8 + OLDRWY[1][1] * 0.2)
leader(s, _o, (-1050, -560), PAL['muted'])
callout(s, -1050, -600, ['09/27 fechada (X)'], PAL['muted'])
frame(s)
save('sbsl-visao-geral.svg', s)


# ======================================================== 2/3. fluxos
def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, pts, 'alt', dashed=True, width=14)
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


taxi_out = chain(AP1, TW('APN', 'A'), A_R)
taxi_in = chain(A_R, TW('A', 'APN'), AP1)

# --- pista 06: entra pela A, backtrack até a cabeceira 06
dep06 = taxi_out + on_rwy([rwy_pt(RW, T_A), rwy_pt(RW, 40)], -14)
arr06 = on_rwy([rwy_pt(RW, 350), rwy_pt(RW, T_A)], 14) + taxi_in
flow_map('sbsl-fluxo-06.svg', 'SBSL: fluxo de solo, pista 06',
         [dep06], [arr06], [],
         [((-700, 230), ['Decolagem 06: A e', 'backtrack até a cabeceira'], 'dep', rwy_pt(RW, 700)),
          ((820, 230), ['Pouso 06: livram pela A', f'(~{T_A/100:.0f}00 m da cabeceira)'], 'arr', A_R)])

# --- pista 24: entra pela A, backtrack curto até a cabeceira 24
dep24 = taxi_out + on_rwy([rwy_pt(RW, T_A), rwy_pt(RW, L - 40)], -14)
arr24 = on_rwy([rwy_pt(RW, L - 300), rwy_pt(RW, T_A)], 14) + taxi_in
alt24 = on_rwy([rwy_pt(RW, T_A - 100), rwy_pt(RW, 60)], 16) + on_rwy([rwy_pt(RW, 60), rwy_pt(RW, T_A)], -16)
flow_map('sbsl-fluxo-24.svg', 'SBSL: fluxo de solo, pista 24',
         [dep24], [arr24], [alt24],
         [((830, 230), ['Decolagem 24: A e', 'backtrack até a cabeceira'], 'dep', rwy_pt(RW, L - 300)),
          ((-200, 230), ['Pouso 24: leves livram pela A', f'(~{(L-T_A)/100:.0f}00 m da cabeceira)'], 'arr', A_R),
          ((-1000, 230), ['Jatos: giro na cabeceira 06', 'e backtrack até a A'], 'alt', rwy_pt(RW, 200))])
