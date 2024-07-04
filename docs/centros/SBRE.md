---
  title: SBRE - Recife
---

--8<-- "includes/abreviacoes.md"

## Setorização

### Combinados
- **SBRE_N_CTR**
    - Composto pela combinação (união) dos setores 1, 2, 3 e 6 da FIR Recife.
    - Frequência: 134.800 MHz
- **SBRE_W_CTR**
    - Composto pela combinação (união) dos setores 4, 5, 8 e 9 da FIR Recife.
    - Frequência: 124.550 MHz
- **SBRE_S_CTR**
    - Composto pela combinação (união) dos setores 7, 10, 11, 12, 13, 14 e 15 da FIR Recife.
    - Frequência: 125.100 MHz
### Supercombinados
- **SBRE_NS_CTR**
    - Composto pela combinação (união) dos combinados N e S da FIR Recife.
    - Frequência: 125.150 MHz
- **SBRE_NW_CTR**
    - Composto pela combinação (união) dos combinados N e W da FIR Recife.
    - Frequência: 126.100 MHz
- **SBRE_SW_CTR**
    - Composto pela combinação (união) dos combinados S e W da FIR Recife.
    - Frequência: 124.250 MHz
### Posição Geral
- **SBRE_CTR**
    - Composto pela combinação (união) de todos os combinados da FIR Recife.
    - Frequência: 125.400 MHz

 <!-- ![](sbre.png){ : style="height:800px" } -->


!!! info "Uma informação"

    Selecione o combinado no canto superior direito do mapa para visualizar o limite lateral no mapa.


<div id="mapa1" class="mapa"></div>

<!--
Daqui pra baixo, são os mapas.
-->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>
<script src="https://cdn.jsdelivr.net/npm/leaflet-geometryutil@0.10.2/src/leaflet.geometryutil.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/leaflet-arrowheads@1.4.0/src/leaflet-arrowheads.min.js"></script>

<style>
    .mapa { height: 680px }
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
    zoomMin: 3,
    zoomMax: 14,
    zoomPadrao: 5,
    pontoCentral: [-9.382442, -38.714408],
    tileMapaUrlSatelite: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    tileMapaUrlStadia: 'https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png',
    tileMapaUrlStadiaDark: 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png',
    tileMapaUrlEscuro: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
    tileMapaUrlClaro: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    tileMapaUrlOsm: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
    tileMapaUrlOPNV: 'https://tileserver.memomaps.de/tilegen/{z}/{x}/{y}.png',
};

function reverteCoord(arrayOrig) {
    arrayOrig.forEach(function(part, index, array) {
        array[index][2] = array[index][0]
        array[index][0] = array[index][1]
        array[index][1] = array[index][2]
        array[index][2] = ""
    });
    return arrayOrig
}

