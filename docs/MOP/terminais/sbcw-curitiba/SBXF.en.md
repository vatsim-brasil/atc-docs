---
title: SBXF - Florianópolis
tags:
  - Terminal
  - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Florianópolis TMA |
| **Position** | `SBXF_APP` |
| **Callsign** | Florianópolis Control |
| **Frequency** | **119.650** MHz[^pacote] |
| **ATS surveillance** | Radar |
| **Aerodromes in the TMA** | [SBFL](../../aerodromos/sbcw-curitiba/twr/SBFL.en.md), [SBNF](../../aerodromos/sbcw-curitiba/twr/SBNF.en.md), [SBJV](../../aerodromos/sbcw-curitiba/afis/SBJV.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Use the tabs above: **Aeronautical Charts** shows the TMA charts, **Visual Chart** shows the visual chart from AISWEB, **Weather** shows a weather map of the area and **VATSIM Traffic** opens the traffic at the main aerodrome (SBFL).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBXF?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Visual Chart"
    [:material-open-in-new: Open in new tab](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Source: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Weather"
    <div class="tma-meteo" data-lat="-27.154" data-lon="-48.619" data-zoom="8" data-lang="en"></div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBFL){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

The **Visual corridors (REA)** layer shows the 12 corridors of the CCV REA XF chart and the gates (yellow). Solid magenta line: class D; dashed blue: class G; the arrow marks the one-way exit to PONTA DO ARAÇÁ. Click a segment to see the tracks, altitudes and contact. Details in [Visual corridors (REA)](#visual-corridors-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Florianópolis 2 | 1500 FT – 5500 FT | <span class="classe-badge classe-d">D</span> |
| Florianópolis 3 (Navegantes) | 1500 FT – 5500 FT | <span class="classe-badge classe-c">C</span> |
| Florianópolis 1 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Florianópolis CTR | GND – 1500 FT | <span class="classe-badge classe-d">D</span> |
| Navegantes CTR | GND – 1500 FT | <span class="classe-badge classe-c">C</span> |
| Navegantes ATZ | GND – 1500 FT | — |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBXF_APP** | `XF` | Florianópolis Control | **119.650** |  |
| **SBFL_TWR** | `TFL` | Florianópolis Tower | **118.700** |  |
| **SBNF_TWR** | `TNF` | Navegantes Tower | **118.200** |  |

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
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CSE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CSW_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CWE_CTR</span>"]:::grpctr
        g1["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CS_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBCW_CW_CTR</span>"]:::grpctr
        p1["SBCW_C_CTR"]:::ctr
        p2["SBXF_APP"]:::app
        p3["SBFL_TWR"]:::twr
        p4["SBNF_TWR"]:::twr
        a0(["Florianópolis TMA"]):::esp --> p2
        a1(["Florianópolis CTR"]):::esp --> p3
        a2(["Navegantes CTR<br>Navegantes ATZ"]):::esp --> p4
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

## :material-airplane: VFR circulation

!!! abstract "Visual navigation documents"
    - **Circular:** [AIC N 22/24 – VFR circulation in the Florianópolis Terminal Area](https://publicacoes.decea.mil.br/publicacao/aic-n-2224){ target="_blank" } (in force since 03 OCT 2024, replaces AIC N 06/24)
    - **Visual chart – Aircraft routes (REA):** [CCV REA XF-Florianópolis](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xf-florianopolis_rea_20241003.pdf){ target="_blank" } (03 OCT 2024), which is Annex B of the AIC

    The chart is embedded in the **Visual Chart** tab under **Useful Information**. The rules in this section come from AIC N 22/24[^aic2224]; the track, altitudes and class of each corridor come from the chart.

### TMA layers and who handles VFR

| Airspace | Limits | Class | VFR |
| --- | --- | :---: | --- |
| **Florianópolis 1** | 5500 FT – FL195 | <span class="classe-badge classe-c">C</span> up to FL145, <span class="classe-badge classe-a">A</span> above | With APP clearance; above FL145, class A, no VFR |
| **Florianópolis 2** | 1500 FT – 5500 FT | <span class="classe-badge classe-d">D</span> | Around SBFL; along the REAs or with APP clearance |
| **Florianópolis 3** | 1500 FT – 5500 FT | <span class="classe-badge classe-c">C</span> | Around SBNF; along the REAs or with APP clearance |
| **Florianópolis CTR** | GND – 1500 FT | <span class="classe-badge classe-d">D</span> | Entry and exit through the gates |
| **Navegantes CTR** | GND – 1500 FT | <span class="classe-badge classe-c">C</span> | Entry and exit through the gates |
| **TMA projection** | Below Florianópolis 1, outside TMA 2 and 3 and the CTRs | <span class="classe-badge classe-g">G</span> | Along the REAs, coordinating on the sector's FCA |

- **Corridor class:** each segment takes the corridor's class, marked on the chart. Segments inside controlled airspace, near SBFL, SBNF and SSKT, are **class D**, with the APP; the rest, in the hills, on the north coast and along the island's east coast, are **class G**, with FCA coordination.
- **FCA:** the TMA projection is split into three coordination sectors: **North 122.850** (Blumenau, Itajaí and the north coast), **East 126.575** (Porto Belo, Tijucas and the Santa Catarina Island coast) and **South 119.100** (Ituporanga, the hills and the south). FCA 123.450 is **not** used below the Florianópolis TMA.
- **In the real world**, Florianópolis APP provides flight information and alerting in class G on the sector frequency; the chart gives sector 1 (128.950 and 119.650), sector 2 (119.650 and 128.950), sector 3 (120.325 and 119.500) and sector 4 (119.500 and 120.325).
- **In the package**, VFR traffic calls `SBXF_APP` (**119.650**); inside the CTRs, `SBFL_TWR` (**118.700**) and `SBNF_TWR` (**118.200**). Pilots call the **online** position, not the real-world frequency. Without it, the next position in the [coverage](#top-down-coverage) takes over. Air-to-air coordination goes on **UNICOM 122.800**.

### General VFR rules

- **Using the REAs:** in and below the TMA, VFR traffic **preferably** flies the REAs, joining or leaving them at any point stated in the flight plan. To operate at **SBFL, SBNF, SSKT and SDEN**, the REAs are **mandatory**, with entry and exit through the gates. In contact with the APP, and traffic permitting, the flight may be cleared off them.
- **In controlled airspace**, joining the REAs requires APP clearance; gates and positions are **compulsory reporting points**. To cross the TMA or the CTRs, use the REAs until leaving them or ask the APP for a direct track.
- **In class G**, the routes are mandatory or suggested and the altitudes are **mandatory**: they keep clear of restricted areas, IFR procedures and aerodrome circuits.
- **Right of the centreline:** pilots fly to the **right** of the corridor centreline, with the visual references on their left.
- **Width:** 3 NM (1.5 NM either side of the centreline).
- **Altitudes:** changes are made over the points, coordinated on the FCA, under the pilot's responsibility and in VMC; on controlled segments the APP may assign another altitude.
- **QNH:** sectors 1 and 2 (Florianópolis), from the SBFL ATIS; sectors 3 and 4 (Navegantes), from the SBNF ATIS; without ATIS, ask the APP.
- **Flight plan:** in item 15, the **coordinates** of the gates and positions (the system does not accept the names); in item 18, the corridor names.
- **Radio contact:** brief, with registration, origin and destination, corridor, position, altitude and estimate for the next point.
- A mode A/C or S **transponder** is mandatory; landing or taxi lights on are recommended.
- **Holding:** to space out entries into the TMA and CTRs, the APP may hold traffic over REA points; in class G, holding in VMC is the pilot's responsibility, without entering controlled airspace uncleared.
- **Helicopters** may use the REAs; below the TMA and off the REAs, they may ask the APP to enter the CTRs at another altitude. To land inside the CTRs, call the APP or the Tower with altitude, origin, destination and estimate.
- **IMC:** turn back and land at the departure aerodrome or the nearest one, change to IFR, or ask to leave the REA.

### Visual corridors (REA)

The 12 corridors of the TMA. Altitudes in feet (QNH), as **maximum / minimum**; a single altitude is mandatory. **⇄** is a two-way segment, with tracks as outbound / return; **→** is one-way.

| REA | Segment | Tracks | Altitudes | Class · contact |
| :---: | :--- | :---: | :---: | :--- |
| **NORTE** | BLUMENAU ⇄ RODOVIA | 092° / 272° | 3000 / 1900 | G · FCA Norte 122.850 |
|  | RODOVIA ⇄ PIÇARRAS | 092° / 272° | 2500 / 2300 | D · APP-FL |
|  | PIÇARRAS ⇄ BARRA VELHA | 014° / 194° | 2500 / 0900 | D · APP-FL |
| **BAIA** | BARRA VELHA ⇄ ARMAÇÃO | 143° / 323° | 1000 / 0700 | G · FCA Norte 122.850 |
|  | ARMAÇÃO ⇄ NAVEGA | 166° / 346° | 1000 / 0500 | G · FCA Norte 122.850 |
|  | NAVEGA ⇄ ESTALEIRINHO | 234° / 054° | 1400 / 1200 | G · FCA Norte 122.850 |
|  | ESTALEIRINHO ⇄ COSTA ESMERALDA | 222° / 042° | 3000 / 1700 | G · FCA Leste 126.575 |
|  | COSTA ESMERALDA ⇄ GANCHOS | 190° / 010° | 3500 / 2000 | G · FCA Leste 126.575 |
|  | GANCHOS ⇄ FLY VILLE | 205° / 025° | 4000 / 2100 | G · FCA Leste 126.575 |
|  | FLY VILLE ⇄ BIGUAÇU | 189° / 009° | 4000 / 2100 | D · APP-FL |
|  | BIGUAÇU ⇄ TRAPICHE | 189° / 009° | 1000 / 0700 | D · APP-FL |
|  | TREVO ⇄ RIBEIRÃO DA ILHA | 168° / 348° | 2000 / 1700 | D · APP-FL |
|  | RIBEIRÃO DA ILHA ⇄ PAPAGAIO | 188° / 008° | 2500 / 2000 | D · APP-FL |
| **EUROPA** | BLUMENAU ⇄ BRUSQUE | 165° / 345° | 3000 / 2700 | G · FCA Norte 122.850 |
|  | BRUSQUE ⇄ DECKER | 167° / 347° | 3000 / 2500 | G · FCA Norte 122.850 |
|  | DECKER ⇄ COSTA ESMERALDA | 116° / 296° | 3500 | G · FCA Leste 126.575 |
| **SERRA DO ITAJAÍ** | ITAJAÍ-AÇU ⇄ PARQUE | 108° / 288° | 5000 / 4500 | G · FCA Norte 122.850 |
|  | PARQUE ⇄ BRUSQUE | 109° / 289° | 4500 / 4000 | G · FCA Norte 122.850 |
| **PORTO BELO** | CALCÁRIO ⇄ TÊXTIL | 111° / 291° | 5000 / 3500 | G · FCA Norte 122.850 |
|  | TÊXTIL ⇄ COSTA ESMERALDA | 097° / 277° | 4000 / 2300 | G · FCA Leste 126.575 |
|  | COSTA ESMERALDA → PONTA DO ARAÇÁ | 079° | 5000 / 1300 | G · FCA Leste 126.575 |
| **MADRE PAULINA** | ITUPORANGA ⇄ SALSEIRO | 097° / 277° | 5000 / 3600 | G · FCA Sul 119.100 |
|  | SALSEIRO ⇄ NOVA TRENTO | 097° / 277° | 5000 / 4000 | G · FCA Sul 119.100 |
|  | NOVA TRENTO ⇄ CANELINHA | 102° / 282° | 4500 / 2600 | G · FCA Sul 119.100 |
|  | CANELINHA ⇄ COSTA ESMERALDA | 069° / 249° | 3500 / 1800 | G · FCA Leste 126.575 |
| **BELA VISTA** | ITUPORANGA ⇄ BARRAGEM | 124° / 304° | 5000 / 3800 | G · FCA Sul 119.100 |
| **OESTE** | BARRAGEM ⇄ CANELINHA | 060° / 240° | 5000 / 4000 | D · APP-FL |
|  | BARRAGEM ⇄ SÃO PEDRO DE ALCÂNTARA | 129° / 309° | 4500 / 3700 | D · APP-FL |
|  | RANCHO QUEIMADO ⇄ SÃO PEDRO DE ALCÂNTARA | 073° / 253° | 4500 / 3800 | D · APP-FL |
| **CENTRAL** | RATONES ⇄ BIGUAÇU | 234° / 054° | 2000 / 1500 | D · APP-FL |
| **LESTE** | GANCHOS ⇄ LAGOINHA | 137° / 317° | 3500 / 1100 | G · FCA Leste 126.575 |
|  | LAGOINHA ⇄ RATONES | 234° / 054° | 3500 / 1000 | G · FCA Leste 126.575 |
|  | LAGOINHA ⇄ BRAVA | 137° / 317° | 3500 / 1000 | G · FCA Leste 126.575 |
|  | BRAVA ⇄ SANTINHO | 163° / 343° | 3500 / 1000 | G · FCA Leste 126.575 |
|  | SANTINHO ⇄ ILHA DAS ARANHAS | 199° / 019° | 1500 / 1100 | G · FCA Leste 126.575 |
|  | ILHA DAS ARANHAS ⇄ ILHA XAVIER | 222° / 042° | 1000 / 0900 | G · FCA Leste 126.575 |
|  | ILHA XAVIER ⇄ JOAQUINA | 244° / 064° | 1000 / 0700 | G · FCA Leste 126.575 |
|  | PANTANO DO SUL ⇄ TRÊS IRMÃS | 240° / 060° | 1500 / 1000 | G · FCA Leste 126.575 |
|  | PAPAGAIO ⇄ TRÊS IRMÃS | 107° / 287° | 1500 / 1200 | D · APP-FL |
|  | PAPAGAIO ⇄ GAMBOA | 210° / 030° | 4500 / 2000 | D · APP-FL |
|  | GAMBOA ⇄ IMBITUBA | 209° / 029° | 4500 / 1500 | G · FCA Sul 119.100 |

What each corridor does:

- **BAIA** is the coastal axis: from BARRA VELHA via ARMAÇÃO, NAVEGA and ESTALEIRINHO, very low over the sea, to COSTA ESMERALDA (SDEN), then via GANCHOS and FLY VILLE to BIGUAÇU and into SBFL through the TRAPICHE gate. South of the island it continues from TREVO via RIBEIRÃO DA ILHA to PAPAGAIO.
- **NORTE** links Blumenau to the coast: from BLUMENAU via RODOVIA (an SBNF gate) to PIÇARRAS and BARRA VELHA, where the Curitiba TMA's BARRA DO SUL REA carries on north.
- **EUROPA** runs from BLUMENAU via BRUSQUE and DECKER to COSTA ESMERALDA.
- **SERRA DO ITAJAÍ** comes from the ITAJAÍ-AÇU gate over the hills and PARQUE to BRUSQUE; **PORTO BELO** comes from the CALCÁRIO gate via TÊXTIL to COSTA ESMERALDA and leaves, eastbound only, through PONTA DO ARAÇÁ. It is the SDEN route for high-performance aircraft, which plan via CALCÁRIO or PONTA DO ARAÇÁ.
- **MADRE PAULINA** comes from the ITUPORANGA gate via SALSEIRO and NOVA TRENTO to CANELINHA and COSTA ESMERALDA; **BELA VISTA** links ITUPORANGA to BARRAGEM.
- **OESTE** links BARRAGEM to CANELINHA and, to the south, to SÃO PEDRO DE ALCÂNTARA, which the segment from the RANCHO QUEIMADO gate also reaches.
- **CENTRAL** links RATONES, in the north of the island, to BIGUAÇU across the north bay.
- **LESTE** goes round Santa Catarina Island over the sea: from GANCHOS via LAGOINHA, BRAVA, SANTINHO and ILHA DAS ARANHAS to ILHA XAVIER and the JOAQUINA gate; in the south, from the PANTANO DO SUL gate via TRÊS IRMÃS to PAPAGAIO, and on via GAMBOA to the IMBITUBA gate. A branch links LAGOINHA to RATONES.

### Aerodrome gates

| Aerodrome | Gates |
| :---: | :--- |
| **SBFL** | TRAPICHE · JOAQUINA · RIBEIRÃO DA ILHA · PANTANO DO SUL · SÃO PEDRO DE ALCÂNTARA |
| **SSKT** | BIGUAÇU · TREVO · SÃO PEDRO DE ALCÂNTARA |
| **SBNF** | PIÇARRAS · RODOVIA · ESTALEIRINHO |
| **SDEN** | TÊXTIL · PONTA DO ARAÇÁ (exit only) · ESTALEIRINHO · DECKER · CANELINHA · GANCHOS |

The BARRA VELHA, CALCÁRIO, ITAJAÍ-AÇU, ITUPORANGA, RANCHO QUEIMADO and IMBITUBA gates are on the edges of the TMA.

**SDEN (Costa Esmeralda):** Z-plan departures and Y-plan arrivals plan along the PORTO BELO REA. Y-plan arrivals join via BAIA, through NAVEGA or ESTALEIRINHO, or via PORTO BELO, through CALCÁRIO; the APP may give another position and altitude. On PORTO BELO, the chart altitudes apply until two-way contact with the APP.

### Other rules

- AFIL flight plans are not accepted.
- SBNF: circuit to the northwest only, at 1100 FT for category A and B aeroplanes (category C prohibited) and 600 FT for helicopters. Entries via the Containers and Foz gates; overflights at 2400 FT minimum.
- Departures from aerodromes or heliports inside the CTRs or below the REAs call first, on the FCA or the sector's ATS unit, for crossing or joining instructions.
- With a full flight plan and a change from VFR to IFR (Z plan), wait for the APP clearance, keeping to the corridor altitudes.
- On busy dates or with temporary restricted areas active, the REAs may be suspended or have their class changed by NOTAM.

### Phraseology

On contact, the pilot gives registration, origin and destination, corridor, position, altitude and estimate for the next point[^aic2224]. Brazilian VFR traffic usually calls in Portuguese:

```
Controle Florianópolis, PR-AFS, de SSET para SDEN, corredor BAIA, vertical de PAPAGAIO, 1500 pés, estima RIBEIRÃO DA ILHA aos 1100Z.
```

In class G, on the FCA (UNICOM on VATSIM):

```
Tráfego Leste, PR-MWN, REA LESTE, BRAVA, 3000 pés, proa SANTINHO.
```

## :material-note-text-outline: Remarks

- Florianópolis 1 is class A between FL145 and FL195 and class C between 5500 FT and FL145.
- SBJV (Joinville) lies in the Joinville 1 and 2 FIZs (class G), served by Joinville Radio.
- Volumes and map follow AIP AMDT AIRAC 2612A1 (26 NOV 2026).

---

Back to the Curitiba FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.
[^aic2224]: [AIC N 22/24](https://publicacoes.decea.mil.br/publicacao/aic-n-2224){ target="_blank" }, items 3 to 6 and Annexes A and B.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude]; os arcos da Florianópolis 2 viram polilinhas.
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
    {"tipo": "tma", "id": "SBXF", "nome": "Florianópolis 1", "posicao": "SBXF_APP", "freq": "119.650", "lim": "5500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-48.326111, -28.302222], [-48.686667, -28.107778], [-48.832778, -28.2675], [-49.348333, -28.087222], [-49.510556, -27.983611], [-49.748611, -27.771944], [-49.668611, -27.374167], [-49.226944, -26.895278], [-48.753611, -26.608611], [-48.568056, -26.495556], [-48.511944, -26.261111], [-48.157222, -26.01], [-47.921667, -26.3375], [-47.729444, -26.744167], [-47.691944, -26.84], [-47.488333, -27.36]]},
    {"tipo": "tma", "id": "SBXF", "nome": "Florianópolis 2", "posicao": "SBXF_APP", "freq": "119.650", "lim": "1500 FT – 5500 FT", "classe": "D", "link": "", "contorno": [[-48.305833, -28.031944], [-49.009444, -27.651667], [-49.008778, -27.641268], [-49.007818, -27.630888], [-49.006565, -27.620532], [-49.005019, -27.610207], [-49.003182, -27.599919], [-49.001054, -27.589676], [-48.998637, -27.579483], [-48.995933, -27.569347], [-48.992942, -27.559274], [-48.989668, -27.54927], [-48.986111, -27.539342], [-48.982275, -27.529497], [-48.978162, -27.519739], [-48.973773, -27.510076], [-48.969113, -27.500514], [-48.964184, -27.491057], [-48.958988, -27.481713], [-48.95353, -27.472488], [-48.947813, -27.463386], [-48.94184, -27.454414], [-48.935615, -27.445577], [-48.929142, -27.436882], [-48.922425, -27.428332], [-48.915468, -27.419935], [-48.908276, -27.411694], [-48.900853, -27.403616], [-48.893204, -27.395704], [-48.885333, -27.387965], [-48.877246, -27.380403], [-48.868948, -27.373023], [-48.860443, -27.36583], [-48.851738, -27.358827], [-48.842837, -27.35202], [-48.833746, -27.345412], [-48.824472, -27.339008], [-48.815019, -27.332812], [-48.805393, -27.326828], [-48.795602, -27.321059], [-48.78565, -27.315509], [-48.775545, -27.310182], [-48.071667, -27.6875], [-48.072313, -27.697951], [-48.073256, -27.708385], [-48.074496, -27.718794], [-48.076031, -27.729172], [-48.077861, -27.739513], [-48.079984, -27.749809], [-48.082399, -27.760055], [-48.085105, -27.770244], [-48.0881, -27.780369], [-48.091381, -27.790424], [-48.094947, -27.800403], [-48.098796, -27.8103], [-48.102926, -27.820107], [-48.107332, -27.829819], [-48.112014, -27.83943], [-48.116967, -27.848933], [-48.122189, -27.858323], [-48.127676, -27.867593], [-48.133425, -27.876738], [-48.139432, -27.885752], [-48.145694, -27.894629], [-48.152205, -27.903364], [-48.158964, -27.91195], [-48.165964, -27.920383], [-48.173202, -27.928658], [-48.180673, -27.936768], [-48.188372, -27.944709], [-48.196294, -27.952476], [-48.204435, -27.960064], [-48.212788, -27.967468], [-48.22135, -27.974683], [-48.230114, -27.981705], [-48.239075, -27.98853], [-48.248227, -27.995152], [-48.257565, -28.001568], [-48.267082, -28.007774], [-48.276772, -28.013766], [-48.28663, -28.019539], [-48.296649, -28.025091], [-48.306822, -28.030418]]},
    {"tipo": "tma", "id": "SBXF", "nome": "Florianópolis 3 (Navegantes)", "posicao": "SBXF_APP", "freq": "119.650", "lim": "1500 FT – 5500 FT", "classe": "C", "link": "", "contorno": [[-49.005278, -26.825556], [-48.521944, -26.530556], [-48.265833, -26.8675], [-48.678889, -27.119722], [-48.858333, -27.104167], [-49.005833, -26.910278]]},
    {"tipo": "ctr", "id": "SBXF", "nome": "Florianópolis CTR", "posicao": "SBFL_TWR", "freq": "118.700", "lim": "GND – 1500 FT", "classe": "D", "link": "", "contorno": [[-48.441667, -27.802778], [-48.363889, -27.688611], [-48.606667, -27.5575], [-48.684722, -27.671944]]},
    {"tipo": "ctr", "id": "SBXF", "nome": "Navegantes CTR", "posicao": "SBNF_TWR", "freq": "118.200", "lim": "GND – 1500 FT", "classe": "C", "link": "", "contorno": [[-48.816111, -26.913056], [-48.555556, -26.753889], [-48.483333, -26.848889], [-48.743889, -27.007778]]},
    {"tipo": "ctr", "id": "SBXF", "nome": "Navegantes ATZ", "posicao": "SBNF_TWR", "freq": "118.200", "lim": "GND – 1500 FT", "classe": "—", "link": "", "contorno": [[-48.682222, -26.911389], [-48.635, -26.91], [-48.590833, -26.883333], [-48.633056, -26.828056], [-48.71, -26.875]]}
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

// Corredores visuais (REA) e portões da carta CCV REA XF (03 OUT 2024), Anexo B da AIC N 22/24; trechos retos entre os pontos nomeados
const reaTrechos = [{"rota": "NORTE", "de": "BLUMENAU", "para": "RODOVIA", "rumo": "092°", "rumoVolta": "272°", "max": "3000", "min": "1900", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "NORTE", "de": "RODOVIA", "para": "PIÇARRAS", "rumo": "092°", "rumoVolta": "272°", "max": "2500", "min": "2300", "classe": "D", "esp": "D · APP-FL"}, {"rota": "NORTE", "de": "PIÇARRAS", "para": "BARRA VELHA", "rumo": "014°", "rumoVolta": "194°", "max": "2500", "min": "0900", "classe": "D", "esp": "D · APP-FL"}, {"rota": "BAIA", "de": "BARRA VELHA", "para": "ARMAÇÃO", "rumo": "143°", "rumoVolta": "323°", "max": "1000", "min": "0700", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "BAIA", "de": "ARMAÇÃO", "para": "NAVEGA", "rumo": "166°", "rumoVolta": "346°", "max": "1000", "min": "0500", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "BAIA", "de": "NAVEGA", "para": "ESTALEIRINHO", "rumo": "234°", "rumoVolta": "054°", "max": "1400", "min": "1200", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "BAIA", "de": "ESTALEIRINHO", "para": "COSTA ESMERALDA", "rumo": "222°", "rumoVolta": "042°", "max": "3000", "min": "1700", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "BAIA", "de": "COSTA ESMERALDA", "para": "GANCHOS", "rumo": "190°", "rumoVolta": "010°", "max": "3500", "min": "2000", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "BAIA", "de": "GANCHOS", "para": "FLY VILLE", "rumo": "205°", "rumoVolta": "025°", "max": "4000", "min": "2100", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "BAIA", "de": "FLY VILLE", "para": "BIGUAÇU", "rumo": "189°", "rumoVolta": "009°", "max": "4000", "min": "2100", "classe": "D", "esp": "D · APP-FL"}, {"rota": "BAIA", "de": "BIGUAÇU", "para": "TRAPICHE", "rumo": "189°", "rumoVolta": "009°", "max": "1000", "min": "0700", "classe": "D", "esp": "D · APP-FL"}, {"rota": "BAIA", "de": "TREVO", "para": "RIBEIRÃO DA ILHA", "rumo": "168°", "rumoVolta": "348°", "max": "2000", "min": "1700", "classe": "D", "esp": "D · APP-FL"}, {"rota": "BAIA", "de": "RIBEIRÃO DA ILHA", "para": "PAPAGAIO", "rumo": "188°", "rumoVolta": "008°", "max": "2500", "min": "2000", "classe": "D", "esp": "D · APP-FL"}, {"rota": "EUROPA", "de": "BLUMENAU", "para": "BRUSQUE", "rumo": "165°", "rumoVolta": "345°", "max": "3000", "min": "2700", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "EUROPA", "de": "BRUSQUE", "para": "DECKER", "rumo": "167°", "rumoVolta": "347°", "max": "3000", "min": "2500", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "EUROPA", "de": "DECKER", "para": "COSTA ESMERALDA", "rumo": "116°", "rumoVolta": "296°", "max": "3500", "min": "3500", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "SERRA DO ITAJAÍ", "de": "ITAJAÍ-AÇU", "para": "PARQUE", "rumo": "108°", "rumoVolta": "288°", "max": "5000", "min": "4500", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "SERRA DO ITAJAÍ", "de": "PARQUE", "para": "BRUSQUE", "rumo": "109°", "rumoVolta": "289°", "max": "4500", "min": "4000", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "PORTO BELO", "de": "CALCÁRIO", "para": "TÊXTIL", "rumo": "111°", "rumoVolta": "291°", "max": "5000", "min": "3500", "classe": "G", "esp": "G · FCA Norte 122.850"}, {"rota": "PORTO BELO", "de": "TÊXTIL", "para": "COSTA ESMERALDA", "rumo": "097°", "rumoVolta": "277°", "max": "4000", "min": "2300", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "PORTO BELO", "de": "COSTA ESMERALDA", "para": "PONTA DO ARAÇÁ", "rumo": "079°", "rumoVolta": null, "max": "5000", "min": "1300", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "MADRE PAULINA", "de": "ITUPORANGA", "para": "SALSEIRO", "rumo": "097°", "rumoVolta": "277°", "max": "5000", "min": "3600", "classe": "G", "esp": "G · FCA Sul 119.100"}, {"rota": "MADRE PAULINA", "de": "SALSEIRO", "para": "NOVA TRENTO", "rumo": "097°", "rumoVolta": "277°", "max": "5000", "min": "4000", "classe": "G", "esp": "G · FCA Sul 119.100"}, {"rota": "MADRE PAULINA", "de": "NOVA TRENTO", "para": "CANELINHA", "rumo": "102°", "rumoVolta": "282°", "max": "4500", "min": "2600", "classe": "G", "esp": "G · FCA Sul 119.100"}, {"rota": "MADRE PAULINA", "de": "CANELINHA", "para": "COSTA ESMERALDA", "rumo": "069°", "rumoVolta": "249°", "max": "3500", "min": "1800", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "BELA VISTA", "de": "ITUPORANGA", "para": "BARRAGEM", "rumo": "124°", "rumoVolta": "304°", "max": "5000", "min": "3800", "classe": "G", "esp": "G · FCA Sul 119.100"}, {"rota": "OESTE", "de": "BARRAGEM", "para": "CANELINHA", "rumo": "060°", "rumoVolta": "240°", "max": "5000", "min": "4000", "classe": "D", "esp": "D · APP-FL"}, {"rota": "OESTE", "de": "BARRAGEM", "para": "SÃO PEDRO DE ALCÂNTARA", "rumo": "129°", "rumoVolta": "309°", "max": "4500", "min": "3700", "classe": "D", "esp": "D · APP-FL"}, {"rota": "OESTE", "de": "RANCHO QUEIMADO", "para": "SÃO PEDRO DE ALCÂNTARA", "rumo": "073°", "rumoVolta": "253°", "max": "4500", "min": "3800", "classe": "D", "esp": "D · APP-FL"}, {"rota": "CENTRAL", "de": "RATONES", "para": "BIGUAÇU", "rumo": "234°", "rumoVolta": "054°", "max": "2000", "min": "1500", "classe": "D", "esp": "D · APP-FL"}, {"rota": "LESTE", "de": "GANCHOS", "para": "LAGOINHA", "rumo": "137°", "rumoVolta": "317°", "max": "3500", "min": "1100", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "LAGOINHA", "para": "RATONES", "rumo": "234°", "rumoVolta": "054°", "max": "3500", "min": "1000", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "LAGOINHA", "para": "BRAVA", "rumo": "137°", "rumoVolta": "317°", "max": "3500", "min": "1000", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "BRAVA", "para": "SANTINHO", "rumo": "163°", "rumoVolta": "343°", "max": "3500", "min": "1000", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "SANTINHO", "para": "ILHA DAS ARANHAS", "rumo": "199°", "rumoVolta": "019°", "max": "1500", "min": "1100", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "ILHA DAS ARANHAS", "para": "ILHA XAVIER", "rumo": "222°", "rumoVolta": "042°", "max": "1000", "min": "0900", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "ILHA XAVIER", "para": "JOAQUINA", "rumo": "244°", "rumoVolta": "064°", "max": "1000", "min": "0700", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "PANTANO DO SUL", "para": "TRÊS IRMÃS", "rumo": "240°", "rumoVolta": "060°", "max": "1500", "min": "1000", "classe": "G", "esp": "G · FCA Leste 126.575"}, {"rota": "LESTE", "de": "PAPAGAIO", "para": "TRÊS IRMÃS", "rumo": "107°", "rumoVolta": "287°", "max": "1500", "min": "1200", "classe": "D", "esp": "D · APP-FL"}, {"rota": "LESTE", "de": "PAPAGAIO", "para": "GAMBOA", "rumo": "210°", "rumoVolta": "030°", "max": "4500", "min": "2000", "classe": "D", "esp": "D · APP-FL"}, {"rota": "LESTE", "de": "GAMBOA", "para": "IMBITUBA", "rumo": "209°", "rumoVolta": "029°", "max": "4500", "min": "1500", "classe": "G", "esp": "G · FCA Sul 119.100"}];
const reaPontos = {"BARRA VELHA": [-48.6825, -26.629167], "CALCÁRIO": [-49.149833, -27.216667], "IMBITUBA": [-48.650167, -28.23], "ITAJAÍ-AÇU": [-49.517167, -27.113167], "ITUPORANGA": [-49.596, -27.4185], "JOAQUINA": [-48.421, -27.642667], "PANTANO DO SUL": [-48.466167, -27.811], "PONTA DO ARAÇÁ": [-48.510167, -27.107333], "RANCHO QUEIMADO": [-49.012667, -27.673], "SÃO PEDRO DE ALCÂNTARA": [-48.892167, -27.593], "TRAPICHE": [-48.575667, -27.55], "TREVO": [-48.6305, -27.717667], "ARMAÇÃO": [-48.524667, -26.719833], "BARRAGEM": [-49.0205, -27.553], "BIGUAÇU": [-48.59, -27.484333], "BLUMENAU": [-49.0805, -26.890833], "BRAVA": [-48.389667, -27.353], "BRUSQUE": [-48.916, -27.101167], "CANELINHA": [-48.7435, -27.260333], "COSTA ESMERALDA": [-48.621667, -27.166667], "DECKER": [-48.8855, -27.143667], "ESTALEIRINHO": [-48.572333, -27.054667], "FLY VILLE": [-48.614333, -27.369333], "GAMBOA": [-48.596667, -27.947333], "GANCHOS": [-48.6045, -27.256833], "ILHA DAS ARANHAS": [-48.331333, -27.486], "ILHA XAVIER": [-48.386, -27.61], "LAGOINHA": [-48.465167, -27.319333], "NAVEGA": [-48.423167, -26.853833], "NOVA TRENTO": [-48.917167, -27.283333], "PAPAGAIO": [-48.578833, -27.855], "PARQUE": [-49.199833, -27.107], "PIÇARRAS": [-48.665667, -26.7675], "RATONES": [-48.533167, -27.409167], "RIBEIRÃO DA ILHA": [-48.600833, -27.760167], "RODOVIA": [-49.0055, -26.8685], "SALSEIRO": [-49.332833, -27.367], "SANTINHO": [-48.3335, -27.418], "TÊXTIL": [-48.886667, -27.222833], "TRÊS IRMÃS": [-48.505, -27.852167]};
const portoes = {"TRAPICHE": "SBFL", "JOAQUINA": "SBFL", "RIBEIRÃO DA ILHA": "SBFL", "PANTANO DO SUL": "SBFL", "SÃO PEDRO DE ALCÂNTARA": "SBFL/SSKT", "BIGUAÇU": "SSKT", "TREVO": "SSKT", "PIÇARRAS": "SBNF", "RODOVIA": "SBNF", "ESTALEIRINHO": "SBNF/SDEN", "TÊXTIL": "SDEN", "PONTA DO ARAÇÁ": "SDEN, só saída", "DECKER": "SDEN", "CANELINHA": "SDEN", "GANCHOS": "SDEN", "BARRA VELHA": "", "CALCÁRIO": "", "IMBITUBA": "", "ITAJAÍ-AÇU": "", "ITUPORANGA": "", "RANCHO QUEIMADO": ""};
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
        '<div><span class="rea-linha"></span>REA class D</div>' +
        '<div><span class="rea-linha g"></span>REA class G</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Gate</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
