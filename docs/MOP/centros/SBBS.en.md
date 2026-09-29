---
  title: SBBS - Brasília
---

--8<-- "includes/abreviacoes.md"

## Sectorization

!!! info "Map Interactivity"

    Click any of the sectors below the map to highlight it. You can also change the base map and toggle sectors on/off using the layer control in the upper right corner of the map.

<div class="fir-map-top">
    <div id="mapa1" class="mapa"></div>
</div>

<div class="fir-cards-section">
    <div class="sbre-cards-section-title">Combined Sectors</div>
    <div class="fir-cards-grid">
        <div class="sector-card" id="card-SBBS_N_CTR" onclick="selecionarSetor('SBBS_N_CTR')">
            <div class="sector-header">
                <span class="sector-badge bs-n">SBBS_N_CTR</span>
                <span class="sector-freq">124.700 MHz</span>
            </div>
            <div class="sector-body">
                Composed of the combination (union) of sectors 11, 12, 13, 14, 15, 16, 17 and 18 of the Brasilia FIR.
            </div>
        </div>
        <div class="sector-card" id="card-SBBS_E_CTR" onclick="selecionarSetor('SBBS_E_CTR')">
            <div class="sector-header">
                <span class="sector-badge bs-e">SBBS_E_CTR</span>
                <span class="sector-freq">124.800 MHz</span>
            </div>
            <div class="sector-body">
                Composed of the combination (union) of sectors 1, 2 and 3 of the Brasilia FIR.
            </div>
        </div>
        <div class="sector-card" id="card-SBBS_S_CTR" onclick="selecionarSetor('SBBS_S_CTR')">
            <div class="sector-header">
                <span class="sector-badge bs-s">SBBS_S_CTR</span>
                <span class="sector-freq">126.800 MHz</span>
            </div>
            <div class="sector-body">
                Composed of the combination (union) of sectors 4, 5, 6, 7, 8, 9 and 10 of the Brasilia FIR.
            </div>
        </div>
    </div>
</div>

<div class="fir-cards-section">
    <div class="sbre-cards-section-title">Super-Combined Sectors</div>
    <div class="fir-cards-grid">
        <div class="sector-card" id="card-SBBS_NE_CTR" onclick="selecionarSetor('SBBS_NE_CTR')">
            <div class="sector-header">
                <span class="sector-badge bs-ne">SBBS_NE_CTR</span>
                <span class="sector-freq">125.550 MHz</span>
            </div>
            <div class="sector-body">
                Composed of the combination (union) of the N and E combined sectors of the Brasilia FIR.
            </div>
        </div>
        <div class="sector-card" id="card-SBBS_NS_CTR" onclick="selecionarSetor('SBBS_NS_CTR')">
            <div class="sector-header">
                <span class="sector-badge bs-ns">SBBS_NS_CTR</span>
                <span class="sector-freq">133.750 MHz</span>
            </div>
            <div class="sector-body">
                Composed of the combination (union) of the N and S combined sectors of the Brasilia FIR.
            </div>
        </div>
        <div class="sector-card" id="card-SBBS_SE_CTR" onclick="selecionarSetor('SBBS_SE_CTR')">
            <div class="sector-header">
                <span class="sector-badge bs-se">SBBS_SE_CTR</span>
                <span class="sector-freq">128.050 MHz</span>
            </div>
            <div class="sector-body">
                Composed of the combination (union) of the S and E combined sectors of the Brasilia FIR.
            </div>
        </div>
    </div>
</div>

<div class="fir-cards-section">
    <div class="sbre-cards-section-title">General Position</div>
    <div class="fir-cards-grid">
        <div class="sector-card" id="card-SBBS_CTR" onclick="selecionarSetor('SBBS_CTR')">
            <div class="sector-header">
                <span class="sector-badge ctr">SBBS_CTR</span>
                <span class="sector-freq">134.000 MHz</span>
            </div>
            <div class="sector-body">
                Composed of the combination (union) of all combined sectors of the Brasilia FIR.
            </div>
        </div>
    </div>
</div>

<!--
Daqui pra baixo, são os mapas.
-->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>

<style>
    .mapa { height: 600px }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {
    ciano: '#2dd4bf',
    rosa: '#f472b6',
    verde: '#a3e635',
    amarelo: '#fbbf24',
    roxo: '#a78bfa',
    laranja: '#fb923c',
    vermelho: '#f87171'
}

const configMapa = {
    zoomMin: 3,
    zoomMax: 14,
    zoomPadrao: 6,
    pontoCentral: [-16.63, -47.97],
    tileMapaUrlSatelite: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    tileMapaUrlOsm: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
};

