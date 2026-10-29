"""Changelog do portal ("Novidades").

Cada deploy (merge de pull request no master) vira uma página em novidades/,
gerada a partir do histórico do git: o título é o do PR e o corpo lista todos os
commits que ele publicou, agrupados por tipo. O tipo da faixa (aeródromos,
terminais, manuais...) vem dos arquivos que o PR alterou. O hook expõe a lista em
ordem decrescente como `novidades` (e agrupada como `novidades_por_mes`) para os
templates da home e da página de listagem. As páginas usam o template
novidade.html.
"""

import collections
import datetime
import html
import logging
import re
import subprocess
from types import SimpleNamespace

from mkdocs.plugins import event_priority
from mkdocs.structure.files import File

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

# Tipos de faixa e seus rótulos (a cor vem de .vb-strip--<tipo>)
TIPOS = {
    "manual": {"pt": "Manual", "en": "Manual"},
    "ad": {"pt": "Aeródromos", "en": "Aerodromes"},
    "tma": {"pt": "Terminais", "en": "Terminals"},
    "fir": {"pt": "Centros", "en": "Centers"},
    "oca": {"pt": "Atlântico", "en": "Oceanic"},
    "fundamentos": {"pt": "Fundamentos", "en": "Fundamentals"},
    "portal": {"pt": "Portal", "en": "Portal"},
}

# Pasta alterada pelo PR -> tipo da faixa; vence a que tiver mais arquivos
PASTAS_TIPO = [
    ("docs/documentos/manuais/", "manual"),
    ("docs/MOP/aerodromos/", "ad"),
    ("docs/MOP/terminais/", "tma"),
    ("docs/MOP/centros/", "fir"),
    ("docs/MOP/oceanico/", "oca"),
    ("docs/fundamentos/", "fundamentos"),
]

# Grupos de commits pelo prefixo convencional (feat, fix, docs...)
GRUPOS = [
    ("feat", {"pt": "Recursos", "en": "Features"}),
    ("docs", {"pt": "Conteúdo", "en": "Content"}),
    ("fix", {"pt": "Correções", "en": "Fixes"}),
    ("outros", {"pt": "Outros ajustes", "en": "Other changes"}),
]

TEXTOS = {
    "pt": {
        "titulo": "Atualização do portal",
        "resumo": lambda n: f"{n} commit" if n == 1 else f"{n} commits",
    },
    "en": {
        "titulo": "Portal update",
        "resumo": lambda n: f"{n} commit" if n == 1 else f"{n} commits",
    },
}

RE_MERGE = re.compile(r"^Merge pull request #(\d+) from \S+?/(\S+)")
RE_CONVENCIONAL = re.compile(r"^(\w+)(?:\(([^)]*)\))?!?:\s*(.+)$")

_cache = {}
_geradas = set()
_entradas = []


def _idioma(config):
    return "en" if str(config.theme["language"]).startswith("en") else "pt"


def _eh_entrada(file):
    return file.src_uri in _geradas


def _git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True
    ).stdout


def _tipo(merge):
    contagem = collections.Counter()
    for caminho in _git("diff", "--name-only", f"{merge}^1", merge).splitlines():
        for pasta, tipo in PASTAS_TIPO:
            if caminho.startswith(pasta):
                contagem[tipo] += 1
    return contagem.most_common(1)[0][0] if contagem else "portal"


def _deploys():
    """Merges de PR no histórico de primeiro pai do HEAD, com os commits de cada um."""
    try:
        head = _git("rev-parse", "HEAD").strip()
    except (OSError, subprocess.CalledProcessError) as erro:
        log.warning("sem histórico do git, Novidades fica vazia: %s", erro)
        return []
    if head in _cache:
        return _cache[head]

    deploys = []
    saida = _git("log", "--first-parent", "--merges", "--format=%H%x1f%cI%x1f%B%x1e", "HEAD")
    for registro in saida.split("\x1e"):
        if not registro.strip():
            continue
        sha, quando, corpo = registro.strip().split("\x1f", 2)
        linhas = corpo.strip().splitlines()
        m = RE_MERGE.match(linhas[0]) if linhas else None
        if not m:
            continue
        numero, ramo = m.groups()
        titulo = " ".join(l.strip() for l in linhas[1:] if l.strip())
        # Títulos no formato "docs(sbxp): ..." perdem o prefixo convencional
        m = RE_CONVENCIONAL.match(titulo)
        if m:
            titulo = m.group(3)[:1].upper() + m.group(3)[1:]
        # PRs antigos repetem o nome do ramo ("Develop") no lugar do título
        if titulo.lower() in ("", ramo.lower(), ramo.rsplit("/", 1)[-1].lower()):
            titulo = None
        commits = []
        for linha in _git("log", "--no-merges", "--format=%H%x1f%s", f"{sha}^1..{sha}^2").splitlines():
            csha, assunto = linha.split("\x1f", 1)
            commits.append((csha, assunto))
        deploys.append({
            "numero": int(numero),
            "quando": datetime.datetime.fromisoformat(quando),
            "titulo": titulo,
            "commits": commits,
            "tipo": _tipo(sha),
        })
    _cache[head] = deploys
    return deploys


