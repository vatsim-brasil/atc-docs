---
title: SBWL - Ilhéus
tags:
  - Terminal
  - SBRE
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Ilhéus TMA |
| **Position** | `SBWL_APP` |
| **Callsign** | Ilhéus Control |
| **Frequency** | **120.100** MHz[^pacote] |
| **Real-world frequencies** | 120.100 MHz |
| **Real-world hours** | DLY 0915–0100 |
| **ATS surveillance** | Procedural (not listed in AIP ENR 1.6) |
| **Aerodromes in the TMA** | [SBIL](../../aerodromos/sbre-recife/twr/SBIL.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Select one of the tools in the tabs above (Charts, Weather or Traffic) to access the information for the main aerodrome of the TMA (SBIL).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBIL?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Weather"
    <div id="metar-taf-container" data-airport="SBIL" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Loading METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Loading TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBIL){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Ilhéus TMA | FL035 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> |
| Ilhéus CTR | GND – FL035 | <span class="classe-badge classe-d">D</span> |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWL_APP** | `WL` | Controle Ilhéus | **120.100** |  |
| **SBIL_R_TWR** | `RIL` | Rádio Ilhéus | **120.100** |  |

## :material-arrow-down-bold-box-outline: Top-down coverage

**Ilhéus TMA:** `SBWL_APP` → `SBRE_S_CTR` → `SBRE_NS_CTR` → `SBRE_SW_CTR` → `SBRE_CTR`

**Ilhéus CTR:** `SBIL_R_TWR` → `SBWL_APP` → `SBRE_S_CTR` → `SBRE_NS_CTR` → `SBRE_SW_CTR` → `SBRE_CTR`

## :material-airplane: VFR circulation

- AFIL flight plans are not accepted.
- There is no REA chart published for this TMA.

## :material-note-text-outline: Remarks

- The TMA is class A between FL145 and FL195 and class D between FL035 and FL145.
- SBIL has no tower: Ilhéus APP provides AFIS in the circuit and on the movement area (in the package, `SBIL_R_TWR`, Rádio Ilhéus, on the same frequency).
- In the real world, the APP operates from 0915 to 0100 UTC. General aviation and air taxi require prior permission (PPR) 48 h in advance.

---

Sources: VATSIM Brasil SBRE sector package (lateral limits, positions, frequencies and top-down coverage) and AIP Brasil, AIRAC A 17/2026 (classes, vertical limits, ATS surveillance and VFR rules).

Back to the Recife FIR [terminals overview](index.en.md).

[^pacote]: Frequency in the VATSIM Brasil sector package.

<!--
Daqui pra baixo, é o mapa. Contornos extraídos do pacote SBRE (setores TMA_* e CTR_*), em [longitude, latitude].
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
    {"tipo": "tma", "id": "SBWL", "nome": "Ilhéus TMA", "posicao": "SBWL_APP", "freq": "120.100", "lim": "FL035 – FL195", "classe": "A/D", "link": "", "contorno": [[-38.416389, -13.941389], [-38.556389, -14.320833], [-38.477222, -14.406111], [-38.41, -14.51], [-38.369167, -14.61], [-38.333611, -14.734167], [-38.330833, -14.869722], [-38.351944, -14.995], [-38.355215, -15.003454], [-38.396667, -15.110556], [-38.467222, -15.2225], [-38.546667, -15.308889], [-38.632222, -15.381667], [-38.709167, -15.421667], [-38.799722, -15.463333], [-38.823611, -15.649444], [-39.374722, -15.609722], [-39.350278, -15.422222], [-39.472778, -15.346389], [-39.565, -15.255278], [-39.580833, -15.234611], [-39.627778, -15.172778], [-39.675, -15.075], [-39.714722, -14.955556], [-39.728611, -14.822778], [-39.715278, -14.683889], [-39.691389, -14.579167], [-39.663583, -14.52576], [-39.642222, -14.484722], [-39.568611, -14.380556], [-39.448333, -14.271667], [-39.344722, -14.21], [-39.203056, -14.163333], [-39.07, -14.141111], [-38.931389, -13.757778], [-38.416389, -13.941389]]},
    {"tipo": "ctr", "id": "SBWL", "nome": "Ilhéus CTR", "posicao": "SBIL_R_TWR", "freq": "120.100", "lim": "GND – FL035", "classe": "D", "link": "", "contorno": [[-39.033889, -14.555833], [-39.104722, -14.567778], [-39.166389, -14.591667], [-39.224167, -14.635556], [-39.270833, -14.704444], [-39.285833, -14.793611], [-39.266667, -14.893056], [-39.208889, -14.981944], [-39.121111, -15.036389], [-39.038889, -15.0525], [-38.952222, -15.041667], [-38.882222, -15.011111], [-38.820278, -14.956667], [-38.775278, -14.865556], [-38.768611, -14.771111], [-38.790556, -14.695556], [-38.845278, -14.631667], [-38.914167, -14.583889], [-38.977778, -14.561111], [-39.033889, -14.555833]]}
];

const limiteFir = [[-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-42.086944, -2.855278], [-42.1475, -3.03], [-42.368056, -3.686111], [-42.523889, -4.176944], [-42.979444, -4.398611], [-43.157778, -4.485278], [-43.182573, -4.510323], [-43.386389, -4.703611], [-44.201389, -6.094444], [-44.796667, -6.304444], [-45.780278, -8.143611], [-46.672222, -8.86], [-47.150833, -9.530556], [-47.315278, -10.328611], [-46.934722, -11.848889], [-46.891111, -12.021944], [-45.62204, -13.306131], [-45.278124, -13.796406], [-45.010227, -14.217837], [-44.580004, -14.779477], [-44.251448, -15.354465], [-44.095833, -15.626499], [-42.819853, -16.378574], [-42.337778, -16.624722], [-41.820556, -16.948333], [-42.448056, -18.758056], [-42.440556, -19.105], [-42.479444, -19.463056], [-42.526944, -20.003333], [-42.752222, -20.411667], [-42.594444, -20.460833], [-42.316668, -20.533343], [-42.000004, -20.61667], [-41.400004, -20.48334], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.674833, -20.807667], [-40.5675, -20.901667], [-40.409614, -20.924606], [-40.348833, -20.933333], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189]];

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
