---
title: SBGL - Galeão
tags:
    - Aeródromo
    - Controlado
    - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados Gerais

|                              | Informações                                   |
|------------------------------|-----------------------------------------------|
| **Nome do aeródromo**        | Galeão - Antônio Carlos Jobim                 |
| **Tipo de Operação**         | Internacional, Público e Militar              |
| **Altitude de transição**    | 7000 pés                                      |
| **Elevação**                 | 28 pés (9 m)                                  |
| **Maior aeronave**           | Wide-bodies (código 4E); A380 e B747-8 com procedimentos especiais[^ad20-1] |
| **Espaço aéreo**             | CTR Galeão, classe D, GND/2000 pés[^ad17]     |
| **Aceita A380?** | :material-check:{ style="color:#12a150" }[^ad20-1] |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo.

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBGL?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Meteorologia"
    <div id="metar-taf-container" data-airport="SBGL" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Carregando o METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Carregando o TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBGL){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

---

## :material-routes: Pistas

### Sistema preferencial de pistas

SBGL tem **duas pistas que não se cruzam**, mas convergem a oeste: a 10/28 (4000 m, concreto), ao norte dos terminais, e a 15/33 (3180 m, asfalto), a sudoeste deles[^ad20-3].

<div class="grid cards" markdown>

-   :material-airplane-takeoff:{ .lg .middle } **Decolagens: `10`**

    ---

    4000 × 45 m. Preferencial para **decolagem** na operação segregada. ILS CAT II na 10 e ILS na 28.

-   :material-airplane-landing:{ .lg .middle } **Pousos: `15`**

    ---

    3180 × 47 m. Preferencial para **pouso** na operação segregada. ILS na 15. Cabeceiras deslocadas nos dois sentidos.

</div>

!!! warning "Sistema preferencial"
    Com {==**componente de vento de cauda de até 7 kt**==} e **pistas secas**, vale a configuração da tabela abaixo, conforme o cenário em uso[^ad20-3].

    Com o sistema preferencial em uso, o piloto que pedir o sistema alternativo deve contar com **atraso** no pouso ou na decolagem[^ad20-3].

| Cenário | Pousos | Decolagens | Quando |
| :--- | :---: | :---: | :--- |
| **Operação segregada** (preferencial) | **15** | **10** | Vento de cauda de até 7 kt e pistas secas |
| **Pista única 15/33** | **15** | **15** | Só a 15/33 disponível |
| **Pista única 10/28** | **10** | **10** | Só a 10/28 disponível |
| **Operação convergente** | **28** | **33** | Ativada pela Torre, ver [Operação convergente](#operacao-convergente) |

### Dados das pistas

| Pista | Dimensões | TORA | LDA | Aproximação | Observações |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **10** | 4000 × 45 m | 4000 m | 4000 m | ILS CAT II | |
| **28** | 4000 × 45 m | 4000 m | 4000 m | ILS | |
| **15** | 3180 × 47 m | 3060 m | 2930 m | ILS | Cabeceira deslocada (130 m) |
| **33** | 3180 × 47 m | 3050 m | 2930 m | Não precisão | Cabeceira deslocada (120 m) |

- Na 15/33, o piloto **inicia a decolagem do início da pista**, sem precisar taxiar até a cabeceira deslocada[^ad20-2].
- O AD recebe aeronaves até o código **4E**. **A380** e **B747-8** operam com procedimentos especiais[^ad20-1].

[^ad20-1]: [AIP Brasil, AD 2 SBGL 2.20, item 1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-2]: [AIP Brasil, AD 2 SBGL 2.20, item 2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-3]: [AIP Brasil, AD 2 SBGL 2.20, item 3](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Distâncias declaradas: AD 2.13.

---

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| :--- | :---: | :--- | :---: | :--- |
| **SBGL_ATIS** | `AGL` | ATIS Galeão | **127.600** | D-ATIS |
| **SBGL_DEL** | `DGL` | Tráfego Galeão | **121.000** | `DCL` (código `SBGL`) |
| **SBGL_RMP** | `RGL` | Pátio Galeão | **121.950** | Apenas durante eventos |
| **SBGL_GND** | `GGL` | Solo Galeão | **121.650** | |
| **SBGL_TWR** | `TGL` | Torre Galeão | **118.000** | |

### DCL

O SBGL tem **DCL** (autorização de tráfego por enlace de dados)[^ad18]. Na rede, a estação usa o código **`SBGL`**.

| | |
| :--- | :--- |
| **Código da estação** | `SBGL` |
| **Quem opera** | SBGL_DEL. Sem DEL, a posição que assume a autorização em top-down (GND, TWR, APP ou ACC) |
| **Ferramenta do controlador** | Janela de DCL do TopSky, com o código pessoal do Hoppie ACARS |
| **Ferramenta do piloto** | ACARS da aeronave ou cliente compatível com Hoppie, enviando o pedido de autorização para `SBGL` |

**Como funciona:**

1. O piloto envia o pedido (RCD) para `SBGL`, com posição de estacionamento e letra do ATIS.
2. O controlador confere o plano e responde com a autorização: limite, pista, SID, código transponder, letra do ATIS e próxima frequência.
3. O piloto aceita (`WILCO`/`ACCEPT`). A autorização está cotada e **não há cotejamento por voz**.
4. Com a autorização aceita, o piloto chama o Pátio (ou o Solo, sem Pátio) para acionamento ou reboque.

!!! tip "Configuração do controlador"
    - Faça login no DCL do TopSky com o código `SBGL` antes de abrir a posição.
    - Anuncie no *controller information*: `DCL AVBL LOGON SBGL`.
    - Pedido com erro (plano inválido, SID errada, sem ATIS) volta como **REVERT TO VOICE**: o piloto chama o Tráfego na frequência.
    - Se o piloto não aceitar em tempo razoável, considere a autorização não entregue e chame por voz.

[^ad18]: [AIP Brasil, AD 2 SBGL 2.18](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-map-marker-radius: Áreas de responsabilidade

<figure markdown="span">
  ![Mapa de SBGL com as faixas das pistas em amarelo, sob a Torre, os pátios 1, 2, 3 e 5 em verde, sob o Pátio, e o restante em azul, sob o Solo](img/sbgl-responsabilidade.svg){ loading=lazy }
  <figcaption>Faixas amarelas: Torre. Verde: Pátio (só em eventos). Restante: Solo. A linha tracejada passa pelos pontos de espera. Círculos brancos: números dos pátios.</figcaption>
</figure>

| Posição | Responsável por |
| :--- | :--- |
| **APRON** (só em eventos) | Pátios **1, 2, 3 e 5**, até a saída do pátio |
| **GND** | TWY **B**, **K**, **N**, **M** e as ligações até o **ponto de espera**; pátios 6, 7 e 8. Sem APRON, também os pátios 1, 2, 3 e 5 |
| **TWR** | As duas pistas, os **cruzamentos da 15/33** e as TWY dentro dos pontos de espera |

- Com o Pátio em serviço, a aeronave com destino aos pátios 1, 2, 3 e 5 **chama o Pátio antes de entrar** no pátio[^ad18].
- **Saída:** o Pátio entrega a aeronave ao Solo na saída do pátio; o Solo transfere para a Torre **antes do ponto de espera**.
- **Chegada:** depois de livrar a pista, a Torre transfere para o Solo; o Solo entrega ao Pátio antes da entrada do pátio.

??? info "Área de atuação do Pátio Galeão"
    ![Área de atuação do Pátio Galeão](SBGL-Apron.png){ loading=lazy }

---

## :material-transit-connection-variant: Fluxo de solo

!!! abstract "Regra geral"
    - **TWY B** acompanha a 15/33 e liga os pátios 2, 3 e 5 às cabeceiras 15 e 33. **K** e **Y** correm entre B e os terminais.
    - **N** e **M** acompanham a 10/28. **L1** liga o pátio 1 à N, que leva à cabeceira **10** pela **P**.
    - **L2** a **L5** ligam os pátios à B.

=== "Operação segregada (pousos 15, decolagens 10)"

    <figure markdown="span">
      ![Fluxo de solo na operação segregada: decolagens pela L1, N e P até a cabeceira 10; pousos na 15 livrando pela D ou pela E](img/sbgl-fluxo-15-10.svg){ loading=lazy }
      <figcaption>Verde: decolagens. Laranja tracejado: envergadura acima de 36 m. Azul: pousos.</figcaption>
    </figure>

    - **Decolagens (10):** **L1**, **N** e **P** até a cabeceira 10.
    - **Envergadura acima de 36 m (10):** saída do pátio 2 pela **L3**, depois **K**, **N** e **P**.
    - **Pousos (15):** livram pela **D** ou pela **E** e seguem pela **B** até a ligação do pátio (L2 a L5).

    Exemplo: `GLO1234, táxi para o ponto de espera da pista 10 via L1, N, P.`

=== "Operação convergente (pousos 28, decolagens 33)"

    <figure markdown="span">
      ![Fluxo de solo na operação convergente: decolagens pela B até a G, cabeceira 33; pousos na 28 livrando pela DD ou BB e seguindo pela N até a L1](img/sbgl-fluxo-28-33.svg){ loading=lazy }
      <figcaption>Verde: decolagens. Laranja tracejado: envergadura acima de 36 m. Azul: pousos. Barra vermelha: espera obrigatória antes de cruzar a 15/33.</figcaption>
    </figure>

    - **Decolagens (33):** **B** para sudeste até a **G**, na cabeceira 33.
    - **Envergadura acima de 36 m (33):** **B** até a **F**, cruza a 15/33 com autorização da Torre, **J**, atravessa o pátio 5 e entra pela **H**. A B entre F e G é limitada a 36 m.
    - **Pousos (28):** livram pela **DD** ou pela **BB** e seguem pela **N** para oeste até a **L1**.

    Exemplo: `TAM3456, táxi para o ponto de espera da pista 33 via L4, B, G.`

### Saídas de pista

O piloto deve ajustar o pouso para o menor tempo de ocupação de pista (MROT), principalmente nos horários de maior movimento[^ad20-8].

| Pista | Saídas |
| :---: | :--- |
| **15** | **D** (~1390 m) ou **E** (~1890 m) |
| **33** | **C** (~1960 m) |
| **10** | **AA** (~1090 m) ou **CC** (~2060 m) |
| **28** | **DD** (~1170 m) ou **BB** (~2080 m) |

<small>Distância aproximada da cabeceira até a saída, medida no diagrama.</small>

### Restrições de táxi

| Restrição | Onde |
| :--- | :--- |
| **Envergadura máxima de 36 m** | **Pátio 1** e TWY **Y1**, **Y2**, **Y3** e **Y4**[^ad28] |
| **Envergadura máxima de 36 m** | TWY **B** entre a **F** e a **G**[^ad28] |
| **Barras de parada** | **K** entre L2 e L3; **M** entre K e L1, entre L1 e P e entre P e Q; **N** entre L1 e P e entre Q e S; **T** entre N e M[^ad29] |

!!! danger "Hotspots"
    - **HS1:** pilotos cruzando a 15/33 pela **F** e pela **J** já entraram na pista sem autorização. Cruzamento só com autorização explícita da Torre.
    - **HS2 e HS3:** na **AA** e na **CC**, atenção ao reingresso inadvertido na 10/28 em uso.

[^ad20-8]: [AIP Brasil, AD 2 SBGL 2.20, itens 2 e 8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad28]: [AIP Brasil, AD 2 SBGL 2.8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e carta ADC.
[^ad29]: [AIP Brasil, AD 2 SBGL 2.9](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Hotspots: carta ADC.

---

## :material-airplane-takeoff: Pontos de decolagem

<figure markdown="span">
  ![Visão geral de SBGL com pátios numerados e os pontos de decolagem marcados com a TORA disponível](img/sbgl-visao-geral.svg){ loading=lazy }
  <figcaption>Pontos de decolagem (roxo) com a TORA disponível. Números em círculo: pátios.</figcaption>
</figure>

| Pista | Ponto | TORA |
| :---: | :---: | :---: |
| **10** | **P** (cabeceira) | 4000 m |
| **28** | **Z** (cabeceira) | 4000 m |
| **15** | **A** (início da pista) | 3060 m |
| **33** | **G** ou **H** (início da pista) | 3050 m |

- O piloto chega ao ponto de espera **pronto para decolar**; se não estiver, avisa o ATC com antecedência[^ad20-2].
- Corrida iniciada em até **10 segundos** após a autorização de decolagem[^ad20-2].
- Aeronaves RBAC 121 podem ser autorizadas a decolar **ao mesmo tempo** da 02 do SBRJ e da 15 do SBGL[^ad22].

[^ad22]: [AIP Brasil, AD 2 SBGL 2.22](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-call-merge: Operação convergente

A Torre pode ativar **operações simultâneas nas pistas 28 e 33**, sempre **segregadas**: pousos na **28** e decolagens da **33**[^ad20-2].

**Condições (todas)**[^ad20-2]:

- Visibilidade igual ou acima do mínimo do procedimento e teto pelo menos **100 pés acima da DH**.
- Operação informada no **ATIS** (ou por rádio, sem ATIS) quando o tráfego entra na TMA.
- Carta de aproximação específica em uso, com **"Converging"** no nome (ex.: *IAC ILS U (Converging) RWY 28*). O ponto de aproximação perdida dessas cartas é recuado em relação à cabeceira.

**O piloto deve**[^ad20-2]:

- Avisar o APP **no primeiro contato** se não puder executar a aproximação "Converging".
- Em arremetida após o MAPT, **curvar antes da radial limite** da carta. Se não puder, avisar o APP ou a Torre.

### Ponto de corte

É o ponto da final da 28 que a aeronave em aproximação ainda não pode ter passado para a Torre autorizar uma decolagem da 33. Depois dele, ninguém decola da 33 até a aeronave pousar ou arremeter.

| Condição | Ponto de corte |
| :--- | :---: |
| **IMC** | **3 NM** da cabeceira 28 |
| **VMC** (teto ≥ 1500 pés e visibilidade ≥ 5000 m) | **1,4 NM** da cabeceira 28 |

<small>Ponto de corte e fraseologia: modelo operacional da TWR-GL, citado no AIP[^ad20-2].</small>

Numa arremetida após o MAPT na 28, a separação com quem decola da 33 pode ficar reduzida. Em VMC, a separação visual pode resolver; passe a **informação de tráfego essencial** o quanto antes.

=== "Para quem arremete"
    ```
    PTATC, curve à direita para o procedimento de aproximação perdida, tráfego essencial local, B737 iniciando a decolagem da pista 33.
    PTATC, curve à direita para o procedimento de aproximação perdida, tráfego essencial local, B737 decolando da pista 33, passando o ponto médio da pista.
    PTATC, curve à direita para o procedimento de aproximação perdida, tráfego essencial local, B737 decolando da pista 33, cruzando a cabeceira 15.
    ```

=== "Para quem decola"
    ```
    PTATC, tráfego, B737 iniciando arremetida da pista 28, atenção tráfego essencial local, passando a cabeceira 28.
    PTATC, tráfego, B737 iniciando arremetida da pista 28, atenção tráfego essencial local, passando o ponto médio da pista.
    ```

---

## :material-sign-direction: Pátios e companhias

Referência para a simulação. As posições seguem as cartas PDC e o AIP; as companhias seguem a [lista de companhias do aeroporto na Wikipedia](https://en.wikipedia.org/wiki/Rio_de_Janeiro/Gale%C3%A3o_International_Airport#Airlines_and_destinations). A divisão entre posições é uma simplificação, não a alocação oficial do aeroporto. **VAs** usam as posições da companhia real que representam.

<div class="patios">
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátios 1 e 2"><small>Pátio</small>1·2</span><span class="patio__info"><strong>Terminais 1 e 2</strong><span>Doméstico · pátio 1 até 36 m de envergadura</span><span class="patio__pos">Posições 23 a 45</span></span></header>
<div class="patio__cias"><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="/images/cias/GLO.gif" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="/images/cias/AZU.gif" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure></div>
</section>
<section class="patio patio--largo">
<header class="patio__cab"><span class="patio__num" title="Pátio 3"><small>Pátio</small>3</span><span class="patio__info"><strong>Terminal 2 · Píer Sul</strong><span>Internacional</span><span class="patio__pos">Posições 46 a 84</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="/images/cias/GLO.gif" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="/images/cias/AZU.gif" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure><figure class="cia" title="LATAM Chile (LAN)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM Chile" loading="lazy"><figcaption>LAN</figcaption></figure><figure class="cia" title="LATAM Perú (LPE)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM Perú" loading="lazy"><figcaption>LPE</figcaption></figure><figure class="cia" title="Aerolíneas Argentinas (ARG)"><img class="off-glb" src="/images/cias/ARG.gif" alt="Aerolíneas Argentinas" loading="lazy"><figcaption>ARG</figcaption></figure><figure class="cia" title="Avianca (AVA)"><img class="off-glb" src="/images/cias/AVA.png" alt="Avianca" loading="lazy"><figcaption>AVA</figcaption></figure><figure class="cia" title="BoA (BOV)"><img class="off-glb" src="/images/cias/BOV.gif" alt="BoA" loading="lazy"><figcaption>BOV</figcaption></figure><figure class="cia" title="Copa (CMP)"><img class="off-glb" src="/images/cias/CMP.gif" alt="Copa" loading="lazy"><figcaption>CMP</figcaption></figure><figure class="cia" title="JetSMART (JAT)"><img class="off-glb" src="/images/cias/JAT.png" alt="JetSMART" loading="lazy"><figcaption>JAT</figcaption></figure><figure class="cia" title="SKY Airline (SKU)"><img class="off-glb" src="/images/cias/SKU.png" alt="SKY Airline" loading="lazy"><figcaption>SKU</figcaption></figure><figure class="cia" title="Paranair"><span class="cia__texto">Paranair</span></figure><figure class="cia" title="American Airlines (AAL)"><img class="off-glb" src="/images/cias/AAL.gif" alt="American Airlines" loading="lazy"><figcaption>AAL</figcaption></figure><figure class="cia" title="Delta (DAL)"><img class="off-glb" src="/images/cias/DAL.jpg" alt="Delta" loading="lazy"><figcaption>DAL</figcaption></figure><figure class="cia" title="United (UAL)"><img class="off-glb" src="/images/cias/UAL.gif" alt="United" loading="lazy"><figcaption>UAL</figcaption></figure><figure class="cia" title="Air Canada (ACA)"><img class="off-glb" src="/images/cias/ACA.gif" alt="Air Canada" loading="lazy"><figcaption>ACA</figcaption></figure><figure class="cia" title="Air Transat (TSC)"><span class="cia__texto">Air Transat</span><figcaption>TSC</figcaption></figure><figure class="cia" title="Air France (AFR)"><img class="off-glb" src="/images/cias/AFR.gif" alt="Air France" loading="lazy"><figcaption>AFR</figcaption></figure><figure class="cia" title="KLM (KLM)"><img class="off-glb" src="/images/cias/KLM.gif" alt="KLM" loading="lazy"><figcaption>KLM</figcaption></figure><figure class="cia" title="British Airways (BAW)"><img class="off-glb" src="/images/cias/BAW.gif" alt="British Airways" loading="lazy"><figcaption>BAW</figcaption></figure><figure class="cia" title="Iberia (IBE)"><img class="off-glb" src="/images/cias/IBE.gif" alt="Iberia" loading="lazy"><figcaption>IBE</figcaption></figure><figure class="cia" title="ITA Airways (ITY)"><img class="off-glb" src="/images/cias/ITY.jpg" alt="ITA Airways" loading="lazy"><figcaption>ITY</figcaption></figure><figure class="cia" title="Lufthansa (DLH)"><img class="off-glb" src="/images/cias/DLH.png" alt="Lufthansa" loading="lazy"><figcaption>DLH</figcaption></figure><figure class="cia" title="TAP (TAP)"><img class="off-glb" src="/images/cias/TAP.gif" alt="TAP" loading="lazy"><figcaption>TAP</figcaption></figure><figure class="cia" title="Emirates (UAE)"><img class="off-glb" src="/images/cias/UAE.gif" alt="Emirates" loading="lazy"><figcaption>UAE</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátios 1, 2 e 3"><small>Pátio</small>1·2·3</span><span class="patio__info"><strong>Remoto</strong><span>Pernoite e excedente</span><span class="patio__pos">Posições 85 a 149</span></span></header>
<div class="patio__cias"><p class="patio__nota">Qualquer companhia, conforme a disponibilidade e a envergadura.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 5"><small>Pátio</small>5</span><span class="patio__info"><strong>Terminal de cargas</strong><span>Cargueiros, aviação geral e estadia prolongada</span><span class="patio__pos">Posições 1 a 31</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM Cargo (LCO)"><img class="off-glb" src="/images/cias/TAM.gif" alt="LATAM Cargo" loading="lazy"><figcaption>LCO</figcaption></figure><figure class="cia" title="Atlas Air (GTI)"><img class="off-glb" src="/images/cias/GTI.png" alt="Atlas Air" loading="lazy"><figcaption>GTI</figcaption></figure><figure class="cia" title="Cargolux (CLX)"><img class="off-glb" src="/images/cias/CLX.png" alt="Cargolux" loading="lazy"><figcaption>CLX</figcaption></figure><figure class="cia" title="Total (TTL)"><span class="cia__texto">Total</span><figcaption>TTL</figcaption></figure><figure class="cia" title="Modern Logistics (MWM)"><span class="cia__texto">Modern</span><figcaption>MWM</figcaption></figure><figure class="cia" title="Sky Lease Cargo (KYE)"><span class="cia__texto">Sky Lease</span><figcaption>KYE</figcaption></figure><figure class="cia" title="Aerotranscargo"><span class="cia__texto">Aerotrans</span></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 6"><small>Pátio</small>6</span><span class="patio__info"><strong>Manutenção</strong><span>Hangares junto à TWY L7</span></span></header>
<div class="patio__cias"><p class="patio__nota">Aeronaves em manutenção.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátios 7 e 8"><small>Pátio</small>7·8</span><span class="patio__info"><strong>Base Aérea do Galeão</strong><span>Militar · 8: Correio Aéreo Nacional</span></span></header>
<div class="patio__cias"><figure class="cia" title="Força Aérea Brasileira (FAB)"><span class="cia__texto">FAB</span></figure></div>
</section>
</div>

- Os pátios 1, 2 e 3 recebem aviação comercial doméstica e internacional, aviação geral, táxi aéreo e órgãos de governo. O pátio 5 recebe cargueiros, aviação geral, estadia prolongada e transporte militar[^ad28].
- Aeronaves com mais de 36 m de envergadura não usam o pátio 1[^ad28].

<small>Logos obtidas da [GRU Airport](https://www.gru.com.br/pt/passageiro/descubra-gru/cias-aereas) e da [Travelpayouts](https://pics.avs.io) (Cargolux e Atlas Air). As marcas pertencem às respectivas companhias.</small>

---

## :material-clipboard-text-outline: Outros procedimentos

### Aproximações e pousos

- Livrar a pista no menor tempo possível (MROT)[^ad20-8].
- Os pilotos **não reportam** trem baixado, exceto em emergência.

### Regulamentos do aeródromo

- Observar a VAC para entrar e sair do circuito de tráfego[^ad23].

[^ad17]: [AIP Brasil, AD 2 SBGL 2.17](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad23]: [AIP Brasil, AD 2 SBGL 2.23](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

<small>Diagramas desenhados pela VATSIM Brasil sobre a geometria do [OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL), conferida com as cartas ADC e PDC SBGL. Não use para navegação real. Fonte normativa: AIP Brasil, AD 2 SBGL, AMDT 2610A1.</small>
