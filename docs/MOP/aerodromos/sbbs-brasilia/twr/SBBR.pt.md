---
title: SBBR - Brasília
tags:
  - Aeródromo
  - Controlado
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados Gerais
|                           | Informações                      |
|---------------------------|----------------------------------|
| **Nome do aeródromo**     | Presidente Juscelino Kubitschek  |
| **Tipo de Operação**      | Internacional, Público e Militar |
| **Altitude de transição** | 7000 pés |
| **Elevação** | 3498 pés (1066m) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo.

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
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBBR){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

## :material-routes: Pistas
### Descrição

| Pistas | Preferencial                                  | ILS                                      | Circuito            |
|--------|-----------------------------------------------|------------------------------------------|---------------------|
| **11L** | Preferencial com **componente de vento de cauda até 7 nós** com **pista seca**.[^1] / Preferencial para **operações** originadas de ou destinadas a localidades situadas ao **Norte** e **Nordeste** de Brasília.[^1]  | :fontawesome-solid-circle-check:{.corok} | Padrão |
| **29R** | Preferencial para **operações** originadas de ou destinadas a localidades situadas ao **Norte** e **Nordeste** de Brasília.[^1]  | :fontawesome-solid-circle-xmark:{ .cornot } | Não-padrão              |
| **11R** | Preferencial com **componente de vento de cauda até 7 nós** com **pista seca**.[^1] / Preferencial para **operações** originadas de ou destinadas a localidades situadas ao **Sul** e **Sudeste** de Brasília.[^1]  | :fontawesome-solid-circle-check:{.corok} | Não-padrão |
| **29L** | Preferencial para **operações** originadas de ou destinadas a localidades situadas ao **Sul** e **Sudeste** de Brasília.[^1]  | :fontawesome-solid-circle-check:{.corok} | Padrão              |

[^1]: [AIP Brasil, AD 2 SBBR 2.22](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) 

!!! warning "Operação Preferencial de Pista"

    Em condições meteorológicas com {==**componente de vento de cauda menor ou igual a 7KT**==}, a pista preferencial de pouso e decolagem será a RWY 11L/11R. Tal configuração será normalmente utilizada em preferência à utilização das RWYS 29R/29L, desde que a superfície da pista **esteja seca**. Quando a pista de pouso e decolagem em uso for RWY 11L/11R com componente de vento de cauda, os pilotos que solicitarem autorização para utilizar a RWY 29R/29L devem considerar que seu pouso ou decolagem {==**pode sofrer atraso**==}.

!!! warning "Operação em Horário de Pico de Decolagem"

    Nos momentos de pico de decolagem para os Setores N/NE/NW, a pista RWY 11L/29R será utilizada somente para DEP. As aproximações de todos os setores e as decolagens para o Setor S serão realizadas na RWY 11R/29L.

<!--
### Configurações

| Configuração | Decolagem   | Pouso       | Observações                                                                                     |
| ------------ | ----------- | ----------- | ----------------------------------------------------------------------------------------------- |
| **LESTE**    | `11L` `11R` | `11L` `11R` | Prioriza-se a `11L` nas saídas para o setor **NORTE** e a `11R` nas saídas para o setor **SUL** |
| **OESTE**    | `29L` `29R` | `29L` `29R` | Prioriza-se a `29R` nas saídas para o setor **NORTE** e a `29L` nas saídas para o setor **SUL** |
-->

## :material-headset: Órgãos ATC
| Código     | Abrev. | Indicativo de Chamada | Frequência              | Observações |
| ---------- | ------ | --------------------- | ----------------------- | ----------- |
| **SBBR_ATIS** | `ABR` | ATIS Brasília | **127.800** |  |
| **SBBR_DEL** | `DBR` | Tráfego Brasília | **121.000** | `DCL` |
| **SBBR_GND** | `GBR` | Solo Brasília | **121.800** |  |
| **SBBR_TWR** | `TBR` | Torre Brasília | **118.100** |  |
| **SBBR_M_TWR** | `OBR` | Operações Brasília | **122.500** |  |

## :material-airplane-takeoff: Operações

### Decolagens

- As ACFT serão instruídas pelo DEL a monitorarem (manter-se na escuta) a frequência do GND, para autorização de acionamento, sendo *desnecessária chamada inicial*.
- Na transferência de comunicações para a TWR, o GND instruirá às ACFT a monitorarem (manter-se na escuta) a frequência da TWR, não sendo necessária a chamada inicial. Nesse caso, as ACFT deverão aguardar a chamada da TWR, preparando-se para possível decolagem imediata.
- Os pilotos deverão planejar a TKOF de forma a chegar no ponto de espera prontos para executá-la. Havendo indisponibilidade de TKOF imediata, informar ao órgão ATC com antecedência.
- Espera-se que ao receber autorização de TKOF, o piloto inicie a corrida imediatamente (o tempo de reação esperado é de até 10 segundos).
- A TWR não informará a hora de TKOF às ACFT. A instrução quanto à FREQ do próximo órgão a ser chamado AFT TKOF e, se necessárias, instruções complementares, serão emitidas juntamente com a AUTH de TKOF.
- Todas as decolagens deverão empregar procedimento de abatimento de ruído, conforme manual de cada aeronave.
- Efetuar imediatamente a chamada inicial ao APP após a decolagem, a fim de obter instruções para livrar o eixo de pista de decolagem;
- A chamada inicial ao APP após a decolagem deverá ser imediata e observar somente o seguinte padrão: *CONTROLE BRASÍLIA, [CALLSIGN]*. Não incluir qualquer informação adicional ao mencionado padrão.
- Aguardar vetoração ou autorização direto a um waypoint publicado logo após a decolagem.
- As aeronaves código de referência A e B **deverão** ser configuradas para decolar das interseções abaixo:
    - *RWY 11L:*
        * Aeronaves código de referência A e B
            * TWY `C`
            * Distância da TWY `C` até a THR 29R: TORA Disponível: 2193 m
    - *RWY 11R:*
        * Aeronaves código de referência A e B
            * TWY `BB`
            * Distância da TWY `BB` até a THR 29L: TORA Disponível: 2188 m
    - *RWY 29R:*
        * Aeronaves código de referência A e B
            * TWY `F`
            * Distância da TWY `F` até a THR 29R: TORA Disponível: 1956 m
    - *RWY 29L:*
        * Aeronaves código de referência A e B
            * TWY `EE`
            * Distância da TWY `EE` até a THR 11R: TORA Disponível: 2161 m
- As aeronaves código de referência C ou acima também poderão ser autorizadas a decolar das interseções acima, a partir de solicitação da aeronave.
- Nas operações de decolagem, as aeronaves devem utilizar, em condições normais de operação, as pistas `11L` ou `29R` com destino a localidades situadas ao **Norte** e **Nordeste** de Brasília. E, aquelas com destino a localidades ao **Sul** e **Sudeste** utilizem `11R` ou `29L`.

### Aproximações e Pousos

- Nas OPS de LDG, os pilotos não reportarão para a TWR a COND de trem de pouso, EXC nas situações de EMERG com referência ao seu baixamento e/ou travamento.
- Os pilotos devem livrar a pista na velocidade mais rápida permitida pelos procedimentos operacionais padronizados e em conformidade com a segurança operacional, permitindo que o ATC aplique a separação mínima na aproximação final.
- Nas operações de pouso, as aeronaves devem utilizar, em condições normais de operação, as pistas `11L` ou `29R` procedentes de localidades situadas ao **Norte** e **Nordeste** de Brasília. E, aquelas procedentes de localidades ao **Sul** e **Sudeste** utilizem `11R` ou `29L`.

### Regulamentos do Aeródromo

- Copiada a autorização, as ACFT informarão ao DEL quando realmente estiverem prontas para o acionamento de motores.
- Alinhamento deve ser imediato assim que autorizado.
Em construção.
- OBS VAC para entrada ou saída do circuito de TFC.

### Pátios e Pistas de Taxi

- BFR ingresso TWY `Q` a partir da TWY `QQ`, compulsório CTC com a TWR informando posicionamento da ACFT. Permitido taxi de ACFT com envergadura até 20m.
- TWY `L4`, `L5`, `L6`, `L8` e `R` BTN `L3` e `L7`, envergadura MAX 36M.
- ACFT aviação geral com DEST ao pátio 02 deverão utilizar obrigatoriamente TWY do pátio 02 (PSN 52 a 61). No período noturno OPR com CTN devido pátio LGTD, porém sem balizamento.
- TWY `QQ`, operação diurna e noturna por responsabilidade do OPR da ACFT.

## :material-sign-direction: Posições de Parada
| Pátio       | Posições | Classificação                    |
| :---: | :---: | :--- |
|     `1`     |  1 - 4   | Internacionais                   |
|     `1`     |  5 - 41  | Domésticos                       |
|     `2`     | 52 - 66  | Cargas / Remotas                 |
|     `3`     | 67 - 70  | Cargas de Grande Porte / Remotas |
| **MILITAR** | ANY    | Militar - Operacional            |

<!--

## Fluxos de Solo

!!! info "Uma informação..."

    Selecione a pista em uso no canto superior direito do mapa para visualizar o respectivo fluxo de solo.

<div id="mapa1" class="mapa"></div>

-->

<!--
Daqui pra baixo, são os mapas.
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

-->