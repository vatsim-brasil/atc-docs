---
title: SBSV - Salvador
tags:
    - Aeródromo
    - Controlado
    - SBRE
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados Gerais

|                              | Informações                                   |
|------------------------------|-----------------------------------------------|
| **Nome do aeródromo**        | Salvador - Deputado Luís Eduardo Magalhães    |
| **Tipo de Operação**         | Internacional, Público e Militar              |
| **Altitude de transição**    | 10000 pés[^ad17]                              |
| **Elevação**                 | 66 pés (20 m)                                 |
| **Maior aeronave**           | Wide-bodies (código 4E) na 10/28; código 4C na 17/35 |
| **Espaço aéreo**             | CTR Salvador, classe C, GND/3500 pés[^ad17]   |
| **Aceita A380?** | :material-close:{ style="color:#d63d3d" } |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo.

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBSV?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Meteorologia"
    <div id="metar-taf-container" data-airport="SBSV" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Carregando o METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Carregando o TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBSV){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

---

## :material-routes: Pistas

### Sistema de pistas

SBSV tem **duas pistas que não se cruzam**: a principal 10/28 (3003 m), com a TWY **A** paralela ao sul, e a 17/35 (1518 m), a oeste, com a TWY **M** paralela a leste. O AIP **não define pista preferencial**: a 10/28 é usada no sentido do vento.

<div class="grid cards" markdown>

-   :material-airplane:{ .lg .middle } **Principal: `10/28`**

    ---

    3003 × 45 m. ILS nas duas cabeceiras, ambas deslocadas em 120 m. Recebe até o código 4E.

-   :material-airplane:{ .lg .middle } **Secundária: `17/35`**

    ---

    1518 × 45 m, sem aproximação de precisão. Durante a HIRO, é a pista **preferencial de decolagem** das aeronaves de categoria A e B[^ad20-12].

</div>

!!! warning "Pista 17/35"
    - Disponível para **operação ocasional** (PCN 44/F/C/X/U)[^ad20-6].
    - A **35 não recebe pousos de jatos** ou aeronaves de desempenho superior[^ad20-6].
    - Concentração de **pássaros** nas proximidades da 17/35[^ad23].

### Dados das pistas

| Pista | Dimensões | TORA | LDA | Aproximação | Observações |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **10** | 3003 × 45 m | 2883 m | 2763 m | ILS | Cabeceira deslocada (120 m); zona livre de obstáculos de 300 m |
| **28** | 3003 × 45 m | 2883 m | 2763 m | ILS CAT I | Cabeceira deslocada (120 m) |
| **17** | 1518 × 45 m | 1518 m | 1518 m | RNP | Código 4C |
| **35** | 1518 × 45 m | 1518 m | 1518 m | Visual | Sem pouso de jatos |

[^ad20-6]: [AIP Brasil, AD 2 SBSV 2.20, item 6](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Distâncias declaradas: AD 2.13.
[^ad23]: [AIP Brasil, AD 2 SBSV 2.23](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| :--- | :---: | :--- | :---: | :--- |
| **SBSV_ATIS** | `ASV` | Informações Salvador | **127.750** | D-ATIS |
| **SBSV_DEL** | `DSV` | Tráfego Salvador | **121.100** | `DCL` (código `SBSV`) |
| **SBSV_GND** | `GSV` | Solo Salvador | **121.900** | |
| **SBSV_TWR** | `TSV` | Torre Salvador | **118.300** | |

### DCL

O SBSV tem **DCL** (autorização de tráfego por enlace de dados)[^ad18]. Na rede, a estação usa o código **`SBSV`**.

| | |
| :--- | :--- |
| **Código da estação** | `SBSV` |
| **Quem opera** | SBSV_DEL. Sem DEL, a posição que assume a autorização em top-down (GND, TWR, APP ou ACC) |
| **Ferramenta do controlador** | Janela de DCL do TopSky, com o código pessoal do Hoppie ACARS |
| **Ferramenta do piloto** | ACARS da aeronave ou cliente compatível com Hoppie, enviando o pedido de autorização para `SBSV` |

**Como funciona:**

1. O piloto envia o pedido (RCD) para `SBSV`, com posição de estacionamento e letra do ATIS.
2. O controlador confere o plano e responde com a autorização: limite, pista, SID, código transponder, letra do ATIS e próxima frequência.
3. O piloto aceita (`WILCO`/`ACCEPT`). A autorização está cotada e **não há cotejamento por voz**.
4. Com a autorização aceita, o piloto chama o Solo para acionamento ou pushback.

!!! tip "Configuração do controlador"
    - Faça login no DCL do TopSky com o código `SBSV` antes de abrir a posição.
    - Anuncie no *controller information*: `DCL AVBL LOGON SBSV`.
    - Pedido com erro (plano inválido, SID errada, sem ATIS) volta como **REVERT TO VOICE**: o piloto chama o Tráfego na frequência.
    - Se o piloto não aceitar em tempo razoável, considere a autorização não entregue e chame por voz.

[^ad18]: [AIP Brasil, AD 2 SBSV 2.18](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-map-marker-radius: Áreas de responsabilidade

<figure markdown="span">
  ![Mapa de SBSV com as faixas das pistas em amarelo, sob a Torre, e o restante em azul, sob o Solo](img/sbsv-responsabilidade.svg){ loading=lazy }
  <figcaption>Faixas amarelas: Torre. Restante: Solo. A linha tracejada passa pelos pontos de espera. Círculos brancos: números dos pátios.</figcaption>
</figure>

| Posição | Responsável por |
| :--- | :--- |
| **GND** | Pátios 1 a 6, TWY **A**, **K**, **M** e as ligações até o **ponto de espera** |
| **TWR** | As duas pistas e as TWY dentro dos pontos de espera |

- SBSV **não tem Pátio** (APRON): o Solo cuida de todos os pátios.
- **Saída:** o Solo transfere para a Torre **antes do ponto de espera**. O piloto chega ao ponto de espera pronto para decolar; se não estiver, avisa o Solo[^ad20-11].
- **Chegada:** depois de livrar a pista, a Torre transfere para o Solo.

---

## :material-transit-connection-variant: Fluxo de solo

!!! abstract "Regra geral"
    - **TWY A** acompanha a 10/28 pelo sul, da **C** (cabeceira 10) até a **G** (cabeceira 28). **K** corre paralela à A entre o pátio 1 e a **D**, junto ao pátio 3.
    - **J1** a **J4** são as pistas de táxi do pátio 1. A **J1** liga o pátio à A e à **C**.
    - **H** e **H1** ligam a 10/28 aos pátios militares 2 e 6, ao norte.
    - **M** acompanha a 17/35 pelo leste. **N**, **R**, **Q**, **P** e **L** ligam a 17/35 aos pátios 4 e 5 e à M.

=== "Pista 10"

    <figure markdown="span">
      ![Fluxo de solo na pista 10: decolagens pela J1, A e C; turboélices pela interseção D; pousos livrando pela F e seguindo pela A até o pátio 1](img/sbsv-fluxo-10.svg){ loading=lazy }
      <figcaption>Verde: decolagens. Laranja tracejado: decolagem da interseção. Azul: pousos.</figcaption>
    </figure>

    - **Decolagens (10):** **J1**, **A** e **C**. A **C** é a entrada padrão; pela **B**, só com coordenação com o Solo, e a aeronave pode perder a vez[^ad20-12].
    - **Turboélices:** decolam da interseção **D** ou **H**, salvo instrução diferente[^ad20-11].
    - **Pousos (10):** livram pela **F** e seguem pela **A** até o pátio 1. Turboélices e aeronaves a pistão podem livrar pela **D**[^ad20-10].

    Exemplo: `GLO1234, táxi para o ponto de espera da pista 10 via J1, A, C.`

=== "Pista 28"

    <figure markdown="span">
      ![Fluxo de solo na pista 28: decolagens pela A até a G; pousos livrando pela D e seguindo pela K até o pátio 1](img/sbsv-fluxo-28.svg){ loading=lazy }
      <figcaption>Verde: decolagens. Azul: pousos.</figcaption>
    </figure>

    - **Decolagens (28):** **A** para leste até a **G**.
    - **Pousos (28):** livram pela **D**[^ad20-10] e seguem pela **K** até o pátio 1. A D é limitada a **36 m** de envergadura: acima disso, livram no fim da pista, pela **C**.

    Exemplo: `AZU4321, táxi para o ponto de espera da pista 28 via A, G.`

### Saídas de pista

O piloto deve livrar a pista no menor tempo de ocupação de pista (MROT), escolhendo uma saída exequível antes de parar[^ad20-10].

| Pista | Saídas |
| :---: | :--- |
| **10** | **D** (~1040 m, turboélices e pistão), **E** (~1390 m) ou **F** (~1960 m) |
| **28** | **F** (~690 m, turboélices), **E** (~1240 m) ou **D** (~1730 m, até 36 m de envergadura) |

<small>Distância aproximada da cabeceira até a saída. D e F na 10 e D na 28: AIP; as demais, medidas no diagrama.</small>

### Restrições de táxi

| Restrição | Onde |
| :--- | :--- |
| **Envergadura máxima de 36 m** | TWY **D** e **L**[^ad28] |
| **Fechada** | TWY **L** entre o pátio 1 e a **M**, por obras de ampliação do terminal[^ad28] |
| **Velocidade máxima de 8 kt** | TWY **J2**[^ad28] |
| **Cheque de motores** | Na TWY **G** entre 0600 e 2200 e na pista 17/35 a qualquer hora, com autorização prévia. Proibido em frente à Torre e em qualquer lugar entre 2200 e 0600[^ad20-1] |

!!! danger "Hotspot"
    **HP**, na **C** e na **J1**, junto à cabeceira 10: o ponto de espera demarcado **não forma 90° com a pista**, e o piloto pode achar que há outro ponto de espera à frente. Risco de **incursão na pista**: confirme que a aeronave para no ponto de espera.

[^ad28]: [AIP Brasil, AD 2 SBSV 2.8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e carta ADC. Hotspot: carta ADC.
[^ad20-1]: [AIP Brasil, AD 2 SBSV 2.20, item 1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e AD 2.23.
[^ad20-10]: [AIP Brasil, AD 2 SBSV 2.20, item 10](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-airplane-takeoff: Pontos de decolagem

<figure markdown="span">
  ![Visão geral de SBSV com pátios numerados e os pontos de decolagem marcados com a TORA disponível](img/sbsv-visao-geral.svg){ loading=lazy }
  <figcaption>Pontos de decolagem (roxo) com a TORA disponível. Números em círculo: pátios.</figcaption>
</figure>

| Pista | Ponto | TORA | Quem usa |
| :---: | :---: | :---: | :--- |
| **10** | **C** | 2776 m | Jatos (entrada padrão)[^ad20-11] |
| **10** | **B** (início da pista) | 2883 m | Com coordenação com o Solo durante a HIRO[^ad20-12] |
| **10** | **D** ou **H** | 1848 m | Turboélices[^ad20-11] |
| **28** | **G** | 2883 m | Todos |
| **17** ou **35** | Cabeceira | 1518 m | Categoria A e B durante a HIRO[^ad20-12] |

- O piloto chega ao ponto de espera **pronto para decolar**; se não estiver, avisa o Solo[^ad20-11].
- Alinhamento **imediato** quando autorizado, e corrida iniciada em até **10 segundos** após a autorização de decolagem[^ad20-11].
- Após decolar, chamar o APP imediatamente só com `CONTROLE SALVADOR, [INDICATIVO]`, sem informação adicional[^ad20-11].
- Turboélices e aeronaves a pistão aguardam **vetoração** ou autorização **direto** a um waypoint logo após a decolagem[^ad20-11].
- Quem não puder decolar da interseção avisa o Solo[^ad20-12].

[^ad20-11]: [AIP Brasil, AD 2 SBSV 2.20, item 11](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-speedometer: HIRO

A **HIRO** (operação de pista de alta intensidade) reduz o tempo de ocupação de pista para encurtar a separação na final, entre decolagens e entre pousos e decolagens[^ad20-12].

| | |
| :--- | :--- |
| **Horário** | **1300–1500**, **1600–1830** e **2000–2100 UTC**. O ATC pode mudar conforme a demanda; o horário vai no **ATIS** |
| **Velocidade na aproximação** | **170 a 150 kt IAS** a 5 NM da cabeceira. Velocidades atribuídas pelo ATC são obrigatórias |
| **Pouso na 10** | Livrar pela **D**, **E** ou **F** (868, 1169 e 1651 m da cabeceira 10). Se não puder, avisar o APP ou a Torre no primeiro contato |
| **Decolagem da 10** | Entrada padrão pela **C** (2594 m até a cabeceira 28, medidos com a aeronave alinhada). Pela **B** (2767 m), só com coordenação. Interseção **D**: 1645 m |
| **Categorias A e B** | Decolam **da 17/35**. Da 10/28, só militares saindo dos pátios 2 e 6, aeronaves com prioridade, em IMC ou por necessidade da Torre |

[^ad20-12]: [AIP Brasil, AD 2 SBSV 2.20, item 12](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-sign-direction: Pátios e companhias

Referência para a simulação. As posições seguem as cartas PDC; as companhias seguem a [lista de companhias do aeroporto na Wikipedia](https://en.wikipedia.org/wiki/Salvador_International_Airport#Airlines_and_destinations). A divisão entre posições é uma simplificação, não a alocação oficial do aeroporto. **VAs** usam as posições da companhia real que representam.

<div class="patios">
<section class="patio patio--largo">
<header class="patio__cab"><span class="patio__num" title="Pátio 1"><small>Pátio</small>1</span><span class="patio__info"><strong>Terminal de passageiros</strong><span>Doméstico e internacional</span><span class="patio__pos">Posições 01 a 19</span></span></header>
<div class="patio__cias"><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="/images/cias/AZU.gif" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="/images/cias/GLO.gif" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="Abaeté Aviação"><span class="cia__texto">Abaeté</span></figure><figure class="cia" title="Aerolíneas Argentinas (ARG)"><img class="off-glb" src="/images/cias/ARG.gif" alt="Aerolíneas Argentinas" loading="lazy"><figcaption>ARG</figcaption></figure><figure class="cia" title="SKY Airline (SKU)"><img class="off-glb" src="/images/cias/SKU.png" alt="SKY Airline" loading="lazy"><figcaption>SKU</figcaption></figure><figure class="cia" title="Copa (CMP)"><img class="off-glb" src="/images/cias/CMP.gif" alt="Copa" loading="lazy"><figcaption>CMP</figcaption></figure><figure class="cia" title="TAP (TAP)"><img class="off-glb" src="/images/cias/TAP.gif" alt="TAP" loading="lazy"><figcaption>TAP</figcaption></figure><figure class="cia" title="Air Europa (AEA)"><img class="off-glb" src="/images/cias/AEA.gif" alt="Air Europa" loading="lazy"><figcaption>AEA</figcaption></figure><figure class="cia" title="Air France (AFR)"><img class="off-glb" src="/images/cias/AFR.gif" alt="Air France" loading="lazy"><figcaption>AFR</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 3"><small>Pátio</small>3</span><span class="patio__info"><strong>Terminal de cargas</strong><span>Cargueiros, pela K</span><span class="patio__pos">Posições 20 a 26</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM Cargo (LCO)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM Cargo" loading="lazy"><figcaption>LCO</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátios 2 e 6"><small>Pátio</small>2·6</span><span class="patio__info"><strong>Militar</strong><span>Ao norte da 10/28 · 2 pela H, 6 pela H1</span><span class="patio__pos">Posições 01 a 13 (2) e 01 a 03 (6)</span></span></header>
<div class="patio__cias"><figure class="cia" title="Força Aérea Brasileira (FAB)"><span class="cia__texto">FAB</span></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátios 4 e 5"><small>Pátio</small>4·5</span><span class="patio__info"><strong>Aviação geral e hangares</strong><span>Junto à 17/35 · 4 pela R, 5 pela P</span></span></header>
<div class="patio__cias"><p class="patio__nota">Aviação geral e helicópteros.</p></div>
</section>
</div>

<small>Logos obtidas da [GRU Airport](https://www.gru.com.br/pt/passageiro/descubra-gru/cias-aereas). As marcas pertencem às respectivas companhias.</small>

---

## :material-clipboard-text-outline: Outros procedimentos

- Observar a VAC para entrar e sair do circuito de tráfego e a AIC de corredores visuais da TMA Salvador[^ad22].
- Proibida a apresentação de plano de voo por radiotelefonia, exceto helidecks de plataformas de petróleo e gás em emergência[^ad22].

[^ad17]: [AIP Brasil, AD 2 SBSV 2.17](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e cartas IAC.
[^ad22]: [AIP Brasil, AD 2 SBSV 2.22](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

<small>Diagramas desenhados pela VATSIM Brasil sobre a geometria do [OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL), conferida com as cartas ADC e PDC SBSV. Não use para navegação real. Fonte normativa: AIP Brasil, AD 2 SBSV, AMDT 2610A1.</small>
