# Mapas de SBNF (executado por gen.py, que define a geometria e as funções de desenho)
TW = lambda *r: set(r)
RW = '08/26'
L = math.dist(*RWY[RW])

# rótulos: ponto médio do trecho mais longo de cada TWY, com ajustes à mão em LBL_FIX
LBL_FIX = {'A': (92, 128), 'B': (200, 128), 'APN': (-70, 158)}
_best = {}
for ref, pts in TWY:
    if ref in (None, 'GIRO08', 'GIRO26'):
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
            LABELS.append((ref, LBL_FIX.get(ref, (a[0] + (b[0] - a[0]) * k + 30, a[1] + (b[1] - a[1]) * k - 16))))
            break
        acc += d

AP1 = node_on('APN', (110, 176))      # pátio 1 (terminal)
AW = node_on('A', (-69, 68))          # A, ramo oeste (lado da 08)
AE = node_on('A', (71, 67))           # A, ramo leste
BW = node_on('B', (148, 67))          # B, ramo oeste
BE = node_on('B', (203, 67))          # B, ramo leste
P08a, P08b = node_on('GIRO08', (-684, 67)), node_on('GIRO08', (-868, 89))
P26a, P26b = node_on('GIRO26', (722, 65)), node_on('GIRO26', (907, 45))
T08, T26 = thr('08'), thr('26')


def d08(n):
    return round(rwy_dist(RW, n)[1])


EX = {'AW': d08(AW), 'AE': d08(AE), 'BW': d08(BW), 'BE': d08(BE)}
print('saídas (m da THR 08):', EX, 'pista', round(L))

# ======================================================== 1. visão geral
s = svg_open('SBNF: visão geral, pátios e pontos de decolagem')
base_layers(s)
pts = [
    (T08, (-640, -200), ['08 · cabeceira, após backtrack', 'TORA 1800 m']),
    (T26, (640, -200), ['26 · cabeceira, após backtrack', 'TORA 1800 m']),
]
for n, c, ls in pts:
    leader(s, n, c, PAL['tora'])
for n, (cx, cy), ls in pts:
    s.append(f'<circle cx="{n[0]:.0f}" cy="{n[1]:.0f}" r="18" fill="{PAL["tora"]}" stroke="#fff" stroke-width="4"/>')
    callout(s, cx, cy, ls, PAL['tora'])
callout(s, -420, 250, ['Sem paralela: A e B são', 'as únicas ligações com a pista'], PAL['muted'])
frame(s)
save('sbnf-visao-geral.svg', s)


# ======================================================== 2/3. fluxos
def flow_map(fname, title, deps, arrs, alts=(), notes=()):
    s = svg_open(title)
    base_layers(s, labels=False)
    for pts in alts:
        flow(s, [(x + 6, y - 6) for x, y in pts], 'alt', dashed=True, width=9)
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


def off(pts, dy):
    """Desloca uma rota sobre a pista para o lado, para não cobrir a outra."""
    return [(x, y + dy) for x, y in pts]


# --- pista 08: decolagem pela A e backtrack até a área de giro da 08
dep08 = chain(AP1, TW('APN', 'A'), AW) + off(chain(AW, TW('RWY' + RW), P08a), -14)[1:] \
    + chain(P08a, TW('GIRO08'), P08b)[1:] + [T08, rwy_pt(RW, 120)]
arr08 = [rwy_pt(RW, 450)] + chain(rwy_node(RW, 450), TW('RWY' + RW), BW, TW('B', 'APN'), AP1)[1:]
alt08 =[rwy_pt(RW, EX['BE'] + 40)] + off(chain(rwy_node(RW, EX['BE'] + 40), TW('RWY' + RW), P26a), 14)[1:] \
    + chain(P26a, TW('GIRO26'), P26b)[1:] + [T26] + off(chain(rwy_node(RW, L - 40), TW('RWY' + RW), BE), -14)[1:]
flow_map('sbnf-fluxo-08.svg', 'SBNF: fluxo de solo, pista 08',
         [dep08], [arr08], [alt08],
         [((-560, -190), ['Decolagem 08: A e backtrack', 'pela pista até a cabeceira'], 'dep', rwy_pt(RW, 300)),
          ((480, 250), ['Pouso 08: livram pela B', f'(~{EX["BW"]} m da cabeceira)'], 'arr', BW),
          ((620, -190), ['Sem livrar na B: giro no fim', 'da pista e backtrack até a B'], 'alt', rwy_pt(RW, L - 150))])

# --- pista 26: decolagem pela B e backtrack até a área de giro da 26
dep26 = chain(AP1, TW('APN', 'B'), BE) + off(chain(BE, TW('RWY' + RW), P26a), -14)[1:] \
    + chain(P26a, TW('GIRO26'), P26b)[1:] + [T26, rwy_pt(RW, L - 120)]
arr26 = [rwy_pt(RW, L - 450)] + chain(rwy_node(RW, L - 450), TW('RWY' + RW), AE, TW('A', 'APN'), AP1)[1:]
alt26 = [rwy_pt(RW, EX['AW'] - 40)] + off(chain(rwy_node(RW, EX['AW'] - 40), TW('RWY' + RW), P08a), 14)[1:] \
    + chain(P08a, TW('GIRO08'), P08b)[1:] + [T08] + off(chain(rwy_node(RW, 40), TW('RWY' + RW), AW), -14)[1:]
flow_map('sbnf-fluxo-26.svg', 'SBNF: fluxo de solo, pista 26',
         [dep26], [arr26], [alt26],
         [((560, -190), ['Decolagem 26: B e backtrack', 'pela pista até a cabeceira'], 'dep', rwy_pt(RW, L - 300)),
          ((560, 250), ['Pouso 26: livram pela A', f'(~{round(L) - EX["AE"]} m da cabeceira)'], 'arr', AE),
          ((-620, -190), ['Sem livrar na A: giro no fim', 'da pista e backtrack até a A'], 'alt', rwy_pt(RW, 150))])