function reverteCoord(arrayOrig) {
    return arrayOrig.map(function(coord) {
        return [coord[1], coord[0]];
    });
}

// Limites laterais extraídos do pacote SBBS (setores FIR_SBBS_S01 a S18)
const sbbs_n = [[-51.3619, -20.4271], [-52.0114, -19.7046], [-52.7536, -18.9223], [-54.1235, -17.4059], [-53.1008, -16.7092], [-53.3203, -15.8089], [-53.3927, -15.4768], [-53.6267, -14.5625], [-53.5013, -12.96], [-53.051, -12.1836], [-51.672778, -11.0275], [-51.4728, -10.8474], [-51.0866, -10.5156], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.3153, -10.3287], [-46.891, -12.0218], [-45.6083, -13.3218], [-45.278124, -13.796406], [-44.5772, -14.7847], [-44.2492, -15.3602], [-45.0292, -16.3608], [-45.8172, -17.3584], [-46.0441, -17.903], [-46.5301, -19.0563], [-47.283397, -18.978726], [-48.2209, -18.8774], [-48.913423, -18.920339], [-49.2865, -18.9425], [-49.9843, -19.4474], [-50.3958, -19.7425]]
const sbbs_e = [[-45.4551, -20.3237], [-46.011, -19.4422], [-46.5301, -19.0563], [-46.0441, -17.903], [-45.8172, -17.3584], [-45.0292, -16.3608], [-44.2492, -15.3602], [-44.095833, -15.626499], [-42.6788, -16.4093], [-42.3377, -16.6247], [-41.8206, -16.9483], [-42.4482, -18.758], [-42.4406, -19.105], [-42.4795, -19.463], [-42.5269, -20.0033], [-42.7521, -20.4117], [-43.3928, -20.1562], [-43.965, -20.5375], [-44.7076, -21.4759], [-45.0073, -21.0164]]
const sbbs_s = [[-45.7749, -22.7993], [-45.8108, -23.0094], [-45.86, -23.2332], [-46.655, -23.6273], [-47.2173, -23.3154], [-47.573, -23.1164], [-47.726084, -23.065083], [-48.832226, -22.69952], [-49.9178, -22.3302], [-50.105463, -22.08634], [-50.4579, -21.6254], [-51.3619, -20.4271], [-50.3958, -19.7425], [-49.9843, -19.4474], [-49.2865, -18.9425], [-48.913423, -18.920339], [-48.2209, -18.8774], [-47.283397, -18.978726], [-46.5301, -19.0563], [-46.011, -19.4422], [-45.4551, -20.3237], [-45.0073, -21.0164], [-44.7076, -21.4759]]
const sbbs_ne = [[-51.3619, -20.4271], [-52.0114, -19.7046], [-52.7536, -18.9223], [-54.1235, -17.4059], [-53.1008, -16.7092], [-53.3203, -15.8089], [-53.3927, -15.4768], [-53.6267, -14.5625], [-53.5013, -12.96], [-53.051, -12.1836], [-51.672778, -11.0275], [-51.4728, -10.8474], [-51.0866, -10.5156], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.3153, -10.3287], [-46.891, -12.0218], [-45.6083, -13.3218], [-45.278124, -13.796406], [-44.5772, -14.7847], [-44.3306, -15.2179], [-44.095833, -15.626499], [-42.6788, -16.4093], [-42.3377, -16.6247], [-41.8206, -16.9483], [-42.4482, -18.758], [-42.4406, -19.105], [-42.4795, -19.463], [-42.5269, -20.0033], [-42.7521, -20.4117], [-43.3928, -20.1562], [-43.965, -20.5375], [-44.7076, -21.4759], [-45.0073, -21.0164], [-45.4551, -20.3237], [-46.011, -19.4422], [-46.5301, -19.0563], [-47.283397, -18.978726], [-48.2209, -18.8774], [-48.913423, -18.920339], [-49.2865, -18.9425], [-49.9843, -19.4474], [-50.3958, -19.7425]]
const sbbs_ns = [[-50.105463, -22.08634], [-50.4579, -21.6254], [-51.3619, -20.4271], [-52.0114, -19.7046], [-52.7536, -18.9223], [-54.1235, -17.4059], [-53.1008, -16.7092], [-53.3203, -15.8089], [-53.3927, -15.4768], [-53.6267, -14.5625], [-53.5013, -12.96], [-53.051, -12.1836], [-51.672778, -11.0275], [-51.4728, -10.8474], [-51.0866, -10.5156], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.3153, -10.3287], [-46.891, -12.0218], [-45.6083, -13.3218], [-45.278124, -13.796406], [-44.5772, -14.7847], [-44.2492, -15.3602], [-45.0292, -16.3608], [-45.8172, -17.3584], [-46.0441, -17.903], [-46.5301, -19.0563], [-46.011, -19.4422], [-45.4551, -20.3237], [-45.0073, -21.0164], [-44.7076, -21.4759], [-45.7749, -22.7993], [-45.8108, -23.0094], [-45.86, -23.2332], [-46.655, -23.6273], [-47.2173, -23.3154], [-47.573, -23.1164], [-47.726084, -23.065083], [-48.832226, -22.69952], [-49.9178, -22.3302]]
const sbbs_se = [[-49.9178, -22.3302], [-50.105463, -22.08634], [-50.4579, -21.6254], [-51.3619, -20.4271], [-50.3958, -19.7425], [-49.9843, -19.4474], [-49.2865, -18.9425], [-48.913423, -18.920339], [-48.2209, -18.8774], [-47.283397, -18.978726], [-46.5301, -19.0563], [-46.0441, -17.903], [-45.8172, -17.3584], [-45.0292, -16.3608], [-44.2492, -15.3602], [-44.095833, -15.626499], [-42.6788, -16.4093], [-42.3377, -16.6247], [-41.8206, -16.9483], [-42.4482, -18.758], [-42.4406, -19.105], [-42.4795, -19.463], [-42.5269, -20.0033], [-42.7521, -20.4117], [-43.3928, -20.1562], [-43.965, -20.5375], [-44.7076, -21.4759], [-45.7749, -22.7993], [-45.8108, -23.0094], [-45.86, -23.2332], [-46.655, -23.6273], [-47.2173, -23.3154], [-47.573, -23.1164], [-47.726084, -23.065083], [-48.832226, -22.69952]]
const sbbs = [[-50.105463, -22.08634], [-50.4579, -21.6254], [-51.3619, -20.4271], [-52.0114, -19.7046], [-52.7536, -18.9223], [-54.1235, -17.4059], [-53.1008, -16.7092], [-53.3203, -15.8089], [-53.3927, -15.4768], [-53.6267, -14.5625], [-53.5013, -12.96], [-53.051, -12.1836], [-51.672778, -11.0275], [-51.4728, -10.8474], [-51.0866, -10.5156], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.3153, -10.3287], [-46.891, -12.0218], [-45.6083, -13.3218], [-45.278124, -13.796406], [-44.5772, -14.7847], [-44.3306, -15.2179], [-44.095833, -15.626499], [-42.6788, -16.4093], [-42.3377, -16.6247], [-41.8206, -16.9483], [-42.4482, -18.758], [-42.4406, -19.105], [-42.4795, -19.463], [-42.5269, -20.0033], [-42.7521, -20.4117], [-43.3928, -20.1562], [-43.965, -20.5375], [-44.7076, -21.4759], [-45.7749, -22.7993], [-45.8108, -23.0094], [-45.86, -23.2332], [-46.655, -23.6273], [-47.2173, -23.3154], [-47.573, -23.1164], [-47.726084, -23.065083], [-48.832226, -22.69952], [-49.9178, -22.3302]]

