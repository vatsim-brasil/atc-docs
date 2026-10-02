---
title: SBXF - Florianópolis
tags:
  - Terminal
  - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Florianópolis |
| **Posição** | `SBXF_APP` |
| **Indicativo** | Controle Florianópolis |
| **Frequência** | **119.650** MHz[^pacote] |
| **Vigilância ATS** | Radar |
| **Aeródromos na TMA** | `SBFL`, `SBNF`, `SBJV` |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Use as abas acima: **Cartas Aeronáuticas** traz as cartas da TMA, **Carta Visual** traz a carta visual da AISWEB, **Meteorologia** mostra o mapa meteorológico da área e **Tráfego VATSIM** abre o tráfego no aeródromo principal (SBFL).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBXF?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Carta Visual"
    [:material-open-in-new: Abrir em nova aba](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf" loading="lazy" title="PDF"></iframe></div>

    Fonte: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Meteorologia"
    <div class="tma-meteo" data-lat="-27.154" data-lon="-48.619" data-zoom="8" data-lang="pt"></div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBFL){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| Florianópolis 2 | 1500 FT – 5500 FT | <span class="classe-badge classe-d">D</span> |
| Florianópolis 3 (Navegantes) | 1500 FT – 5500 FT | <span class="classe-badge classe-c">C</span> |
| Florianópolis 1 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Florianópolis | GND – 1500 FT | <span class="classe-badge classe-d">D</span> |
| CTR Navegantes | GND – 1500 FT | <span class="classe-badge classe-c">C</span> |
| ATZ Navegantes | GND – 1500 FT | — |

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBXF_APP** | `XF` | Controle Florianópolis | **119.650** |  |
| **SBFL_TWR** | `TFL` | Torre Florianópolis | **118.700** |  |
| **SBNF_TWR** | `TNF` | Torre Navegantes | **118.200** |  |

## :material-arrow-down-bold-box-outline: Cobertura top-down

Leia de baixo para cima: com a posição desconectada, o espaço aéreo passa para a próxima posição on-line acima.

??? info "Ver diagrama de cobertura"
    ```mermaid
    ---
    config:
      flowchart:
        wrappingWidth: 1000
    ---
    flowchart BT
        p0["SBCW_CTR"]:::ctr
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBCW_CSE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBCW_CSW_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBCW_CWE_CTR</span>"]:::grpctr
        g1["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBCW_CE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBCW_CS_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBCW_CW_CTR</span>"]:::grpctr
        p1["SBCW_C_CTR"]:::ctr
        p2["SBXF_APP"]:::app
        p3["SBFL_TWR"]:::twr
        p4["SBNF_TWR"]:::twr
        a0(["TMA Florianópolis"]):::esp --> p2
        a1(["CTR Florianópolis"]):::esp --> p3
        a2(["CTR Navegantes<br>ATZ Navegantes"]):::esp --> p4
        g0 --> p0
        g1 --> g0
        p1 --> g1
        p2 --> p1
        p3 --> p2
        p4 --> p2
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
        classDef grpctr fill:none,stroke:#8a56c9,stroke-dasharray:4 3
    ```

## :material-airplane: Circulação VFR

!!! abstract "Documentos de navegação visual"
    - **Circular:** [AIC N 22/24 – Circulação Visual na Terminal Florianópolis](https://publicacoes.decea.mil.br/publicacao/aic-n-2224){ target="_blank" } (em vigor desde 03 OUT 2024)
    - **Carta visual – Rotas de aeronaves (REA):** [CCV REA XF-Florianópolis](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf){ target="_blank" }

    A carta está embutida na aba **Carta Visual** em **Informações Úteis**.

- Não são aceitos planos AFIL.
- SBNF: circuito só a noroeste, a 1100 FT para aviões categorias A e B (categoria C proibida) e a 600 FT para helicópteros. Entradas pelos portões Containers e Foz; sobrevoo no mínimo a 2400 FT.

## :material-note-text-outline: Observações

- Florianópolis 1 é classe A entre FL145 e FL195 e classe C entre 5500 FT e FL145.
- SBJV (Joinville) fica nas FIZs Joinville 1 e 2 (classe G), atendidas pela Rádio Joinville.

---

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
    {"tipo": "tma", "id": "SBXF", "nome": "Florianópolis 1", "posicao": "SBXF_APP", "freq": "119.650", "lim": "5500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-49.2271, -26.8953], [-49.041389, -26.783333], [-48.6653, -26.5549], [-48.5681, -26.4956], [-48.511944, -26.261111], [-48.157222, -26.01], [-47.917602, -26.345541], [-47.837661, -26.517101], [-47.722474, -26.7643], [-47.704787, -26.802181], [-47.488761, -27.360389], [-47.819684, -27.731567], [-47.87258, -27.790643], [-48.326667, -28.297778], [-48.685426, -28.106767], [-48.834886, -28.266467], [-49.351081, -28.086168], [-49.513281, -27.981674], [-49.748611, -27.771944], [-49.668611, -27.374167], [-49.2271, -26.8953]]},
    {"tipo": "tma", "id": "SBXF", "nome": "Florianópolis 2", "posicao": "SBXF_APP", "freq": "119.650", "lim": "1500 FT – 5500 FT", "classe": "D", "link": "", "contorno": [[-48.3058, -28.032], [-49.0093, -27.6516], [-49.0046, -27.6082], [-48.997, -27.5738], [-48.9864, -27.5402], [-48.9686, -27.4994], [-48.9251, -27.431], [-48.8949, -27.3965], [-48.8609, -27.365], [-48.8156, -27.3317], [-48.7764, -27.3089], [-48.0716, -27.6876], [-48.0775, -27.7389], [-48.0908, -27.79], [-48.1112, -27.8393], [-48.1384, -27.8859], [-48.1719, -27.929], [-48.2113, -27.9681], [-48.256, -28.0025], [-48.3058, -28.032]]},
    {"tipo": "tma", "id": "SBXF", "nome": "Florianópolis 3 (Navegantes)", "posicao": "SBXF_APP", "freq": "119.650", "lim": "1500 FT – 5500 FT", "classe": "C", "link": "", "contorno": [[-48.2937, -26.8839], [-48.7108, -27.1384], [-48.7697, -27.1255], [-48.824, -27.1032], [-48.8727, -27.0722], [-48.9098, -27.0381], [-48.94, -26.999], [-48.9647, -26.9504], [-48.9788, -26.8984], [-48.9818, -26.845], [-48.9735, -26.7921], [-48.5565, -26.5375], [-48.5, -26.5577], [-48.4467, -26.5866], [-48.3995, -26.6231], [-48.3597, -26.6661], [-48.3252, -26.7208], [-48.3045, -26.7736], [-48.294, -26.8288], [-48.2937, -26.8839]]},
    {"tipo": "ctr", "id": "SBXF", "nome": "CTR Florianópolis", "posicao": "SBFL_TWR", "freq": "118.700", "lim": "GND – 1500 FT", "classe": "D", "link": "", "contorno": [[-48.382222, -27.6725], [-48.645833, -27.533611], [-48.725556, -27.643333], [-48.450833, -27.793889], [-48.374167, -27.677222], [-48.382222, -27.6725]]},
    {"tipo": "ctr", "id": "SBXF", "nome": "CTR Navegantes", "posicao": "SBNF_TWR", "freq": "118.200", "lim": "GND – 1500 FT", "classe": "C", "link": "", "contorno": [[-48.564722, -26.745], [-48.480556, -26.855278], [-48.741389, -27.013056], [-48.826111, -26.903889], [-48.564722, -26.745]]},
    {"tipo": "ctr", "id": "SBXF", "nome": "ATZ Navegantes", "posicao": "SBNF_TWR", "freq": "118.200", "lim": "GND – 1500 FT", "classe": "—", "link": "", "contorno": [[-48.71, -26.875], [-48.682222, -26.911389], [-48.635, -26.91], [-48.590833, -26.883333], [-48.633056, -26.828056], [-48.71, -26.875]]}
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
const setores = [];
const paletaSetores = ['#60a5fa', '#f472b6', '#a3e635', '#fb923c', '#a78bfa', '#2dd4bf', '#fbbf24', '#f87171', '#34d399', '#e879f9', '#38bdf8', '#fda4af', '#818cf8'];
var grupoSetores = L.featureGroup();
setores.forEach(function (s, k) {
    var cor = paletaSetores[k % paletaSetores.length];
    L.polygon(s.contorno.map(paraLatLng), { color: cor, fillColor: cor, weight: 2, fillOpacity: 0.2 })
        .bindPopup('<b>' + s.posicao + '</b><br>' + s.freq + ' MHz<br>' + s.lim)
        .addTo(grupoSetores);
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
    "Limite da FIR": grupoFir
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
