"""Mapas de circulação da TMA: chegadas, saídas e pontos de conflito potencial.

Lê as SID e STAR do pacote de setores (.ese) e as coordenadas dos fixos e das
cabeceiras (.sct), monta as rotas de cada configuração de pistas e marca onde
uma chegada cruza uma saída dentro da TMA com níveis estimados próximos.

Níveis estimados em cada cruzamento, a partir das restrições das cartas
(restricoes.py):
- chegada: rampa de 3° (318 pés por NM) desde a cabeceira, para trás, presa
  às restrições de cada fixo;
- saída: subida de 500 pés por NM desde a cabeceira, presa às restrições.
Há conflito potencial quando os dois níveis estimados ficam a menos de 4000 pés
um do outro, abaixo do topo da TMA (vermelho: menos de 2000 pés; laranja: 2000 a
4000 pés). Com diretos, vetores ou restrições canceladas, é ali que a separação
vertical dada pelas cartas pode acabar. Cruzamentos a menos de 5 NM da cabeceira
ficam com a Torre e não entram.

Uso: python3 -I gen.py <pacote.ese> <pacote.sct> [pagina_da_tma.md] [pasta_de_saida]
"""
import json
import math
import re
import sys

from restricoes import SID, STAR, faixa

ESE, SCT = sys.argv[1], sys.argv[2]
PAGE = sys.argv[3] if len(sys.argv) > 3 else "docs/MOP/terminais/sbcw-curitiba/SBXP.pt.md"
OUT = sys.argv[4] if len(sys.argv) > 4 else "docs/MOP/terminais/sbcw-curitiba/img"

ELEV = {"SBGR": 2461, "SBSP": 2634, "SBKP": 2170}
# STAR com arco de point merge: fora do mapa, que mostra a operação do dia a dia
ARCO = {"MOLLE1A", "MOLLE1B", "VUNOX1A", "VUNOX1C"}
CONFIGS = {
    "sudeste": {"titulo": "SBGR 10 · SBSP 17 · SBKP 15",
                "pouso": {"SBGR": "10R", "SBSP": "17R", "SBKP": "15"},
                "decolagem": {"SBGR": "10L", "SBSP": "17R", "SBKP": "15"}},
    "noroeste": {"titulo": "SBGR 28 · SBSP 35 · SBKP 33",
                 "pouso": {"SBGR": "28L", "SBSP": "35L", "SBKP": "33"},
                 "decolagem": {"SBGR": "28R", "SBSP": "35L", "SBKP": "33"}},
}
COR = {"SBGR": "#2563eb", "SBSP": "#0d9488", "SBKP": "#9333ea"}
INK, MUTED, RED = "#1e293b", "#64748b", "#dc2626"
FONT = 'font-family="Ubuntu Sans, Ubuntu, Segoe UI, Roboto, Arial, sans-serif"'
NM_POR_GRAU = 60.0
AGRUPAR_NM = 3.0
TOPO_TMA = 24500
LIMITE_PES = 4000
ORANGE = "#ea580c"


def dms(txt):
    """S023.25.36.861 -> -23.4269"""
    h, g, m, s = txt[0], *txt[1:].split(".", 2)
    s = float(s)
    v = int(g) + int(m) / 60 + s / 3600
    return -v if h in "SW" else v


def ler_sct(path):
    fixos, cabeceiras, secao = {}, {}, None
    for linha in open(path, encoding="latin-1"):
        linha = linha.split(";")[0].rstrip()
        if linha.startswith("["):
            secao = linha
            continue
        partes = linha.split()
        if secao == "[FIXES]" and len(partes) >= 3:
            fixos[partes[0]] = (dms(partes[2]), dms(partes[1]))
        elif secao in ("[VOR]", "[NDB]") and len(partes) >= 4:
            fixos[partes[0]] = (dms(partes[3]), dms(partes[2]))
        elif secao == "[RUNWAY]" and len(partes) >= 9:
            r1, r2, _, _, la1, lo1, la2, lo2, ad = partes[:9]
            cabeceiras[(ad, r1)] = (dms(lo1), dms(la1))
            cabeceiras[(ad, r2)] = (dms(lo2), dms(la2))
    return fixos, cabeceiras


def ler_procedimentos(path):
    procs = []
    for linha in open(path, encoding="latin-1"):
        if linha.startswith(("SID:", "STAR:")):
            tipo, ad, rwy, nome, rota = linha.rstrip("\n").split(":", 4)
            procs.append((tipo, ad, rwy, nome, rota.split()))
    return procs


