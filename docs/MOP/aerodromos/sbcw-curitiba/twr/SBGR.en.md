---
title: SBGR - Guarulhos
tags:
    - Aeródromo
    - Controlado
    - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General Information

|                              | Information                                   |
|------------------------------|-----------------------------------------------|
| **Aerodrome name**           | Governador André Franco Montoro               |
| **Type of Operation**        | International, Public and Military            |
| **Transition altitude**      | 8000 ft                                       |
| **Elevation**                | 2461 ft (750 m)                               |
| **Reference code**           | 4E (B747-8 and A380 with special authorization)[^ad23] |
| **Airspace**                 | Guarulhos CTR, class D, GND/3600 ft[^ad17]    |
| **Operation**                | IFR. Fixed-wing VFR prohibited, except Brazilian military[^ad22] |
| **Accepts A380?** | :material-check:{ style="color:#12a150" }[^ad23] |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Select one of the tools in the tabs above (Charts, Weather or Traffic) to access the aerodrome information.

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBGR?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Weather"
    <div id="metar-taf-container" data-airport="SBGR" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Loading METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Loading TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBGR){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

---

## :material-routes: Runways

### Preferred runways

The two runways are parallel and only 375 m apart, centreline to centreline. That is why there are **no independent operations**: normally one runway is for landing and the other for takeoff[^ad20-1].

<div class="grid cards" markdown>

-   :material-airplane-landing:{ .lg .middle } **Landings: `10R` / `28L`**

    ---

    South runway, 3000 × 45 m. Preferred for **landing**. ILS CAT III on 10R and CAT I on 28L.

-   :material-airplane-takeoff:{ .lg .middle } **Takeoffs: `10L` / `28R`**

    ---

    North runway, 3700 × 45 m, next to the aprons. Preferred for **takeoff**. ILS CAT II on 10L and CAT I on 28R.

</div>

!!! warning "Preferred system: runways 10"
    With a {==**tailwind component of less than 7 kt**==} and a **dry runway**, the preferred system is **10R/10L**, used in preference to 28L/28R[^ad20-1].

    With system 10 in use and a tailwind, pilots who request system 28 must expect a **delay** in landing or takeoff[^ad20-1].

| Configuration | Landing | Takeoff | When |
| :--- | :---: | :---: | :--- |
| **10** (preferred) | **10R** | **10L** | Tailwind < 7 kt and dry runway |
| **28** | **28L** | **28R** | Other cases (tailwind ≥ 7 kt on 10 or runway not dry), according to the wind |

### Runway data

| Runway | Dimensions | TORA | LDA | Approach | Remarks |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **10L** | 3700 × 45 m | 3700 m | 3610 m | ILS CAT II, RNP | Threshold displaced 90 m |
| **28R** | 3700 × 45 m | 3700 m | 3640 m | ILS CAT I, RNP | Threshold displaced 60 m |
| **10R** | 3000 × 45 m | 3000 m | 3000 m | ILS CAT III, RNP | TODA 3300 m (300 m clearway) |
| **28L** | 3000 × 45 m | 3000 m | 3000 m | ILS CAT I, RNP | |

[^ad20-1]: [AIP Brasil, AD 2 SBGR 2.20, item 1.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Declared distances: AD 2.13 and ADC chart.

---

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| :--- | :---: | :--- | :---: | :--- |
| **SBGR_ATIS** | `AGR` | ATIS | **127.750** | D-ATIS |
| **SBGR_DEL** | `DGR` | Guarulhos Clearance | **121.000** | `DCL` (code `SBGR`) |
| **SBGR_GND** | `GGR` | Guarulhos Ground | **121.700** | |
| **SBGR_TWR** | `TGR` | Guarulhos Tower | **132.750** | |

### DCL

SBGR has **DCL** (departure clearance via datalink). On the network, the station code is **`SBGR`**.

| | |
| :--- | :--- |
| **Station code** | `SBGR` |
| **Who operates it** | SBGR_DEL. Without DEL, whichever position covers clearance top-down (GND, TWR, APP or ACC) |
| **Controller tool** | TopSky DCL window, with your personal Hoppie ACARS code |
| **Pilot tool** | Aircraft ACARS or a Hoppie-compatible client, sending the clearance request to `SBGR` |
| **Timing** | Request no earlier than **15 minutes before EOBT**[^ad20-7] |

**How it works:**

1. The pilot sends the request (RCD) to `SBGR`, with the stand and the ATIS letter.
2. The controller checks the flight plan and replies with the clearance: limit, runway, SID, squawk, ATIS letter and next frequency.
3. The pilot accepts (`WILCO`/`ACCEPT`). The clearance is then delivered and **no voice readback is needed**.
4. Once the clearance is accepted, the pilot calls Ground directly for start-up or pushback.

!!! tip "Controller setup"
    - Log in to the TopSky DCL with the code `SBGR` before opening the position.
    - Announce it in the controller information: `DCL AVBL LOGON SBGR`.
    - A request with errors (invalid plan, wrong SID, no ATIS) is answered with **REVERT TO VOICE**: the pilot calls Clearance on frequency.
    - If the pilot does not accept within a reasonable time, treat the clearance as not delivered and call by voice.

!!! info "Intersection takeoff in the clearance request"
    Pilots **must say when requesting clearance** if they cannot take off from the published intersections (see [Takeoff points](#takeoff-points)). In a DCL, this goes in the free-text field of the request[^ad20-1-2].

[^ad20-7]: [AIP Brasil, AD 2 SBGR 2.20, item 7.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-1-2]: [AIP Brasil, AD 2 SBGR 2.20, items 1.2.3.5 and 1.2.3.6](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-map-marker-radius: Areas of responsibility

<figure markdown="span">
  ![SBGR map with the runway strip in yellow, under Tower, and the rest in blue, under Ground](img/sbgr-responsabilidade.svg){ loading=lazy }
  <figcaption>Yellow strip: Tower. Blue area: Ground. The dashed line runs through the runway holding points.</figcaption>
</figure>

The split follows the **runway holding points**. Everything between the holding points north of 10L/28R and south of 10R/28L belongs to Tower.

| Position | Responsible for |
| :--- | :--- |
| **GND** | Aprons 1 to 10, TWY **A** and **B**, Y taxilanes, TWY V and M and the links (G, H, I, J, K, L, N, O, P, Q) **up to the 10L/28R holding point**. South side: aprons 12 and 13 and TWY S, T and U **up to the 10R/28L holding point** |
| **TWR** | Both runways, all **crossings**, the rapid exits **BB, CC, DD, FF** and the taxiways **between the runways** (C, D, E and the parts of G, BB, CC and O between 10L and 10R) |

**Handoff points** (numbers on the map):

1. **Arrival on 10R/28L bound for the north aprons:** the aircraft stays on Tower frequency, holds and crosses 10L/28R with Tower clearance and **only calls Ground after crossing and vacating 10L/28R**[^ad20-1-2-4].
2. **Departure:** Ground hands the aircraft to Tower **before the holding point** of the departure runway. To ease frequency load, Ground may instruct the pilot to **monitor** Tower, without an initial call[^ad20-6].
3. **Arrival bound for aprons 12 and 13:** the aircraft vacates 10R/28L to the south (T or U) and calls Ground after vacating.

!!! warning "Crossing the adjacent runway"
    - An aircraft vacating a runway must **NEVER** cross the parallel runway without specific ATC clearance.
    - An aircraft holding to cross stays on **Tower** frequency and **does not request** the crossing: Tower will call.
    - Once cleared, cross promptly. Single-engine taxi is not allowed before crossing[^ad20-1-2-4].

[^ad20-1-2-4]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2.4](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-6]: [AIP Brasil, AD 2 SBGR 2.20, item 6.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-transit-connection-variant: Ground flow

!!! abstract "General rule"
    - **TWY A** is the standard route, in both directions, between the aprons and the runway ends.
    - **TWY B** is the **alternative**: use it when A is busy or closed, to pass a stopped aircraft or to keep opposite flows apart.
    - The links between A, B and the runway (G, H, L, N, O, P, Q) are used to enter and vacate. Rapid exits BB, CC, DD and FF are **for vacating only**.

=== "Configuration 10 (landing 10R, takeoff 10L)"

    <figure markdown="span">
      ![Ground flow in configuration 10: departures via TWY A to G and H; arrivals on 10R vacating via BB, CC or O and crossing 10L via L, N or O](img/sbgr-fluxo-10.svg){ loading=lazy }
      <figcaption>Green: departures, from the apron exit to the runway. Blue: arrivals. Red bar: mandatory hold before crossing the runway. Dashed orange: alternative via TWY B.</figcaption>
    </figure>

    - **Departures (10L):** taxi via **A** westbound to **G** (full length) or **H** (intersection).
    - **Arrivals (10R):** CAT C, D and E vacate via **BB**, **CC** or **O** (end of the runway), hold short of 10L and cross via **L**, **N** or **O** onto A. CAT A and B vacate via **T** or **U**, to the south.
    - **Aprons 12 and 13:** via **S** to **G**, crossing 10R with Tower clearance, to the 10L holding point on G.
    - **Alternative:** **B** westbound to H or G.

    Example: `TAM3456, taxi to holding point runway 10L via A, G.`

=== "Configuration 28 (landing 28L, takeoff 28R)"

    <figure markdown="span">
      ![Ground flow in configuration 28: departures via TWY A to Q and P; arrivals on 28L vacating via G and crossing 10L via G](img/sbgr-fluxo-28.svg){ loading=lazy }
      <figcaption>Green: departures, from the apron exit to the runway. Blue: arrivals. Red bar: mandatory hold before crossing the runway. Dashed orange: alternative via TWY B.</figcaption>
    </figure>

    - **Departures (28R):** taxi via **A** eastbound to **Q** (full length), **P** or **O** (intersections).
    - **Arrivals (28L):** CAT C, D and E vacate via **G**, hold short of 10L and cross via **G** onto A. CAT A and B vacate via **T** or **U**, to the south.
    - **Aprons 12 and 13:** via **S** to **G**, crossing 10R and 10L with Tower clearance, then via **A**.
    - **Alternative:** **B** eastbound to P or Q.

    Example: `GLO1234, taxi to holding point runway 28R via A, Q.`

### Runway exits

To ensure minimum runway occupancy time (MROT), pilots must vacate via the taxiways below or tell Tower **on first contact** if they cannot[^ad20-1-2-2].

| Runway | CAT A and B | CAT C and D | CAT E |
| :---: | :--- | :--- | :--- |
| **10R** | T (1497 m) or U (1795 m) | BB or CC (2450 m) or O (3000 m, end of the runway) | BB, CC or O |
| **10L** | L (1061 m) | N (2212 m) or O (2397 m) | N, O or FF (2840 m) |
| **28R** | O (1155 m) or N (1340 m) | L (1951 m) or DD (2340 m) | L or DD |
| **28L** | T (1502 m) or U (1204 m) | G (2487 m) | G |

<small>Distance from the threshold to the exit taxiway.</small>

### Taxi restrictions

- **TWY S, T and U:** wingspan above 44 m only under tow[^ad20-12].
- **Code F:** no taxiing on A between G and apron 1, on the Y taxilanes of aprons 1 to 5, on TWY M and V, or on G between 10R/28L and apron 12. TWY V and A between G and apron 1: maximum wingspan 65 m[^ad20-12].
- No turning where there are no matching markings and lights[^ad20-1-2-4].
- **Low visibility (RVR < 400 m):** taxi with the *Follow-me* vehicle as per the AIP, on the standard taxi routes[^ad20-16].

[^ad20-1-2-2]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2.2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-12]: [AIP Brasil, AD 2 SBGR 2.20, item 12](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) and AD 2.8.
[^ad20-16]: [AIP Brasil, AD 2 SBGR 2.20, item 16](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-airplane-takeoff: Takeoff points

<figure markdown="span">
  ![SBGR overview with numbered aprons and the takeoff points marked with the available TORA](img/sbgr-visao-geral.svg){ loading=lazy }
  <figcaption>Takeoff points (purple) with the available TORA. Circled numbers: aprons.</figcaption>
</figure>

Aircraft of **category D or smaller** must be ready to take off from the intersections below[^ad20-1-2-3]. In practice, Tower uses the intersection to fit departures between arrivals.

| Runway | Point | TORA | Used by |
| :---: | :---: | :---: | :--- |
| **10L** | **G** (full length) | 3700 m | Aprons 1 and 2, CAT E and anyone unable to accept the intersection |
| **10L** | **H** | **3400 m** | Aircraft from **aprons 3, 4, 5, 6 and 7** |
| **28R** | **Q** (full length) | 3700 m | CAT E and anyone unable to accept the intersection |
| **28R** | **P** | **3460 m** | CAT D or smaller |
| **28R** | **O** | **2397 m** | CAT D or smaller |
| **10R** | **G** | **2487 m** | Dependent parallel departures (see below) |

- Pilots say **when requesting clearance** if they cannot take off from the intersection[^ad20-1-2].
- Pilots reach the holding point **ready for departure**; if not, they tell Ground.
- Line up **immediately** when cleared, and start the takeoff roll within **10 seconds** of the takeoff clearance.
- Tower **does not give** landing and takeoff times[^ad22-8].

[^ad20-1-2-3]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2.3](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad22-8]: [AIP Brasil, AD 2 SBGR 2.22, item 8.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-call-split: Segregated operations

In **segregated operations**, 10R/28L takes the landings and 10L/28R the takeoffs **at the same time**. Because the runways are only 375 m apart, a go-around from one and a takeoff from the other may conflict. That is why separation between them is **visual**, kept by the pilot of the aircraft going around[^ad20-3].

**Conditions**[^ad20-3]:

| Condition | Value |
| :--- | :--- |
| Weather | **VMC**, ceiling ≥ **1000 ft** and visibility ≥ **5000 m** |
| Divergence | Departure and missed approach paths diverge by at least **15°** |
| Wake on final | The aircraft on final approach must **not** be **HEAVY** |
| Wake on runway 28 departures | The aircraft taking off from RWY 28 must **not** be **HEAVY** |
| Publication | Operation in progress and IAC in use announced on the **ATIS** (or on VHF, without ATIS) |

Outside these conditions there are no segregated operations: Tower separates landings and takeoffs on the two runways without relying on visual separation.

**The pilot-in-command must**[^ad20-3]:

1. Tell Tower if **visual references are lost** on final. Without a report, ATC assumes the pilot has visual references below 1000 ft and will apply visual separation in case of a go-around.
2. In a go-around, **maintain visual separation** from the aircraft taking off from the adjacent runway.
3. Keep the other aircraft in sight until it is no longer essential traffic.
4. Observe wake turbulence separation when told to maintain visual separation, and ask for extra spacing if needed.
5. Add **HEAVY** or **SUPER** right after the callsign on initial contact, when applicable.

**Go-around phraseology**[^ad20-3]:

=== "Portuguese"
    To the aircraft **going around**:

    ```
    PTATC, tráfego, B757 decolando da pista 10L, mantenha separação visual, atento à esteira de turbulência.
    ```

    To the **departing** aircraft:

    ```
    PTATC, tráfego, B757 arremetendo da pista 28L, mantenha separação visual, atento à esteira de turbulência.
    ```

=== "English"
    To the aircraft **going around**:

    ```
    PTATC, traffic, B757 departing runway 10L, maintain visual separation, caution wake turbulence.
    ```

    To the **departing** aircraft:

    ```
    PTATC, traffic, B757 going around runway 28L, maintain visual separation, caution wake turbulence.
    ```

### Dependent parallel departures

When there are more departures than arrivals, Tower may launch from **both runways** (10R/10L or 28L/28R)[^ad20-5]:

- Minima: visibility ≥ **5000 m** and ceiling ≥ **1000 ft**.
- Departure paths diverge by at least **15°** up to 2 NM from the end of the runway.
- Operation announced on the **ATIS**.
- Pilots say at clearance if they cannot operate on 10R/28L and, for code C or D, when requesting taxi if they cannot take off from **H** (10L), **G** (10R) or **P** (28R). On first contact with São Paulo Control they state the departure runway.

[^ad20-3]: [AIP Brasil, AD 2 SBGR 2.20, item 3](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-5]: [AIP Brasil, AD 2 SBGR 2.20, item 5](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-arrow-collapse-horizontal: RRSM

**RRSM** (*Reduced Runway Separation Minima*) is the reduced minimum separation between aircraft **on the same runway**. With RRSM, Tower may clear a landing or takeoff **before the preceding aircraft has vacated the runway**, provided there is reasonable assurance that the distance below will exist. SBGR was the first aerodrome in Brazil to use it[^ad20-4].

**Conditions (all of them)**[^ad20-4]:

- From **sunrise to sunset**.
- Visibility ≥ **5 km** and ceiling ≥ **1000 ft**.
- Tailwind **up to 3 kt**.
- Braking action **not affected** by contaminants (water, ice, snow).
- **Wake turbulence** minima applied as usual.
- RRSM announced on the **ATIS**.

**Minimum distance: 2400 m from the threshold**, which corresponds to:

| Runway in use | Landing after landing | Landing after takeoff / takeoff after takeoff |
| :---: | :--- | :--- |
| **10R** | Preceding aircraft past **CC**, moving and vacating without backtracking | Preceding aircraft past **CC** |
| **28L** | Preceding aircraft past **G**, moving and vacating without backtracking | Preceding aircraft past **G** |
| **10L** | Preceding aircraft past **O**, moving and vacating without backtracking | Preceding aircraft past **O** |
| **28R** | Preceding aircraft past **DD**, moving and vacating without backtracking | Preceding aircraft past **DD** |

Tower gives **traffic information** with the clearance:

=== "Portuguese"
    ```
    TAM3456, autorizado pouso pista 10R, vento 090 graus 11 nós, B747 à frente liberando a pista.
    TAM3456, autorizado pouso pista 28L, vento 230 graus 6 nós, MD11 à frente decolando.
    GLO1234, autorizado decolagem pista 28R, vento 230 graus 6 nós, MD11 à frente decolando.
    ```

=== "English"
    ```
    TAM3456, runway 10R cleared to land, wind 090 degrees 11 knots, B747 ahead vacating the runway.
    TAM3456, runway 28L cleared to land, wind 230 degrees 6 knots, MD11 departing ahead.
    GLO1234, runway 28R cleared for takeoff, wind 230 degrees 6 knots, MD11 departing ahead.
    ```

[^ad20-4]: [AIP Brasil, AD 2 SBGR 2.20, item 4.2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). See also the [DECEA news item](https://decea.mil.br/?i=midia-e-informacao&materia=aeroporto-de-guarulhos-e-o-primeiro-do-brasil-a-implementar-minimos-de-separacao-reduzidos-entre-aeronaves-que-utilizam-a-mesma-pista&p=pg_noticia) (Portuguese).

---

## :material-sign-direction: Aprons and airlines

A reference for simulation, based on the real terminal layout. It is not the airport's official allocation, which changes every season. **VAs** use the aprons of the real airline they represent.

<div class="patios">
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 1"><small>Apron</small>1</span><span class="patio__info"><strong>Terminal 1</strong><span>Domestic</span><span class="patio__pos">Stands 101 to 105</span></span></header>
<div class="patio__cias"><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="https://pics.avs.io/240/80/AD.png" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 2·3"><small>Apron</small>2·3</span><span class="patio__info"><strong>Terminal 2</strong><span>Domestic and regional international</span><span class="patio__pos">Stands 201 to 212 · 301 to 312</span></span></header>
<div class="patio__cias"><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="https://pics.avs.io/240/80/G3.png" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 4"><small>Apron</small>4</span><span class="patio__info"><strong>Terminal 2</strong><span>Domestic and South America</span><span class="patio__pos">Stands 401 to 411</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="Aerolíneas Argentinas (ARG)"><img class="off-glb" src="https://pics.avs.io/240/80/AR.png" alt="Aerolíneas Argentinas" loading="lazy"><figcaption>ARG</figcaption></figure><figure class="cia" title="Avianca (AVA)"><img class="off-glb" src="https://pics.avs.io/240/80/AV.png" alt="Avianca" loading="lazy"><figcaption>AVA</figcaption></figure><figure class="cia" title="BoA (BOV)"><img class="off-glb" src="https://pics.avs.io/240/80/OB.png" alt="BoA" loading="lazy"><figcaption>BOV</figcaption></figure><figure class="cia" title="Arajet (DWI)"><img class="off-glb" src="https://pics.avs.io/240/80/DM.png" alt="Arajet" loading="lazy"><figcaption>DWI</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 1"><small>Apron</small>1</span><span class="patio__info"><strong>Cargo terminal</strong><span>Freighters</span><span class="patio__pos">Stands 106 to 115</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM Cargo (LCO)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM Cargo" loading="lazy"><figcaption>LCO</figcaption></figure><figure class="cia" title="Lufthansa Cargo (GEC)"><img class="off-glb" src="https://pics.avs.io/240/80/LH.png" alt="Lufthansa Cargo" loading="lazy"><figcaption>GEC</figcaption></figure><figure class="cia" title="Cargolux (CLX)"><img class="off-glb" src="https://pics.avs.io/240/80/CV.png" alt="Cargolux" loading="lazy"><figcaption>CLX</figcaption></figure><figure class="cia" title="Atlas Air (GTI)"><img class="off-glb" src="https://pics.avs.io/240/80/5Y.png" alt="Atlas Air" loading="lazy"><figcaption>GTI</figcaption></figure><figure class="cia" title="Qatar Airways Cargo (QTR)"><img class="off-glb" src="https://pics.avs.io/240/80/QR.png" alt="Qatar Airways Cargo" loading="lazy"><figcaption>QTR</figcaption></figure><figure class="cia" title="Turkish Cargo (THY)"><img class="off-glb" src="https://pics.avs.io/240/80/TK.png" alt="Turkish Cargo" loading="lazy"><figcaption>THY</figcaption></figure><figure class="cia" title="Emirates SkyCargo (UAE)"><img class="off-glb" src="https://pics.avs.io/240/80/EK.png" alt="Emirates SkyCargo" loading="lazy"><figcaption>UAE</figcaption></figure><figure class="cia" title="Total (TTL)"><span class="cia__texto">Total</span><figcaption>TTL</figcaption></figure></div>
</section>
<section class="patio patio--largo">
<header class="patio__cab"><span class="patio__num" title="Apron 5·6"><small>Apron</small>5·6</span><span class="patio__info"><strong>Terminal 3</strong><span>International</span><span class="patio__pos">Stands 501 to 511 · 601 to 612</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="American Airlines (AAL)"><img class="off-glb" src="https://pics.avs.io/240/80/AA.png" alt="American Airlines" loading="lazy"><figcaption>AAL</figcaption></figure><figure class="cia" title="Delta (DAL)"><img class="off-glb" src="https://pics.avs.io/240/80/DL.png" alt="Delta" loading="lazy"><figcaption>DAL</figcaption></figure><figure class="cia" title="United (UAL)"><img class="off-glb" src="https://pics.avs.io/240/80/UA.png" alt="United" loading="lazy"><figcaption>UAL</figcaption></figure><figure class="cia" title="Air France (AFR)"><img class="off-glb" src="https://pics.avs.io/240/80/AF.png" alt="Air France" loading="lazy"><figcaption>AFR</figcaption></figure><figure class="cia" title="KLM (KLM)"><img class="off-glb" src="https://pics.avs.io/240/80/KL.png" alt="KLM" loading="lazy"><figcaption>KLM</figcaption></figure><figure class="cia" title="Lufthansa (DLH)"><img class="off-glb" src="https://pics.avs.io/240/80/LH.png" alt="Lufthansa" loading="lazy"><figcaption>DLH</figcaption></figure><figure class="cia" title="British Airways (BAW)"><img class="off-glb" src="https://pics.avs.io/240/80/BA.png" alt="British Airways" loading="lazy"><figcaption>BAW</figcaption></figure><figure class="cia" title="Iberia (IBE)"><img class="off-glb" src="https://pics.avs.io/240/80/IB.png" alt="Iberia" loading="lazy"><figcaption>IBE</figcaption></figure><figure class="cia" title="TAP (TAP)"><img class="off-glb" src="https://pics.avs.io/240/80/TP.png" alt="TAP" loading="lazy"><figcaption>TAP</figcaption></figure><figure class="cia" title="Emirates (UAE)"><img class="off-glb" src="https://pics.avs.io/240/80/EK.png" alt="Emirates" loading="lazy"><figcaption>UAE</figcaption></figure><figure class="cia" title="Qatar Airways (QTR)"><img class="off-glb" src="https://pics.avs.io/240/80/QR.png" alt="Qatar Airways" loading="lazy"><figcaption>QTR</figcaption></figure><figure class="cia" title="Turkish Airlines (THY)"><img class="off-glb" src="https://pics.avs.io/240/80/TK.png" alt="Turkish Airlines" loading="lazy"><figcaption>THY</figcaption></figure><figure class="cia" title="Ethiopian (ETH)"><img class="off-glb" src="https://pics.avs.io/240/80/ET.png" alt="Ethiopian" loading="lazy"><figcaption>ETH</figcaption></figure><figure class="cia" title="Air Canada (ACA)"><img class="off-glb" src="https://pics.avs.io/240/80/AC.png" alt="Air Canada" loading="lazy"><figcaption>ACA</figcaption></figure><figure class="cia" title="Aeroméxico (AMX)"><img class="off-glb" src="https://pics.avs.io/240/80/AM.png" alt="Aeroméxico" loading="lazy"><figcaption>AMX</figcaption></figure><figure class="cia" title="Copa (CMP)"><img class="off-glb" src="https://pics.avs.io/240/80/CM.png" alt="Copa" loading="lazy"><figcaption>CMP</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 7"><small>Apron</small>7</span><span class="patio__info"><strong>Remote</strong><span>Overnight, charters and wide-body overflow</span><span class="patio__pos">Stands 701 to 715</span></span></header>
<div class="patio__cias"><p class="patio__nota">Any airline, subject to availability.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 9"><small>Apron</small>9</span><span class="patio__info"><strong>Remote, next to the hangars</strong><span>Overnight and maintenance</span><span class="patio__pos">Stands 901 to 911</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="American Airlines (AAL)"><img class="off-glb" src="https://pics.avs.io/240/80/AA.png" alt="American Airlines" loading="lazy"><figcaption>AAL</figcaption></figure><p class="patio__nota">and overflow from the other aprons.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 12"><small>Apron</small>12</span><span class="patio__info"><strong>General aviation</strong><span>Business, air taxi and helicopters</span><span class="patio__pos">Stands 1 to 12 · H1 to H3</span></span></header>
<div class="patio__cias"><p class="patio__nota">General aviation and air taxi, with prior authorization.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Apron 13"><small>Apron</small>13</span><span class="patio__info"><strong>BASP</strong><span>Military · São Paulo Air Force Base</span></span></header>
<div class="patio__cias"><figure class="cia" title="Brazilian Air Force (FAB)"><span class="cia__texto">FAB</span></figure></div>
</section>
</div>

- **General aviation** parks only on apron 12, with prior authorization from the airport; maximum stay 3 h (international) or 2 h (domestic)[^ad20-8].
- **Military** aircraft bound for BASP (apron 13) call **Guarulhos Operations (122.500)**[^ad20-8].
- **SBGR is not an alternate** for flights planned to SBSP, SBKP or other TMA-SP aerodromes, due to apron capacity, except military or coordinated flights[^ad22-8].

<small>Logos via [Travelpayouts](https://pics.avs.io), loaded from the original source. Trademarks belong to their respective airlines.</small>

[^ad20-8]: [AIP Brasil, AD 2 SBGR 2.20, item 8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) and AD 2.8.

---

## :material-clipboard-text-outline: Other procedures

### Approaches and landings

- **HIRO** (high-intensity runway operations) H24: pilots adjust landing and takeoff for minimum runway occupancy[^ad20-1-2-1].
- **Approach speeds:** **180 kt at 10 NM** and **160 kt at 5 NM** from the threshold. ATC-assigned speeds are mandatory; pilots unable to comply must say so[^ad20-2].
- Minimum surveillance separation on final: **3 NM**[^ad20-4].
- Vacate the runway **completely** before stopping.
- Pilots **do not report** gear down, except in an emergency.

### Communications

- To avoid frequency congestion, ATC may instruct pilots to **monitor** the next frequency. In that case there is **no** initial call[^ad20-6].
- Flight plans and their changes are **not** accepted by radiotelephony[^ad23].

### Aerodrome regulations

- Fixed-wing VFR **prohibited**, except Brazilian military or non-RNAV aircraft when conventional procedures are unavailable[^ad22].
- No landings or takeoffs of **turboprop and piston** aircraft between **0930–1300 UTC and 2200–0200 UTC**, except military, MEDEVAC and RBAC 121/129[^ad20-8].
- No training flights, except BASP military aircraft and authorized ILS CAT II/III training[^ad20-13].

[^ad20-1-2-1]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-2]: [AIP Brasil, AD 2 SBGR 2.20, item 2.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-13]: [AIP Brasil, AD 2 SBGR 2.20, item 13](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad17]: [AIP Brasil, AD 2 SBGR 2.17](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad22]: [AIP Brasil, AD 2 SBGR 2.22, item 1.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad23]: [AIP Brasil, AD 2 SBGR 2.23](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

<small>Diagrams drawn by VATSIM Brasil on [OpenStreetMap](https://www.openstreetmap.org/copyright) geometry (ODbL), checked against the SBGR ADC chart (AIRAC 2605). Not for real-world navigation. Normative source: AIP Brasil, AD 2 SBGR, AMDT 2610A1.</small>