def _data_longa(data, idioma):
    mes = MESES_EXTENSO[idioma][data.month - 1]
    if idioma == "en":
        return f"{mes} {data.day}, {data.year}"
    return f"{data.day} de {mes.lower()} de {data.year}"


def _markdown(deploy, titulo, idioma, repo):
    grupos = collections.defaultdict(list)
    for sha, assunto in deploy["commits"]:
        m = RE_CONVENCIONAL.match(assunto)
        tipo, escopo, texto = m.groups() if m else ("outros", None, assunto)
        if tipo not in dict(GRUPOS):
            tipo = "outros"
        grupos[tipo].append((sha, escopo, texto))

    partes = [f"# {titulo}\n"]
    for chave, rotulos in GRUPOS:
        if not grupos[chave]:
            continue
        itens = []
        for sha, escopo, texto in grupos[chave]:
            escopo_html = f'<code class="vb-commit__escopo">{html.escape(escopo)}</code> ' if escopo else ""
            itens.append(
                f'<li>{escopo_html}{html.escape(texto)} '
                f'<a class="vb-commit__sha" href="{repo}/commit/{sha}">{sha[:7]}</a></li>'
            )
        partes.append(f"## {rotulos[idioma]}\n\n<ul class=\"vb-commits\">\n" + "\n".join(itens) + "\n</ul>\n")
    return "\n".join(partes)


@event_priority(-110)  # depois do i18n, que descartaria arquivos fora de docs/
def on_files(files, config):
    idioma = _idioma(config)
    prefixo = "en/" if idioma == "en" else ""
    repo = (config.repo_url or "").rstrip("/")
    _geradas.clear()
    entradas = []

    for deploy in _deploys():
        data = deploy["quando"].date()
        slug = f"{data.isoformat()}-pr{deploy['numero']}"
        titulo = deploy["titulo"] or f"{TEXTOS[idioma]['titulo']} #{deploy['numero']}"
        file = File.generated(
            config, f"{PASTA}{slug}.md",
            content=_markdown(deploy, titulo, idioma, repo),
        )
        # O src_uri fica sem o idioma para a página cair na seção Novidades do menu
        file.dest_uri = f"{prefixo}{PASTA}{slug}/index.html"
        # O seletor de idioma do i18n procura esses atributos em toda página
        file.locale_alternate_of = file.src_uri
        file.alternates = {
            "pt": SimpleNamespace(url=f"{PASTA}{slug}/"),
            "en": SimpleNamespace(url=f"en/{PASTA}{slug}/"),
        }
        files.append(file)
        _geradas.add(file.src_uri)
        entradas.append({
            "titulo": titulo,
            "resumo": f"{TEXTOS[idioma]['resumo'](len(deploy['commits']))} · PR #{deploy['numero']}",
            "tipo": deploy["tipo"],
            "rotulo": TIPOS[deploy["tipo"]][idioma],
            "data": data,
            "quando": deploy["quando"],
            "data_curta": f"{data.day:02d} {MESES[idioma][data.month - 1]}",
            "mes": f"{MESES_EXTENSO[idioma][data.month - 1]} {data.year}",
            "data_longa": _data_longa(data, idioma),
            "url": file.url,
            "pr": f"{repo}/pull/{deploy['numero']}",
        })

    entradas.sort(key=lambda e: e["quando"], reverse=True)
    _entradas[:] = entradas
    return files


def on_env(env, config, files):
    env.globals["novidades"] = _entradas
    por_mes = {}
    for e in _entradas:
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
