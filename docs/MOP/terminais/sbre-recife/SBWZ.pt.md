---
title: SBWZ - Fortaleza
tags:
  - Terminal
  - SBRE
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Fortaleza |
| **Posição** | `SBWZ_APP` |
| **Indicativo** | Controle Fortaleza |
| **Frequência** | **133.000** MHz[^pacote] |
| **Vigilância ATS** | Radar |
| **Aeródromos na TMA** | [SBFZ](../../aerodromos/sbre-recife/twr/SBFZ.pt.md) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Use as abas acima: **Cartas Aeronáuticas** traz as cartas da TMA, **Carta Visual** traz a carta visual da AISWEB, **Meteorologia** mostra o mapa meteorológico da área e **Tráfego VATSIM** abre o tráfego no aeródromo principal (SBFZ).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWZ?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Carta Visual"
    [:material-open-in-new: Abrir em nova aba](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wz-fortaleza_rea_20251127.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wz-fortaleza_rea_20251127.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Fonte: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wz-fortaleza_rea_20251127.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Meteorologia"
    <div class="tma-meteo" data-lat="-3.745" data-lon="-38.560" data-zoom="8" data-lang="pt"></div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBFZ){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

A camada **Corredores visuais (REA)** mostra as 8 REA da AIC N 49/25 e os portões (em amarelo). Linha cheia magenta: classe C ou D, com o APP; tracejada azul: classe G. Clique em um trecho para ver os rumos, as altitudes e o contato. Detalhes em [Corredores visuais (REA)](#corredores-visuais-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| TMA Fortaleza | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Fortaleza | GND – 3500 FT | <span class="classe-badge classe-c">C</span> |

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBWZ_APP** | `WZ` | Controle Fortaleza | **133.000** |  |
| **SBFZ_TWR** | `TFZ` | Torre Fortaleza | **129.000** |  |

## :material-arrow-down-bold-box-outline: Cobertura top-down

Leia de baixo para cima: com a posição desconectada, o espaço aéreo passa para a próxima posição on-line acima.

??? info "Ver diagrama de cobertura"
    ```mermaid
    ---
    config:
      flowchart:
        wrappingWidth: 1000
    ---
    flowchart BT
        p0["SBRE_CTR"]:::ctr
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBRE_NS_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBRE_NW_CTR</span>"]:::grpctr
        p1["SBRE_N_CTR"]:::ctr
        p2["SBWZ_APP"]:::app
        p3["SBFZ_TWR"]:::twr
        a0(["TMA Fortaleza"]):::esp --> p2
        a1(["CTR Fortaleza"]):::esp --> p3
        g0 --> p0
        p1 --> g0
        p2 --> p1
        p3 --> p2
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
        classDef grpctr fill:none,stroke:#8a56c9,stroke-dasharray:4 3
    ```

## :material-airplane: Circulação VFR

!!! abstract "Documentos de navegação visual"
    - **Circular:** [AIC N 49/25 – Circulação de Aeronaves em Voo VFR na Terminal Fortaleza](https://publicacoes.decea.mil.br/publicacao/aic-n-4925){ target="_blank" } (em vigor desde 27 NOV 2025, substitui a AIC N 16/20)
    - **Carta visual – Rotas de aeronaves (REA):** [CCV REA WZ-Fortaleza](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wz-fortaleza_rea_20251127.pdf){ target="_blank" } (27 NOV 2025)

    A carta está embutida na aba **Carta Visual** em **Informações Úteis**. Os dados desta seção vêm da AIC N 49/25[^aic4925].

### Camadas da TMA e quem atende o VFR

| Espaço | Limites | Classe | VFR |
| --- | --- | :---: | --- |
| **TMA Fortaleza** | 3500 FT – FL195 | <span class="classe-badge classe-c">C</span> até FL145, <span class="classe-badge classe-a">A</span> acima | Com autorização do APP; acima do FL145, classe A, não há VFR |
| **CTR Fortaleza** | GND – 3500 FT | <span class="classe-badge classe-c">C</span> | Pelas REA; entrada e saída pelos portões |
| **REA** | 1000 a 3500 FT | <span class="classe-badge classe-c">C</span>, <span class="classe-badge classe-d">D</span> ou <span class="classe-badge classe-g">G</span> | A classe é a do corredor |

- **REA obrigatórias:** toda aeronave VFR na TMA que vai para os aeródromos de Fortaleza ou vem deles usa **compulsoriamente** as REA, salvo autorização do APP ou emergência. Com o tráfego e o tempo permitindo, o APP ou a Torre podem autorizar o voo fora delas.
- **Classe dos corredores:** BARRA e PICI (a oeste e noroeste de SBFZ) são **classe C**; CANINDÉ, FEIJÓ e HORIZONTE (sudoeste e sul) são **classe D**, todas com o APP; BEACH PARK, CATULEVE e CAPONGA (sudeste e litoral) são **classe G**, com coordenação na FCA **123.450** e uso só recomendado.
- **No mundo real**, o APP Fortaleza atende o VFR em **133.000**, **134.550** ou **120.500**.
- **No pacote**, o VFR chama `SBWZ_APP` (**133.000**); para o circuito de SBFZ, `SBFZ_TWR` (**129.000**). O piloto chama a posição **on-line**, não a frequência do mundo real. Sem ela, quem assume é a próxima posição na [cobertura](#cobertura-top-down). A coordenação ar-ar fica na **UNICOM 122.800**.

### Regras gerais para o VFR

- **Transponder** modo A/C ou S obrigatório; faróis de pouso ou táxi acesos, recomendados.
- **Direita do eixo:** o piloto voa à **direita** do eixo do corredor.
- **Largura:** 3 NM (1,5 NM para cada lado), inclusive nos portões.
- **Altitudes:** nas áreas controladas, a máxima e a mínima devem ser obedecidas; a mínima dá ao menos 500 pés sobre o relevo. As mudanças de altitude são feitas dentro dos limites do trecho, entre o ponto anterior e o seguinte, sob responsabilidade do piloto e em VMC. O APP pode dar outra altitude nos trechos controlados.
- **QNH** do APP, da Torre ou do ATIS de SBFZ.
- **Plano de voo:** a REA vai no item 18. Quem vai para SBFZ informa a REA no primeiro contato com o APP, mesmo que já conste do plano.
- **Cruzando a TMA:** pelos trechos das REA até sair da CTR ou, excepcionalmente, em rota direta autorizada pelo APP.
- **Esperas:** o APP pode mandar esperar sobre os pontos das REA para espaçar a entrada na TMA e na CTR.
- **Helicópteros** podem usar as REA e, com o APP, pousar em outro local da CTR, informando as REA até o destino.
- **IMC:** voltar e pousar no aeródromo de partida ou no mais próximo, pedir VFR especial, mudar para IFR ou pedir para sair da REA.

### Corredores visuais (REA)

As 8 REA da TMA, todas de mão dupla. Altitudes em pés (QNH), no formato **máxima / mínima**; uma só altitude vale para as duas. O rumo vale para o sentido de ida / volta.

| REA | Trecho | Rumos | Altitudes | Classe · contato |
| :---: | :--- | :---: | :---: | :--- |
| **BARRA** | BARRA ⇄ CUMBUCO | 317° / 137° | 1000 | C · APP Fortaleza 133.000 |
|  | CUMBUCO ⇄ PECÉM | 335° / 155° | 3500 / 1600 | C · APP Fortaleza 133.000 |
| **PICI** | CUMBUCO ⇄ TREVO VIÁRIO | 178° / 358° | 1000 | C · APP Fortaleza 133.000 |
| **CANINDÉ** | BOISA ⇄ TREVO VIÁRIO | 070° / 250° | 3500 / 1000 | D · APP Fortaleza 133.000 |
| **FEIJÓ** | TREVO VIÁRIO ⇄ FÁBRICA FORTALEZA | 152° / 332° | 1000 | D · APP Fortaleza 133.000 |
| **HORIZONTE** | ESTÁDIO DOMINGÃO ⇄ FÁBRICA FORTALEZA | 021° / 201° | 3500 / 1000 | D · APP Fortaleza 133.000 |
| **BEACH PARK** | FÁBRICA FORTALEZA ⇄ BEACH PARK | 073° / 253° | 1000 | G · FCA 123.450 |
| **CATULEVE** | FÁBRICA FORTALEZA ⇄ IGUAPE | 118° / 298° | 2000 / 1000 | G · FCA 123.450 |
| **CAPONGA** | BEACH PARK ⇄ IGUAPE | 154° / 334° | 1500 / 1000 | G · FCA 123.450 |
|  | IGUAPE ⇄ CAPONGA | 161° / 341° | 2000 / 1000 | G · FCA 123.450 |

O que cada corredor faz:

- **BARRA** é a chegada e a saída de SBFZ pelo noroeste: do portão PECÉM (porto do Pecém) por CUMBUCO até o portão BARRA (ponte da Barra do Ceará), **sobre o mar**, na linha do litoral. No portão BARRA, o piloto chama a Torre para entrar no circuito. Para seguir na PICI, desce para estar a **1000 pés em CUMBUCO**.
- **PICI** liga CUMBUCO ao TREVO VIÁRIO (Quarto Anel Viário com a CE-060), a 1000 pés. Para entrar nela vindo da BARRA, ou nela seguir vindo da CANINDÉ ou da FEIJÓ, o piloto pede ao APP o **cruzamento do eixo de aproximação da RWY 13**.
- **CANINDÉ** vem do portão BOISA (Fazenda Boisa), a sudoeste, até o TREVO VIÁRIO, onde o piloto chega a 1000 pés.
- **FEIJÓ** liga o TREVO VIÁRIO à FÁBRICA FORTALEZA (aeródromo M. Dias Branco, SJDS), a 1000 pés.
- **HORIZONTE** vem do portão ESTÁDIO DOMINGÃO, ao sul, até a FÁBRICA FORTALEZA; ali o piloto está a no máximo 2000 pés se seguir na CATULEVE, ou a 1000 pés se seguir na BEACH PARK ou na FEIJÓ.
- **BEACH PARK** liga a FÁBRICA FORTALEZA ao portão BEACH PARK, a 1000 pés. **CATULEVE** liga a FÁBRICA FORTALEZA a IGUAPE, servindo aos aeródromos M. Dias Branco e Catuleve.
- **CAPONGA** é o litoral sudeste: do portão BEACH PARK por IGUAPE até o portão CAPONGA. Quem vai para o BEACH PARK chega a ele a 1000 pés.
- **Cruzando o prolongamento da RWY 13:** nas REA BEACH PARK e CAPONGA, o piloto fica sobre o mar no portão BEACH PARK e aguarda a autorização do APP.

### Portões

Os portões são a entrada e a saída da CTR Fortaleza, salvo outra autorização do APP:

| Portão | REA |
| :---: | :--- |
| **BARRA** · **PECÉM** | BARRA (noroeste) |
| **BOISA** | CANINDÉ (sudoeste) |
| **ESTÁDIO DOMINGÃO** | HORIZONTE (sul) |
| **BEACH PARK** · **CAPONGA** | BEACH PARK, CAPONGA e CATULEVE (sudeste) |

### Outras regras

- Quem decola de aeródromo sem órgão ATS sob a TMA apresenta plano de voo à sala AIS, chama o APP antes do táxi e informa a hora real de decolagem.
- Quem vai decolar de aeródromo ou heliponto dentro da CTR chama antes, na FCA ou no APP, para receber instruções.
- Com plano Z, aguardar a autorização do APP para mudar as regras de voo, respeitando as altitudes do corredor.
- Em datas de muito movimento, a classe de qualquer REA pode passar de G para C por NOTAM.

### Fraseologia

No contato, o piloto informa matrícula, REA, posição, altitude e sentido[^aic4925]:

```
Controle Fortaleza, PR-GHF, REA CAPONGA, vertical da Prainha, 1000 pés, proa BEACH PARK.
```

```
Controle Fortaleza, PR-GHF, REA BARRA, posição CUMBUCO, 1000 pés, solicita REA PICI.
```

## :material-note-text-outline: Observações

- A TMA é classe A entre FL145 e FL195 e classe C entre 3500 FT e FL145.
- Volumes e mapa seguem a AIP, AMDT AIRAC 2612A1 (26 NOV 2026): a CTR vai até 3500 FT AMSL.

---

Voltar para a [visão geral das terminais](index.pt.md) da FIR Recife.

[^pacote]: Frequência no pacote de setores da VATSIM Brasil.
[^aic4925]: [AIC N 49/25](https://publicacoes.decea.mil.br/publicacao/aic-n-4925){ target="_blank" }, itens 3 e 4 e Anexo A.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude].
-->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>

<style>
    .mapa { height: 550px }
    .rea-rotulo { background: #0f172a; color: #fff; border: 0; font-weight: 700; font-size: 11px; padding: 0 5px; box-shadow: none }
    .rea-rotulo::before { display: none }
    .rea-zoom-baixo .rea-rotulo, .rea-zoom-medio .rea-rotulo-trecho { display: none }
    .rea-seta span { display: block; width: 16px; height: 16px; line-height: 16px; text-align: center; color: #0284c7; font-size: 15px; text-shadow: 0 0 2px #fff, 0 0 2px #fff }
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
    .mapa-legenda .rea-linha.g { border-top: 3px dashed #0284c7 }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWZ", "nome": "TMA Fortaleza", "posicao": "SBWZ_APP", "freq": "133.000", "lim": "3500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-38.300833, -4.531667], [-38.767778, -4.526667], [-39.245833, -4.396667], [-39.595833, -3.837222], [-39.469444, -3.276667], [-39.043056, -2.967222], [-38.242222, -2.958611], [-37.822778, -3.203056], [-37.575833, -3.536111], [-37.524167, -4.006389], [-37.804167, -4.302778], [-37.968056, -4.474444]]},
    {"tipo": "ctr", "id": "SBWZ", "nome": "CTR Fortaleza", "posicao": "SBFZ_TWR", "freq": "129.000", "lim": "GND – 3500 FT", "classe": "C", "link": "", "contorno": [[-38.851667, -3.379722], [-39.000556, -3.937222], [-38.221667, -4.146389], [-38.073889, -3.587778]]}
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
        v.lim + ' · Classe ' + v.classe 
    );
    poligono.on('mouseover', function () { this.setStyle({ weight: 4 }); });
    poligono.on('mouseout', function () { this.setStyle({ weight: ctr ? 2 : 2.5 }); });
    poligono.addTo(ctr ? grupoCtr : grupoTma);
});

// Corredores visuais (REA) e portões da AIC N 49/25 (Anexo A); pontos da carta CCV REA WZ
const reaTrechos = [{"rota": "BARRA", "de": "BARRA", "para": "CUMBUCO", "rumo": "317°", "rumoVolta": "137°", "max": "1000", "min": "1000", "classe": "C", "esp": "C · APP Fortaleza 133.000"}, {"rota": "BARRA", "de": "CUMBUCO", "para": "PECÉM", "rumo": "335°", "rumoVolta": "155°", "max": "3500", "min": "1600", "classe": "C", "esp": "C · APP Fortaleza 133.000"}, {"rota": "PICI", "de": "CUMBUCO", "para": "TREVO VIÁRIO", "rumo": "178°", "rumoVolta": "358°", "max": "1000", "min": "1000", "classe": "C", "esp": "C · APP Fortaleza 133.000"}, {"rota": "CANINDÉ", "de": "BOISA", "para": "TREVO VIÁRIO", "rumo": "070°", "rumoVolta": "250°", "max": "3500", "min": "1000", "classe": "D", "esp": "D · APP Fortaleza 133.000"}, {"rota": "FEIJÓ", "de": "TREVO VIÁRIO", "para": "FÁBRICA FORTALEZA", "rumo": "152°", "rumoVolta": "332°", "max": "1000", "min": "1000", "classe": "D", "esp": "D · APP Fortaleza 133.000"}, {"rota": "HORIZONTE", "de": "ESTÁDIO DOMINGÃO", "para": "FÁBRICA FORTALEZA", "rumo": "021°", "rumoVolta": "201°", "max": "3500", "min": "1000", "classe": "D", "esp": "D · APP Fortaleza 133.000"}, {"rota": "BEACH PARK", "de": "FÁBRICA FORTALEZA", "para": "BEACH PARK", "rumo": "073°", "rumoVolta": "253°", "max": "1000", "min": "1000", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "CATULEVE", "de": "FÁBRICA FORTALEZA", "para": "IGUAPE", "rumo": "118°", "rumoVolta": "298°", "max": "2000", "min": "1000", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "CAPONGA", "de": "BEACH PARK", "para": "IGUAPE", "rumo": "154°", "rumoVolta": "334°", "max": "1500", "min": "1000", "classe": "G", "esp": "G · FCA 123.450"}, {"rota": "CAPONGA", "de": "IGUAPE", "para": "CAPONGA", "rumo": "161°", "rumoVolta": "341°", "max": "2000", "min": "1000", "classe": "G", "esp": "G · FCA 123.450"}];
const reaPontos = {"BARRA": [-38.585667, -3.689167], "BEACH PARK": [-38.385667, -3.840333], "BOISA": [-38.887, -3.9675], "CAPONGA": [-38.189, -4.039], "CUMBUCO": [-38.7205, -3.622333], "ESTÁDIO DOMINGÃO": [-38.485833, -4.102833], "FÁBRICA FORTALEZA": [-38.486667, -3.9195], "IGUAPE": [-38.274333, -3.943833], "PECÉM": [-38.807, -3.538], "TREVO VIÁRIO": [-38.659167, -3.767333]};
const portoes = {"BARRA": "SBFZ", "BEACH PARK": "SBFZ", "BOISA": "SBFZ", "CAPONGA": "SBFZ", "ESTÁDIO DOMINGÃO": "SBFZ", "PECÉM": "SBFZ"};
var corD = '#c026d3', corG = '#0284c7';
var grupoRea = L.featureGroup();
reaTrechos.forEach(function (t) {
    var a = paraLatLng(reaPontos[t.de]), b = paraLatLng(reaPontos[t.para]);
    var g = t.classe === 'G', duplo = !!t.rumoVolta;
    L.polyline([a, b], { color: g ? corG : corD, weight: 4, opacity: 0.9, dashArray: g ? '8 6' : null })
        .bindPopup('<b>REA ' + t.rota + '</b><br>' + t.de + (duplo ? ' ⇄ ' : ' → ') + t.para + '<br>Rumos: ' + t.rumo + (duplo ? ' / ' + t.rumoVolta : '') +
            '<br>Máx. / mín. (ft): ' + t.max + (t.max === t.min ? '' : ' / ' + t.min) + '<br>' + t.esp + (duplo ? '' : '<br>Mão única'))
        .addTo(grupoRea);
    if (!duplo) {
        // seta no sentido do voo, a um terço do trecho (o meio fica para o rótulo)
        var ang = Math.atan2(-(b[0] - a[0]), (b[1] - a[1]) * Math.cos(a[0] * Math.PI / 180)) * 180 / Math.PI;
        L.marker([a[0] + (b[0] - a[0]) / 3, a[1] + (b[1] - a[1]) / 3], { interactive: false, icon: L.divIcon({ className: 'rea-seta', iconSize: [16, 16],
            html: '<span style="transform:rotate(' + ang.toFixed(0) + 'deg)">➤</span>' }) })
            .addTo(grupoRea);
    }
    // Um rótulo por corredor no trecho do meio; os demais trechos só com zoom maior
    var trechosRea = reaTrechos.filter(function (x) { return x.rota === t.rota; });
    var principal = trechosRea[Math.floor((trechosRea.length - 1) / 2)] === t;
    L.marker([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2], { opacity: 0, interactive: false, icon: L.divIcon({ className: '', iconSize: [0, 0] }) })
        .bindTooltip(t.rota, { permanent: true, direction: 'center', className: principal ? 'rea-rotulo' : 'rea-rotulo rea-rotulo-trecho' })
        .addTo(grupoRea);
});
Object.keys(reaPontos).forEach(function (n) {
    var portao = n in portoes;
    L.circleMarker(paraLatLng(reaPontos[n]), portao ?
        { radius: 5, color: '#0f172a', weight: 2, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 3.5, color: '#334155', weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Portão ' + n + (portoes[n] ? ' (' + portoes[n] + ')' : '') : n).addTo(grupoRea);
});

var mapa = L.map('mapa-tma', {
    minZoom: 3,
    maxZoom: 13,
    layers: [tileMapaClaro, grupoFir, grupoTma, grupoCtr, grupoRea]
});

mapa.fitBounds(grupoTma.getBounds().extend(grupoCtr.getBounds()), { padding: [20, 20] });

L.control.layers({
    "Claro": tileMapaClaro,
    "Escuro": tileMapaEscuro,
    "Arcgis Satélite": tileMapaSatelite
}, {
    "TMAs": grupoTma,
    "CTRs": grupoCtr,
    "Limite da FIR": grupoFir,
    "Corredores visuais (REA)": grupoRea
}).addTo(mapa);

// Rótulos dos corredores só com zoom suficiente para não embolar
function detalheRea() {
    elemento.classList.toggle('rea-zoom-baixo', mapa.getZoom() < 8);
    elemento.classList.toggle('rea-zoom-medio', mapa.getZoom() < 10);
}
mapa.on('zoomend', detalheRea);
detalheRea();

// Legenda das classes
var legenda = L.control({ position: 'bottomleft' });
legenda.onAdd = function () {
    var div = L.DomUtil.create('div', 'mapa-legenda');
    div.innerHTML = '<b>Classe</b>' + ['A', 'C', 'D'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('') +
        '<div><span class="rea-linha"></span>REA classe C ou D</div>' +
        '<div><span class="rea-linha g"></span>REA classe G</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Portão</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
