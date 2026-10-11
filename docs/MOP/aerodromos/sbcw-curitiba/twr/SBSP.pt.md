---
title: SBSP - Congonhas
tags:
    - Aeródromo
    - Controlado
    - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados Gerais

|                              | Informações                                   |
|------------------------------|-----------------------------------------------|
| **Nome do aeródromo**        | São Paulo - Congonhas - Deputado Freitas Nobre |
| **Tipo de Operação**         | Nacional, Público e Militar                   |
| **Altitude de transição**    | 8000 pés[^ad17]                               |
| **Elevação**                 | 2634 pés (803 m)                              |
| **Maior aeronave**           | Código 4C (A320, B737)[^ad20-1]               |
| **Espaço aéreo**             | CTR São Paulo, classe D, GND/3600 pés[^ad17]  |
| **Aceita A380?** | :material-close:{ style="color:#d63d3d" } |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo.

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBSP?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Meteorologia"
    <div id="metar-taf-container" data-airport="SBSP" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Carregando o METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Carregando o TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBSP){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

---

## :material-routes: Pistas

### Pista principal e pista auxiliar

SBSP tem **duas pistas paralelas**, a ~220 m uma da outra: a **17R/35L**, principal, a oeste, junto ao terminal, e a **17L/35R**, auxiliar, a leste, junto aos hangares da aviação geral. Todas as cabeceiras são deslocadas.

<div class="grid cards" markdown>

-   :material-airplane:{ .lg .middle } **Principal: `17R` / `35L`**

    ---

    Código 4C (A320, B737). ILS CAT I nas duas cabeceiras e EMAS nas duas pontas. Voos regulares.

-   :material-airplane-landing:{ .lg .middle } **Auxiliar: `17L` / `35R`**

    ---

    Código 2B; código 3C só em VMC. RNP e VOR. Turboélices, aviões a pistão e aviação geral.

</div>

!!! warning "Quem usa cada pista"
    - Na **17R/35L** é **proibido** pousar e decolar com envergadura **menor que 14,5 m** (salvo em IMC CAT I e voos aeromédicos) e com **turboélice ou pistão** (salvo RBAC 121 e voos aeromédicos)[^ad12].
    - Só operam em SBSP aeronaves que possam usar **as duas pistas**, exceto voos domésticos regulares de passageiros e voos com enfermos e órgãos[^ad20-1].
    - Voo regular de passageiros que **não puder operar na auxiliar** avisa a Torre **no primeiro contato**[^ad18].
    - Na **17L/35R**, aeronaves de **código 3** só em **VMC**[^ad20-1].

O AIP não define pista preferencial: a configuração (17 ou 35) segue o vento e vale para as duas pistas.

### Dados das pistas

| Pista | Dimensões | TORA | LDA | Aproximação | Observações |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **17R** | 1883 × 45 m | 1760 m | 1660 m | ILS CAT I | Cabeceira deslocada (103 m). EMAS |
| **35L** | 1883 × 45 m | 1760 m | 1660 m | ILS CAT I | Cabeceira deslocada (27 m). EMAS |
| **17L** | 1495 × 45 m | 1345 m | 1195 m | Não precisão | RNP e VOR. Cabeceira deslocada (60 m) |
| **35R** | 1495 × 45 m | 1345 m | 1195 m | Não precisão | RNP e VOR. Cabeceira deslocada (60 m) |

[^ad12]: [AIP Brasil, AD 2 SBSP 2.12](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Distâncias declaradas: AD 2.13.
[^ad20-1]: [AIP Brasil, AD 2 SBSP 2.20, item 1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| :--- | :---: | :--- | :---: | :--- |
| **SBSP_ATIS** | `ASP` | Informações São Paulo | **127.650** | D-ATIS |
| **SBSP_DEL** | `DSP` | Tráfego São Paulo | **120.600** | `DCL` (código `SBSP`) |
| **SBSP_GND** | `GSP` | Solo São Paulo | **121.900** | |
| **SBSP_TWR** | `TSP` | Torre São Paulo | **127.150** | 118.050 é a reserva |
| **SBSP_H_TWR** | `HSP` | Controle Helicóptero | **118.350** | Área de controle de helicópteros |

- O **Solo** define a sequência de acionamento e táxi, conforme o fluxo da TMA e do AD[^ad22].
- A Torre não informa a hora da decolagem. A aeronave fica na frequência da Torre até **cruzar a cabeceira oposta**[^ad18].
- Nas horas de alta densidade, pousos e decolagens com o **menor tempo de ocupação de pista** possível[^ad22].

### DCL

O SBSP tem **DCL** (autorização de tráfego por enlace de dados)[^ad18]. Na rede, a estação usa o código **`SBSP`**.

| | |
| :--- | :--- |
| **Código da estação** | `SBSP` |
| **Quem opera** | SBSP_DEL. Sem DEL, a posição que assume a autorização em top-down (GND, TWR, APP ou ACC) |
| **Ferramenta do controlador** | Janela de DCL do TopSky, com o código pessoal do Hoppie ACARS |
| **Ferramenta do piloto** | ACARS da aeronave ou cliente compatível com Hoppie, enviando o pedido de autorização para `SBSP` |

**Como funciona:**

1. O piloto envia o pedido (RCD) para `SBSP`, com posição de estacionamento e letra do ATIS.
2. O controlador confere o plano e responde com a autorização: limite, pista, SID, código transponder, letra do ATIS e próxima frequência.
3. O piloto aceita (`WILCO`/`ACCEPT`). A autorização está cotada e **não há cotejamento por voz**.
4. Com a autorização aceita, o piloto chama o Solo para acionamento ou pushback.

!!! tip "Configuração do controlador"
    - Faça login no DCL do TopSky com o código `SBSP` antes de abrir a posição.
    - Anuncie no *controller information*: `DCL AVBL LOGON SBSP`.
    - Pedido com erro (plano inválido, SID errada, sem ATIS) volta como **REVERT TO VOICE**: o piloto chama o Tráfego na frequência.
    - Se o piloto não aceitar em tempo razoável, considere a autorização não entregue e chame por voz.

[^ad18]: [AIP Brasil, AD 2 SBSP 2.18](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-map-marker-radius: Áreas de responsabilidade

<figure markdown="span">
  ![Mapa de SBSP com as faixas das duas pistas em amarelo, sob a Torre, e o restante em azul, sob o Solo](img/sbsp-responsabilidade.svg){ loading=lazy }
  <figcaption>Faixas amarelas: Torre. Restante: Solo. A linha tracejada passa pelos pontos de espera. Círculos brancos: números dos pátios.</figcaption>
</figure>

| Posição | Responsável por |
| :--- | :--- |
| **GND** | Pátios 1, 2 e 3 e as TWY até o **ponto de espera** |
| **TWR** | As duas pistas e as TWY dentro dos pontos de espera, inclusive **A**, **B**, **C** e **D**, entre as pistas |
| **Controle Helicóptero** | Helicópteros VFR na área de controle de helicópteros |

- SBSP **não tem Pátio** (APRON): o Solo cuida de todos os pátios.
- Entre as duas pistas só há as ligações **A**, **B**, **C** e **D**, todas dentro das faixas: quem passa de um lado ao outro fica com a **Torre**.
- **Chegada:** depois de livrar a pista, a Torre transfere para o Solo.

---

## :material-transit-connection-variant: Fluxo de solo

!!! abstract "Regra geral"
    - **Lado oeste (pista principal):** **M** e **N** correm em frente ao pátio 3. **E** e **F** levam à cabeceira 17R; **H** liga o meio do pátio à pista; **L** segue para o sul até **I**, **J** e **K** (cabeceira 35L).
    - **Lado leste (pista auxiliar):** **S** corre em frente aos pátios 1 e 2; **O** e **P** chegam à 17L, **Q** ao meio e **R** à 35R.
    - **A**, **B**, **C** e **D** ligam as duas pistas.
    - Saída do pátio principal com **pushback**[^ad20-1].

=== "Pistas 17R e 17L"

    <figure markdown="span">
      ![Fluxo de solo nas pistas 17: decolagens 17R pelo N, M e E; pousos 17R livrando pela I e voltando pela L e H; aviação geral na 17L pela S e O](img/sbsp-fluxo-17.svg){ loading=lazy }
      <figcaption>Verde: decolagens na principal. Laranja tracejado: pista auxiliar. Azul: pousos.</figcaption>
    </figure>

    - **Decolagens (17R):** **N** ou **M** para o norte e **E** até a cabeceira.
    - **Pousos (17R):** livram pela **I** (saída rápida) ou pela **J**/**K** no fim, e voltam pela **L** e pela **H** até o pátio 3. Quem precisa de menos pista livra pela **H**.
    - **Pista auxiliar (17L):** dos pátios 1 e 2 pela **S** e pela **O**.

    Exemplo: `GLO1234, táxi para o ponto de espera da pista 17R via N e E.`

=== "Pistas 35L e 35R"

    <figure markdown="span">
      ![Fluxo de solo nas pistas 35: decolagens 35L pelo N, H, L e K; pousos 35L livrando pela F e voltando pela M; aviação geral na 35R pela S e R](img/sbsp-fluxo-35.svg){ loading=lazy }
      <figcaption>Verde: decolagens na principal. Laranja tracejado: pista auxiliar. Azul: pousos.</figcaption>
    </figure>

    - **Decolagens (35L):** **N**, **H**, **L** e **K** (ou **J**) até a cabeceira.
    - **Pousos (35L):** livram pela **F** ou, no fim, pela **E**, e voltam pela **M**. Quem para cedo livra pela **H**.
    - **Pista auxiliar (35R):** dos pátios 1 e 2 pela **S** e pela **R**.

    Exemplo: `AZU4321, táxi para o ponto de espera da pista 35L via N, H, L e K.`

### Saídas de pista

| Pista | Saídas |
| :---: | :--- |
| **17R** | **H** (~1010 m), **I** (~1260 m, saída rápida) ou **J**/**K** (fim) |
| **35L** | **H** (~660 m), **F** (~1600 m) ou **E**/**A** (fim) |
| **17L** | **P** (~320 m), **Q**/**C** (~900 m) ou **R**/**D** (fim) |
| **35R** | **Q**/**C** (~400 m), **P** (~1060 m), **O**/**B** (~1250 m) ou **A** (fim) |

<small>Distância aproximada da cabeceira até a saída, medida no diagrama.</small>

### Hotspots

| Hotspot | Onde | Atenção |
| :---: | :--- | :--- |
| **HS1** | Cabeceira 17R, na **E** | Risco de incursão na pista |
| **HS2** | **F**, junto à **E** | Jato-reação de aeronaves na E |
| **HS3** | Encontro da **H**, **L**, **M**, **N**, **W** e **X** | Risco de colisão no solo |

### Restrições de táxi

| Restrição | Onde |
| :--- | :--- |
| **Envergadura máxima de 24 m** | TWY **O** e **S**[^ad20-6] |
| **TWY O em IMC** | Proibido táxi de letra de código **B** com pousos e decolagens de código **1 ou 2** na 17L/35R; proibido usar a O com código **3** na 17L/35R[^ad20-6] |
| **Velocidade máxima de 15 kt** | TWY **N**, pela proximidade da M e da linha de segurança do pátio 3[^ad20-6] |

[^ad20-6]: [AIP Brasil, AD 2 SBSP 2.20, item 6](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e carta ADC.

---

## :material-airplane-takeoff: Pontos de decolagem

<figure markdown="span">
  ![Visão geral de SBSP com pátios numerados, hotspots e os pontos de decolagem marcados com a TORA disponível](img/sbsp-visao-geral.svg){ loading=lazy }
  <figcaption>Pontos de decolagem (roxo) com a TORA disponível. Círculos vermelhos: hotspots. Números em círculo: pátios.</figcaption>
</figure>

| Pista | Ponto | TORA | Quem usa |
| :---: | :---: | :---: | :--- |
| **17R** | **E** (cabeceira) | 1760 m | Jatos |
| **35L** | **K** (cabeceira) | 1760 m | Jatos |
| **17L** | **O** (cabeceira) | 1345 m | Turboélices, pistão e aviação geral |
| **35R** | **R** (cabeceira) | 1345 m | Turboélices, pistão e aviação geral |

- O AIP de SBSP não publica interseções de decolagem.

---

## :material-helicopter: Helicópteros

- Helicópteros pousam e decolam **só nas pistas**; não em TWY, pátios ou hangares[^ad20-8]. O trecho da 17L/35R na interseção com a **B** serve para pouso e decolagem de helicópteros[^ad20-2].
- Na final da 17 e na rampa de decolagem da 35 pode ser aplicada **separação composta** entre aviões IFR e helicópteros VFR na área de controle de helicópteros: mínimo de **2,5 NM × 500 pés**[^ad22].

[^ad20-2]: [AIP Brasil, AD 2 SBSP 2.20, item 2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-8]: [AIP Brasil, AD 2 SBSP 2.20, item 8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-sign-direction: Pátios e companhias

Referência para a simulação. As posições seguem as cartas PDC; as companhias seguem a [lista de companhias do aeroporto na Wikipedia](https://en.wikipedia.org/wiki/S%C3%A3o_Paulo%E2%80%93Congonhas_Airport#Airlines_and_destinations). A divisão entre posições é uma simplificação, não a alocação oficial do aeroporto. **VAs** usam as posições da companhia real que representam.

<div class="patios">
<section class="patio patio--largo">
<header class="patio__cab"><span class="patio__num" title="Pátio 3"><small>Pátio</small>3</span><span class="patio__info"><strong>Terminal de passageiros</strong><span>Doméstico</span><span class="patio__pos">Posições 01 a 29</span></span></header>
<div class="patio__cias"><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="/images/cias/AZU.gif" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="/images/cias/GLO.gif" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 3"><small>Pátio</small>3</span><span class="patio__info"><strong>Pavilhão de Autoridades</strong><span>Junto à F</span><span class="patio__pos">Posições P01 a P03</span></span></header>
<div class="patio__cias"><p class="patio__nota">Autoridades. A P01 é só para embarque e desembarque (até 2 h).</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátios 1 e 2"><small>Pátio</small>1·2</span><span class="patio__info"><strong>Aviação geral</strong><span>Lado leste, pela S</span></span></header>
<div class="patio__cias"><p class="patio__nota">Aviação geral, executiva e táxi aéreo, junto aos hangares.</p></div>
</section>
</div>

<small>Logos obtidas da [GRU Airport](https://www.gru.com.br/pt/passageiro/descubra-gru/cias-aereas). As marcas pertencem às respectivas companhias.</small>

---

## :material-clipboard-text-outline: Outros procedimentos

- Não são aceitos planos **VFR** de aviões com origem ou destino em SBSP, salvo militares ou com auxílios de navegação indisponíveis[^ad22].
- O APP pode vetorar para **aproximação visual** com visibilidade de 5 km ou mais e teto de 1000 pés ou mais; o plano segue IFR até o piloto reportar a pista à vista[^ad22].
- O aeródromo **não pode ser usado como alternativa**[^ad20-1].
- Observar a VAC para entrar e sair do circuito de tráfego[^ad23].

[^ad17]: [AIP Brasil, AD 2 SBSP 2.17](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e cartas IAC.
[^ad22]: [AIP Brasil, AD 2 SBSP 2.22](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad23]: [AIP Brasil, AD 2 SBSP 2.23](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

<small>Diagramas desenhados pela VATSIM Brasil sobre a geometria do [OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL), conferida com as cartas ADC e PDC SBSP. Não use para navegação real. Fonte normativa: AIP Brasil, AD 2 SBSP, AMDT 2610A1.</small>
