"""Mapa dos pontos de transferência de chegadas da TMA, lido da tabela da página.

Lê a tabela "Pontos e níveis de transferência" e o contorno da TMA na página, e
as coordenadas dos fixos no .sct do pacote. Cada fixo vira uma seta para dentro
da TMA, na cor do órgão que entrega, com o nível de cada destino.

Uso: python3 -I gen.py <pacote.sct> [pagina.md] [saida.svg]
"""
import json
import math
import re
import sys

SCT = sys.argv[1]
PAGE = sys.argv[2] if len(sys.argv) > 2 else "docs/MOP/terminais/sbcw-curitiba/SBXP.pt.md"
OUT = sys.argv[3] if len(sys.argv) > 3 else "docs/MOP/terminais/sbcw-curitiba/img/sbxp-transferencias.svg"

INK, MUTED = "#1e293b", "#64748b"
PALETA = ["#2563eb", "#16a34a", "#c2410c", "#9333ea", "#0891b2"]
AERODROMOS = {"SBGR": (-46.4731, -23.4356), "SBSP": (-46.6564, -23.6261),
              "SBKP": (-47.1345, -23.0074), "SBSJ": (-45.8615, -23.2292)}
FONT = 'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif"'


def dms(txt):
    h, g, m, s = txt[0], *txt[1:].split(".", 2)
    v = int(g) + int(m) / 60 + float(s) / 3600
    return -v if h in "SW" else v


def ler_fixos(path):
    fixos, secao = {}, None
    for linha in open(path, encoding="latin-1"):
        linha = linha.split(";")[0].rstrip()
        if linha.startswith("["):
            secao = linha
        elif secao == "[FIXES]" and len(linha.split()) >= 3:
            nome, lat, lon = linha.split()[:3]
            fixos[nome] = (dms(lon), dms(lat))
    return fixos


def ler_tabela(texto):
    """[(órgão, código, fixo, destinos, nível)] da tabela de transferência."""
    bloco = texto.split("### Pontos e níveis de transferência", 1)[1].split("\n\n|", 1)[1]
    linhas = []
    for linha in ("|" + bloco).split("\n")[2:]:  # pula cabeçalho e separador
        if not linha.startswith("| **"):
            break
        cols = [c.strip() for c in linha.strip("|").split("|")]
        orgao = re.sub(r"\*\*|\(.*\)", "", cols[0]).strip()
        codigo = (re.findall(r"`([A-Z_]+)`", cols[0]) or [""])[0]
        linhas.append((orgao, codigo, cols[1].strip("*"), cols[2], cols[3].strip("*")))
    return linhas


