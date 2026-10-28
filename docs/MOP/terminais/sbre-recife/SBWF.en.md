---
title: SBWF - Recife
tags:
  - Terminal
  - SBRE
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Recife TMA |
| **Position** | `SBWF_APP` |
| **Callsign** | Recife Control |
| **Frequency** | **120.400** MHz[^pacote] |
| **ATS surveillance** | Radar |
| **Aerodromes in the TMA** | [SBRF](../../aerodromos/sbre-recife/twr/SBRF.en.md), [SBJP](../../aerodromos/sbre-recife/twr/SBJP.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Use the tabs above: **Aeronautical Charts** shows the TMA charts, **Visual Chart** shows the visual chart from AISWEB, **Weather** shows a weather map of the area and **VATSIM Traffic** opens the traffic at the main aerodrome (SBRF).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWF?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Visual Chart"
    [:material-open-in-new: Open in new tab](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Source: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Weather"
    <div class="tma-meteo" data-lat="-7.990" data-lon="-34.975" data-zoom="8" data-lang="en"></div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBRF){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

The **Visual corridors (REA)** layer shows the 5 REAs of AIC N 06/25 and the gates (yellow). Solid magenta line: class C, with the APP; dashed blue: class G. Click a segment to see the tracks, altitudes and contact. Details in [Visual corridors (REA)](#visual-corridors-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Recife TMA | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Recife CTR | GND – 3500 FT | <span class="classe-badge classe-c">C</span> |
| João Pessoa CTR | GND – 3500 FT | <span class="classe-badge classe-d">D</span> |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWF_APP** | `WF` | Recife Control | **120.400** |  |
| **SBRF_TWR** | `TRF` | Recife Tower | **118.350** |  |
| **SBJP_TWR** | `TJP` | João Pessoa Tower | **118.300** |  |

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
        p0["SBRE_CTR"]:::ctr
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBRE_NS_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBRE_NW_CTR</span>"]:::grpctr
        p1["SBRE_N_CTR"]:::ctr
        p2["SBWF_APP"]:::app
        p3["SBRF_TWR"]:::twr
        p4["SBJP_TWR"]:::twr
        a0(["Recife TMA"]):::esp --> p2
        a1(["Recife CTR"]):::esp --> p3
        a2(["João Pessoa CTR"]):::esp --> p4
        g0 --> p0
        p1 --> g0
        p2 --> p1
        p3 --> p2
        p4 --> p2
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
        classDef grpctr fill:none,stroke:#8a56c9,stroke-dasharray:4 3
    ```

## :material-airplane: VFR circulation

!!! abstract "Visual navigation documents"
    - **Circular:** [AIC N 06/25 – VFR aircraft circulation in the Recife Terminal Area](https://publicacoes.decea.mil.br/publicacao/aic-n-0625){ target="_blank" } (in force since 20 MAR 2025, replaces AIC N 13/21)
    - **Visual chart – Aircraft routes (REA):** [CCV REA WF-Recife](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf){ target="_blank" } (20 MAR 2025)

    The chart is embedded in the **Visual Chart** tab under **Useful Information**. The data in this section comes from AIC N 06/25[^aic0625].

### TMA layers and who handles VFR

| Airspace | Limits | Class | VFR |
| --- | --- | :---: | --- |
| **Recife TMA** | 3500 FT – FL195 | <span class="classe-badge classe-c">C</span> up to FL145, <span class="classe-badge classe-a">A</span> above | With APP clearance; above FL145, class A, no VFR |
| **Recife CTR** | GND – 3500 FT | <span class="classe-badge classe-c">C</span> | Only along the REAs and through the gates, unless the APP clears otherwise |
| **João Pessoa CTR** | GND – 3500 FT | <span class="classe-badge classe-d">D</span> | With Pessoa Tower |
| **TMA projection** | Below the TMA, outside the CTRs | <span class="classe-badge classe-g">G</span> | Free FCA 123.450 |

- **Mandatory REAs:** in the Recife CTR and along the north coast, between Caaporã (PB) and Itapissuma (PE), VFR traffic **must** use the REAs and gates, at the published tracks and altitudes, unless the APP instructs otherwise.
- **Corridor class:** all are **class C**, with the APP, except the start of ALFA, from TABU to CERVEJARIA, in **class G** on the free FCA 123.450.
- **In the real world**, VFR traffic talks to Recife APP on **129.600**, **129.200**, **120.400** or **128.950**.
- **In the package**, VFR traffic calls `SBWF_APP` (**120.400**); for the SBRF circuit, `SBRF_TWR` (**118.350**). Pilots call the **online** position, not the real-world frequency. Without it, the next position in the [coverage](#top-down-coverage) takes over. Air-to-air coordination goes on **UNICOM 122.800**.

### General VFR rules

- A mode A/C or S **transponder**, a **VHF radio** and landing or taxi **lights** on are mandatory in and below the TMA. The transponder exception applies only on the special routes for aircraft without transponder (REAST) in the Recife CTR.
- **Right of the centreline:** aeroplanes and helicopters fly to the **right** of the corridor centreline and keep their own separation; if they can't, they tell the APP.
- **Width:** REAs 3 NM (1.5 NM either side); gates 1 NM (0.5 NM either side).
- **Altitudes:** the maximum must be obeyed (it separates VFR from IFR above); the minimum is the segment's obstacle clearance altitude. Keeping to the maximum is recommended, because of noise.
- **Speed:** maximum **200 kt** in controlled airspace.
- **QNH** from the SBRF ATIS (**127.650**).
- **Helicopters** may use the REAs.
- **Z plan:** departures from aerodromes in the TMA changing from VFR to IFR wait for the APP clearance, keeping to the corridor altitudes.
- On busy dates, the class of any part of the airspace, including the REAs, may change from G to C by NOTAM.

### Visual corridors (REA)

The 5 REAs of the TMA, all two-way. Altitudes in feet (QNH), as **maximum / minimum**; a single altitude is the mandatory maximum. Tracks are given as outbound / return.

| REA | Segment | Tracks | Altitudes | Class · contact |
| :---: | :--- | :---: | :---: | :--- |
| **ALFA** | TABU ⇄ TEJUCUPAPO | 215° / 035° | 1600 / 1000 | G · free FCA 123.450 |
|  | TEJUCUPAPO ⇄ CERVEJARIA | 210° / 030° | 1600 | G · free FCA 123.450 |
|  | CERVEJARIA ⇄ FORTE ORANGE | 146° / 326° | 1600 | C · Recife APP |
|  | FORTE ORANGE ⇄ CASA CAIADA | 200° / 020° | 1600 | C · Recife APP |
|  | CASA CAIADA ⇄ CAIS DE SANTA RITA | 224° / 044° | 1200 | C · Recife APP |
| **BRAVO** | ACADEMIA DA POLÍCIA MILITAR ⇄ MORENO PARK AQUÁTICO | 198° / 018° | 1500 | C · Recife APP |
|  | MORENO PARK AQUÁTICO ⇄ BARRAGEM | 179° / 359° | 1600 | C · Recife APP |
|  | BARRAGEM ⇄ MURO ALTO | 173° / 353° | 1600 | C · Recife APP |
|  | MURO ALTO ⇄ PORTO DE GALINHAS | 217° / 037° | 1600 / 1000 | C · Recife APP |
| **CHARLIE** | ACADEMIA DA POLÍCIA MILITAR ⇄ ARAÇOIABA | 047° / 227° | 1500 / 1400 | C · Recife APP |
|  | ARAÇOIABA ⇄ CERVEJARIA | 100° / 280° | 1500 / 1300 | C · Recife APP |
| **DELTA** | PEDREIRA ⇄ MORENO PARK AQUÁTICO | 109° / 289° | 2100 | C · Recife APP |
|  | MORENO PARK AQUÁTICO ⇄ LAGOA AZUL | 126° / 306° | 1600 | C · Recife APP |
| **ECHO** | BARRAGEM ⇄ LAGOA AZUL | 053° / 233° | 1200 | C · Recife APP |

What each corridor does:

- **ALFA** is the arrival from the north coast: from the TABU gate via TEJUCUPAPO to CERVEJARIA (Itapissuma), in class G, and from there, with the APP, via FORTE ORANGE (Itamaracá) and CASA CAIADA (Olinda) to the CAIS DE SANTA RITA gate, the northern entry to SBRF. The SBR-221, SBR-222, SBR-246 and SBR-278 areas and the SBP-227 prohibited area (Coroa do Avião island) lie nearby.
- **BRAVO** is the north-south axis west of the city: from the ACADEMIA DA POLÍCIA MILITAR via MORENO PARK AQUÁTICO and BARRAGEM (Pirapama) to MURO ALTO and the PORTO DE GALINHAS gate. Watch the SBP-209 (Suape port) and SBP-268 (Abreu e Lima refinery) prohibited areas, GND to 1500 ft.
- **CHARLIE** links the ACADEMIA DA POLÍCIA MILITAR to the ARAÇOIABA gate and CERVEJARIA, where it meets ALFA. It is **unavailable** while the SBR-220 area (Aldeia, GND to FL100) is active.
- **DELTA** comes from the PEDREIRA gate (Itamatamirim) via MORENO PARK AQUÁTICO to LAGOA AZUL, the southern entry to SBRF.
- **ECHO** links BARRAGEM to LAGOA AZUL, at 1200 ft.

### SBRF arrivals, departures and crossings

| Gate | Use |
| :---: | :--- |
| **CAIS DE SANTA RITA** | SBRF entry and exit via ALFA (north) |
| **LAGOA AZUL** | SBRF entry and exit via DELTA and ECHO (south and west) |
| ARAÇOIABA · PEDREIRA · PORTO DE GALINHAS · TABU | Gates at the ends of the REAs |

- Joining the SBRF RWY 18 and 36 circuits, or crossing the aerodrome, is via CAIS DE SANTA RITA (ALFA) or LAGOA AZUL (DELTA and ECHO), with Recife Tower clearance.
- On the ALFA, DELTA and ECHO REAs, crossing the RWY 18/36 departure and approach sector needs an **express** APP clearance, coordinated with the Tower. Without it, the aircraft stays in its own sector, at the CAIS DE SANTA RITA or LAGOA AZUL gates.
- Traffic from the north sector to SBRF, other than the Coroa do Avião (SIFC) training flights, uses ALFA and waits for clearance at the CAIS DE SANTA RITA gate.
- **Crossing the TMA north to south** (or south to north): preferably CHARLIE and BRAVO, with SBR-220 deactivated. ALFA and ECHO are subject to holding at SBRF's busy times.
- From the southwest or west to the north sector: CHARLIE (with SBR-220 deactivated), or DELTA, BRAVO and CHARLIE leaving through the ARAÇOIABA gate. With SBR-220 active, use ALFA, DELTA or ECHO, waiting at the gates for the Tower to clear the field crossing.
- Departures from aerodromes or landing areas inside the Recife CTR call the APP before start-up for instructions.
- **Special VFR** at SBRF may be cleared by the APP; the clearance limit is the TMA boundary.

### Other rules

- AFIL flight plans are not accepted.
- SBJP: aircraft without radio may not operate; contact with Pessoa Tower is mandatory before taxi.

### Phraseology

On contact, the pilot gives registration, route, position or gate, altitude and direction[^aic0625]. Brazilian VFR traffic usually calls in Portuguese:

```
Controle Recife, PP-IUR, corredor ECHO, posição Barragem, 1200 pés, proa de Lagoa Azul.
```

```
Controle Recife, PT-IUR, corredor CHARLIE, portão Araçoiaba, 1500 pés, proa de Cervejaria.
```

In class G, on the free FCA (UNICOM on VATSIM):

```
Coordenação, PT-IUR, corredor ALFA, portão Tabu, 1600 pés, proa de Tejucupapo.
```

## :material-note-text-outline: Remarks

- The TMA is class A between FL145 and FL195 and class C between 3500 FT and FL145.
- Volumes and map follow AIP AMDT AIRAC 2612A1 (26 NOV 2026): the CTRs go up to 3500 FT AMSL.
- There is no João Pessoa TMA: SBJP lies inside the Recife TMA. In the real world, Pessoa Tower also provides approach service inside the João Pessoa CTR.

---

Back to the Recife FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.
[^aic0625]: [AIC N 06/25](https://publicacoes.decea.mil.br/publicacao/aic-n-0625){ target="_blank" }, items 3 and 4 and Annex A.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude]; a CTR João Pessoa é um círculo de 15 NM.
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
    .rea-seta span { display: block; width: 16px; height: 16px; line-height: 16px; text-align: center; color: #0284c7; font-size: 15px; text-shadow: 0 0 2px #fff, 0 0 2px #fff }
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
    .mapa-legenda .rea-linha.g { border-top: 3px dashed #0284c7 }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWF", "nome": "Recife TMA", "posicao": "SBWF_APP", "freq": "120.400", "lim": "3500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-34.240278, -8.348056], [-34.289444, -7.086111], [-34.774722, -6.844722], [-35.43, -6.940278], [-35.5175, -7.502778], [-35.709167, -7.841667], [-35.707778, -8.18], [-35.706111, -8.609444], [-35.588056, -8.685278], [-35.134167, -8.976944], [-34.885833, -9.136111]]},
    {"tipo": "ctr", "id": "SBWF", "nome": "Recife CTR", "posicao": "SBRF_TWR", "freq": "118.350", "lim": "GND – 3500 FT", "classe": "C", "link": "", "contorno": [[-35.245278, -7.811111], [-34.858056, -7.682222], [-34.616667, -8.394722], [-35.014167, -8.528333]]},
    {"tipo": "ctr", "id": "SBWF", "nome": "João Pessoa CTR", "posicao": "SBJP_TWR", "freq": "118.300", "lim": "GND – 3500 FT", "classe": "D", "link": "", "contorno": [[-34.700824, -7.140556], [-34.701783, -7.118767], [-34.704652, -7.097144], [-34.709409, -7.075851], [-34.716019, -7.055051], [-34.72443, -7.034901], [-34.734579, -7.015556], [-34.746389, -6.997162], [-34.75977, -6.979859], [-34.77462, -6.963779], [-34.790825, -6.949045], [-34.808263, -6.935768], [-34.826801, -6.92405], [-34.846298, -6.913979], [-34.866605, -6.905633], [-34.887567, -6.899075], [-34.909027, -6.894354], [-34.930819, -6.891507], [-34.952778, -6.890556], [-34.974737, -6.891507], [-34.996529, -6.894354], [-35.017989, -6.899075], [-35.038951, -6.905633], [-35.059258, -6.913979], [-35.078755, -6.92405], [-35.097293, -6.935768], [-35.114731, -6.949045], [-35.130936, -6.963779], [-35.145786, -6.979859], [-35.159167, -6.997162], [-35.170977, -7.015556], [-35.181126, -7.034901], [-35.189537, -7.055051], [-35.196147, -7.075851], [-35.200904, -7.097144], [-35.203773, -7.118767], [-35.204732, -7.140556], [-35.203773, -7.162345], [-35.200904, -7.183968], [-35.196147, -7.205261], [-35.189537, -7.226061], [-35.181126, -7.246211], [-35.170977, -7.265556], [-35.159167, -7.28395], [-35.145786, -7.301253], [-35.130936, -7.317333], [-35.114731, -7.332067], [-35.097293, -7.345344], [-35.078755, -7.357062], [-35.059258, -7.367133], [-35.038951, -7.375479], [-35.017989, -7.382037], [-34.996529, -7.386758], [-34.974737, -7.389605], [-34.952778, -7.390556], [-34.930819, -7.389605], [-34.909027, -7.386758], [-34.887567, -7.382037], [-34.866605, -7.375479], [-34.846298, -7.367133], [-34.826801, -7.357062], [-34.808263, -7.345344], [-34.790825, -7.332067], [-34.77462, -7.317333], [-34.75977, -7.301253], [-34.746389, -7.28395], [-34.734579, -7.265556], [-34.72443, -7.246211], [-34.716019, -7.226061], [-34.709409, -7.205261], [-34.704652, -7.183968], [-34.701783, -7.162345]]}
];

const limiteFir = [[-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-42.086944, -2.855278], [-42.1475, -3.03], [-42.368056, -3.686111], [-42.523889, -4.176944], [-42.979444, -4.398611], [-43.157778, -4.485278], [-43.182573, -4.510323], [-43.386389, -4.703611], [-44.201389, -6.094444], [-44.796667, -6.304444], [-45.780278, -8.143611], [-46.672222, -8.86], [-47.150833, -9.530556], [-47.315278, -10.328611], [-46.934722, -11.848889], [-46.891111, -12.021944], [-45.62204, -13.306131], [-45.278124, -13.796406], [-45.010227, -14.217837], [-44.580004, -14.779477], [-44.251448, -15.354465], [-44.095833, -15.626499], [-42.819853, -16.378574], [-42.337778, -16.624722], [-41.820556, -16.948333], [-42.448056, -18.758056], [-42.440556, -19.105], [-42.479444, -19.463056], [-42.526944, -20.003333], [-42.752222, -20.411667], [-42.594444, -20.460833], [-42.316668, -20.533343], [-42.000004, -20.61667], [-41.400004, -20.48334], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.674833, -20.807667], [-40.5675, -20.901667], [-40.409614, -20.924606], [-40.348833, -20.933333], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189]];

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

// Corredores visuais (REA) e portões da AIC N 06/25 (Anexo A); pontos da carta CCV REA WF
const reaTrechos = [{"rota": "ALFA", "de": "TABU", "para": "TEJUCUPAPO", "rumo": "215°", "rumoVolta": "035°", "max": "1600", "min": "1000", "classe": "G", "esp": "G · FCA livre 123.450"}, {"rota": "ALFA", "de": "TEJUCUPAPO", "para": "CERVEJARIA", "rumo": "210°", "rumoVolta": "030°", "max": "1600", "min": "1600", "classe": "G", "esp": "G · FCA livre 123.450"}, {"rota": "ALFA", "de": "CERVEJARIA", "para": "FORTE ORANGE", "rumo": "146°", "rumoVolta": "326°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "ALFA", "de": "FORTE ORANGE", "para": "CASA CAIADA", "rumo": "200°", "rumoVolta": "020°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "ALFA", "de": "CASA CAIADA", "para": "CAIS DE SANTA RITA", "rumo": "224°", "rumoVolta": "044°", "max": "1200", "min": "1200", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "ACADEMIA DA POLÍCIA MILITAR", "para": "MORENO PARK AQUÁTICO", "rumo": "198°", "rumoVolta": "018°", "max": "1500", "min": "1500", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "MORENO PARK AQUÁTICO", "para": "BARRAGEM", "rumo": "179°", "rumoVolta": "359°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "BARRAGEM", "para": "MURO ALTO", "rumo": "173°", "rumoVolta": "353°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "MURO ALTO", "para": "PORTO DE GALINHAS", "rumo": "217°", "rumoVolta": "037°", "max": "1600", "min": "1000", "classe": "C", "esp": "C · APP Recife"}, {"rota": "CHARLIE", "de": "ACADEMIA DA POLÍCIA MILITAR", "para": "ARAÇOIABA", "rumo": "047°", "rumoVolta": "227°", "max": "1500", "min": "1400", "classe": "C", "esp": "C · APP Recife"}, {"rota": "CHARLIE", "de": "ARAÇOIABA", "para": "CERVEJARIA", "rumo": "100°", "rumoVolta": "280°", "max": "1500", "min": "1300", "classe": "C", "esp": "C · APP Recife"}, {"rota": "DELTA", "de": "PEDREIRA", "para": "MORENO PARK AQUÁTICO", "rumo": "109°", "rumoVolta": "289°", "max": "2100", "min": "2100", "classe": "C", "esp": "C · APP Recife"}, {"rota": "DELTA", "de": "MORENO PARK AQUÁTICO", "para": "LAGOA AZUL", "rumo": "126°", "rumoVolta": "306°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "ECHO", "de": "BARRAGEM", "para": "LAGOA AZUL", "rumo": "053°", "rumoVolta": "233°", "max": "1200", "min": "1200", "classe": "C", "esp": "C · APP Recife"}];
const reaPontos = {"ARAÇOIABA": [-35.088833, -7.788333], "CAIS DE SANTA RITA": [-34.8695, -8.062], "LAGOA AZUL": [-34.988833, -8.152], "PEDREIRA": [-35.230333, -8.116667], "PORTO DE GALINHAS": [-35.000333, -8.508667], "TABU": [-34.876667, -7.508833], "ACADEMIA DA POLÍCIA MILITAR": [-35.155, -7.925], "BARRAGEM": [-35.072, -8.287], "CASA CAIADA": [-34.836333, -7.984667], "CERVEJARIA": [-34.922833, -7.753833], "FORTE ORANGE": [-34.84, -7.81], "MORENO PARK AQUÁTICO": [-35.143667, -8.112167], "MURO ALTO": [-34.984167, -8.451333], "TEJUCUPAPO": [-34.8995, -7.6005]};
const portoes = {"ARAÇOIABA": "", "PEDREIRA": "", "PORTO DE GALINHAS": "", "TABU": "", "CAIS DE SANTA RITA": "SBRF", "LAGOA AZUL": "SBRF"};
var corD = '#c026d3', corG = '#0284c7';
var grupoRea = L.featureGroup();
reaTrechos.forEach(function (t) {
    var a = paraLatLng(reaPontos[t.de]), b = paraLatLng(reaPontos[t.para]);
    var g = t.classe === 'G', duplo = !!t.rumoVolta;
    L.polyline([a, b], { color: g ? corG : corD, weight: 4, opacity: 0.9, dashArray: g ? '8 6' : null })
        .bindPopup('<b>REA ' + t.rota + '</b><br>' + t.de + (duplo ? ' ⇄ ' : ' → ') + t.para + '<br>Tracks: ' + t.rumo + (duplo ? ' / ' + t.rumoVolta : '') +
            '<br>Max. / min. (ft): ' + t.max + (t.max === t.min ? '' : ' / ' + t.min) + '<br>' + t.esp + (duplo ? '' : '<br>One-way'))
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
    var portao = n in portoes;
    L.circleMarker(paraLatLng(reaPontos[n]), portao ?
        { radius: 5, color: '#0f172a', weight: 2, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 3.5, color: '#334155', weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Gate ' + n + (portoes[n] ? ' (' + portoes[n] + ')' : '') : n).addTo(grupoRea);
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
        '<div><span class="rea-linha"></span>REA class C</div>' +
        '<div><span class="rea-linha g"></span>REA class G</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Gate</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
