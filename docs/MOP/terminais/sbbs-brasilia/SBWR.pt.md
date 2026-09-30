---
title: SBWR - Brasília
tags:
  - Terminal
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Brasília |
| **Posição** | `SBWR_APP` |
| **Indicativo** | Controle Brasília |
| **Frequência** | **119.200** MHz[^pacote] |
| **Frequências no mundo real** | 119.200 / 119.500 / 119.700 / 120.000 / 120.300 / 120.650 / 129.150 / 129.600 / 121.150 (VFR) MHz |
| **Horário no mundo real** | H24 |
| **Vigilância ATS** | Radar (consta na AIP ENR 1.6) |
| **Aeródromos na TMA** | [SBBR](../../aerodromos/sbbs-brasilia/twr/SBBR.pt.md) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo principal da TMA (SBBR).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBBR?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Meteorologia"
    <div id="metar-taf-container" data-airport="SBBR" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Carregando o METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Carregando o TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBBR){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| TMA Brasília | FL065 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Brasília | GND – FL065 | <span class="classe-badge classe-c">C</span> |
| ATZ Brasília | GND – 5500 FT | — |

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBWR_APP** | `WR` | Controle Brasília | **119.200** |  |
| **SBBR_TWR** | `TBR` | Torre Brasília | **118.100** |  |

## :material-arrow-down-bold-box-outline: Cobertura top-down

Leia de baixo para cima: com a posição desconectada, o espaço aéreo passa para a próxima posição on-line acima.

??? info "Ver diagrama de cobertura"
    ```mermaid
    flowchart BT
        p0["SBBS_CTR"]:::ctr
        p1["SBBS_NE_CTR"]:::ctr
        p2["SBBS_NS_CTR"]:::ctr
        p3["SBBS_N_CTR"]:::ctr
        p4["SBWR_APP"]:::app
        p5["SBBR_TWR"]:::twr
        a0(["TMA Brasília"]):::esp --> p4
        a1(["CTR Brasília<br>ATZ Brasília"]):::esp --> p5
        p1 --> p0
        p2 --> p1
        p3 --> p2
        p4 --> p3
        p5 --> p4
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
    ```

## :material-airplane: Circulação VFR

- A frequência 121.150 MHz é a primária para tráfego VFR no mundo real.
- Não são aceitos planos AFIL, nem plano de voo simplificado por radiotelefonia a partir do solo.
- Helicópteros no setor Sul: altitude mínima de 4100 FT (600 FT AGL).
- Decolagens de aeródromos e helipontos dentro da projeção da ATZ devem chamar a TWR antes de decolar.
- Proibidos treinamento e toque e arremetida em SBBR das 0800 às 1500 e das 2100 às 0100 UTC.
- Carta de rotas VFR: [CCV REA WR-Brasília](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf){ target="_blank" }

## :material-note-text-outline: Observações

- A TMA é classe A entre FL145 e FL195 e classe C entre FL065 e FL145. O APP é dividido em oito setores; os setores 05 a 08 atendem as saídas norte e sul.
- No mundo real há separação mínima de 3 NM dentro de 40 NM de SBBR.
- As ATZs não têm classe publicada na AIP (ENR 2.2).

---

Fontes: pacote de setores SBBS da VATSIM Brasil (limites laterais, posições, frequências e cobertura top-down) e AIP Brasil, emendas AIRAC A 13, A 15 e A 17/2026 (classes, limites verticais, vigilância ATS e regras VFR).

Voltar para a [visão geral das terminais](index.pt.md) da FIR Brasília.

[^pacote]: Frequência no pacote de setores da VATSIM Brasil.

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
    {"tipo": "tma", "id": "SBWR", "nome": "TMA Brasília", "posicao": "SBWR_APP", "freq": "119.200", "lim": "FL065 – FL195", "classe": "A/C", "link": "", "contorno": [[-47.864047, -15.002428], [-47.764833, -15.015167], [-47.446, -15.162667], [-47.140167, -15.4365], [-47.063742, -16.008367], [-47.060556, -16.032222], [-47.242833, -16.388], [-47.325, -16.486667], [-47.339352, -16.499838], [-47.427097, -16.579906], [-47.442167, -16.593667], [-47.542167, -16.6595], [-47.694508, -16.708267], [-47.931333, -16.780833], [-48.084167, -16.7755], [-48.299, -16.742167], [-48.448333, -16.689667], [-48.477, -16.664667], [-48.644833, -16.548667], [-48.5995, -16.235667], [-48.541667, -16.099333], [-48.602333, -15.852833], [-48.775105, -15.785841], [-48.936167, -15.723167], [-48.946667, -15.671333], [-48.7775, -15.333333], [-48.674833, -15.243], [-48.401431, -15.049731], [-48.077167, -14.965], [-47.960556, -14.99], [-47.889153, -14.999181], [-47.864047, -15.002428]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "CTR Brasília", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – FL065", "classe": "C", "link": "", "contorno": [[-48.4375, -15.645], [-48.393056, -16.179444], [-47.391389, -16.108333], [-47.432778, -15.573611], [-48.4375, -15.645]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "ATZ Brasília", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – 5500 FT", "classe": "—", "link": "", "contorno": [[-48.021944, -15.837778], [-47.988889, -15.806944], [-47.858333, -15.798056], [-47.823056, -15.826667], [-47.816667, -15.912778], [-47.849722, -15.943611], [-47.980278, -15.952778], [-48.015278, -15.924444], [-48.021944, -15.837778]]}
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
        v.lim + ' · Classe ' + v.classe 
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
    "Claro": tileMapaClaro,
    "Escuro": tileMapaEscuro,
    "Arcgis Satélite": tileMapaSatelite
}, {
    "TMAs": grupoTma,
    "CTRs": grupoCtr,
    "Limite da FIR": grupoFir
}).addTo(mapa);

// Legenda das classes
var legenda = L.control({ position: 'bottomleft' });
legenda.onAdd = function () {
    var div = L.DomUtil.create('div', 'mapa-legenda');
    div.innerHTML = '<b>Classe</b>' + ['A', 'C', 'D'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('');
    return div;
};
legenda.addTo(mapa);

})();
</script>
