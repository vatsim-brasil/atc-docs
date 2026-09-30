---
title: SBWU - Bauru
tags:
  - Terminal
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: General data

| | |
| --- | --- |
| **TMA** | Bauru TMA |
| **Position** | `SBWU_APP` |
| **Callsign** | Bauru Control |
| **Frequency** | **121.300** MHz[^pacote] |
| **Real-world frequencies** | 121.300 MHz |
| **Real-world hours** | DLY 0900–0200 |
| **ATS surveillance** | Procedural (not listed in AIP ENR 1.6) |
| **Aerodromes in the TMA** | `SBBU`, [SBAE](../../aerodromos/sbbs-brasilia/afis/SBAE.en.md), [SBML](../../aerodromos/sbbs-brasilia/afis/SBML.en.md) |

## :material-monitor-dashboard: Useful Information

=== ":material-monitor-dashboard: Dashboard"
    Use the tabs above: **Aeronautical Charts** shows the charts for the main aerodrome (SBBU), **Weather** shows a weather map of the area and **VATSIM Traffic** opens the traffic at the main aerodrome (SBBU).

=== ":material-file-document: Aeronautical Charts"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBBU?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Weather"
    <div class="tma-meteo" data-lat="-22.313" data-lon="-49.399" data-zoom="8" data-lang="en"></div>

=== ":material-radar: VATSIM Traffic"
    [:material-radar: Traffic](https://vatsim-radar.com/?airport=SBBU){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Map

Click a volume to see its limits and class. Use the layer control to change the base map and toggle the volumes.

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limits | Class |
| --- | --- | :---: |
| Bauru TMA | FL045 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> |
| Bauru CTR | GND – FL045 | <span class="classe-badge classe-d">D</span> |
| Arealva ATZ | GND – 1500 FT AGL | — |

## :material-headset: ATC Units

| Code | Abbr. | Callsign | Frequency | Remarks |
| --- | --- | --- | --- | --- |
| **SBWU_APP** | `WU` | Controle Bauru | **121.300** |  |
| **SBBU_R_TWR** | `RBU` | Rádio Bauru | **121.300** |  |
| **SBAE_R_TWR** | `RAE` | Rádio Arealva | **126.600** |  |

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
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBBS_NS_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color)'>SBBS_SE_CTR</span>"]:::grpctr
        p1["SBBS_S_CTR"]:::ctr
        p2["SBWU_APP"]:::app
        p3["SBBU_R_TWR"]:::twr
        p4["SBAE_R_TWR"]:::twr
        a0(["Bauru TMA"]):::esp --> p2
        a1(["Bauru CTR"]):::esp --> p3
        a2(["Arealva ATZ"]):::esp --> p4
        g0 --> p0
        p1 --> g0
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

- AFIL flight plans are not accepted. A flight plan is mandatory before take-off, except for VFR flights from aerodromes without an ATS unit that do not enter controlled airspace.
- SBAE: two-way contact with Rádio Arealva and Bauru APP.
- There is no REA chart published for this TMA.

## :material-note-text-outline: Remarks

- The TMA is class A between FL145 and FL195 and class D between FL045 and FL145.
- At SBBU, AFIS (121.300) is provided by Bauru APP itself, operated by NAV Brasil.
- In the real world, the APP and CTR operate from 0900 to 0200 UTC.
- ATZs have no class published in the AIP (ENR 2.2).

---

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
    {"tipo": "tma", "id": "SBWU", "nome": "Bauru TMA", "posicao": "SBWU_APP", "freq": "121.300", "lim": "FL045 – FL195", "classe": "A/D", "link": "", "contorno": [[-48.832226, -22.69952], [-48.7105, -22.5875], [-48.6833, -22.5508], [-48.642, -22.48], [-48.5486, -22.2114], [-48.6587, -22.083], [-49.7337, -21.6635], [-50.006, -21.7598], [-50.0593, -21.9363], [-50.105463, -22.08634], [-50.171111, -22.299444], [-50.224367, -22.498381], [-50.2487, -22.5827], [-49.1192, -22.9628], [-48.861, -22.726], [-48.832226, -22.69952]]},
    {"tipo": "ctr", "id": "SBWU", "nome": "Bauru CTR", "posicao": "SBBU_R_TWR", "freq": "121.300", "lim": "GND – FL045", "classe": "D", "link": "", "contorno": [[-49.05, -21.9821], [-48.968, -21.9901], [-48.8971, -22.0107], [-48.8247, -22.0477], [-48.7679, -22.0923], [-48.721, -22.146], [-48.6826, -22.2141], [-48.6602, -22.2882], [-48.6545, -22.3572], [-48.6647, -22.4336], [-48.6883, -22.4993], [-48.7247, -22.5597], [-48.7787, -22.618], [-48.8446, -22.6646], [-48.9118, -22.6948], [-48.9839, -22.7128], [-49.0583, -22.7179], [-49.1325, -22.7099], [-49.2037, -22.6891], [-49.2762, -22.652], [-49.3331, -22.6072], [-49.3799, -22.5533], [-49.415, -22.4922], [-49.4371, -22.426], [-49.4455, -22.3495], [-49.4367, -22.273], [-49.4143, -22.207], [-49.379, -22.146], [-49.3321, -22.0923], [-49.2753, -22.0477], [-49.2029, -22.0107], [-49.132, -21.9901], [-49.05, -21.9821]]},
    {"tipo": "ctr", "id": "SBWU", "nome": "Arealva ATZ", "posicao": "SBAE_R_TWR", "freq": "126.600", "lim": "GND – 1500 FT AGL", "classe": "—", "link": "", "contorno": [[-49.068333, -22.074501], [-49.040563, -22.078574], [-49.015506, -22.090397], [-48.995614, -22.108813], [-48.982832, -22.132021], [-48.978416, -22.157753], [-48.982801, -22.183489], [-48.995563, -22.206711], [-49.015456, -22.225142], [-49.040532, -22.236977], [-49.068333, -22.241055], [-49.096135, -22.236977], [-49.121211, -22.225142], [-49.141104, -22.206711], [-49.153866, -22.183489], [-49.158251, -22.157753], [-49.153834, -22.132021], [-49.141053, -22.108813], [-49.12116, -22.090397], [-49.096104, -22.078574], [-49.068333, -22.074501]]}
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
