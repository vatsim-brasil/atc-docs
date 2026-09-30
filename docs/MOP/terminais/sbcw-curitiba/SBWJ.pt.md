---
title: SBWJ - Rio de Janeiro
tags:
  - Terminal
  - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Rio de Janeiro |
| **Posição** | `SBWJ_APP` |
| **Indicativo** | Controle Rio |
| **Frequência** | **119.000** MHz[^pacote] |
| **Frequências no mundo real** | 119.000 / 119.350 / 120.550 / 120.750 / 124.950 / 125.950 / 133.700; VFR 133.300 / 126.200 MHz |
| **Horário no mundo real** | H24 |
| **Vigilância ATS** | Radar (consta na AIP ENR 1.6) |
| **Aeródromos na TMA** | [SBGL](../../aerodromos/sbcw-curitiba/twr/SBGL.pt.md), [SBRJ](../../aerodromos/sbcw-curitiba/twr/SBRJ.pt.md), `SBJR`, `SBSC`, `SBAF`, `SBMI` |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo principal da TMA (SBGL).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBGL?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Meteorologia"
    <div id="metar-taf-container" data-airport="SBGL" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Carregando o METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Carregando o TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBGL){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| Rio 3 | 1000 FT – 3500 FT | <span class="classe-badge classe-c">C</span> |
| Rio 2 | 3500 FT – 6500 FT | <span class="classe-badge classe-c">C</span> |
| Rio 1 | 6500 FT – FL245 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Galeão | GND – 2000 FT | <span class="classe-badge classe-d">D</span> |
| CTR Rio (SBRJ) | GND – 2000 FT | <span class="classe-badge classe-d">D</span> |
| CTR Santa Cruz | GND – 2500 FT | <span class="classe-badge classe-c">C</span> |
| CTR Afonsos | GND – 1500 FT | <span class="classe-badge classe-d">D</span> |
| ATZ Jacarepaguá | GND – 2000 FT | — |

## :material-view-grid-outline: Setorização do APP

O APP é dividido em setores, cada um com posição e frequência próprias no pacote. Ligue a camada **Setores do APP** no mapa para vê-los. Quando a posição de um setor está desconectada, o setor passa para a posição indicada em *Cobertura*.

| Posição | Frequência | Limites | Cobertura |
| --- | --- | --- | --- |
| `SBWJ_S_APP` | **126.200** | 6500 FT – FL245 | `SBWJ_APP` |
| `SBWJ_RJ_APP` | **120.750** | 1500 FT – FL120 | `SBWJ_N_APP` / `SBWJ_S_APP` |
| `SBWJ_N_APP` | **125.950** | 6500 FT – FL245 | `SBWJ_NE_APP` |
| `SBWJ_E_APP` | **133.300** | 6500 FT – FL245 | `SBWJ_NE_APP` |
| `SBWJ_GL_APP` | **128.900** | 1500 FT – FL120 | `SBWJ_N_APP` |

### Posições combinadas

| Posição | Frequência | Assume |
| --- | --- | --- |
| `SBWJ_APP` | **119.000** | `SBWJ_S_APP`, `SBWJ_NE_APP` |
| `SBWJ_NE_APP` | **120.550** | `SBWJ_N_APP`, `SBWJ_E_APP` |

## :material-handshake-outline: Espaço aéreo delegado e subordinado

### Tubulão (delegado pelo ACC Curitiba)

O Tubulão é o corredor da FIR Curitiba entre as TMAs São Paulo e Rio de Janeiro, por onde passa a ponte aérea. No pacote, o ACC Curitiba (`SBCW_CTR`) delega esse espaço ao APP Rio, dividido em duas metades. Ligue a camada **Tubulão** no mapa para vê-las.

| Setor | Limites | Posição | Cobertura |
| --- | --- | --- | --- |
| Tubulão Norte (CTA T8N) | FL105 – FL245 | `SBWJ_N_APP` | `SBWJ_NE_APP` → `SBWJ_APP` |
| Tubulão Sul (CTA T8S) | FL105 – FL245 | `SBWJ_S_APP` | `SBWJ_APP` |
| Tubulão Norte (UTA T8N) | FL245 – FL600 | `SBWJ_N_APP` | `SBWJ_NE_APP` → `SBWJ_APP` |
| Tubulão Sul (UTA T8S) | FL245 – FL600 | `SBWJ_S_APP` | `SBWJ_APP` |

Acima do FL245, os setores UTA T8N e T8S também cobrem a projeção da TMA Rio de Janeiro. Com todas as posições do APP Rio desconectadas, o Tubulão volta para o ACC Curitiba, a partir de `SBCW_E_CTR`.

### Controle Aldeia (`SBES_APP`)

O APP São Pedro da Aldeia (`SBES_APP`, Controle Aldeia, **119.450**) controla a CTR Aldeia 1 (2000 FT – 6500 FT), dentro da [TMA Macaé](SBWE.pt.md). No pacote, ele é subordinado ao APP Rio, e não ao APP Macaé: desconectado, a CTR Aldeia 1 passa para `SBWJ_E_APP`, depois `SBWJ_NE_APP` e `SBWJ_APP`. A CTR Aldeia 2 (GND – 2000 FT) é da Torre Aldeia (`SBES_TWR`) e, sem ela, sobe para `SBES_APP`.

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBWJ_APP** | `WJ` | Controle Rio | **119.000** |  |
| **SBGL_TWR** | `TGL` | Torre Galeão | **118.200** |  |
| **SBRJ_TWR** | `TRJ` | Torre Rio | **118.700** |  |
| **SBSC_TWR** | `TSC` | Torre Santa Cruz | **118.800** |  |
| **SBAF_R_TWR** | `RAF` | Rádio Afonsos | **118.900** |  |
| **SBJR_TWR** | `TJR` | Torre Jacarepaguá | **118.400** |  |
| **SBES_APP** | `XES` | Controle Aldeia | **119.450** | Subordinado ao APP Rio |

## :material-arrow-down-bold-box-outline: Cobertura top-down

Leia de baixo para cima: com a posição desconectada, o espaço aéreo passa para a próxima posição on-line acima.

??? info "Ver diagrama de cobertura"
    ```mermaid
    flowchart BT
        p0["SBCW_CTR"]:::ctr
        p1["SBCW_CSE_CTR"]:::ctr
        p2["SBCW_CWE_CTR"]:::ctr
        p3["SBCW_SE_CTR"]:::ctr
        p4["SBCW_CE_CTR"]:::ctr
        p5["SBCW_E_CTR"]:::ctr
        p6["SBWJ_APP"]:::app
        p7["SBWJ_NE_APP"]:::app
        p8["SBWJ_N_APP"]:::app
        p9["SBWJ_GL_APP"]:::app
        p10["SBGL_TWR"]:::twr
        p11["SBWJ_S_APP"]:::app
        p12["SBWJ_RJ_APP"]:::app
        p13["SBRJ_TWR"]:::twr
        p14["SBSC_TWR"]:::twr
        p15["SBAF_R_TWR"]:::twr
        p16["SBJR_TWR"]:::twr
        p17["SBWJ_E_APP"]:::app
        p18["SBES_APP"]:::app
        a0(["TMA Rio de Janeiro"]):::esp --> p6
        a1(["CTR Galeão"]):::esp --> p10
        a2(["CTR Rio (SBRJ)"]):::esp --> p13
        a3(["CTR Santa Cruz"]):::esp --> p14
        a4(["CTR Afonsos"]):::esp --> p15
        a5(["ATZ Jacarepaguá"]):::esp --> p16
        a6(["CTR Aldeia 1"]):::esp --> p18
        a7(["Tubulão Norte"]):::esp --> p8
        a8(["Tubulão Sul"]):::esp --> p11
        p1 --> p0
        p2 --> p1
        p3 --> p2
        p4 --> p3
        p5 --> p4
        p6 --> p5
        p7 --> p6
        p8 --> p7
        p9 --> p8
        p10 --> p9
        p11 --> p6
        p12 --> p11
        p13 --> p12
        p14 --> p12
        p15 --> p9
        p16 --> p12
        p17 --> p7
        p18 --> p17
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
    ```

## :material-airplane: Circulação VFR

- Voos vindos de fora do espaço controlado que entram na TMA pelos corredores REA ou REH estão dispensados de plano de voo, mas devem informar antes matrícula, posição, pessoas a bordo, autonomia, origem e destino.
- Rio 2 e Rio 3 usam frequências VFR no mundo real: 133.300 (primária) e 126.200 (secundária).
- SBRJ: com aproximações IFR na RWY 02R, as saídas VFR para a REA FOXTROT seguem Icaraí, a Lagoa de Piratininga e o portão Itaipu.
- Carta de rotas de helicópteros: [CCV REH WJ2-Rio de Janeiro](https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wj2-rio-de-janeiro_reh_20260319.pdf){ target="_blank" }
- Carta de rotas de helicópteros: [CCV REH WJ3-Rio de Janeiro](https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wj3-rio-de-janeiro_reh_20260319.pdf){ target="_blank" }
- Carta de rotas de helicópteros: [REH Bacia de Santos](https://aisweb.decea.mil.br/cartas/visuais/reh/bacia-de-santos_reh_20241128.pdf){ target="_blank" }
- Carta de rotas de ultraleves: [CCV REUL WJ3-Rio de Janeiro](https://aisweb.decea.mil.br/cartas/visuais/reul/ccv-reul-wj3-rio-de-janeiro_reul_20250807.pdf){ target="_blank" }
- Carta de rotas VFR: [CCV REA WJ1-Rio de Janeiro](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wj1-rio-de-janeiro_rea_20260319.pdf){ target="_blank" }

## :material-note-text-outline: Observações

- Rio 1 é classe A entre FL145 e FL245 e classe C entre 6500 FT e FL145.
- O pacote não separa os volumes Rio 1, 2 e 3: o mapa mostra o contorno lateral da TMA, formado pela união dos setores do APP.
- SBSC (Santa Cruz) e SBAF (Afonsos) são bases da Força Aérea: aeronaves civis dependem de autorização do comando da base. SBMI (Maricá) fica numa FIZ classe G.

---

Fontes: pacote de setores SBCW da VATSIM Brasil (limites laterais, posições, frequências, cobertura top-down, delegação do Tubulão e subordinação do Controle Aldeia) e AIP Brasil, AIRAC A 17/2026 (classes, limites verticais, vigilância ATS e regras VFR).

Voltar para a [visão geral das terminais](index.pt.md) da FIR Curitiba.

[^pacote]: Frequência no pacote de setores da VATSIM Brasil.

<!--
Daqui pra baixo, é o mapa. Contornos extraídos do pacote SBCW (setores TMA_* e CTR_*), em [longitude, latitude].
-->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>

<style>
    .mapa { height: 550px }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWJ", "nome": "Rio 1", "posicao": "SBWJ_APP", "freq": "119.000", "lim": "6500 FT – FL245", "classe": "A/C", "link": "", "contorno": [[-44.03667, -23.80861], [-44.67651, -23.03083], [-44.05694, -22.45917], [-44.11417, -22.09611], [-43.69861, -21.95194], [-43.34611, -22.19417], [-42.55611, -22.03333], [-41.9927, -22.6708], [-41.91472, -22.94528], [-42.77944, -23.1775], [-43.13639, -23.56861], [-44.03667, -23.80861]]},
    {"tipo": "ctr", "id": "SBWJ", "nome": "CTR Santa Cruz", "posicao": "SBSC_TWR", "freq": "118.800", "lim": "GND – 2500 FT", "classe": "C", "link": "", "contorno": [[-43.9037, -22.9312], [-43.6492, -22.8008], [-43.5845, -23.0672], [-43.8887, -23.0888], [-43.9037, -22.9312]]},
    {"tipo": "ctr", "id": "SBWJ", "nome": "CTR Galeão", "posicao": "SBGL_TWR", "freq": "118.200", "lim": "GND – 2000 FT", "classe": "D", "link": "", "contorno": [[-43.086111, -22.805833], [-43.111111, -22.72], [-43.253333, -22.755556], [-43.344167, -22.711111], [-43.373611, -22.751389], [-43.3875, -22.815556], [-43.3625, -22.840556], [-43.3425, -22.830556], [-43.311944, -22.853889], [-43.246111, -22.869722], [-43.231944, -22.884167], [-43.086111, -22.805833]]},
    {"tipo": "ctr", "id": "SBWJ", "nome": "CTR Rio (SBRJ)", "posicao": "SBRJ_TWR", "freq": "118.700", "lim": "GND – 2000 FT", "classe": "D", "link": "", "contorno": [[-43.086111, -22.805833], [-43.1025, -22.846389], [-43.064167, -22.906111], [-43.059722, -23.013056], [-43.113056, -23.024167], [-43.158333, -22.996111], [-43.164444, -22.97], [-43.175833, -22.9575], [-43.201389, -22.963611], [-43.209444, -22.910556], [-43.231944, -22.884167], [-43.086111, -22.805833]]},
    {"tipo": "ctr", "id": "SBWJ", "nome": "ATZ Jacarepaguá", "posicao": "SBJR_TWR", "freq": "118.400", "lim": "GND – 2000 FT", "classe": "—", "link": "", "contorno": [[-43.376389, -22.933889], [-43.3625, -22.932222], [-43.346389, -22.935833], [-43.330556, -22.945278], [-43.320278, -22.955], [-43.313889, -22.965556], [-43.310278, -22.98], [-43.310278, -22.993889], [-43.318333, -23.014444], [-43.326111, -23.025833], [-43.340556, -23.036944], [-43.356111, -23.041944], [-43.370556, -23.0425], [-43.383889, -23.041111], [-43.376389, -22.933889]]},
    {"tipo": "ctr", "id": "SBWJ", "nome": "CTR Afonsos", "posicao": "SBAF_R_TWR", "freq": "118.900", "lim": "GND – 1500 FT", "classe": "D", "link": "", "contorno": [[-43.3625, -22.840556], [-43.3425, -22.830556], [-43.311944, -22.853889], [-43.334444, -22.878889], [-43.418056, -22.903056], [-43.434167, -22.876389], [-43.3625, -22.840556]]}
];

const limiteFir = [[-50.3972, -34.0], [-53.0, -34.0], [-53.383333, -33.883333], [-53.387237, -33.74664], [-53.424893, -33.735434], [-53.420159, -33.701367], [-53.526028, -33.685803], [-53.527608, -33.566477], [-53.503906, -33.384895], [-53.521288, -33.196827], [-53.451761, -33.064532], [-53.248621, -32.932626], [-53.2915, -32.923992], [-53.295545, -32.909383], [-53.191989, -32.857585], [-53.150728, -32.787858], [-53.080342, -32.772584], [-53.069825, -32.751998], [-53.174412, -32.656452], [-53.236546, -32.622982], [-53.241076, -32.603326], [-53.277321, -32.618733], [-53.333629, -32.584732], [-53.400143, -32.575655], [-53.454753, -32.485175], [-53.531611, -32.480194], [-53.591277, -32.430389], [-53.635774, -32.378093], [-53.628538, -32.344116], [-53.648421, -32.314522], [-53.638082, -32.290151], [-53.732091, -32.15263], [-53.722771, -32.101204], [-53.738822, -32.083354], [-53.827004, -32.056419], [-53.841584, -32.030089], [-53.861202, -32.030959], [-53.860937, -31.999842], [-53.954598, -31.959268], [-53.970599, -31.917193], [-54.008624, -31.914536], [-54.03694, -31.887974], [-54.099236, -31.902583], [-54.451958, -31.672975], [-54.457653, -31.644499], [-54.430211, -31.630899], [-54.515127, -31.505523], [-54.610544, -31.464337], [-54.733776, -31.437136], [-54.860114, -31.435861], [-54.887039, -31.404836], [-54.952884, -31.386675], [-55.013076, -31.283611], [-55.048673, -31.313361], [-55.09851, -31.323986], [-55.191063, -31.26661], [-55.242194, -31.255454], [-55.286205, -31.164077], [-55.34575, -31.118921], [-55.350599, -31.073114], [-55.375879, -31.033523], [-55.439954, -30.993147], [-55.591405, -30.844926], [-55.638653, -30.85927], [-55.645772, -30.944803], [-55.706473, -30.960963], [-55.858164, -31.073581], [-55.932747, -31.090182], [-56.006065, -31.064242], [-56.017581, -30.943866], [-55.985978, -30.840105], [-56.013789, -30.81624], [-56.012525, -30.799638], [-56.031486, -30.795488], [-56.070674, -30.742569], [-56.123767, -30.734268], [-56.185104, -30.602327], [-56.212443, -30.601647], [-56.232739, -30.573087], [-56.25635, -30.575807], [-56.294045, -30.523446], [-56.322212, -30.528546], [-56.359544, -30.487783], [-56.365369, -30.497878], [-56.389963, -30.48619], [-56.415765, -30.427856], [-56.451389, -30.418336], [-56.459259, -30.388415], [-56.48784, -30.391815], [-56.545417, -30.350334], [-56.541275, -30.314294], [-56.581869, -30.294234], [-56.610451, -30.300354], [-56.606933, -30.269545], [-56.635917, -30.261401], [-56.626144, -30.238784], [-56.661886, -30.22135], [-56.643317, -30.204594], [-56.694896, -30.202187], [-56.707023, -30.180267], [-56.76899, -30.162782], [-56.782764, -30.132932], [-56.838966, -30.092023], [-56.902061, -30.108125], [-57.001475, -30.082448], [-57.048972, -30.099345], [-57.091952, -30.088969], [-57.091952, -30.112834], [-57.113442, -30.108684], [-57.11597, -30.135662], [-57.172855, -30.192731], [-57.165271, -30.234235], [-57.201364, -30.277255], [-57.250076, -30.283783], [-57.268634, -30.265015], [-57.29647, -30.283783], [-57.320329, -30.259574], [-57.350484, -30.277527], [-57.377989, -30.271543], [-57.404499, -30.297111], [-57.475188, -30.26349], [-57.51103, -30.279331], [-57.554295, -30.270976], [-57.566808, -30.203954], [-57.40212, -30.033623], [-57.319688, -29.975245], [-57.317634, -29.874918], [-57.295632, -29.823581], [-57.227868, -29.780458], [-57.110526, -29.76667], [-56.972943, -29.637301], [-56.967956, -29.600338], [-56.809251, -29.448967], [-56.773755, -29.383256], [-56.720951, -29.362134], [-56.6702, -29.294368], [-56.655239, -29.234231], [-56.611237, -29.15884], [-56.529978, -29.099876], [-56.425682, -29.068517], [-56.407356, -28.966986], [-56.311775, -28.909934], [-56.281506, -28.778359], [-56.191446, -28.758704], [-56.015141, -28.591198], [-56.018367, -28.507886], [-55.895159, -28.46975], [-55.890066, -28.365916], [-55.847636, -28.352702], [-55.756695, -28.361503], [-55.726774, -28.36825], [-55.702424, -28.41372], [-55.69245, -28.409026], [-55.676316, -28.306938], [-55.768722, -28.255602], [-55.756402, -28.220106], [-55.694211, -28.201918], [-55.607085, -28.119779], [-55.565135, -28.152047], [-55.490916, -28.072255], [-55.465395, -28.090736], [-55.381789, -28.027958], [-55.374161, -27.973687], [-55.336026, -27.963127], [-55.326051, -27.924403], [-55.224257, -27.892136], [-55.17292, -27.855466], [-55.139185, -27.887148], [-55.110729, -27.852533], [-55.019441, -27.849691], [-55.082804, -27.782513], [-55.054497, -27.770565], [-55.003655, -27.791808], [-54.912127, -27.737244], [-54.904207, -27.629583], [-54.847365, -27.610051], [-54.806227, -27.530136], [-54.787093, -27.566102], [-54.68023, -27.55202], [-54.673925, -27.506961], [-54.633148, -27.531602], [-54.586211, -27.448584], [-54.547737, -27.489662], [-54.450974, -27.469118], [-54.465935, -27.415141], [-54.417533, -27.408101], [-54.357982, -27.457091], [-54.345954, -27.3993], [-54.234186, -27.381406], [-54.190477, -27.261717], [-54.176446, -27.253055], [-54.140348, -27.292916], [-54.010064, -27.197766], [-53.970754, -27.199231], [-53.961366, -27.159042], [-53.69852, -26.88945], [-53.712601, -26.360532], [-53.65041, -26.243777], [-53.730203, -26.113528], [-53.732578, -26.047428], [-53.82701, -25.95277], [-53.8238, -25.817216], [-53.873947, -25.7307], [-53.862072, -25.689946], [-53.886855, -25.635653], [-53.939659, -25.655601], [-53.967234, -25.587837], [-54.027178, -25.557681], [-54.039378, -25.568899], [-54.06756, -25.550581], [-54.080468, -25.598397], [-54.114203, -25.567302], [-54.109804, -25.495723], [-54.156153, -25.53562], [-54.203384, -25.531219], [-54.176102, -25.573756], [-54.241814, -25.596637], [-54.27819, -25.548821], [-54.340381, -25.585783], [-54.377978, -25.57757], [-54.421346, -25.674963], [-54.529008, -25.607492], [-54.531413, -25.570443], [-54.601758, -25.576103], [-54.616944, -25.444722], [-54.524722, -25.316111], [-54.433889, -25.135556], [-54.466667, -25.062222], [-54.461111, -25.032222], [-54.338333, -24.670833], [-54.326111, -24.476667], [-54.256111, -24.358056], [-54.278056, -24.285278], [-54.3275, -24.237778], [-54.3275, -24.123889], [-54.279444, -24.08], [-54.316389, -24.011944], [-54.375556, -23.993056], [-54.422222, -23.916667], [-54.516389, -23.873611], [-54.571389, -23.882222], [-54.564444, -23.854722], [-54.642778, -23.837222], [-54.664722, -23.818333], [-54.710556, -23.864167], [-54.76, -23.861667], [-54.858889, -23.901944], [-54.905278, -23.902222], [-54.923056, -23.959722], [-55.002778, -23.962222], [-55.052222, -23.99], [-55.086389, -23.986944], [-55.109722, -23.964444], [-55.192222, -23.986944], [-55.215556, -24.014444], [-55.32, -23.959444], [-55.336389, -23.993333], [-55.416111, -23.954444], [-55.443611, -23.894167], [-55.435556, -23.770556], [-55.446667, -23.726389], [-55.482222, -23.638611], [-55.537222, -23.618333], [-55.5275, -23.575556], [-55.548056, -23.503333], [-55.542778, -23.449167], [-55.520833, -23.431389], [-55.502778, -23.378333], [-55.556389, -23.315556], [-55.548056, -23.278889], [-55.523333, -23.2625], [-55.54, -23.228333], [-55.520833, -23.198056], [-55.552222, -23.154444], [-55.598889, -23.143056], [-55.622222, -23.091389], [-55.623611, -23.035833], [-55.65, -23.022778], [-55.656944, -22.996389], [-55.688333, -22.9975], [-55.651389, -22.941944], [-55.652778, -22.893889], [-55.6725, -22.866944], [-55.619167, -22.72], [-55.623056, -22.623611], [-55.671111, -22.598333], [-55.744722, -22.524167], [-55.747222, -22.393333], [-55.784444, -22.389444], [-55.861944, -22.278056], [-56.179167, -22.289444], [-56.345278, -22.205], [-56.389444, -22.153056], [-56.404444, -22.080556], [-56.4525, -22.075278], [-56.504722, -22.090556], [-56.559722, -22.183611], [-56.605, -22.224167], [-56.651667, -22.245833], [-56.683333, -22.224167], [-56.710556, -22.248333], [-56.783333, -22.247222], [-56.834722, -22.303056], [-57.005, -22.226667], [-57.105278, -22.239444], [-57.117778, -22.219167], [-57.1575, -22.231944], [-57.200833, -22.215556], [-57.240833, -22.238611], [-57.373889, -22.228333], [-57.406944, -22.200556], [-57.58, -22.168333], [-57.633056, -22.098056], [-57.697778, -22.092778], [-57.811667, -22.141389], [-57.830833, -22.117222], [-57.869444, -22.131111], [-57.9175, -22.120833], [-57.953056, -22.086667], [-57.983333, -22.090556], [-58.015, -22.033333], [-57.971111, -22.007778], [-57.924444, -21.886667], [-57.973889, -21.838333], [-57.928333, -21.810278], [-57.916111, -21.771944], [-57.951667, -21.753056], [-57.945, -21.7325], [-57.895556, -21.699444], [-57.941667, -21.632222], [-57.925833, -21.585833], [-57.958611, -21.565556], [-57.968056, -21.512222], [-57.853333, -21.319722], [-57.893056, -21.305833], [-57.926667, -21.270833], [-57.870278, -21.249722], [-57.853333, -21.197222], [-57.864722, -21.135833], [-57.853333, -21.098889], [-57.870278, -21.035278], [-57.8275, -20.980278], [-57.8275, -20.931389], [-57.862778, -20.943889], [-57.894722, -20.905], [-57.933056, -20.886944], [-57.856111, -20.840833], [-57.874167, -20.808611], [-57.908333, -20.789444], [-57.945556, -20.799722], [-57.968889, -20.783056], [-57.957778, -20.757222], [-57.874167, -20.733056], [-57.940833, -20.662778], [-57.960278, -20.7025], [-57.994444, -20.685833], [-57.975278, -20.643333], [-58.020556, -20.604722], [-58.005556, -20.561111], [-58.019444, -20.481667], [-58.003056, -20.443056], [-58.084167, -20.378889], [-58.100556, -20.311944], [-58.085556, -20.275833], [-58.108889, -20.255278], [-58.168611, -20.258611], [-58.138333, -20.1925], [-58.175556, -20.173056], [-57.918611, -20.014722], [-57.879167, -19.966944], [-58.001389, -19.8875], [-58.133056, -19.7725], [-58.141111, -19.749722], [-57.789167, -19.033333], [-57.714722, -19.044722], [-57.705278, -19.000556], [-57.724444, -18.908611], [-57.777778, -18.908889], [-57.698056, -18.645], [-57.559444, -18.247222], [-57.464722, -18.234167], [-57.578056, -18.137222], [-57.609444, -18.035278], [-57.714167, -17.832222], [-56.980278, -17.788056], [-54.691, -17.571333], [-54.1235, -17.4059], [-52.7536, -18.9223], [-52.0114, -19.7046], [-51.3619, -20.4271], [-49.9178, -22.3302], [-47.573, -23.1164], [-46.655, -23.6273], [-45.86, -23.2332], [-45.7749, -22.7993], [-43.965, -20.5375], [-43.3928, -20.1562], [-42.7521, -20.4117], [-42.319444, -20.549722], [-42.000004, -20.61667], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.5675, -20.901667], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-38.1472, -22.4338], [-39.5692, -23.5814], [-40.9592, -24.6653], [-43.75, -26.75], [-45.396, -28.7836], [-46.8336, -30.4004]];

