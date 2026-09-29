---
title: SBBR - Brasília
tags:
  - Aeródromo
  - Controlado
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General Information
|                           | Information                      |
|---------------------------|----------------------------------|
| **Aerodrome name**        | Presidente Juscelino Kubitschek  |
| **Type of Operation**     | International, Public and Military |
| **Transition altitude**   | 7000 ft |
| **Elevation** | 3498 ft (1066m) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Select one of the tools in the tabs above (Charts, Weather or Traffic) to access the aerodrome information.

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBBR?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Weather"
    <div id="metar-taf-container" data-airport="SBBR" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Loading METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Loading TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBBR){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

## :material-routes: Runways
### Description

| Runways | Preferred                                     | ILS                                      | Circuit             |
|--------|-----------------------------------------------|------------------------------------------|---------------------|
| **11L** | Preferred with **tailwind component up to 7 knots** on a **dry runway**.[^1] / Preferred for **operations** originating from or destined to locations **North** and **Northeast** of Brasília.[^1]  | :fontawesome-solid-circle-check:{.corok} | Standard |
| **29R** | Preferred for **operations** originating from or destined to locations **North** and **Northeast** of Brasília.[^1]  | :fontawesome-solid-circle-xmark:{ .cornot } | Non-standard            |
| **11R** | Preferred with **tailwind component up to 7 knots** on a **dry runway**.[^1] / Preferred for **operations** originating from or destined to locations **South** and **Southeast** of Brasília.[^1]  | :fontawesome-solid-circle-check:{.corok} | Non-standard |
| **29L** | Preferred for **operations** originating from or destined to locations **South** and **Southeast** of Brasília.[^1]  | :fontawesome-solid-circle-check:{.corok} | Standard            |

[^1]: [AIP Brasil, AD 2 SBBR 2.22](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) 

!!! warning "Preferred Runway Operation"

    In weather conditions with a {==**tailwind component less than or equal to 7KT**==}, the preferred runway for landing and takeoff will be RWY 11L/11R. This configuration will normally be used in preference to RWYS 29R/29L, provided that the runway surface **is dry**. When the runway in use is RWY 11L/11R with a tailwind component, pilots requesting clearance to use RWY 29R/29L should consider that their landing or takeoff {==**may be delayed**==}.

!!! warning "Operation During Peak Departure Periods"

    During peak departure periods for Sectors N/NE/NW, RWY 11L/29R will be used for DEP only. Approaches from all sectors and departures to Sector S will be conducted on RWY 11R/29L.

<!--
### Configurations

| Configuration | Takeoff     | Landing     | Remarks                                                                                         |
| ------------ | ----------- | ----------- | ----------------------------------------------------------------------------------------------- |
| **EAST**     | `11L` `11R` | `11L` `11R` | `11L` is prioritized for departures to the **NORTH** sector and `11R` for departures to the **SOUTH** sector |
| **WEST**     | `29L` `29R` | `29L` `29R` | `29R` is prioritized for departures to the **NORTH** sector and `29L` for departures to the **SOUTH** sector |
-->

## :material-headset: ATC Units
| Code       | Abbr.  | Callsign              | Frequency               | Remarks     |
| ---------- | ------ | --------------------- | ----------------------- | ----------- |
| **SBBR_ATIS** | `ABR` | Brasília ATIS | **127.800** |  |
| **SBBR_DEL** | `DBR` | Brasília Delivery | **121.000** | `DCL` |
| **SBBR_GND** | `GBR` | Brasília Ground | **121.800** |  |
| **SBBR_TWR** | `TBR` | Brasília Tower | **118.100** |  |
| **SBBR_M_TWR** | `OBR` | Brasília Operations | **122.500** |  |

## :material-airplane-takeoff: Operations

### Departures

- ACFT will be instructed by DEL to monitor (stand by on) the GND frequency for start-up clearance, *no initial call being required*.
- When transferring communications to TWR, GND will instruct ACFT to monitor (stand by on) the TWR frequency, no initial call being required. In this case, ACFT shall wait for TWR to call, preparing for a possible immediate takeoff.
- Pilots shall plan the TKOF so as to arrive at the holding point ready to execute it. If an immediate TKOF is not possible, inform the ATC unit in advance.
- Upon receiving TKOF clearance, the pilot is expected to begin the takeoff roll immediately (the expected reaction time is up to 10 seconds).
- TWR will not inform ACFT of the TKOF time. The instruction regarding the FREQ of the next unit to be contacted AFT TKOF and, if necessary, additional instructions, will be issued together with the TKOF AUTH.
- All departures shall use noise abatement procedures, in accordance with each aircraft's manual.
- Make the initial call to APP immediately after takeoff in order to obtain instructions to leave the departure runway centerline;
- The initial call to APP after takeoff shall be immediate and follow only this format: *BRASÍLIA CONTROL, [CALLSIGN]*. Do not include any additional information beyond this format.
- Expect vectors or clearance direct to a published waypoint shortly after takeoff.
- Aircraft of reference code A and B **shall** be configured to take off from the intersections below:
    - *RWY 11L:*
        * Aircraft of reference code A and B
            * TWY `C`
            * Distance from TWY `C` to THR 29R: TORA Available: 2193 m
    - *RWY 11R:*
        * Aircraft of reference code A and B
            * TWY `BB`
            * Distance from TWY `BB` to THR 29L: TORA Available: 2188 m
    - *RWY 29R:*
        * Aircraft of reference code A and B
            * TWY `F`
            * Distance from TWY `F` to THR 29R: TORA Available: 1956 m
    - *RWY 29L:*
        * Aircraft of reference code A and B
            * TWY `EE`
            * Distance from TWY `EE` to THR 11R: TORA Available: 2161 m
- Aircraft of reference code C or above may also be cleared to take off from the intersections above, upon the aircraft's request.
- In takeoff operations, under normal operating conditions, aircraft bound for locations **North** and **Northeast** of Brasília should use runways `11L` or `29R`, and those bound for locations **South** and **Southeast** should use `11R` or `29L`.

### Approaches and Landings

- In LDG OPS, pilots will not report the landing gear COND to TWR, EXC in EMERG situations concerning its extension and/or locking.
- Pilots should vacate the runway at the fastest speed permitted by standard operating procedures and consistent with operational safety, allowing ATC to apply minimum separation on final approach.
- In landing operations, under normal operating conditions, aircraft arriving from locations **North** and **Northeast** of Brasília should use runways `11L` or `29R`, and those arriving from locations **South** and **Southeast** should use `11R` or `29L`.

### Aerodrome Regulations

- Once the clearance has been copied, ACFT will inform DEL when they are actually ready for engine start.
- Line-up must be immediate once cleared.
Under construction.
- OBS VAC for entering or leaving the TFC circuit.

### Aprons and Taxiways

- BFR entering TWY `Q` from TWY `QQ`, CTC with TWR reporting the ACFT position is compulsory. Taxiing permitted for ACFT with wingspan up to 20m.
- TWY `L4`, `L5`, `L6`, `L8` and `R` BTN `L3` and `L7`, MAX wingspan 36M.
- General aviation ACFT with DEST to apron 02 must use the apron 02 TWY (PSN 52 to 61). At night, OPR with CTN as the apron is LGTD but has no edge lighting.
- TWY `QQ`, day and night operation under the responsibility of the ACFT OPR.

## :material-sign-direction: Parking Stands
| Apron       | Stands   | Classification                   |
| :---: | :---: | :--- |
|     `1`     |  1 - 4   | International                    |
|     `1`     |  5 - 41  | Domestic                         |
|     `2`     | 52 - 66  | Cargo / Remote                   |
|     `3`     | 67 - 70  | Large Cargo / Remote             |
| **MILITARY** | ANY    | Military - Operational           |

<!--

## Ground Flows

!!! info "Information..."

    Select the runway in use in the upper right corner of the map to view the respective ground flow.

<div id="mapa1" class="mapa"></div>

-->

<!--
From here down are the maps.
-->

<!--

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>
<script src="https://cdn.jsdelivr.net/npm/leaflet-geometryutil@0.10.2/src/leaflet.geometryutil.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/leaflet-arrowheads@1.4.0/src/leaflet-arrowheads.min.js"></script>

<style>
    .mapa { height: 480px }
</style>

<script>

const cores = {
    ciano: '#2dd4bf',
    rosa: '#f472b6',
    verde: '#a3e635',
    amarelo: '#fbbf24',
    vermelho: '#f87171'
}

const configMapa = {
    zoomMin: 14,
    zoomMax: 17,
    zoomPadrao: 14,
    pontoCentral: [-15.871111, -47.919611],
    tileMapaUrlSatelite: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    tileMapaUrlOsm: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    tileMapaUrlOPNV: 'https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png',
};

const configSeta8 = {
    fill: true,
    size: "12px",
    yawn: 30,
    frequency: 8
}
const configSeta6 = {
    fill: true,
    size: "12px",
    yawn: 30,
    frequency: 6
}
const configSeta4 = {
    fill: true,
    size: "12px",
    yawn: 30,
    frequency: 4
}
const configSeta2 = {
    fill: true,
    size: "12px",
    yawn: 30,
    frequency: 2
}
const configSeta1 = {
    fill: true,
    size: "12px",
    yawn: 30,
    frequency: 1
}

const oesteHotelCoords = [
    [-15.865492, -47.927612],
    [-15.863532, -47.897419]
]

const oesteKiloCoords = [
    [-15.865189, -47.916296],
    [-15.876957, -47.915498]
]

const CharlieSaida11LCoords = [
    [-15.865054, -47.923476],
    [-15.863859, -47.921680]
]

const HotelSaida11LCoords = [
    [-15.864201, -47.907356],
    [-15.865492, -47.927612],
    [-15.864216, -47.927696]
]

const KiloSaida11LCoords = [
    [-15.876002, -47.915563],
    [-15.865189, -47.916296]
]

const Lima3Saida11LCoords = [
    [-15.866820, -47.917119],
    [-15.866774, -47.916277]
]

const Lima4Saida11LCoords = [
    [-15.869070, -47.917833],
    [-15.868957, -47.916112]
]

const Lima5Saida11LCoords = [
    [-15.869789, -47.916912],
    [-15.869733, -47.916091]
]

const Lima6Saida11LCoords = [
    [-15.870627, -47.917711],
    [-15.870522, -47.916133]
]

const Lima7Saida11LCoords = [
    [-15.872350, -47.916737],
    [-15.872286, -47.916024]
]

const Lima8Saida11LCoords = [
    [-15.873359, -47.920212],
    [-15.873083, -47.916008]
]

const NovemberSaida11LCoords = [
    [-15.865582, -47.910846],
    [-15.864508, -47.910920]
]

const OscarSaida11LCoords = [
    [-15.865633, -47.906973],
    [-15.864262, -47.907068]
]

const QuebecSaida11LCoords = [
    [-15.867942, -47.926849],
    [-15.867896, -47.925293],
    [-15.865452, -47.923938]
]

const QuebecQuebecSaida11LCoords = [
    [-15.867551, -47.926833],
    [-15.867438, -47.925157]
]

const TangoSaida11LCoords = [
    [-15.876592, -47.918864],
    [-15.876397, -47.915799]
]

var oesteHotel = L.polyline(oesteHotelCoords, {
    color: cores.ciano,
    weight: 3
}).arrowheads(configSeta8);

var oesteKilo = L.polyline(oesteKiloCoords, {
    color: cores.ciano,
    weight: 3
}).arrowheads(configSeta8);

var CharlieSaida11L = L.polyline(CharlieSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

var HotelSaida11L = L.polyline(HotelSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta8);

var KiloSaida11L = L.polyline(KiloSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta6);

var Lima3Saida11L = L.polyline(Lima3Saida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta1);

var Lima4Saida11L = L.polyline(Lima4Saida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

var Lima5Saida11L = L.polyline(Lima5Saida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta1);

var Lima6Saida11L = L.polyline(Lima6Saida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

var Lima7Saida11L = L.polyline(Lima7Saida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta1);

var Lima8Saida11L = L.polyline(Lima8Saida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

var NovemberSaida11L = L.polyline(NovemberSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

var OscarSaida11L = L.polyline(OscarSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

var QuebecSaida11L = L.polyline(QuebecSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta4);

var QuebecQuebecSaida11L = L.polyline(QuebecQuebecSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

var TangoSaida11L = L.polyline(TangoSaida11LCoords, {
    color: cores.amarelo,
    weight: 3
}).arrowheads(configSeta2);

/**
 *  Fluxos
 * 
 */ 
var fluxoPista11Ldep = L.layerGroup([CharlieSaida11L,HotelSaida11L,KiloSaida11L,Lima3Saida11L,Lima4Saida11L,Lima5Saida11L,Lima6Saida11L,Lima7Saida11L,Lima8Saida11L,NovemberSaida11L,OscarSaida11L,QuebecSaida11L,QuebecQuebecSaida11L,TangoSaida11L]);
var fluxoPista29Ldep = L.layerGroup([oesteKilo,oesteHotel]);

var tileMapaSatelite = L.tileLayer(configMapa.tileMapaUrlSatelite, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; Esri'
});

var tileMapaClaro = camadaMapbox('claro', {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax
});

var tileMapaEscuro = camadaMapbox('escuro', {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax
});

var tileMapaOsm = L.tileLayer(configMapa.tileMapaUrlOsm, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; OSM'
});

var tileMapaOPNV = L.tileLayer(configMapa.tileMapaUrlOPNV, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; memomaps'
});

var mapa1 = L.map('mapa1', {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    layers: [ tileMapaSatelite ]
}).setView(configMapa.pontoCentral, configMapa.zoomPadrao);

var opcoesDeMapa = {
    "Satellite": tileMapaSatelite,
    "Light": tileMapaClaro,
    "Dark": tileMapaEscuro,
    "OSM": tileMapaOsm,
    "OPNV": tileMapaOPNV,
};

var opcoesDeFluxo = {
    "Runway 11L - Departures": fluxoPista11Ldep,
    "Runway 29L - Departures": fluxoPista29Ldep,
};

var layerControl = L.control.layers(opcoesDeMapa, opcoesDeFluxo).addTo(mapa1);

</script>

-->