def nome_star(chave):
    """'BUXUKxMOLLE1DxILSxY' -> ('BUXUK MOLLE1D', 'ILS'); só chaves com nome de STAR."""
    partes = chave.split("x")
    aprox = partes[-2] if len(partes) >= 3 and partes[-2] in ("ILS", "RNP", "LOC", "VORDME") else None
    corpo = partes[:-2] if aprox else partes
    if not any(re.fullmatch(r"[A-Z]{3,5}\d[A-Z]", p) for p in corpo):
        return None, None
    return " ".join(corpo), aprox


def rotas_config(cfg, procs, fixos, cabeceiras):
    chegadas, saidas = {}, {}
    pref = {"ILS": 0, "RNP": 1, "LOC": 2, "VORDME": 3}
    for tipo, ad, rwy, nome, rota in procs:
        if ad not in ELEV:
            continue
        if tipo == "STAR" and rwy == cfg["pouso"][ad]:
            star, aprox = nome_star(nome)
            if not star or any(a in star for a in ARCO):
                continue
            chave = (ad, star)
            if chave in chegadas and pref.get(aprox, 9) >= chegadas[chave][0]:
                continue
            pts = [(f, fixos[f]) for f in rota if f in fixos] + [("THR", cabeceiras[(ad, rwy)])]
            base = next(t for t in star.split() if re.fullmatch(r"[A-Z]{3,5}\d[A-Z]", t))
            chegadas[chave] = (pref.get(aprox, 9), perfil_chegada(pts, STAR.get(base, {}), ELEV[ad]))
        elif tipo == "SID" and rwy == cfg["decolagem"][ad] and nome != "OMNI":
            pts = [("THR", cabeceiras[(ad, rwy)])] + [(f, fixos[f]) for f in rota if f in fixos]
            saidas[(ad, nome.replace("x", " "))] = perfil_saida(pts, SID.get(nome.split("x")[0], {}), ELEV[ad])
    return {k: v[1] for k, v in chegadas.items()}, saidas


def prender(alt, restr):
    lo, hi = faixa(restr) if restr else (None, None)
    if hi is not None and alt > hi:
        alt = hi
    if lo is not None and alt < lo:
        alt = lo
    return alt


def perfil_chegada(pts, restr, elev):
    """[(ponto, altitude estimada)], da entrada até a cabeceira."""
    alts = [elev] * len(pts)
    for i in range(len(pts) - 2, -1, -1):
        alts[i] = prender(alts[i + 1] + 318 * dist_nm(pts[i][1], pts[i + 1][1]), restr.get(pts[i][0]))
    return [(p, a) for (_, p), a in zip(pts, alts)]


def perfil_saida(pts, restr, elev):
    alts = [elev] * len(pts)
    for i in range(1, len(pts)):
        alts[i] = prender(alts[i - 1] + 500 * dist_nm(pts[i - 1][1], pts[i][1]), restr.get(pts[i][0]))
    return [(p, a) for (_, p), a in zip(pts, alts)]


def dist_nm(a, b):
    kx = math.cos(math.radians((a[1] + b[1]) / 2))
    return math.hypot((a[0] - b[0]) * kx, a[1] - b[1]) * NM_POR_GRAU


def cruzamento(p1, p2, q1, q2):
    """Interseção de dois segmentos (lon/lat), com o parâmetro em cada um."""
    d = (p2[0] - p1[0]) * (q2[1] - q1[1]) - (p2[1] - p1[1]) * (q2[0] - q1[0])
    if abs(d) < 1e-12:
        return None
    t = ((q1[0] - p1[0]) * (q2[1] - q1[1]) - (q1[1] - p1[1]) * (q2[0] - q1[0])) / d
    u = ((q1[0] - p1[0]) * (p2[1] - p1[1]) - (q1[1] - p1[1]) * (p2[0] - p1[0])) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1])), t, u
    return None


