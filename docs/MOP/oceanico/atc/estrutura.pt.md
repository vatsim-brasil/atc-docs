---
title: Estrutura e Setorização
icon: material/layers-triple
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Esta página concentra os dados que mudam com o tempo. Nenhuma outra página do manual repete esses valores.

## Limites e classificação

O ACC Atlântico opera H24, em português e inglês, com indicativos **CENTRO ATLÂNTICO** e **ATLANTICO CENTER**[^1]. A responsabilidade se estende para leste até o meridiano **010° W**, por acordo regional[^2]. Ao sul, a FIR chega ao paralelo **34° S**[^1].

| Espaço aéreo  | Limites        | Classificação publicada                   |
| ------------- | -------------- | ----------------------------------------- |
| FIR Atlântico | GND a UNL      | `A` acima do FL 245, `G` abaixo do FL 145 |
| Atlântico UIR | FL 245 a UNL   | `A` acima do FL 245                       |

Duas observações que valem na prática:

- O espaço superior é uma **UIR**, e não uma UTA como nas FIR continentais[^1]. A classe é `A` nos dois casos.
- Entre o FL 145 e o FL 245 não há classificação publicada específica para esta FIR. Vale a regra geral: aerovias acima do FL 145 são Classe `A`[^3].

## Setores e frequências HF publicadas

A AIP divide a FIR em **oito setores**, `SECT 01` a `SECT 08`, todos GND/UNL e todos do ACC Atlântico[^1].

| Setores AIP           | Frequências HF publicadas (kHz)       |
| --------------------- | ------------------------------------- |
| `SECT 01` a `SECT 04` | 3452, 4669, 6649, 8861, 13357         |
| `SECT 05` a `SECT 08` | 4669, 5565, 8855, 10096, 13315, 17955 |

**4669 kHz** é a única publicada para os oito setores, e por isso é a referência da posição que cobre a FIR inteira.

## Corredor EUR/SAM e AORRA

Dois volumes se sobrepõem à FIR e concentram quase todo o tráfego. Ambos entre o **FL 290 e o FL 410**.

| | Corredor EUR/SAM | AORRA |
| --- | --- | --- |
| **Tráfego** | Brasil e Europa ou norte da África | Brasil e África Meridional |
| **Estrutura** | Rotas ATS fixas | Rotas aleatórias entre portões |
| **Exigência** | RNP 10 e RVSM[^4] [^5] | RNP 10[^6] |
| **Rotas ou portões** | UN741, UN866, UN873, UN857, e os prolongamentos por `DAKAP` (UZ51) e `BUGAT` (UL206)[^7] | `SORSA`, `CIDER`, `MIGEX`, `VURTO`, `EKALO`, `EDVEL`, `MUKEK`, `OBKOL`, `GELAM`, `VURIL`, `GARUP`[^6] |
| **Reporte obrigatório** | Pontos de notificação da rota | 010° E, 000°, 010° W, 020° W, 030° W, 040° W e 050° W[^6] |

Entrando na FIR rumo à AORRA pelos fixos `ARUSI` ou `UKEDI` com trajetória por waypoints brasileiros, **a capacidade ADS-C e CPDLC é obrigatória**[^6].

## Níveis de cruzeiro

| Rumo magnético | RVSM (geral)[^5]                            | AORRA[^6]              | RVSM suspenso[^5]      |
| :------------: | :-----------------------------------------: | :--------------------: | :--------------------: |
| 000° a 179°    | 290, 310, 330, 350, 370, 390, 410           | 290, 350, 410          | 290, 350, 410          |
| 180° a 359°    | 300, 320, 340, 360, 380, 400                | 320, 380               | 320, 380               |

O RVSM é suspenso quando houver informação de pilotos sobre turbulência severa[^8].

## Órgãos adjacentes

| Sentido               | Órgãos                                                          |
| --------------------- | ---------------------------------------------------------------- |
| Continente brasileiro | ACC Recife, ACC Curitiba, ACC Amazônico                          |
| Norte e nordeste      | ACC Sal Oceânica, ACC Dacar e Dacar Oceânica, ACC Canárias       |
| Leste e sudeste       | ACC Accra, ACC Luanda, ACC Johannesburg Oceânica, ACC Cape Town  |
| Noroeste              | ACC Caiena                                                       |
| Sul e sudoeste        | ACC Montevidéu, ACC Ezeiza, ACC Comodoro Rivadávia               |

