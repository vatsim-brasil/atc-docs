"""Gera o SVG dos setores do APP de uma TMA a partir do mapa da própria página.

Lê os arrays `setores` e `volumes` do script Leaflet da página (que vêm do
pacote de setores) e desenha dois painéis lado a lado: camada baixa
(até FL135, com as finais por cima) e camada alta (FL135 a FL245).

Uso: python3 -I gen.py [pagina.md] [saida.svg]
     python3 -I gen.py <pagina.md> <saida.svg> --setor T1   (um mapa por setor)
     python3 -I gen.py <pagina.md> <saida.svg> --combinado SBXP_S_APP   (posição combinada)

Os ajustes de cada TMA (aeródromos, cores, setores baixos) estão em TMAS.
"""
import json
import math
import re
import sys

ARGS = [a for a in sys.argv[1:] if not a.startswith("--")]
SETOR = sys.argv[sys.argv.index("--setor") + 1] if "--setor" in sys.argv else None
if SETOR:
    ARGS.remove(SETOR)
COMBINADO = sys.argv[sys.argv.index("--combinado") + 1] if "--combinado" in sys.argv else None
if COMBINADO:
    ARGS.remove(COMBINADO)
PAGE = ARGS[0] if len(ARGS) > 0 else "docs/MOP/terminais/sbcw-curitiba/SBXP.pt.md"
OUT = ARGS[1] if len(ARGS) > 1 else "docs/MOP/terminais/sbcw-curitiba/img/sbxp-setores.svg"

# Por TMA (campo "id" dos volumes da página): aeródromos de referência (ARP, graus
# decimais), nome, cores das posições combinadas, setores baixos que ficam dentro dos
# outros (as "finais", desenhadas por cima e hachuradas) e a cobertura deles, que
# entra na área de uma posição combinada.
TMAS = {
    "SBXP": {
        "nome": "TMA São Paulo",
        "aerodromos": {"SBGR": (-46.4731, -23.4356), "SBSP": (-46.6564, -23.6261),
                       "SBKP": (-47.1345, -23.0074), "SBSJ": (-45.8615, -23.2292)},
        "cores": {"S": "#60a5fa", "E": "#34d399", "N": "#f472b6", "NL": "#fb923c", "NU": "#a78bfa", "APP": "#38bdf8"},
        "final": lambda s: s["rot"].startswith("F"),
        "cobertura": {},
    },
    "SBWJ": {
        "nome": "TMA Rio de Janeiro",
        "aerodromos": {"SBGL": (-43.2506, -22.8100), "SBRJ": (-43.1628, -22.9104),
                       "SBJR": (-43.3722, -22.9868), "SBSC": (-43.7191, -22.9324)},
        "cores": {"NE": "#f472b6", "APP": "#38bdf8"},
        "final": lambda s: s["rot"] in ("RJ", "GL"),
        "cobertura": {"SBWJ_N_APP": ["SBWJ_GL_APP"], "SBWJ_S_APP": ["SBWJ_RJ_APP"]},
    },
    # Setores da AIP (o pacote só tem SBWH_APP): rótulo no campo "rot" de cada setor
    "SBWH": {
        "nome": "TMA Belo Horizonte",
        "aerodromos": {"SBCF": (-43.9719, -19.6244), "SBBH": (-43.9506, -19.8512), "SBLS": (-43.8964, -19.6616)},
        "cores": {"APP": "#38bdf8"},
        "final": lambda s: s["rot"] in ("05", "06", "07", "08"),
        "cobertura": {},
    },
    # Setores da AIP (o pacote só tem SBWR_APP); 05 a 08 são o miolo, do GND a 6500 FT
    "SBWR": {
        "nome": "TMA Brasília",
        "aerodromos": {"SBBR": (-47.9206, -15.8711)},
        "cores": {"APP": "#38bdf8"},
        "final": lambda s: False,
        "cobertura": {},
    },
    # Setores da AIP (o pacote só tem SBWP_APP); 05/06 é a faixa de Canoas e 07/08 são os setores VFR dentro do 03
    "SBWP": {
        "nome": "TMA Porto Alegre",
        "aerodromos": {"SBPA": (-51.1714, -29.9939), "SBCO": (-51.1442, -29.9459), "SBCX": (-51.1875, -29.1971)},
        "cores": {"APP": "#38bdf8"},
        "final": lambda s: s["rot"] in ("05", "06", "07", "08"),
        "cobertura": {},
    },
}
AERODROMOS = {}
INK, MUTED, BG = "#1e293b", "#64748b", "#f8fafc"
FONT = 'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif"'


