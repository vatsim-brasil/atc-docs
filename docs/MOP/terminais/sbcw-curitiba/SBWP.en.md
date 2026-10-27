---
title: SBWP - Porto Alegre
tags:
  - Terminal
  - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Porto Alegre TMA |
| **Position** | `SBWP_APP` |
| **Callsign** | Palegre Control |
| **Frequency** | **129.600** MHz[^pacote] |
| **ATS surveillance** | Radar |
| **Aerodromes in the TMA** | [SBPA](../../aerodromos/sbcw-curitiba/twr/SBPA.en.md), [SBCO](../../aerodromos/sbcw-curitiba/twr/SBCO.en.md), [SBCX](../../aerodromos/sbcw-curitiba/afis/SBCX.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Use the tabs above: **Aeronautical Charts** shows the TMA charts, **Visual Chart** shows the visual chart from AISWEB, **Weather** shows a weather map of the area and **VATSIM Traffic** opens the traffic at the main aerodrome (SBPA).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWP?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Visual Chart"
    [:material-open-in-new: Open in new tab](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wp-porto-alegre_rea_20250320.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wp-porto-alegre_rea_20250320.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Source: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wp-porto-alegre_rea_20250320.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Weather"
    <div class="tma-meteo" data-lat="-29.654" data-lon="-51.094" data-zoom="8" data-lang="en"></div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBPA){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

The **Visual corridors (REA)** layer shows the 12 corridors of the CCV REA WP chart and the gates (yellow). Solid magenta line: class D segment; dashed blue: class G. Click a segment to see the tracks, altitudes and class. Details in [Visual corridors (REA)](#visual-corridors-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Porto Alegre 1 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Porto Alegre 2 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Porto Alegre 1 CTR | GND – 1500 FT | <span class="classe-badge classe-c">C</span> |
| Porto Alegre 2 CTR | 1500 FT – 3500 FT | <span class="classe-badge classe-c">C</span> |
| Caxias do Sul FIZ | GND – 5500 FT | <span class="classe-badge classe-g">G</span> |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWP_APP** | `WP` | Palegre Control | **129.600** |  |
| **SBPA_TWR** | `TPA` | Palegre Tower | **118.100** |  |

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
        p0["SBCW_CTR"]:::ctr
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CSE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CSW_CTR</span>"]:::grpctr
        g1["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CS_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_SE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_SW_CTR</span>"]:::grpctr
        p1["SBCW_S_CTR"]:::ctr
        p2["SBWP_APP"]:::app
        p3["SBPA_TWR"]:::twr
        a0(["Porto Alegre TMA"]):::esp --> p2
        a1(["Porto Alegre 1 CTR<br>Porto Alegre 2 CTR"]):::esp --> p3
        g0 --> p0
        g1 --> g0
        p1 --> g1
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
    - **Circular:** [AIC N 14/25 – VFR circulation in the Porto Alegre Terminal Area](https://publicacoes.decea.mil.br/publicacao/aic-n-1425){ target="_blank" } (in force since 15 MAY 2025, replaces AIC N 02/25)
    - **Visual chart – Aircraft routes (REA):** [CCV REA WP-Porto Alegre](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wp-porto-alegre_rea_20250320.pdf){ target="_blank" } (20 MAR 2025), which is Annex B of the AIC

    The chart is embedded in the **Visual Chart** tab under **Useful Information**. The rules in this section come from AIC N 14/25[^aic1425]; the track, altitudes and class of each corridor come from the chart.

### TMA layers and who handles VFR

| Airspace | Limits | Class | VFR |
| --- | --- | :---: | --- |
| **Porto Alegre 1** | 3500 FT – FL195 | <span class="classe-badge classe-c">C</span> up to FL145, <span class="classe-badge classe-a">A</span> above | Along the REAs or with APP clearance; above FL145, class A, no VFR |
| **Porto Alegre 2** | 5500 FT – FL195 | <span class="classe-badge classe-c">C</span> up to FL145, <span class="classe-badge classe-a">A</span> above | Same, over the Serra |
| **Porto Alegre 1 and 2 CTR** | GND – 3500 FT | <span class="classe-badge classe-c">C</span> | Entry and exit only through the gates, along the REAs |
| **Caxias do Sul FIZ** | GND – 5500 FT | <span class="classe-badge classe-g">G</span> | Caxias Radio AFIS; entry and exit through the FORQUETA and 4 FOLHAS gates |
| **REA** | 1000 to 5500 FT | <span class="classe-badge classe-d">D</span> or <span class="classe-badge classe-g">G</span> | The class is the corridor's own, marked on the chart |

- **Corridor class:** each segment takes the corridor's class, not that of the volume it crosses. The corridors near Porto Alegre and its metropolitan area are **class D**; those in the Serra, around the Caxias FIZ, are **class G** (NORTE, OESTE between VERANÓPOLIS and GARIBALDI, SÃO VENDELINO between FORQUETA and SÃO VENDELINO, and LESTE between 4 FOLHAS and CANELA).
- **In class D**, the APP provides flight information and alerting, and pilots coordinate among themselves; on controlled segments the APP may change the altitude or clear the flight off the REAs.
- **In the real world**, VFR traffic talks to Porto Alegre APP; in the Caxias FIZ, to Caxias Radio (**131.600**). Air-to-air coordination uses the REA coordination frequency (FCA).
- **In the package** there is only `SBWP_APP` (**129.600**), which handles all VFR traffic on the REAs. Pilots call the **online** position, not the real-world frequency. Without the APP, the next position in the [coverage](#top-down-coverage) takes over. Air-to-air coordination goes on **UNICOM 122.800**.

### General VFR rules

- **Using the REAs:** in the TMA and below it, VFR traffic **preferably** flies the REAs, joining or leaving them at any point stated in the flight plan. To operate at SBPA, SBCO, SBCX or in the Caxias FIZ, the REAs are **mandatory**. In contact with the APP, and traffic permitting, the flight may be cleared off them.
- **To cross the TMA**, use the REA segments until leaving it or ask the APP for a direct track.
- **Right of the centreline:** pilots fly to the **right** of the corridor centreline, with the visual references on their left.
- **Width:** 3 NM (1.5 NM either side of the centreline).
- **Altitudes:** each segment has a maximum and a minimum altitude; altitude changes are made over the points, under the pilot's responsibility and in VMC. Preferably use the level table altitude for the track; on controlled segments the APP may assign another.
- **Flight plan:** in item 15, the **coordinates** of the gates and positions (the system does not accept the names); in item 18, the corridor names.
- **Radio contact:** brief, with registration, origin and destination, altitude, corridor and estimate for the next point. Call the ATS unit before entering controlled airspace or the Caxias FIZ. Departures from an aerodrome or heliport inside the CTR, the FIZ or below the REAs call first, to get joining or crossing instructions.
- **QNH** from the SBPA ATIS or the APP; in the Caxias FIZ, from Caxias Radio.
- A mode A/C or S **transponder** is mandatory; landing or taxi lights on are recommended.
- **Holding:** to space out entries into the TMA and CTR, the APP may hold traffic over REA points.
- **Helicopters** may use the REAs. Off them, they may ask the APP to enter the CTR at another altitude and land elsewhere in the CTR or the FIZ, calling the ATS unit.
- **IMC:** turn back and land at the departure aerodrome or the nearest one, ask for special VFR, change to IFR, or ask to leave the REA.

Unless the APP assigns a code, traffic departing from a place without an ATS unit under the TMA, or coming from outside it, squawks the **destination** code on entering the TMA projection:

| Destination | Indicator | Code |
| --- | :---: | :---: |
| Porto Alegre – Salgado Filho | SBPA | **0220** |
| Canoas | SBCO | **0230** |
| Caxias do Sul | SBCX | **0240** |
| Eldorado do Sul | SIXE | **0250** |
| Belém Novo | SSBN | **0260** |
| Novo Hamburgo | SSNH | **0270** |
| Other places | — | **2000** |

For touch-and-go flights at more than one aerodrome, use the code of the first one.

### Visual corridors (REA)

The 12 corridors of the TMA, all two-way. Altitudes in feet (QNH), as **maximum / minimum**. Tracks are given as outbound / return.

| REA | Segment | Tracks | Altitudes | Class |
| :---: | :--- | :---: | :---: | :---: |
| **NORTE** | VERANÓPOLIS ⇄ ANTÔNIO PRADO | 091° / 271° | 5000 / 4000 | G |
|  | ANTÔNIO PRADO ⇄ SÃO MARCOS | 140° / 320° | 5000 / 4000 | G |
|  | SÃO MARCOS ⇄ 4 FOLHAS | 215° / 035° | 4500 / 4000 | G |
| **OESTE** | VERANÓPOLIS ⇄ GARIBALDI | 193° / 013° | 5000 / 4000 | G |
|  | GARIBALDI ⇄ MONTENEGRO | 193° / 013° | 5500 / 4500 | D |
|  | MONTENEGRO ⇄ TABAÍ | 204° / 024° | 3500 / 2500 | D |
|  | TABAÍ ⇄ CHARQUEADAS | 234° / 054° | 2500 / 2000 | D |
| **SÃO VENDELINO** | FORQUETA ⇄ SÃO VENDELINO | 221° / 041° | 4500 / 4000 | G |
|  | SÃO VENDELINO ⇄ MONTENEGRO | 216° / 036° | 5000 / 4000 | D |
| **CENTRAL** | TEUTÔNIA ⇄ MONTENEGRO | 147° / 327° | 4500 / 3500 | D |
|  | MONTENEGRO ⇄ ZEZIL | 077° / 257° | 5000 / 4000 | D |
|  | ZEZIL ⇄ CANELA | 077° / 257° | 5000 / 4000 | D |
| **LESTE** | 4 FOLHAS ⇄ VILA OLIVA | 131° / 311° | 4500 / 4000 | G |
|  | VILA OLIVA ⇄ CANELA | 178° / 358° | 5000 / 4000 | G |
|  | CANELA ⇄ TRÊS COROAS | 167° / 347° | 5000 / 4000 | D |
|  | TRÊS COROAS ⇄ TAQUARA | 210° / 030° | 5000 / 4000 | D |
|  | TAQUARA ⇄ GLORINHA | 200° / 020° | 3000 / 2000 | D |
|  | GLORINHA ⇄ SILOS | 189° / 009° | 3000 / 2000 | D |
| **TAQUARA** | CHAPÉU ⇄ LOMBA GRANDE | 076° / 256° | 2000 (mandatory) | D |
|  | LOMBA GRANDE ⇄ TAQUARA | 078° / 258° | 3000 / 2000 | D |
| **GM** | GM ⇄ GLORINHA | 081° / 261° | 2000 / 1000 | D |
| **FREEWAY** | GLORINHA ⇄ PEDÁGIO FREEWAY | 109° / 289° | 3000 / 2000 | D |
| **POLO** | POLO NORTE ⇄ TABAÍ | 293° / 113° | 2000 / 1500 | D |
| **SUL** | CHARQUEADAS ⇄ ELDORADO | 145° / 325° | 2500 / 2000 | D |
|  | ELDORADO ⇄ GUAÍBA | 137° / 317° | 2000 / 1500 | D |
|  | GUAÍBA ⇄ PEDÁGIO VIAMÃO | 104° / 284° | 2000 / 1500 | D |
|  | PEDÁGIO VIAMÃO ⇄ SILOS | 105° / 285° | 2000 / 1500 | D |
| **BEIRA RIO** | GUAÍBA ⇄ BEIRA RIO | 063° / 243° | 2000 / 1500 | D |
| **TARUMÃ** | TARUMÃ ⇄ PEDÁGIO VIAMÃO | 150° / 330° | 2000 / 1000 | D |

What each corridor does:

- **SUL** goes round Porto Alegre to the south: from CHARQUEADAS via ELDORADO to GUAÍBA, across the Guaíba and on via PEDÁGIO VIAMÃO to SILOS. It is the lowest corridor on the south side, between 1500 and 2500 ft.
- **BEIRA RIO** leaves GUAÍBA and crosses the river to the BEIRA RIO gate (Beira-Rio stadium), the southern entry to SBPA.
- **TARUMÃ** links the TARUMÃ gate (Tarumã racetrack, in Viamão) to the SUL at PEDÁGIO VIAMÃO, from 1000 to 2000 ft.
- **POLO** links the POLO NORTE gate (Triunfo petrochemical complex) to TABAÍ, on the OESTE corridor, between 1500 and 2000 ft.
- **TAQUARA** leaves the CHAPÉU gate (Chapéu hill, in Sapucaia do Sul) at a **mandatory 2000 ft**, passes LOMBA GRANDE and climbs to TAQUARA.
- **GM** links the GM gate (General Motors plant, in Gravataí) to GLORINHA, from 1000 to 2000 ft.
- **FREEWAY** runs east from GLORINHA along the BR-290 to the PEDÁGIO FREEWAY gate, in Santo Antônio da Patrulha.
- **LESTE** is the long eastern axis: from 4 FOLHAS (Caxias do Sul) via VILA OLIVA, CANELA, TRÊS COROAS and TAQUARA, down to GLORINHA and on to SILOS. Class G as far as CANELA; class D from there south.
- **CENTRAL** crosses the TMA west to east: from the TEUTÔNIA gate to MONTENEGRO and then, via ZEZIL, to CANELA.
- **OESTE** comes from VERANÓPOLIS via GARIBALDI and MONTENEGRO, crosses TABAÍ and reaches CHARQUEADAS, where it meets the SUL.
- **SÃO VENDELINO** links the FORQUETA gate (Caxias do Sul) to MONTENEGRO via SÃO VENDELINO.
- **NORTE** closes the Serra ring: from VERANÓPOLIS via ANTÔNIO PRADO and SÃO MARCOS to the 4 FOLHAS gate.

### Aerodrome gates

Entry to and exit from the Porto Alegre CTR and the Caxias FIZ are **through the gates**, unless the APP clears otherwise:

| Aerodrome | Gates |
| :---: | :--- |
| **SBPA** and **SBCO** | BEIRA RIO · TARUMÃ · GM · CHAPÉU · POLO NORTE |
| **SBCX** | FORQUETA · 4 FOLHAS |

The chart also marks TEUTÔNIA and PEDÁGIO FREEWAY as gates, at the western and eastern ends of the TMA.

### Other rules

- Abbreviated flight plans filed by radiotelephony with the TWR are not accepted.
- AFIL flight plans are not accepted from aircraft departing aerodromes without an ATS unit in the CTR or TMA.
- With a full flight plan and a change from VFR to IFR (Z plan), wait for the APP clearance, keeping to the corridor altitudes.
- On busy dates or with temporary restricted areas active, the REAs may be suspended or have their class changed by NOTAM.

### Phraseology

On contact, the pilot gives registration, origin and destination, altitude, corridor and estimate for the next point[^aic1425]. Brazilian VFR traffic usually calls in Portuguese. Arrival at SBPA along the SUL:

```
Controle Palegre, PR-MWN, de Charqueadas para Porto Alegre, 2000 pés, REA SUL, estimando GUAÍBA aos 35.
```

Departure from SBCX towards Porto Alegre, leaving the FIZ:

```
Rádio Caxias, PR-MWN, portão FORQUETA, 4500 pés, REA SÃO VENDELINO para Montenegro, estimando SÃO VENDELINO aos 12.
```

Air-to-air coordination (UNICOM on VATSIM):

```
Tráfego REA LESTE, PR-MWN, CANELA, 4500 pés, proa TRÊS COROAS.
```

## :material-note-text-outline: Remarks

- The TMA is class A between FL145 and FL195 and class C between 3500 FT and FL145.
- Volumes and map follow AIP AMDT AIRAC 2612A1 (26 NOV 2026). The VATSIM sector package only has the Porto Alegre 1 outline, which differs slightly.
- SBCO (Canoas) is an air base; civil aircraft require authorization from the base commander.

---

Back to the Curitiba FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.
[^aic1425]: [AIC N 14/25](https://publicacoes.decea.mil.br/publicacao/aic-n-1425){ target="_blank" }, items 3 to 5 and Annexes A and B.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude]. A Porto Alegre 1 é a união dos setores 01 a 08.
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
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
    .mapa-legenda .rea-linha.g { border-top: 3px dashed #0284c7 }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "G": "#a3a3a3", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWP", "nome": "Porto Alegre 1", "posicao": "SBWP_APP", "freq": "129.600", "lim": "3500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-51.805, -29.659167], [-51.882222, -29.276667], [-51.588889, -29.026944], [-51.598889, -28.916944], [-51.277222, -28.829444], [-50.958056, -28.8], [-50.464167, -29.133333], [-50.219167, -29.475278], [-50.528056, -29.779722], [-50.608056, -29.858056], [-50.624722, -30.174722], [-50.875, -30.425], [-51.191667, -30.491667], [-51.843611, -30.508889], [-51.915556, -30.452778], [-51.968333, -30.382778], [-51.831944, -30.108611]]},
    {"tipo": "tma", "id": "SBWP", "nome": "Porto Alegre 2", "posicao": "SBWP_APP", "freq": "129.600", "lim": "5500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-51.598889, -28.916944], [-51.277222, -28.829444], [-50.958056, -28.8], [-50.822778, -28.900278], [-50.7225, -29.042778], [-50.643889, -29.077222], [-50.464167, -29.133333], [-50.493333, -29.252222], [-50.827222, -29.364722], [-51.097778, -29.413611], [-51.364444, -29.382222], [-51.560833, -29.270833]]},
    {"tipo": "ctr", "id": "SBWP", "nome": "Porto Alegre 2 CTR", "posicao": "SBPA_TWR", "freq": "118.100", "lim": "1500 FT – 3500 FT", "classe": "C", "link": "", "contorno": [[-51.351944, -29.765278], [-50.768056, -29.792778], [-50.713889, -30.126944], [-50.94, -30.135833], [-51.202222, -30.152222], [-51.327222, -30.154722], [-51.492778, -30.153889], [-51.495833, -30.081667], [-51.663333, -29.956944], [-51.524167, -29.7925]]},
    {"tipo": "ctr", "id": "SBWP", "nome": "Porto Alegre 1 CTR", "posicao": "SBPA_TWR", "freq": "118.100", "lim": "GND – 1500 FT", "classe": "C", "link": "", "contorno": [[-51.351944, -29.765278], [-51.054722, -29.779722], [-50.972222, -29.793611], [-50.842778, -29.876944], [-50.810278, -29.918889], [-50.775, -30.103056], [-50.946667, -30.111111], [-51.011667, -30.09], [-51.239444, -30.104167], [-51.319722, -30.102778], [-51.401111, -30.061944], [-51.411944, -29.895556], [-51.383333, -29.816667]]},
    {"tipo": "ctr", "id": "SBWP", "nome": "Caxias do Sul FIZ", "posicao": "SBCX_R_TWR", "freq": "131.600", "lim": "GND – 5500 FT", "classe": "G", "link": "", "contorno": [[-51.598889, -28.916944], [-51.277222, -28.829444], [-51.037778, -28.958889], [-50.866667, -29.201111], [-50.805, -29.345278], [-50.827222, -29.364722], [-51.097778, -29.413611], [-51.364444, -29.382222], [-51.560833, -29.270833]]}
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
        v.lim + ' · Class ' + v.classe 
    );
    poligono.on('mouseover', function () { this.setStyle({ weight: 4 }); });
    poligono.on('mouseout', function () { this.setStyle({ weight: ctr ? 2 : 2.5 }); });
    poligono.addTo(ctr ? grupoCtr : grupoTma);
});

// Corredores visuais (REA) e portões da carta CCV REA WP (20 MAR 2025), Anexo B da AIC N 14/25; trechos retos entre os pontos nomeados
const reaTrechos = [{"rota": "NORTE", "de": "VERANÓPOLIS", "para": "ANTÔNIO PRADO", "max": "5000", "min": "4000", "classe": "G", "rumos": "091° / 271°"}, {"rota": "NORTE", "de": "ANTÔNIO PRADO", "para": "SÃO MARCOS", "max": "5000", "min": "4000", "classe": "G", "rumos": "140° / 320°"}, {"rota": "NORTE", "de": "SÃO MARCOS", "para": "4 FOLHAS", "max": "4500", "min": "4000", "classe": "G", "rumos": "215° / 035°"}, {"rota": "OESTE", "de": "VERANÓPOLIS", "para": "GARIBALDI", "max": "5000", "min": "4000", "classe": "G", "rumos": "193° / 013°"}, {"rota": "OESTE", "de": "GARIBALDI", "para": "MONTENEGRO", "max": "5500", "min": "4500", "classe": "D", "rumos": "193° / 013°"}, {"rota": "OESTE", "de": "MONTENEGRO", "para": "TABAÍ", "max": "3500", "min": "2500", "classe": "D", "rumos": "204° / 024°"}, {"rota": "OESTE", "de": "TABAÍ", "para": "CHARQUEADAS", "max": "2500", "min": "2000", "classe": "D", "rumos": "234° / 054°"}, {"rota": "SÃO VENDELINO", "de": "FORQUETA", "para": "SÃO VENDELINO", "max": "4500", "min": "4000", "classe": "G", "rumos": "221° / 041°"}, {"rota": "SÃO VENDELINO", "de": "SÃO VENDELINO", "para": "MONTENEGRO", "max": "5000", "min": "4000", "classe": "D", "rumos": "216° / 036°"}, {"rota": "CENTRAL", "de": "TEUTÔNIA", "para": "MONTENEGRO", "max": "4500", "min": "3500", "classe": "D", "rumos": "147° / 327°"}, {"rota": "CENTRAL", "de": "MONTENEGRO", "para": "ZEZIL", "max": "5000", "min": "4000", "classe": "D", "rumos": "077° / 257°"}, {"rota": "CENTRAL", "de": "ZEZIL", "para": "CANELA", "max": "5000", "min": "4000", "classe": "D", "rumos": "077° / 257°"}, {"rota": "LESTE", "de": "4 FOLHAS", "para": "VILA OLIVA", "max": "4500", "min": "4000", "classe": "G", "rumos": "131° / 311°"}, {"rota": "LESTE", "de": "VILA OLIVA", "para": "CANELA", "max": "5000", "min": "4000", "classe": "G", "rumos": "178° / 358°"}, {"rota": "LESTE", "de": "CANELA", "para": "TRÊS COROAS", "max": "5000", "min": "4000", "classe": "D", "rumos": "167° / 347°"}, {"rota": "LESTE", "de": "TRÊS COROAS", "para": "TAQUARA", "max": "5000", "min": "4000", "classe": "D", "rumos": "210° / 030°"}, {"rota": "LESTE", "de": "TAQUARA", "para": "GLORINHA", "max": "3000", "min": "2000", "classe": "D", "rumos": "200° / 020°"}, {"rota": "LESTE", "de": "GLORINHA", "para": "SILOS", "max": "3000", "min": "2000", "classe": "D", "rumos": "189° / 009°"}, {"rota": "TAQUARA", "de": "CHAPÉU", "para": "LOMBA GRANDE", "max": "2000", "min": "2000", "classe": "D", "rumos": "076° / 256°"}, {"rota": "TAQUARA", "de": "LOMBA GRANDE", "para": "TAQUARA", "max": "3000", "min": "2000", "classe": "D", "rumos": "078° / 258°"}, {"rota": "GM", "de": "GM", "para": "GLORINHA", "max": "2000", "min": "1000", "classe": "D", "rumos": "081° / 261°"}, {"rota": "FREEWAY", "de": "GLORINHA", "para": "PEDÁGIO FREEWAY", "max": "3000", "min": "2000", "classe": "D", "rumos": "109° / 289°"}, {"rota": "POLO", "de": "POLO NORTE", "para": "TABAÍ", "max": "2000", "min": "1500", "classe": "D", "rumos": "293° / 113°"}, {"rota": "SUL", "de": "CHARQUEADAS", "para": "ELDORADO", "max": "2500", "min": "2000", "classe": "D", "rumos": "145° / 325°"}, {"rota": "SUL", "de": "ELDORADO", "para": "GUAÍBA", "max": "2000", "min": "1500", "classe": "D", "rumos": "137° / 317°"}, {"rota": "SUL", "de": "GUAÍBA", "para": "PEDÁGIO VIAMÃO", "max": "2000", "min": "1500", "classe": "D", "rumos": "104° / 284°"}, {"rota": "SUL", "de": "PEDÁGIO VIAMÃO", "para": "SILOS", "max": "2000", "min": "1500", "classe": "D", "rumos": "105° / 285°"}, {"rota": "BEIRA RIO", "de": "GUAÍBA", "para": "BEIRA RIO", "max": "2000", "min": "1500", "classe": "D", "rumos": "063° / 243°"}, {"rota": "TARUMÃ", "de": "TARUMÃ", "para": "PEDÁGIO VIAMÃO", "max": "2000", "min": "1000", "classe": "D", "rumos": "150° / 330°"}];
const reaPontos = {"4 FOLHAS": [-51.129167, -29.1325], "BEIRA RIO": [-51.236167, -30.065833], "CHAPÉU": [-51.1045, -29.837], "FORQUETA": [-51.282, -29.215833], "GM": [-50.915, -29.937833], "PEDÁGIO FREEWAY": [-50.448833, -29.885833], "POLO NORTE": [-51.383333, -29.816667], "TARUMÃ": [-51.019167, -30.050333], "TEUTÔNIA": [-51.816333, -29.482167], "ANTÔNIO PRADO": [-51.281167, -28.857], "CANELA": [-50.827167, -29.364667], "CHARQUEADAS": [-51.623, -29.951667], "ELDORADO": [-51.4455, -30.0695], "GARIBALDI": [-51.532167, -29.268333], "GLORINHA": [-50.788333, -29.880833], "GUAÍBA": [-51.315, -30.133833], "LOMBA GRANDE": [-50.970833, -29.763], "MONTENEGRO": [-51.4895, -29.7195], "PEDÁGIO VIAMÃO": [-50.942167, -30.110833], "SÃO MARCOS": [-51.071667, -28.97], "SÃO VENDELINO": [-51.3645, -29.382167], "SILOS": [-50.745833, -30.103], "TABAÍ": [-51.5005, -29.807], "TAQUARA": [-50.781167, -29.668833], "TRÊS COROAS": [-50.740333, -29.491667], "VERANÓPOLIS": [-51.568333, -28.935], "VILA OLIVA": [-50.889167, -29.22], "ZEZIL": [-51.189, -29.558333]};
const portoes = {"BEIRA RIO": "SBPA/SBCO", "TARUMÃ": "SBPA/SBCO", "GM": "SBPA/SBCO", "CHAPÉU": "SBPA/SBCO", "POLO NORTE": "SBPA/SBCO", "FORQUETA": "SBCX", "4 FOLHAS": "SBCX", "TEUTÔNIA": "", "PEDÁGIO FREEWAY": ""};
var corD = '#c026d3', corG = '#0284c7';
var grupoRea = L.featureGroup();
reaTrechos.forEach(function (t) {
    var a = paraLatLng(reaPontos[t.de]), b = paraLatLng(reaPontos[t.para]);
    var g = t.classe === 'G';
    L.polyline([a, b], { color: g ? corG : corD, weight: 4, opacity: 0.9, dashArray: g ? '8 6' : null })
        .bindPopup('<b>REA ' + t.rota + '</b><br>' + t.de + ' ⇄ ' + t.para + '<br>Tracks: ' + t.rumos +
            '<br>Max. / min. (ft): ' + t.max + (t.max === t.min ? '' : ' / ' + t.min) + '<br>Class ' + t.classe)
        .addTo(grupoRea);
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
    div.innerHTML = '<b>Class</b>' + ['A', 'C', 'D', 'G'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('') +
        '<div><span class="rea-linha"></span>REA class D</div>' +
        '<div><span class="rea-linha g"></span>REA class G</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Gate</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
