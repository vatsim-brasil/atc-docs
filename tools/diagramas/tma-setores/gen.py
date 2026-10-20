"""Gera o SVG dos setores do APP de uma TMA a partir do mapa da própria página.

Lê os arrays `setores` e `volumes` do script Leaflet da página (que vêm do
pacote de setores) e desenha dois painéis lado a lado: camada baixa
(até FL135, com as finais por cima) e camada alta (FL135 a FL245).

Uso: python3 -I gen.py [pagina.md] [saida.svg]
     python3 -I gen.py <pagina.md> <saida.svg> --setor T1   (um mapa por setor)
     python3 -I gen.py <pagina.md> <saida.svg> --combinado SBXP_S_APP   (posição combinada)
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

# Aeródromos de referência (ARP, graus decimais)
AERODROMOS = {
    "SBGR": (-46.4731, -23.4356),
    "SBSP": (-46.6564, -23.6261),
    "SBKP": (-47.1345, -23.0074),
    "SBSJ": (-45.8615, -23.2292),
}
INK, MUTED, BG = "#1e293b", "#64748b", "#f8fafc"
FONT = 'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif"'


def ler_combinadas(path):
    """Tabela "Posições combinadas" da página: posição -> posições que assume."""
    texto = open(path, encoding="utf-8").read()
    bloco = texto.split("### Posições combinadas", 1)[1].split("\n## ", 1)[0]
    res = {}
    for linha in bloco.splitlines():
        cols = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(cols) == 3 and cols[0].startswith("`"):
            res[cols[0].strip("`")] = re.findall(r"`([A-Z0-9_]+)`", cols[2])
    return res


def expandir(posicao, combinadas):
    """Posições elementares que uma posição combinada assume."""
    if posicao not in combinadas:
        return [posicao]
    return [e for p in combinadas[posicao] for e in expandir(p, combinadas)]


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
    return f"FL{ft // 100:03d}" if ft >= 10000 else f"{ft} FT"


def mapa_setor(alvo, setores, tma, proj, caminho, W):
    """Um setor preenchido; o resto da TMA em cinza, só com as divisas."""
    out = ['<defs><pattern id="hach" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           f'<rect width="8" height="8" fill="#fff" fill-opacity="0.55"/><path d="M0,0 V8" stroke="{INK}" stroke-width="2"/></pattern>'
           f'<clipPath id="clip-alvo"><path d="{caminho(alvo["contorno"], 0)}"/></clipPath></defs>']
    out.append(f'<path d="{caminho(tma, 0)}" fill="#e2e8f0"/>')
    for s in setores:
        if s is not alvo and not s["rot"].startswith("F"):
            out.append(f'<path d="{caminho(s["contorno"], 0)}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>')
    out.append(f'<path d="{caminho(alvo["contorno"], 0)}" fill="{alvo["cor"]}" fill-opacity="0.85" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>')
    # finais que tomam parte do setor abaixo de FL100: hachuradas, recortadas no setor
    tomadas = []
    for f in setores:
        if f is not alvo and not alvo["rot"].startswith("F") and f["rot"].startswith("F") and f["max"] > alvo["min"]:
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


def mapa_combinado(nome, membros, setores, tma, proj, caminho, W, cor):
    """Setores de uma posição combinada preenchidos; finais hachuradas por cima."""
    ts = [m for m in membros if not m["rot"].startswith("F")]
    fs = [m for m in membros if m["rot"].startswith("F")]
    clip = "".join(f'<path d="{caminho(m["contorno"], 0)}"/>' for m in ts)
    out = ['<defs><pattern id="hach" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           f'<rect width="8" height="8" fill="#fff" fill-opacity="0.55"/><path d="M0,0 V8" stroke="{INK}" stroke-width="2"/></pattern>'
           f'<clipPath id="clip-alvo">{clip}</clipPath></defs>']
    out.append(f'<path d="{caminho(tma, 0)}" fill="#e2e8f0"/>')
    for s in setores:
        if s not in ts and not s["rot"].startswith("F"):
            out.append(f'<path d="{caminho(s["contorno"], 0)}" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>')
    for m in ts:
        out.append(f'<path d="{caminho(m["contorno"], 0)}" fill="{cor}" fill-opacity="0.85" stroke="{cor}" stroke-width="2" stroke-linejoin="round"/>')
    for m in ts:  # divisas internas
        out.append(f'<path d="{caminho(m["contorno"], 0)}" fill="none" stroke="#fff" stroke-width="1.5" stroke-dasharray="6 4"/>')
    # finais dentro da área: as assumidas explicitamente e as que caem nos setores membros
    tomadas = []
    for f in setores:
        if not f["rot"].startswith("F"):
            continue
        poli = [proj(p, 0) for p in f["contorno"]]
        comuns = []
        for m in ts:
            if f["max"] <= m["min"]:  # final abaixo do setor: não toma parte dele
                continue
            c, total = pontos_comuns([proj(p, 0) for p in m["contorno"]], poli)
            if total and len(c) / total > 0.01:
                comuns += c
        if f in fs:
            comuns = comuns or [(x, y) for x, y in poli]
            out.append(f'<path d="{caminho(f["contorno"], 0)}" fill="url(#hach)" stroke="{INK}" stroke-width="1.4" stroke-dasharray="5 3"/>')
        elif comuns:
            out.append(f'<path d="{caminho(f["contorno"], 0)}" fill="url(#hach)" stroke="{INK}" stroke-width="1.4" '
                       'stroke-dasharray="5 3" clip-path="url(#clip-alvo)"/>')
        if comuns:
            tomadas.append((f, poli, comuns))
    out.append(f'<path d="{caminho(tma, 0)}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
    for icao, p in AERODROMOS.items():
        x, y = proj(p, 0)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" fill="{INK}"/>')
        out.append(f'<text x="{x + 6:.1f}" y="{y + 13:.1f}" font-size="10.5" fill="{MUTED}" font-weight="600" '
                   f'paint-order="stroke" stroke="#fff" stroke-width="3">{icao}</text>')
    usados = []
    evitar = [t[1] for t in tomadas]
    camadas = len({(m["min"], m["max"]) for m in ts}) > 1
    for m in ts:  # setores maiores primeiro, para os menores desviarem dos rótulos
        poli = [proj(p, 0) for p in m["contorno"]]
        x, y = ponto_rotulo(poli, evitar)
        usados.append((x - 34, y - 16, x + 34, y + (24 if camadas else 8)))
        evitar.append([(x - 34, y - 16), (x + 34, y - 16), (x + 34, y + 24), (x - 34, y + 24)])
        out.append(f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" font-size="17" font-weight="800" fill="{INK}" '
                   f'paint-order="stroke" stroke="#fff" stroke-width="4">{m["rot"]}</text>')
        if camadas:  # com camadas diferentes, cada rótulo leva os seus limites
            out.append(f'<text x="{x:.1f}" y="{y + 19:.1f}" text-anchor="middle" font-size="10.5" font-weight="700" fill="{INK}" '
                       f'paint-order="stroke" stroke="#fff" stroke-width="3">{nivel(m["min"])} – {nivel(m["max"])}</text>')
    for f, poli, pts in sorted(tomadas, key=lambda t: sum(p[1] for p in t[2]) / len(t[2])):
        hx = sum(p[0] for p in pts) / len(pts)
        hy = sum(p[1] for p in pts) / len(pts)
        texto = f'{f["rot"]} {nivel(f["min"])} – {nivel(f["max"])}'
        largura_txt = 7.2 * len(texto)
        lx, anchor = max(p[0] for p in pts) + 30, "start"
        if lx + largura_txt > W - 8:
            lx, anchor = min(p[0] for p in pts) - 30, "end"

        def caixa(ly):
            x0 = lx if anchor == "start" else lx - largura_txt
            return (x0 - 3, ly - 13, x0 + largura_txt + 3, ly + 4)

        def colide(c):
            return any(c[0] < u[2] and u[0] < c[2] and c[1] < u[3] and u[1] < c[3] for u in usados)

        ly = hy + 4
        for k in range(1, 30):  # procura a vaga livre mais próxima, alternando acima e abaixo
            if not colide(caixa(ly)):
                break
            ly = hy + 4 + (k + 1) // 2 * 18 * (1 if k % 2 else -1)
        usados.append(caixa(ly))
        fim = lx - 4 if anchor == "start" else lx + 4
        out.append(f'<path d="M{hx:.1f},{hy:.1f} L{fim:.1f},{ly - 4:.1f}" stroke="{INK}" stroke-width="1.2"/>')
        out.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="2.5" fill="{INK}"/>')
        out.append(f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anchor}" font-size="12" font-weight="700" fill="{INK}" '
                   f'paint-order="stroke" stroke="#fff" stroke-width="4">{texto}</text>')
    # cabeçalho: nome da combinada e limites
    lo = min(m["min"] for m in ts)
    hi = max(m["max"] for m in ts)
    out.append(f'<text x="22" y="40" font-size="26" font-weight="800" fill="{INK}">{nome}</text>')
    out.append(f'<text x="22" y="62" font-size="14" font-weight="700" fill="{MUTED}">{nivel(lo)} – {nivel(hi)}</text>')
    return out


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

    if COMBINADO:
        combinadas = ler_combinadas(PAGE)
        elementares = expandir(COMBINADO, combinadas)
        membros = [s for s in setores if s["posicao"] in elementares]
        cores = {"S": "#60a5fa", "E": "#34d399", "N": "#f472b6", "NL": "#fb923c", "NU": "#a78bfa", "APP": "#38bdf8"}
        nome = COMBINADO.split("_")[1] if COMBINADO.count("_") == 2 else "APP"
        corpo = mapa_combinado(COMBINADO, membros, setores, tma, proj, caminho, W, cores.get(nome, "#60a5fa"))
        largura = W
    elif SETOR:
        alvo = next(s for s in setores if s["rot"] == SETOR)
        corpo = mapa_setor(alvo, setores, tma, proj, caminho, W)
        largura = W
    else:
        corpo = painel(0, "5500 FT – FL135", baixos, finais) + painel(W + 20, "FL135 – FL245", altos)
        largura = 2 * W + 20
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura} {H}" width="{largura}" height="{H}" role="img" '
           f'aria-label="TMA São Paulo: setores do APP" {FONT}>\n<title>TMA São Paulo: setores do APP</title>\n'
           f'<rect width="{largura}" height="{H}" rx="12" fill="{BG}"/>\n' + "\n".join(corpo) + "\n</svg>\n")
    open(OUT, "w", encoding="utf-8").write(svg)


if __name__ == "__main__":
    main()