def ler_combinadas(path):
    """Tabela "Posições combinadas" da página: posição -> posições que assume."""
    texto = open(path, encoding="utf-8").read()
    if "### Posições combinadas" not in texto:
        return {}
    bloco = texto.split("### Posições combinadas", 1)[1].split("\n## ", 1)[0]
    res = {}
    for linha in bloco.splitlines():
        cols = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(cols) == 3 and cols[0].startswith("`"):
            res[cols[0].strip("`")] = re.findall(r"`([A-Z0-9_]+)`", cols[2])
    return res


def expandir(posicao, combinadas, cobertura={}):
    """Posições elementares que uma posição combinada assume (com as que ela cobre)."""
    if posicao not in combinadas:
        return [posicao] + cobertura.get(posicao, [])
    return [e for p in combinadas[posicao] for e in expandir(p, combinadas, cobertura)]


def ler_pagina(path):
    texto = open(path, encoding="utf-8").read()
    setores = json.loads(re.search(r"const setores = (\[.*?\]);\n", texto, re.S).group(1))
    volumes = json.loads(re.search(r"const volumes = (\[.*?\]);\n", texto, re.S).group(1))
    paleta = json.loads(re.search(r"const paletaSetores = (\[.*?\]);", texto).group(1).replace("'", '"'))
    tmas = [v for v in volumes if v["tipo"] == "tma"]
    tma = next((v for v in tmas if v["nome"].endswith("1")), tmas[0])
    return setores, tma["contorno"], paleta, TMAS[tma["id"]]


def rotulo(posicao):
    """SBXP_T1_APP -> T1; SBGR_F_APP -> FGR."""
    icao, meio = posicao.split("_")[0], posicao.split("_")[1]
    return "F" + icao[2:] if meio == "F" else meio


def limites(lim):
    def ft(t):
        t = t.strip()
        if t == "GND":
            return 0
        return int(t[2:]) * 100 if t.startswith("FL") else int(t.split()[0])
    a, b = lim.split("–")
    return ft(a), ft(b)


def dentro(p, poli):
    x, y = p
    res = False
    for (x1, y1), (x2, y2) in zip(poli, poli[1:] + poli[:1]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            res = not res
    return res


def dist_seg(p, a, b):
    (px, py), (ax, ay), (bx, by) = p, a, b
    dx, dy = bx - ax, by - ay
    t = 0 if dx == dy == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)


def dist_borda(p, poli):
    return min(dist_seg(p, a, b) for a, b in zip(poli, poli[1:] + poli[:1]))


def ponto_rotulo(poli, evitar=()):
    """Ponto interno mais longe das bordas (e fora dos polígonos a evitar)."""
    xs, ys = [p[0] for p in poli], [p[1] for p in poli]
    melhor, md = None, -1
    passo = max(max(xs) - min(xs), max(ys) - min(ys)) / 60
    y = min(ys)
    while y <= max(ys):
        x = min(xs)
        while x <= max(xs):
            p = (x, y)
            if dentro(p, poli) and not any(dentro(p, e) for e in evitar):
                d = min([dist_borda(p, poli)] + [dist_borda(p, e) for e in evitar])
                if d > md:
                    melhor, md = p, d
            x += passo
        y += passo
    if melhor is None:  # tudo coberto: cai no centro geométrico
        melhor = (sum(xs) / len(xs), sum(ys) / len(ys))
    return melhor


def pontos_comuns(a, b, n=90):
    """Amostra de pontos dentro dos dois polígonos (aproxima a interseção)."""
    xs, ys = [p[0] for p in a], [p[1] for p in a]
    passo = max(max(xs) - min(xs), max(ys) - min(ys)) / n
    res, total = [], 0
    y = min(ys)
    while y <= max(ys):
        x = min(xs)
        while x <= max(xs):
            if dentro((x, y), a):
                total += 1
                if dentro((x, y), b):
                    res.append((x, y))
            x += passo
        y += passo
    return res, total


