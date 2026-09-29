---
title: Structure and Sectorization
icon: material/layers-triple
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

This page gathers the data that changes over time. No other page in the manual repeats these values.

## Boundaries and classification

The Atlântico ACC operates H24, in Portuguese and English, with callsigns **CENTRO ATLÂNTICO** and **ATLANTICO CENTER**[^1]. Its responsibility extends east to the **010° W** meridian, by regional agreement[^2]. To the south, the FIR reaches the **34° S** parallel[^1].

| Airspace       | Limits         | Published classification                  |
| -------------- | -------------- | ----------------------------------------- |
| Atlântico FIR  | GND to UNL     | `A` above FL 245, `G` below FL 145        |
| Atlântico UIR  | FL 245 to UNL  | `A` above FL 245                          |

Two remarks that matter in practice:

- The upper airspace is a **UIR**, not a UTA as in the continental FIRs[^1]. The class is `A` in both cases.
- Between FL 145 and FL 245 there is no specific published classification for this FIR. The general rule applies: airways above FL 145 are Class `A`[^3].

## Sectors and published HF frequencies

The AIP divides the FIR into **eight sectors**, `SECT 01` to `SECT 08`, all GND/UNL and all belonging to the Atlântico ACC[^1].

| AIP sectors           | Published HF frequencies (kHz)        |
| --------------------- | ------------------------------------- |
| `SECT 01` to `SECT 04` | 3452, 4669, 6649, 8861, 13357        |
| `SECT 05` to `SECT 08` | 4669, 5565, 8855, 10096, 13315, 17955 |

**4669 kHz** is the only frequency published for all eight sectors, and is therefore the reference for the position covering the whole FIR.

## EUR/SAM Corridor and AORRA

Two volumes overlap the FIR and carry almost all of its traffic. Both lie between **FL 290 and FL 410**.

| | EUR/SAM Corridor | AORRA |
| --- | --- | --- |
| **Traffic** | Brazil and Europe or North Africa | Brazil and Southern Africa |
| **Structure** | Fixed ATS routes | Random routes between gates |
| **Requirement** | RNP 10 and RVSM[^4] [^5] | RNP 10[^6] |
| **Routes or gates** | UN741, UN866, UN873, UN857, and the extensions via `DAKAP` (UZ51) and `BUGAT` (UL206)[^7] | `SORSA`, `CIDER`, `MIGEX`, `VURTO`, `EKALO`, `EDVEL`, `MUKEK`, `OBKOL`, `GELAM`, `VURIL`, `GARUP`[^6] |
| **Compulsory reporting** | The route's reporting points | 010° E, 000°, 010° W, 020° W, 030° W, 040° W and 050° W[^6] |

When entering the FIR bound for the AORRA via the `ARUSI` or `UKEDI` fixes on a track through Brazilian waypoints, **ADS-C and CPDLC capability is mandatory**[^6].

## Cruising levels { #niveis-de-cruzeiro }

| Magnetic track | RVSM (general)[^5]                          | AORRA[^6]              | RVSM suspended[^5]     |
| :------------: | :-----------------------------------------: | :--------------------: | :--------------------: |
| 000° to 179°   | 290, 310, 330, 350, 370, 390, 410           | 290, 350, 410          | 290, 350, 410          |
| 180° to 359°   | 300, 320, 340, 360, 380, 400                | 320, 380               | 320, 380               |

RVSM is suspended when there are pilot reports of severe turbulence[^8].

## Adjacent units

| Direction             | Units                                                            |
| --------------------- | ---------------------------------------------------------------- |
| Brazilian mainland    | Recife ACC, Curitiba ACC, Amazônico ACC                          |
| North and northeast   | Sal Oceanic ACC, Dakar and Dakar Oceanic ACC, Canarias ACC       |
| East and southeast    | Accra ACC, Luanda ACC, Johannesburg Oceanic ACC, Cape Town ACC   |
| Northwest             | Cayenne ACC                                                      |
| South and southwest   | Montevideo ACC, Ezeiza ACC, Comodoro Rivadavia ACC               |

