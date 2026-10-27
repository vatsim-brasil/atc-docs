---
title: SBWT - Curitiba
tags:
  - Terminal
  - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Curitiba TMA |
| **Position** | `SBWT_APP` |
| **Callsign** | Curitiba Control |
| **Frequency** | **119.950** MHz[^pacote] |
| **ATS surveillance** | Radar |
| **Aerodromes in the TMA** | [SBCT](../../aerodromos/sbcw-curitiba/twr/SBCT.en.md), [SBBI](../../aerodromos/sbcw-curitiba/twr/SBBI.en.md), [SBJV](../../aerodromos/sbcw-curitiba/afis/SBJV.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Use the tabs above: **Aeronautical Charts** shows the TMA charts, **Visual Charts** shows the visual charts (REA/REH) from AISWEB, **Weather** shows a weather map of the area and **VATSIM Traffic** opens the traffic at the main aerodrome (SBCT).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWT?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Visual Charts"
    <div class="ccv-viewer" data-lang="en">
    <ul class="ccv-lista">
    <li><a href="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wt-curitiba_rea_20231228.pdf" target="_blank" rel="noopener">CCV REA WT-Curitiba</a></li>
    <li><a href="https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wt-curitiba_reh_20231228.pdf" target="_blank" rel="noopener">CCV REH WT-Curitiba</a></li>
    </ul>
    </div>

    Source: [AISWEB](https://aisweb.decea.mil.br/?i=cartas){ target="_blank" }.

=== ":material-weather-partly-cloudy: Weather"
    <div class="tma-meteo" data-lat="-25.851" data-lon="-49.079" data-zoom="8" data-lang="en"></div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBCT){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

The **Visual corridors (REA)** layer shows the 18 REAs of AIC N 34/23 and the gates (yellow). Solid magenta line: class D; dashed blue: class G; arrows mark the one-way NORTE and SUL. Click a segment to see the tracks, altitudes and contact. Details in [Visual corridors (REA)](#visual-corridors-rea).

The **Helicopter routes (REH)** layer (7 routes) is off by default. Solid line is class D, dashed is class G; names appear when zoomed in. See [Helicopters (REH)](#helicopters-reh).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Curitiba 2 | 4500 FT – 5500 FT | <span class="classe-badge classe-c">C</span> |
| Curitiba 1 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Curitiba CTR | GND – 4500 FT | <span class="classe-badge classe-d">D</span> |
| Bacacheri FIZ | GND – 4500 FT | <span class="classe-badge classe-g">G</span> |
| Joinville 1 FIZ | GND – 3000 FT | <span class="classe-badge classe-g">G</span> |
| Joinville 2 FIZ | 3000 FT – 5500 FT | <span class="classe-badge classe-g">G</span> |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWT_APP** | `WT` | Curitiba Control | **119.950** |  |
| **SBCT_TWR** | `TCT` | Curitiba Tower | **118.150** |  |

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
        p2["SBWT_APP"]:::app
        p3["SBCT_TWR"]:::twr
        a0(["Curitiba TMA"]):::esp --> p2
        a1(["Curitiba CTR"]):::esp --> p3
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
    - **Circular:** [AIC N 34/23 – VFR circulation in the Curitiba Terminal Area](https://publicacoes.decea.mil.br/publicacao/aic-n-34-23){ target="_blank" } (in force since 28 DEC 2023, replaces AIC N 30/18)
    - **Visual chart – Aircraft routes (REA):** [CCV REA WT-Curitiba](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wt-curitiba_rea_20231228.pdf){ target="_blank" }
    - **Visual chart – Helicopter routes (REH):** [CCV REH WT-Curitiba](https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wt-curitiba_reh_20231228.pdf){ target="_blank" }

    The charts are embedded in the **Visual Charts** tab under **Useful Information**. The data in this section comes from AIC N 34/23[^aic3423].

### TMA layers and who handles VFR

| Airspace | Limits | Class | VFR |
| --- | --- | :---: | --- |
| **Curitiba 1** | 5500 FT – FL195 | <span class="classe-badge classe-c">C</span> up to FL145, <span class="classe-badge classe-a">A</span> above | Along the REAs or with APP clearance; above FL145, class A, no VFR |
| **Curitiba 2** | 4500 FT – 5500 FT | <span class="classe-badge classe-c">C</span> | Along the REAs or with APP clearance |
| **Curitiba CTR** | GND – 4500 FT | <span class="classe-badge classe-d">D</span> | Entry and exit through the gates, along the REAs and REHs |
| **Bacacheri FIZ** | GND – 4500 FT | <span class="classe-badge classe-g">G</span> | Around SBBI, inside the CTR; Bacacheri Tower |
| **Joinville 1 and 2 FIZ** | GND – 5500 FT | <span class="classe-badge classe-g">G</span> | Joinville Radio AFIS (1 up to 3000 ft, 2 from 3000 to 5500) |
| **REA and REH** | 2000 to 6500 FT | <span class="classe-badge classe-d">D</span> or <span class="classe-badge classe-g">G</span> | The class is the corridor's own |

- **Corridor class:** each segment takes the corridor's class. Almost every REA is **class D**, with the APP. The exceptions are NORTE and SUL, the Bacacheri flight-school training corridors, in **class G** on the Bacacheri Tower frequency. On the REHs, the segments around Barigui Park are class G, with FCA coordination, and the rest are class D.
- **In the real world**, the REAs around Curitiba use Curitiba APP on **119.950**, **119.700**, **129.550** or **120.650**; those on the coast, near Joinville, **120.950** or **133.150**. The REHs talk to Curitiba Tower (**118.150**), Bacacheri Tower (**118.900**) or the APP, depending on the segment; on class G segments the FCA is **123.450**.
- **In the package**, VFR traffic on the REAs calls `SBWT_APP` (**119.950**); inside the CTR, `SBCT_TWR` (**118.150**), and at Bacacheri and Joinville the aerodrome positions. Pilots call the **online** position, not the real-world frequency. Without it, the next position in the [coverage](#top-down-coverage) takes over. Air-to-air coordination goes on **UNICOM 122.800**.
- **Joinville:** the AIC still refers to a Joinville CTR (CTR-JV), but today's AIP has the Joinville 1 and 2 FIZ, class G.

### General VFR rules

- **Using the REAs:** **mandatory** to land at or depart from SBCT, SBBI and SBJV; entry into the Curitiba CTR is through the gates. Other VFR traffic in or below the TMA **preferably** uses the REAs and REHs, joining or leaving them at any point stated in the flight plan. In contact with the APP, and traffic permitting, the flight may be cleared off them.
- **Right of the centreline:** pilots fly to the **right** of the corridor centreline, with the visual references on their left.
- **Width:** REAs 3 NM (1.5 NM either side); REHs 1 NM (0.5 NM either side).
- **Altitudes:** each segment has a maximum and a minimum; in controlled areas the limits must be respected. Altitude changes are made over the points, under the pilot's responsibility and in VMC; on controlled segments the APP may assign another altitude.
- **Flight plan:** in item 15, the **coordinates** of the gates and positions (the system does not accept the names); in item 18, the corridor names.
- **Radio contact:** brief, with registration, origin and destination, corridor, position, altitude and estimate for the next point.
- **QNH** from the SBCT ATIS; near Joinville, from the SBJV ATIS; without ATIS, ask the APP.
- A mode A/C or S **transponder** is mandatory; landing or taxi lights on are recommended.
- **Holding:** to space out entries into the TMA and CTR, the APP may hold traffic over REA and REH points.
- **Helicopters** may use the REAs.
- **IMC:** turn back and land at the departure aerodrome or the nearest one, ask for special VFR, change to IFR, or ask to leave the REA.

Unless the APP assigns a code, traffic departing from a place without an ATS unit under the TMA, or coming from outside it, squawks the **destination** code on entering the TMA projection:

| Destination | Indicator | Code |
| --- | :---: | :---: |
| Curitiba – Afonso Pena | SBCT | **0220** |
| Curitiba – Bacacheri | SBBI | **0230** |
| Joinville | SBJV | **0240** |
| Other places | — | **2000** |

### Visual corridors (REA)

The 18 REAs of the TMA. Altitudes in feet (QNH), as **maximum / minimum**; a single altitude is mandatory. **⇄** is a two-way segment, with tracks as outbound / return; **→** is one-way.

| REA | Segment | Tracks | Altitudes | Class · contact |
| :---: | :--- | :---: | :---: | :--- |
| **PORTO AMAZONAS** | PORTO AMAZONAS ⇄ CONTENDA | 131° / 311° | 5500 / 4500 | D · APP-CT 119.950 |
| **VOÇOROCA** | CONTENDA ⇄ VOÇOROCA | 130° / 310° | 5500 / 4500 | D · APP-CT 119.950 |
| **SANEPAR** | CONTENDA ⇄ SANEPAR | 086° / 266° | 4500 / 4000 | D · APP-CT 119.950 |
| **RIO VERDE** | CONTENDA ⇄ CAMPO MAGRO | 033° / 213° | 5500 / 4500 | D · APP-CT 119.950 |
| **RIO BRANCO** | CAMPO MAGRO ⇄ RIO BRANCO | 051° / 231° | 5500 / 5000 | D · APP-CT 119.950 |
| **TUNAS** | RIO BRANCO ⇄ TUNAS | 064° / 244° | 6000 / 5500 | D · APP-CT 119.950 |
| **COLOMBO** | RIO BRANCO ⇄ COLOMBO | 144° / 324° | 5500 / 5000 | D · APP-CT 119.950 |
| **TAMANDARÉ** | RIO BRANCO ⇄ TAMANDARÉ | 177° / 357° | 5000 / 4800 | D · APP-CT 119.950 |
| **BARIGUI** | TAMANDARÉ ⇄ BARIGUI | 207° / 027° | 4600 / 4100 | D · APP-CT 119.950 |
| **CAMPO MAGRO** | CAMPO MAGRO ⇄ BARIGUI | 137° / 317° | 4600 / 4100 | D · APP-CT 119.950 |
| **JAZIDA** | JAZIDA ⇄ ITARETAMA | 115° / 295° | 6000 / 5000 | D · APP-CT 119.950 |
| **ITARETAMA** | ITARETAMA ⇄ RIO BRANCO | 175° / 355° | 5500 / 5000 | D · APP-CT 119.950 |
| **NORTE** | CAMPINA → IGREJA DA ROSEIRA | 289° | 4000 | G · TWR-BI 118.900 |
|  | IGREJA DA ROSEIRA → ATUBA | 238° | 4000 | G · TWR-BI 118.900 |
| **SUL** | ATUBA → CAMPINA | 079° | 4000 | G · TWR-BI 118.900 |
| **REPRESA** | IRAÍ ⇄ PEDREIRA | 109° / 289° | 4500 / 4000 | D · APP-CT 119.950 |
|  | PEDREIRA ⇄ MARUMBI | 109° / 289° | 5500 / 4800 | D · APP-CT 119.950 |
| **MARUMBI** | MARUMBI ⇄ TREVO 277 | 138° / 318° | 6500 / 5500 | D · APP-CT 119.950 |
| **SÃO FRANCISCO DO SUL** | GUARATUBA ⇄ SÃO FRANCISCO DO SUL | 193° / 013° | 3000 / 2000 | D · APP-CT 120.950 |
|  | SÃO FRANCISCO DO SUL ⇄ BARRA DO SUL | 217° / 037° | 3000 / 2000 | D · APP-CT 120.950 |
| **BARRA DO SUL** | BARRA DO SUL ⇄ BARRA VELHA | 224° / 044° | 3000 / 2000 | D · APP-CT 120.950 |

What each corridor does:

- **From the west and south**, everything converges on **CONTENDA**: PORTO AMAZONAS comes from the gate of the same name, VOÇOROCA from the Voçoroca dam, SANEPAR leads to the SANEPAR gate of the CTR, and RIO VERDE climbs north to CAMPO MAGRO.
- **From the north**, the hub is **RIO BRANCO** (Rio Branco do Sul): CAMPO MAGRO's RIO BRANCO corridor, ITARETAMA and, before it, JAZIDA from the JAZIDA gate to the northwest all arrive there; TUNAS leaves it for the TUNAS gate, and COLOMBO and TAMANDARÉ for the CTR gates. The SBR 594 (Santana Alto) restricted area lies near TUNAS.
- **BARIGUI** (from TAMANDARÉ) and **CAMPO MAGRO** (from CAMPO MAGRO) enter the CTR through the BARIGUI gate, Barigui Park, between 4100 and 4600 ft.
- **From the east**, **REPRESA** leaves the IRAÍ gate (Iraí reservoir), passes PEDREIRA and reaches MARUMBI, from where **MARUMBI** runs down to the TREVO 277 gate on the BR-277, towards the coast.
- **NORTE** and **SUL** are one-way, at a **mandatory 4000 ft**, and serve only the SBBI flight schools going to the SBR 595 (Capivari) and SBR 836 (Capivari Alto) training areas: SUL leaves the ATUBA gate for CAMPINA, and NORTE returns from CAMPINA via IGREJA DA ROSEIRA to ATUBA.
- **On the coast**, **SÃO FRANCISCO DO SUL** runs from GUARATUBA via SÃO FRANCISCO DO SUL to BARRA DO SUL, and **BARRA DO SUL** continues to BARRA VELHA, between 2000 and 3000 ft.

### Aerodrome gates

Entry to and exit from the Curitiba CTR and the Joinville area are **through the gates**, unless the APP clears otherwise:

| Aerodrome | REA gates (aeroplanes) | REH gates (helicopters) |
| :---: | :--- | :--- |
| **SBCT** | TAMANDARÉ · COLOMBO · BARIGUI · IRAÍ · SANEPAR | SANEPAR · BARRO PRETO · GUATUPÊ |
| **SBBI** | TAMANDARÉ · COLOMBO · BARIGUI · IRAÍ · SANEPAR · ATUBA (flight schools only, via NORTE and SUL) | ATUBA · IGREJA SANTA CÂNDIDA · PARQUE SÃO LOURENÇO · PRESÍDIO AHU |
| **SBJV** | GUARATUBA · TREVO BR-101 · BARRA DO SUL | — |

The GUATUPÊ gate (football pitch of the Guatupê Military Academy) is not part of any REH: it is the northeastern entry to SBCT, with Curitiba Tower clearance.

### Helicopters (REH)

The 7 REHs form the helicopter network over Curitiba, between **3500 and 4100 ft**, mostly over highways, avenues and parks. Their tracks are on the **Helicopter routes (REH)** layer of the [map](#map).

| REH | Segment | Altitudes | Class · contact |
| :---: | :--- | :---: | :--- |
| **ALFA** | BARIGUI ⇄ EXÉRCITO | 3800 / 3600 | G · FCA 123.450 |
|  | EXÉRCITO ⇄ GARAGEM | 3700 / 3500 | D · APP-CT 119.950 |
|  | GARAGEM ⇄ SANEPAR | 3700 / 3500 | D · APP-CT 119.950 |
|  | SANEPAR ⇄ BARRO PRETO | 3700 / 3500 | D · APP-CT 119.950 |
|  | BARRO PRETO ⇄ TREVO COLÔNIA MURICI | 3700 / 3500 | D · TWR-CT 118.150 |
|  | TREVO COLÔNIA MURICI ⇄ IGREJA GAMELAS | 3700 / 3500 | D · TWR-CT 118.150 |
|  | IGREJA GAMELAS ⇄ PEDÁGIO BR277 | 3800 / 3600 | D · TWR-CT 118.150 |
| **BRAVO** | EXÉRCITO ⇄ TAÇA | 3800 / 3600 | G · FCA 123.450 |
|  | TAÇA ⇄ B1 | 3800 / 3600 | D · TWR-CT 118.150 |
|  | B1 ⇄ B2 | 3800 / 3600 | D · TWR-CT 118.150 |
|  | B2 ⇄ B3 | 3800 / 3600 | D · TWR-CT 118.150 |
|  | B3 ⇄ SHOPPING ESTAÇÃO | 3800 / 3700 | D · APP-CT 119.950 |
|  | SHOPPING ESTAÇÃO ⇄ B4 | 3800 / 3700 | G · FCA 123.450 |
|  | B4 ⇄ BARIGUI | 3800 / 3700 | G · FCA 123.450 |
| **CHARLIE** | BARIGUI ⇄ MUSEU DO OLHO | 3900 / 3800 | G · FCA 123.450 |
|  | MUSEU DO OLHO ⇄ PRESÍDIO AHU | 3800 / 3700 | D · TWR-BI 118.900 |
| **DELTA** | BARIGUI ⇄ PARQUE TINGUI | 3800 / 3600 | G · FCA 123.450 |
|  | PARQUE TINGUI ⇄ PARQUE TANGUÁ | 3900 / 3700 | G · FCA 123.450 |
|  | PARQUE TANGUÁ ⇄ MUSEU DO OLHO | 4000 / 3900 | D · TWR-BI 118.900 |
|  | MUSEU DO OLHO ⇄ SHOPPING ESTAÇÃO | 3900 / 3700 | D · TWR-BI 118.900 |
| **ECHO** | ATUBA ⇄ ESTRADA DA GRACIOSA | 3700 / 3500 | D · TWR-BI 118.900 |
|  | ESTRADA DA GRACIOSA ⇄ ALPHAVILLE | 3700 / 3600 | D · TWR-BI 118.900 |
|  | ALPHAVILLE ⇄ CLUBE PANORÂMICO | 3700 / 3600 | D · APP-CT 119.950 |
|  | CLUBE PANORÂMICO ⇄ TREVO PIRAQUARA | 3800 / 3600 | D · APP-CT 119.950 |
|  | TREVO PIRAQUARA ⇄ PEDÁGIO BR277 | 3800 / 3600 | D · TWR-CT 118.150 |
| **FOXTROT** | PARQUE SÃO LOURENÇO ⇄ F1 | 3900 / 3700 | D · TWR-BI 118.900 |
|  | F1 ⇄ F2 | 3900 / 3700 | D · TWR-BI 118.900 |
|  | F2 ⇄ TAMANDARÉ | 3900 / 3800 | D · TWR-BI 118.900 |
| **GOLF** | IGREJA SANTA CÂNDIDA ⇄ G1 | 3900 / 3700 | D · TWR-BI 118.900 |
|  | G1 ⇄ G2 | 3900 / 3700 | D · TWR-BI 118.900 |
|  | G2 ⇄ COLOMBO | 4100 / 3900 | D · TWR-BI 118.900 |

- **Junctions:** BARIGUI joins ALFA, BRAVO, CHARLIE and DELTA; EXÉRCITO joins ALFA and BRAVO; MUSEU DO OLHO, CHARLIE and DELTA.
- **Reference on the left, mandatory:** the REH's highway, avenue or street stays on the pilot's left and within the lateral limits.
- **Speed** must be between **70 and 90 kt** on the REHs.
- **DELTA** is reserved for authorised sightseeing flights.
- **SBCT:** through the SANEPAR or BARRO PRETO gates (ALFA), at the 3600 ft circuit altitude, with Curitiba Tower clearance. **SBBI:** through the PRESÍDIO AHU (CHARLIE, reporting MUSEU DO OLHO first), ATUBA (ECHO), PARQUE SÃO LOURENÇO (FOXTROT) and IGREJA SANTA CÂNDIDA (GOLF) gates, with Bacacheri Tower clearance.
- **In the CTR**, helicopters call before entering; ATC sets the REHs, the separation from IFR and the transponder code (0101 to 0113). They may be told to hold, slow down or deviate. Departures from heliports inside the CTR make contact while still on the ground or up to 50 ft.
- **Off the REHs**, helicopters take the shortest way to the nearest REH, without crossing the SBCT and SBBI runway alignment or IFR tracks without clearance.
- **Transponder:** without contact with the APP, in class G below the TMA, **0100**; parked on a heliport in the CTR, **STANDBY**.
- News, power-line inspection and sightseeing flights that may affect SBCT and SBBI operations are coordinated with the APP in advance.

### Other rules

- AFIL flight plans are not accepted.
- With a full flight plan and a change from VFR to IFR (Z plan), wait for the APP clearance, keeping to the corridor altitudes.
- On busy dates or with temporary restricted areas active, the REAs and REHs may be suspended or have their class changed by NOTAM.

### Phraseology

On contact, the pilot gives registration, origin and destination, corridor, position, altitude and estimate for the next point[^aic3423]. Brazilian VFR traffic usually calls in Portuguese. Arrival at SBBI from the northwest:

```
Controle Curitiba, PR-MWN, de Ponta Grossa para Bacacheri, corredor JAZIDA, vertical JAZIDA, 5000 pés, estima ITARETAMA aos 10.
```

Helicopter entering the CTR, with registration, route, position, altitude and direction:

```
Torre Curitiba, PP-HMW, REH ALFA, posição EXÉRCITO, 3600 pés, proa SANEPAR.
```

Class G coordination (FCA 123.450 in the real world; UNICOM on VATSIM):

```
Tráfego Barigui, PP-HMW, REH DELTA, PARQUE TINGUI, 3700 pés, proa PARQUE TANGUÁ.
```

## :material-note-text-outline: Remarks

- Curitiba 1 is class A between FL145 and FL195 and class C between 5500 FT and FL145.
- SBBI (Bacacheri) lies in the Bacacheri FIZ (class G), inside the Curitiba CTR.
- Joinville has no CTR: the AIP has the Joinville 1 and 2 FIZ (class G, Joinville Radio).
- Volumes and map follow AIP AMDT AIRAC 2612A1 (26 NOV 2026).

---

Back to the Curitiba FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.
[^aic3423]: [AIC N 34/23](https://publicacoes.decea.mil.br/publicacao/aic-n-34-23){ target="_blank" }, items 3 to 6 and Annexes A and B.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude].
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
    .reh-rotulo { background: #0f766e; color: #fff; border: 0; font-weight: 600; font-size: 10px; padding: 0 4px; box-shadow: none }
    .reh-rotulo::before { display: none }
    .reh-zoom-baixo .reh-rotulo { display: none }
    .rea-zoom-baixo .rea-rotulo, .rea-zoom-medio .rea-rotulo-trecho { display: none }
    .rea-seta span { display: block; width: 16px; height: 16px; line-height: 16px; text-align: center; color: #0284c7; font-size: 15px; text-shadow: 0 0 2px #fff, 0 0 2px #fff }
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
    .mapa-legenda .rea-linha.g { border-top: 3px dashed #0284c7 }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "G": "#a3a3a3", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWT", "nome": "Curitiba 1", "posicao": "SBWT_APP", "freq": "119.950", "lim": "5500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-50.001111, -25.630278], [-49.861111, -25.279722], [-49.445833, -24.8225], [-48.934167, -24.8075], [-48.548889, -24.995833], [-48.264167, -24.98], [-48.209444, -25.4225], [-48.157222, -26.01], [-48.511944, -26.261111], [-48.568056, -26.495556], [-49.226944, -26.895278], [-49.617778, -26.261111]]},
    {"tipo": "tma", "id": "SBWT", "nome": "Curitiba 2", "posicao": "SBWT_APP", "freq": "119.950", "lim": "4500 FT – 5500 FT", "classe": "C", "link": "", "contorno": [[-49.0575, -25.875], [-49.566111, -25.699167], [-49.475833, -25.358611], [-49.381111, -25.218056], [-49.341111, -25.176111], [-49.216667, -25.192778], [-48.915278, -25.397222]]},
    {"tipo": "ctr", "id": "SBWT", "nome": "Curitiba CTR", "posicao": "SBCT_TWR", "freq": "118.150", "lim": "GND – 4500 FT", "classe": "D", "link": "", "contorno": [[-49.222778, -25.292222], [-49.175833, -25.398333], [-49.104444, -25.415833], [-49.104722, -25.492778], [-49.013611, -25.495278], [-49.016389, -25.574444], [-49.029722, -25.600278], [-49.094444, -25.659722], [-49.195278, -25.569722], [-49.273611, -25.5675], [-49.271389, -25.501667], [-49.300556, -25.475556], [-49.253056, -25.436389], [-49.305556, -25.324444]]},
    {"tipo": "ctr", "id": "SBWT", "nome": "Bacacheri FIZ", "posicao": "SBBI_TWR", "freq": "118.900", "lim": "GND – 4500 FT", "classe": "G", "link": "", "contorno": [[-49.222778, -25.292222], [-49.175833, -25.4], [-49.166111, -25.491111], [-49.253056, -25.436389], [-49.305556, -25.324444]]},
    {"tipo": "ctr", "id": "SBWT", "nome": "Joinville 2 FIZ", "posicao": "SBJV_R_TWR", "freq": "118.000", "lim": "3000 FT – 5500 FT", "classe": "G", "link": "", "contorno": [[-48.748333, -26.474167], [-48.488333, -26.183611], [-48.458889, -26.101944], [-48.608889, -25.917778], [-48.748889, -25.8425], [-48.853333, -25.992778], [-49.037222, -26.265556]]},
    {"tipo": "ctr", "id": "SBWT", "nome": "Joinville 1 FIZ", "posicao": "SBJV_R_TWR", "freq": "118.000", "lim": "GND – 3000 FT", "classe": "G", "link": "", "contorno": [[-48.853333, -25.992778], [-48.549722, -26.208333], [-48.573333, -26.278889], [-48.69, -26.409167], [-48.968333, -26.263056], [-48.923611, -26.097222]]}
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

// Corredores visuais (REA), REH e portões da AIC N 34/23 (Anexos A e B); pontos das cartas CCV REA/REH WT
const reaTrechos = [{"rota": "PORTO AMAZONAS", "de": "PORTO AMAZONAS", "para": "CONTENDA", "rumo": "131°", "rumoVolta": "311°", "max": "5500", "min": "4500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "VOÇOROCA", "de": "CONTENDA", "para": "VOÇOROCA", "rumo": "130°", "rumoVolta": "310°", "max": "5500", "min": "4500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "SANEPAR", "de": "CONTENDA", "para": "SANEPAR", "rumo": "086°", "rumoVolta": "266°", "max": "4500", "min": "4000", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "RIO VERDE", "de": "CONTENDA", "para": "CAMPO MAGRO", "rumo": "033°", "rumoVolta": "213°", "max": "5500", "min": "4500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "RIO BRANCO", "de": "CAMPO MAGRO", "para": "RIO BRANCO", "rumo": "051°", "rumoVolta": "231°", "max": "5500", "min": "5000", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "TUNAS", "de": "RIO BRANCO", "para": "TUNAS", "rumo": "064°", "rumoVolta": "244°", "max": "6000", "min": "5500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "COLOMBO", "de": "RIO BRANCO", "para": "COLOMBO", "rumo": "144°", "rumoVolta": "324°", "max": "5500", "min": "5000", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "TAMANDARÉ", "de": "RIO BRANCO", "para": "TAMANDARÉ", "rumo": "177°", "rumoVolta": "357°", "max": "5000", "min": "4800", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "BARIGUI", "de": "TAMANDARÉ", "para": "BARIGUI", "rumo": "207°", "rumoVolta": "027°", "max": "4600", "min": "4100", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "CAMPO MAGRO", "de": "CAMPO MAGRO", "para": "BARIGUI", "rumo": "137°", "rumoVolta": "317°", "max": "4600", "min": "4100", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "JAZIDA", "de": "JAZIDA", "para": "ITARETAMA", "rumo": "115°", "rumoVolta": "295°", "max": "6000", "min": "5000", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "ITARETAMA", "de": "ITARETAMA", "para": "RIO BRANCO", "rumo": "175°", "rumoVolta": "355°", "max": "5500", "min": "5000", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "NORTE", "de": "CAMPINA", "para": "IGREJA DA ROSEIRA", "rumo": "289°", "rumoVolta": null, "max": "4000", "min": "4000", "classe": "G", "esp": "G · TWR-BI 118.900"}, {"rota": "NORTE", "de": "IGREJA DA ROSEIRA", "para": "ATUBA", "rumo": "238°", "rumoVolta": null, "max": "4000", "min": "4000", "classe": "G", "esp": "G · TWR-BI 118.900"}, {"rota": "SUL", "de": "ATUBA", "para": "CAMPINA", "rumo": "079°", "rumoVolta": null, "max": "4000", "min": "4000", "classe": "G", "esp": "G · TWR-BI 118.900"}, {"rota": "REPRESA", "de": "IRAÍ", "para": "PEDREIRA", "rumo": "109°", "rumoVolta": "289°", "max": "4500", "min": "4000", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "REPRESA", "de": "PEDREIRA", "para": "MARUMBI", "rumo": "109°", "rumoVolta": "289°", "max": "5500", "min": "4800", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "MARUMBI", "de": "MARUMBI", "para": "TREVO 277", "rumo": "138°", "rumoVolta": "318°", "max": "6500", "min": "5500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "SÃO FRANCISCO DO SUL", "de": "GUARATUBA", "para": "SÃO FRANCISCO DO SUL", "rumo": "193°", "rumoVolta": "013°", "max": "3000", "min": "2000", "classe": "D", "esp": "D · APP-CT 120.950"}, {"rota": "SÃO FRANCISCO DO SUL", "de": "SÃO FRANCISCO DO SUL", "para": "BARRA DO SUL", "rumo": "217°", "rumoVolta": "037°", "max": "3000", "min": "2000", "classe": "D", "esp": "D · APP-CT 120.950"}, {"rota": "BARRA DO SUL", "de": "BARRA DO SUL", "para": "BARRA VELHA", "rumo": "224°", "rumoVolta": "044°", "max": "3000", "min": "2000", "classe": "D", "esp": "D · APP-CT 120.950"}];
const reaPontos = {"ATUBA": [-49.2055, -25.388667], "BARIGUI": [-49.312667, -25.4285], "BARRA VELHA": [-48.682667, -26.629333], "CAMPINA": [-49.052833, -25.301333], "COLOMBO": [-49.222833, -25.292167], "GUARATUBA": [-48.564667, -25.891167], "IRAÍ": [-49.097333, -25.422333], "JAZIDA": [-49.706667, -25.073], "PORTO AMAZONAS": [-49.895667, -25.5465], "SANEPAR": [-49.2455, -25.563333], "TREVO 277": [-48.614, -25.565667], "TUNAS": [-49.080667, -24.972333], "VOÇOROCA": [-49.047333, -25.847333], "BARRA DO SUL": [-48.600167, -26.458667], "CAMPO MAGRO": [-49.447333, -25.365667], "CONTENDA": [-49.530667, -25.680667], "IGREJA DA ROSEIRA": [-49.132833, -25.302833], "ITARETAMA": [-49.405667, -25.097333], "MARUMBI": [-48.919, -25.419833], "PEDREIRA": [-49.0235, -25.421167], "RIO BRANCO": [-49.347333, -25.217333], "SÃO FRANCISCO DO SUL": [-48.5185, -26.209833], "TAMANDARÉ": [-49.299333, -25.320667]};
const rehTrechos = [{"rota": "ALFA", "de": "BARIGUI", "para": "EXÉRCITO", "max": "3800", "min": "3600", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "ALFA", "de": "EXÉRCITO", "para": "GARAGEM", "max": "3700", "min": "3500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "ALFA", "de": "GARAGEM", "para": "SANEPAR", "max": "3700", "min": "3500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "ALFA", "de": "SANEPAR", "para": "BARRO PRETO", "max": "3700", "min": "3500", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "ALFA", "de": "BARRO PRETO", "para": "TREVO COLÔNIA MURICI", "max": "3700", "min": "3500", "classe": "D", "esp": "D · TWR-CT 118.150"}, {"rota": "ALFA", "de": "TREVO COLÔNIA MURICI", "para": "IGREJA GAMELAS", "max": "3700", "min": "3500", "classe": "D", "esp": "D · TWR-CT 118.150"}, {"rota": "ALFA", "de": "IGREJA GAMELAS", "para": "PEDÁGIO BR277", "max": "3800", "min": "3600", "classe": "D", "esp": "D · TWR-CT 118.150"}, {"rota": "BRAVO", "de": "EXÉRCITO", "para": "TAÇA", "max": "3800", "min": "3600", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "BRAVO", "de": "TAÇA", "para": "B1", "max": "3800", "min": "3600", "classe": "D", "esp": "D · TWR-CT 118.150"}, {"rota": "BRAVO", "de": "B1", "para": "B2", "max": "3800", "min": "3600", "classe": "D", "esp": "D · TWR-CT 118.150"}, {"rota": "BRAVO", "de": "B2", "para": "B3", "max": "3800", "min": "3600", "classe": "D", "esp": "D · TWR-CT 118.150"}, {"rota": "BRAVO", "de": "B3", "para": "SHOPPING ESTAÇÃO", "max": "3800", "min": "3700", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "BRAVO", "de": "SHOPPING ESTAÇÃO", "para": "B4", "max": "3800", "min": "3700", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "BRAVO", "de": "B4", "para": "BARIGUI", "max": "3800", "min": "3700", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "CHARLIE", "de": "BARIGUI", "para": "MUSEU DO OLHO", "max": "3900", "min": "3800", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "CHARLIE", "de": "MUSEU DO OLHO", "para": "PRESÍDIO AHU", "max": "3800", "min": "3700", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "DELTA", "de": "BARIGUI", "para": "PARQUE TINGUI", "max": "3800", "min": "3600", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "DELTA", "de": "PARQUE TINGUI", "para": "PARQUE TANGUÁ", "max": "3900", "min": "3700", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "DELTA", "de": "PARQUE TANGUÁ", "para": "MUSEU DO OLHO", "max": "4000", "min": "3900", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "DELTA", "de": "MUSEU DO OLHO", "para": "SHOPPING ESTAÇÃO", "max": "3900", "min": "3700", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "ECHO", "de": "ATUBA", "para": "ESTRADA DA GRACIOSA", "max": "3700", "min": "3500", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "ECHO", "de": "ESTRADA DA GRACIOSA", "para": "ALPHAVILLE", "max": "3700", "min": "3600", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "ECHO", "de": "ALPHAVILLE", "para": "CLUBE PANORÂMICO", "max": "3700", "min": "3600", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "ECHO", "de": "CLUBE PANORÂMICO", "para": "TREVO PIRAQUARA", "max": "3800", "min": "3600", "classe": "D", "esp": "D · APP-CT 119.950"}, {"rota": "ECHO", "de": "TREVO PIRAQUARA", "para": "PEDÁGIO BR277", "max": "3800", "min": "3600", "classe": "D", "esp": "D · TWR-CT 118.150"}, {"rota": "FOXTROT", "de": "PARQUE SÃO LOURENÇO", "para": "F1", "max": "3900", "min": "3700", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "FOXTROT", "de": "F1", "para": "F2", "max": "3900", "min": "3700", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "FOXTROT", "de": "F2", "para": "TAMANDARÉ", "max": "3900", "min": "3800", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "GOLF", "de": "IGREJA SANTA CÂNDIDA", "para": "G1", "max": "3900", "min": "3700", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "GOLF", "de": "G1", "para": "G2", "max": "3900", "min": "3700", "classe": "D", "esp": "D · TWR-BI 118.900"}, {"rota": "GOLF", "de": "G2", "para": "COLOMBO", "max": "4100", "min": "3900", "classe": "D", "esp": "D · TWR-BI 118.900"}];
const rehPontos = {"BARIGUI": [-49.312778, -25.428333], "EXÉRCITO": [-49.3, -25.531667], "GARAGEM": [-49.289444, -25.547222], "SANEPAR": [-49.245556, -25.563333], "BARRO PRETO": [-49.176667, -25.583333], "TREVO COLÔNIA MURICI": [-49.123611, -25.589444], "IGREJA GAMELAS": [-49.095833, -25.594444], "PEDÁGIO BR277": [-49.036667, -25.551667], "TAÇA": [-49.289167, -25.513056], "B1": [-49.253611, -25.468611], "B2": [-49.243056, -25.453056], "B3": [-49.251111, -25.442222], "SHOPPING ESTAÇÃO": [-49.267222, -25.438056], "B4": [-49.296944, -25.446667], "MUSEU DO OLHO": [-49.266667, -25.409722], "PRESÍDIO AHU": [-49.255833, -25.405], "PARQUE TINGUI": [-49.304444, -25.387222], "PARQUE TANGUÁ": [-49.284722, -25.379444], "ATUBA": [-49.205556, -25.388611], "ESTRADA DA GRACIOSA": [-49.1825, -25.393333], "ALPHAVILLE": [-49.161111, -25.396944], "CLUBE PANORÂMICO": [-49.133056, -25.421111], "TREVO PIRAQUARA": [-49.088889, -25.461944], "PARQUE SÃO LOURENÇO": [-49.266389, -25.384722], "F1": [-49.281389, -25.36], "F2": [-49.283611, -25.338889], "TAMANDARÉ": [-49.299444, -25.320556], "IGREJA SANTA CÂNDIDA": [-49.222778, -25.373333], "G1": [-49.221111, -25.347778], "G2": [-49.219722, -25.320556], "COLOMBO": [-49.222778, -25.292222]};
const portoes = {"REA": {"TAMANDARÉ": "SBCT/SBBI", "COLOMBO": "SBCT/SBBI", "BARIGUI": "SBCT/SBBI", "IRAÍ": "SBCT/SBBI", "SANEPAR": "SBCT/SBBI", "ATUBA": "SBBI", "GUARATUBA": "SBJV", "TREVO 277": "", "BARRA VELHA": "", "PORTO AMAZONAS": "", "JAZIDA": "", "TUNAS": "", "VOÇOROCA": "", "CAMPINA": ""}, "REH": {"ATUBA": "SBBI", "IGREJA SANTA CÂNDIDA": "SBBI", "PARQUE SÃO LOURENÇO": "SBBI", "PRESÍDIO AHU": "SBBI", "BARRO PRETO": "SBCT", "SANEPAR": "SBCT"}};
var corD = '#c026d3', corG = '#0284c7', corReh = '#0f766e';
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
    var portao = n in portoes.REA;
    L.circleMarker(paraLatLng(reaPontos[n]), portao ?
        { radius: 5, color: '#0f172a', weight: 2, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 3.5, color: '#334155', weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Gate ' + n + (portoes.REA[n] ? ' (' + portoes.REA[n] + ')' : '') : n).addTo(grupoRea);
});

var grupoReh = L.featureGroup();
var rehRotuladas = {};
rehTrechos.forEach(function (t) {
    var linha = [paraLatLng(rehPontos[t.de]), paraLatLng(rehPontos[t.para])];
    var g = t.classe === 'G';
    L.polyline(linha, { color: corReh, weight: 2.5, opacity: 0.9, dashArray: g ? '5 4' : null })
        .bindPopup('<b>REH ' + t.rota + '</b><br>' + t.de + ' ⇄ ' + t.para + '<br>Max. / min. (ft): ' + t.max + ' / ' + t.min + '<br>' + t.esp)
        .addTo(grupoReh);
    // Um rótulo por REH, no primeiro trecho, só com zoom maior
    if (!rehRotuladas[t.rota]) {
        rehRotuladas[t.rota] = true;
        L.marker([(linha[0][0] + linha[1][0]) / 2, (linha[0][1] + linha[1][1]) / 2], { opacity: 0, interactive: false, icon: L.divIcon({ className: '', iconSize: [0, 0] }) })
            .bindTooltip(t.rota, { permanent: true, direction: 'center', className: 'reh-rotulo' })
            .addTo(grupoReh);
    }
});
Object.keys(rehPontos).forEach(function (n) {
    var portao = portoes.REH[n];
    L.circleMarker(paraLatLng(rehPontos[n]), portao ?
        { radius: 4, color: '#0f172a', weight: 1.5, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 2.5, color: corReh, weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Gate ' + n + ' (' + portao + ')' : n).addTo(grupoReh);
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
    "Visual corridors (REA)": grupoRea,
    "Helicopter routes (REH)": grupoReh
}).addTo(mapa);

// Rótulos dos corredores só com zoom suficiente para não embolar
function detalheRea() {
    elemento.classList.toggle('rea-zoom-baixo', mapa.getZoom() < 8);
    elemento.classList.toggle('rea-zoom-medio', mapa.getZoom() < 10);
    elemento.classList.toggle('reh-zoom-baixo', mapa.getZoom() < 11);
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
