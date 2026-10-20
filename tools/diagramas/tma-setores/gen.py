"""Gera o SVG dos setores do APP de uma TMA a partir do mapa da própria página.

Lê os arrays `setores` e `volumes` do script Leaflet da página (que vêm do
pacote de setores) e desenha dois painéis lado a lado: camada baixa
(até FL135, com as finais por cima) e camada alta (FL135 a FL245).

Uso: python3 -I gen.py [pagina.md] [saida.svg]
"""
import json
import math
import re
import sys

PAGE = sys.argv[1] if len(sys.argv) > 1 else "docs/MOP/terminais/sbcw-curitiba/SBXP.pt.md"
OUT = sys.argv[2] if len(sys.argv) > 2 else "docs/MOP/terminais/sbcw-curitiba/img/sbxp-setores.svg"

# Aeródromos de referência (ARP, graus decimais)
AERODROMOS = {
    "SBGR": (-46.4731, -23.4356),
    "SBSP": (-46.6564, -23.6261),
    "SBKP": (-47.1345, -23.0074),
    "SBSJ": (-45.8615, -23.2292),
}
INK, MUTED, BG = "#1e293b", "#64748b", "#f8fafc"
FONT = 'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif"'


def ler_pagina(path):
    texto = open(path, encoding="utf-8").read()
    setores = json.loads(re.search(r"const setores = (\[.*?\]);\n", texto, re.S).group(1))
    volumes = json.loads(re.search(r"const volumes = (\[.*?\]);\n", texto, re.S).group(1))
    paleta = json.loads(re.search(r"const paletaSetores = (\[.*?\]);", texto).group(1).replace("'", '"'))
    tma = next(v for v in volumes if v["tipo"] == "tma" and v["nome"].endswith("1"))
    return setores, tma["contorno"], paleta


def rotulo(posicao):
    """SBXP_T1_APP -> T1; SBGR_F_APP -> FGR."""
    icao, meio = posicao.split("_")[0], posicao.split("_")[1]
    return "F" + icao[2:] if meio == "F" else meio


def limites(lim):
    def ft(t):
        t = t.strip()
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


def main():
    setores, tma, paleta = ler_pagina(PAGE)
    for k, s in enumerate(setores):
        s["cor"] = paleta[k % len(paleta)]
        s["rot"] = rotulo(s["posicao"])
        s["min"], s["max"] = limites(s["lim"])

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

    finais = [s for s in setores if s["rot"].startswith("F")]
    baixos = [s for s in setores if s["min"] < 13500 and not s["rot"].startswith("F")]
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

    corpo = painel(0, "5500 FT – FL135", baixos, finais) + painel(W + 20, "FL135 – FL245", altos)
    largura = 2 * W + 20
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura} {H}" width="{largura}" height="{H}" role="img" '
           f'aria-label="TMA São Paulo: setores do APP" {FONT}>\n<title>TMA São Paulo: setores do APP</title>\n'
           f'<rect width="{largura}" height="{H}" rx="12" fill="{BG}"/>\n' + "\n".join(corpo) + "\n</svg>\n")
    open(OUT, "w", encoding="utf-8").write(svg)


if __name__ == "__main__":
    main()
