---
title: Estrutura da FIR Atlântico
tags:
  - Centro
  - SBAO
---

## Classificação

| Espaço Aéreo  | Classificação | Limites Verticais | Serviço Prestado      |
|:-------------:|:-------------:|:-----------------:|:---------------------:|
| UTA Atlântico | `A`           | FL245 - UNL       | ATCS sem radar        |
| FIR Atlântico | `G`           | GND - FL245       | FIS/ALRS Limitado O/R |

## Setorização

A FIR Atlântico está atualmente dividida da seguinte forma:

### Posição Geral

| Identificação | Código CPDLC                                       | Frequência (kHz) | Frequência (*alias*) |
|:-------------:|:--------------------------------------------------:|:----------------:|:--------------------:|
| **SBAO_FSS**  | :material-checkbox-marked-circle:{ .corok } `SBAO` | 4669             | 133.500              |


### Supercombinados

| Identificação  | Código CPDLC                                       | Setores             | Frequência (kHz) | Frequência (*alias*) |
|:--------------:|:--------------------------------------------------:|:-------------------:|:----------------:|:--------------------:|
| **SBAO_N_FSS** | :material-checkbox-marked-circle:{ .corok } `SJAN` | 1, 2, 3, 4, 5, 6, 7 | 13315            | 133.025              |
| **SBAO_S_FSS** | :material-checkbox-marked-circle:{ .corok } `SJAS` | 8                   | 10096            | 133.125              |


### Combinados

| Identificação   | Código CPDLC                                       | Setores          | Frequência (kHz) | Frequência (*alias*) |
|:---------------:|:--------------------------------------------------:|:----------------:|:----------------:|:------------------:|
| **SBAO_NW_FSS** | :material-checkbox-marked-circle:{ .corok } `SJNW` | 1, 2, 3, 4, 5, 6 | 8861             | 133.275            |
| **SBAO_NE_FSS** | :material-checkbox-marked-circle:{ .corok } `SJNE` | 7                | 17955            | 133.075            |
| **SBAO_SW_FSS** | :material-checkbox-marked-circle:{ .corok } `SJSW` | 8W               | 8855             | 133.450            |
| **SBAO_SE_FSS** | :material-checkbox-marked-circle:{ .corok } `SJSE` | 8E               | 5565             | 133.325            |

## Mapa Geral dos Combinados

<!-- ![Divisão da FIR Atlântico](../sbao.png){ align=left } -->


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
    zoomPadrao: 4,
    pontoCentral: [-15.382442, -30.714408],
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

