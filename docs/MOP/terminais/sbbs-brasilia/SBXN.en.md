---
title: SBXN - Anápolis
tags:
  - Terminal
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Anápolis TMA |
| **Position** | `SBXN_APP` |
| **Callsign** | Anápolis Control |
| **Frequency** | **129.450** MHz[^pacote] |
| **Real-world frequencies** | 119.150 / 120.550 / 129.450 / 133.000 MHz |
| **Real-world hours** | H24 |
| **ATS surveillance** | Radar (listed in AIP ENR 1.6) |
| **Aerodromes in the TMA** | `SBAN`, [SBGO](../../aerodromos/sbbs-brasilia/twr/SBGO.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Select one of the tools in the tabs above (Charts, Weather or Traffic) to access the information for the main aerodrome of the TMA (SBGO).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBGO?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Weather"
    <div id="metar-taf-container" data-airport="SBGO" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Loading METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Loading TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBGO){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Anápolis TMA | FL065 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| Anápolis 1 CTR (SBAN) | GND – FL065 | <span class="classe-badge classe-c">C</span> |
| Anápolis 2 CTR (SBGO) | GND – FL065 | <span class="classe-badge classe-c">C</span> |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBXN_APP** | `XN` | Controle Anápolis | **129.450** | TMA approach control |
| **SBAN_TWR** | `TAN` | Torre Anápolis | **118.300** | Anápolis 1 CTR (SBAN) |
| **SBGO_TWR** | `TGO` | Torre Goiânia | **118.700** | Anápolis 2 CTR (SBGO) |

## :material-arrow-down-bold-box-outline: Top-down coverage

**Anápolis TMA:** `SBXN_APP` → `SBBS_N_CTR` → `SBBS_NS_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

**Anápolis 1 CTR (SBAN):** `SBAN_TWR` → `SBXN_APP` → `SBBS_N_CTR` → `SBBS_NS_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

**Anápolis 2 CTR (SBGO):** `SBGO_TWR` → `SBXN_APP` → `SBBS_N_CTR` → `SBBS_NS_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

## :material-airplane: VFR circulation

- AFIL flight plans are not accepted.
- SBGO: training is restricted to certain hours.
- VFR routes chart: [CCV REA XN-Anápolis](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xn-anapolis_rea_20240711.pdf){ target="_blank" }

## :material-alert-octagon-outline: Nearby special use airspace

| Area | Limits | Remark |
| --- | --- | --- |
| SBR605 e SBR606 Anápolis 1 e 2 | GND – 5500 FT | training, HJ; SBR606 activated in coordination with Anápolis APP |
| SBR607 Goiânia | GND – 5500 FT AGL | HJ |
| SBR601 e SBR613 Dourada | FL100 – UNL | military operations |
| SBR728 PQD AN e SBR877 Skydive Cerrado | até FL160 / FL210 | parachuting, with Anápolis APP authorization |
| SBD638 Fazenda Jussara | até FL090 |  |

## :material-note-text-outline: Remarks

- The TMA is class A between FL145 and FL195 and class C between FL065 and FL145.
- SBAN is Anápolis Air Base. Civil aircraft may only operate with authorization from the COMAR VI commander, requested 72 h in advance. Foreign aircraft are prohibited in TMA sector 1 and in the Anápolis 1 CTR.
- SBGO (Goiânia) lies in the Anápolis 2 CTR.

---

Sources: VATSIM Brasil SBBS sector package (lateral limits, positions, frequencies and top-down coverage) and AIP Brasil, emendas AIRAC A 13, A 15 e A 17/2026 (classes, vertical limits, ATS surveillance, VFR rules and special use airspace).

Back to the Brasília FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.

<!--
Daqui pra baixo, é o mapa. Contornos extraídos do pacote SBBS (setores TMA_* e CTR_*), em [longitude, latitude].
-->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>

<style>
    .mapa { height: 550px }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBXN", "nome": "Anápolis TMA", "posicao": "SBXN_APP", "freq": "129.450", "lim": "FL065 – FL195", "classe": "A/C", "link": "", "contorno": [[-48.936167, -15.723167], [-48.775105, -15.785841], [-48.602333, -15.852833], [-48.541667, -16.099333], [-48.5995, -16.235667], [-48.644833, -16.548667], [-48.477, -16.664667], [-48.542662, -17.280069], [-48.559833, -17.440167], [-49.036514, -17.542154], [-49.318, -17.601833], [-49.737219, -17.352773], [-49.884167, -17.265167], [-49.972133, -16.953389], [-50.039162, -16.715102], [-50.054333, -16.661], [-49.748989, -16.294681], [-49.2915, -15.745833], [-49.00315, -15.727439], [-48.936167, -15.723167]]},
    {"tipo": "ctr", "id": "SBXN", "nome": "Anápolis 2 CTR (SBGO)", "posicao": "SBGO_TWR", "freq": "118.700", "lim": "GND – FL065", "classe": "C", "link": "", "contorno": [[-49.098889, -16.4875], [-49.313056, -16.367222], [-49.411667, -16.3125], [-49.500278, -16.308056], [-49.709167, -16.65], [-48.998056, -17.046944], [-48.770833, -16.670278], [-49.098889, -16.4875]]},
    {"tipo": "ctr", "id": "SBXN", "nome": "Anápolis 1 CTR (SBAN)", "posicao": "SBAN_TWR", "freq": "118.300", "lim": "GND – FL065", "classe": "C", "link": "", "contorno": [[-49.098889, -16.4875], [-49.313056, -16.367222], [-48.896111, -15.872222], [-48.643056, -16.071111], [-48.854722, -16.323056], [-48.916389, -16.275], [-49.015556, -16.378611], [-49.098889, -16.4875]]}
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

var mapa = L.map('mapa-tma', {
    minZoom: 3,
    maxZoom: 13,
    layers: [tileMapaClaro, grupoFir, grupoTma, grupoCtr]
});

mapa.fitBounds(grupoTma.getBounds().extend(grupoCtr.getBounds()), { padding: [20, 20] });

L.control.layers({
    "Light": tileMapaClaro,
    "Dark": tileMapaEscuro,
    "Arcgis Satellite": tileMapaSatelite
}, {
    "TMAs": grupoTma,
    "CTRs": grupoCtr,
    "FIR boundary": grupoFir
}).addTo(mapa);

// Legenda das classes
var legenda = L.control({ position: 'bottomleft' });
legenda.onAdd = function () {
    var div = L.DomUtil.create('div', 'mapa-legenda');
    div.innerHTML = '<b>Class</b>' + ['A', 'C', 'D'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('');
    return div;
};
legenda.addTo(mapa);

})();
</script>
