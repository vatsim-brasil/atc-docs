---
title: SBGL - Galeão
tags:
    - Aeródromo
    - Controlado
    - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General Information

|                              | Information                                   |
|------------------------------|-----------------------------------------------|
| **Aerodrome name**           | Galeão - Antônio Carlos Jobim                 |
| **Type of Operation**        | International, Public and Military            |
| **Transition altitude**      | 7000 ft                                       |
| **Elevation**                | 28 ft (9 m)                                   |
| **Largest aircraft**         | Wide-bodies (code 4E); A380 and B747-8 under special procedures[^ad20-1] |
| **Airspace**                 | Galeão CTR, class D, GND/2000 ft[^ad17]       |
| **Accepts A380?** | :material-check:{ style="color:#12a150" }[^ad20-1] |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Select one of the tools in the tabs above (Charts, Weather or Traffic) to access the aerodrome information.

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBGL?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Weather"
    <div id="metar-taf-container" data-airport="SBGL" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Loading METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Loading TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBGL){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

---

## :material-routes: Runways

### Preferential runway system

SBGL has **two runways that do not cross** but converge to the west: 10/28 (4000 m, concrete), north of the terminals, and 15/33 (3180 m, asphalt), southwest of them[^ad20-3].

<div class="grid cards" markdown>

-   :material-airplane-takeoff:{ .lg .middle } **Takeoffs: `10`**

    ---

    4000 × 45 m. Preferential for **takeoff** in segregated operations. ILS CAT II on 10 and ILS on 28.

-   :material-airplane-landing:{ .lg .middle } **Landings: `15`**

    ---

    3180 × 47 m. Preferential for **landing** in segregated operations. ILS on 15. Displaced thresholds in both directions.

</div>

!!! warning "Preferential system"
    With a {==**tailwind component of 7 kt or less**==} and **dry runways**, the configuration in the table below applies, according to the scenario in use[^ad20-3].

    With the preferential system in use, pilots requesting the alternate system should expect a **delay** to their landing or takeoff[^ad20-3].

| Scenario | Landings | Takeoffs | When |
| :--- | :---: | :---: | :--- |
| **Segregated operations** (preferential) | **15** | **10** | Tailwind of 7 kt or less and dry runways |
| **Single runway 15/33** | **15** | **15** | Only 15/33 available |
| **Single runway 10/28** | **10** | **10** | Only 10/28 available |
| **Converging operations** | **28** | **33** | Activated by Tower, see [Converging operations](#converging-operations) |

### Runway data

| Runway | Dimensions | TORA | LDA | Approach | Remarks |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **10** | 4000 × 45 m | 4000 m | 4000 m | ILS CAT II | |
| **28** | 4000 × 45 m | 4000 m | 4000 m | ILS | |
| **15** | 3180 × 47 m | 3060 m | 2930 m | ILS | Displaced threshold (130 m) |
| **33** | 3180 × 47 m | 3050 m | 2930 m | Non-precision | Displaced threshold (120 m) |

- On 15/33, pilots **start the takeoff from the beginning of the runway**, without taxiing to the displaced threshold[^ad20-2].
- The aerodrome accepts aircraft up to code **4E**. The **A380** and **B747-8** operate under special procedures approved by ANAC[^ad20-1].

[^ad20-1]: [AIP Brasil, AD 2 SBGL 2.20, item 1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-2]: [AIP Brasil, AD 2 SBGL 2.20, item 2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-3]: [AIP Brasil, AD 2 SBGL 2.20, item 3](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Declared distances: AD 2.13.

---

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| :--- | :---: | :--- | :---: | :--- |
| **SBGL_ATIS** | `AGL` | Galeão ATIS | **127.600** | D-ATIS |
| **SBGL_DEL** | `DGL` | Galeão Clearance | **121.000** | `DCL` (code `SBGL`) |
| **SBGL_RMP** | `RGL` | Galeão Apron | **121.950** | Events only |
| **SBGL_GND** | `GGL` | Galeão Ground | **121.650** | |
| **SBGL_TWR** | `TGL` | Galeão Tower | **118.000** | |

### DCL

SBGL has **DCL** (departure clearance via datalink)[^ad18]. On the network, the station code is **`SBGL`**.

| | |
| :--- | :--- |
| **Station code** | `SBGL` |
| **Who operates it** | SBGL_DEL. Without DEL, whichever position covers clearance top-down (GND, TWR, APP or ACC) |
| **Controller tool** | TopSky DCL window, with your personal Hoppie ACARS code |
| **Pilot tool** | Aircraft ACARS or a Hoppie-compatible client, sending the clearance request to `SBGL` |

**How it works:**

1. The pilot sends the request (RCD) to `SBGL`, with the stand and the ATIS letter.
2. The controller checks the flight plan and replies with the clearance: limit, runway, SID, squawk, ATIS letter and next frequency.
3. The pilot accepts (`WILCO`/`ACCEPT`). The clearance is then delivered and **no voice readback is needed**.
4. Once the clearance is accepted, the pilot calls Apron (or Ground, without Apron) for start-up or pushback.

!!! tip "Controller setup"
    - Log in to the TopSky DCL with the code `SBGL` before opening the position.
    - Announce it in the controller information: `DCL AVBL LOGON SBGL`.
    - A request with errors (invalid plan, wrong SID, no ATIS) is answered with **REVERT TO VOICE**: the pilot calls Clearance on frequency.
    - If the pilot does not accept within a reasonable time, treat the clearance as not delivered and call by voice.

[^ad18]: [AIP Brasil, AD 2 SBGL 2.18](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-map-marker-radius: Areas of responsibility

<figure markdown="span">
  ![SBGL map with the runway strips in yellow, under Tower, aprons 1, 2, 3 and 5 in green, under Apron, and the rest in blue, under Ground](img/sbgl-responsabilidade.svg){ loading=lazy }
  <figcaption>Yellow strips: Tower. Green: Apron (events only). Everything else: Ground. The dashed line runs through the runway holding points. White circles: apron numbers.</figcaption>
</figure>

| Position | Responsible for |
| :--- | :--- |
| **APRON** (events only) | Aprons **1, 2, 3 and 5**, up to the apron exit |
| **GND** | TWY **B**, **K**, **N**, **M** and the links up to the **holding point**; aprons 6, 7 and 8. Without APRON, also aprons 1, 2, 3 and 5 |
| **TWR** | Both runways, the **15/33 crossings** and the taxiways inside the holding points |

- With Apron online, aircraft bound for aprons 1, 2, 3 and 5 **call Apron before entering** the apron[^ad18].
- **Departure:** Apron hands the aircraft to Ground at the apron exit; Ground hands it to Tower **before the holding point**.
- **Arrival:** after vacating, Tower hands the aircraft to Ground; Ground hands it to Apron before the apron entry.
- Transponder in **ALT RPTG** and ADS-B (if equipped) at all times on aprons, taxiways and runways: surface multilateration is in use[^ad20-1].

??? info "Galeão Apron area of responsibility"
    ![Galeão Apron area of responsibility](SBGL-Apron.png){ loading=lazy }

---

## :material-transit-connection-variant: Ground flow

!!! abstract "General rule"
    - **TWY B** runs along 15/33 and links aprons 2, 3 and 5 to the runway 15 and 33 ends. **K** and **Y** run between B and the terminals.
    - **N** and **M** run along 10/28. **L1** links apron 1 to N, which leads to the runway 10 threshold via **P**.
    - **L2** to **L5** link the aprons to B.

=== "Segregated operations (landing 15, takeoff 10)"

    <figure markdown="span">
      ![Ground flow in segregated operations: departures via L1, N and P to the runway 10 threshold; landings on 15 vacating via D or E](img/sbgl-fluxo-15-10.svg){ loading=lazy }
      <figcaption>Green: departures. Dashed orange: wingspan above 36 m. Blue: arrivals.</figcaption>
    </figure>

    - **Departures (10):** **L1**, **N** and **P** to the runway 10 threshold.
    - **Wingspan above 36 m (10):** leave apron 2 via **L3**, then **K**, **N** and **P**.
    - **Landings (15):** vacate via **D** or **E** and continue on **B** to the apron link (L2 to L5).

    Example: `GLO1234, taxi to holding point runway 10 via L1, N, P.`

=== "Converging operations (landing 28, takeoff 33)"

    <figure markdown="span">
      ![Ground flow in converging operations: departures via B to G, runway 33 threshold; landings on 28 vacating via DD or BB and continuing on N to L1](img/sbgl-fluxo-28-33.svg){ loading=lazy }
      <figcaption>Green: departures. Dashed orange: wingspan above 36 m. Blue: arrivals. Red bar: mandatory hold before crossing 15/33.</figcaption>
    </figure>

    - **Departures (33):** **B** southeastbound to **G**, at the runway 33 end.
    - **Wingspan above 36 m (33):** **B** to **F**, cross 15/33 with Tower clearance, **J**, across apron 5 and enter via **H**. B between F and G is limited to 36 m.
    - **Landings (28):** vacate via **DD** or **BB** and continue westbound on **N** to **L1**.

    Example: `TAM3456, taxi to holding point runway 33 via L4, B, G.`

### Runway exits

Pilots must adjust their landing for minimum runway occupancy (MROT), especially at busy times[^ad20-8].

| Runway | Exits |
| :---: | :--- |
| **15** | **D** (~1390 m) or **E** (~1890 m) |
| **33** | **C** (~1960 m) |
| **10** | **AA** (~1090 m) or **CC** (~2060 m) |
| **28** | **DD** (~1170 m) or **BB** (~2080 m) |

<small>Approximate distance from the threshold to the exit, measured on the diagram.</small>

### Taxi restrictions

| Restriction | Where |
| :--- | :--- |
| **Maximum wingspan 36 m** | **Apron 1** and TWY **Y1**, **Y2**, **Y3** and **Y4**[^ad28] |
| **Maximum wingspan 36 m** | TWY **B** between **F** and **G**. Larger aircraft only with a *follow-me*[^ad28] |
| **Stop bars** | **K** between L2 and L3; **M** between K and L1, between L1 and P and between P and Q; **N** between L1 and P and between Q and S; **T** between N and M[^ad29] |

!!! danger "Hotspots"
    - **HS1:** pilots crossing 15/33 via **F** and **J** have entered the runway without clearance. Cross only with explicit Tower clearance.
    - **HS2 and HS3:** on **AA** and **CC**, watch out for inadvertently re-entering the active 10/28.

[^ad20-8]: [AIP Brasil, AD 2 SBGL 2.20, items 2 and 8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad28]: [AIP Brasil, AD 2 SBGL 2.8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) and ADC chart.
[^ad29]: [AIP Brasil, AD 2 SBGL 2.9](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Hotspots: ADC chart.

---

## :material-airplane-takeoff: Takeoff points

<figure markdown="span">
  ![SBGL overview with numbered aprons and the takeoff points marked with the available TORA](img/sbgl-visao-geral.svg){ loading=lazy }
  <figcaption>Takeoff points (purple) with the available TORA. Circled numbers: aprons.</figcaption>
</figure>

| Runway | Point | TORA |
| :---: | :---: | :---: |
| **10** | **P** (threshold) | 4000 m |
| **28** | **Z** (threshold) | 4000 m |
| **15** | **A** (start of the runway) | 3060 m |
| **33** | **G** or **H** (start of the runway) | 3050 m |

- Pilots reach the holding point **ready for departure**; if not, they tell ATC in advance[^ad20-2].
- Start the takeoff roll within **10 seconds** of the takeoff clearance[^ad20-2].
- RBAC 121 aircraft may be cleared for **simultaneous** departures from SBRJ runway 02 and SBGL runway 15[^ad22].

[^ad22]: [AIP Brasil, AD 2 SBGL 2.22](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-call-merge: Converging operations

Tower may activate **simultaneous operations on runways 28 and 33**, always **segregated**: landings on **28** and takeoffs from **33**[^ad20-2].

**Conditions (all)**[^ad20-2]:

- Visibility at or above the procedure minimum and ceiling at least **100 ft above the DH**.
- The operation is announced on the **ATIS** (or by radio, without ATIS) when traffic enters the TMA.
- A specific approach chart in use, with **"Converging"** in its name (e.g. *IAC ILS U (Converging) RWY 28*). These charts have the missed approach point moved back from the threshold.

**Pilots must**[^ad20-2]:

- Tell APP **on first contact** if they cannot fly the "Converging" approach.
- On a go-around after the MAPT, **turn before the limiting radial** on the chart. If unable, tell APP or Tower.

### Cut-off point

The point on the 28 final that the approaching aircraft must not yet have passed for Tower to clear a takeoff from 33. Beyond it, nobody takes off from 33 until the aircraft has landed or gone around.

| Condition | Cut-off point |
| :--- | :---: |
| **IMC** | **3 NM** from the runway 28 threshold |
| **VMC** (ceiling ≥ 1500 ft and visibility ≥ 5000 m) | **1.4 NM** from the runway 28 threshold |

<small>Cut-off point and phraseology: TWR-GL operational model, referenced in the AIP[^ad20-2].</small>

On a go-around after the MAPT on 28, separation from the aircraft taking off from 33 may be reduced. In VMC, visual separation may work; give **essential traffic information** as early as possible.

=== "To the aircraft going around"
    ```
    PTATC, turn right for the missed approach procedure, essential local traffic, B737 starting takeoff runway 33.
    PTATC, turn right for the missed approach procedure, essential local traffic, B737 taking off runway 33, passing midfield.
    PTATC, turn right for the missed approach procedure, essential local traffic, B737 taking off runway 33, crossing threshold 15.
    ```

=== "To the departing aircraft"
    ```
    PTATC, traffic, B737 going around runway 28, caution essential local traffic, passing threshold 28.
    PTATC, traffic, B737 going around runway 28, caution essential local traffic, passing midfield.
    ```

---

## :material-sign-direction: Aprons and airlines

A reference for simulation. Stands follow the PDC charts and the AIP; airlines follow the [airport's airline list on Wikipedia](https://en.wikipedia.org/wiki/Rio_de_Janeiro/Gale%C3%A3o_International_Airport#Airlines_and_destinations). The split between stands is a simplification, not the airport's official allocation. **VAs** use the stands of the real airline they represent.

<div class="patios">
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Aprons 1 and 2"><small>Apron</small>1·2</span><span class="patio__info"><strong>Terminals 1 and 2</strong><span>Domestic · apron 1 up to 36 m wingspan</span><span class="patio__pos">Stands 23 to 45</span></span></header>
<div class="patio__cias"><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="/images/cias/GLO.gif" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="/images/cias/AZU.gif" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure></div>
</section>
<section class="patio patio--largo">
<header class="patio__cab"><span class="patio__num" title="Apron 3"><small>Apron</small>3</span><span class="patio__info"><strong>Terminal 2 · South Pier</strong><span>International</span><span class="patio__pos">Stands 46 to 84</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="/images/cias/GLO.gif" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="/images/cias/AZU.gif" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure><figure class="cia" title="LATAM Chile (LAN)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM Chile" loading="lazy"><figcaption>LAN</figcaption></figure><figure class="cia" title="LATAM Perú (LPE)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM Perú" loading="lazy"><figcaption>LPE</figcaption></figure><figure class="cia" title="Aerolíneas Argentinas (ARG)"><img class="off-glb" src="/images/cias/ARG.gif" alt="Aerolíneas Argentinas" loading="lazy"><figcaption>ARG</figcaption></figure><figure class="cia" title="Avianca (AVA)"><img class="off-glb" src="/images/cias/AVA.png" alt="Avianca" loading="lazy"><figcaption>AVA</figcaption></figure><figure class="cia" title="BoA (BOV)"><img class="off-glb" src="/images/cias/BOV.gif" alt="BoA" loading="lazy"><figcaption>BOV</figcaption></figure><figure class="cia" title="Copa (CMP)"><img class="off-glb" src="/images/cias/CMP.gif" alt="Copa" loading="lazy"><figcaption>CMP</figcaption></figure><figure class="cia" title="JetSMART (JAT)"><img class="off-glb" src="/images/cias/JAT.png" alt="JetSMART" loading="lazy"><figcaption>JAT</figcaption></figure><figure class="cia" title="SKY Airline (SKU)"><img class="off-glb" src="/images/cias/SKU.png" alt="SKY Airline" loading="lazy"><figcaption>SKU</figcaption></figure><figure class="cia" title="Paranair"><span class="cia__texto">Paranair</span></figure><figure class="cia" title="American Airlines (AAL)"><img class="off-glb" src="/images/cias/AAL.gif" alt="American Airlines" loading="lazy"><figcaption>AAL</figcaption></figure><figure class="cia" title="Delta (DAL)"><img class="off-glb" src="/images/cias/DAL.jpg" alt="Delta" loading="lazy"><figcaption>DAL</figcaption></figure><figure class="cia" title="United (UAL)"><img class="off-glb" src="/images/cias/UAL.gif" alt="United" loading="lazy"><figcaption>UAL</figcaption></figure><figure class="cia" title="Air Canada (ACA)"><img class="off-glb" src="/images/cias/ACA.gif" alt="Air Canada" loading="lazy"><figcaption>ACA</figcaption></figure><figure class="cia" title="Air Transat (TSC)"><span class="cia__texto">Air Transat</span><figcaption>TSC</figcaption></figure><figure class="cia" title="Air France (AFR)"><img class="off-glb" src="/images/cias/AFR.gif" alt="Air France" loading="lazy"><figcaption>AFR</figcaption></figure><figure class="cia" title="KLM (KLM)"><img class="off-glb" src="/images/cias/KLM.gif" alt="KLM" loading="lazy"><figcaption>KLM</figcaption></figure><figure class="cia" title="British Airways (BAW)"><img class="off-glb" src="/images/cias/BAW.gif" alt="British Airways" loading="lazy"><figcaption>BAW</figcaption></figure><figure class="cia" title="Iberia (IBE)"><img class="off-glb" src="/images/cias/IBE.gif" alt="Iberia" loading="lazy"><figcaption>IBE</figcaption></figure><figure class="cia" title="ITA Airways (ITY)"><img class="off-glb" src="/images/cias/ITY.jpg" alt="ITA Airways" loading="lazy"><figcaption>ITY</figcaption></figure><figure class="cia" title="Lufthansa (DLH)"><img class="off-glb" src="/images/cias/DLH.png" alt="Lufthansa" loading="lazy"><figcaption>DLH</figcaption></figure><figure class="cia" title="TAP (TAP)"><img class="off-glb" src="/images/cias/TAP.gif" alt="TAP" loading="lazy"><figcaption>TAP</figcaption></figure><figure class="cia" title="Emirates (UAE)"><img class="off-glb" src="/images/cias/UAE.gif" alt="Emirates" loading="lazy"><figcaption>UAE</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Aprons 1, 2 and 3"><small>Apron</small>1·2·3</span><span class="patio__info"><strong>Remote</strong><span>Overnight and overflow</span><span class="patio__pos">Stands 85 to 149</span></span></header>
<div class="patio__cias"><p class="patio__nota">Any airline, subject to availability and wingspan.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 5"><small>Apron</small>5</span><span class="patio__info"><strong>Cargo terminal</strong><span>Freighters, general aviation and extended stays</span><span class="patio__pos">Stands 1 to 31</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM Cargo (LCO)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM Cargo" loading="lazy"><figcaption>LCO</figcaption></figure><figure class="cia" title="Atlas Air (GTI)"><img class="off-glb" src="/images/cias/GTI.png" alt="Atlas Air" loading="lazy"><figcaption>GTI</figcaption></figure><figure class="cia" title="Cargolux (CLX)"><img class="off-glb" src="/images/cias/CLX.png" alt="Cargolux" loading="lazy"><figcaption>CLX</figcaption></figure><figure class="cia" title="Total (TTL)"><span class="cia__texto">Total</span><figcaption>TTL</figcaption></figure><figure class="cia" title="Modern Logistics (MWM)"><span class="cia__texto">Modern</span><figcaption>MWM</figcaption></figure><figure class="cia" title="Sky Lease Cargo (KYE)"><span class="cia__texto">Sky Lease</span><figcaption>KYE</figcaption></figure><figure class="cia" title="Aerotranscargo"><span class="cia__texto">Aerotrans</span></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 6"><small>Apron</small>6</span><span class="patio__info"><strong>Maintenance</strong><span>Hangars by TWY L7</span></span></header>
<div class="patio__cias"><p class="patio__nota">Aircraft under maintenance.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Aprons 7 and 8"><small>Apron</small>7·8</span><span class="patio__info"><strong>Galeão Air Base</strong><span>Military · 8: National Air Mail (CAN)</span></span></header>
<div class="patio__cias"><figure class="cia" title="Brazilian Air Force (FAB)"><span class="cia__texto">FAB</span></figure></div>
</section>
</div>

- Aprons 1, 2 and 3 take domestic and international commercial aviation, general aviation, air taxi and government aircraft. Apron 5 takes freighters, general aviation, extended stays, military transport and aircraft undergoing customs clearance[^ad28].
- Aircraft with a wingspan above 36 m do not use apron 1[^ad28].

<small>Logos from [GRU Airport](https://www.gru.com.br/pt/passageiro/descubra-gru/cias-aereas) and [Travelpayouts](https://pics.avs.io) (Cargolux and Atlas Air). Trademarks belong to their respective airlines.</small>

---

## :material-clipboard-text-outline: Other procedures

### Approaches and landings

- Vacate the runway as quickly as possible (MROT)[^ad20-8].
- Pilots **do not report** gear down, except in an emergency.

### Aerodrome regulations

- **Touch-and-go** by civil and military aircraft only **daily between 0300 and 0800 UTC** and on **Tuesdays, Wednesdays and Saturdays between 1400 and 1600 UTC**[^ad20-1].
- **Restricted** aircraft: no radio, gliders, no transponder (or transponder failure) and powered ultralights[^ad20-1].
- **Restricted** air services: object dropping or spraying, aerial towing, parachute dropping and aerobatic flight[^ad20-1].
- Engine run-ups prohibited at the parking area of the military AIS office at Galeão Air Base[^ad20-1].
- Follow the VAC to join and leave the traffic pattern[^ad23].

[^ad17]: [AIP Brasil, AD 2 SBGL 2.17](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad23]: [AIP Brasil, AD 2 SBGL 2.23](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

<small>Diagrams drawn by VATSIM Brasil on [OpenStreetMap](https://www.openstreetmap.org/copyright) geometry (ODbL), checked against the SBGL ADC and PDC charts. Not for real-world navigation. Normative source: AIP Brasil, AD 2 SBGL, AMDT 2610A1.</small>