var sbbsnPolygon = L.polygon(reverteCoord(sbbs_n), {
    color: cores.amarelo,
    weight: 3
});
sbbsnPolygon.bindPopup("<b>SBBS_N_CTR</b><br><i>124.700 MHz</i>");

var sbbsePolygon = L.polygon(reverteCoord(sbbs_e), {
    color: cores.ciano,
    weight: 3
});
sbbsePolygon.bindPopup("<b>SBBS_E_CTR</b><br><i>124.800 MHz</i>");

var sbbssPolygon = L.polygon(reverteCoord(sbbs_s), {
    color: cores.verde,
    weight: 3
});
sbbssPolygon.bindPopup("<b>SBBS_S_CTR</b><br><i>126.800 MHz</i>");

var sbbsnePolygon = L.polygon(reverteCoord(sbbs_ne), {
    color: cores.rosa,
    weight: 3
});
sbbsnePolygon.bindPopup("<b>SBBS_NE_CTR</b><br><i>125.550 MHz</i>");

var sbbsnsPolygon = L.polygon(reverteCoord(sbbs_ns), {
    color: cores.roxo,
    weight: 3
});
sbbsnsPolygon.bindPopup("<b>SBBS_NS_CTR</b><br><i>133.750 MHz</i>");

var sbbssePolygon = L.polygon(reverteCoord(sbbs_se), {
    color: cores.laranja,
    weight: 3
});
sbbssePolygon.bindPopup("<b>SBBS_SE_CTR</b><br><i>128.050 MHz</i>");

