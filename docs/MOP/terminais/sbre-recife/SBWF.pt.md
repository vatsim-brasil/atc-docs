---
title: SBWF - Recife
tags:
  - Terminal
  - SBRE
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Recife |
| **Posição** | `SBWF_APP` |
| **Indicativo** | Controle Recife |
| **Frequência** | **120.400** MHz[^pacote] |
| **Vigilância ATS** | Radar |
| **Aeródromos na TMA** | [SBRF](../../aerodromos/sbre-recife/twr/SBRF.pt.md), [SBJP](../../aerodromos/sbre-recife/twr/SBJP.pt.md) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Use as abas acima: **Cartas Aeronáuticas** traz as cartas da TMA, **Carta Visual** traz a carta visual da AISWEB, **Meteorologia** mostra o mapa meteorológico da área e **Tráfego VATSIM** abre o tráfego no aeródromo principal (SBRF).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWF?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Carta Visual"
    [:material-open-in-new: Abrir em nova aba](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Fonte: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Meteorologia"
    <div class="tma-meteo" data-lat="-7.990" data-lon="-34.975" data-zoom="8" data-lang="pt"></div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBRF){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

A camada **Corredores visuais (REA)** mostra as 5 REA da AIC N 06/25 e os portões (em amarelo). Linha cheia magenta: classe C, com o APP; tracejada azul: classe G. Clique em um trecho para ver os rumos, as altitudes e o contato. Detalhes em [Corredores visuais (REA)](#corredores-visuais-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| TMA Recife | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Recife | GND – 3500 FT | <span class="classe-badge classe-c">C</span> |
| CTR João Pessoa | GND – 3500 FT | <span class="classe-badge classe-d">D</span> |

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBWF_APP** | `WF` | Controle Recife | **120.400** |  |
| **SBRF_TWR** | `TRF` | Torre Recife | **118.350** |  |
| **SBJP_TWR** | `TJP` | Torre João Pessoa | **118.300** |  |

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
        p2["SBWF_APP"]:::app
        p3["SBRF_TWR"]:::twr
        p4["SBJP_TWR"]:::twr
        a0(["TMA Recife"]):::esp --> p2
        a1(["CTR Recife"]):::esp --> p3
        a2(["CTR João Pessoa"]):::esp --> p4
        g0 --> p0
        p1 --> g0
        p2 --> p1
        p3 --> p2
        p4 --> p2
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
        classDef grpctr fill:none,stroke:#8a56c9,stroke-dasharray:4 3
    ```

## :material-airplane: Circulação VFR

!!! abstract "Documentos de navegação visual"
    - **Circular:** [AIC N 06/25 – Circulação de Aeronaves em Voo VFR na Terminal Recife](https://publicacoes.decea.mil.br/publicacao/aic-n-0625){ target="_blank" } (em vigor desde 20 MAR 2025, substitui a AIC N 13/21)
    - **Carta visual – Rotas de aeronaves (REA):** [CCV REA WF-Recife](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wf-recife_rea_20250320.pdf){ target="_blank" } (20 MAR 2025)

    A carta está embutida na aba **Carta Visual** em **Informações Úteis**. Os dados desta seção vêm da AIC N 06/25[^aic0625].

### Camadas da TMA e quem atende o VFR

| Espaço | Limites | Classe | VFR |
| --- | --- | :---: | --- |
| **TMA Recife** | 3500 FT – FL195 | <span class="classe-badge classe-c">C</span> até FL145, <span class="classe-badge classe-a">A</span> acima | Com autorização do APP; acima do FL145, classe A, não há VFR |
| **CTR Recife** | GND – 3500 FT | <span class="classe-badge classe-c">C</span> | Só pelas REA e pelos portões, salvo autorização do APP |
| **CTR João Pessoa** | GND – 3500 FT | <span class="classe-badge classe-d">D</span> | Com a Torre Pessoa |
| **Projeção da TMA** | Abaixo da TMA, fora das CTR | <span class="classe-badge classe-g">G</span> | FCA livre 123.450 |

- **REA obrigatórias:** na CTR Recife e no litoral norte, entre Caaporã (PB) e Itapissuma (PE), o VFR usa **obrigatoriamente** as REA e os portões, nos rumos e altitudes publicados, salvo instrução do APP.
- **Classe dos corredores:** todos são **classe C**, com o APP, exceto o início da ALFA, de TABU a CERVEJARIA, em **classe G** na FCA livre 123.450.
- **No mundo real**, o VFR fala com o APP Recife em **129.600**, **129.200**, **120.400** ou **128.950**.
- **No pacote**, o VFR chama `SBWF_APP` (**120.400**); para o circuito de SBRF, `SBRF_TWR` (**118.350**). O piloto chama a posição **on-line**, não a frequência do mundo real. Sem ela, quem assume é a próxima posição na [cobertura](#cobertura-top-down). A coordenação ar-ar fica na **UNICOM 122.800**.

### Regras gerais para o VFR

- **Transponder** modo A/C ou S, **rádio VHF** e **faróis** de pouso ou táxi acesos são obrigatórios na TMA e sob ela. A exceção ao transponder vale só nas rotas especiais para aeronaves sem transponder (REAST) da CTR Recife.
- **Direita do eixo:** avião e helicóptero voam à **direita** do eixo do corredor e fazem a própria separação; se não for possível, avisam o APP.
- **Largura:** REA com 3 NM (1,5 NM para cada lado); portões com 1 NM (0,5 NM para cada lado).
- **Altitudes:** a máxima deve ser obedecida (é a separação do IFR acima); a mínima é a altitude livre de obstáculos do trecho. Recomenda-se manter a máxima, por causa do ruído.
- **Velocidade** máxima de **200 kt** nas áreas controladas.
- **QNH** do ATIS de SBRF (**127.650**).
- **Helicópteros** podem usar as REA.
- **Plano Z:** quem decola de aeródromo na TMA com mudança de VFR para IFR aguarda a autorização do APP, respeitando as altitudes do corredor.
- Em datas de muito movimento, a classe de qualquer parte do espaço aéreo, inclusive das REA, pode passar de G para C por NOTAM.

### Corredores visuais (REA)

As 5 REA da TMA, todas de mão dupla. Altitudes em pés (QNH), no formato **máxima / mínima**; uma só altitude é a máxima obrigatória. O rumo vale para o sentido de ida / volta.

| REA | Trecho | Rumos | Altitudes | Classe · contato |
| :---: | :--- | :---: | :---: | :--- |
| **ALFA** | TABU ⇄ TEJUCUPAPO | 215° / 035° | 1600 / 1000 | G · FCA livre 123.450 |
|  | TEJUCUPAPO ⇄ CERVEJARIA | 210° / 030° | 1600 | G · FCA livre 123.450 |
|  | CERVEJARIA ⇄ FORTE ORANGE | 146° / 326° | 1600 | C · APP Recife |
|  | FORTE ORANGE ⇄ CASA CAIADA | 200° / 020° | 1600 | C · APP Recife |
|  | CASA CAIADA ⇄ CAIS DE SANTA RITA | 224° / 044° | 1200 | C · APP Recife |
| **BRAVO** | ACADEMIA DA POLÍCIA MILITAR ⇄ MORENO PARK AQUÁTICO | 198° / 018° | 1500 | C · APP Recife |
|  | MORENO PARK AQUÁTICO ⇄ BARRAGEM | 179° / 359° | 1600 | C · APP Recife |
|  | BARRAGEM ⇄ MURO ALTO | 173° / 353° | 1600 | C · APP Recife |
|  | MURO ALTO ⇄ PORTO DE GALINHAS | 217° / 037° | 1600 / 1000 | C · APP Recife |
| **CHARLIE** | ACADEMIA DA POLÍCIA MILITAR ⇄ ARAÇOIABA | 047° / 227° | 1500 / 1400 | C · APP Recife |
|  | ARAÇOIABA ⇄ CERVEJARIA | 100° / 280° | 1500 / 1300 | C · APP Recife |
| **DELTA** | PEDREIRA ⇄ MORENO PARK AQUÁTICO | 109° / 289° | 2100 | C · APP Recife |
|  | MORENO PARK AQUÁTICO ⇄ LAGOA AZUL | 126° / 306° | 1600 | C · APP Recife |
| **ECHO** | BARRAGEM ⇄ LAGOA AZUL | 053° / 233° | 1200 | C · APP Recife |

O que cada corredor faz:

- **ALFA** é a chegada do litoral norte: do portão TABU por TEJUCUPAPO até CERVEJARIA (Itapissuma), em classe G, e dali, já com o APP, por FORTE ORANGE (Itamaracá) e CASA CAIADA (Olinda) até o portão CAIS DE SANTA RITA, a entrada de SBRF pelo norte. Perto dela ficam as áreas SBR-221, SBR-222, SBR-246, SBR-278 e a proibida SBP-227 (Ilha Coroa do Avião).
- **BRAVO** é o eixo norte-sul a oeste da cidade: da ACADEMIA DA POLÍCIA MILITAR por MORENO PARK AQUÁTICO e BARRAGEM (Pirapama) até MURO ALTO e o portão PORTO DE GALINHAS. Atenção às áreas proibidas SBP-209 (Porto de Suape) e SBP-268 (Refinaria Abreu e Lima), do GND a 1500 pés.
- **CHARLIE** liga a ACADEMIA DA POLÍCIA MILITAR ao portão ARAÇOIABA e a CERVEJARIA, onde encontra a ALFA. Fica **indisponível** com a área SBR-220 (Aldeia, GND ao FL100) ativa.
- **DELTA** vem do portão PEDREIRA (Itamatamirim) por MORENO PARK AQUÁTICO até LAGOA AZUL, a entrada de SBRF pelo sul.
- **ECHO** liga BARRAGEM a LAGOA AZUL, a 1200 pés.

### Chegadas, saídas e cruzamentos de SBRF

| Portão | Uso |
| :---: | :--- |
| **CAIS DE SANTA RITA** | Entrada e saída de SBRF pela ALFA (norte) |
| **LAGOA AZUL** | Entrada e saída de SBRF pela DELTA e pela ECHO (sul e oeste) |
| ARAÇOIABA · PEDREIRA · PORTO DE GALINHAS · TABU | Portões nas pontas das REA |

- A entrada no circuito das RWY 18 e 36 de SBRF, ou o cruzamento do aeródromo, é pela posição CAIS DE SANTA RITA (ALFA) ou LAGOA AZUL (DELTA e ECHO), com autorização da Torre Recife.
- Nas REA ALFA, DELTA e ECHO, o cruzamento do setor de decolagem e aproximação das RWY 18/36 depende de autorização **expressa** do APP, que coordena com a Torre. Sem ela, a aeronave fica no seu setor, nos portões CAIS DE SANTA RITA ou LAGOA AZUL.
- Quem vem do setor norte para SBRF, fora dos treinamentos em Coroa do Avião (SIFC), usa a ALFA e aguarda autorização no portão CAIS DE SANTA RITA.
- **Cruzando a TMA de norte a sul** (ou de sul a norte), de preferência CHARLIE e BRAVO, com a SBR-220 desativada. ALFA e ECHO ficam sujeitas a esperas nos horários de muito movimento de SBRF.
- Do sudoeste ou do oeste para o setor norte: CHARLIE (com a SBR-220 desativada), ou DELTA, BRAVO e CHARLIE saindo pelo portão ARAÇOIABA. Com a SBR-220 ativa, use ALFA, DELTA ou ECHO, aguardando nos portões o cruzamento do campo com a Torre.
- Quem vai decolar de aeródromo ou área de pouso dentro da CTR Recife chama o APP antes de acionar, para receber instruções.
- **VFR especial** em SBRF pode ser autorizado pelo APP; o limite da autorização é a borda da TMA.

### Outras regras

- Não são aceitos planos AFIL.
- SBJP: proibida a operação de aeronaves sem rádio; contato compulsório com a Torre Pessoa antes do táxi.

### Fraseologia

No contato, o piloto informa matrícula, rota, posição ou portão, altitude e sentido[^aic0625]:

```
Controle Recife, PP-IUR, corredor ECHO, posição Barragem, 1200 pés, proa de Lagoa Azul.
```

```
Controle Recife, PT-IUR, corredor CHARLIE, portão Araçoiaba, 1500 pés, proa de Cervejaria.
```

Na classe G, na FCA livre (UNICOM na VATSIM):

```
Coordenação, PT-IUR, corredor ALFA, portão Tabu, 1600 pés, proa de Tejucupapo.
```

## :material-note-text-outline: Observações

- A TMA é classe A entre FL145 e FL195 e classe C entre 3500 FT e FL145.
- Volumes e mapa seguem a AIP, AMDT AIRAC 2612A1 (26 NOV 2026): as CTR vão até 3500 FT AMSL.
- Não existe TMA João Pessoa: SBJP fica dentro da TMA Recife. No mundo real, a Torre Pessoa presta também o serviço de aproximação dentro da CTR João Pessoa.

---

Voltar para a [visão geral das terminais](index.pt.md) da FIR Recife.

[^pacote]: Frequência no pacote de setores da VATSIM Brasil.
[^aic0625]: [AIC N 06/25](https://publicacoes.decea.mil.br/publicacao/aic-n-0625){ target="_blank" }, itens 3 e 4 e Anexo A.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude]; a CTR João Pessoa é um círculo de 15 NM.
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
    {"tipo": "tma", "id": "SBWF", "nome": "TMA Recife", "posicao": "SBWF_APP", "freq": "120.400", "lim": "3500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-34.240278, -8.348056], [-34.289444, -7.086111], [-34.774722, -6.844722], [-35.43, -6.940278], [-35.5175, -7.502778], [-35.709167, -7.841667], [-35.707778, -8.18], [-35.706111, -8.609444], [-35.588056, -8.685278], [-35.134167, -8.976944], [-34.885833, -9.136111]]},
    {"tipo": "ctr", "id": "SBWF", "nome": "CTR Recife", "posicao": "SBRF_TWR", "freq": "118.350", "lim": "GND – 3500 FT", "classe": "C", "link": "", "contorno": [[-35.245278, -7.811111], [-34.858056, -7.682222], [-34.616667, -8.394722], [-35.014167, -8.528333]]},
    {"tipo": "ctr", "id": "SBWF", "nome": "CTR João Pessoa", "posicao": "SBJP_TWR", "freq": "118.300", "lim": "GND – 3500 FT", "classe": "D", "link": "", "contorno": [[-34.700824, -7.140556], [-34.701783, -7.118767], [-34.704652, -7.097144], [-34.709409, -7.075851], [-34.716019, -7.055051], [-34.72443, -7.034901], [-34.734579, -7.015556], [-34.746389, -6.997162], [-34.75977, -6.979859], [-34.77462, -6.963779], [-34.790825, -6.949045], [-34.808263, -6.935768], [-34.826801, -6.92405], [-34.846298, -6.913979], [-34.866605, -6.905633], [-34.887567, -6.899075], [-34.909027, -6.894354], [-34.930819, -6.891507], [-34.952778, -6.890556], [-34.974737, -6.891507], [-34.996529, -6.894354], [-35.017989, -6.899075], [-35.038951, -6.905633], [-35.059258, -6.913979], [-35.078755, -6.92405], [-35.097293, -6.935768], [-35.114731, -6.949045], [-35.130936, -6.963779], [-35.145786, -6.979859], [-35.159167, -6.997162], [-35.170977, -7.015556], [-35.181126, -7.034901], [-35.189537, -7.055051], [-35.196147, -7.075851], [-35.200904, -7.097144], [-35.203773, -7.118767], [-35.204732, -7.140556], [-35.203773, -7.162345], [-35.200904, -7.183968], [-35.196147, -7.205261], [-35.189537, -7.226061], [-35.181126, -7.246211], [-35.170977, -7.265556], [-35.159167, -7.28395], [-35.145786, -7.301253], [-35.130936, -7.317333], [-35.114731, -7.332067], [-35.097293, -7.345344], [-35.078755, -7.357062], [-35.059258, -7.367133], [-35.038951, -7.375479], [-35.017989, -7.382037], [-34.996529, -7.386758], [-34.974737, -7.389605], [-34.952778, -7.390556], [-34.930819, -7.389605], [-34.909027, -7.386758], [-34.887567, -7.382037], [-34.866605, -7.375479], [-34.846298, -7.367133], [-34.826801, -7.357062], [-34.808263, -7.345344], [-34.790825, -7.332067], [-34.77462, -7.317333], [-34.75977, -7.301253], [-34.746389, -7.28395], [-34.734579, -7.265556], [-34.72443, -7.246211], [-34.716019, -7.226061], [-34.709409, -7.205261], [-34.704652, -7.183968], [-34.701783, -7.162345]]}
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

// Corredores visuais (REA) e portões da AIC N 06/25 (Anexo A); pontos da carta CCV REA WF
const reaTrechos = [{"rota": "ALFA", "de": "TABU", "para": "TEJUCUPAPO", "rumo": "215°", "rumoVolta": "035°", "max": "1600", "min": "1000", "classe": "G", "esp": "G · FCA livre 123.450"}, {"rota": "ALFA", "de": "TEJUCUPAPO", "para": "CERVEJARIA", "rumo": "210°", "rumoVolta": "030°", "max": "1600", "min": "1600", "classe": "G", "esp": "G · FCA livre 123.450"}, {"rota": "ALFA", "de": "CERVEJARIA", "para": "FORTE ORANGE", "rumo": "146°", "rumoVolta": "326°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "ALFA", "de": "FORTE ORANGE", "para": "CASA CAIADA", "rumo": "200°", "rumoVolta": "020°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "ALFA", "de": "CASA CAIADA", "para": "CAIS DE SANTA RITA", "rumo": "224°", "rumoVolta": "044°", "max": "1200", "min": "1200", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "ACADEMIA DA POLÍCIA MILITAR", "para": "MORENO PARK AQUÁTICO", "rumo": "198°", "rumoVolta": "018°", "max": "1500", "min": "1500", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "MORENO PARK AQUÁTICO", "para": "BARRAGEM", "rumo": "179°", "rumoVolta": "359°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "BARRAGEM", "para": "MURO ALTO", "rumo": "173°", "rumoVolta": "353°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "BRAVO", "de": "MURO ALTO", "para": "PORTO DE GALINHAS", "rumo": "217°", "rumoVolta": "037°", "max": "1600", "min": "1000", "classe": "C", "esp": "C · APP Recife"}, {"rota": "CHARLIE", "de": "ACADEMIA DA POLÍCIA MILITAR", "para": "ARAÇOIABA", "rumo": "047°", "rumoVolta": "227°", "max": "1500", "min": "1400", "classe": "C", "esp": "C · APP Recife"}, {"rota": "CHARLIE", "de": "ARAÇOIABA", "para": "CERVEJARIA", "rumo": "100°", "rumoVolta": "280°", "max": "1500", "min": "1300", "classe": "C", "esp": "C · APP Recife"}, {"rota": "DELTA", "de": "PEDREIRA", "para": "MORENO PARK AQUÁTICO", "rumo": "109°", "rumoVolta": "289°", "max": "2100", "min": "2100", "classe": "C", "esp": "C · APP Recife"}, {"rota": "DELTA", "de": "MORENO PARK AQUÁTICO", "para": "LAGOA AZUL", "rumo": "126°", "rumoVolta": "306°", "max": "1600", "min": "1600", "classe": "C", "esp": "C · APP Recife"}, {"rota": "ECHO", "de": "BARRAGEM", "para": "LAGOA AZUL", "rumo": "053°", "rumoVolta": "233°", "max": "1200", "min": "1200", "classe": "C", "esp": "C · APP Recife"}];
const reaPontos = {"ARAÇOIABA": [-35.088833, -7.788333], "CAIS DE SANTA RITA": [-34.8695, -8.062], "LAGOA AZUL": [-34.988833, -8.152], "PEDREIRA": [-35.230333, -8.116667], "PORTO DE GALINHAS": [-35.000333, -8.508667], "TABU": [-34.876667, -7.508833], "ACADEMIA DA POLÍCIA MILITAR": [-35.155, -7.925], "BARRAGEM": [-35.072, -8.287], "CASA CAIADA": [-34.836333, -7.984667], "CERVEJARIA": [-34.922833, -7.753833], "FORTE ORANGE": [-34.84, -7.81], "MORENO PARK AQUÁTICO": [-35.143667, -8.112167], "MURO ALTO": [-34.984167, -8.451333], "TEJUCUPAPO": [-34.8995, -7.6005]};
const portoes = {"ARAÇOIABA": "", "PEDREIRA": "", "PORTO DE GALINHAS": "", "TABU": "", "CAIS DE SANTA RITA": "SBRF", "LAGOA AZUL": "SBRF"};
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
        '<div><span class="rea-linha"></span>REA classe C</div>' +
        '<div><span class="rea-linha g"></span>REA classe G</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Portão</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