const sbao = [ [-51.6122, 4.4131], [-48, 5], [-40, 5], [-38.6544, 5.6908], [-37.3333, 6.4167], [-37.0767, 6.5883], [-35, 7.6667], [-34.1104, 7.0236], [-32.3326, 5.7295], [-31.6317, 5.2167], [-30.805, 4.6019], [-28.8, 3.1283], [-27.5094, 2.1675], [-24.1349, -0.3502], [-21.4245, -2.3693], [-19.308, -3.9386], [-17.4706, -5.2926], [-16, -6.3667], [-10, -6.3667], [-10, -12.000556], [-9.9994, -19.8819], [-10, -34], [-30, -34], [-42, -34], [-50.3972, -34], [-46.8336, -30.4004], [-45.396, -28.7836], [-43.75, -26.75], [-40.9592, -24.6653], [-40.273056, -24.130556], [-39.5692, -23.5814], [-38.8208, -22.9825], [-38.1472, -22.4338], [-39.0163, -21.5594], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189], [-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-47.0542, 1.2353], [-49.3301, 2.8265] ]
const sbao_n = [ [-51.6122,4.4131], [-48,5], [-40,5], [-38.6544,5.6908], [-37.3333,6.4167], [-37.0767,6.5883], [-35,7.6667], [-34.1104,7.0236], [-32.3326,5.7295], [-31.6317,5.2167], [-30.805,4.6019], [-28.8,3.1283], [-27.5094,2.1675], [-24.1349,-0.3502], [-21.4245,-2.3693], [-19.308,-3.9386], [-17.4706,-5.2926], [-16,-6.3667], [-10,-6.3667], [-10,-12.000556], [-9.9994,-19.8819], [-11.7341,-19.2015], [-13.4545,-18.5048], [-15.1608,-17.7924], [-16.8535,-17.0653], [-18.533,-16.3241], [-20.1998,-15.5696], [-21.8544,-14.8026], [-23.4973,-14.0236], [-25.1291,-13.2336], [-26.7503,-12.4332], [-28.0482,-11.4999], [-30.0907,-10.0145], [-31.1903,-9.4499], [-31.8644,-9.1011], [-30.1192,-6.5894], [-28.3914,-4.0714], [-29.2432,-3.6192], [-31.2094,-3.3882], [-32.1211,-3.2717], [-33.5089,-2.6381], [-34.8803,-2.0189], [-35.4608,-1.7439], [-36.2217,-1.3619], [-37.9531,-0.4917], [-39,0], [-39.9331,0.5036], [-40.7822,0.9303], [-41.7,-1.7569], [-41.8556,-2.1744], [-47.0542,1.2353], [-49.3301,2.8265] ]
const sbao_s = [ [-9.9994,-19.8819], [-10,-34], [-30,-34], [-42,-34], [-50.3972,-34], [-46.8336,-30.4004], [-45.396,-28.7836], [-43.75,-26.75], [-40.9592,-24.6653], [-40.273056,-24.130556], [-39.5692,-23.5814], [-38.8208,-22.9825], [-38.1472,-22.4338], [-39.0163,-21.5594], [-39.8122,-20.745], [-39.678,-20.598], [-39.6257,-20.5074], [-38.3444,-19.7896], [-37.6728,-18.8625], [-38.2428,-18.6793], [-37.6216,-17.4696], [-37.0281,-16.2961], [-35.8551,-14.6957], [-35.0828,-13.6253], [-34.4171,-12.7023], [-33.7561,-11.7775], [-32.9956,-10.7084], [-31.8644,-9.1011], [-31.1903,-9.4499], [-30.0907,-10.0145], [-28.0482,-11.4999], [-26.7503,-12.4332], [-25.1291,-13.2336], [-23.4973,-14.0236], [-21.8544,-14.8026], [-20.1998,-15.5696], [-18.533,-16.3241], [-16.8535,-17.0653], [-15.1608,-17.7924], [-13.4545,-18.5048], [-11.7341,-19.2015] ]
const sbao_nw = [ [-51.6122,4.4131], [-48,5], [-40,5], [-38.6544,5.6908], [-37.3333,6.4167], [-37.0767,6.5883], [-35,7.6667], [-34.1104,7.0236], [-32.3326,5.7295], [-31.6317,5.2167], [-30.805,4.6019], [-28.8,3.1283], [-27.5094,2.1675], [-24.1349,-0.3502], [-26.2339,-3.0872], [-28.3437,-5.8198], [-29.761,-7.6373], [-31.1903,-9.4499], [-31.8644,-9.1011], [-30.1192,-6.5894], [-28.3914,-4.0714], [-29.2432,-3.6192], [-31.2094,-3.3882], [-32.1211,-3.2717], [-33.5089,-2.6381], [-34.8803,-2.0189], [-35.4608,-1.7439], [-36.2217,-1.3619], [-37.9531,-0.4917], [-39,0], [-39.9331,0.5036], [-40.7822,0.9303], [-41.7,-1.7569], [-41.8556,-2.1744], [-47.0542,1.2353], [-49.3301,2.8265] ]
const sbao_ne = [ [-24.1349,-0.3502], [-21.4245,-2.3693], [-19.308,-3.9386], [-17.4706,-5.2926], [-16,-6.3667], [-10,-6.3667], [-10,-12.000556], [-9.9994,-19.8819], [-11.7341,-19.2015], [-13.4545,-18.5048], [-15.1608,-17.7924], [-16.8535,-17.0653], [-18.533,-16.3241], [-20.1998,-15.5696], [-21.8544,-14.8026], [-23.4973,-14.0236], [-25.1291,-13.2336], [-26.7503,-12.4332], [-28.0482,-11.4999], [-30.0907,-10.0145], [-31.1903,-9.4499], [-29.761,-7.6373], [-28.3437,-5.8198], [-26.2339,-3.0872] ]
const sbao_sw = [ [-30,-34], [-42,-34], [-50.3972,-34], [-46.8336,-30.4004], [-45.396,-28.7836], [-43.75,-26.75], [-40.9592,-24.6653], [-40.273056,-24.130556], [-39.5692,-23.5814], [-38.8208,-22.9825], [-38.1472,-22.4338], [-39.0163,-21.5594], [-39.8122,-20.745], [-39.678,-20.598], [-39.6257,-20.5074], [-38.3444,-19.7896], [-37.6728,-18.8625], [-38.2428,-18.6793], [-37.6216,-17.4696], [-37.0281,-16.2961], [-35.8551,-14.6957], [-35.0828,-13.6253], [-34.4171,-12.7023], [-33.7561,-11.7775], [-32.9956,-10.7084], [-31.8644,-9.1011], [-31.1903,-9.4499], [-30.0907,-10.0145], [-28.0482,-11.4999], [-26.7503,-12.4332], [-25.1291,-13.2336], [-30,-16] ]
const sbao_se = [ [-30,-34], [-30,-16], [-25.1291,-13.2336], [-23.4973,-14.0236], [-21.8544,-14.8026], [-20.1998,-15.5696], [-18.533,-16.3241], [-16.8535,-17.0653], [-15.1608,-17.7924], [-13.4545,-18.5048], [-11.7341,-19.2015], [-9.9994,-19.8819], [-10,-34] ]

