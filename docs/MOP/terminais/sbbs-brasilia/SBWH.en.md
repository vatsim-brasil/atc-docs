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
| **Real-world frequencies** | 119.100 / 119.300 / 119.650 / 120.200 / 128.550 / 129.100 / 129.400 MHz |
| **Real-world hours** | H24 |
| **ATS surveillance** | Radar (listed in AIP ENR 1.6) |
| **Aerodromes in the TMA** | [SBCF](../../aerodromos/sbbs-brasilia/twr/SBCF.en.md), [SBBH](../../aerodromos/sbbs-brasilia/twr/SBBH.en.md), [SBLS](../../aerodromos/sbbs-brasilia/afis/SBLS.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Select one of the tools in the tabs above (Charts, Weather or Traffic) to access the information for the main aerodrome of the TMA (SBCF).

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
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBCF){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

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

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWH_APP** | `WH` | Controle Belo Horizonte | **129.100** |  |
| **SBBH_TWR** | `TBH` | Torre Belo Horizonte | **118.000** |  |
| **SBCF_TWR** | `TCF` | Torre Confins | **118.200** |  |
| **SBLS_R_TWR** | `RLS` | Rádio Lagoa Santa | **122.850** |  |

## :material-arrow-down-bold-box-outline: Top-down coverage

**Belo Horizonte TMA:** `SBWH_APP` → `SBBS_E_CTR` → `SBBS_NE_CTR` → `SBBS_SE_CTR` → `SBBS_CTR`

**Belo Horizonte CTR:** `SBBH_TWR` → `SBWH_APP` → `SBBS_E_CTR` → `SBBS_SE_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

**Confins CTR:** `SBCF_TWR` → `SBWH_APP` → `SBBS_E_CTR` → `SBBS_SE_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

**Belo Horizonte ATZ (Pampulha):** `SBBH_TWR` → `SBWH_APP` → `SBBS_E_CTR` → `SBBS_SE_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

**Confins ATZ:** `SBCF_TWR` → `SBWH_APP` → `SBBS_E_CTR` → `SBBS_SE_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

**Lagoa Santa ATZ:** `SBLS_R_TWR` → `SBWH_APP` → `SBBS_E_CTR` → `SBBS_SE_CTR` → `SBBS_NE_CTR` → `SBBS_CTR`

## :material-airplane: VFR circulation

- AFIL flight plans from aerodromes without an ATS unit inside the Belo Horizonte and Confins CTRs, the TMA or their projections are not accepted: aircraft entering must file a flight plan beforehand.
- In VMC, a composite separation of 2.5 NM or 500 FT is applied between IFR on RNP procedures to SBBH RWY 13/31 and VFR aeroplanes or helicopters on the REA and REH.
- Operations by aircraft without radio are prohibited at SBCF. Observe the simultaneous aeroplane and helicopter operating area in sector ECHO.
- SBLS: mandatory contact with Belo Horizonte Control when entering the TMA; remain within the ATZ and do not extend the base leg (RWY 13) or delay the turn (RWY 31) beyond position BOSQUE, due to SBCF.
- Helicopter routes chart: [CCV REH WH-Belo Horizonte](https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wh-belo-horizonte_reh_20240905.pdf){ target="_blank" }
- VFR routes chart: [CCV REA WH-Belo Horizonte](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wh-belo-horizonte_rea_20240905.pdf){ target="_blank" }

## :material-note-text-outline: Remarks

- Belo Horizonte 1 is class A between FL145 and FL195 and class C between 5500 FT and FL145. APP sectors 05 and 06 are the SBBH and SBCF finals.
- The Belo Horizonte CTR excludes the Confins CTR.
- SBLS is a military aerodrome (PAMALS); civil aviation requires authorization from the PAMALS director.
- ATZs have no class published in the AIP (ENR 2.2).

---

Sources: VATSIM Brasil SBBS sector package (lateral limits, positions, frequencies and top-down coverage) and AIP Brasil, emendas AIRAC A 13, A 15 e A 17/2026 (classes, vertical limits, ATS surveillance and VFR rules).

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
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 1", "posicao": "SBWH_APP", "freq": "129.100", "lim": "5500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-43.266908, -20.206404], [-43.4576, -20.4966], [-43.9047, -20.5654], [-43.969076, -20.54265], [-44.4974, -20.3533], [-44.6949, -19.8], [-44.7775, -19.569], [-44.6146, -19.1277], [-44.353616, -18.988162], [-44.3214, -18.9709], [-43.951268, -18.949964], [-43.692, -18.9348], [-43.1142, -19.6081], [-43.1373, -20.0084], [-43.266908, -20.206404]]},
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 2", "posicao": "SBWH_APP", "freq": "129.100", "lim": "4100 FT – 5500 FT", "classe": "C", "link": "", "contorno": [[-44.3793, -19.2945], [-44.2396, -19.225], [-43.9432, -19.166], [-43.4868, -19.5018], [-43.5229, -19.9021], [-43.7936, -20.1036], [-43.9467, -20.0488], [-43.9806, -19.9293], [-44.3038, -19.9772], [-44.4276, -19.5236], [-44.3793, -19.2945]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Confins CTR", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 5500 FT", "classe": "D", "link": "", "contorno": [[-43.7636, -19.6104], [-43.8163, -19.7746], [-43.9881, -19.8107], [-44.1995, -19.5813], [-43.9659, -19.39], [-43.7636, -19.6104]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Belo Horizonte CTR", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 5500 FT", "classe": "C", "link": "", "contorno": [[-43.7636, -19.6104], [-43.6578, -19.7253], [-43.7524, -19.9447], [-43.8544, -19.9932], [-43.9475, -19.9796], [-43.9592, -19.9384], [-44.1801, -19.8593], [-44.1995, -19.5813], [-43.9881, -19.8107], [-43.8163, -19.7746], [-43.7636, -19.6104]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Confins ATZ", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.912222, -19.620833], [-43.935278, -19.64], [-43.939722, -19.652222], [-43.93, -19.662778], [-43.899167, -19.696389], [-43.951667, -19.738333], [-44.083056, -19.596389], [-43.973889, -19.509722], [-43.888889, -19.601667], [-43.912222, -19.620833]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Belo Horizonte ATZ (Pampulha)", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.891667, -19.813056], [-43.856944, -19.840833], [-43.881667, -19.911111], [-43.928056, -19.917778], [-44.009444, -19.892222], [-44.0425, -19.859722], [-44.017778, -19.789444], [-43.974722, -19.786944], [-43.891667, -19.813056]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Lagoa Santa ATZ", "posicao": "SBLS_R_TWR", "freq": "122.850", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.912222, -19.620833], [-43.863611, -19.632778], [-43.8575, -19.6625], [-43.863611, -19.679444], [-43.93, -19.662778], [-43.939722, -19.652222], [-43.935278, -19.64], [-43.912222, -19.620833]]}
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
