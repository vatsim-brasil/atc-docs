# Diagramas de solo dos aeródromos

Scripts que geram os SVGs das páginas de aeródromo do MOP (visão geral com pontos de decolagem, áreas de responsabilidade GND/TWR e fluxos de solo). Cada aeródromo tem a sua pasta:

| Pasta | Saída | Taxiways |
| :--- | :--- | :--- |
| `sbgr/` | `docs/MOP/aerodromos/sbcw-curitiba/twr/img/sbgr-*.svg` | GND_DRAW (com `ref`) |
| `sbct/` | `docs/MOP/aerodromos/sbcw-curitiba/twr/img/sbct-*.svg` | GND_DRAW (nomes pelo índice da feição) |
| `sbgl/` | `docs/MOP/aerodromos/sbcw-curitiba/twr/img/sbgl-*.svg` | OSM (`osm.json`) |
| `sbrf/` | `docs/MOP/aerodromos/sbre-recife/twr/img/sbrf-*.svg` | OSM (`osm.json`) |
| `sbsv/` | `docs/MOP/aerodromos/sbre-recife/twr/img/sbsv-*.svg` | OSM (`osm.json`) |
| `sbvt/` | `docs/MOP/aerodromos/sbre-recife/twr/img/sbvt-*.svg` | OSM (`osm.json`) |

## Fontes

- **GND_DRAW** (pátios, prédios e, em alguns aeródromos, taxiways e pontos de espera): pasta `GND_DRAW/<ICAO>` do repositório **privado** `vatsim-brasil/atcops-desenho-solo`. Não é versionada aqui; `baixar.sh` baixa a versão usada (commit fixo) para `.dados/<ICAO>/`, que está no `.gitignore`.
- **OpenStreetMap**: `osm.json` é um extrato do Overpass (ODbL) guardado junto do script. Os mapas de nomes das taxiways (`REF`) usam a posição de cada *way* nesse extrato, então **não troque o `osm.json`** sem refazer o `REF` (o `debug.py` desenha cada *way* com o índice para ajudar).
- **Pistas**: coordenadas das cabeceiras do AIP AD 2.12, em `base.py`.
- **Rotas, rótulos e balões**: posições escolhidas à mão a partir das cartas ADC/PDC, em `gen.py`/`maps.py`.

## Uso

Precisa de Python 3 (só biblioteca padrão) e do `gh` autenticado com acesso ao repositório privado.

```bash
tools/diagramas/baixar.sh            # todos os aeródromos, ou: baixar.sh SBRF SBSV
python3 -I tools/diagramas/sbrf/gen.py docs/MOP/aerodromos/sbre-recife/twr/img
```

O argumento é a pasta de saída. Os SVGs têm fundo próprio (funcionam nos dois temas) e servem às páginas PT e EN; a legenda fica no `.md`.

Para conferir o resultado em PNG, renderize o SVG com o Chromium headless:

```bash
chrome-headless-shell --no-sandbox --hide-scrollbars --window-size=1000,400 --screenshot=out.png file://$PWD/sbrf-fluxo-18.svg
```

`python3 -I <icao>/debug.py dbg.svg` (todas as pastas menos `sbgr`) gera um mapa de depuração com o índice e o `ref` de cada taxiway.

## Novo aeródromo

1. Copie a pasta do aeródromo mais parecido (pista única: `sbrf`; duas pistas: `sbsv` ou `sbvt`).
2. Em `base.py`, troque o ARP e as cabeceiras (AIP AD 2.12) e a rotação da projeção.
3. Baixe o `GND_DRAW/<ICAO>` e, se as taxiways não tiverem `ref`, um extrato do Overpass com `aeroway=taxiway|runway` na área do aeródromo (o Overpass exige cabeçalho `User-Agent`).
4. Use o `debug.py` para preencher o `REF`, depois ajuste rótulos, rotas e balões em `gen.py`/`maps.py`.