var sbbsPolygon = L.polygon(reverteCoord(sbbs), {
    color: cores.vermelho,
    weight: 3
});
sbbsPolygon.bindPopup("<b>SBBS_CTR</b><br><i>134.000 MHz</i>");

/**
 *  Fluxos
 *
 */
var firInteiraGrupo = L.layerGroup([sbbsPolygon]);
var combinadosGrupo = L.layerGroup([sbbsnPolygon, sbbsePolygon, sbbssPolygon]);
var superCombinadoNE = L.layerGroup([sbbsnePolygon]);
var superCombinadoNS = L.layerGroup([sbbsnsPolygon]);
var superCombinadoSE = L.layerGroup([sbbssePolygon]);


var tileMapaClaro = camadaMapbox('claro', {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax
});

var tileMapaEscuro = camadaMapbox('escuro', {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax
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
    layers: [ tileMapaClaro, firInteiraGrupo ]
}).setView(configMapa.pontoCentral, configMapa.zoomPadrao);

mapa1.fitBounds(sbbsPolygon.getBounds(), { padding: [20, 20] });


var opcoesDeMapa = {
    "Light": tileMapaClaro,
    "Dark": tileMapaEscuro,
    "Arcgis Satellite": tileMapaSatelite,
    "Open Street Map": tileMapaOsm,
};

var opcoesDeFluxo = {
    "SBBS_CTR": firInteiraGrupo,
    "SBBS_NE_CTR": superCombinadoNE,
    "SBBS_NS_CTR": superCombinadoNS,
    "SBBS_SE_CTR": superCombinadoSE,
    "Combined": combinadosGrupo
};

var layerControl = L.control.layers(opcoesDeMapa, opcoesDeFluxo).addTo(mapa1);

// Mapeamento dos setores para suas respectivas camadas e polígonos
const gruposDeSetor = {
    'SBBS_CTR': firInteiraGrupo,
    'SBBS_N_CTR': combinadosGrupo,
    'SBBS_E_CTR': combinadosGrupo,
    'SBBS_S_CTR': combinadosGrupo,
    'SBBS_NE_CTR': superCombinadoNE,
    'SBBS_NS_CTR': superCombinadoNS,
    'SBBS_SE_CTR': superCombinadoSE
};

const poligonosDeSetor = {
    'SBBS_CTR': sbbsPolygon,
    'SBBS_N_CTR': sbbsnPolygon,
    'SBBS_E_CTR': sbbsePolygon,
    'SBBS_S_CTR': sbbssPolygon,
    'SBBS_NE_CTR': sbbsnePolygon,
    'SBBS_NS_CTR': sbbsnsPolygon,
    'SBBS_SE_CTR': sbbssePolygon
};

function marcarCardAtivo(nomeSetor) {
    document.querySelectorAll('.sector-card').forEach(function(card) {
        card.classList.remove('active');
    });
    const cardAtivo = document.getElementById('card-' + nomeSetor);
    if (cardAtivo) {
        cardAtivo.classList.add('active');
    }
}

// Função global para selecionar um setor ao clicar no card correspondente
window.selecionarSetor = function(nomeSetor) {
    // 1. Remove todos os outros grupos do mapa
    Object.values(gruposDeSetor).forEach(function(grupo) {
        if (mapa1.hasLayer(grupo)) {
            mapa1.removeLayer(grupo);
        }
    });

    // 2. Adiciona o grupo correto
    const grupo = gruposDeSetor[nomeSetor];
    if (grupo) {
        mapa1.addLayer(grupo);
    }

    // 3. Destaca o polígono, ajusta o zoom e abre o popup
    const poligono = poligonosDeSetor[nomeSetor];
    if (poligono) {
        mapa1.fitBounds(poligono.getBounds(), { padding: [30, 30] });
        poligono.openPopup();
    }

    // 4. Atualiza o estado visual dos cards
    marcarCardAtivo(nomeSetor);

    // 5. Rola a página até o mapa
    document.getElementById('mapa1').scrollIntoView({ behavior: 'smooth', block: 'center' });
};

// Selecionar o setor geral como ativo na carga inicial
marcarCardAtivo('SBBS_CTR');

// Sincroniza os cards se o usuário interagir diretamente com o controle de camadas
mapa1.on('overlayadd', function(event) {
    for (const [setor, grupo] of Object.entries(gruposDeSetor)) {
        if (grupo === event.layer) {
            marcarCardAtivo(setor);
            break;
        }
    }
});

})();
</script>