def nivel(ft):
    if ft == 0:
        return "GND"
    return f"FL{ft // 100:03d}" if ft >= 10000 else f"{ft} FT"


def mapa_setor(alvo, setores, tma, proj, caminho, W):
    """Um setor preenchido; o resto da TMA em cinza, só com as divisas."""
    out = ['<defs><pattern id="hach" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           f'<rect width="8" height="8" fill="#fff" fill-opacity="0.55"/><path d="M0,0 V8" stroke="{INK}" stroke-width="2"/></pattern>'
           f'<clipPath id="clip-alvo"><path d="{caminho(alvo["contorno"], 0)}"/></clipPath></defs>']
    out.append(f'<path d="{caminho(tma, 0)}" fill="#e2e8f0"/>')
    for s in setores:
        if s is not alvo and not s["final"]:
            out.append(f'<path d="{caminho(s["contorno"], 0)}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>')
    out.append(f'<path d="{caminho(alvo["contorno"], 0)}" fill="{alvo["cor"]}" fill-opacity="0.85" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>')
    # finais que tomam parte do setor abaixo de FL100: hachuradas, recortadas no setor
    tomadas = []
    for f in setores:
        if f is not alvo and not alvo["final"] and f["final"] and f["max"] > alvo["min"]:
            poli = [proj(p, 0) for p in f["contorno"]]
            alvo_poli = [proj(p, 0) for p in alvo["contorno"]]
            comuns, total = pontos_comuns(alvo_poli, poli)
            if total and len(comuns) / total > 0.01:  # só sobreposição real, não divisa
                out.append(f'<path d="{caminho(f["contorno"], 0)}" fill="url(#hach)" stroke="{INK}" stroke-width="1.4" '
                           'stroke-dasharray="5 3" clip-path="url(#clip-alvo)"/>')
                tomadas.append((f, poli, comuns))
    out.append(f'<path d="{caminho(tma, 0)}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
    for icao, p in AERODROMOS.items():
        x, y = proj(p, 0)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{INK}"/>')
        out.append(f'<text x="{x + 6:.1f}" y="{y + 13:.1f}" font-size="10.5" fill="{MUTED}" font-weight="600" '
                   f'paint-order="stroke" stroke="#fff" stroke-width="3">{icao}</text>')
    alvo_poli = [proj(p, 0) for p in alvo["contorno"]]
    x, y = ponto_rotulo(alvo_poli, [t[1] for t in tomadas])
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="26" font-weight="800" fill="{INK}" '
               f'paint-order="stroke" stroke="#fff" stroke-width="5">{alvo["rot"]}</text>')
    out.append(f'<text x="{x:.1f}" y="{y + 22:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="{INK}" '
               f'paint-order="stroke" stroke="#fff" stroke-width="4">{nivel(alvo["min"])} – {nivel(alvo["max"])}</text>')
    usados = [(x, y)]  # posições já ocupadas por rótulos
    for f, poli, pts in sorted(tomadas, key=lambda t: sum(p[1] for p in t[2]) / len(t[2])):
        hx = sum(p[0] for p in pts) / len(pts)
        hy = sum(p[1] for p in pts) / len(pts)
        texto = f'{f["rot"]} {nivel(f["min"])} – {nivel(f["max"])}'
        largura_txt = 7.2 * len(texto)
        lx = max(p[0] for p in pts) + 30
        anchor = "start"
        if lx + largura_txt > W - 8:  # não cabe à direita: vai para a esquerda
            lx, anchor = min(p[0] for p in pts) - 30, "end"
        ly = hy + 4
        while any(abs(ly - uy) < 18 and abs(lx - ux) < largura_txt for ux, uy in usados):
            ly += 18
        usados.append((lx, ly))
        fim = lx - 4 if anchor == "start" else lx + 4
        out.append(f'<path d="M{hx:.1f},{hy:.1f} L{fim:.1f},{ly - 4:.1f}" stroke="{INK}" stroke-width="1.2"/>')
        out.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="2.5" fill="{INK}"/>')
        out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" font-size="12" font-weight="700" fill="{INK}" '
                   f'paint-order="stroke" stroke="#fff" stroke-width="4">{texto}</text>')
    return out