def dentro(p, poli):
    x, y = p
    res = False
    for (x1, y1), (x2, y2) in zip(poli, poli[1:] + poli[:1]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            res = not res
    return res


def conflitos(chegadas, saidas, tma):
    achados = []
    for (ad_c, star), rc in chegadas.items():
        falta = [0.0] * len(rc)
        for i in range(len(rc) - 2, -1, -1):
            falta[i] = falta[i + 1] + dist_nm(rc[i][0], rc[i + 1][0])
        for (ad_s, sid), rs in saidas.items():
            andado = [0.0]
            for i in range(1, len(rs)):
                andado.append(andado[-1] + dist_nm(rs[i - 1][0], rs[i][0]))
            for i in range(len(rc) - 1):
                for j in range(len(rs) - 1):
                    r = cruzamento(rc[i][0], rc[i + 1][0], rs[j][0], rs[j + 1][0])
                    if not r:
                        continue
                    p, t, u = r
                    if not dentro(p, tma):
                        continue
                    if falta[i + 1] + dist_nm(p, rc[i + 1][0]) < 5 or andado[j] + dist_nm(rs[j][0], p) < 5:
                        continue
                    alt_c = rc[i][1] + t * (rc[i + 1][1] - rc[i][1])
                    alt_s = rs[j][1] + u * (rs[j + 1][1] - rs[j][1])
                    if max(alt_c, alt_s) > TOPO_TMA + 500:
                        continue
                    if abs(alt_c - alt_s) < LIMITE_PES:
                        achados.append({"p": p, "chegada": f"{ad_c} {star}", "saida": f"{ad_s} {sid}",
                                        "alt_c": alt_c, "alt_s": alt_s})
    # agrupa cruzamentos próximos num ponto só
    grupos = []
    for a in achados:
        for g in grupos:
            if dist_nm(a["p"], g["p"]) <= AGRUPAR_NM:
                g["itens"].append(a)
                n = len(g["itens"])
                g["p"] = ((g["p"][0] * (n - 1) + a["p"][0]) / n, (g["p"][1] * (n - 1) + a["p"][1]) / n)
                break
        else:
            grupos.append({"p": a["p"], "itens": [a]})
    return grupos


def base(nome):
    """'SBGR BUXUK MOLLE1D' -> 'SBGR MOLLE 1D'; 'SBKP EGBEN1A GERTU' -> 'SBKP EGBEN 1A'."""
    ad, *resto = nome.split()
    proc = next((t for t in resto if re.fullmatch(r"[A-Z]{3,5}\d[A-Z]", t)), resto[0])
    return f"{ad} {proc[:-2]} {proc[-2:]}"


def faixa_txt(f):
    a, b = fl(f[0]), fl(f[1])
    return a if a == b else f"{a}–{b}"


def fl(ft):
    ft = int(round(ft / 500.0) * 500)
    return f"FL{ft // 100:03d}" if ft >= 10000 else f"{ft} FT"


def svg_config(nome, cfg, chegadas, saidas, grupos, tma):
    lon0 = sum(p[0] for p in tma) / len(tma)
    lat0 = sum(p[1] for p in tma) / len(tma)
    kx = math.cos(math.radians(lat0))
    xs = [(p[0] - lon0) * kx for p in tma]
    ys = [-(p[1] - lat0) for p in tma]
    W, H, M, TOPO = 900, 760, 30, 50
    esc = min((W - 2 * M) / (max(xs) - min(xs)), (H - TOPO - M) / (max(ys) - min(ys)))
    x0, y0 = min(xs), min(ys)

    def pr(p):
        return (M + ((p[0] - lon0) * kx - x0) * esc, TOPO + (-(p[1] - lat0) - y0) * esc)

    def linha(pts):
        return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in map(pr, pts))

    out = [f'<defs><clipPath id="vista"><path d="{linha(tma)} Z"/></clipPath>'
           f'<marker id="seta" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto">'
           f'<path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker></defs>',
           f'<rect width="{W}" height="{H}" rx="12" fill="#f8fafc"/>',
           f'<path d="{linha(tma)} Z" fill="#eef2f7" stroke="{INK}" stroke-width="2.4"/>',
           '<g clip-path="url(#vista)" fill="none" stroke-linejoin="round" stroke-linecap="round">']
    for (ad, _), perfil in chegadas.items():
        pts = [p for p, _ in perfil]
        out.append(f'<path d="{linha(pts)}" stroke="{COR[ad]}" stroke-width="2" stroke-opacity="0.8"/>')
    for (ad, _), perfil in saidas.items():
        pts = [p for p, _ in perfil]
        out.append(f'<path d="{linha(pts)}" stroke="{COR[ad]}" stroke-width="2" stroke-opacity="0.8" stroke-dasharray="6 4"/>')
    out.append("</g>")
    for ad in ELEV:
        x, y = pr(next(perfil[-1][0] for (a, _), perfil in chegadas.items() if a == ad))
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{COR[ad]}" stroke="#fff" stroke-width="2"/>')
        out.append(f'<text x="{x + 8:.1f}" y="{y - 8:.1f}" font-size="13" font-weight="800" fill="{COR[ad]}" '
                   f'paint-order="stroke" stroke="#fff" stroke-width="4">{ad}</text>')
    for k, g in enumerate(grupos, 1):
        x, y = pr(g["p"])
        dif = min(abs(i["alt_c"] - i["alt_s"]) for i in g["itens"])
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="{RED if dif < 2000 else ORANGE}" stroke="#fff" stroke-width="2.5"/>')
        out.append(f'<text x="{x:.1f}" y="{y + 4.5:.1f}" text-anchor="middle" font-size="12.5" font-weight="800" fill="#fff">{k}</text>')
    out.append(f'<text x="{W / 2:.0f}" y="32" text-anchor="middle" font-size="19" font-weight="800" fill="{INK}">{cfg["titulo"]}</text>')
    # legenda
    ly = H - 24
    lx = 24
    for ad in ELEV:
        out.append(f'<path d="M{lx},{ly} h26" stroke="{COR[ad]}" stroke-width="3"/>')
        out.append(f'<text x="{lx + 32}" y="{ly + 4}" font-size="12" font-weight="700" fill="{INK}">{ad}</text>')
        lx += 86
    out.append(f'<path d="M{lx},{ly} h26" stroke="{INK}" stroke-width="3"/>')
    out.append(f'<text x="{lx + 32}" y="{ly + 4}" font-size="12" fill="{INK}">ARR</text>')
    lx += 76
    out.append(f'<path d="M{lx},{ly} h26" stroke="{INK}" stroke-width="3" stroke-dasharray="7 5"/>')
    out.append(f'<text x="{lx + 32}" y="{ly + 4}" font-size="12" fill="{INK}">DEP</text>')
    lx += 76
    out.append(f'<circle cx="{lx + 10}" cy="{ly}" r="8" fill="{RED}"/>')
    out.append(f'<text x="{lx + 24}" y="{ly + 4}" font-size="12" fill="{INK}">&lt; 2000 FT</text>')
    lx += 104
    out.append(f'<circle cx="{lx + 10}" cy="{ly}" r="8" fill="{ORANGE}"/>')
    out.append(f'<text x="{lx + 24}" y="{ly + 4}" font-size="12" fill="{INK}">2000–4000 FT</text>')
    titulo = f"TMA São Paulo: circulação {cfg['titulo']}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="{titulo}" {FONT}>\n<title>{titulo}</title>\n' + "\n".join(out) + "\n</svg>\n")