!!! tip "Na rede (Vatbrz)"
    Na prática, os únicos adjacentes conectados costumam ser `SBRE_CTR` e `SBCW_CTR`. O que fazer quando o próximo órgão está offline está em [Fluxo operacional](fluxo.pt.md#quando-o-proximo-orgao-nao-esta-online).

## Posições na VATSIM

| Posição          | Setores  | Logon                                               | Frequência VATSIM | HF de referência |
| :--------------: | :------: | :-------------------------------------------------: | :---------------: | :--------------: |
| **SBAO_FSS**     | 01 a 08  | :material-checkbox-marked-circle:{ .corok } `SBAO`  | 133.500 MHz       | 4669 kHz         |
| **SBAO_N_FSS**   | 01 a 07  | :material-checkbox-marked-circle:{ .corok } `SJAN`  | 133.025 MHz       | 13315 kHz        |
| **SBAO_S_FSS**   | 08       | :material-checkbox-marked-circle:{ .corok } `SJAS`  | 133.125 MHz       | 10096 kHz        |
| **SBAO_NW_FSS**  | 01 a 06  | :material-checkbox-marked-circle:{ .corok } `SJNW`  | 133.275 MHz       | 8861 kHz         |
| **SBAO_NE_FSS**  | 07       | :material-checkbox-marked-circle:{ .corok } `SJNE`  | 133.075 MHz       | 17955 kHz        |
| **SBAO_SW_FSS**  | 08 oeste | :material-checkbox-marked-circle:{ .corok } `SJSW`  | 133.450 MHz       | 8855 kHz         |
| **SBAO_SE_FSS**  | 08 leste | :material-checkbox-marked-circle:{ .corok } `SJSE`  | 133.325 MHz       | 5565 kHz         |

**Frequência VATSIM** é o canal de voz que se sintoniza na rede. Está na faixa VHF porque é o que a rede transporta, e não é frequência aeronáutica publicada. A **HF de referência** é a frequência real associada à posição, útil para contextualizar o piloto e preencher o *controller information*, nunca para sintonia. Apenas o logon `SBAO` é publicado em AIP[^9]; os demais códigos são convenção da divisão.

???+ warning "Atenção!"
    Em caso de divergência entre esta tabela e o pacote de setor instalado, prevalece o **pacote de setor**. Confira antes de conectar.

## Quando desmembrar

1. **Regra geral:** abra `SBAO_FSS`, que cobre a FIR inteira.
2. **Primeiro corte:** `SBAO_N_FSS` e `SBAO_S_FSS`, separando o corredor EUR/SAM da AORRA.
3. **Combinados:** apenas em evento ou demanda excepcional.
4. **Coordene ao abrir e ao fechar.** Quem chega assume espaço aéreo de quem já está online; quem sai devolve os tráfegos. A transferência é coordenada, nunca presumida.

A política de abertura de setores da VATSIM Brasil prevalece sobre esta orientação.

## Mapa Geral dos Combinados

!!! info "Como usar o mapa"
    Selecione a posição no canto superior direito para ver o limite lateral. Clique sobre a área para ver indicativo, frequência e logon.

<div id="mapa1" class="mapa"></div>

<style>
    .mapa { height: 680px; }
    .mapa-indisponivel { height: auto; padding: 1rem; border: 1px solid var(--md-default-fg-color--lightest); }
</style>

<script>
(function () {
  "use strict";

  var LEAFLET_CSS = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css";
  var LEAFLET_JS = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js";

  var cores = {
    ciano: "#2dd4bf",
    rosa: "#f472b6",
    verde: "#a3e635",
    amarelo: "#fbbf24",
    vermelho: "#f87171"
  };

  var configMapa = {
    zoomMin: 3,
    zoomMax: 14,
    zoomPadrao: 4,
    pontoCentral: [-15.382442, -30.714408],
    tileStadia: "https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.png",
    tileStadiaDark: "https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png",
    tileSatelite: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    tileOsm: "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
  };

  var atribuicaoStadia = '&copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>';

  // Os contornos estao em [longitude, latitude]; o Leaflet espera [latitude, longitude].
  var contornos = {
    sbao: [ [-51.6122, 4.4131], [-48, 5], [-40, 5], [-38.6544, 5.6908], [-37.3333, 6.4167], [-37.0767, 6.5883], [-35, 7.6667], [-34.1104, 7.0236], [-32.3326, 5.7295], [-31.6317, 5.2167], [-30.805, 4.6019], [-28.8, 3.1283], [-27.5094, 2.1675], [-24.1349, -0.3502], [-21.4245, -2.3693], [-19.308, -3.9386], [-17.4706, -5.2926], [-16, -6.3667], [-10, -6.3667], [-10, -12.000556], [-9.9994, -19.8819], [-10, -34], [-30, -34], [-42, -34], [-50.3972, -34], [-46.8336, -30.4004], [-45.396, -28.7836], [-43.75, -26.75], [-40.9592, -24.6653], [-40.273056, -24.130556], [-39.5692, -23.5814], [-38.8208, -22.9825], [-38.1472, -22.4338], [-39.0163, -21.5594], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189], [-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-47.0542, 1.2353], [-49.3301, 2.8265] ],
    sbao_n: [ [-51.6122,4.4131], [-48,5], [-40,5], [-38.6544,5.6908], [-37.3333,6.4167], [-37.0767,6.5883], [-35,7.6667], [-34.1104,7.0236], [-32.3326,5.7295], [-31.6317,5.2167], [-30.805,4.6019], [-28.8,3.1283], [-27.5094,2.1675], [-24.1349,-0.3502], [-21.4245,-2.3693], [-19.308,-3.9386], [-17.4706,-5.2926], [-16,-6.3667], [-10,-6.3667], [-10,-12.000556], [-9.9994,-19.8819], [-11.7341,-19.2015], [-13.4545,-18.5048], [-15.1608,-17.7924], [-16.8535,-17.0653], [-18.533,-16.3241], [-20.1998,-15.5696], [-21.8544,-14.8026], [-23.4973,-14.0236], [-25.1291,-13.2336], [-26.7503,-12.4332], [-28.0482,-11.4999], [-30.0907,-10.0145], [-31.1903,-9.4499], [-31.8644,-9.1011], [-30.1192,-6.5894], [-28.3914,-4.0714], [-29.2432,-3.6192], [-31.2094,-3.3882], [-32.1211,-3.2717], [-33.5089,-2.6381], [-34.8803,-2.0189], [-35.4608,-1.7439], [-36.2217,-1.3619], [-37.9531,-0.4917], [-39,0], [-39.9331,0.5036], [-40.7822,0.9303], [-41.7,-1.7569], [-41.8556,-2.1744], [-47.0542,1.2353], [-49.3301,2.8265] ],
    sbao_s: [ [-9.9994,-19.8819], [-10,-34], [-30,-34], [-42,-34], [-50.3972,-34], [-46.8336,-30.4004], [-45.396,-28.7836], [-43.75,-26.75], [-40.9592,-24.6653], [-40.273056,-24.130556], [-39.5692,-23.5814], [-38.8208,-22.9825], [-38.1472,-22.4338], [-39.0163,-21.5594], [-39.8122,-20.745], [-39.678,-20.598], [-39.6257,-20.5074], [-38.3444,-19.7896], [-37.6728,-18.8625], [-38.2428,-18.6793], [-37.6216,-17.4696], [-37.0281,-16.2961], [-35.8551,-14.6957], [-35.0828,-13.6253], [-34.4171,-12.7023], [-33.7561,-11.7775], [-32.9956,-10.7084], [-31.8644,-9.1011], [-31.1903,-9.4499], [-30.0907,-10.0145], [-28.0482,-11.4999], [-26.7503,-12.4332], [-25.1291,-13.2336], [-23.4973,-14.0236], [-21.8544,-14.8026], [-20.1998,-15.5696], [-18.533,-16.3241], [-16.8535,-17.0653], [-15.1608,-17.7924], [-13.4545,-18.5048], [-11.7341,-19.2015] ],
    sbao_nw: [ [-51.6122,4.4131], [-48,5], [-40,5], [-38.6544,5.6908], [-37.3333,6.4167], [-37.0767,6.5883], [-35,7.6667], [-34.1104,7.0236], [-32.3326,5.7295], [-31.6317,5.2167], [-30.805,4.6019], [-28.8,3.1283], [-27.5094,2.1675], [-24.1349,-0.3502], [-26.2339,-3.0872], [-28.3437,-5.8198], [-29.761,-7.6373], [-31.1903,-9.4499], [-31.8644,-9.1011], [-30.1192,-6.5894], [-28.3914,-4.0714], [-29.2432,-3.6192], [-31.2094,-3.3882], [-32.1211,-3.2717], [-33.5089,-2.6381], [-34.8803,-2.0189], [-35.4608,-1.7439], [-36.2217,-1.3619], [-37.9531,-0.4917], [-39,0], [-39.9331,0.5036], [-40.7822,0.9303], [-41.7,-1.7569], [-41.8556,-2.1744], [-47.0542,1.2353], [-49.3301,2.8265] ],
    sbao_ne: [ [-24.1349,-0.3502], [-21.4245,-2.3693], [-19.308,-3.9386], [-17.4706,-5.2926], [-16,-6.3667], [-10,-6.3667], [-10,-12.000556], [-9.9994,-19.8819], [-11.7341,-19.2015], [-13.4545,-18.5048], [-15.1608,-17.7924], [-16.8535,-17.0653], [-18.533,-16.3241], [-20.1998,-15.5696], [-21.8544,-14.8026], [-23.4973,-14.0236], [-25.1291,-13.2336], [-26.7503,-12.4332], [-28.0482,-11.4999], [-30.0907,-10.0145], [-31.1903,-9.4499], [-29.761,-7.6373], [-28.3437,-5.8198], [-26.2339,-3.0872] ],
    sbao_sw: [ [-30,-34], [-42,-34], [-50.3972,-34], [-46.8336,-30.4004], [-45.396,-28.7836], [-43.75,-26.75], [-40.9592,-24.6653], [-40.273056,-24.130556], [-39.5692,-23.5814], [-38.8208,-22.9825], [-38.1472,-22.4338], [-39.0163,-21.5594], [-39.8122,-20.745], [-39.678,-20.598], [-39.6257,-20.5074], [-38.3444,-19.7896], [-37.6728,-18.8625], [-38.2428,-18.6793], [-37.6216,-17.4696], [-37.0281,-16.2961], [-35.8551,-14.6957], [-35.0828,-13.6253], [-34.4171,-12.7023], [-33.7561,-11.7775], [-32.9956,-10.7084], [-31.8644,-9.1011], [-31.1903,-9.4499], [-30.0907,-10.0145], [-28.0482,-11.4999], [-26.7503,-12.4332], [-25.1291,-13.2336], [-30,-16] ],
    sbao_se: [ [-30,-34], [-30,-16], [-25.1291,-13.2336], [-23.4973,-14.0236], [-21.8544,-14.8026], [-20.1998,-15.5696], [-18.533,-16.3241], [-16.8535,-17.0653], [-15.1608,-17.7924], [-13.4545,-18.5048], [-11.7341,-19.2015], [-9.9994,-19.8819], [-10,-34] ]
  };

  var posicoes = [
    { chave: "sbao", indicativo: "SBAO_FSS", cor: cores.vermelho, freq: "133.500 MHz (HF 4669 kHz)", logon: "SBAO" },
    { chave: "sbao_n", indicativo: "SBAO_N_FSS", cor: cores.ciano, freq: "133.025 MHz (HF 13315 kHz)", logon: "SJAN" },
    { chave: "sbao_s", indicativo: "SBAO_S_FSS", cor: cores.amarelo, freq: "133.125 MHz (HF 10096 kHz)", logon: "SJAS" },
    { chave: "sbao_nw", indicativo: "SBAO_NW_FSS", cor: cores.verde, freq: "133.275 MHz (HF 8861 kHz)", logon: "SJNW" },
    { chave: "sbao_ne", indicativo: "SBAO_NE_FSS", cor: cores.rosa, freq: "133.075 MHz (HF 17955 kHz)", logon: "SJNE" },
    { chave: "sbao_sw", indicativo: "SBAO_SW_FSS", cor: cores.amarelo, freq: "133.450 MHz (HF 8855 kHz)", logon: "SJSW" },
    { chave: "sbao_se", indicativo: "SBAO_SE_FSS", cor: cores.verde, freq: "133.325 MHz (HF 5565 kHz)", logon: "SJSE" }
  ];

  function paraLatLng(par) {
    return [par[1], par[0]];
  }

  function carregarEstilo() {
    if (document.querySelector("link[data-leaflet-css]")) return;
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = LEAFLET_CSS;
    link.setAttribute("data-leaflet-css", "");
    document.head.appendChild(link);
  }

  // Carrega o Leaflet uma unica vez e guarda a promessa, para que a navegacao
  // instantanea do tema nao dispare uma segunda carga nem execute o desenho
  // antes de a biblioteca estar disponivel.
  function carregarBiblioteca() {
    if (window.L && window.L.map) return Promise.resolve();
    if (!window.__leafletPromessa) {
      window.__leafletPromessa = new Promise(function (resolve, reject) {
        var script = document.createElement("script");
        script.src = LEAFLET_JS;
        script.onload = resolve;
        script.onerror = function () { reject(new Error("Leaflet indisponivel")); };
        document.head.appendChild(script);
      });
    }
    return window.__leafletPromessa;
  }

  function desenhar() {
    var elemento = document.getElementById("mapa1");
    if (!elemento || elemento._leaflet_id) return;

    var camadas = {};
    posicoes.forEach(function (posicao) {
      var poligono = L.polygon(contornos[posicao.chave].map(paraLatLng), {
        color: posicao.cor,
        weight: 3
      });
      poligono.bindPopup(
        "<b>" + posicao.indicativo + "</b><br><i>" + posicao.freq +
        "</i><br><b>Logon:</b> " + posicao.logon
      );
      camadas[posicao.chave] = poligono;
    });

    var bases = {
      "Stadia": L.tileLayer(configMapa.tileStadia, { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax, attribution: atribuicaoStadia }),
      "Stadia Dark": L.tileLayer(configMapa.tileStadiaDark, { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax, attribution: atribuicaoStadia }),
      "Arcgis Satelite": L.tileLayer(configMapa.tileSatelite, { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax, attribution: "&copy; Esri" }),
      "Open Street Map": L.tileLayer(configMapa.tileOsm, { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax, attribution: "&copy; OpenStreetMap" })
    };

    var sobreposicoes = {
      "SBAO_FSS": L.layerGroup([camadas.sbao]),
      "SBAO_N_FSS": L.layerGroup([camadas.sbao_n]),
      "SBAO_S_FSS": L.layerGroup([camadas.sbao_s]),
      "Combinados": L.layerGroup([camadas.sbao_nw, camadas.sbao_ne, camadas.sbao_sw, camadas.sbao_se])
    };

    var mapa = L.map(elemento, {
      minZoom: configMapa.zoomMin,
      maxZoom: configMapa.zoomMax,
      layers: [bases["Stadia"]]
    }).setView(configMapa.pontoCentral, configMapa.zoomPadrao);

    L.control.layers(bases, sobreposicoes).addTo(mapa);
    setTimeout(function () { mapa.invalidateSize(); }, 200);
  }

  function avisarFalha() {
    var elemento = document.getElementById("mapa1");
    if (!elemento) return;
    elemento.classList.add("mapa-indisponivel");
    elemento.textContent = "Nao foi possivel carregar o mapa. Verifique a conexao e recarregue a pagina. Os limites de cada posicao estao descritos nas tabelas acima.";
  }

  function iniciar() {
    if (!document.getElementById("mapa1")) return;
    carregarEstilo();
    carregarBiblioteca().then(desenhar).catch(avisarFalha);
  }

  iniciar();
})();
</script>

[^1]: **AIP-Brasil, ENR 2.1**.
[^2]: **AIP-Brasil, GEN 3.3, item 2, NOTA 1**.
[^3]: **AIP-Brasil, ENR 1.4, itens 1 e 2**.
[^4]: **AIP-Brasil, ENR 3.5, item 6**.
[^5]: **AIP-Brasil, ENR 2.2, item 1, e ENR 3.5, item 7**.
[^6]: **AIP-Brasil, ENR 3.5, item 8**.
[^7]: **CIRCEA 100-66, Art. 3°**.
[^8]: **AIP-Brasil, ENR 3.5, item 7.8.1**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.2.1**.