def polo_uniao(polis, n=120, obstaculos=(), raio=0):
    """Ponto interno da união de polígonos mais longe da borda (grade + distância)."""
    xs = [p[0] for poli in polis for p in poli]
    ys = [p[1] for poli in polis for p in poli]
    passo = max(max(xs) - min(xs), max(ys) - min(ys)) / n
    nx, ny = int((max(xs) - min(xs)) / passo) + 1, int((max(ys) - min(ys)) / passo) + 1
    def livre(x, y):
        return any(dentro((x, y), poli) for poli in polis) and all(
            math.hypot(x - ox, y - oy) > raio for ox, oy in obstaculos)
    dentro_g = [[livre(min(xs) + i * passo, min(ys) + j * passo) for i in range(nx)] for j in range(ny)]
    # distância (em células) até a célula de fora mais próxima, por varredura em largura
    from collections import deque
    dist = [[0 if not dentro_g[j][i] else None for i in range(nx)] for j in range(ny)]
    fila = deque((i, j) for j in range(ny) for i in range(nx) if dist[j][i] == 0)
    for j in range(ny):
        for i in range(nx):
            if dist[j][i] is None and (i in (0, nx - 1) or j in (0, ny - 1)):
                dist[j][i] = 1
                fila.append((i, j))
    while fila:
        i, j = fila.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            a, b = i + di, j + dj
            if 0 <= a < nx and 0 <= b < ny and dist[b][a] is None:
                dist[b][a] = dist[j][i] + 1
                fila.append((a, b))
    j, i = max(((j, i) for j in range(ny) for i in range(nx)), key=lambda c: dist[c[0]][c[1]])
    return min(xs) + i * passo, min(ys) + j * passo


def mapa_combinado(nome, membros, setores, tma, proj, caminho, W, cor):
    """Área consolidada de uma posição combinada, sem as divisas internas."""
    out = [f'<path d="{caminho(tma, 0)}" fill="#e2e8f0"/>']
    for s in setores:
        if s not in membros and not s["final"]:
            out.append(f'<path d="{caminho(s["contorno"], 0)}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>')
    # todos os membros com a mesma cor e contorno da mesma cor: as divisas internas somem
    # cor opaca (equivale a 85% sobre o cinza): as divisas dos outros setores não aparecem por baixo
    base = [0xE2, 0xE8, 0xF0]
    rgb = [int(cor[k:k + 2], 16) for k in (1, 3, 5)]
    cor = "#" + "".join(f"{round(0.85 * c + 0.15 * b):02x}" for c, b in zip(rgb, base))
    out.append(f'<g>' + "".join(
        f'<path d="{caminho(m["contorno"], 0)}" fill="{cor}" stroke="{cor}" stroke-width="3.5" stroke-linejoin="round"/>'
        for m in membros) + '</g>')
    out.append(f'<path d="{caminho(tma, 0)}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
    for icao, p in AERODROMOS.items():
        x, y = proj(p, 0)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{INK}"/>')
        out.append(f'<text x="{x + 6:.1f}" y="{y + 13:.1f}" font-size="10.5" fill="{MUTED}" font-weight="600" '
                   f'paint-order="stroke" stroke="#fff" stroke-width="3">{icao}</text>')
    # o rótulo (nome e limites) desvia dos aeródromos
    x, y = polo_uniao([[proj(p, 0) for p in m["contorno"]] for m in membros],
                      obstaculos=[proj(p, 0) for p in AERODROMOS.values()], raio=45)
    lo = min(m["min"] for m in membros)
    hi = max(m["max"] for m in membros)
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" font-size="24" font-weight="800" fill="{INK}" '
               f'paint-order="stroke" stroke="#fff" stroke-width="5">{nome}</text>')
    out.append(f'<text x="{x:.1f}" y="{y + 22:.1f}" text-anchor="middle" font-size="14" font-weight="700" fill="{INK}" '
               f'paint-order="stroke" stroke="#fff" stroke-width="4">{nivel(lo)} – {nivel(hi)}</text>')
    return out