const elemento = document.getElementById('mapa-tma');
if (!elemento || elemento._leaflet_id) return;

function paraLatLng(c) {
    return [c[1], c[0]];
}

var tileMapaClaro = camadaMapbox('claro', { minZoom: 3, maxZoom: 13 });
var tileMapaEscuro = camadaMapbox('escuro', { minZoom: 3, maxZoom: 13 });
var tileMapaSatelite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    minZoom: 3,
    maxZoom: 13,
    attribution: '&copy; Esri'
});

var grupoFir = L.layerGroup([
    L.polygon(limiteFir.map(paraLatLng), { color: '#94a3b8', weight: 2, dashArray: '6 6', fill: false, interactive: false })
]);
var grupoTma = L.featureGroup();
var grupoCtr = L.featureGroup();

// Setores do APP (só nas TMAs setorizadas), agrupados por posição
const setores = [{"posicao": "SBWJ_S_APP", "freq": "126.200", "lim": "6500 FT – FL245", "contorno": [[-44.03667, -23.80861], [-44.48423, -23.26482], [-44.02642, -23.05023], [-43.57917, -22.83293], [-43.5542, -22.9169], [-43.1436, -22.8167], [-42.9275, -22.9244], [-42.8308, -22.9686], [-42.9633, -23.1164], [-42.77944, -23.1775], [-43.13639, -23.56861], [-44.03667, -23.80861]]}, {"posicao": "SBWJ_RJ_APP", "freq": "120.750", "lim": "1500 FT – FL120", "contorno": [[-43.5542, -22.9169], [-43.1436, -22.8167], [-42.9275, -22.9244], [-42.8308, -22.9686], [-42.9633, -23.1164], [-43.1644, -22.98], [-43.51278, -23.0575], [-43.4578, -23.2442], [-44.1314, -23.3969], [-43.9683, -22.8575], [-43.8558, -22.6903], [-43.65833, -22.56417], [-43.5542, -22.9169]]}, {"posicao": "SBWJ_N_APP", "freq": "125.950", "lim": "6500 FT – FL245", "contorno": [[-44.02642, -23.05023], [-44.48423, -23.26482], [-44.67651, -23.03083], [-44.05694, -22.45917], [-44.11417, -22.09611], [-43.69861, -21.95194], [-43.3253, -22.5472], [-43.03, -22.5306], [-42.9272, -22.7692], [-42.9275, -22.9244], [-43.1436, -22.8167], [-43.5542, -22.9169], [-43.57917, -22.83293], [-44.02642, -23.05023]]}, {"posicao": "SBWJ_E_APP", "freq": "133.300", "lim": "6500 FT – FL245", "contorno": [[-43.34611, -22.19417], [-42.55611, -22.03333], [-41.9927, -22.6708], [-41.91472, -22.94528], [-42.77944, -23.1775], [-42.9633, -23.1164], [-42.8308, -22.9686], [-42.9275, -22.9244], [-42.9272, -22.7692], [-43.03, -22.5306], [-43.3253, -22.5472], [-43.69861, -21.95194], [-43.34611, -22.19417]]}, {"posicao": "SBWJ_GL_APP", "freq": "128.900", "lim": "1500 FT – FL120", "contorno": [[-43.65833, -22.56417], [-43.3253, -22.5472], [-43.03, -22.5306], [-42.9272, -22.7692], [-42.9275, -22.9244], [-43.1436, -22.8167], [-43.5542, -22.9169], [-43.65833, -22.56417]]}];
const paletaSetores = ['#60a5fa', '#f472b6', '#a3e635', '#fb923c', '#a78bfa', '#2dd4bf', '#fbbf24', '#f87171', '#34d399', '#e879f9', '#38bdf8', '#fda4af', '#818cf8'];
var grupoSetores = L.featureGroup();
setores.forEach(function (s, k) {
    var cor = paletaSetores[k % paletaSetores.length];
    L.polygon(s.contorno.map(paraLatLng), { color: cor, fillColor: cor, weight: 2, fillOpacity: 0.2 })
        .bindPopup('<b>' + s.posicao + '</b><br>' + s.freq + ' MHz<br>' + s.lim)
        .addTo(grupoSetores);
});