const sbre = [ [-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-42.086944, -2.855278], [-42.1475, -3.03], [-42.368056, -3.686111], [-42.523889, -4.176944], [-42.979444, -4.398611], [-43.157778, -4.485278], [-43.182573, -4.510323], [-43.386389, -4.703611], [-44.201389, -6.094444], [-44.796667, -6.304444], [-45.780278, -8.143611], [-46.672222, -8.86], [-47.150833, -9.530556], [-47.315278, -10.328611], [-46.934722, -11.848889], [-46.891111, -12.021944], [-45.62204, -13.306131], [-45.278124, -13.796406], [-45.010227, -14.217837], [-44.580004, -14.779477], [-44.251448, -15.354465], [-44.095833, -15.626499], [-42.819853, -16.378574], [-42.337778, -16.624722], [-41.820556, -16.948333], [-42.448056, -18.758056], [-42.440556, -19.105], [-42.479444, -19.463056], [-42.526944, -20.003333], [-42.752222, -20.411667], [-42.594444, -20.460833], [-42.316668, -20.533343], [-42.000004, -20.61667], [-41.400004, -20.48334], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.674833, -20.807667], [-40.5675, -20.901667], [-40.409614, -20.924606], [-40.348833, -20.933333], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189] ]
const sbre_n = [ [-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-42.086944, -2.855278], [-42.1475, -3.03], [-42.368056, -3.686111], [-42.523889, -4.176944], [-42.979444, -4.398611], [-42.983739, -4.4197], [-42.825, -5.0625], [-42.263344, -5.404994], [-40.364167, -6.548333], [-39.274722, -7.213611], [-38.255, -7.453611], [-38.200556, -7.771944], [-38.250833, -9.406389], [-38.700278, -10.100278], [-37.67785, -10.67154], [-37.389167, -10.832], [-37.077353, -10.981925], [-36.411614, -11.097711], [-36.2365, -11.128056], [-34.363889, -11.595278], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189] ]
const sbre_w = [ [-40.364167, -6.548333], [-42.263344, -5.404994], [-42.825, -5.0625], [-42.983739, -4.4197], [-42.979444, -4.398611], [-43.157778, -4.485278], [-43.182573, -4.510323], [-43.386389, -4.703611], [-44.201389, -6.094444], [-44.796667, -6.304444], [-45.780278, -8.143611], [-46.672222, -8.86], [-47.150833, -9.530556], [-47.315278, -10.328611], [-46.934722, -11.848889], [-46.891111, -12.021944], [-45.62204, -13.306131], [-45.278124, -13.796406], [-45.010227, -14.217837], [-44.580004, -14.779477], [-44.251448, -15.354465], [-44.095833, -15.626499], [-42.819853, -16.378574], [-41.18, -14.316944], [-40.2725, -12.638333], [-40.1, -12.24], [-38.700278, -10.100278], [-38.250833, -9.406389], [-38.200556, -7.771944], [-38.255, -7.453611], [-39.274722, -7.213611] ]
const sbre_s = [ [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-34.363889, -11.595278], [-36.2365, -11.128056], [-36.411614, -11.097711], [-37.077353, -10.981925], [-37.389167, -10.832], [-37.67785, -10.67154], [-38.700278, -10.100278], [-40.1, -12.24], [-40.2725, -12.638333], [-41.18, -14.316944], [-42.819853, -16.378574], [-42.337778, -16.624722], [-41.820556, -16.948333], [-42.448056, -18.758056], [-42.440556, -19.105], [-42.479444, -19.463056], [-42.526944, -20.003333], [-42.752222, -20.411667], [-42.594444, -20.460833], [-42.316668, -20.533343], [-42.000004, -20.61667], [-41.400004, -20.48334], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.674833, -20.807667], [-40.5675, -20.901667], [-40.409614, -20.924606], [-40.348833, -20.933333], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957] ]
const sbre_ns = [ [-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-42.086944, -2.855278], [-42.1475, -3.03], [-42.368056, -3.686111], [-42.523889, -4.176944], [-42.979444, -4.398611], [-42.983739, -4.4197], [-42.825, -5.0625], [-42.263344, -5.404994], [-40.364167, -6.548333], [-39.274722, -7.213611], [-38.255, -7.453611], [-38.200556, -7.771944], [-38.250833, -9.406389], [-38.700278, -10.100278], [-40.1, -12.24], [-40.2725, -12.638333], [-41.18, -14.316944], [-42.819853, -16.378574], [-42.337778, -16.624722], [-41.820556, -16.948333], [-42.448056, -18.758056], [-42.440556, -19.105], [-42.479444, -19.463056], [-42.526944, -20.003333], [-42.752222, -20.411667], [-42.594444, -20.460833], [-42.316668, -20.533343], [-42.000004, -20.61667], [-41.400004, -20.48334], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.674833, -20.807667], [-40.5675, -20.901667], [-40.409614, -20.924606], [-40.348833, -20.933333], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189] ]
const sbre_nw = [ [-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-42.086944, -2.855278], [-42.1475, -3.03], [-42.368056, -3.686111], [-42.523889, -4.176944], [-42.979444, -4.398611], [-43.157778, -4.485278], [-43.182573, -4.510323], [-43.386389, -4.703611], [-44.201389, -6.094444], [-44.796667, -6.304444], [-45.780278, -8.143611], [-46.672222, -8.86], [-47.150833, -9.530556], [-47.315278, -10.328611], [-46.934722, -11.848889], [-46.891111, -12.021944], [-45.62204, -13.306131], [-45.278124, -13.796406], [-45.010227, -14.217837], [-44.580004, -14.779477], [-44.251448, -15.354465], [-44.095833, -15.626499], [-42.819853, -16.378574], [-41.18, -14.316944], [-40.2725, -12.638333], [-40.1, -12.24], [-38.700278, -10.100278], [-37.67785, -10.67154], [-37.389167, -10.832], [-37.077353, -10.981925], [-36.411614, -11.097711], [-36.2365, -11.128056], [-34.363889, -11.595278], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189] ]
const sbre_sw = [ [-42.979444, -4.398611], [-43.157778, -4.485278], [-43.182573, -4.510323], [-43.386389, -4.703611], [-44.201389, -6.094444], [-44.796667, -6.304444], [-45.780278, -8.143611], [-46.672222, -8.86], [-47.150833, -9.530556], [-47.315278, -10.328611], [-46.934722, -11.848889], [-46.891111, -12.021944], [-45.62204, -13.306131], [-45.278124, -13.796406], [-45.010227, -14.217837], [-44.580004, -14.779477], [-44.251448, -15.354465], [-44.095833, -15.626499], [-42.819853, -16.378574], [-42.337778, -16.624722], [-41.820556, -16.948333], [-42.448056, -18.758056], [-42.440556, -19.105], [-42.479444, -19.463056], [-42.526944, -20.003333], [-42.752222, -20.411667], [-42.594444, -20.460833], [-42.316668, -20.533343], [-42.000004, -20.61667], [-41.400004, -20.48334], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.674833, -20.807667], [-40.5675, -20.901667], [-40.409614, -20.924606], [-40.348833, -20.933333], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-34.363889, -11.595278], [-36.2365, -11.128056], [-36.411614, -11.097711], [-37.077353, -10.981925], [-37.389167, -10.832], [-37.67785, -10.67154], [-38.700278, -10.100278], [-38.250833, -9.406389], [-38.200556, -7.771944], [-38.255, -7.453611], [-39.274722, -7.213611] ]