def main():
    setores, tma, paleta, cfg = ler_pagina(PAGE)
    AERODROMOS.update(cfg["aerodromos"])
    for k, s in enumerate(setores):
        s["cor"] = paleta[k % len(paleta)]
        s["rot"] = s.get("rot") or rotulo(s["posicao"])
        s["min"], s["max"] = limites(s["lim"])
        s["final"] = cfg["final"](s)

    # projeção equirretangular local
    lon0 = sum(p[0] for p in tma) / len(tma)
    lat0 = sum(p[1] for p in tma) / len(tma)
    kx = math.cos(math.radians(lat0))
    xs = [(p[0] - lon0) * kx for p in tma]
    ys = [-(p[1] - lat0) for p in tma]
    W, H, M, TOPO = 620, 560, 24, 46
    esc = min((W - 2 * M) / (max(xs) - min(xs)), (H - TOPO - M) / (max(ys) - min(ys)))
    x0, y0 = min(xs), min(ys)

    def proj(p, dx):
        return (dx + M + ((p[0] - lon0) * kx - x0) * esc, TOPO + ((-(p[1] - lat0)) - y0) * esc)

    def caminho(poli, dx):
        return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in (proj(p, dx) for p in poli)) + " Z"

    finais = [s for s in setores if s["final"]]
    baixos = [s for s in setores if s["min"] < 13500 and not s["final"]]
    altos = [s for s in setores if s["max"] > 13500]

    def painel(dx, titulo, base, topo=()):
        out = [f'<text x="{dx + W / 2:.0f}" y="28" text-anchor="middle" font-size="17" font-weight="700" fill="{INK}">{titulo}</text>']
        for s in base:
            out.append(f'<path d="{caminho(s["contorno"], dx)}" fill="{s["cor"]}" fill-opacity="0.45" stroke="{INK}" stroke-width="1.2" stroke-linejoin="round"/>')
        for s in topo:
            out.append(f'<path d="{caminho(s["contorno"], dx)}" fill="{s["cor"]}" fill-opacity="0.8" stroke="{INK}" stroke-width="1.6" stroke-dasharray="5 3" stroke-linejoin="round"/>')
        out.append(f'<path d="{caminho(tma, dx)}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
        for icao, p in AERODROMOS.items():
            x, y = proj(p, dx)
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{INK}"/>')
            out.append(f'<text x="{x + 6:.1f}" y="{y + 13:.1f}" font-size="10.5" fill="{MUTED}" font-weight="600" '
                       f'paint-order="stroke" stroke="#fff" stroke-width="3">{icao}</text>')
        evitar = [[proj(f["contorno"][i], dx) for i in range(len(f["contorno"]))] for f in topo]
        for s in list(base) + list(topo):
            poli = [proj(p, dx) for p in s["contorno"]]
            x, y = ponto_rotulo(poli, () if s in topo else evitar)
            out.append(f'<text x="{x:.1f}" y="{y + 6:.1f}" text-anchor="middle" font-size="16" font-weight="800" fill="{INK}" '
                       f'paint-order="stroke" stroke="#fff" stroke-width="4">{s["rot"]}</text>')
        return out

    if COMBINADO:
        combinadas = ler_combinadas(PAGE)
        elementares = expandir(COMBINADO, combinadas, cfg["cobertura"])
        membros = [s for s in setores if s["posicao"] in elementares]
        if not membros:  # TMA sem posições combinadas: a posição única assume tudo
            membros = [s for s in setores if not s["final"]]
        nome = COMBINADO.split("_")[1] if COMBINADO.count("_") == 2 else "APP"
        corpo = mapa_combinado(COMBINADO, membros, setores, tma, proj, caminho, W, cfg["cores"].get(nome, "#60a5fa"))
        largura = W
    elif SETOR:
        alvo = next(s for s in setores if s["rot"] == SETOR)
        corpo = mapa_setor(alvo, setores, tma, proj, caminho, W)
        largura = W
    else:
        corpo = painel(0, "5500 FT – FL135", baixos, finais) + painel(W + 20, "FL135 – FL245", altos)
        largura = 2 * W + 20
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura} {H}" width="{largura}" height="{H}" role="img" '
           f'aria-label="{cfg["nome"]}: setores do APP" {FONT}>\n<title>{cfg["nome"]}: setores do APP</title>\n'
           f'<rect width="{largura}" height="{H}" rx="12" fill="{BG}"/>\n' + "\n".join(corpo) + "\n</svg>\n")
    open(OUT, "w", encoding="utf-8").write(svg)


if __name__ == "__main__":
    main()