// Tubulão: CTA e UTA T8 do pacote SBCW, delegados pelo ACC Curitiba ao APP Rio
const tubulao = [{"nome": "Tubulão Norte (CTA T8N)", "posicao": "SBWJ_N_APP", "freq": "125.950", "lim": "FL105 – FL245", "contorno": [[-45.605556, -23.038611], [-44.409444, -22.784444], [-44.676514, -23.030825], [-44.484227, -23.264821], [-45.4925, -23.48], [-45.539722, -23.309167], [-45.554722, -23.248056], [-45.605556, -23.038611]]}, {"nome": "Tubulão Sul (CTA T8S)", "posicao": "SBWJ_S_APP", "freq": "126.200", "lim": "FL105 – FL245", "contorno": [[-44.896944, -23.805556], [-44.178889, -23.636389], [-44.484227, -23.264821], [-45.4925, -23.48], [-45.428333, -23.712222], [-45.373333, -23.910556], [-44.896944, -23.805556]]}, {"nome": "Tubulão Norte (UTA T8N)", "posicao": "SBWJ_N_APP", "freq": "125.950", "lim": "FL245 – FL600", "contorno": [[-45.605556, -23.038611], [-44.409444, -22.784444], [-44.056944, -22.459167], [-43.730278, -22.451389], [-43.658333, -22.564167], [-43.512778, -23.0575], [-45.4925, -23.48], [-45.605556, -23.038611]]}, {"nome": "Tubulão Sul (UTA T8S)", "posicao": "SBWJ_S_APP", "freq": "126.200", "lim": "FL245 – FL600", "contorno": [[-43.512778, -23.0575], [-45.4925, -23.48], [-45.373333, -23.910556], [-44.896944, -23.805556], [-44.178889, -23.636389], [-43.645278, -23.510833], [-43.416944, -23.381944], [-43.512778, -23.0575]]}];
var grupoTubulao = L.featureGroup();
tubulao.forEach(function (s) {
    var cor = s.nome.indexOf('UTA') >= 0 ? '#a78bfa' : '#e879f9';
    L.polygon(s.contorno.map(paraLatLng), { color: cor, fillColor: cor, weight: 2, dashArray: '8 4', fillOpacity: 0.15 })
        .bindPopup('<b>' + s.nome + '</b><br><code>' + s.posicao + '</code> · ' + s.freq + ' MHz<br>' + s.lim)
        .addTo(grupoTubulao);
});