var sbrePolygon = L.polygon(reverteCoord(sbre), {
    color: cores.vermelho,
    weight: 3
});
sbrePolygon.bindPopup("<b>SBRE_CTR</b><br><i>125.400 MHz</i>");

var sbrenPolygon = L.polygon(reverteCoord(sbre_n), {
    color: cores.ciano,
    weight: 3
});
sbrenPolygon.bindPopup("<b>SBRE_N_CTR</b><br><i>134.800 MHz</i>");

var sbrewPolygon = L.polygon(reverteCoord(sbre_w), {
    color: cores.amarelo,
    weight: 3
});
sbrewPolygon.bindPopup("<b>SBRE_W_CTR</b><br><i>124.550 MHz</i>");

var sbresPolygon = L.polygon(reverteCoord(sbre_s), {
    color: cores.verde,
    weight: 3
});
sbresPolygon.bindPopup("<b>SBRE_S_CTR</b><br><i>125.100 MHz</i>");

var sbrensPolygon = L.polygon(reverteCoord(sbre_ns), {
    color: cores.rosa,
    weight: 3
});
sbrensPolygon.bindPopup("<b>SBRE_NS_CTR</b><br><i>125.150 MHz</i>");

var sbrenwPolygon = L.polygon(reverteCoord(sbre_nw), {
    color: cores.verde,
    weight: 3
});
sbrenwPolygon.bindPopup("<b>SBRE_NW_CTR</b><br><i>126.100 MHz</i>");

var sbreswPolygon = L.polygon(reverteCoord(sbre_sw), {
    color: cores.amarelo,
    weight: 3
});
sbreswPolygon.bindPopup("<b>SBRE_SW_CTR</b><br><i>124.250 MHz</i>");

/**
 *  Fluxos
 * 
 */ 
var firInteiraGrupo = L.layerGroup([sbrePolygon]);
var combinadosGrupo = L.layerGroup([sbrenPolygon,sbrewPolygon,sbresPolygon]);
var superCombinadoNS = L.layerGroup([sbrensPolygon]);
var superCombinadoNW = L.layerGroup([sbrenwPolygon]);
var superCombinadoSW = L.layerGroup([sbreswPolygon]);


var tileMapaStadia = L.tileLayer(configMapa.tileMapaUrlStadia, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>'
});

var tileMapaStadiaDark = L.tileLayer(configMapa.tileMapaUrlStadiaDark, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>'
});

var tileMapaSatelite = L.tileLayer(configMapa.tileMapaUrlSatelite, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; Esri'
});

var tileMapaOsm = L.tileLayer(configMapa.tileMapaUrlOsm, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; OSM'
});


var mapa1 = L.map('mapa1', {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    layers: [ tileMapaStadia ]
}).setView(configMapa.pontoCentral, configMapa.zoomPadrao);


var opcoesDeMapa = {
    "Stadia": tileMapaStadia,
    "Stadia Dark": tileMapaStadiaDark,
    "Arcgis Satélite": tileMapaSatelite,
    "Open Street Map": tileMapaOsm,
};

var opcoesDeFluxo = {
    "SBRE_CTR": firInteiraGrupo,
    "SBRE_NS_CTR": superCombinadoNS,
    "SBRE_NW_CTR": superCombinadoNW,
    "SBRE_SW_CTR": superCombinadoSW,
    "Combinados": combinadosGrupo
};

var layerControl = L.control.layers(opcoesDeMapa, opcoesDeFluxo).addTo(mapa1);

</script>