!!! tip "On the network (Vatbrz)"
    In practice, the only connected adjacent units are usually `SBRE_CTR` and `SBCW_CTR`. What to do when the next unit is offline is covered in [Operational flow](fluxo.en.md#quando-o-proximo-orgao-nao-esta-online).

## Positions on VATSIM { #posicoes-na-vatsim }

| Position         | Sectors  | Logon                                               | VATSIM frequency  | Reference HF     |
| :--------------: | :------: | :-------------------------------------------------: | :---------------: | :--------------: |
| **SBAO_FSS**     | 01 to 08 | :material-checkbox-marked-circle:{ .corok } `SBAO`  | 133.500 MHz       | 4669 kHz         |
| **SBAO_N_FSS**   | 01 to 07 | :material-checkbox-marked-circle:{ .corok } `SJAN`  | 133.025 MHz       | 13315 kHz        |
| **SBAO_S_FSS**   | 08       | :material-checkbox-marked-circle:{ .corok } `SJAS`  | 133.125 MHz       | 10096 kHz        |
| **SBAO_NW_FSS**  | 01 to 06 | :material-checkbox-marked-circle:{ .corok } `SJNW`  | 133.275 MHz       | 8861 kHz         |
| **SBAO_NE_FSS**  | 07       | :material-checkbox-marked-circle:{ .corok } `SJNE`  | 133.075 MHz       | 17955 kHz        |
| **SBAO_SW_FSS**  | 08 west  | :material-checkbox-marked-circle:{ .corok } `SJSW`  | 133.450 MHz       | 8855 kHz         |
| **SBAO_SE_FSS**  | 08 east  | :material-checkbox-marked-circle:{ .corok } `SJSE`  | 133.325 MHz       | 5565 kHz         |

**VATSIM frequency** is the voice channel you tune on the network. It is in the VHF band because that is what the network carries, and it is not a published aeronautical frequency. The **reference HF** is the real-world frequency associated with the position, useful to give the pilot context and to fill in the *controller information*, never for tuning. Only the `SBAO` logon is published in the AIP[^9]; the other codes are a division convention.

???+ warning "Attention!"
    If this table differs from the installed sector package, the **sector package** prevails. Check before connecting.

## When to split

1. **General rule:** open `SBAO_FSS`, which covers the whole FIR.
2. **First split:** `SBAO_N_FSS` and `SBAO_S_FSS`, separating the EUR/SAM corridor from the AORRA.
3. **Combined sectors:** only for events or exceptional demand.
4. **Coordinate when opening and closing.** Whoever arrives takes over airspace from whoever is already online; whoever leaves hands the traffic back. The transfer is coordinated, never assumed.

The VATSIM Brasil sector opening policy takes precedence over this guidance.

## Combined Sectors Overview Map

!!! info "How to use the map"
    Select the position in the top right corner to see its lateral boundary. Click on the area to see callsign, frequency and logon.

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
    tileSatelite: "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    tileOsm: "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
  };

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
      "Light": camadaMapbox("claro", { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax }),
      "Dark": camadaMapbox("escuro", { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax }),
      "Arcgis Satellite": L.tileLayer(configMapa.tileSatelite, { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax, attribution: "&copy; Esri" }),
      "Open Street Map": L.tileLayer(configMapa.tileOsm, { minZoom: configMapa.zoomMin, maxZoom: configMapa.zoomMax, attribution: "&copy; OpenStreetMap" })
    };

    var sobreposicoes = {
      "SBAO_FSS": L.layerGroup([camadas.sbao]),
      "SBAO_N_FSS": L.layerGroup([camadas.sbao_n]),
      "SBAO_S_FSS": L.layerGroup([camadas.sbao_s]),
      "Combined": L.layerGroup([camadas.sbao_nw, camadas.sbao_ne, camadas.sbao_sw, camadas.sbao_se])
    };

    var mapa = L.map(elemento, {
      minZoom: configMapa.zoomMin,
      maxZoom: configMapa.zoomMax,
      layers: [bases["Light"]]
    }).setView(configMapa.pontoCentral, configMapa.zoomPadrao);

    L.control.layers(bases, sobreposicoes).addTo(mapa);
    setTimeout(function () { mapa.invalidateSize(); }, 200);
  }

  function avisarFalha() {
    var elemento = document.getElementById("mapa1");
    if (!elemento) return;
    elemento.classList.add("mapa-indisponivel");
    elemento.textContent = "The map could not be loaded. Check your connection and reload the page. The boundaries of each position are described in the tables above.";
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
[^2]: **AIP-Brasil, GEN 3.3, item 2, NOTE 1**.
[^3]: **AIP-Brasil, ENR 1.4, items 1 and 2**.
[^4]: **AIP-Brasil, ENR 3.5, item 6**.
[^5]: **AIP-Brasil, ENR 2.2, item 1, and ENR 3.5, item 7**.
[^6]: **AIP-Brasil, ENR 3.5, item 8**.
[^7]: **CIRCEA 100-66, Art. 3°**.
[^8]: **AIP-Brasil, ENR 3.5, item 7.8.1**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.2.1**.
