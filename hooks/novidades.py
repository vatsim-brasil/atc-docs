"""Changelog do portal ("Novidades").

Cada entrada é um arquivo em docs/novidades/ (AAAA-MM-DD-slug.pt.md, com .en.md
opcional). Este hook lê o front matter das entradas do idioma em construção e
expõe a lista em ordem decrescente de data como `novidades` (e agrupada como
`novidades_por_mes`) para os templates da home e da página de listagem. As
entradas usam o template novidade.html.
"""

import datetime
import logging
import re

from mkdocs.utils.meta import get_data

log = logging.getLogger("mkdocs.hooks.novidades")

PASTA = "novidades/"

MESES = {
    "pt": ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"],
    "en": ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
}

MESES_EXTENSO = {
    "pt": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",
           "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
    "en": ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"],
}

# Tipos aceitos no front matter e seus rótulos (a cor vem de .vb-strip--<tipo>)
TIPOS = {
    "manual": {"pt": "Manual", "en": "Manual"},
    "ad": {"pt": "Aeródromos", "en": "Aerodromes"},
    "tma": {"pt": "Terminais", "en": "Terminals"},
    "fir": {"pt": "Centros", "en": "Centers"},
    "oca": {"pt": "Atlântico", "en": "Oceanic"},
    "fundamentos": {"pt": "Fundamentos", "en": "Fundamentals"},
    "portal": {"pt": "Portal", "en": "Portal"},
}


def _idioma(config):
    return "en" if str(config.theme["language"]).startswith("en") else "pt"


def _eh_entrada(file):
    return (
        file.src_uri.startswith(PASTA)
        and file.is_documentation_page()
        and not file.name.startswith("index")
    )


def _data(meta, file):
    data = meta.get("date")
    if isinstance(data, datetime.datetime):
        return data.date()
    if isinstance(data, datetime.date):
        return data
    m = re.match(r"(\d{4}-\d{2}-\d{2})", file.name)
    if m:
        return datetime.date.fromisoformat(m.group(1))
    log.warning("%s: sem 'date' no front matter nem no nome do arquivo", file.src_uri)
    return datetime.date.min


def _titulo(meta, markdown, file):
    if meta.get("title"):
        return meta["title"]
    m = re.search(r"^#\s+(.+?)\s*$", markdown, re.MULTILINE)
    return m.group(1) if m else file.name


def _data_longa(data, idioma):
    if data.year <= 1:
        return ""
    mes = MESES_EXTENSO[idioma][data.month - 1]
    if idioma == "en":
        return f"{mes} {data.day}, {data.year}"
    return f"{data.day} de {mes.lower()} de {data.year}"


def on_env(env, config, files):
    idioma = _idioma(config)
    prefixo = "en/" if idioma == "en" else ""
    entradas = []

    for file in files.documentation_pages():
        if not _eh_entrada(file):
            continue
        markdown, meta = get_data(file.content_string)
        tipo = meta.get("tipo", "portal")
        if tipo not in TIPOS:
            log.warning("%s: tipo '%s' desconhecido (use %s)", file.src_uri, tipo, ", ".join(TIPOS))
            tipo = "portal"
        data = _data(meta, file)
        link = meta.get("link")
        entradas.append({
            "titulo": _titulo(meta, markdown, file),
            "resumo": meta.get("resumo", ""),
            "tipo": tipo,
            "rotulo": TIPOS[tipo][idioma],
            "data": data,
            "data_curta": f"{data.day:02d} {MESES[idioma][data.month - 1]}" if data.year > 1 else "",
            "mes": f"{MESES_EXTENSO[idioma][data.month - 1]} {data.year}" if data.year > 1 else "",
            "data_longa": _data_longa(data, idioma),
            "url": file.url,
            "link": (prefixo + link) if link else None,
            "src_uri": file.src_uri,
        })

    entradas.sort(key=lambda e: (e["data"], e["src_uri"]), reverse=True)
    env.globals["novidades"] = entradas
    por_mes = {}
    for e in entradas:
        por_mes.setdefault(e["mes"], []).append(e)
    env.globals["novidades_por_mes"] = list(por_mes.items())
    return env


def on_nav(nav, config, files):
    """Deixa só a listagem no menu; as entradas são alcançadas por ela e pela home."""

    def filtrar(itens):
        restantes = []
        for item in itens:
            if item.is_page and _eh_entrada(item.file):
                continue
            if item.is_section:
                item.children = filtrar(item.children)
            restantes.append(item)
        return restantes

    nav.items = filtrar(nav.items)

    # Refaz os links de anterior/próximo do rodapé sem as entradas
    for page in nav.pages:
        page.previous_page = page.next_page = None
    nav.pages = [p for p in nav.pages if not _eh_entrada(p.file)]
    for anterior, proxima in zip(nav.pages, nav.pages[1:]):
        anterior.next_page = proxima
        proxima.previous_page = anterior
    return nav


def on_page_markdown(markdown, page, config, files):
    if _eh_entrada(page.file):
        page.meta.setdefault("template", "novidade.html")
        page.meta.setdefault("hide", ["navigation", "toc"])
    return markdown