volumes.forEach(function (v) {
    // A cor segue a classe do volume inferior (ex.: A/C é desenhado como C)
    var cor = cores[v.classe.split('/').pop()];
    var ctr = v.tipo === 'ctr';
    var poligono = L.polygon(v.contorno.map(paraLatLng), {
        color: cor,
        fillColor: cor,
        weight: ctr ? 2 : 2.5,
        dashArray: ctr ? '4 4' : null,
        fillOpacity: ctr ? 0.3 : 0.12
    });
    poligono.bindPopup(
        '<b>' + v.nome + '</b><br>' +
        '<code>' + v.posicao + '</code> · ' + v.freq + ' MHz<br>' +
        v.lim + ' · Classe ' + v.classe 
    );
    poligono.on('mouseover', function () { this.setStyle({ weight: 4 }); });
    poligono.on('mouseout', function () { this.setStyle({ weight: ctr ? 2 : 2.5 }); });
    poligono.addTo(ctr ? grupoCtr : grupoTma);
});

var mapa = L.map('mapa-tma', {
    minZoom: 3,
    maxZoom: 13,
    layers: [tileMapaClaro, grupoFir, grupoTma, grupoCtr]
});

mapa.fitBounds(grupoTma.getBounds().extend(grupoCtr.getBounds()), { padding: [20, 20] });

L.control.layers({
    "Claro": tileMapaClaro,
    "Escuro": tileMapaEscuro,
    "Arcgis Satélite": tileMapaSatelite
}, {
    "TMAs": grupoTma,
    "CTRs": grupoCtr,
    "Limite da FIR": grupoFir,
    "Setores do APP": grupoSetores,
    "Tubulão": grupoTubulao
}).addTo(mapa);

// Legenda das classes
var legenda = L.control({ position: 'bottomleft' });
legenda.onAdd = function () {
    var div = L.DomUtil.create('div', 'mapa-legenda');
    div.innerHTML = '<b>Classe</b>' + ['A', 'C', 'D'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('');
    return div;
};
legenda.addTo(mapa);

})();
</script>