var sbaoPolygon = L.polygon(reverteCoord(sbao), {
    color: cores.vermelho,
    weight: 3
});
sbaoPolygon.bindPopup("<b>SBAO_FSS</b><br><i>133.500 MHz (4669 kHz)</i><br><b>CPDLC:</b> SBAO");

var sbaonPolygon = L.polygon(reverteCoord(sbao_n), {
    color: cores.ciano,
    weight: 3
});
sbaonPolygon.bindPopup("<b>SBAO_N_FSS</b><br><i>133.025 MHz (13315 kHz)</i><br><b>CPDLC:</b> SJAN");

var sbaosPolygon = L.polygon(reverteCoord(sbao_s), {
    color: cores.amarelo,
    weight: 3
});
sbaosPolygon.bindPopup("<b>SBAO_S_FSS</b><br><i>133.125 MHz (10096 kHz)</i><br><b>CPDLC:</b> SJAS");

var sbaonwPolygon = L.polygon(reverteCoord(sbao_nw), {
    color: cores.verde,
    weight: 3
});
sbaonwPolygon.bindPopup("<b>SBAO_NW_FSS</b><br><i>133.275 MHz (8861 kHz)</i><br><b>CPDLC:</b> SJNW");

var sbaonePolygon = L.polygon(reverteCoord(sbao_ne), {
    color: cores.rosa,
    weight: 3
});
sbaonePolygon.bindPopup("<b>SBAO_NE_FSS</b><br><i>133.075 MHz (17955 kHz)</i><br><b>CPDLC:</b> SJNE");

var sbaoswPolygon = L.polygon(reverteCoord(sbao_sw), {
    color: cores.amarelo,
    weight: 3
});
sbaoswPolygon.bindPopup("<b>SBAO_SW_FSS</b><br><i>133.450 MHz (8855 kHz)</i><br><b>CPDLC:</b> SJSW");

var sbaosePolygon = L.polygon(reverteCoord(sbao_se), {
    color: cores.verde,
    weight: 3
});
sbaosePolygon.bindPopup("<b>SBAO_SE_FSS</b><br><i>133.325 MHz (5565 kHz)</i><br><b>CPDLC:</b> SJSE");

/**
 *  Fluxos
 * 
 */ 
var firInteiraGrupo = L.layerGroup([sbaoPolygon]);
var combinadosGrupo = L.layerGroup([sbaonwPolygon,sbaonePolygon,sbaoswPolygon,sbaosePolygon]);
var superCombinadoN = L.layerGroup([sbaonPolygon]);
var superCombinadoS = L.layerGroup([sbaosPolygon]);

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
    "SBAO_FSS": firInteiraGrupo,
    "SBAO_N_FSS": superCombinadoN,
    "SBAO_S_FSS": superCombinadoS,
    "Combinados": combinadosGrupo
};

var layerControl = L.control.layers(opcoesDeMapa, opcoesDeFluxo).addTo(mapa1);

</script>

<!-- SB
SD - RE
SJ - AO
SN - AZ
SS - CW
SW - BS -->