def main():
    texto = open(PAGE, encoding="utf-8").read()
    volumes = json.loads(re.search(r"const volumes = (\[.*?\]);\n", texto, re.S).group(1))
    tma = next(v for v in volumes if v["tipo"] == "tma" and v["nome"].endswith("1"))["contorno"]
    fixos = ler_fixos(SCT)
    linhas = ler_tabela(texto)

    orgaos = []
    for o, c, *_ in linhas:
        if (o, c) not in orgaos:
            orgaos.append((o, c))
    cor = {o: PALETA[k % len(PALETA)] for k, (o, _) in enumerate(orgaos)}

    # um rótulo por fixo, com uma linha por destino
    por_fixo = {}
    for o, c, fx, dest, nivel in linhas:
        por_fixo.setdefault(fx, {"orgao": o, "linhas": []})["linhas"].append((dest, nivel))

    pts = tma + [fixos[f] for f in por_fixo]
    lon0 = sum(p[0] for p in tma) / len(tma)
    lat0 = sum(p[1] for p in tma) / len(tma)
    kx = math.cos(math.radians(lat0))
    xs = [(p[0] - lon0) * kx for p in pts]
    ys = [-(p[1] - lat0) for p in pts]
    W, H, M = 940, 760, 120
    esc = min((W - 2 * M) / (max(xs) - min(xs)), (H - 2 * M + 40) / (max(ys) - min(ys)))
    x0 = min(xs) - ((W - 2 * M) / esc - (max(xs) - min(xs))) / 2
    y0 = min(ys) - ((H - 2 * M + 40) / esc - (max(ys) - min(ys))) / 2

    def pr(p):
        return (M + ((p[0] - lon0) * kx - x0) * esc, M - 20 + (-(p[1] - lat0) - y0) * esc)

    cx, cy = pr((lon0, lat0))
    out = [f'<rect width="{W}" height="{H}" rx="12" fill="#f8fafc"/>',
           '<defs>' + "".join(
               f'<marker id="s{k}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
               f'<path d="M0,0 L10,5 L0,10 z" fill="{cor[o]}"/></marker>' for k, (o, _) in enumerate(orgaos)) + '</defs>',
           '<path d="M' + " L".join(f"{x:.1f},{y:.1f}" for x, y in map(pr, tma)) +
           f' Z" fill="#e2e8f0" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>']
    for icao, p in AERODROMOS.items():
        x, y = pr(p)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{INK}"/>')
        out.append(f'<text x="{x + 7:.1f}" y="{y + 4:.1f}" font-size="12" font-weight="700" fill="{MUTED}">{icao}</text>')

    for fx, info in por_fixo.items():
        x, y = pr(fixos[fx])
        k = [o for o, _ in orgaos].index(info["orgao"])
        c = cor[info["orgao"]]
        # seta do fixo em direção ao centro da TMA
        d = math.hypot(cx - x, cy - y)
        ux, uy = (cx - x) / d, (cy - y) / d
        out.append(f'<path d="M{x:.1f},{y:.1f} L{x + ux * 70:.1f},{y + uy * 70:.1f}" stroke="{c}" stroke-width="5" '
                   f'marker-end="url(#s{k})"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#fff" stroke="{c}" stroke-width="3"/>')
        # rótulo do lado de fora (oposto ao centro)
        lx, ly = x - ux * 16, y - uy * 16
        anchor = "end" if ux > 0.35 else "start" if ux < -0.35 else "middle"
        n = len(info["linhas"])
        topo = ly - (n * 17 + 20) if uy > 0.35 else ly + 18 if uy < -0.35 else ly - (n * 17) / 2 - 4
        out.append(f'<text x="{lx:.1f}" y="{topo + 14:.1f}" text-anchor="{anchor}" font-size="17" font-weight="800" fill="{c}" '
                   f'paint-order="stroke" stroke="#f8fafc" stroke-width="4">{fx}</text>')
        for j, (dest, nivel) in enumerate(info["linhas"]):
            out.append(f'<text x="{lx:.1f}" y="{topo + 32 + j * 17:.1f}" text-anchor="{anchor}" font-size="13.5" fill="{INK}" '
                       f'paint-order="stroke" stroke="#f8fafc" stroke-width="4">{dest.replace(", ", " · ")} '
                       f'<tspan font-weight="800">{nivel}</tspan></text>')

    # legenda dos órgãos, empilhada no canto inferior direito
    for k, (o, c) in enumerate(orgaos):
        ly = H - 24 - (len(orgaos) - 1 - k) * 22
        out.append(f'<path d="M{W - 300},{ly - 5} h28" stroke="{cor[o]}" stroke-width="5"/>')
        rot = f"{o} ({c})" if c else o
        out.append(f'<text x="{W - 264}" y="{ly}" font-size="13" font-weight="700" fill="{INK}">{rot}</text>')
    titulo = "TMA São Paulo: pontos e níveis de transferência das chegadas"
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
           f'aria-label="{titulo}" {FONT}>\n<title>{titulo}</title>\n' + "\n".join(out) + "\n</svg>\n")
    open(OUT, "w", encoding="utf-8").write(svg)


if __name__ == "__main__":
    main()
