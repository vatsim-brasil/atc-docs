---
title: SBXS - Salvador
tags:
  - Terminal
  - SBRE
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Salvador |
| **Posição** | `SBXS_APP` |
| **Indicativo** | Controle Salvador |
| **Frequência** | **119.350** MHz[^pacote] |
| **Vigilância ATS** | Radar |
| **Aeródromos na TMA** | [SBSV](../../aerodromos/sbre-recife/twr/SBSV.pt.md) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Use as abas acima: **Cartas Aeronáuticas** traz as cartas da TMA, **Carta Visual** traz a carta visual da AISWEB, **Meteorologia** mostra o mapa meteorológico da área e **Tráfego VATSIM** abre o tráfego no aeródromo principal (SBSV).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBXS?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Carta Visual"
    [:material-open-in-new: Abrir em nova aba](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xs-salvador_rea_20241128.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xs-salvador_rea_20241128.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Fonte: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xs-salvador_rea_20241128.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Meteorologia"
    <div class="tma-meteo" data-lat="-12.869" data-lon="-38.379" data-zoom="8" data-lang="pt"></div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBSV){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

A camada **Corredores visuais (REA)** mostra as 7 REA da AIC N 06/22 e os portões (em amarelo). Linha cheia magenta: classe D, dentro da CTR; tracejada azul: classe G, fora dela; as setas marcam os trechos de mão única. Clique em um trecho para ver os rumos, as altitudes e a classe. Detalhes em [Corredores visuais (REA)](#corredores-visuais-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| TMA Salvador | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Salvador | GND – 3500 FT | <span class="classe-badge classe-c">C</span> |

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBXS_APP** | `XS` | Controle Salvador | **119.350** |  |
| **SBSV_TWR** | `TSV` | Torre Salvador | **118.300** |  |

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
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBRE_NS_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBRE_SW_CTR</span>"]:::grpctr
        p1["SBRE_S_CTR"]:::ctr
        p2["SBXS_APP"]:::app
        p3["SBSV_TWR"]:::twr
        a0(["TMA Salvador"]):::esp --> p2
        a1(["CTR Salvador"]):::esp --> p3
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
    - **Circular:** [AIC N 06/22 – Circulação de Aeronaves em Voo VFR na Terminal Salvador](https://publicacoes.decea.mil.br/publicacao/aic-n-0622){ target="_blank" } (em vigor desde 24 MAR 2022, substitui a AIC N 24/21)
    - **Carta visual – Rotas de aeronaves (REA):** [CCV REA XS-Salvador](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-xs-salvador_rea_20241128.pdf){ target="_blank" } (28 NOV 2024)

    A carta está embutida na aba **Carta Visual** em **Informações Úteis**. Os dados desta seção vêm da AIC N 06/22[^aic0622].

### Camadas da TMA e quem atende o VFR

| Espaço | Limites | Classe | VFR |
| --- | --- | :---: | --- |
| **TMA Salvador** | 3500 FT – FL195 | <span class="classe-badge classe-c">C</span> até FL145, <span class="classe-badge classe-a">A</span> acima | Com autorização do APP; acima do FL145, classe A, não há VFR |
| **CTR Salvador** | GND – 3500 FT, círculo de 21 NM | <span class="classe-badge classe-c">C</span> | Pelas REA; entrada e saída pelos portões |
| **REA dentro da CTR** | 1200 a 3000 FT | <span class="classe-badge classe-d">D</span> | Contato bilateral com o APP ou a Torre |
| **REA fora da CTR**, sob a TMA | 1200 a 1500 FT | <span class="classe-badge classe-g">G</span> | Coordenação ar-ar na FCA |

- **REA obrigatórias:** toda aeronave VFR na Área Metropolitana de Salvador ou na TMA, indo para os aeródromos de Salvador ou vindo deles, usa **compulsoriamente** as REA, salvo autorização diferente do APP ou emergência. Com o tráfego e o tempo permitindo, o APP ou a Torre podem autorizar o voo fora delas.
- **Fora da CTR**, sob a TMA, as rotas são **recomendadas**, não obrigatórias, e podem ser acessadas ou abandonadas em qualquer ponto.
- **No mundo real**, o VFR fala com o APP Salvador e, perto de SBSV, com a Torre Salvador.
- **No pacote**, o VFR chama `SBXS_APP` (**119.350**); para o circuito de SBSV, `SBSV_TWR` (**118.300**). O piloto chama a posição **on-line**, não a frequência do mundo real. Sem ela, quem assume é a próxima posição na [cobertura](#cobertura-top-down). A coordenação ar-ar fica na **UNICOM 122.800**.

### Regras gerais para o VFR

- **Transponder** modo A/C ou S obrigatório nas REA e na TMA/CTR; faróis de pouso ou táxi acesos, recomendados.
- **Direita do eixo:** o piloto voa à **direita** do eixo do corredor.
- **Largura:** REA com 3 NM (1,5 NM para cada lado); portões com 1 NM.
- **Altitudes:** nas áreas controladas, a máxima e a mínima devem ser obedecidas; a mínima dá 500 pés de margem sobre o relevo. As mudanças de altitude são feitas nos fixos de posição, sob responsabilidade do piloto e em VMC: na BONFIM em FAROL DA BARRA (sentidos norte e oeste/noroeste) e no TRAVÉS DE PARIPE (sentido sul), na FRADE em ITAPARICA e na INTERLAGOS em INTERLAGOS. O APP pode dar outra altitude nos trechos controlados.
- **QNH** dado pelo APP ou pela Torre Salvador.
- **Plano de voo:** as REA a usar vão no item 18 (observações). Quem vai para SBSV informa a REA no primeiro contato com o APP, mesmo que já conste do plano.
- **Cruzando a TMA:** pelos trechos das REA até sair dela ou, excepcionalmente, em rota direta autorizada pelo APP.
- **Esperas:** para espaçar a entrada na TMA e na CTR, o APP pode mandar esperar sobre os pontos das REA.
- **Helicópteros** podem usar as REA e, com o APP, pousar em outro local da CTR, informando a REA até o destino.
- **IMC:** voltar e pousar no aeródromo de partida ou no mais próximo, pedir VFR especial ou mudar para IFR.

### Corredores visuais (REA)

As 7 REA da TMA. Altitudes em pés (QNH), no formato **máxima / mínima**; uma só altitude vale para as duas. **⇄** é trecho de mão dupla, com rumo no formato ida / volta; **→** é de mão única.

| REA | Trecho | Rumos | Altitudes | Classe · contato |
| :---: | :--- | :---: | :---: | :--- |
| **AXEH** | FAROL DE ITAPUÃ → AMARALINA | 265° | 1200 | D · APP Salvador |
|  | AMARALINA → FAROL DA BARRA | 299° | 1200 | D · APP Salvador |
| **BONFIM** | CANDEIAS ⇄ TRAVÉS DE PARIPE | 197° / 017° | 3000 / 1200 | D · APP Salvador |
|  | FAROL DA BARRA → TRAVÉS DE PARIPE | 029° | 1200 | D · APP Salvador |
| **CAIXA PREGOS** | CAIXA PREGOS ⇄ SNCL | 228° / 048° | 1500 / 1200 | G · FCA |
| **FORTE** | PRAIA DO FORTE ⇄ INTERLAGOS | 241° / 061° | 1500 / 1200 | G fora da CTR, D dentro |
| **FRADE** | SALINAS DA MARGARIDA ⇄ ITAPARICA | 121° / 301° | 1500 / 1200 | G · FCA |
|  | ITAPARICA ⇄ FAROL DA BARRA | 155° / 335° | 1200 | D · APP Salvador |
| **VERA CRUZ** | CAIXA PREGOS ⇄ TRAVÉS DE SNVR | 084° / 264° | 1500 / 1200 | G · FCA |
|  | TRAVÉS DE SNVR ⇄ FAROL DA BARRA | 092° / 272° | 1500 / 1200 | D · APP Salvador |
| **INTERLAGOS** | INTERLAGOS ⇄ CEASA | 282° / 102° | 1200 | D · APP Salvador |
|  | TRAVÉS DE PARIPE → CEASA | 110° | 1200 | D · APP Salvador |

O que cada corredor faz:

- **AXEH** é a saída de SBSV pela orla: mão única, do portão FAROL DE ITAPUÃ por AMARALINA até o FAROL DA BARRA, a 1200 pés, **sobre o mar**, sem passar da faixa de areia.
- **BONFIM** liga os aeródromos ao norte da TMA: de CANDEIAS (Base Naval de Aratu) ao TRAVÉS DE PARIPE, de mão dupla, até 3000 pés; do FAROL DA BARRA ao TRAVÉS DE PARIPE, só para o norte, a 1200 pés, pela Igreja do Bonfim.
- **INTERLAGOS** leva a SBSV: do TRAVÉS DE PARIPE (mão única) e de INTERLAGOS até o portão CEASA, de onde o piloto toma a proa de SBSV com autorização da Torre.
- **FORTE** vem do litoral norte: do portão PRAIA DO FORTE por Arembepe até INTERLAGOS.
- **FRADE** atravessa a Baía de Todos os Santos: de SALINAS DA MARGARIDA pelo portão ITAPARICA (ponta norte da ilha) até o FAROL DA BARRA.
- **VERA CRUZ** vem do sudoeste: de CAIXA PREGOS pelo portão TRAVÉS DE SNVR até o FAROL DA BARRA.
- **CAIXA PREGOS** liga CAIXA PREGOS ao portão SNCL (Morro de São Paulo), a sudoeste.

### Portões

| Portão | Uso |
| :---: | :--- |
| **FAROL DE ITAPUÃ** | Entrada na REA AXEH das aeronaves que saem de SBSV |
| **CEASA** | Entrada no circuito de SBSV, vindo da BONFIM e da INTERLAGOS; sem autorização, espera visual no portão |
| **ITAPARICA** · **TRAVÉS DE SNVR** (Vera Cruz) · **PRAIA DO FORTE** | Entrada e saída da CTR Salvador, com autorização do APP |
| CANDEIAS · SALINAS DA MARGARIDA · SNCL | Portões nas pontas das REA, marcados na carta |

### Outras regras

- Quem decola de aeródromo sem órgão ATS sob a TMA apresenta plano de voo à sala AIS, chama o APP antes do táxi e informa a hora real de decolagem.
- Proibido apresentar plano de voo por radiotelefonia, exceto helidecks em emergência.
- Quem vai decolar de aeródromo ou heliponto dentro da CTR chama antes, na FCA ou no APP, para receber instruções de cruzamento ou ingresso nas REA.
- Com plano Z, aguardar a autorização do APP para mudar as regras de voo, respeitando as altitudes do corredor.

### Fraseologia

No contato, o piloto informa matrícula, rota ou corredor, posição, altitude e sentido[^aic0622]:

```
Controle Salvador, PT-THE, corredor CAIXA PREGOS, vertical de CAIXA PREGOS, 1000 pés, proa FAROL DA BARRA.
```

```
Controle Salvador, PT-THE, corredor INTERLAGOS, través de PARIPE, 1200 pés, proa CEASA, pouso em Salvador.
```

## :material-note-text-outline: Observações

- A TMA é classe A entre FL145 e FL195 e classe C entre 3500 FT e FL145.
- A CTR Salvador é um círculo de 21 NM, do GND a 3500 FT.
- Volumes e mapa seguem a AIP, AMDT AIRAC 2612A1 (26 NOV 2026).

---

Voltar para a [visão geral das terminais](index.pt.md) da FIR Recife.

[^pacote]: Frequência no pacote de setores da VATSIM Brasil.
[^aic0622]: [AIC N 06/22](https://publicacoes.decea.mil.br/publicacao/aic-n-0622){ target="_blank" }, itens 2 a 5 e Anexo A.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude]; a CTR Salvador é um círculo de 21 NM.
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
    {"tipo": "tma", "id": "SBXS", "nome": "TMA Salvador", "posicao": "SBXS_APP", "freq": "119.350", "lim": "3500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-37.4625, -12.085278], [-37.921389, -11.7975], [-39.203333, -12.0], [-39.258611, -12.156111], [-39.286944, -12.961944], [-39.295833, -13.211389], [-38.931389, -13.757778], [-38.416389, -13.941389], [-38.0775, -13.348056], [-37.841111, -13.005], [-37.812778, -12.963611]]},
    {"tipo": "ctr", "id": "SBXS", "nome": "CTR Salvador", "posicao": "SBSV_TWR", "freq": "118.300", "lim": "GND – 3500 FT", "classe": "C", "link": "", "contorno": [[-37.957605, -12.9], [-37.958971, -12.869495], [-37.96306, -12.839223], [-37.969839, -12.809413], [-37.979259, -12.780293], [-37.991246, -12.752084], [-38.00571, -12.725], [-38.02254, -12.699248], [-38.041609, -12.675024], [-38.062772, -12.652513], [-38.085866, -12.631884], [-38.110717, -12.613297], [-38.137136, -12.596891], [-38.164921, -12.582792], [-38.19386, -12.571108], [-38.223735, -12.561926], [-38.254316, -12.555317], [-38.285373, -12.551332], [-38.316667, -12.55], [-38.347961, -12.551332], [-38.379018, -12.555317], [-38.409599, -12.561926], [-38.439474, -12.571108], [-38.468413, -12.582792], [-38.496198, -12.596891], [-38.522617, -12.613297], [-38.547468, -12.631884], [-38.570562, -12.652513], [-38.591725, -12.675024], [-38.610794, -12.699248], [-38.627624, -12.725], [-38.642088, -12.752084], [-38.654075, -12.780293], [-38.663495, -12.809413], [-38.670274, -12.839223], [-38.674363, -12.869495], [-38.675729, -12.9], [-38.674363, -12.930505], [-38.670274, -12.960777], [-38.663495, -12.990587], [-38.654075, -13.019707], [-38.642088, -13.047916], [-38.627624, -13.075], [-38.610794, -13.100752], [-38.591725, -13.124976], [-38.570562, -13.147487], [-38.547468, -13.168116], [-38.522617, -13.186703], [-38.496198, -13.203109], [-38.468413, -13.217208], [-38.439474, -13.228892], [-38.409599, -13.238074], [-38.379018, -13.244683], [-38.347961, -13.248668], [-38.316667, -13.25], [-38.285373, -13.248668], [-38.254316, -13.244683], [-38.223735, -13.238074], [-38.19386, -13.228892], [-38.164921, -13.217208], [-38.137136, -13.203109], [-38.110717, -13.186703], [-38.085866, -13.168116], [-38.062772, -13.147487], [-38.041609, -13.124976], [-38.02254, -13.100752], [-38.00571, -13.075], [-37.991246, -13.047916], [-37.979259, -13.019707], [-37.969839, -12.990587], [-37.96306, -12.960777], [-37.958971, -12.930505]]}
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

// Corredores visuais (REA) e portões da AIC N 06/22 (Anexo A); pontos da carta CCV REA XS
const reaTrechos = [{"rota": "AXEH", "de": "FAROL DE ITAPUÃ", "para": "AMARALINA", "rumo": "265°", "rumoVolta": null, "max": "1200", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}, {"rota": "AXEH", "de": "AMARALINA", "para": "FAROL DA BARRA", "rumo": "299°", "rumoVolta": null, "max": "1200", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}, {"rota": "BONFIM", "de": "CANDEIAS", "para": "TRAVÉS DE PARIPE", "rumo": "197°", "rumoVolta": "017°", "max": "3000", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}, {"rota": "BONFIM", "de": "FAROL DA BARRA", "para": "TRAVÉS DE PARIPE", "rumo": "029°", "rumoVolta": null, "max": "1200", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}, {"rota": "CAIXA PREGOS", "de": "CAIXA PREGOS", "para": "SNCL", "rumo": "228°", "rumoVolta": "048°", "max": "1500", "min": "1200", "classe": "G", "esp": "G · FCA"}, {"rota": "FORTE", "de": "PRAIA DO FORTE", "para": "INTERLAGOS", "rumo": "241°", "rumoVolta": "061°", "max": "1500", "min": "1200", "classe": "D/G", "esp": "G fora da CTR, D dentro"}, {"rota": "FRADE", "de": "SALINAS DA MARGARIDA", "para": "ITAPARICA", "rumo": "121°", "rumoVolta": "301°", "max": "1500", "min": "1200", "classe": "G", "esp": "G · FCA"}, {"rota": "FRADE", "de": "ITAPARICA", "para": "FAROL DA BARRA", "rumo": "155°", "rumoVolta": "335°", "max": "1200", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}, {"rota": "VERA CRUZ", "de": "CAIXA PREGOS", "para": "TRAVÉS DE SNVR", "rumo": "084°", "rumoVolta": "264°", "max": "1500", "min": "1200", "classe": "G", "esp": "G · FCA"}, {"rota": "VERA CRUZ", "de": "TRAVÉS DE SNVR", "para": "FAROL DA BARRA", "rumo": "092°", "rumoVolta": "272°", "max": "1500", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}, {"rota": "INTERLAGOS", "de": "INTERLAGOS", "para": "CEASA", "rumo": "282°", "rumoVolta": "102°", "max": "1200", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}, {"rota": "INTERLAGOS", "de": "TRAVÉS DE PARIPE", "para": "CEASA", "rumo": "110°", "rumoVolta": null, "max": "1200", "min": "1200", "classe": "D", "esp": "D · APP Salvador"}];
const reaPontos = {"CANDEIAS": [-38.536333, -12.6725], "CEASA": [-38.369167, -12.838833], "FAROL DE ITAPUÃ": [-38.353833, -12.957167], "PRAIA DO FORTE": [-38.002833, -12.583333], "SALINAS DA MARGARIDA": [-38.7645, -12.871667], "SNCL": [-38.9105, -13.39], "AMARALINA": [-38.467, -13.016667], "CAIXA PREGOS": [-38.788833, -13.1305], "FAROL DA BARRA": [-38.532833, -13.010333], "INTERLAGOS": [-38.208333, -12.808333], "ITAPARICA": [-38.681667, -12.882167], "TRAVÉS DE PARIPE": [-38.5155, -12.846667], "TRAVÉS DE SNVR": [-38.658833, -13.0595]};
const portoes = {"FAROL DE ITAPUÃ": "SBSV", "CEASA": "SBSV", "ITAPARICA": "CTR", "TRAVÉS DE SNVR": "CTR", "PRAIA DO FORTE": "CTR", "CANDEIAS": "", "SALINAS DA MARGARIDA": "", "SNCL": ""};
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
        '<div><span class="rea-linha"></span>REA classe D</div>' +
        '<div><span class="rea-linha g"></span>REA classe G</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Portão</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
