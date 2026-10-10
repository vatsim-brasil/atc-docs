---
title: SBCF - Confins
tags:
  - Aeródromo
  - Controlado
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General Information
|                              | Information                      |
|------------------------------|----------------------------------|
| **Aerodrome name**           | Confins - Tancredo Neves         |
| **Type of Operation**         | International and Public          |
| **Transition altitude** | 7000 ft |
| **Elevation** | 2721 ft (829 m) |
| **Accepts A380?** | :material-close:{ style="color:#d63d3d" } |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Select one of the tools in the tabs above (Charts, Weather or Traffic) to access the aerodrome information.

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBCF?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Weather"
    <div id="metar-taf-container" data-airport="SBCF" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Loading METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Loading TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBCF){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

## :material-routes: Runways
### Description

| Runway | Preferred                                                                      | ILS                                         | Pattern             |
| :---: | :--- | :---: | :---: |
| **16** | Preferred with **tailwind component up to 7 knots** and **dry runway**[^1]         | :fontawesome-solid-circle-check:{.corok}    | Non-standard        |
| **34** | -                                                                                  | :fontawesome-solid-circle-check:{.corok}    | Standard              |

[^1]: [AIP Brasil, AD 2 SBCF 10](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) 

!!! warning "Preferential Runway Operation"

    In weather conditions with a {==**tailwind component less than or equal to 7KT**==}, the preferred runway for landing and takeoff will be RWY 16. This configuration will normally be used in preference to RWY 34, provided that the runway surface **is dry**. When the runway in use is RWY 16 with a tailwind component, pilots requesting clearance to use RWY 34 should consider that their landing or takeoff {==**may be delayed**==}.

## :material-headset: ATC Units
| Code       | Abbr.  | Callsign              | Frequency  | Remarks     |
| ---------- | ------ | --------------------- | ---------- | ----------- |
| **SBCF_ATIS** | `ACF` | ATIS | **127.850** |  |
| **SBCF_DEL** | `DCF` | Confins Delivery | **121.000** | `DCL` |
| **SBCF_GND** | `GCF` | Confins Ground | **121.900** |  |
| **SBCF_TWR** | `TCF` | Confins Tower | **118.200** |  |

### DCL / CPDLC
- [x] DCL service is available at the aerodrome. The controller must use the code <span class="badge corVatbrzVermelho">SBCF</span> when connecting.

## :material-airplane-takeoff: Operations

### Takeoffs

- Pilots shall plan the TKOF so as to arrive at the holding point ready to carry it out. If an immediate TKOF is not possible, inform the ATC unit in advance.
- Upon receiving TKOF clearance, the pilot is expected to begin the takeoff roll immediately (the expected reaction time is up to 10 seconds).
- Confins TWR will not inform ACFT of the TKOF time. The instruction regarding the FREQ of the next unit to be called AFT TKOF and, if necessary, any additional instructions will be issued together with the TKOF AUTH.
- All takeoffs shall use a noise abatement procedure, in accordance with each aircraft's manual.
- The initial call to APP after takeoff shall be made immediately and follow only this format: *BELO HORIZONTE CONTROL [CALLSIGN]*. Do not add any information to this format.
- Turboprop and piston aircraft should expect radar vectors or clearance direct to a published waypoint shortly after takeoff.
- CAT A and B aircraft shall **compulsorily** be configured to take off from the following intersections:
    - *RWY 16:*
        * Taxiway `C1`
        * Distance from Taxiway `C1` to threshold 34: Available TORA: 2720 m
    - *RWY 34:*
        * Taxiway `H`
        * Distance from Taxiway `H` to threshold 16: Available TORA: 2987 m
    * If it is not possible to take off from the intersections above, the pilot must advise when requesting the flight plan clearance.
* Aircraft with reference code C or above may also be cleared to take off from the intersections above, upon the aircraft's request.
- For aircraft with a wingspan equal to or greater than 17m, with piston or jet engines, the use of tug push-back is **compulsory** to leave any parking stand.

### Approaches and Landings

- During LDG OPS, pilots will not report the landing gear COND to Confins TWR, EXC in EMERG situations concerning its extension and/or locking.

### Aerodrome Regulations

- OBS VAC for joining or leaving the TFC circuit.
- The following classes and types of ACFT are restricted:
    - ACFT WO EQPT RDO;
    - GLD;
    - ACFT WO transponder or with a failure of this EQPT;
    - Powered ultralight FLT.
- The following air services are restricted:
    - Dropping of objects or spraying;
    - ACFT towing;
    - Parachute dropping;
    - Aerobatic FLT.

### Aprons and Taxiways

- For aircraft with a wingspan less than or equal to 15m, **piston-engine**, **Turboprop** and **Very Light Jets (VLJ)** only, departure from parking stands `216` to `225` under own power is permitted, even with the adjacent stand occupied, with a 180-degree turn to the pilot's left.
- For aircraft with a wingspan equal to 15m and less than 17m, **piston-engine** only, departure from parking stands `216` to `224` under own power is permitted, necessarily with the adjacent stand vacant, with a 180-degree turn to the pilot's left.
- For **Cessna 208 Caravan** aircraft, departure from parking stands `216` to `225` under own power is permitted, even with the adjacent stand occupied, with a 180-degree turn to the pilot's left.

### Runways

- OBS on APCH to RWY 34: do not confuse with Lagoa Santa AD to the right of the flight path.

## :material-sign-direction: Parking Stands
| Apron     | Stands    | Classification            |
| :---: | :---: | :--- |
| **1** | ANY       | Domestic                  |
| **2** | ANY       | Domestic / International |
| **3** | ANY       | Cargo                     |
| **4** | ANY       | Maintenance - Gol          |