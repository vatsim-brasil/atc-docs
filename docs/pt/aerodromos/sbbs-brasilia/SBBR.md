# SBBR - Brasília

## Dados Gerais

|                           | Informações                      |
|---------------------------|----------------------------------|
| **Nome do aeródromo**     | Presidente Juscelino Kubitschek  |
| **Tipo de Operação**      | Internacional, Público e Militar |
| **Regras de voo**         | IFR/VFR                          |
| **Altitude de transição** | 7000 pés                         |
| **Elevação**              | 3498 pés (1066m)                 |

## Pistas

### Descrição

| Pista | ILS                                         | Circuito                                          |
| ----- | ------------------------------------------- | ------------------------------------------------- |
| `11L` | :fontawesome-solid-circle-check:{ .corok }  | :fontawesome-solid-left-long: Padrão (`VAC`)      |
| `29R` | :fontawesome-solid-circle-xmark:{ .cornot } | :fontawesome-solid-right-long: Não-padrão (`VAC`) |
| `11R` | :fontawesome-solid-circle-check:{ .corok }  | :fontawesome-solid-right-long: Não-padrão (`VAC`) |
| `29L` | :fontawesome-solid-circle-check:{ .corok }  | :fontawesome-solid-left-long: Padrão (`VAC`)      |

| Pistas | Preferencial                                  | ILS                                      | Circuito            |
|--------|-----------------------------------------------|------------------------------------------|---------------------|
| `10L`  | Preferencial para **decolagem**               | :fontawesome-solid-circle-check:{.corok} | Circuito não padrão |
| `10R`  | Preferencial para **pousos**                  | :fontawesome-solid-circle-check:{.corok} | Circuito não padrão | 
| `28L`  | Preferencial para **pousos** quando em uso    | :fontawesome-solid-circle-check:{.corok} | Padrão              |
| `28R`  | Preferencial para **decolagem** quando em uso | :fontawesome-solid-circle-check:{.corok} | Padrão              |

<!--
### Configurações

| Configuração | Decolagem   | Pouso       | Observações                                                                                     |
| ------------ | ----------- | ----------- | ----------------------------------------------------------------------------------------------- |
| **LESTE**    | `11L` `11R` | `11L` `11R` | Prioriza-se a `11L` nas saídas para o setor **NORTE** e a `11R` nas saídas para o setor **SUL** |
| **OESTE**    | `29L` `29R` | `29L` `29R` | Prioriza-se a `29R` nas saídas para o setor **NORTE** e a `29L` nas saídas para o setor **SUL** |
-->

## Órgãos ATC

| Código     | Abrev. | Indicativo de Chamada | Frequência              | Observações |
| ---------- | ------ | --------------------- | ----------------------- | ----------- |
| SBBR_ATIS  | `ABR`  | ATIS Brasília         | 127.800                 |             |
| SBBR_DEL   | `DBR`  | Tráfego Brasília      | 121.000                 | `DCL`       |
| SBBR_GND   | `GBR`  | Solo Brasília         | 121.800 121.950         |             |
| SBBR_TWR   | `TBR`  | Torre Brasília        | 118.100 118.450 118.750 |             |
| SBBR_M_TWR | `OBR`  | Operações Brasília    | 122.500 135.850         |             |

## Operações

### Gerais

- A TWR Brasília não informará a hora de decolagem às ACFT. A instrução quanto à FREQ do próximo órgão a ser chamado AFT TKOF e, se necessárias, instruções complementares, serão emitidas juntamente com a AUTH de TKOF.
- Nas OPS de LDG, os pilotos não reportarão para TWR Brasília a COND de trem de pouso, EXC nas situações de EMERG com referência ao seu baixamento e/ou travamento.
- Todas as decolagens deverão empregar procedimento de abatimento de ruído, conforme manual de cada aeronave.
- Nas operações de decolagem, as aeronaves devem utilizar, em condições normais de operação, as pistas `11L` ou `29R` com destino a localidades situadas ao **Norte** e **Nordeste** de Brasília. E, aquelas com destino a localidades ao **Sul** e **Sudeste** utilizem `11R` ou `29L`.
- Nas operações de pouso, as aeronaves devem utilizar, em condições normais de operação, as pistas `11L` ou `29R` procedentes de localidades situadas ao **Norte** e **Nordeste** de Brasília. E, aquelas procedentes de localidades ao **Sul** e **Sudeste** utilizem `11R` ou `29L`.

### Específicas

#### Operações Paralelas Simultâneas

#### Tráfego VFR

- OBS VAC para entrada ou saída do circuito de TFC.

#### Pátios e Pistas de Taxi

- BFR ingresso TWY `Q` a partir da TWY `QQ`, compulsório CTC com a TWR informando posicionamento da ACFT. Permitido taxi de ACFT com envergadura até 20m.
- TWY `L4`, `L5`, `L6`, `L8` e `R` BTN `L3` e `L7`, envergadura MAX 36M.
- ACFT aviação geral com DEST ao pátio 02 deverão utilizar obrigatoriamente TWY do pátio 02 (PSN 52 a 61). No período noturno OPR com CTN devido pátio LGTD, porém sem balizamento.
- TWY `QQ`, operação diurna e noturna por responsabilidade do OPR da ACFT.

#### Locais

`NIL`

## Posições de Parada

| Posições | Classificação                    |
| :------: | -------------------------------- |
|  1 - 4   | Voos Internacionais              |
|  5 - 16  | Gol                              |
| 17 - 24  | Azul                             |
| 25 - 41  | Latam                            |
| 47 - 51  | Cargas de Grande Porte / Remotas |
| 52 - 66  | Cargas de Grande Porte / Remotas |

## Fluxos de Solo

!!! info "Uma informação..."

    Selecione a pista em uso no canto superior direito do mapa para visualizar o respectivo fluxo de solo.

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
    tileMapaUrlEscuro: 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
    tileMapaUrlClaro: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
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

var tileMapaClaro = L.tileLayer(configMapa.tileMapaUrlClaro, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; CartoDB'
});

var tileMapaEscuro = L.tileLayer(configMapa.tileMapaUrlEscuro, {
    minZoom: configMapa.zoomMin,
    maxZoom: configMapa.zoomMax,
    attribution: '&copy; CartoDB'
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
    "Satélite": tileMapaSatelite,
    //"Claro": tileMapaClaro,
    //"Escuro": tileMapaEscuro,
    "OSM": tileMapaOsm,
    "OPNV": tileMapaOPNV,
};

var opcoesDeFluxo = {
    "Pista 11L - Saídas": fluxoPista11Ldep,
    "Pista 29L - Saídas": fluxoPista29Ldep,
};

var layerControl = L.control.layers(opcoesDeMapa, opcoesDeFluxo).addTo(mapa1);

</script>
