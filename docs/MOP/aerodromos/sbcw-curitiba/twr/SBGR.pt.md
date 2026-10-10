---
title: SBGR - Guarulhos
tags:
    - Aeródromo
    - Controlado
    - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados Gerais

|                              | Informações                                   |
|------------------------------|-----------------------------------------------|
| **Nome do aeródromo**        | Governador André Franco Montoro               |
| **Tipo de Operação**         | Internacional, Público e Militar              |
| **Altitude de transição**    | 8000 pés                                      |
| **Elevação**                 | 2461 pés (750 m)                              |
| **Código de referência**     | 4E (B747-8 e A380 com autorização especial)[^ad23] |
| **Espaço aéreo**             | CTR Guarulhos, classe D, GND/3600 pés[^ad17]  |
| **Operação**                 | IFR. VFR de asa fixa proibido, exceto militares brasileiras[^ad22] |
| **Aceita A380?** | :material-check:{ style="color:#12a150" }[^ad23] |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo.

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBGR?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Meteorologia"
    <div id="metar-taf-container" data-airport="SBGR" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Carregando o METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Carregando o TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBGR){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

---

## :material-routes: Pistas

### Pistas preferenciais

As duas pistas são paralelas e distam apenas 375 m entre eixos. Por isso **não há operação independente**: em condições normais uma pista é de pouso e a outra de decolagem[^ad20-1].

<div class="grid cards" markdown>

-   :material-airplane-landing:{ .lg .middle } **Pousos: `10R` / `28L`**

    ---

    Pista sul, 3000 × 45 m. Preferencial para **pouso**. ILS CAT III na 10R e CAT I na 28L.

-   :material-airplane-takeoff:{ .lg .middle } **Decolagens: `10L` / `28R`**

    ---

    Pista norte, 3700 × 45 m, junto aos pátios. Preferencial para **decolagem**. ILS CAT II na 10L e CAT I na 28R.

</div>

!!! warning "Sistema preferencial: cabeceiras 10"
    Com {==**componente de vento de cauda menor que 7 kt**==} e **pista seca**, o sistema preferencial é o **10R/10L**, usado em preferência ao 28L/28R[^ad20-1].

    Com o sistema 10 em uso e vento de cauda, o piloto que pedir o sistema 28 deve contar com **atraso** no pouso ou na decolagem[^ad20-1].

| Configuração | Pouso | Decolagem | Quando |
| :--- | :---: | :---: | :--- |
| **10** (preferencial) | **10R** | **10L** | Vento de cauda < 7 kt e pista seca |
| **28** | **28L** | **28R** | Demais casos (vento de cauda ≥ 7 kt na 10 ou pista não seca), conforme o vento |

### Dados das pistas

| Pista | Dimensões | TORA | LDA | Aproximação | Observações |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **10L** | 3700 × 45 m | 3700 m | 3610 m | ILS CAT II, RNP | Cabeceira deslocada 90 m |
| **28R** | 3700 × 45 m | 3700 m | 3640 m | ILS CAT I, RNP | Cabeceira deslocada 60 m |
| **10R** | 3000 × 45 m | 3000 m | 3000 m | ILS CAT III, RNP | TODA 3300 m (zona livre de obstáculos de 300 m) |
| **28L** | 3000 × 45 m | 3000 m | 3000 m | ILS CAT I, RNP | |

[^ad20-1]: [AIP Brasil, AD 2 SBGR 2.20, item 1.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Distâncias declaradas: AD 2.13 e carta ADC.

---

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| :--- | :---: | :--- | :---: | :--- |
| **SBGR_ATIS** | `AGR` | ATIS | **127.750** | D-ATIS |
| **SBGR_DEL** | `DGR` | Tráfego Guarulhos | **121.000** | `DCL` (código `SBGR`) |
| **SBGR_GND** | `GGR` | Solo Guarulhos | **121.700** | |
| **SBGR_TWR** | `TGR` | Torre Guarulhos | **132.750** | |

### DCL

O SBGR tem **DCL** (autorização de tráfego por enlace de dados). Na rede, a estação usa o código **`SBGR`**.

| | |
| :--- | :--- |
| **Código da estação** | `SBGR` |
| **Quem opera** | SBGR_DEL. Sem DEL, a posição que assume a autorização em top-down (GND, TWR, APP ou ACC) |
| **Ferramenta do controlador** | Janela de DCL do TopSky, com o código pessoal do Hoppie ACARS |
| **Ferramenta do piloto** | ACARS da aeronave ou cliente compatível com Hoppie, enviando o pedido de autorização para `SBGR` |
| **Prazo** | Pedido até **15 minutos antes do EOBT**[^ad20-7] |

**Como funciona:**

1. O piloto envia o pedido (RCD) para `SBGR`, com posição de estacionamento e letra do ATIS.
2. O controlador confere o plano e responde com a autorização: limite, pista, SID, código transponder, letra do ATIS e próxima frequência.
3. O piloto aceita (`WILCO`/`ACCEPT`). A autorização está cotada e **não há cotejamento por voz**.
4. Com a autorização aceita, o piloto chama o Solo direto para acionamento ou reboque.

!!! tip "Configuração do controlador"
    - Faça login no DCL do TopSky com o código `SBGR` antes de abrir a posição.
    - Anuncie no *controller information*: `DCL AVBL LOGON SBGR`.
    - Pedido com erro (plano inválido, SID errada, sem ATIS) volta como **REVERT TO VOICE**: o piloto chama o Tráfego na frequência.
    - Se o piloto não aceitar em tempo razoável, considere a autorização não entregue e chame por voz.

!!! info "Decolagem de interseção no pedido de autorização"
    O piloto **deve informar já ao pedir a autorização** se não puder decolar das interseções previstas (veja [Pontos de decolagem](#pontos-de-decolagem)). No DCL, isso vai no campo livre do pedido[^ad20-1-2].

[^ad20-7]: [AIP Brasil, AD 2 SBGR 2.20, item 7.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-1-2]: [AIP Brasil, AD 2 SBGR 2.20, itens 1.2.3.5 e 1.2.3.6](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-map-marker-radius: Áreas de responsabilidade

<figure markdown="span">
  ![Mapa de SBGR com a faixa das pistas em amarelo, sob a Torre, e o restante em azul, sob o Solo](img/sbgr-responsabilidade.svg){ loading=lazy }
  <figcaption>Faixa amarela: Torre. Área azul: Solo. A linha tracejada passa pelos pontos de espera.</figcaption>
</figure>

A divisão segue os **pontos de espera das pistas**. Tudo que fica entre os pontos de espera ao norte da 10L/28R e ao sul da 10R/28L é da Torre.

| Posição | Responsável por |
| :--- | :--- |
| **GND** | Pátios 1 a 10, TWY **A** e **B**, taxilanes Y, TWY V e M e as ligações (G, H, I, J, K, L, N, O, P, Q) **até o ponto de espera da 10L/28R**. Ao sul: pátios 12 e 13 e TWY S, T e U **até o ponto de espera da 10R/28L** |
| **TWR** | As duas pistas, todos os **cruzamentos**, as saídas rápidas **BB, CC, DD, FF** e as TWY **entre as pistas** (C, D, E e os trechos de G, BB, CC e O entre a 10L e a 10R) |

**Pontos de transferência** (números no mapa):

1. **Chegada pela 10R/28L com destino aos pátios norte:** a aeronave segue na frequência da Torre, aguarda e cruza a 10L/28R com autorização da Torre e **só chama o Solo depois de cruzar e livrar a 10L/28R**[^ad20-1-2-4].
2. **Saída:** o Solo transfere a aeronave para a Torre **antes do ponto de espera** da pista de decolagem. Para aliviar a frequência, o Solo pode mandar **monitorar** a Torre, sem chamada inicial[^ad20-6].
3. **Chegada com destino aos pátios 12 e 13:** a aeronave livra a 10R/28L pelo lado sul (T ou U) e chama o Solo depois de livrar a pista.

!!! warning "Cruzamento da pista adjacente"
    - Aeronave que livra uma pista **NUNCA** cruza a pista paralela sem autorização específica do ATC.
    - Aeronave aguardando para cruzar fica na frequência da **Torre** e **não pede** cruzamento: a Torre chama.
    - Uma vez autorizada, o cruzamento deve ser rápido. Não é permitido táxi monomotor antes de cruzar[^ad20-1-2-4].

[^ad20-1-2-4]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2.4](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-6]: [AIP Brasil, AD 2 SBGR 2.20, item 6.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-transit-connection-variant: Fluxo de solo

!!! abstract "Regra geral"
    - **TWY A** é o caminho padrão de deslocamento, nos dois sentidos, entre os pátios e as cabeceiras.
    - **TWY B** é a **alternativa**: use quando a A estiver ocupada ou interditada, para ultrapassar uma aeronave parada ou para separar fluxos em sentidos opostos.
    - As ligações entre A, B e a pista (G, H, L, N, O, P, Q) servem de entrada e saída. As saídas rápidas BB, CC, DD e FF são **só de saída de pista**.

=== "Configuração 10 (pousos 10R, decolagens 10L)"

    <figure markdown="span">
      ![Fluxo de solo na configuração 10: decolagens pela TWY A para G e H; pousos na 10R saindo por BB, CC ou O e cruzando a 10L por L, N ou O](img/sbgr-fluxo-10.svg){ loading=lazy }
      <figcaption>Verde: decolagens, da saída do pátio até a pista. Azul: pousos. Barra vermelha: espera obrigatória antes de cruzar a pista. Laranja tracejado: alternativa pela TWY B.</figcaption>
    </figure>

    - **Decolagens (10L):** táxi pela **A** para oeste até **G** (cabeceira) ou **H** (interseção).
    - **Pousos (10R):** CAT C, D e E livram por **BB**, **CC** ou **O** (fim da pista), aguardam antes da 10L e cruzam por **L**, **N** ou **O** para a A. CAT A e B livram por **T** ou **U**, ao sul.
    - **Pátios 12 e 13:** pela **S** até a **G**, cruzando a 10R com autorização da Torre, até o ponto de espera da 10L na G.
    - **Alternativa:** **B** para oeste até H ou G.

    Exemplo: `TAM3456, táxi para o ponto de espera da pista 10L via A, G.`

=== "Configuração 28 (pousos 28L, decolagens 28R)"

    <figure markdown="span">
      ![Fluxo de solo na configuração 28: decolagens pela TWY A para Q e P; pousos na 28L saindo por G e cruzando a 10L por G](img/sbgr-fluxo-28.svg){ loading=lazy }
      <figcaption>Verde: decolagens, da saída do pátio até a pista. Azul: pousos. Barra vermelha: espera obrigatória antes de cruzar a pista. Laranja tracejado: alternativa pela TWY B.</figcaption>
    </figure>

    - **Decolagens (28R):** táxi pela **A** para leste até **Q** (cabeceira), **P** ou **O** (interseções).
    - **Pousos (28L):** CAT C, D e E livram por **G**, aguardam antes da 10L e cruzam por **G** para a A. CAT A e B livram por **T** ou **U**, ao sul.
    - **Pátios 12 e 13:** pela **S** até a **G**, cruzando a 10R e a 10L com autorização da Torre, e depois pela **A**.
    - **Alternativa:** **B** para leste até P ou Q.

    Exemplo: `GLO1234, táxi para o ponto de espera da pista 28R via A, Q.`

### Saídas de pista

Para garantir o tempo mínimo de ocupação de pista (MROT), o piloto deve livrar pelas TWY abaixo ou avisar a Torre **no primeiro contato** se não puder[^ad20-1-2-2].

| Pista | CAT A e B | CAT C e D | CAT E |
| :---: | :--- | :--- | :--- |
| **10R** | T (1497 m) ou U (1795 m) | BB ou CC (2450 m) ou O (3000 m, fim da pista) | BB, CC ou O |
| **10L** | L (1061 m) | N (2212 m) ou O (2397 m) | N, O ou FF (2840 m) |
| **28R** | O (1155 m) ou N (1340 m) | L (1951 m) ou DD (2340 m) | L ou DD |
| **28L** | T (1502 m) ou U (1204 m) | G (2487 m) | G |

<small>Distância da cabeceira até a TWY de saída.</small>

### Restrições de táxi

- **TWY S, T e U:** envergadura acima de 44 m só rebocada[^ad20-12].
- **Código F:** proibido táxi pela A entre G e o pátio 1, pelas taxilanes Y dos pátios 1 a 5, pelas TWY M e V e pela G entre a 10R/28L e o pátio 12. TWY V e A entre G e o pátio 1: envergadura máxima 65 m[^ad20-12].
- Curva proibida onde não houver sinalização horizontal e iluminação correspondentes[^ad20-1-2-4].
- **Baixa visibilidade (RVR < 400 m):** táxi com viatura *Siga-me* conforme o AIP, pelas rotas padronizadas[^ad20-16].

[^ad20-1-2-2]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2.2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-12]: [AIP Brasil, AD 2 SBGR 2.20, item 12](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e AD 2.8.
[^ad20-16]: [AIP Brasil, AD 2 SBGR 2.20, item 16](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-airplane-takeoff: Pontos de decolagem

<figure markdown="span">
  ![Visão geral de SBGR com pátios numerados e os pontos de decolagem marcados com a TORA disponível](img/sbgr-visao-geral.svg){ loading=lazy }
  <figcaption>Pontos de decolagem (roxo) com a TORA disponível. Números em círculo: pátios.</figcaption>
</figure>

Aeronaves **categoria D ou menores** devem estar configuradas para decolar das interseções abaixo[^ad20-1-2-3]. Na prática, a Torre usa a interseção para encaixar a decolagem entre pousos.

| Pista | Ponto | TORA | Quem usa |
| :---: | :---: | :---: | :--- |
| **10L** | **G** (cabeceira) | 3700 m | Pátios 1 e 2, CAT E e quem não aceitar a interseção |
| **10L** | **H** | **3400 m** | Aeronaves vindas dos **pátios 3, 4, 5, 6 e 7** |
| **28R** | **Q** (cabeceira) | 3700 m | CAT E e quem não aceitar a interseção |
| **28R** | **P** | **3460 m** | CAT D ou menor |
| **28R** | **O** | **2397 m** | CAT D ou menor |
| **10R** | **G** | **2487 m** | Decolagens paralelas dependentes (ver abaixo) |

- O piloto informa **ao pedir a autorização** se não puder decolar da interseção[^ad20-1-2].
- O piloto chega ao ponto de espera **pronto para decolar**; se não estiver, avisa o Solo.
- Alinhamento **imediato** quando autorizado, e corrida iniciada em até **10 segundos** após a autorização de decolagem.
- A TWR **não informa** hora de pouso e decolagem[^ad22-8].

[^ad20-1-2-3]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2.3](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad22-8]: [AIP Brasil, AD 2 SBGR 2.22, item 8.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-call-split: Operação segregada

Na **operação segregada** a 10R/28L recebe os pousos e a 10L/28R as decolagens **ao mesmo tempo**. Como as pistas estão a 375 m uma da outra, a arremetida de quem pousa e a decolagem da pista ao lado podem se cruzar. Por isso a separação entre elas é **visual**, mantida pelo piloto da aeronave que arremete[^ad20-3].

**Condições para usar**[^ad20-3]:

| Condição | Valor |
| :--- | :--- |
| Meteorologia | **VMC**, teto ≥ **1000 pés** e visibilidade ≥ **5000 m** |
| Divergência | Trajetórias de decolagem e de aproximação perdida divergentes em pelo menos **15°** |
| Esteira na final | A aeronave na aproximação final **não** pode ser **PESADA** |
| Esteira na decolagem pela 28 | A aeronave decolando da RWY 28 **não** pode ser **PESADA** |
| Divulgação | Operação em andamento e IAC em uso informadas no **ATIS** (ou em VHF, sem ATIS) |

Fora dessas condições não há operação segregada: a Torre separa pousos e decolagens das duas pistas sem contar com a separação visual.

**O piloto em comando deve**[^ad20-3]:

1. Avisar a TWR se **perder as referências visuais** na final. Sem aviso, o ATC entende que ele tem referências visuais abaixo de 1000 pés e aplicará separação visual em caso de arremetida.
2. Em arremetida, **manter separação visual** com a aeronave decolando da pista ao lado.
3. Manter a outra aeronave à vista até ela deixar de ser tráfego essencial.
4. Observar a separação de esteira quando instruído a manter separação visual e pedir espaçamento adicional se julgar necessário.
5. Incluir **PESADA** ou **SUPER** logo após o indicativo no contato inicial, se aplicável.

**Fraseologia em caso de arremetida**[^ad20-3]:

=== "Português"
    Para a aeronave **arremetendo**:

    ```
    PTATC, tráfego, B757 decolando da pista 10L, mantenha separação visual, atento à esteira de turbulência.
    ```

    Para a aeronave **decolando**:

    ```
    PTATC, tráfego, B757 arremetendo da pista 28L, mantenha separação visual, atento à esteira de turbulência.
    ```

=== "Inglês"
    To the aircraft **going around**:

    ```
    PTATC, traffic, B757 departing runway 10L, maintain visual separation, caution wake turbulence.
    ```

    To the **departing** aircraft:

    ```
    PTATC, traffic, B757 going around runway 28L, maintain visual separation, caution wake turbulence.
    ```

### Decolagens paralelas dependentes

Quando há mais decolagens que pousos, a Torre pode decolar pelas **duas pistas** (10R/10L ou 28L/28R)[^ad20-5]:

- Mínimos: visibilidade ≥ **5000 m** e teto ≥ **1000 pés**.
- Trajetórias de decolagem divergentes em pelo menos **15°** até 2 NM do fim da pista.
- Operação divulgada no **ATIS**.
- O piloto avisa na autorização se não puder operar na 10R/28L e, código C ou D, ao pedir táxi se não puder decolar de **H** (10L), **G** (10R) ou **P** (28R). No primeiro contato com o Controle São Paulo, informa a pista de decolagem.

[^ad20-3]: [AIP Brasil, AD 2 SBGR 2.20, item 3](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-5]: [AIP Brasil, AD 2 SBGR 2.20, item 5](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

---

## :material-arrow-collapse-horizontal: RRSM

**RRSM** (*Reduced Runway Separation Minima*) é a separação mínima reduzida entre aeronaves **na mesma pista**. Com RRSM, a Torre pode autorizar um pouso ou decolagem **antes de a aeronave precedente livrar a pista**, desde que haja razoável certeza de que a distância abaixo será mantida. SBGR foi o primeiro aeródromo do Brasil a usá-la[^ad20-4].

**Condições (todas)**[^ad20-4]:

- Do **nascer ao pôr do sol**.
- Visibilidade ≥ **5 km** e teto ≥ **1000 pés**.
- Vento de cauda **até 3 kt**.
- Ação de frenagem **não afetada** por contaminantes (água, gelo, neve).
- Mínimos de **esteira de turbulência** aplicados normalmente.
- RRSM informada no **ATIS**.

**Distância mínima: 2400 m da cabeceira**, que corresponde a:

| Pista em uso | Pouso após pouso | Pouso após decolagem / decolagem após decolagem |
| :---: | :--- | :--- |
| **10R** | Precedente passou a **CC**, em movimento e vai livrar sem recuo | Precedente passou a **CC** |
| **28L** | Precedente passou a **G**, em movimento e vai livrar sem recuo | Precedente passou a **G** |
| **10L** | Precedente passou a **O**, em movimento e vai livrar sem recuo | Precedente passou a **O** |
| **28R** | Precedente passou a **DD**, em movimento e vai livrar sem recuo | Precedente passou a **DD** |

A Torre dá **informação de tráfego** junto com a autorização:

=== "Português"
    ```
    TAM3456, autorizado pouso pista 10R, vento 090 graus 11 nós, B747 à frente liberando a pista.
    TAM3456, autorizado pouso pista 28L, vento 230 graus 6 nós, MD11 à frente decolando.
    GLO1234, autorizado decolagem pista 28R, vento 230 graus 6 nós, MD11 à frente decolando.
    ```

=== "Inglês"
    ```
    TAM3456, runway 10R cleared to land, wind 090 degrees 11 knots, B747 ahead vacating the runway.
    TAM3456, runway 28L cleared to land, wind 230 degrees 6 knots, MD11 departing ahead.
    GLO1234, runway 28R cleared for takeoff, wind 230 degrees 6 knots, MD11 departing ahead.
    ```

[^ad20-4]: [AIP Brasil, AD 2 SBGR 2.20, item 4.2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip). Ver também a [notícia do DECEA](https://decea.mil.br/?i=midia-e-informacao&materia=aeroporto-de-guarulhos-e-o-primeiro-do-brasil-a-implementar-minimos-de-separacao-reduzidos-entre-aeronaves-que-utilizam-a-mesma-pista&p=pg_noticia).

---

## :material-sign-direction: Pátios e companhias

Referência para a simulação, montada a partir da distribuição real dos terminais. Não é a alocação oficial do aeroporto, que muda a cada temporada. **VAs** usam os pátios da companhia real que representam.

<div class="patios">
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 1"><small>Pátio</small>1</span><span class="patio__info"><strong>Terminal 1</strong><span>Doméstico</span><span class="patio__pos">Posições 101 a 105</span></span></header>
<div class="patio__cias"><figure class="cia" title="Azul (AZU)"><img class="off-glb" src="https://pics.avs.io/240/80/AD.png" alt="Azul" loading="lazy"><figcaption>AZU</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 2·3"><small>Pátio</small>2·3</span><span class="patio__info"><strong>Terminal 2</strong><span>Doméstico e internacional regional</span><span class="patio__pos">Posições 201 a 212 · 301 a 312</span></span></header>
<div class="patio__cias"><figure class="cia" title="GOL (GLO)"><img class="off-glb" src="https://pics.avs.io/240/80/G3.png" alt="GOL" loading="lazy"><figcaption>GLO</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 4"><small>Pátio</small>4</span><span class="patio__info"><strong>Terminal 2</strong><span>Doméstico e América do Sul</span><span class="patio__pos">Posições 401 a 411</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="Aerolíneas Argentinas (ARG)"><img class="off-glb" src="https://pics.avs.io/240/80/AR.png" alt="Aerolíneas Argentinas" loading="lazy"><figcaption>ARG</figcaption></figure><figure class="cia" title="Avianca (AVA)"><img class="off-glb" src="https://pics.avs.io/240/80/AV.png" alt="Avianca" loading="lazy"><figcaption>AVA</figcaption></figure><figure class="cia" title="BoA (BOV)"><img class="off-glb" src="https://pics.avs.io/240/80/OB.png" alt="BoA" loading="lazy"><figcaption>BOV</figcaption></figure><figure class="cia" title="Arajet (DWI)"><img class="off-glb" src="https://pics.avs.io/240/80/DM.png" alt="Arajet" loading="lazy"><figcaption>DWI</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 1"><small>Pátio</small>1</span><span class="patio__info"><strong>Terminal de cargas</strong><span>Cargueiros</span><span class="patio__pos">Posições 106 a 115</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM Cargo (LCO)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM Cargo" loading="lazy"><figcaption>LCO</figcaption></figure><figure class="cia" title="Lufthansa Cargo (GEC)"><img class="off-glb" src="https://pics.avs.io/240/80/LH.png" alt="Lufthansa Cargo" loading="lazy"><figcaption>GEC</figcaption></figure><figure class="cia" title="Cargolux (CLX)"><img class="off-glb" src="https://pics.avs.io/240/80/CV.png" alt="Cargolux" loading="lazy"><figcaption>CLX</figcaption></figure><figure class="cia" title="Atlas Air (GTI)"><img class="off-glb" src="https://pics.avs.io/240/80/5Y.png" alt="Atlas Air" loading="lazy"><figcaption>GTI</figcaption></figure><figure class="cia" title="Qatar Airways Cargo (QTR)"><img class="off-glb" src="https://pics.avs.io/240/80/QR.png" alt="Qatar Airways Cargo" loading="lazy"><figcaption>QTR</figcaption></figure><figure class="cia" title="Turkish Cargo (THY)"><img class="off-glb" src="https://pics.avs.io/240/80/TK.png" alt="Turkish Cargo" loading="lazy"><figcaption>THY</figcaption></figure><figure class="cia" title="Emirates SkyCargo (UAE)"><img class="off-glb" src="https://pics.avs.io/240/80/EK.png" alt="Emirates SkyCargo" loading="lazy"><figcaption>UAE</figcaption></figure><figure class="cia" title="Total (TTL)"><span class="cia__texto">Total</span><figcaption>TTL</figcaption></figure></div>
</section>
<section class="patio patio--largo">
<header class="patio__cab"><span class="patio__num" title="Pátio 5·6"><small>Pátio</small>5·6</span><span class="patio__info"><strong>Terminal 3</strong><span>Internacional</span><span class="patio__pos">Posições 501 a 511 · 601 a 612</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="American Airlines (AAL)"><img class="off-glb" src="https://pics.avs.io/240/80/AA.png" alt="American Airlines" loading="lazy"><figcaption>AAL</figcaption></figure><figure class="cia" title="Delta (DAL)"><img class="off-glb" src="https://pics.avs.io/240/80/DL.png" alt="Delta" loading="lazy"><figcaption>DAL</figcaption></figure><figure class="cia" title="United (UAL)"><img class="off-glb" src="https://pics.avs.io/240/80/UA.png" alt="United" loading="lazy"><figcaption>UAL</figcaption></figure><figure class="cia" title="Air France (AFR)"><img class="off-glb" src="https://pics.avs.io/240/80/AF.png" alt="Air France" loading="lazy"><figcaption>AFR</figcaption></figure><figure class="cia" title="KLM (KLM)"><img class="off-glb" src="https://pics.avs.io/240/80/KL.png" alt="KLM" loading="lazy"><figcaption>KLM</figcaption></figure><figure class="cia" title="Lufthansa (DLH)"><img class="off-glb" src="https://pics.avs.io/240/80/LH.png" alt="Lufthansa" loading="lazy"><figcaption>DLH</figcaption></figure><figure class="cia" title="British Airways (BAW)"><img class="off-glb" src="https://pics.avs.io/240/80/BA.png" alt="British Airways" loading="lazy"><figcaption>BAW</figcaption></figure><figure class="cia" title="Iberia (IBE)"><img class="off-glb" src="https://pics.avs.io/240/80/IB.png" alt="Iberia" loading="lazy"><figcaption>IBE</figcaption></figure><figure class="cia" title="TAP (TAP)"><img class="off-glb" src="https://pics.avs.io/240/80/TP.png" alt="TAP" loading="lazy"><figcaption>TAP</figcaption></figure><figure class="cia" title="Emirates (UAE)"><img class="off-glb" src="https://pics.avs.io/240/80/EK.png" alt="Emirates" loading="lazy"><figcaption>UAE</figcaption></figure><figure class="cia" title="Qatar Airways (QTR)"><img class="off-glb" src="https://pics.avs.io/240/80/QR.png" alt="Qatar Airways" loading="lazy"><figcaption>QTR</figcaption></figure><figure class="cia" title="Turkish Airlines (THY)"><img class="off-glb" src="https://pics.avs.io/240/80/TK.png" alt="Turkish Airlines" loading="lazy"><figcaption>THY</figcaption></figure><figure class="cia" title="Ethiopian (ETH)"><img class="off-glb" src="https://pics.avs.io/240/80/ET.png" alt="Ethiopian" loading="lazy"><figcaption>ETH</figcaption></figure><figure class="cia" title="Air Canada (ACA)"><img class="off-glb" src="https://pics.avs.io/240/80/AC.png" alt="Air Canada" loading="lazy"><figcaption>ACA</figcaption></figure><figure class="cia" title="Aeroméxico (AMX)"><img class="off-glb" src="https://pics.avs.io/240/80/AM.png" alt="Aeroméxico" loading="lazy"><figcaption>AMX</figcaption></figure><figure class="cia" title="Copa (CMP)"><img class="off-glb" src="https://pics.avs.io/240/80/CM.png" alt="Copa" loading="lazy"><figcaption>CMP</figcaption></figure></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 7"><small>Pátio</small>7</span><span class="patio__info"><strong>Remoto</strong><span>Pernoite, charters e excedente de wide-bodies</span><span class="patio__pos">Posições 701 a 715</span></span></header>
<div class="patio__cias"><p class="patio__nota">Qualquer companhia, conforme a disponibilidade.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 9"><small>Pátio</small>9</span><span class="patio__info"><strong>Remoto, junto aos hangares</strong><span>Pernoite e manutenção</span><span class="patio__pos">Posições 901 a 911</span></span></header>
<div class="patio__cias"><figure class="cia" title="LATAM (TAM)"><img class="off-glb" src="https://pics.avs.io/240/80/LA.png" alt="LATAM" loading="lazy"><figcaption>TAM</figcaption></figure><figure class="cia" title="American Airlines (AAL)"><img class="off-glb" src="https://pics.avs.io/240/80/AA.png" alt="American Airlines" loading="lazy"><figcaption>AAL</figcaption></figure><p class="patio__nota">e excedente dos demais pátios.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 12"><small>Pátio</small>12</span><span class="patio__info"><strong>Aviação geral</strong><span>Executiva, táxi aéreo e helicópteros</span><span class="patio__pos">Posições 1 a 12 · H1 a H3</span></span></header>
<div class="patio__cias"><p class="patio__nota">Aviação geral e táxi aéreo, com autorização prévia.</p></div>
</section>
<section class="patio">
<header class="patio__cab"><span class="patio__num" title="Pátio 13"><small>Pátio</small>13</span><span class="patio__info"><strong>BASP</strong><span>Militar · Base Aérea de São Paulo</span></span></header>
<div class="patio__cias"><figure class="cia" title="Força Aérea Brasileira (FAB)"><span class="cia__texto">FAB</span></figure></div>
</section>
</div>

- **Aviação geral** só estaciona no pátio 12, com autorização prévia da administração; permanência máxima de 3 h (internacional) ou 2 h (doméstico)[^ad20-8].
- **Militares** com destino à BASP (pátio 13) chamam **Operações Guarulhos (122.500)**[^ad20-8].
- **SBGR não é alternativa** para voos planejados para SBSP, SBKP ou outros aeródromos da TMA-SP, por capacidade de pátio, exceto militares ou com coordenação[^ad22-8].

<small>Logos via [Travelpayouts](https://pics.avs.io), exibidas da fonte original. As marcas pertencem às respectivas companhias.</small>

[^ad20-8]: [AIP Brasil, AD 2 SBGR 2.20, item 8](https://aisweb.decea.mil.br/?i=publicacoes&p=aip) e AD 2.8.

---

## :material-clipboard-text-outline: Outros procedimentos

### Aproximações e pousos

- **HIRO** (operação de pista de alta intensidade) H24: o piloto ajusta pouso e decolagem para o menor tempo de ocupação de pista[^ad20-1-2-1].
- **Velocidades na aproximação:** **180 kt a 10 NM** e **160 kt a 5 NM** da cabeceira. Velocidade atribuída pelo ATC é obrigatória; quem não puder cumprir avisa[^ad20-2].
- Separação mínima de vigilância na final: **3 NM**[^ad20-4].
- Livrar a pista **completamente** antes de parar.
- Os pilotos **não reportam** trem baixado, exceto em emergência.

### Comunicações

- Para evitar congestionamento, o ATC pode mandar **monitorar** a próxima frequência. Nesse caso, **não** há chamada inicial[^ad20-6].
- Plano de voo e suas alterações **não** são aceitos por radiotelefonia[^ad23].

### Regulamentos do aeródromo

- VFR de asa fixa **proibido**, exceto militares brasileiras ou aeronaves não RNAV quando os procedimentos convencionais estiverem indisponíveis[^ad22].
- Proibidos pousos e decolagens de **turboélices e pistão** entre **0930–1300 UTC e 2200–0200 UTC**, exceto militares, MEDEVAC e RBAC 121/129[^ad20-8].
- Proibidos voos de treinamento, exceto militares da BASP e treinamento ILS CAT II/III autorizado[^ad20-13].

[^ad20-1-2-1]: [AIP Brasil, AD 2 SBGR 2.20, item 1.2](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-2]: [AIP Brasil, AD 2 SBGR 2.20, item 2.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad20-13]: [AIP Brasil, AD 2 SBGR 2.20, item 13](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad17]: [AIP Brasil, AD 2 SBGR 2.17](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad22]: [AIP Brasil, AD 2 SBGR 2.22, item 1.1](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).
[^ad23]: [AIP Brasil, AD 2 SBGR 2.23](https://aisweb.decea.mil.br/?i=publicacoes&p=aip).

<small>Diagramas desenhados pela VATSIM Brasil sobre a geometria do [OpenStreetMap](https://www.openstreetmap.org/copyright) (ODbL), conferida com a carta ADC SBGR (AIRAC 2605). Não use para navegação real. Fonte normativa: AIP Brasil, AD 2 SBGR, AMDT 2610A1.</small>
