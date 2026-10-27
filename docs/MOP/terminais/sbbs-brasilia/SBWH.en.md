---
title: SBWH - Belo Horizonte
tags:
  - Terminal
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Belo Horizonte TMA |
| **Position** | `SBWH_APP` |
| **Callsign** | Belo Horizonte Control |
| **Frequency** | **129.100** MHz[^pacote] |
| **ATS surveillance** | Radar |
| **Aerodromes in the TMA** | [SBCF](../../aerodromos/sbbs-brasilia/twr/SBCF.en.md), [SBBH](../../aerodromos/sbbs-brasilia/twr/SBBH.en.md), [SBLS](../../aerodromos/sbbs-brasilia/afis/SBLS.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Use the tabs above: **Aeronautical Charts** shows the TMA charts, **Visual Charts** shows the visual charts (REA/REH) from AISWEB, **Weather** shows a weather map of the area and **VATSIM Traffic** opens the traffic at the main aerodrome (SBCF).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWH?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Visual Charts"
    <div class="ccv-viewer" data-lang="en">
    <ul class="ccv-lista">
    <li><a href="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wh1-belo-horizonte_rea_20261126.pdf" target="_blank" rel="noopener">CCV REA WH1-Belo Horizonte</a></li>
    <li><a href="https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wh2-belo-horizonte_reh_20261126.pdf" target="_blank" rel="noopener">CCV REH WH2-Belo Horizonte</a></li>
    </ul>
    </div>

    Source: [AISWEB](https://aisweb.decea.mil.br/?i=cartas){ target="_blank" }.

=== ":material-weather-partly-cloudy: Weather"
    <div class="tma-meteo" data-lat="-19.750" data-lon="-43.946" data-zoom="8" data-lang="en"></div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBCF){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

The **Visual corridors (REA)** layer shows the 25 REAs and the aerodrome gates. Solid magenta: **recommended** route (class D, APP clearance before entering); dashed blue: **mandatory** route in class G, with coordination on an FCA. Click a segment to see the tracks, altitudes and contact. Details in [Visual corridors (REA)](#visual-corridors-rea).

The **Helicopter routes (REH)** layer (23 routes) is off by default. Solid lines are class D segments, dashed lines class G, and orange segments are recommended; names show up when zoomed in. See [Helicopters (REH)](#helicopters-reh).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Belo Horizonte 2 | 4100 FT – 5500 FT | <span class="classe-badge classe-c">C</span> |
| Belo Horizonte 1 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Belo Horizonte CTR | GND – 5500 FT | <span class="classe-badge classe-c">C</span> |
| Confins CTR | GND – 5500 FT | <span class="classe-badge classe-d">D</span> |
| Belo Horizonte ATZ (Pampulha) | GND – 4500 FT | — |
| Confins ATZ | GND – 4500 FT | — |
| Lagoa Santa ATZ | GND – 4500 FT | — |

## :material-view-grid-outline: APP Sectorization

With the TMA-BH Project, the AIP splits Belo Horizonte APP into nine sectors[^amdt]. **Belo Horizonte 1** is the union of high sectors 01 to 04; sectors 05 to 08 are the **finals** below them, around SBCF and SBLS (up to FL110) and SBBH (up to 9000 ft). Turn on the **APP sectors (AIP)** layer on the map to see them.

In the package the APP **has no sectors**: `SBWH_APP` (**129.100**) covers all of them. The sectorization helps to understand the flows and finals, not to split positions on VATSIM.

Pick an area in the list: the whole TMA or an AIP sector. The area is filled, with its vertical limits below the name; the rest of the TMA is grey. Hatched: the part of the sector that belongs to a final below the final's ceiling.

<div class="setor-viewer" data-lang="en" markdown="block">
<figure data-grupo="total" data-titulo="SBWH_APP" data-info="129.100 · whole TMA" markdown="span">
  ![SBWH_APP: the whole Belo Horizonte TMA](img/sbwh-comb-app.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="01" data-info="5500 FT – FL195" markdown="span">
  ![Belo Horizonte APP sector 01, 5500 FT – FL195](img/sbwh-setor-01.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="02" data-info="5500 FT – FL195" markdown="span">
  ![Belo Horizonte APP sector 02, 5500 FT – FL195](img/sbwh-setor-02.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="03A" data-info="5500 FT – FL195" markdown="span">
  ![Belo Horizonte APP sector 03A, 5500 FT – FL195](img/sbwh-setor-03a.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="03B" data-info="5500 FT – FL195" markdown="span">
  ![Belo Horizonte APP sector 03B, 5500 FT – FL195](img/sbwh-setor-03b.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="04" data-info="5500 FT – FL195" markdown="span">
  ![Belo Horizonte APP sector 04, 5500 FT – FL195](img/sbwh-setor-04.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="05" data-info="5500 FT – FL110" markdown="span">
  ![Belo Horizonte APP sector 05, 5500 FT – FL110](img/sbwh-setor-05.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="06" data-info="5500 FT – FL110" markdown="span">
  ![Belo Horizonte APP sector 06, 5500 FT – FL110](img/sbwh-setor-06.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="07" data-info="5500 FT – 9000 FT" markdown="span">
  ![Belo Horizonte APP sector 07, 5500 FT – 9000 FT](img/sbwh-setor-07.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="08" data-info="5500 FT – 9000 FT" markdown="span">
  ![Belo Horizonte APP sector 08, 5500 FT – 9000 FT](img/sbwh-setor-08.svg){ loading=lazy }
</figure>

</div>

| Sector | Limits | Role |
| :---: | --- | --- |
| **01** | 5500 FT – FL195 | **High sector** west, from Pará de Minas to Itaúna |
| **02** | 5500 FT – FL195 | **High sector** north and northwest, from Sete Lagoas to Paraopeba |
| **03A** | 5500 FT – FL195 | **High sector** northeast, from Serra do Cipó to SBCF |
| **03B** | 5500 FT – FL195 | **High sector** east, from Itabira to Santa Bárbara |
| **04** | 5500 FT – FL195 | **High sector** south and over SBBH, down to the Iron Quadrangle |
| **05** | 5500 FT – FL110 | **SBCF final to the north and northwest (RWY 16)** |
| **06** | 5500 FT – FL110 | **SBCF final to the south and southeast (RWY 34) and SBLS** |
| **07** | 5500 FT – 9000 FT | **SBBH final to the west and northwest (RWY 13)** |
| **08** | 5500 FT – 9000 FT | **SBBH final to the southeast (RWY 31)** |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWH_APP** | `WH` | Belo Horizonte Control | **129.100** |  |
| **SBBH_TWR** | `TBH` | Belo Horizonte Tower | **118.000** |  |
| **SBCF_TWR** | `TCF` | Confins Tower | **118.200** |  |
| **SBLS_R_TWR** | `RLS` | Lagoa Santa Radio | **122.850** |  |

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
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_NE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_SE_CTR</span>"]:::grpctr
        p1["SBBS_E_CTR"]:::ctr
        p2["SBWH_APP"]:::app
        p3["SBBH_TWR"]:::twr
        p4["SBCF_TWR"]:::twr
        p5["SBLS_R_TWR"]:::twr
        a0(["Belo Horizonte TMA"]):::esp --> p2
        a1(["Belo Horizonte CTR<br>Belo Horizonte ATZ (Pampulha)"]):::esp --> p3
        a2(["Confins CTR<br>Confins ATZ"]):::esp --> p4
        a3(["Lagoa Santa ATZ"]):::esp --> p5
        g0 --> p0
        p1 --> g0
        p2 --> p1
        p3 --> p2
        p4 --> p2
        p5 --> p2
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
        classDef grpctr fill:none,stroke:#8a56c9,stroke-dasharray:4 3
    ```

## :material-airplane: VFR circulation

!!! abstract "Visual navigation documents"
    - **Circular:** [AIC N 27/26 – Circulação VFR na TMA-BH](https://publicacoes.decea.mil.br/publicacao/aic-n-2726){ target="_blank" } (replaces AIC N 20/24)
    - **Circular:** [AIC N 25/26 – Projeto TMA BH: alterações no espaço aéreo da TMA-BH e procedimentos em aeroportos associados](https://publicacoes.decea.mil.br/publicacao/aic-n-2526){ target="_blank" }
    - **Visual chart – Aircraft routes (REA):** [CCV REA WH1-Belo Horizonte](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wh1-belo-horizonte_rea_20261126.pdf){ target="_blank" }
    - **Visual chart – Helicopter routes (REH):** [CCV REH WH2-Belo Horizonte](https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wh2-belo-horizonte_reh_20261126.pdf){ target="_blank" }

    The charts are embedded in the **Visual Charts** tab under **Useful Information**. The data in this section comes from AIC N 27/26[^aic2726].

### TMA layers and who handles VFR

| Airspace | Limits | Class | VFR |
| --- | --- | :---: | --- |
| **Belo Horizonte 1** | 5500 FT – FL195 | <span class="classe-badge classe-c">C</span> up to FL145, <span class="classe-badge classe-a">A</span> above | Above 5500 ft, only inside the REAs (or with APP clearance) |
| **Belo Horizonte 2** | 4100 FT – 5500 FT | <span class="classe-badge classe-c">C</span> | On the REAs and REHs |
| **Belo Horizonte CTR** | GND – 5500 FT | <span class="classe-badge classe-c">C</span> | On the REAs and REHs; in and out through the gates |
| **Confins CTR** | GND – 5500 FT | <span class="classe-badge classe-d">D</span> | On the REAs and REHs; off the REHs, only after calling the APP |
| TMA projection | Below Belo Horizonte 1, outside the CTRs and ATZs | <span class="classe-badge classe-g">G</span> | Up to **5500 ft**, except on corridors that publish another altitude; coordination on an FCA |

- **Corridors have their own class:** each REA and REH segment has the corridor's class, not the class of the volume it crosses. There are two kinds of REA:
    - **Recommended** (class D): ALFA to JULIET, close to the aerodromes. The pilot calls the APP **before entering** and enters only when cleared.
    - **Mandatory** (class G): KILO to YANKEE, around the edge. Coordination on an FCA, no ATS surveillance; the APP may just be monitored.
- **In the real world**, VFR traffic talks to Belo Horizonte APP on **120.200** (primary) or **128.550** (secondary), which also give FIS and QNH.
- **In the package** there is only `SBWH_APP` (**129.100**), which handles all VFR traffic on the controlled REAs and REHs. Pilots call the position that is **online**, not the real-world frequency. Without the APP, the next position in the [coverage](#top-down-coverage) takes over.
- On class D REAs and REHs, the APP separates **IFR from VFR** and gives **traffic information** between VFR flights. Class G segments have no surveillance service.

### General VFR rules

- **Corridors are mandatory above 5500 ft:** VFR traffic above 5500 ft stays inside the REAs unless the APP clears otherwise. In the TMA projection (class G), flying above 5500 ft is prohibited outside the corridors that publish another altitude.
- **Keep right:** aeroplanes and helicopters fly to the **right** of the corridor axis, keeping the visual references on the left. All REAs are two-way, except ALFA and CHARLIE, whose direction depends on the SBBH runway ([flow reversal](#flow-reversal-at-sbbh)).
- **Width:** REAs are **3 NM** wide (1.5 NM each side); ALFA between CLUBE and INTERSEÇÃO and the whole of CHARLIE are **1 NM**; REHs are **0.28 NM** (250 m each side).
- **Helicopters** may use the REAs if they meet their requirements. **Aeroplanes do not use REHs.**
- **Altitudes:** the maximum separates VFR from the IFR traffic above and must be respected in controlled airspace. The minimum is the obstacle clearance altitude of the segment; below it, the pilot is responsible. Altitude changes always stay within the corridor's limits.
- **Reports:** when crossing a gate or position, the pilot reports on the frequency of the ATC unit or FCA for that segment.
- **Flight plan:** departures from a controlled aerodrome put `REA` in item 15 and the corridors in item 18 (e.g. `ALFA, BRAVO, OSCAR`). Traffic from an aerodrome without an ATS unit tells the APP which REAs or REHs it will use before entering controlled airspace.
- **Holding:** the APP may hold VFR traffic over REA and REH visual references to space out entries into the CTRs and the TMA.
- **IMC:** when VMC can no longer be kept, aeroplanes return and land at the departure aerodrome or the nearest one, or ask the APP to change to IFR. A helicopter on a class D REH **stops in a hover** and tells the APP at once.
- **QNH:** SBBH ATIS (**127.450**) or SBCF ATIS (**127.850**); without ATIS, ask the APP.
- **Transponder** on (mode A/C or S) and **VHF radio** are mandatory on the REAs and REHs and throughout the TMA projection. Landing lights on is recommended.

Without an ATC code, VFR traffic from outside the TMA or from an aerodrome without an ATS unit squawks the destination's code:

| Destination | Code |
| --- | :---: |
| SBBH | **2011** |
| SBCF | **2012** |
| SBLS | **2013** |
| Other aerodromes in the Belo Horizonte and Confins CTRs | **2014** |
| Training at SNLG | **0300** |
| Helicopters in class G only (including class G REAs and REHs) | **0100** |
| Other cases | **2000** |

### Visual corridors (REA)

The 25 REAs of the TMA. Altitudes in feet (QNH), as **maximum / minimum**; in controlled airspace the maximum must be respected. Tracks are given for each direction. Class D: **recommended** route, APP clearance before entering. Class G: **mandatory** route, with coordination on the FCA.

| REA | Segment | Tracks | Altitudes | Class · contact |
| :---: | :--- | :---: | :--- | :--- |
| **ALFA** | SINUOSO ⇄ FLORES | 128° / 308° | 4500 / 4400 | D · APP-BH 120.200 |
|  | FLORES ⇄ CLUBE | 109° / 289° | 4500 / 4300 | D · APP-BH 120.200 |
|  | CLUBE ⇄ INTERSEÇÃO | 086° / 266° | 4500 / 4300 | D · APP-BH 120.200 |
| **BRAVO** | IBIRITÉ ⇄ CLUBE | 023° / 203° | 5600 / 4500 | D · APP-BH 120.200 |
| **CHARLIE** | IBIRITÉ ⇄ VALLOUREC | 068° / 248° | 5600 / 4600 | D · APP-BH 120.200 |
|  | VALLOUREC ⇄ PAZ | 052° / 232° | 5000 / 4500 | D · APP-BH 120.200 |
| **DELTA** | MINA ⇄ SÍTIOS | 093° / 273° | 4900 / 4700 | D · APP-BH 120.200 |
|  | SÍTIOS ⇄ UNIÃO | 092° / 272° | 5000 / 4700 | D · APP-BH 120.200 |
|  | UNIÃO ⇄ CONDOMÍNIO | 095° / 275° | 5500 / 4700 | D · APP-BH 120.200 |
| **ECHO** | UNIÃO ⇄ JABOTICATUBAS | 346° / 166° | 5000 / 4800 | D · APP-BH 120.200 |
|  | JABOTICATUBAS ⇄ TREVO | 336° / 156° | 5000 / 4500 | D · APP-BH 120.200 |
|  | TREVO ⇄ BALDIM | 346° / 166° | 5000 / 4500 | D · APP-BH 120.200 |
|  | BALDIM ⇄ JEQUITIBÁ | 010° / 190° | 5500 / 4500 | D · APP-BH 120.200 |
| **FOXTROT** | TREVO ⇄ PONTE | 231° / 051° | 4500 / 4300 | D · APP-BH 120.200 |
| **GOLF** | JABOTICATUBAS ⇄ PONTE | 278° / 098° | 4500 / 4300 | D · APP-BH 120.200 |
| **HOTEL** | GARÇAS ⇄ ANDIROBA | 097° / 277° | 4500 / 4200 | D · APP-BH 120.200 |
|  | ANDIROBA ⇄ CAMPINHO | 115° / 295° | 4400 / 4200 | D · APP-BH 120.200 |
| **INDIA** | FORTUNA ⇄ SETE LAGOAS | 083° / 263° | 5000 / 4200 | D · APP-BH 120.200 |
| **JULIET** | ARAÇAÍ ⇄ IVECO | 188° / 008° | 5500 / 3500 | D · APP-BH 120.200 |
| **KILO** | ARDÓSIA ⇄ FORTUNA | 175° / 355° | 6000 / 4000 | G · FCA North 120.425 |
|  | FORTUNA ⇄ GARÇAS | 188° / 008° | 5500 / 4000 | G · FCA North 120.425 |
|  | GARÇAS ⇄ SINUOSO | 192° / 012° | 5500 / 4200 | G · FCA South 122.550 |
|  | SINUOSO ⇄ REPRESA | 190° / 010° | 5500 / 5200 | G · FCA South 122.550 |
| **LIMA** | SINUOSO ⇄ ITAÚNA | 244° / 064° | 5500 / 4700 | G · FCA South 122.550 |
|  | ITAÚNA ⇄ REPRESA | 135° / 315° | 6000 / 5000 | G · FCA South 122.550 |
|  | REPRESA ⇄ MOEDA | 147° / 327° | 6000 / 5500 | G · FCA South 122.550 |
| **MIKE** | GERAIS ⇄ MOEDA | 073° / 253° | 6500 / 4500 | G · FCA South 122.550 |
|  | MOEDA ⇄ ITABIRITO | 092° / 272° | 6500 / 5700 | G · FCA South 122.550 |
|  | ITABIRITO ⇄ SANTA BÁRBARA | 075° / 255° | 6200 / 6000 | G · FCA South 122.550 |
|  | SANTA BÁRBARA ⇄ CONDOMÍNIO | 028° / 208° | 6200 / 4200 | G · FCA North 120.425 |
|  | CONDOMÍNIO ⇄ ITABIRA | 094° / 274° | 7000 / 4700 | G · FCA North 120.425 |
|  | ITABIRA ⇄ AREAL | 097° / 277° | 7000 / 4500 | G · FCA North 120.425 |
| **NOVEMBER** | CONDOMÍNIO ⇄ MONLEVADE | 152° / 322° | 7000 / 4700 | G · FCA North 120.425 |
|  | MONLEVADE ⇄ SANTA BÁRBARA | 268° / 088° | 6200 / 5000 | G · FCA North 120.425 |
| **OSCAR** | CACHOEIRAS ⇄ ITABIRITO | 339° / 159° | 6500 / 5700 | G · FCA South 122.550 |
|  | ITABIRITO ⇄ CHAPÉU | 334° / 154° | 6000 / 5700 | G · FCA South 122.550 |
|  | CHAPÉU ⇄ IBIRITÉ | 329° / 149° | 6000 / 5600 | G · FCA South 122.550 |
| **PAPA** | IBIRITÉ ⇄ FEIJÃO | 231° / 051° | 6000 / 5500 | G · FCA South 122.550 |
|  | FEIJÃO ⇄ MOEDA | 183° / 003° | 6000 / 5500 | G · FCA South 122.550 |
|  | MOEDA ⇄ JECEABA | 186° / 006° | 6500 / 5000 | G · FCA South 122.550 |
| **QUEBEC** | CHAPÉU ⇄ FEIJÃO | 283° / 103° | 6000 / 5600 | G · FCA South 122.550 |
|  | FEIJÃO ⇄ REPRESA | 280° / 100° | 6000 / 5700 | G · FCA South 122.550 |
|  | REPRESA ⇄ ITAGUARA | 243° / 063° | 6000 / 5000 | G · FCA South 122.550 |
| **ROMEU** | GARÇAS ⇄ GRANJAS | 246° / 066° | 6000 / 4000 | G · FCA South 122.550 |
|  | GRANJAS ⇄ SINUOSO | 118° / 298° | 5500 / 4000 | G · FCA South 122.550 |
| **SIERRA** | PAPAGAIOS ⇄ FORTUNA | 134° / 314° | 6000 / 4000 | G · FCA North 120.425 |
| **TANGO** | FORTUNA ⇄ PARAOPEBA | 032° / 212° | 6000 / 4000 | G · FCA North 120.425 |
|  | PARAOPEBA ⇄ FISCAL | 029° / 209° | 6000 / 4000 | G · FCA North 120.425 |
| **UNIFORM** | PARAOPEBA ⇄ ARAÇAÍ | 086° / 266° | 6000 / 4000 | G · FCA North 120.425 |
|  | ARAÇAÍ ⇄ JEQUITIBÁ | 101° / 281° | 6000 / 4000 | G · FCA North 120.425 |
|  | JEQUITIBÁ ⇄ LAPINHA | 103° / 283° | 7000 / 4500 | G · FCA North 120.425 |
|  | LAPINHA ⇄ CONCEIÇÃO | 103° / 283° | 7000 / 6300 | G · FCA North 120.425 |
| **VICTOR** | FISCAL ⇄ ARAÇAÍ | 178° / 358° | 6000 / 3600 | G · FCA North 120.425 |
| **WHISKEY** | PRES. JUSCELINO ⇄ PIRAPAMA | 172° / 352° | 6000 / 3500 | G · FCA North 120.425 |
|  | PIRAPAMA ⇄ JEQUITIBÁ | 181° / 001° | 6000 / 3500 | G · FCA North 120.425 |
| **X-RAY** | ELEFANTE ⇄ JEQUITIBÁ | 245° / 065° | 7000 / 5200 | G · FCA North 120.425 |
| **YANKEE** | MANOEL ⇄ SANTA BÁRBARA | 345° / 165° | 6200 / 4900 | G · FCA North 120.425 |
|  | SANTA BÁRBARA ⇄ UNIÃO | 350° / 170° | 5500 / 4900 | G · FCA North 120.425 |

What each corridor does and where the traps are:

- **ALFA** and **CHARLIE** are the SBBH entries and exits from the west and southwest, with a **reversible direction** depending on the runway ([flow reversal](#flow-reversal-at-sbbh)). ALFA comes from SINUOSO (Paraopeba river) past Várzea das Flores to the INTERSEÇÃO gate; CHARLIE comes from IBIRITÉ past Vallourec to the PAZ gate. Both pass above the heavy helicopter traffic on the ARENA, CEASA, CENTRAL, CHAMINÉ and PRATES REHs; do not go below the minimum, not even when holding. On RWY 13, ALFA aeroplanes head for the Mineirinho arena to join the circuit.
- **BRAVO** links IBIRITÉ to CLUBE and feeds ALFA. SINUOSO, IBIRITÉ and CLUBE are *hot spots* where several routes converge.
- **DELTA** leaves SBBH through the MINA gate eastbound along the BR-381 to CONDOMÍNIO (Itabira). **It cannot be planned for arrivals to SBBH**: on the way back, the pilot asks the APP before UNIÃO or CONDOMÍNIO, because of the SBCF RWY 34 approach.
- **ECHO** is **only** for SBCF and SBLS arrivals and departures, from UNIÃO along the Taquaraçu valley to Jaboticatubas, Baldim and Jequitibá. Do not exceed the maximum (SBCF RWY 16/34 flows). JABOTICATUBAS concentrates test and training flights from SBLS and SNLG.
- **FOXTROT** (TREVO) and **GOLF** (JABOTICATUBAS) reach the SBCF PONTE gate from the north and east; **HOTEL** reaches the CAMPINHO gate (SBCF and SBLS) from the west, from GARÇAS. Expect holding because of SBCF RWY 16/34. Watch SBR 879 (GND – 3500 ft) near GOLF; the APP warns when it is active.
- **INDIA** (FORTUNA – Sete Lagoas) and **JULIET** (ARAÇAÍ – IVECO) cover the northwest, also below the SBCF flows.
- **Class G ring:** KILO (west, from ARDÓSIA to the Rio Manso reservoir), LIMA, PAPA and QUEBEC (southwest), MIKE and OSCAR (south, over Serra da Moeda and Itabirito), NOVEMBER and YANKEE (east, Santa Bárbara and Monlevade), SIERRA, TANGO, UNIFORM, VICTOR, WHISKEY and X-RAY (north). They bring VFR traffic to the start of the recommended routes: for ALFA, HOTEL and INDIA, call the APP before SINUOSO, GARÇAS and FORTUNA; for BRAVO and CHARLIE, before IBIRITÉ; for DELTA, before CONDOMÍNIO or UNIÃO; for ECHO and JULIET, before JEQUITIBÁ and ARAÇAÍ.
- **Restricted areas near the corridors:** SBR 327 Serra da Moeda (GND – 7000 ft) by MIKE, OSCAR, PAPA and QUEBEC; SBD 387 Brumadinho below LIMA and QUEBEC; SBR 817 and SBR 318 near CACHOEIRAS (OSCAR); SBR 388 Pará de Minas by ROMEU and SIERRA.

### Flow reversal at SBBH

Aeroplanes west and southwest of SBBH use the **ALFA** and **CHARLIE** REAs as reversible corridors: the direction depends on the runway in use, unless the APP clears otherwise. Traffic for SBBH calls the APP **before SINUOSO or IBIRITÉ** for the entry clearance. The runway in use is on the SBBH ATIS.

| SBBH runway | Entry | Exit | APP contact |
| :---: | :--- | :--- | :--- |
| **13** | INTERSEÇÃO gate (ALFA) | PAZ gate (CHARLIE), when cleared | Before SINUOSO or IBIRITÉ |
| **31** | PAZ gate (CHARLIE) | INTERSEÇÃO gate (ALFA), when cleared | Before IBIRITÉ |

The Tower gives the flow direction to departures, and the APP to arrivals.

### Aerodrome gates

Entry into and exit from the CTRs and ATZs are **through the gates**, unless ATC instructs otherwise.

| Aerodrome | REA gates (aeroplanes) | REH gates (helicopters) |
| :---: | :--- | :--- |
| **SBBH** | INTERSEÇÃO (RWY 13 arrivals, RWY 31 departures) · PAZ (RWY 31 arrivals, RWY 13 departures) · MINA | CEASA · CIDADE ADM · ETE · MATRIZ STA LUZIA · PARQUE |
| **SBCF** | CAMPINHO · PONTE | LAGOA DOS MARES · PONTE · VILLE |
| **SBLS** | CAMPINHO · JABOTICATUBAS | LAGOA · OLHOS |

**SBBH.** Aeroplanes arrive on ALFA or CHARLIE, depending on the runway, or on DELTA (with the restrictions above).

- **RWY 13** departures: turn right towards the PAZ gate, or left heading for position RIO to join DELTA.
- **RWY 31** departures: turn left towards the INTERSEÇÃO gate, or right towards the MINA gate, inside the ATZ, to join DELTA.
- Traffic departing or in the SBBH circuit and heading east may be cleared **direct MINA**, keeping circuit altitude until leaving the ATZ.
- Helicopters arrive and depart on the CEASA (CEASA and PARQUE gates), CIPÓ and LESTE (MATRIZ STA LUZIA), CONFINS (CIDADE ADM) and NORTE (ETE) REHs, subject to SBBH traffic. At the gate, the helicopter needs APP clearance to continue to SBBH.

**SBCF and SBLS.** Aeroplanes use the ECHO, FOXTROT, GOLF and HOTEL REAs, always with prior APP clearance; on departure the APP normally routes them on the same REAs.

- Helicopters to or from SBCF from the **west, southwest and south**: CONFINS or NEVES REH, handed to Confins Tower near the LAGOA DOS MARES gate. On departure, call the APP when passing that gate.
- From the **east, northeast and southeast**: PONTE or VILLE REH, handed over near the PONTE or VILLE gates.
- To SBLS and the town of Lagoa Santa from the east: LAGOA REH, waiting for APP instructions before switching to Lagoa Santa Radio.
- Do not overfly the SBCF fuel farm or passenger terminals.
- In the Confins CTR, flying off the REHs requires calling the APP first. Northeast of SBLS there are military test and training flights near the CIPÓ, JABOTICATUBAS, LAGOA, PONTE and VILLE REHs.

### Uncontrolled airspace below the TMA (FCA)

In class G below the TMA and on class G REAs and REHs, aircraft coordinate on the air-to-air coordination frequencies (FCA):

| FCA | Frequency | Where |
| :--- | :---: | :--- |
| **North** | 120.425 | Northern half of the TMA: REAs SIERRA, TANGO, UNIFORM, VICTOR, WHISKEY, X-RAY, YANKEE, NOVEMBER, KILO north of GARÇAS and MIKE from SANTA BÁRBARA to AREAL |
| **South** | 122.550 | Southern half of the TMA: REAs LIMA, OSCAR, PAPA, QUEBEC, ROMEU, KILO south of GARÇAS and MIKE from GERAIS to SANTA BÁRBARA |

- The FCA changes at **GARÇAS** (KILO) and **SANTA BÁRBARA** (MIKE, YANKEE and NOVEMBER); the AIC recommends monitoring the next FCA 1 minute before. SNLG and SNPA have their own FCAs.
- On VATSIM the FCAs are not positions: with no ATC online, pilots use **UNICOM 122.800**. With the APP online, VFR traffic in class G may ask it for flight information.

### Helicopters (REH)

- The 23 **REHs** form the helicopter network over Belo Horizonte, Contagem, Betim, Nova Lima and the Confins area, mostly between **3400 and 5000 ft**, 250 m either side of the axis. They are two-way, and pilots keep right of the axis. The full layout is on the **Helicopter routes (REH)** layer of the [map](#map), with altitudes and contact per segment.
- **Mandatory class D:** the pilot **notifies** the APP on entry and keeps listening until leaving. **Mandatory class G:** coordination on an FCA (ESMERALDAS, JABOTICATUBAS, NOVA LIMA, OESTE, RAPOSOS, SETE LAGOAS and SUL have class G segments).
- **Recommended** (APP clearance **before** entering): the whole of CEASA, CONFINS, LAGOA, PONTE, SABARÁ and VILLE, plus the segments SABARÁ – CAETÉ (CAETÉ), MATRIZ STA LUZIA – RAVENA (LESTE), VERA CRUZ – LAGOA DOS MARES (NEVES) and ETE – VERA CRUZ (NORTE). Without clearance, the helicopter returns to where it came from or holds its position.
- **SABARÁ** cannot be used for flight planning. CAETÉ, CEASA, CONFINS, LESTE, NORTE and SABARÁ cross the SBBH RWY 31 approach and RWY 13 departure sectors; the APP may hold them, especially with slow RWY 13 departures.
- CEASA between PEDREIRA and PARQUE depends on SBBH traffic. Near PARQUE and in south-central BH there are many local flights (news, police) and low-flying drones; the APP may give alternative instructions.
- **GARAGEM hot spot** (CENTRAL, CHAMINÉ, PRATES and SETE LAGOAS) and the crossing below the ALFA, BRAVO and CHARLIE REAs: aeroplanes fly above, at 4300–5600 ft.
- Between GALPÕES and HARAS, the **4100 ft** minimum is mandatory (prison below).

### Other rules

- In VMC, a composite separation of 2.5 NM or 500 FT is applied between IFR on RNP procedures to SBBH RWY 13/31 and VFR aeroplanes or helicopters on the REAs and REHs.
- Operations by aircraft without radio are prohibited at SBCF.
- SBLS: mandatory contact with Belo Horizonte Control when entering the TMA; remain within the ATZ and do not extend the base leg (RWY 13) or delay the turn (RWY 31) beyond position BOSQUE, due to SBCF.

### Phraseology

On first contact, the pilot keeps it short: station, registration, corridor, gate or position, altitude and direction[^aic2726]. Brazilian VFR traffic usually calls in Portuguese. Recommended route, asking to enter:

```
Controle Belo Horizonte, PR-MWN, REA ROMEU, posição SINUOSO, mantendo 5500 pés, solicita ingresso na REA ALFA.
```

Mandatory class D REH, notifying entry:

```
Controle Belo Horizonte, PR-MWN, REH SUL, posição BH SHOPPING, mantendo 4400 pés, proa PARQUE.
```

In class G, on the FCA (UNICOM on VATSIM):

```
Coordenação, PR-MWN, REA OSCAR, posição IBIRITÉ, mantendo 6000 pés, proa CHAPÉU, após ITABIRITO.
```

The same in English:

```
Belo Horizonte Control, PR-MWN, REA ROMEU, position SINUOSO, maintaining 5500 feet, request to join REA ALFA.
```

```
Belo Horizonte Control, PR-MWN, REH SUL, position BH SHOPPING, maintaining 4400 feet, heading PARQUE.
```

## :material-note-text-outline: Remarks

- Belo Horizonte 1 is class A between FL145 and FL195 and class C between 5500 FT and FL145.
- The Belo Horizonte CTR excludes the Confins CTR.
- SBLS is a military aerodrome (PAMALS); civil aviation requires authorization from the PAMALS director.
- ATZs have no class published in the AIP (ENR 2.2).
- In the package, Belo Horizonte APP has no sectors: `SBWH_APP` covers the whole TMA.
- Volumes, sectors and map follow the TMA-BH Project ([AIC N 25/26](https://publicacoes.decea.mil.br/publicacao/aic-n-2526){ target="_blank" }), effective with the 26 NOV 2026 AIRAC, which also revises the SIDs, STARs and IACs. The VATSIM sector package may still carry the old TMA and CTR outlines.

---

Back to the Brasília FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.
[^amdt]: AIP Brasil, AMDT AIRAC 2612A1 (26 NOV 2026), ENR 2.1 and ENR 2.2.
[^aic2726]: [AIC N 27/26](https://publicacoes.decea.mil.br/publicacao/aic-n-2726){ target="_blank" }, items 2 to 5 and Annexes A and B.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026, Projeto TMA-BH), em [longitude, latitude]. A Belo Horizonte 1 é a união dos setores 01 a 04.
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
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
    .mapa-legenda .rea-linha.g { border-top: 3px dashed #0284c7 }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 1", "posicao": "SBWH_APP", "freq": "129.100", "lim": "5500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-44.645, -19.21556], [-44.72806, -19.43556], [-44.77083, -19.5875], [-44.73611, -19.685], [-44.60111, -20.065], [-44.55556, -20.19194], [-44.47194, -20.34583], [-44.43556, -20.41278], [-44.33528, -20.48639], [-43.86639, -20.55944], [-43.4575, -20.49667], [-43.23472, -20.15444], [-43.15722, -20.01389], [-43.13528, -19.97417], [-43.11694, -19.65639], [-43.16389, -19.52056], [-43.25278, -19.27972], [-43.37333, -19.13806], [-43.45528, -19.04167], [-43.53639, -18.96222], [-43.58333, -18.92278], [-43.82583, -18.89306], [-43.97444, -18.87472], [-44.12167, -18.87139], [-44.28361, -18.93917], [-44.42583, -18.99861], [-44.61139, -19.12611]]},
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 2", "posicao": "SBWH_APP", "freq": "129.100", "lim": "4100 FT – 5500 FT", "classe": "C", "link": "", "contorno": [[-44.320556, -19.979444], [-43.980556, -19.929167], [-43.946667, -20.048889], [-43.793611, -20.103611], [-43.522778, -19.902222], [-43.486667, -19.501944], [-43.943056, -19.166111], [-44.239444, -19.225], [-44.379444, -19.294444], [-44.414444, -19.517222], [-44.418056, -19.577222], [-44.391667, -19.6675], [-44.379722, -19.716667], [-44.355833, -19.839722], [-44.341389, -19.895556]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Confins CTR", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 5500 FT", "classe": "D", "link": "", "contorno": [[-43.965833, -19.39], [-44.199444, -19.581389], [-43.988056, -19.810833], [-43.852222, -19.793889], [-43.694167, -19.739444], [-43.657778, -19.725278]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Belo Horizonte CTR", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 5500 FT", "classe": "C", "link": "", "contorno": [[-44.199444, -19.581389], [-43.988056, -19.810833], [-43.852222, -19.793889], [-43.694167, -19.739444], [-43.657778, -19.725278], [-43.7525, -19.944722], [-43.854444, -19.993056], [-43.9475, -19.979444], [-43.959167, -19.938333], [-44.18, -19.859167]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Confins ATZ", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.973889, -19.509722], [-43.888889, -19.601667], [-43.935278, -19.64], [-43.939722, -19.652222], [-43.899167, -19.696389], [-43.951667, -19.738333], [-44.083056, -19.596389]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Belo Horizonte ATZ (Pampulha)", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.891667, -19.813056], [-43.856944, -19.840833], [-43.881667, -19.911111], [-43.928056, -19.917778], [-44.009444, -19.892222], [-44.0425, -19.859722], [-44.017778, -19.789444], [-43.974722, -19.786944]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Lagoa Santa ATZ", "posicao": "SBLS_R_TWR", "freq": "122.850", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.912222, -19.620833], [-43.863611, -19.632778], [-43.8575, -19.6625], [-43.863611, -19.679444], [-43.93, -19.662778], [-43.939722, -19.652222], [-43.935278, -19.64]]}
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
const setores = [{"posicao": "Sector 01", "rot": "01", "freq": "129.100", "lim": "5500 FT – FL195", "contorno": [[-44.645, -19.215556], [-44.728056, -19.435556], [-44.770833, -19.5875], [-44.736111, -19.685], [-44.601111, -20.065], [-44.555556, -20.191944], [-44.471944, -20.345833], [-44.164444, -19.810556], [-43.920278, -19.727222], [-44.030278, -19.594167], [-44.075, -19.54]]}, {"posicao": "Sector 02", "rot": "02", "freq": "129.100", "lim": "5500 FT – FL195", "contorno": [[-44.645, -19.215556], [-44.075, -19.54], [-44.030278, -19.594167], [-43.536389, -18.962222], [-43.583333, -18.922778], [-43.825833, -18.893056], [-43.974444, -18.874722], [-44.121667, -18.871389], [-44.283611, -18.939167], [-44.425833, -18.998611], [-44.611389, -19.126111]]}, {"posicao": "Sector 03A", "rot": "03A", "freq": "129.100", "lim": "5500 FT – FL195", "contorno": [[-44.030278, -19.594167], [-43.920278, -19.727222], [-43.163889, -19.520556], [-43.252778, -19.279722], [-43.373333, -19.138056], [-43.455278, -19.041667], [-43.536389, -18.962222]]}, {"posicao": "Sector 03B", "rot": "03B", "freq": "129.100", "lim": "5500 FT – FL195", "contorno": [[-43.920278, -19.727222], [-43.705556, -19.985833], [-43.157222, -20.013889], [-43.135278, -19.974167], [-43.116944, -19.656389], [-43.163889, -19.520556]]}, {"posicao": "Sector 04", "rot": "04", "freq": "129.100", "lim": "5500 FT – FL195", "contorno": [[-44.471944, -20.345833], [-44.435556, -20.412778], [-44.335278, -20.486389], [-43.866389, -20.559444], [-43.4575, -20.496667], [-43.234722, -20.154444], [-43.157222, -20.013889], [-43.705556, -19.985833], [-43.920278, -19.727222], [-44.164444, -19.810556]]}, {"posicao": "Sector 05", "rot": "05", "freq": "129.100", "lim": "5500 FT – FL110", "contorno": [[-44.098333, -19.741944], [-44.345556, -19.4675], [-44.084722, -19.256389], [-43.8375, -19.530278]]}, {"posicao": "Sector 06", "rot": "06", "freq": "129.100", "lim": "5500 FT – FL110", "contorno": [[-43.8375, -19.530278], [-43.734167, -19.644167], [-43.533889, -19.715833], [-43.580556, -19.958333], [-44.056389, -19.788056], [-44.098333, -19.741944]]}, {"posicao": "Sector 07", "rot": "07", "freq": "129.100", "lim": "5500 FT – 9000 FT", "contorno": [[-44.381667, -19.787222], [-44.072778, -19.770278], [-44.056389, -19.788056], [-43.939722, -19.83], [-44.022778, -20.038889], [-44.079167, -20.018611], [-44.290556, -20.031389]]}, {"posicao": "Sector 08", "rot": "08", "freq": "129.100", "lim": "5500 FT – 9000 FT", "contorno": [[-43.939722, -19.83], [-43.580556, -19.958333], [-43.623333, -20.181111], [-44.022778, -20.038889]]}];
const paletaSetores = ['#60a5fa', '#f472b6', '#a3e635', '#fb923c', '#a78bfa', '#2dd4bf', '#fbbf24', '#f87171', '#34d399', '#e879f9', '#38bdf8', '#fda4af', '#818cf8'];
var grupoSetores = L.featureGroup();
setores.forEach(function (s, k) {
    var cor = paletaSetores[k % paletaSetores.length];
    L.polygon(s.contorno.map(paraLatLng), { color: cor, fillColor: cor, weight: 2, fillOpacity: 0.2 })
        .bindPopup('<b>' + s.posicao + '</b><br>' + s.lim + '<br>In the package: <code>SBWH_APP</code> ' + s.freq)
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

// Corredores visuais (REA), REH e portões da AIC N 27/26 (Anexos A e B); gerado de bhgen/emit.py
const reaTrechos = [{"rota": "ALFA", "de": "SINUOSO", "para": "FLORES", "rumos": "128° / 308°", "max": "4500", "min": "4400", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "ALFA", "de": "FLORES", "para": "CLUBE", "rumos": "109° / 289°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "ALFA", "de": "CLUBE", "para": "INTERSEÇÃO", "rumos": "086° / 266°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "BRAVO", "de": "IBIRITÉ", "para": "CLUBE", "rumos": "023° / 203°", "max": "5600", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CHARLIE", "de": "IBIRITÉ", "para": "VALLOUREC", "rumos": "068° / 248°", "max": "5600", "min": "4600", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "CHARLIE", "de": "VALLOUREC", "para": "PAZ", "rumos": "052° / 232°", "max": "5000", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "DELTA", "de": "MINA", "para": "SÍTIOS", "rumos": "093° / 273°", "max": "4900", "min": "4700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "DELTA", "de": "SÍTIOS", "para": "UNIÃO", "rumos": "092° / 272°", "max": "5000", "min": "4700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "DELTA", "de": "UNIÃO", "para": "CONDOMÍNIO", "rumos": "095° / 275°", "max": "5500", "min": "4700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "UNIÃO", "para": "JABOTICATUBAS", "rumos": "346° / 166°", "max": "5000", "min": "4800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "JABOTICATUBAS", "para": "TREVO", "rumos": "336° / 156°", "max": "5000", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "TREVO", "para": "BALDIM", "rumos": "346° / 166°", "max": "5000", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "BALDIM", "para": "JEQUITIBÁ", "rumos": "010° / 190°", "max": "5500", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "FOXTROT", "de": "TREVO", "para": "PONTE", "rumos": "231° / 051°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "GOLF", "de": "JABOTICATUBAS", "para": "PONTE", "rumos": "278° / 098°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "HOTEL", "de": "GARÇAS", "para": "ANDIROBA", "rumos": "097° / 277°", "max": "4500", "min": "4200", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "HOTEL", "de": "ANDIROBA", "para": "CAMPINHO", "rumos": "115° / 295°", "max": "4400", "min": "4200", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "INDIA", "de": "FORTUNA", "para": "SETE LAGOAS", "rumos": "083° / 263°", "max": "5000", "min": "4200", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "JULIET", "de": "ARAÇAÍ", "para": "IVECO", "rumos": "188° / 008°", "max": "5500", "min": "3500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "KILO", "de": "ARDÓSIA", "para": "FORTUNA", "rumos": "175° / 355°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "KILO", "de": "FORTUNA", "para": "GARÇAS", "rumos": "188° / 008°", "max": "5500", "min": "4000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "KILO", "de": "GARÇAS", "para": "SINUOSO", "rumos": "192° / 012°", "max": "5500", "min": "4200", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "KILO", "de": "SINUOSO", "para": "REPRESA", "rumos": "190° / 010°", "max": "5500", "min": "5200", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "LIMA", "de": "SINUOSO", "para": "ITAÚNA", "rumos": "244° / 064°", "max": "5500", "min": "4700", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "LIMA", "de": "ITAÚNA", "para": "REPRESA", "rumos": "135° / 315°", "max": "6000", "min": "5000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "LIMA", "de": "REPRESA", "para": "MOEDA", "rumos": "147° / 327°", "max": "6000", "min": "5500", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "MIKE", "de": "GERAIS", "para": "MOEDA", "rumos": "073° / 253°", "max": "6500", "min": "4500", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "MIKE", "de": "MOEDA", "para": "ITABIRITO", "rumos": "092° / 272°", "max": "6500", "min": "5700", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "MIKE", "de": "ITABIRITO", "para": "SANTA BÁRBARA", "rumos": "075° / 255°", "max": "6200", "min": "6000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "MIKE", "de": "SANTA BÁRBARA", "para": "CONDOMÍNIO", "rumos": "028° / 208°", "max": "6200", "min": "4200", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "MIKE", "de": "CONDOMÍNIO", "para": "ITABIRA", "rumos": "094° / 274°", "max": "7000", "min": "4700", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "MIKE", "de": "ITABIRA", "para": "AREAL", "rumos": "097° / 277°", "max": "7000", "min": "4500", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "NOVEMBER", "de": "CONDOMÍNIO", "para": "MONLEVADE", "rumos": "152° / 322°", "max": "7000", "min": "4700", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "NOVEMBER", "de": "MONLEVADE", "para": "SANTA BÁRBARA", "rumos": "268° / 088°", "max": "6200", "min": "5000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "OSCAR", "de": "CACHOEIRAS", "para": "ITABIRITO", "rumos": "339° / 159°", "max": "6500", "min": "5700", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "OSCAR", "de": "ITABIRITO", "para": "CHAPÉU", "rumos": "334° / 154°", "max": "6000", "min": "5700", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "OSCAR", "de": "CHAPÉU", "para": "IBIRITÉ", "rumos": "329° / 149°", "max": "6000", "min": "5600", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "PAPA", "de": "IBIRITÉ", "para": "FEIJÃO", "rumos": "231° / 051°", "max": "6000", "min": "5500", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "PAPA", "de": "FEIJÃO", "para": "MOEDA", "rumos": "183° / 003°", "max": "6000", "min": "5500", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "PAPA", "de": "MOEDA", "para": "JECEABA", "rumos": "186° / 006°", "max": "6500", "min": "5000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "QUEBEC", "de": "CHAPÉU", "para": "FEIJÃO", "rumos": "283° / 103°", "max": "6000", "min": "5600", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "QUEBEC", "de": "FEIJÃO", "para": "REPRESA", "rumos": "280° / 100°", "max": "6000", "min": "5700", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "QUEBEC", "de": "REPRESA", "para": "ITAGUARA", "rumos": "243° / 063°", "max": "6000", "min": "5000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "ROMEU", "de": "GARÇAS", "para": "GRANJAS", "rumos": "246° / 066°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "ROMEU", "de": "GRANJAS", "para": "SINUOSO", "rumos": "118° / 298°", "max": "5500", "min": "4000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "SIERRA", "de": "PAPAGAIOS", "para": "FORTUNA", "rumos": "134° / 314°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "TANGO", "de": "FORTUNA", "para": "PARAOPEBA", "rumos": "032° / 212°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "TANGO", "de": "PARAOPEBA", "para": "FISCAL", "rumos": "029° / 209°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "UNIFORM", "de": "PARAOPEBA", "para": "ARAÇAÍ", "rumos": "086° / 266°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "UNIFORM", "de": "ARAÇAÍ", "para": "JEQUITIBÁ", "rumos": "101° / 281°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "UNIFORM", "de": "JEQUITIBÁ", "para": "LAPINHA", "rumos": "103° / 283°", "max": "7000", "min": "4500", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "UNIFORM", "de": "LAPINHA", "para": "CONCEIÇÃO", "rumos": "103° / 283°", "max": "7000", "min": "6300", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "VICTOR", "de": "FISCAL", "para": "ARAÇAÍ", "rumos": "178° / 358°", "max": "6000", "min": "3600", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "WHISKEY", "de": "PRES. JUSCELINO", "para": "PIRAPAMA", "rumos": "172° / 352°", "max": "6000", "min": "3500", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "WHISKEY", "de": "PIRAPAMA", "para": "JEQUITIBÁ", "rumos": "181° / 001°", "max": "6000", "min": "3500", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "X-RAY", "de": "ELEFANTE", "para": "JEQUITIBÁ", "rumos": "245° / 065°", "max": "7000", "min": "5200", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "YANKEE", "de": "MANOEL", "para": "SANTA BÁRBARA", "rumos": "345° / 165°", "max": "6200", "min": "4900", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "YANKEE", "de": "SANTA BÁRBARA", "para": "UNIÃO", "rumos": "350° / 170°", "max": "5500", "min": "4900", "rec": false, "esp": "G · FCA North 120.425"}];
const reaPontos = {"SINUOSO": [-44.3777, -19.86028], "FLORES": [-44.16558, -19.91388], "CLUBE": [-44.06085, -19.90563], "INTERSEÇÃO": [-44.00546, -19.87845], "IBIRITÉ": [-44.06083, -20.02024], "VALLOUREC": [-44.00194, -19.96444], "PAZ": [-43.96412, -19.89829], "MINA": [-43.84316, -19.81759], "SÍTIOS": [-43.68472, -19.76306], "UNIÃO": [-43.57951, -19.7233], "CONDOMÍNIO": [-43.38608, -19.66157], "JABOTICATUBAS": [-43.7475, -19.51861], "TREVO": [-43.84248, -19.43555], "BALDIM": [-43.93034, -19.32554], "JEQUITIBÁ": [-43.97581, -19.14602], "PONTE": [-43.91136, -19.56008], "GARÇAS": [-44.40997, -19.69866], "ANDIROBA": [-44.23025, -19.64991], "CAMPINHO": [-44.05762, -19.65458], "FORTUNA": [-44.44912, -19.56517], "SETE LAGOAS": [-44.25988, -19.46129], "ARAÇAÍ": [-44.24858, -19.20102], "IVECO": [-44.20264, -19.35798], "ARDÓSIA": [-44.63941, -19.22192], "REPRESA": [-44.29743, -20.17927], "ITAÚNA": [-44.57747, -20.07602], "MOEDA": [-44.05358, -20.33296], "GERAIS": [-44.22464, -20.47008], "ITABIRITO": [-43.77831, -20.23046], "SANTA BÁRBARA": [-43.4125, -19.95833], "ITABIRA": [-43.21108, -19.60185], "AREAL": [-43.12876, -19.57912], "MONLEVADE": [-43.15192, -19.83796], "CACHOEIRAS": [-43.51011, -20.4883], "CHAPÉU": [-43.93266, -20.10702], "FEIJÃO": [-44.12694, -20.14167], "JECEABA": [-43.98497, -20.53546], "ITAGUARA": [-44.48667, -20.39194], "GRANJAS": [-44.55174, -19.8457], "PAPAGAIOS": [-44.75207, -19.45479], "PARAOPEBA": [-44.40275, -19.27768], "FISCAL": [-44.37014, -18.96132], "LAPINHA": [-43.76139, -19.10889], "CONCEIÇÃO": [-43.41528, -19.04889], "PRES. JUSCELINO": [-44.12087, -18.87619], "PIRAPAMA": [-44.03914, -19.00268], "ELEFANTE": [-43.76091, -18.91956], "MANOEL": [-43.19924, -20.21384]};
const rehTrechos = [{"rota": "ARENA", "de": "ARENA MRV", "para": "INTERLOGOS", "rumos": "148° / 328°", "max": "4300", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "ARENA", "de": "INTERLOGOS", "para": "ESTRELA", "rumos": "150° / 330°", "max": "4400", "min": "4300", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "ARENA", "de": "ESTRELA", "para": "BH SHOPPING", "rumos": "138° / 318°", "max": "4600", "min": "4300", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CAETÉ", "de": "SABARÁ", "para": "CAETÉ", "rumos": "115° / 295°", "max": "4300", "min": "4100", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CAETÉ", "de": "CAETÉ", "para": "RAVENA", "rumos": "336° / 156°", "max": "4600", "min": "4500", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CAETÉ", "de": "RAVENA", "para": "VELHAS", "rumos": "016° / 196°", "max": "4500", "min": "4100", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CAPIM BRANCO", "de": "CAPIM BRANCO", "para": "VERA CRUZ", "rumos": "174° / 354°", "max": "3900", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CEASA", "de": "PEDREIRA", "para": "CEASA", "rumos": "146° / 326°", "max": "4000", "min": "3800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CEASA", "de": "CEASA", "para": "PRATES", "rumos": "127° / 307°", "max": "4000", "min": "3800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CEASA", "de": "PRATES", "para": "PARQUE", "rumos": "130° / 310°", "max": "4000", "min": "3800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "FLORES", "para": "GARAGEM", "rumos": "120° / 300°", "max": "4100", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "GARAGEM", "para": "ARENA MRV", "rumos": "120° / 300°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "ARENA MRV", "para": "MATER DEI", "rumos": "109° / 289°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "MATER DEI", "para": "PARQUE", "rumos": "111° / 291°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CHAMINÉ", "de": "ESMERALDAS", "para": "GARAGEM", "rumos": "161° / 341°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CHAMINÉ", "de": "GARAGEM", "para": "CHAMINÉ", "rumos": "138° / 318°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CHAMINÉ", "de": "CHAMINÉ", "para": "VALLOUREC", "rumos": "153° / 333°", "max": "4000", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "MATRIZ STA LUZIA", "para": "VELHAS", "rumos": "041° / 221°", "max": "3600", "min": "3500", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "VELHAS", "para": "ESTÂNCIA", "rumos": "338° / 158°", "max": "3600", "min": "3400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "ESTÂNCIA", "para": "ROCHEDO", "rumos": "301° / 121°", "max": "3500", "min": "3400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "ROCHEDO", "para": "MINERADORA", "rumos": "270° / 090°", "max": "3500", "min": "3400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CONFINS", "de": "CIDADE ADM", "para": "GALO", "rumos": "013° / 193°", "max": "3500", "min": "3500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CONFINS", "de": "GALO", "para": "LAGOA DOS MARES", "rumos": "357° / 177°", "max": "3500", "min": "3500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ESMERALDAS", "de": "PEDREIRA", "para": "ESMERALDAS", "rumos": "324° / 144°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "ESMERALDAS", "de": "ESMERALDAS", "para": "CHALÉS", "rumos": "017° / 197°", "max": "4000", "min": "3900", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "HARAS", "de": "GALPÕES", "para": "HARAS", "rumos": "019° / 199°", "max": "4100", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "HARAS", "de": "HARAS", "para": "CAPIM BRANCO", "rumos": "019° / 199°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "JABOTICATUBAS", "de": "VELHAS", "para": "JABOTICATUBAS", "rumos": "050° / 230°", "max": "4100", "min": "3400", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "LAGOA", "de": "OLHOS", "para": "LAGOA", "rumos": "082° / 262°", "max": "3600", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "LAGOA", "de": "LAGOA", "para": "VELHAS", "rumos": "098° / 278°", "max": "3600", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "LESTE", "de": "MATRIZ STA LUZIA", "para": "RAVENA", "rumos": "141° / 321°", "max": "4500", "min": "4100", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "LESTE", "de": "RAVENA", "para": "VIADUTO", "rumos": "095° / 275°", "max": "4500", "min": "4400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NEVES", "de": "ESMERALDAS", "para": "GALPÕES", "rumos": "068° / 248°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NEVES", "de": "GALPÕES", "para": "VERA CRUZ", "rumos": "063° / 243°", "max": "3900", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NEVES", "de": "VERA CRUZ", "para": "LAGOA DOS MARES", "rumos": "086° / 266°", "max": "3800", "min": "3700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "ETE", "para": "VERA CRUZ", "rumos": "352° / 172°", "max": "3900", "min": "3600", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "VERA CRUZ", "para": "HARAS", "rumos": "324° / 144°", "max": "3900", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "HARAS", "para": "PEDÁGIO", "rumos": "324° / 144°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "PEDÁGIO", "para": "CAPIM BRANCO", "rumos": "080° / 260°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "CAPIM BRANCO", "para": "MINERADORA", "rumos": "089° / 269°", "max": "3800", "min": "3500", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NOVA LIMA", "de": "BH SHOPPING", "para": "NOVA LIMA", "rumos": "122° / 302°", "max": "4700", "min": "4600", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NOVA LIMA", "de": "NOVA LIMA", "para": "RIO ACIMA", "rumos": "166° / 346°", "max": "4700", "min": "3800", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "OESTE", "de": "LAGOA PETROBRÁS", "para": "VALLOUREC", "rumos": "083° / 263°", "max": "4100", "min": "3800", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "OESTE", "de": "VALLOUREC", "para": "INTERLOGOS", "rumos": "085° / 265°", "max": "4100", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "OESTE", "de": "INTERLOGOS", "para": "PARQUE", "rumos": "082° / 262°", "max": "4200", "min": "4100", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "PONTE", "de": "ESTÂNCIA", "para": "PONTE", "rumos": "208° / 028°", "max": "3500", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "PRATES", "de": "GARAGEM", "para": "PRATES", "rumos": "104° / 284°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "RAPOSOS", "de": "HELICENTRO", "para": "NOVA LIMA", "rumos": "081° / 261°", "max": "5000", "min": "5000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "RAPOSOS", "de": "NOVA LIMA", "para": "RAPOSOS", "rumos": "088° / 268°", "max": "4300", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "RAPOSOS", "de": "RAPOSOS", "para": "CAETÉ", "rumos": "086° / 266°", "max": "4300", "min": "4300", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "SABARÁ", "de": "NOVA LIMA", "para": "SABARÁ", "rumos": "047° / 227°", "max": "4300", "min": "3900", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "SABARÁ", "de": "SABARÁ", "para": "RAVENA", "rumos": "048° / 228°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "SETE LAGOAS", "de": "GARAGEM", "para": "PEDREIRA", "rumos": "008° / 188°", "max": "4000", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "SETE LAGOAS", "de": "PEDREIRA", "para": "GALPÕES", "rumos": "007° / 187°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "SETE LAGOAS", "de": "GALPÕES", "para": "CHALÉS", "rumos": "350° / 170°", "max": "4000", "min": "3900", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "SETE LAGOAS", "de": "CHALÉS", "para": "PEDÁGIO", "rumos": "001° / 181°", "max": "4000", "min": "3900", "rec": false, "esp": "G · FCA North 120.425"}, {"rota": "SUL", "de": "HELICENTRO", "para": "BH SHOPPING", "rumos": "035° / 215°", "max": "5000", "min": "5000", "rec": false, "esp": "G · FCA South 122.550"}, {"rota": "SUL", "de": "BH SHOPPING", "para": "PARQUE", "rumos": "037° / 217°", "max": "4400", "min": "4200", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "VILLE", "de": "VILLE", "para": "VELHAS", "rumos": "123° / 303°", "max": "3700", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}];
const rehPontos = {"ARENA MRV": [-44.01611, -19.93083], "INTERLOGOS": [-43.98131, -19.95386], "ESTRELA": [-43.96778, -19.96333], "BH SHOPPING": [-43.94528, -19.97306], "SABARÁ": [-43.81444, -19.895], "CAETÉ": [-43.67083, -19.89833], "RAVENA": [-43.77194, -19.80972], "VELHAS": [-43.79778, -19.61389], "CAPIM BRANCO": [-44.14056, -19.55083], "VERA CRUZ": [-44.05361, -19.6975], "PEDREIRA": [-44.09333, -19.86917], "CEASA": [-44.04972, -19.89583], "PRATES": [-43.98863, -19.90994], "PARQUE": [-43.93306, -19.92611], "FLORES": [-44.16558, -19.91388], "GARAGEM": [-44.07779, -19.92386], "MATER DEI": [-43.9575, -19.92694], "ESMERALDAS": [-44.17278, -19.825], "CHAMINÉ": [-44.02389, -19.94722], "VALLOUREC": [-44.00194, -19.96444], "MATRIZ STA LUZIA": [-43.85056, -19.77028], "ESTÂNCIA": [-43.90722, -19.50972], "ROCHEDO": [-44.00772, -19.49602], "MINERADORA": [-44.09167, -19.53], "CIDADE ADM": [-43.94889, -19.78417], "GALO": [-43.95694, -19.74167], "LAGOA DOS MARES": [-43.99472, -19.66861], "CHALÉS": [-44.19, -19.67694], "GALPÕES": [-44.12222, -19.77639], "HARAS": [-44.13229, -19.65261], "JABOTICATUBAS": [-43.7475, -19.51861], "OLHOS": [-43.91008, -19.64869], "LAGOA": [-43.89351, -19.63914], "VIADUTO": [-43.67667, -19.78083], "ETE": [-44.00583, -19.77361], "PEDÁGIO": [-44.22194, -19.60139], "NOVA LIMA": [-43.85778, -19.98583], "RIO ACIMA": [-43.78056, -20.08083], "LAGOA PETROBRÁS": [-44.11444, -20.02583], "PONTE": [-43.91143, -19.56004], "HELICENTRO": [-43.96222, -20.04722], "RAPOSOS": [-43.80806, -19.96361], "VILLE": [-43.9041, -19.59583]};
const portoes = {"REA": {"INTERSEÇÃO": "SBBH", "PAZ": "SBBH", "MINA": "SBBH", "CAMPINHO": "SBCF/SBLS", "PONTE": "SBCF", "JABOTICATUBAS": "SBLS"}, "REH": {"CEASA": "SBBH", "CIDADE ADM": "SBBH", "ETE": "SBBH", "MATRIZ STA LUZIA": "SBBH", "PARQUE": "SBBH", "LAGOA DOS MARES": "SBCF", "PONTE": "SBCF", "VILLE": "SBCF", "LAGOA": "SBLS", "OLHOS": "SBLS"}};
var corRec = '#c026d3', corObr = '#0284c7', corReh = '#0f766e', corRehRec = '#b45309';
var grupoRea = L.featureGroup();
var reaRotuladas = {};
reaTrechos.forEach(function (t) {
    var a = paraLatLng(reaPontos[t.de]), b = paraLatLng(reaPontos[t.para]);
    var cor = t.rec ? corRec : corObr;
    L.polyline([a, b], { color: cor, weight: 4, opacity: 0.9, dashArray: t.rec ? null : '8 6' })
        .bindPopup('<b>REA ' + t.rota + '</b><br>' + t.de + ' ⇄ ' + t.para + '<br>Tracks: ' + t.rumos +
            '<br>Max / min (ft): ' + t.max + ' / ' + t.min + '<br>' + t.esp +
            (t.rec ? '<br>Recommended: APP clearance before entering' : '<br>Mandatory') +
            (t.rev ? '<br>Direction depends on the SBBH runway' : ''))
        .addTo(grupoRea);
    // Um rótulo por corredor no trecho do meio; os demais trechos só com zoom maior
    var trechosRea = reaTrechos.filter(function (x) { return x.rota === t.rota; });
    var principal = trechosRea[Math.floor((trechosRea.length - 1) / 2)] === t;
    L.marker([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2], { opacity: 0, interactive: false, icon: L.divIcon({ className: '', iconSize: [0, 0] }) })
        .bindTooltip(t.rota, { permanent: true, direction: 'center', className: principal ? 'rea-rotulo' : 'rea-rotulo rea-rotulo-trecho' })
        .addTo(grupoRea);
});
Object.keys(reaPontos).forEach(function (n) {
    var portao = portoes.REA[n];
    L.circleMarker(paraLatLng(reaPontos[n]), portao ?
        { radius: 5, color: '#0f172a', weight: 2, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 3.5, color: '#334155', weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Gate ' + n + ' (' + portao + ')' : n).addTo(grupoRea);
});

var grupoReh = L.featureGroup();
var rehRotuladas = {};
rehTrechos.forEach(function (t) {
    var linha = [paraLatLng(rehPontos[t.de]), paraLatLng(rehPontos[t.para])];
    var classeG = t.esp.charAt(0) === 'G';
    L.polyline(linha, { color: t.rec ? corRehRec : corReh, weight: 2.5, opacity: 0.9, dashArray: classeG ? '5 4' : null })
        .bindPopup('<b>REH ' + t.rota + '</b><br>' + t.de + ' ⇄ ' + t.para + '<br>Tracks: ' + t.rumos +
            '<br>Max / min (ft): ' + t.max + ' / ' + t.min + '<br>' + t.esp +
            (t.rec ? '<br>Recommended: APP clearance before entering' : '<br>Mandatory'))
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
    "APP sectors (AIP)": grupoSetores,
    "Visual corridors (REA)": grupoRea,
    "Helicopter routes (REH)": grupoReh
}).addTo(mapa);

// Corridor labels only when zoomed in enough not to clutter
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
    div.innerHTML = '<b>Class</b>' + ['A', 'C', 'D'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('') +
        '<div><span class="rea-linha"></span>Recommended REA</div>' +
        '<div><span class="rea-linha g"></span>Mandatory REA (G)</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Gate</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
