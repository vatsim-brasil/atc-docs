---
title: SBWR - Brasília
tags:
  - Terminal
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Brasília TMA |
| **Position** | `SBWR_APP` |
| **Callsign** | Brasília Control |
| **Frequency** | **119.200** MHz[^pacote] |
| **ATS surveillance** | Radar |
| **Aerodromes in the TMA** | [SBBR](../../aerodromos/sbbs-brasilia/twr/SBBR.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Use the tabs above: **Aeronautical Charts** shows the TMA charts, **Visual Chart** shows the visual chart from AISWEB, **Weather** shows a weather map of the area and **VATSIM Traffic** opens the traffic at the main aerodrome (SBBR).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWR?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Visual Chart"
    [:material-open-in-new: Open in new tab](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Source: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Weather"
    <div class="tma-meteo" data-lat="-15.873" data-lon="-48.004" data-zoom="8" data-lang="en"></div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBBR){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

The **Visual corridors (REA)** layer shows the 5 REAs of AIC N 10/17 and their gates (yellow). One-way segments carry an arrow in the direction of flight; on two-way segments the altitude depends on the direction. Click a segment to see its track and altitude. Details in [Visual corridors (REA)](#visual-corridors-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Brasília TMA | 6500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Brasília CTR | GND – 6500 FT | <span class="classe-badge classe-c">C</span> |
| Brasília ATZ | GND – 5500 FT | — |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWR_APP** | `WR` | Brasília Control | **119.200** |  |
| **SBBR_TWR** | `TBR` | Brasília Tower | **118.100** |  |

## :material-arrow-down-bold-box-outline: Top-down coverage

Read from bottom to top: when a position is offline, the airspace falls to the next online position above.

??? info "Show coverage diagram"
    ```mermaid
    ---
    config:
      flowchart:
        wrappingWidth: 1000
    ---
    flowchart BT
        p0["SBBS_CTR"]:::ctr
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_NE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_NS_CTR</span>"]:::grpctr
        p1["SBBS_N_CTR"]:::ctr
        p2["SBWR_APP"]:::app
        p3["SBBR_TWR"]:::twr
        a0(["Brasília TMA"]):::esp --> p2
        a1(["Brasília CTR<br>Brasília ATZ"]):::esp --> p3
        g0 --> p0
        p1 --> g0
        p2 --> p1
        p3 --> p2
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
        classDef grpctr fill:none,stroke:#8a56c9,stroke-dasharray:4 3
    ```

## :material-airplane: VFR circulation

!!! abstract "Visual navigation documents"
    - **Circular:** [AIC N 10/17 – Special VFR aircraft routes in the Brasília Terminal Area](https://publicacoes.decea.mil.br/publicacao/aic-n-1017){ target="_blank" } (in force since 20 JUL 2017)
    - **Visual chart – Aircraft routes (REA):** [CCV REA WR-Brasília](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf){ target="_blank" } (25 JAN 2024)

    The chart is embedded in the **Visual Chart** tab under **Useful Information**. The data in this section comes from AIC N 10/17[^aic1017]; the chart carries the same points and altitudes.

### TMA layers and who handles VFR

| Airspace | Limits | Class | VFR |
| --- | --- | :---: | --- |
| **Brasília TMA** | 6500 FT – FL195 | <span class="classe-badge classe-c">C</span> up to FL145, <span class="classe-badge classe-a">A</span> above | With APP clearance up to FL145; above, class A, no VFR |
| **Brasília CTR** | GND – 6500 FT | <span class="classe-badge classe-c">C</span> | Only along the REAs, unless the APP clears otherwise |
| **Brasília ATZ** | GND – 5500 FT | — | SBBR circuit, with the Tower; entry only with APP clearance |
| **REA** | 4500 or 5000 FT | <span class="classe-badge classe-g">G</span> | Corridors inside the CTR; the AIC classifies their airspace as class G |

- **Mandatory corridors in the CTR:** all VFR traffic within the Brasília CTR projection flies along the REAs. It may join or leave them at any point stated in the flight plan; any other track only with APP clearance.
- **Contact with the APP:** even with the REAs in class G, the pilot makes first contact with the APP **before entering** the corridors, when possible, and keeps a continuous listening watch. After that, speak only when needed or when called.
- **In the real world**, the AIC tells VFR traffic on the REAs to use **120.650**; the current AIP lists **121.150** as the primary VFR frequency of Brasília APP. Air-to-air coordination on the REAs is on the free frequency **123.450**, or on the aerodrome's coordination frequency (FCA), where there is one.
- **In the package** there is only `SBWR_APP` (**119.200**), which handles all VFR traffic on the REAs. Pilots call the **online** position, not the real-world frequency. Without the APP, the next position in the [coverage](#top-down-coverage) takes over. Air-to-air coordination goes on **UNICOM 122.800**.

### General VFR rules

- **Flight plan:** departures from a controlled aerodrome put `REA` in item 15 and the corridors in item 18 (e.g. `BRAVO, CHARLIE`). On a first flight on the REAs, tell the APP. Traffic from an aerodrome without an ATS unit states the origin, destination and the REAs it will use on first contact.
- **References on the left:** pilots fly with the corridor's visual references on their **left**.
- **Width:** 3 NM along the whole route (1.5 NM either side of the centreline).
- **Altitudes:** **4500 or 5000 ft**, depending on the segment and direction, kept preferably for the whole en-route phase. On two-way segments, the altitude separates the two directions.
- **QNH** for Brasília, from the APP or the SBBR ATIS.
- **Landing and taxi lights** on, day and night. A mode A/C or S **transponder** is mandatory.
- **Holding:** to space out entries into the CTR, the APP may hold traffic over the REA reference points.
- **Helicopters** may also use the REAs.
- **IMC:** if VMC can't be kept, turn back and land at the departure aerodrome or the nearest one, ask for special VFR, or ask the APP for a change to IFR.

Unless the APP assigns another code, VFR traffic within the TMA projection builds its transponder code from the origin (first two digits) and the destination (last two):

| Aerodrome | Departing | Destination |
| :---: | :---: | :---: |
| APUB | **21**xx | xx**21** |
| SSGP | **22**xx | xx**22** |
| SIQE | **23**xx | xx**23** |
| SBBR | **24**xx | xx**24** |
| CBAAER | **25**xx | xx**25** |
| SWUZ | **26**xx | xx**26** |
| SWFR | **27**xx | xx**27** |
| Other aerodromes and heliports under the TMA | **31**xx | xx**31** |
| Aerodromes outside the TMA | **32**xx | xx**32** |

AIC examples: from APUB to SSGP, **2122**; from CBAAER to SWUZ, **2526**.

### Visual corridors (REA)

The 5 REAs of the TMA. Altitudes in feet (QNH). **→** is a one-way segment; **⇄** is two-way, with track and altitude given as **outbound / return**.

| REA | Segment | Track | Altitude |
| :---: | :--- | :---: | :---: |
| **ALFA** | LAGOA BONITA → SOBRADINHO 2 | 271° | 5000 |
|  | SOBRADINHO 2 → BARRAGEM SANTA MARIA | 274° | 5000 |
|  | BARRAGEM SANTA MARIA → ESTRADA | 287° | 5000 |
|  | ESTRADA → PONTA NORTE | 279° | 5000 |
| **BRAVO** | LAGOA 2 ⇄ BARRAGEM SANTA MARIA | 028° / 208° | 5000 / 4500 |
|  | BARRAGEM SANTA MARIA → TORRE 4 | 028° | 5000 |
|  | TORRE 4 → FERCAL | 082° | 5000 |
|  | FERCAL → CIPLAN | 084° | 5000 |
| **CHARLIE** | PONTA SUL → ESTACIONAMENTO | 112° | 5000 |
|  | ESTACIONAMENTO → SÍTIO | 098° | 5000 |
|  | SÍTIO → LAGOA 2 | 107° | 5000 |
| **DELTA** | SARA ⇄ CBAAER | 121° / 301° | 4500 / 5000 |
|  | CBAAER ⇄ GRANJA 1 | 140° / 320° | 4500 / 5000 |
|  | GRANJA 1 ⇄ TORRE 1 | 156° / 336° | 4500 / 5000 |
|  | TORRE 1 ⇄ TORRE 2 | 186° / 006° | 4500 / 5000 |
|  | TORRE 2 ⇄ TORRE 3 | 177° / 357° | 4500 / 5000 |
|  | TORRE 3 ⇄ TORRE TROCO | 195° / 015° | 4500 / 5000 |
|  | TORRE TROCO ⇄ BARRAGEM 1 | 199° / 019° | 4500 / 5000 |
|  | BARRAGEM 1 ⇄ GRANJA 2 | 286° / 106° | 4500 / 5000 |
|  | GRANJA 2 ⇄ ALPHAVILLE | 264° / 084° | 4500 / 5000 |
|  | ALPHAVILLE ⇄ BUNGE | 268° / 088° | 4500 / 5000 |
|  | BUNGE ⇄ TANQUES CAESB | 301° / 121° | 4500 / 5000 |
|  | TANQUES CAESB ⇄ POVOADO SERRA DOURADA | 327° / 147° | 4500 / 5000 |
|  | POVOADO SERRA DOURADA ⇄ TORRE ENGENHO | 299° / 119° | 4500 / 5000 |
| **ECHO** | BUNGE ⇄ ESTUFA VERMELHA | 040° / 220° | 5000 / 4500 |

What each corridor does:

- **ALFA** (one-way, westbound) leaves the LAGOA BONITA gate in the northeast, passes Sobradinho and the Santa Maria dam and ends at the PONTA NORTE gate, at the north tip of Lake Descoberto. Traffic from the northeast bound for SBBR turns down the BRAVO at the Santa Maria dam.
- **BRAVO** links the LAGOA 2 gate, near the Army barracks, to the north. Up to the Santa Maria dam it is two-way (5000 ft northbound, 4500 southbound); from there it runs only north and northeast, via TORRE 4 and FERCAL, to the CIPLAN gate.
- **CHARLIE** (one-way, eastbound) is the entry from the west: from the PONTA SUL gate, at the south tip of Lake Descoberto, via ESTACIONAMENTO and SÍTIO to the LAGOA 2 gate.
- **DELTA** is the long two-way arc around the east and south. It leaves the SARA gate (Sarah Kubitschek Hospital), passes CBAAER and the towers along the DF-130 (TORRE 1 to 3 and TORRE TROCO), goes round SBBR and heads west via BARRAGEM 1, GRANJA 2, ALPHAVILLE and BUNGE to the TORRE ENGENHO gate (Engenho das Lajes village). From SARA towards TORRE ENGENHO at **4500 ft**; the other way at **5000**.
- **ECHO** links BUNGE (the Bunge silos and sheds) to the ESTUFA VERMELHA gate to the north: 5000 ft northbound to ESTUFA VERMELHA and 4500 southbound to BUNGE.

**Gates** (REA entry and exit): LAGOA BONITA, CIPLAN, PONTA NORTE, PONTA SUL, LAGOA 2, SARA, ESTUFA VERMELHA, GRANJA 2, BUNGE and TORRE ENGENHO.

### Aerodromes under the TMA

| Aerodrome | Arrival | Departure |
| :---: | :--- | :--- |
| **SBBR** | Wait for APP clearance to join the circuit. If it doesn't come in time, hold in visual conditions at an REA point; with no contact with the APP, ask the Tower | Along the REAs, as the APP instructs |
| **APUB** | LAGOA 2 or SARA gates, or another point cleared by the APP | To the southwest, west, northwest, north and northeast, via the LAGOA 2 gate; to the east, southeast and south, via the SARA gate |
| **SSGP** | CBAAER or TORRE 2 positions, or another point cleared by the APP; once cleared, approach coordinating with departing traffic | At 4000 ft, calling the APP: heading CBAAER for the northwest, north and northeast; heading TORRE 3 for the other sectors |
| **SIQE** | GRANJA 2 gate, or another point cleared by the APP | To SSGP: track north at 4000 ft and, once cleared by the APP, approach coordinating with departing traffic |

From SSGP to SIQE: take off heading for the town of São Sebastião at 4000 ft and, once released from the frequency by the APP, coordinate with traffic in the SIQE circuit.

### Other rules

- AFIL flight plans are not accepted, nor abbreviated flight plans filed by radiotelephony from the ground.
- Helicopters in the South sector: minimum altitude 4100 FT (600 FT AGL).
- Departures from aerodromes and heliports inside the ATZ projection must call Brasília Tower before take-off.

### Phraseology

Brazilian VFR traffic usually calls in Portuguese. First contact with the APP, before entering the corridor:

```
Controle Brasília, PR-MWN, decolado de CBAAER para Luziânia, 4500 pés, solicita REA DELTA até BUNGE.
```

Arrival at SBBR along the CHARLIE:

```
Controle Brasília, PR-MWN, REA CHARLIE, posição SÍTIO, 5000 pés, proa LAGOA 2, pouso em Brasília.
```

Air-to-air coordination (123.450 in the real world; UNICOM on VATSIM), with registration, position, direction or destination and altitude[^aic1017]:

```
Coordenação, PR-MWN, posição TORRE 2, 4500 pés, proa TORRE 3, REA DELTA.
```

## :material-note-text-outline: Remarks

- The TMA is class A between FL145 and FL195 and class C between 6500 FT and FL145.
- In the real world, a 3 NM minimum separation applies within 40 NM of SBBR.
- ATZs have no class published in the AIP (ENR 2.2).
- Volumes and map follow AIP AMDT AIRAC 2612A1 (26 NOV 2026). The VATSIM sector package may carry slightly different TMA and CTR outlines.

---

Back to the Brasília FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.
[^aic1017]: [AIC N 10/17](https://publicacoes.decea.mil.br/publicacao/aic-n-1017){ target="_blank" }, items 3 to 5 and Annex A.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude]. A TMA é a união dos setores 01 a 08.
-->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>

<style>
    .mapa { height: 550px }
    .rea-rotulo { background: #0f172a; color: #fff; border: 0; font-weight: 700; font-size: 11px; padding: 0 5px; box-shadow: none }
    .rea-rotulo::before { display: none }
    .rea-zoom-baixo .rea-rotulo, .rea-zoom-medio .rea-rotulo-trecho { display: none }
    .rea-seta span { display: block; width: 16px; height: 16px; line-height: 16px; text-align: center; color: #c026d3; font-size: 15px; text-shadow: 0 0 2px #fff, 0 0 2px #fff }
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWR", "nome": "Brasília TMA", "posicao": "SBWR_APP", "freq": "119.200", "lim": "6500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-48.541667, -16.099444], [-48.602222, -15.852778], [-48.936111, -15.723056], [-48.946667, -15.671389], [-48.7775, -15.333333], [-48.674722, -15.243056], [-48.401389, -15.049722], [-48.077222, -14.965], [-47.960556, -14.99], [-47.764722, -15.015278], [-47.446111, -15.162778], [-47.140278, -15.436389], [-47.089722, -15.811944], [-47.060556, -16.032222], [-47.242778, -16.388056], [-47.325, -16.486667], [-47.442222, -16.593611], [-47.542222, -16.659444], [-47.780833, -16.735833], [-47.931389, -16.780833], [-48.084167, -16.775556], [-48.298889, -16.742222], [-48.448333, -16.689722], [-48.476944, -16.664722], [-48.644722, -16.548611], [-48.599444, -16.235556]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "Brasília CTR", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – 6500 FT", "classe": "C", "link": "", "contorno": [[-48.438056, -15.641389], [-47.438056, -15.570833], [-47.395, -16.101111], [-48.396667, -16.173611]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "Brasília ATZ", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – 5500 FT", "classe": "—", "link": "", "contorno": [[-48.021944, -15.837778], [-47.988889, -15.806944], [-47.858333, -15.798056], [-47.823056, -15.826667], [-47.816667, -15.912778], [-47.849722, -15.943611], [-47.980278, -15.952778], [-48.015278, -15.924444]]}
];

const limiteFir = [[-50.105463, -22.08634], [-50.4579, -21.6254], [-51.3619, -20.4271], [-52.0114, -19.7046], [-52.7536, -18.9223], [-54.1235, -17.4059], [-53.1008, -16.7092], [-53.3203, -15.8089], [-53.3927, -15.4768], [-53.6267, -14.5625], [-53.5013, -12.96], [-53.051, -12.1836], [-51.672778, -11.0275], [-51.4728, -10.8474], [-51.0866, -10.5156], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.3153, -10.3287], [-46.891, -12.0218], [-45.6083, -13.3218], [-45.278124, -13.796406], [-44.5772, -14.7847], [-44.3306, -15.2179], [-44.095833, -15.626499], [-42.6788, -16.4093], [-42.3377, -16.6247], [-41.8206, -16.9483], [-42.4482, -18.758], [-42.4406, -19.105], [-42.4795, -19.463], [-42.5269, -20.0033], [-42.7521, -20.4117], [-43.3928, -20.1562], [-43.965, -20.5375], [-44.7076, -21.4759], [-45.7749, -22.7993], [-45.8108, -23.0094], [-45.86, -23.2332], [-46.655, -23.6273], [-47.2173, -23.3154], [-47.573, -23.1164], [-47.726084, -23.065083], [-48.832226, -22.69952], [-49.9178, -22.3302]];

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
        v.lim + ' · Class ' + v.classe 
    );
    poligono.on('mouseover', function () { this.setStyle({ weight: 4 }); });
    poligono.on('mouseout', function () { this.setStyle({ weight: ctr ? 2 : 2.5 }); });
    poligono.addTo(ctr ? grupoCtr : grupoTma);
});

// Corredores visuais (REA) e portões da AIC N 10/17 (Anexo A); rumo e altitude de ida, e de volta nos trechos de mão dupla
const reaTrechos = [{"rota": "ALFA", "de": "LAGOA BONITA", "para": "SOBRADINHO 2", "rumo": "271°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "ALFA", "de": "SOBRADINHO 2", "para": "BARRAGEM SANTA MARIA", "rumo": "274°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "ALFA", "de": "BARRAGEM SANTA MARIA", "para": "ESTRADA", "rumo": "287°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "ALFA", "de": "ESTRADA", "para": "PONTA NORTE", "rumo": "279°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "BRAVO", "de": "LAGOA 2", "para": "BARRAGEM SANTA MARIA", "rumo": "028°", "alt": "5000", "rumoVolta": "208°", "altVolta": "4500"}, {"rota": "BRAVO", "de": "BARRAGEM SANTA MARIA", "para": "TORRE 4", "rumo": "028°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "BRAVO", "de": "TORRE 4", "para": "FERCAL", "rumo": "082°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "BRAVO", "de": "FERCAL", "para": "CIPLAN", "rumo": "084°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "CHARLIE", "de": "PONTA SUL", "para": "ESTACIONAMENTO", "rumo": "112°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "CHARLIE", "de": "ESTACIONAMENTO", "para": "SÍTIO", "rumo": "098°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "CHARLIE", "de": "SÍTIO", "para": "LAGOA 2", "rumo": "107°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "DELTA", "de": "SARA", "para": "CBAAER", "rumo": "121°", "alt": "4500", "rumoVolta": "301°", "altVolta": "5000"}, {"rota": "DELTA", "de": "CBAAER", "para": "GRANJA 1", "rumo": "140°", "alt": "4500", "rumoVolta": "320°", "altVolta": "5000"}, {"rota": "DELTA", "de": "GRANJA 1", "para": "TORRE 1", "rumo": "156°", "alt": "4500", "rumoVolta": "336°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE 1", "para": "TORRE 2", "rumo": "186°", "alt": "4500", "rumoVolta": "006°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE 2", "para": "TORRE 3", "rumo": "177°", "alt": "4500", "rumoVolta": "357°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE 3", "para": "TORRE TROCO", "rumo": "195°", "alt": "4500", "rumoVolta": "015°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE TROCO", "para": "BARRAGEM 1", "rumo": "199°", "alt": "4500", "rumoVolta": "019°", "altVolta": "5000"}, {"rota": "DELTA", "de": "BARRAGEM 1", "para": "GRANJA 2", "rumo": "286°", "alt": "4500", "rumoVolta": "106°", "altVolta": "5000"}, {"rota": "DELTA", "de": "GRANJA 2", "para": "ALPHAVILLE", "rumo": "264°", "alt": "4500", "rumoVolta": "084°", "altVolta": "5000"}, {"rota": "DELTA", "de": "ALPHAVILLE", "para": "BUNGE", "rumo": "268°", "alt": "4500", "rumoVolta": "088°", "altVolta": "5000"}, {"rota": "DELTA", "de": "BUNGE", "para": "TANQUES CAESB", "rumo": "301°", "alt": "4500", "rumoVolta": "121°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TANQUES CAESB", "para": "POVOADO SERRA DOURADA", "rumo": "327°", "alt": "4500", "rumoVolta": "147°", "altVolta": "5000"}, {"rota": "DELTA", "de": "POVOADO SERRA DOURADA", "para": "TORRE ENGENHO", "rumo": "299°", "alt": "4500", "rumoVolta": "119°", "altVolta": "5000"}, {"rota": "ECHO", "de": "BUNGE", "para": "ESTUFA VERMELHA", "rumo": "040°", "alt": "5000", "rumoVolta": "220°", "altVolta": "4500"}];
const reaPontos = {"LAGOA BONITA": [-47.693406, -15.580458], "SOBRADINHO 2": [-47.836944, -15.631667], "BARRAGEM SANTA MARIA": [-47.954167, -15.668056], "ESTRADA": [-48.061667, -15.675556], "PONTA NORTE": [-48.213425, -15.709294], "LAGOA 2": [-47.963856, -15.748425], "TORRE 4": [-47.948231, -15.618897], "FERCAL": [-47.887425, -15.585442], "CIPLAN": [-47.851339, -15.5673], "PONTA SUL": [-48.227225, -15.771683], "ESTACIONAMENTO": [-48.129, -15.773167], "SÍTIO": [-48.046658, -15.753981], "SARA": [-47.827931, -15.7529], "CBAAER": [-47.702267, -15.773408], "GRANJA 1": [-47.659294, -15.795708], "TORRE 1": [-47.63205, -15.822039], "TORRE 2": [-47.621031, -15.860994], "TORRE 3": [-47.608889, -15.886667], "TORRE TROCO": [-47.602839, -15.941381], "BARRAGEM 1": [-47.6, -16.004167], "GRANJA 2": [-47.715, -16.015], "ALPHAVILLE": [-47.798414, -16.057139], "BUNGE": [-47.960278, -16.124056], "TANQUES CAESB": [-48.065278, -16.1075], "POVOADO SERRA DOURADA": [-48.137022, -16.058247], "TORRE ENGENHO": [-48.259061, -16.042394], "ESTUFA VERMELHA": [-47.930833, -16.039444]};
const portoes = ["BUNGE", "CIPLAN", "ESTUFA VERMELHA", "GRANJA 2", "LAGOA 2", "LAGOA BONITA", "PONTA NORTE", "PONTA SUL", "SARA", "TORRE ENGENHO"];
var corRea = '#c026d3';
var grupoRea = L.featureGroup();
reaTrechos.forEach(function (t) {
    var a = paraLatLng(reaPontos[t.de]), b = paraLatLng(reaPontos[t.para]);
    var duplo = !!t.rumoVolta;
    L.polyline([a, b], { color: corRea, weight: 4, opacity: 0.9 })
        .bindPopup('<b>REA ' + t.rota + '</b><br>' + t.de + (duplo ? ' ⇄ ' : ' → ') + t.para +
            '<br>Track: ' + t.rumo + (duplo ? ' / ' + t.rumoVolta : '') +
            '<br>Altitude (ft): ' + t.alt + (duplo ? ' / ' + t.altVolta + ' (outbound / return)' : '<br>One-way'))
        .addTo(grupoRea);
    if (!duplo) {
        // seta no sentido do voo, a um terço do trecho (o meio fica para o rótulo)
        var ang = Math.atan2(-(b[0] - a[0]), (b[1] - a[1]) * Math.cos(a[0] * Math.PI / 180)) * 180 / Math.PI;
        L.marker([a[0] + (b[0] - a[0]) / 3, a[1] + (b[1] - a[1]) / 3], { interactive: false, icon: L.divIcon({ className: 'rea-seta', iconSize: [16, 16],
            html: '<span style="transform:rotate(' + ang.toFixed(0) + 'deg)">➤</span>' }) })
            .addTo(grupoRea);
    }
    // Um rótulo por corredor no trecho do meio; os demais trechos só com zoom maior
    var trechosRea = reaTrechos.filter(function (x) { return x.rota === t.rota; });
    var principal = trechosRea[Math.floor((trechosRea.length - 1) / 2)] === t;
    L.marker([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2], { opacity: 0, interactive: false, icon: L.divIcon({ className: '', iconSize: [0, 0] }) })
        .bindTooltip(t.rota, { permanent: true, direction: 'center', className: principal ? 'rea-rotulo' : 'rea-rotulo rea-rotulo-trecho' })
        .addTo(grupoRea);
});
Object.keys(reaPontos).forEach(function (n) {
    var portao = portoes.indexOf(n) >= 0;
    L.circleMarker(paraLatLng(reaPontos[n]), portao ?
        { radius: 5, color: '#0f172a', weight: 2, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 3.5, color: '#334155', weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Gate ' + n : n).addTo(grupoRea);
});

var mapa = L.map('mapa-tma', {
    minZoom: 3,
    maxZoom: 13,
    layers: [tileMapaClaro, grupoFir, grupoTma, grupoCtr, grupoRea]
});

mapa.fitBounds(grupoTma.getBounds().extend(grupoCtr.getBounds()), { padding: [20, 20] });

L.control.layers({
    "Light": tileMapaClaro,
    "Dark": tileMapaEscuro,
    "Arcgis Satellite": tileMapaSatelite
}, {
    "TMAs": grupoTma,
    "CTRs": grupoCtr,
    "FIR boundary": grupoFir,
    "Visual corridors (REA)": grupoRea
}).addTo(mapa);

// Rótulos dos corredores só com zoom suficiente para não embolar
function detalheRea() {
    elemento.classList.toggle('rea-zoom-baixo', mapa.getZoom() < 8);
    elemento.classList.toggle('rea-zoom-medio', mapa.getZoom() < 10);
}
mapa.on('zoomend', detalheRea);
detalheRea();

// Legenda das classes
var legenda = L.control({ position: 'bottomleft' });
legenda.onAdd = function () {
    var div = L.DomUtil.create('div', 'mapa-legenda');
    div.innerHTML = '<b>Class</b>' + ['A', 'C', 'D'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('') +
        '<div><span class="rea-linha"></span>REA</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Gate</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