def main():
    texto = open(PAGE, encoding="utf-8").read()
    volumes = json.loads(re.search(r"const volumes = (\[.*?\]);\n", texto, re.S).group(1))
    tma = next(v for v in volumes if v["tipo"] == "tma" and v["nome"].endswith("1"))["contorno"]
    fixos, cabeceiras = ler_sct(SCT)
    procs = ler_procedimentos(ESE)
    resumo = {}
    for nome, cfg in CONFIGS.items():
        chegadas, saidas = rotas_config(cfg, procs, fixos, cabeceiras)
        grupos = conflitos(chegadas, saidas, tma)
        # numera do norte para o sul, de oeste para leste
        grupos.sort(key=lambda g: (-round(g["p"][1] * 6), g["p"][0]))
        open(f"{OUT}/sbxp-circulacao-{nome}.svg", "w", encoding="utf-8").write(
            svg_config(nome, cfg, chegadas, saidas, grupos, tma))
        resumo[nome] = []
        for k, g in enumerate(grupos, 1):
            pares = sorted({(i["chegada"], i["saida"]) for i in g["itens"]})
            resumo[nome].append({"n": k, "pares": pares,
                                 "alt_c": (min(i["alt_c"] for i in g["itens"]), max(i["alt_c"] for i in g["itens"])),
                                 "alt_s": (min(i["alt_s"] for i in g["itens"]), max(i["alt_s"] for i in g["itens"]))})
        print(f"== {nome}: {len(chegadas)} chegadas, {len(saidas)} saídas, {len(grupos)} pontos")
        print("| Ponto | Chegada | Saída | Nível estimado (chegada / saída) |")
        print("| :---: | :--- | :--- | :--- |")
        for r in resumo[nome]:
            chg = sorted({base(c) for c, _ in r["pares"]})
            sai = sorted({base(s_) for _, s_ in r["pares"]})
            print(f"| **{r['n']}** | {', '.join(chg)} | {', '.join(sai)} | "
                  f"{faixa_txt(r['alt_c'])} / {faixa_txt(r['alt_s'])} |")

if __name__ == "__main__":
    main()
