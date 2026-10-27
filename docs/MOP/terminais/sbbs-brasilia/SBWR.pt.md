---
title: SBWR - Brasília
tags:
  - Terminal
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Brasília |
| **Posição** | `SBWR_APP` |
| **Indicativo** | Controle Brasília |
| **Frequência** | **119.200** MHz[^pacote] |
| **Vigilância ATS** | Radar |
| **Aeródromos na TMA** | [SBBR](../../aerodromos/sbbs-brasilia/twr/SBBR.pt.md) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Use as abas acima: **Cartas Aeronáuticas** traz as cartas da TMA, **Carta Visual** traz a carta visual da AISWEB, **Meteorologia** mostra o mapa meteorológico da área e **Tráfego VATSIM** abre o tráfego no aeródromo principal (SBBR).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWR?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Carta Visual"
    [:material-open-in-new: Abrir em nova aba](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf){ .md-button .md-button--primary target="_blank" }

    <div class="pdf-embed"><iframe class="pdf-iframe" src="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf#view=FitH" loading="lazy" title="PDF"></iframe></div>

    Fonte: [AISWEB](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf){ target="_blank" }.

=== ":material-weather-partly-cloudy: Meteorologia"
    <div class="tma-meteo" data-lat="-15.873" data-lon="-48.004" data-zoom="8" data-lang="pt"></div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBBR){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

A camada **Corredores visuais (REA)** mostra as 5 REA da AIC N 10/17 e os portões (em amarelo). Os trechos de mão única têm uma seta no sentido do voo; nos de mão dupla, a altitude depende do sentido. Clique em um trecho para ver o rumo e a altitude. Detalhes em [Corredores visuais (REA)](#corredores-visuais-rea).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| TMA Brasília | 6500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Brasília | GND – 6500 FT | <span class="classe-badge classe-c">C</span> |
| ATZ Brasília | GND – 5500 FT | — |

## :material-view-grid-outline: Setorização do APP

A AIP divide o APP Brasília em oito setores[^amdt]. Os setores **01 a 04** formam o anel externo da TMA, de 6500 pés ao FL195, um por quadrante. Os setores **05 a 08** são o miolo: quatro quadrantes que se encontram sobre SBBR, publicados do **GND a 6500 pés**, ou seja, a CTR Brasília, que no mundo real também é do APP. Os setores 05 e 07 ficam com as saídas para o norte (120.650, *TKOF NORTE*) e os 06 e 08 com as saídas para o sul (129.150, *TKOF SUL*). Ligue a camada **Setores do APP (AIP)** no mapa para vê-los.

No pacote, o APP **não é setorizado**: `SBWR_APP` (**119.200**) responde por todos os setores. A setorização serve para entender os fluxos, não para dividir posições na VATSIM.

Escolha a área na lista: o setor total ou um setor da AIP. A área está preenchida, com os limites verticais abaixo do nome; o resto da TMA aparece em cinza.

<div class="setor-viewer" data-lang="pt" markdown="block">
<figure data-grupo="total" data-titulo="SBWR_APP" data-info="119.200 · toda a TMA" markdown="span">
  ![SBWR_APP: toda a TMA Brasília](img/sbwr-comb-app.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="01" data-info="6500 FT – FL195" markdown="span">
  ![Setor 01 do APP Brasília, de 6500 FT – FL195](img/sbwr-setor-01.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="02" data-info="6500 FT – FL195" markdown="span">
  ![Setor 02 do APP Brasília, de 6500 FT – FL195](img/sbwr-setor-02.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="03" data-info="6500 FT – FL195" markdown="span">
  ![Setor 03 do APP Brasília, de 6500 FT – FL195](img/sbwr-setor-03.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="04" data-info="6500 FT – FL195" markdown="span">
  ![Setor 04 do APP Brasília, de 6500 FT – FL195](img/sbwr-setor-04.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="05" data-info="GND – 6500 FT" markdown="span">
  ![Setor 05 do APP Brasília, de GND – 6500 FT](img/sbwr-setor-05.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="06" data-info="GND – 6500 FT" markdown="span">
  ![Setor 06 do APP Brasília, de GND – 6500 FT](img/sbwr-setor-06.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="07" data-info="GND – 6500 FT" markdown="span">
  ![Setor 07 do APP Brasília, de GND – 6500 FT](img/sbwr-setor-07.svg){ loading=lazy }
</figure>

<figure data-grupo="elem" data-titulo="08" data-info="GND – 6500 FT" markdown="span">
  ![Setor 08 do APP Brasília, de GND – 6500 FT](img/sbwr-setor-08.svg){ loading=lazy }
</figure>

</div>

| Setor | Limites | Frequência (AIP) | Função |
| :---: | --- | :---: | --- |
| **01** | 6500 FT – FL195 | 120.000 | **Setor externo** oeste e noroeste |
| **02** | 6500 FT – FL195 | 120.300 | **Setor externo** norte e nordeste |
| **03** | 6500 FT – FL195 | 119.500 | **Setor externo** leste e sudeste |
| **04** | 6500 FT – FL195 | 129.600 | **Setor externo** sul e sudoeste |
| **05** | GND – 6500 FT | 119.200 · 120.650 | **Miolo noroeste**, saídas para o norte |
| **06** | GND – 6500 FT | 119.700 · 129.150 | **Miolo sudoeste**, saídas para o sul |
| **07** | GND – 6500 FT | 119.200 · 120.650 | **Miolo nordeste**, saídas para o norte |
| **08** | GND – 6500 FT | 119.700 · 129.150 | **Miolo sudeste**, saídas para o sul |

A AIP lista ainda **121.150** como frequência primária do VFR em quase todos os setores.

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBWR_APP** | `WR` | Controle Brasília | **119.200** |  |
| **SBBR_TWR** | `TBR` | Torre Brasília | **118.100** |  |

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
        p0["SBBS_CTR"]:::ctr
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_NE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_NS_CTR</span>"]:::grpctr
        p1["SBBS_N_CTR"]:::ctr
        p2["SBWR_APP"]:::app
        p3["SBBR_TWR"]:::twr
        a0(["TMA Brasília"]):::esp --> p2
        a1(["CTR Brasília<br>ATZ Brasília"]):::esp --> p3
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
    - **Circular:** [AIC N 10/17 – Rotas Especiais de Aeronaves em Voo Visual na Área Terminal de Brasília](https://publicacoes.decea.mil.br/publicacao/aic-n-1017){ target="_blank" } (em vigor desde 20 JUL 2017)
    - **Carta visual – Rotas de aeronaves (REA):** [CCV REA WR-Brasília](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wr-brasilia_rea_20240125.pdf){ target="_blank" } (25 JAN 2024)

    A carta está embutida na aba **Carta Visual** em **Informações Úteis**. Os dados desta seção vêm da AIC N 10/17[^aic1017]; a carta traz os mesmos pontos e altitudes.

### Camadas da TMA e quem atende o VFR

| Espaço | Limites | Classe | VFR |
| --- | --- | :---: | --- |
| **TMA Brasília** | 6500 FT – FL195 | <span class="classe-badge classe-c">C</span> até FL145, <span class="classe-badge classe-a">A</span> acima | Com autorização do APP até o FL145; acima, classe A, não há VFR |
| **CTR Brasília** | GND – 6500 FT | <span class="classe-badge classe-c">C</span> | Só pelas REA, salvo autorização do APP |
| **ATZ Brasília** | GND – 5500 FT | — | Circuito de SBBR, com a Torre; entrada só com autorização do APP |
| **REA** | 4500 ou 5000 FT | <span class="classe-badge classe-g">G</span> | Corredores dentro da CTR; a AIC classifica o espaço deles como classe G |

- **Corredores obrigatórios na CTR:** todo VFR na projeção da CTR Brasília voa pelas REA. Ele pode entrar ou sair delas em qualquer ponto previsto no plano de voo; outra trajetória, só com autorização do APP.
- **Contato com o APP:** mesmo com as REA em classe G, o piloto faz o primeiro contato com o APP **antes de entrar** nos corredores, se possível, e mantém escuta permanente. Depois, fala só quando necessário ou quando chamado.
- **No mundo real**, a AIC manda o VFR nas REA usar **120.650**; a AIP atual lista **121.150** como frequência primária do VFR no APP Brasília. A coordenação entre aeronaves nas REA é na frequência livre **123.450**, ou na frequência de coordenação (FCA) do aeródromo, quando houver.
- **No pacote**, só existe `SBWR_APP` (**119.200**), que atende todo o VFR das REA. O piloto chama a posição **on-line**, não a frequência do mundo real. Sem o APP, quem assume é a próxima posição na [cobertura](#cobertura-top-down). A coordenação ar-ar fica na **UNICOM 122.800**.

### Regras gerais para o VFR

- **Plano de voo:** quem decola de aeródromo controlado põe `REA` no item 15 e os corredores no item 18 (ex.: `BRAVO, CHARLIE`). No primeiro voo nas REA, avise o APP. Quem vem de aeródromo sem órgão ATS informa no primeiro contato a procedência, o destino e as REA que vai usar.
- **Referências à esquerda:** o piloto voa deixando as referências visuais do corredor à **esquerda**.
- **Largura:** 3 NM em toda a extensão (1,5 NM para cada lado do eixo).
- **Altitudes:** **4500 ou 5000 pés**, conforme o trecho e o sentido, mantidas de preferência em toda a fase em rota. Nos trechos de mão dupla, a altitude separa os dois sentidos.
- **QNH** de Brasília, dado pelo APP ou copiado do ATIS de SBBR.
- **Faróis** de pouso e táxi acesos, de dia e de noite. **Transponder** modo A/C ou S obrigatório.
- **Esperas:** para espaçar a entrada na CTR, o APP pode mandar esperar sobre os pontos de referência das REA.
- **Helicópteros** também podem usar as REA.
- **IMC:** sem condições de seguir em VMC, voltar e pousar no aeródromo de partida ou no mais próximo, pedir VFR especial ou pedir mudança para IFR ao APP.

Sem outro código do APP, o VFR na projeção da TMA monta o código do transponder pela origem (dois primeiros dígitos) e pelo destino (dois últimos):

| Aeródromo | Decolando | Destino |
| :---: | :---: | :---: |
| APUB | **21**xx | xx**21** |
| SSGP | **22**xx | xx**22** |
| SIQE | **23**xx | xx**23** |
| SBBR | **24**xx | xx**24** |
| CBAAER | **25**xx | xx**25** |
| SWUZ | **26**xx | xx**26** |
| SWFR | **27**xx | xx**27** |
| Outros aeródromos e helipontos sob a TMA | **31**xx | xx**31** |
| Aeródromos fora da TMA | **32**xx | xx**32** |

Exemplos da AIC: de APUB para SSGP, **2122**; de CBAAER para SWUZ, **2526**.

### Corredores visuais (REA)

As 5 REA da TMA. Altitudes em pés (QNH). **→** é trecho de mão única; **⇄** é de mão dupla, com rumo e altitude no formato **ida / volta**.

| REA | Trecho | Rumo | Altitude |
| :---: | :--- | :---: | :---: |
| **ALFA** | LAGOA BONITA → SOBRADINHO 2 | 271° | 5000 |
|  | SOBRADINHO 2 → BARRAGEM SANTA MARIA | 274° | 5000 |
|  | BARRAGEM SANTA MARIA → ESTRADA | 287° | 5000 |
|  | ESTRADA → PONTA NORTE | 279° | 5000 |
| **BRAVO** | LAGOA 2 ⇄ BARRAGEM SANTA MARIA | 028° / 208° | 5000 / 4500 |
|  | BARRAGEM SANTA MARIA → TORRE 4 | 028° | 5000 |
|  | TORRE 4 → FERCAL | 082° | 5000 |
|  | FERCAL → CIPLAN | 084° | 5000 |
| **CHARLIE** | PONTA SUL → ESTACIONAMENTO | 112° | 5000 |
|  | ESTACIONAMENTO → SÍTIO | 098° | 5000 |
|  | SÍTIO → LAGOA 2 | 107° | 5000 |
| **DELTA** | SARA ⇄ CBAAER | 121° / 301° | 4500 / 5000 |
|  | CBAAER ⇄ GRANJA 1 | 140° / 320° | 4500 / 5000 |
|  | GRANJA 1 ⇄ TORRE 1 | 156° / 336° | 4500 / 5000 |
|  | TORRE 1 ⇄ TORRE 2 | 186° / 006° | 4500 / 5000 |
|  | TORRE 2 ⇄ TORRE 3 | 177° / 357° | 4500 / 5000 |
|  | TORRE 3 ⇄ TORRE TROCO | 195° / 015° | 4500 / 5000 |
|  | TORRE TROCO ⇄ BARRAGEM 1 | 199° / 019° | 4500 / 5000 |
|  | BARRAGEM 1 ⇄ GRANJA 2 | 286° / 106° | 4500 / 5000 |
|  | GRANJA 2 ⇄ ALPHAVILLE | 264° / 084° | 4500 / 5000 |
|  | ALPHAVILLE ⇄ BUNGE | 268° / 088° | 4500 / 5000 |
|  | BUNGE ⇄ TANQUES CAESB | 301° / 121° | 4500 / 5000 |
|  | TANQUES CAESB ⇄ POVOADO SERRA DOURADA | 327° / 147° | 4500 / 5000 |
|  | POVOADO SERRA DOURADA ⇄ TORRE ENGENHO | 299° / 119° | 4500 / 5000 |
| **ECHO** | BUNGE ⇄ ESTUFA VERMELHA | 040° / 220° | 5000 / 4500 |

O que cada corredor faz:

- **ALFA** (mão única, para oeste) sai do portão LAGOA BONITA, a nordeste, passa por Sobradinho e pela Barragem de Santa Maria e termina no portão PONTA NORTE, na ponta norte do Lago do Descoberto. Quem chega pelo nordeste e vai para SBBR desce pela BRAVO na Barragem de Santa Maria.
- **BRAVO** liga o portão LAGOA 2, perto do Quartel do Exército, ao norte. Até a Barragem de Santa Maria é de mão dupla (5000 pés para o norte, 4500 para o sul); dali segue só para o norte e o nordeste, por TORRE 4 e FERCAL, até o portão CIPLAN.
- **CHARLIE** (mão única, para leste) é a entrada pelo oeste: do portão PONTA SUL, na ponta sul do Lago do Descoberto, por ESTACIONAMENTO e SÍTIO, até o portão LAGOA 2.
- **DELTA** é o grande arco de mão dupla pelo leste e pelo sul. Sai do portão SARA (Hospital Sarah Kubitschek), passa por CBAAER e pelas torres ao longo da DF-130 (TORRE 1 a 3 e TORRE TROCO), contorna SBBR e segue para oeste por BARRAGEM 1, GRANJA 2, ALPHAVILLE e BUNGE até o portão TORRE ENGENHO (Agrovila Engenho das Lajes). De SARA para TORRE ENGENHO a **4500 pés**; no sentido contrário, a **5000**.
- **ECHO** liga BUNGE (silos e galpões da Bunge) ao portão ESTUFA VERMELHA, ao norte: 5000 pés subindo para a ESTUFA VERMELHA e 4500 descendo para BUNGE.

**Portões** (entrada e saída das REA): LAGOA BONITA, CIPLAN, PONTA NORTE, PONTA SUL, LAGOA 2, SARA, ESTUFA VERMELHA, GRANJA 2, BUNGE e TORRE ENGENHO.

### Aeródromos sob a TMA

| Aeródromo | Chegada | Saída |
| :---: | :--- | :--- |
| **SBBR** | Aguardar autorização do APP para entrar no circuito. Sem ela a tempo, esperar em condições visuais num ponto das REA; sem contato com o APP, pedir à Torre | Pelas REA, conforme o APP |
| **APUB** | Portões LAGOA 2 ou SARA, ou outro ponto autorizado pelo APP | Para sudoeste, oeste, noroeste, norte e nordeste, pelo portão LAGOA 2; para leste, sudeste e sul, pelo portão SARA |
| **SSGP** | Posições CBAAER ou TORRE 2, ou outro ponto autorizado pelo APP; depois da autorização, aproximação coordenando com quem vai decolar | A 4000 pés, chamando o APP: proa CBAAER para noroeste, norte e nordeste; proa TORRE 3 para os demais setores |
| **SIQE** | Portão GRANJA 2, ou outro ponto autorizado pelo APP | Para SSGP: rumo norte a 4000 pés e, autorizado pelo APP, aproximação coordenando com quem vai decolar |

De SSGP para SIQE: decolar na proa da cidade de São Sebastião, a 4000 pés, e, liberado da frequência pelo APP, coordenar com o tráfego no circuito de SIQE.

### Outras regras

- Não são aceitos planos AFIL, nem plano de voo simplificado por radiotelefonia a partir do solo.
- Helicópteros no setor Sul: altitude mínima de 4100 FT (600 FT AGL).
- Decolagens de aeródromos e helipontos dentro da projeção da ATZ devem chamar a Torre Brasília antes de decolar.

### Fraseologia

Primeiro contato com o APP, antes de entrar no corredor:

```
Controle Brasília, PR-MWN, decolado de CBAAER para Luziânia, 4500 pés, solicita REA DELTA até BUNGE.
```

Chegada a SBBR pela CHARLIE:

```
Controle Brasília, PR-MWN, REA CHARLIE, posição SÍTIO, 5000 pés, proa LAGOA 2, pouso em Brasília.
```

Coordenação entre aeronaves (123.450 no mundo real; UNICOM na VATSIM), com matrícula, posição, sentido ou destino e altitude[^aic1017]:

```
Coordenação, PR-MWN, posição TORRE 2, 4500 pés, proa TORRE 3, REA DELTA.
```

## :material-note-text-outline: Observações

- A TMA é classe A entre FL145 e FL195 e classe C entre 6500 FT e FL145.
- No mundo real há separação mínima de 3 NM dentro de 40 NM de SBBR.
- As ATZs não têm classe publicada na AIP (ENR 2.2).
- No pacote, o APP Brasília não é setorizado: `SBWR_APP` cobre toda a TMA, e a CTR fica com a `SBBR_TWR`.
- Volumes, setores e mapa seguem a AIP, AMDT AIRAC 2612A1 (26 NOV 2026). O pacote de setores da VATSIM pode trazer contornos um pouco diferentes da TMA e da CTR.

---

Voltar para a [visão geral das terminais](index.pt.md) da FIR Brasília.

[^pacote]: Frequência no pacote de setores da VATSIM Brasil.
[^amdt]: AIP Brasil, AMDT AIRAC 2612A1 (26 NOV 2026), ENR 2.1 e ENR 2.2.
[^aic1017]: [AIC N 10/17](https://publicacoes.decea.mil.br/publicacao/aic-n-1017){ target="_blank" }, itens 3 a 5 e Anexo A.

<!--
Daqui pra baixo, é o mapa. Contornos da AIP AMDT 2612A1 (ENR 2.1 e 2.2, 26 NOV 2026), em [longitude, latitude]. A TMA é a união dos setores 01 a 08.
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
    .rea-seta span { display: block; width: 16px; height: 16px; line-height: 16px; text-align: center; color: #c026d3; font-size: 15px; text-shadow: 0 0 2px #fff, 0 0 2px #fff }
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWR", "nome": "TMA Brasília", "posicao": "SBWR_APP", "freq": "119.200", "lim": "6500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-48.541667, -16.099444], [-48.602222, -15.852778], [-48.936111, -15.723056], [-48.946667, -15.671389], [-48.7775, -15.333333], [-48.674722, -15.243056], [-48.401389, -15.049722], [-48.077222, -14.965], [-47.960556, -14.99], [-47.764722, -15.015278], [-47.446111, -15.162778], [-47.140278, -15.436389], [-47.089722, -15.811944], [-47.060556, -16.032222], [-47.242778, -16.388056], [-47.325, -16.486667], [-47.442222, -16.593611], [-47.542222, -16.659444], [-47.780833, -16.735833], [-47.931389, -16.780833], [-48.084167, -16.775556], [-48.298889, -16.742222], [-48.448333, -16.689722], [-48.476944, -16.664722], [-48.644722, -16.548611], [-48.599444, -16.235556]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "CTR Brasília", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – 6500 FT", "classe": "C", "link": "", "contorno": [[-48.438056, -15.641389], [-47.438056, -15.570833], [-47.395, -16.101111], [-48.396667, -16.173611]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "ATZ Brasília", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – 5500 FT", "classe": "—", "link": "", "contorno": [[-48.021944, -15.837778], [-47.988889, -15.806944], [-47.858333, -15.798056], [-47.823056, -15.826667], [-47.816667, -15.912778], [-47.849722, -15.943611], [-47.980278, -15.952778], [-48.015278, -15.924444]]}
];

const limiteFir = [[-50.105463, -22.08634], [-50.4579, -21.6254], [-51.3619, -20.4271], [-52.0114, -19.7046], [-52.7536, -18.9223], [-54.1235, -17.4059], [-53.1008, -16.7092], [-53.3203, -15.8089], [-53.3927, -15.4768], [-53.6267, -14.5625], [-53.5013, -12.96], [-53.051, -12.1836], [-51.672778, -11.0275], [-51.4728, -10.8474], [-51.0866, -10.5156], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.3153, -10.3287], [-46.891, -12.0218], [-45.6083, -13.3218], [-45.278124, -13.796406], [-44.5772, -14.7847], [-44.3306, -15.2179], [-44.095833, -15.626499], [-42.6788, -16.4093], [-42.3377, -16.6247], [-41.8206, -16.9483], [-42.4482, -18.758], [-42.4406, -19.105], [-42.4795, -19.463], [-42.5269, -20.0033], [-42.7521, -20.4117], [-43.3928, -20.1562], [-43.965, -20.5375], [-44.7076, -21.4759], [-45.7749, -22.7993], [-45.8108, -23.0094], [-45.86, -23.2332], [-46.655, -23.6273], [-47.2173, -23.3154], [-47.573, -23.1164], [-47.726084, -23.065083], [-48.832226, -22.69952], [-49.9178, -22.3302]];

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
const setores = [{"posicao": "Setor 01", "rot": "01", "freq": "119.200", "lim": "6500 FT – FL195", "contorno": [[-48.541667, -16.099444], [-48.602222, -15.852778], [-48.936111, -15.723056], [-48.946667, -15.671389], [-48.7775, -15.333333], [-48.674722, -15.243056], [-48.401389, -15.049722], [-48.077222, -14.965], [-47.960556, -14.99], [-47.929444, -15.703889], [-48.308333, -15.73], [-48.296389, -15.893333], [-48.406667, -15.986111]]}, {"posicao": "Setor 02", "rot": "02", "freq": "119.200", "lim": "6500 FT – FL195", "contorno": [[-47.960556, -14.99], [-47.764722, -15.015278], [-47.446111, -15.162778], [-47.140278, -15.436389], [-47.089722, -15.811944], [-47.536111, -15.845], [-47.550278, -15.677778], [-47.929444, -15.703889]]}, {"posicao": "Setor 03", "rot": "03", "freq": "119.200", "lim": "6500 FT – FL195", "contorno": [[-47.089722, -15.811944], [-47.060556, -16.032222], [-47.242778, -16.388056], [-47.325, -16.486667], [-47.442222, -16.593611], [-47.542222, -16.659444], [-47.780833, -16.735833], [-47.905278, -16.037222], [-47.524444, -16.010833], [-47.536111, -15.845]]}, {"posicao": "Setor 04", "rot": "04", "freq": "119.200", "lim": "6500 FT – FL195", "contorno": [[-47.780833, -16.735833], [-47.931389, -16.780833], [-48.084167, -16.775556], [-48.298889, -16.742222], [-48.448333, -16.689722], [-48.476944, -16.664722], [-48.644722, -16.548611], [-48.599444, -16.235556], [-48.541667, -16.099444], [-48.406667, -15.986111], [-48.296389, -15.893333], [-48.283333, -16.063889], [-47.905278, -16.037222]]}, {"posicao": "Setor 05", "rot": "05", "freq": "119.200", "lim": "GND – 6500 FT", "contorno": [[-47.929444, -15.703889], [-47.9175, -15.870833], [-48.296389, -15.893333], [-48.308333, -15.73]]}, {"posicao": "Setor 06", "rot": "06", "freq": "119.200", "lim": "GND – 6500 FT", "contorno": [[-48.296389, -15.893333], [-48.283333, -16.063889], [-47.905278, -16.037222], [-47.9175, -15.870833]]}, {"posicao": "Setor 07", "rot": "07", "freq": "119.200", "lim": "GND – 6500 FT", "contorno": [[-47.536111, -15.845], [-47.550278, -15.677778], [-47.929444, -15.703889], [-47.9175, -15.870833]]}, {"posicao": "Setor 08", "rot": "08", "freq": "119.200", "lim": "GND – 6500 FT", "contorno": [[-47.536111, -15.845], [-47.524444, -16.010833], [-47.905278, -16.037222], [-47.9175, -15.870833]]}];
const paletaSetores = ['#60a5fa', '#f472b6', '#a3e635', '#fb923c', '#a78bfa', '#2dd4bf', '#fbbf24', '#f87171', '#34d399', '#e879f9', '#38bdf8', '#fda4af', '#818cf8'];
var grupoSetores = L.featureGroup();
setores.forEach(function (s, k) {
    var cor = paletaSetores[k % paletaSetores.length];
    L.polygon(s.contorno.map(paraLatLng), { color: cor, fillColor: cor, weight: 2, fillOpacity: 0.2 })
        .bindPopup('<b>' + s.posicao + '</b><br>' + s.lim + '<br>No pacote: <code>SBWR_APP</code> ' + s.freq)
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

// Corredores visuais (REA) e portões da AIC N 10/17 (Anexo A); rumo e altitude de ida, e de volta nos trechos de mão dupla
const reaTrechos = [{"rota": "ALFA", "de": "LAGOA BONITA", "para": "SOBRADINHO 2", "rumo": "271°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "ALFA", "de": "SOBRADINHO 2", "para": "BARRAGEM SANTA MARIA", "rumo": "274°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "ALFA", "de": "BARRAGEM SANTA MARIA", "para": "ESTRADA", "rumo": "287°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "ALFA", "de": "ESTRADA", "para": "PONTA NORTE", "rumo": "279°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "BRAVO", "de": "LAGOA 2", "para": "BARRAGEM SANTA MARIA", "rumo": "028°", "alt": "5000", "rumoVolta": "208°", "altVolta": "4500"}, {"rota": "BRAVO", "de": "BARRAGEM SANTA MARIA", "para": "TORRE 4", "rumo": "028°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "BRAVO", "de": "TORRE 4", "para": "FERCAL", "rumo": "082°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "BRAVO", "de": "FERCAL", "para": "CIPLAN", "rumo": "084°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "CHARLIE", "de": "PONTA SUL", "para": "ESTACIONAMENTO", "rumo": "112°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "CHARLIE", "de": "ESTACIONAMENTO", "para": "SÍTIO", "rumo": "098°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "CHARLIE", "de": "SÍTIO", "para": "LAGOA 2", "rumo": "107°", "alt": "5000", "rumoVolta": null, "altVolta": null}, {"rota": "DELTA", "de": "SARA", "para": "CBAAER", "rumo": "121°", "alt": "4500", "rumoVolta": "301°", "altVolta": "5000"}, {"rota": "DELTA", "de": "CBAAER", "para": "GRANJA 1", "rumo": "140°", "alt": "4500", "rumoVolta": "320°", "altVolta": "5000"}, {"rota": "DELTA", "de": "GRANJA 1", "para": "TORRE 1", "rumo": "156°", "alt": "4500", "rumoVolta": "336°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE 1", "para": "TORRE 2", "rumo": "186°", "alt": "4500", "rumoVolta": "006°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE 2", "para": "TORRE 3", "rumo": "177°", "alt": "4500", "rumoVolta": "357°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE 3", "para": "TORRE TROCO", "rumo": "195°", "alt": "4500", "rumoVolta": "015°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TORRE TROCO", "para": "BARRAGEM 1", "rumo": "199°", "alt": "4500", "rumoVolta": "019°", "altVolta": "5000"}, {"rota": "DELTA", "de": "BARRAGEM 1", "para": "GRANJA 2", "rumo": "286°", "alt": "4500", "rumoVolta": "106°", "altVolta": "5000"}, {"rota": "DELTA", "de": "GRANJA 2", "para": "ALPHAVILLE", "rumo": "264°", "alt": "4500", "rumoVolta": "084°", "altVolta": "5000"}, {"rota": "DELTA", "de": "ALPHAVILLE", "para": "BUNGE", "rumo": "268°", "alt": "4500", "rumoVolta": "088°", "altVolta": "5000"}, {"rota": "DELTA", "de": "BUNGE", "para": "TANQUES CAESB", "rumo": "301°", "alt": "4500", "rumoVolta": "121°", "altVolta": "5000"}, {"rota": "DELTA", "de": "TANQUES CAESB", "para": "POVOADO SERRA DOURADA", "rumo": "327°", "alt": "4500", "rumoVolta": "147°", "altVolta": "5000"}, {"rota": "DELTA", "de": "POVOADO SERRA DOURADA", "para": "TORRE ENGENHO", "rumo": "299°", "alt": "4500", "rumoVolta": "119°", "altVolta": "5000"}, {"rota": "ECHO", "de": "BUNGE", "para": "ESTUFA VERMELHA", "rumo": "040°", "alt": "5000", "rumoVolta": "220°", "altVolta": "4500"}];
const reaPontos = {"LAGOA BONITA": [-47.693406, -15.580458], "SOBRADINHO 2": [-47.836944, -15.631667], "BARRAGEM SANTA MARIA": [-47.954167, -15.668056], "ESTRADA": [-48.061667, -15.675556], "PONTA NORTE": [-48.213425, -15.709294], "LAGOA 2": [-47.963856, -15.748425], "TORRE 4": [-47.948231, -15.618897], "FERCAL": [-47.887425, -15.585442], "CIPLAN": [-47.851339, -15.5673], "PONTA SUL": [-48.227225, -15.771683], "ESTACIONAMENTO": [-48.129, -15.773167], "SÍTIO": [-48.046658, -15.753981], "SARA": [-47.827931, -15.7529], "CBAAER": [-47.702267, -15.773408], "GRANJA 1": [-47.659294, -15.795708], "TORRE 1": [-47.63205, -15.822039], "TORRE 2": [-47.621031, -15.860994], "TORRE 3": [-47.608889, -15.886667], "TORRE TROCO": [-47.602839, -15.941381], "BARRAGEM 1": [-47.6, -16.004167], "GRANJA 2": [-47.715, -16.015], "ALPHAVILLE": [-47.798414, -16.057139], "BUNGE": [-47.960278, -16.124056], "TANQUES CAESB": [-48.065278, -16.1075], "POVOADO SERRA DOURADA": [-48.137022, -16.058247], "TORRE ENGENHO": [-48.259061, -16.042394], "ESTUFA VERMELHA": [-47.930833, -16.039444]};
const portoes = ["BUNGE", "CIPLAN", "ESTUFA VERMELHA", "GRANJA 2", "LAGOA 2", "LAGOA BONITA", "PONTA NORTE", "PONTA SUL", "SARA", "TORRE ENGENHO"];
var corRea = '#c026d3';
var grupoRea = L.featureGroup();
reaTrechos.forEach(function (t) {
    var a = paraLatLng(reaPontos[t.de]), b = paraLatLng(reaPontos[t.para]);
    var duplo = !!t.rumoVolta;
    L.polyline([a, b], { color: corRea, weight: 4, opacity: 0.9 })
        .bindPopup('<b>REA ' + t.rota + '</b><br>' + t.de + (duplo ? ' ⇄ ' : ' → ') + t.para +
            '<br>Rumo: ' + t.rumo + (duplo ? ' / ' + t.rumoVolta : '') +
            '<br>Altitude (ft): ' + t.alt + (duplo ? ' / ' + t.altVolta + ' (ida / volta)' : '<br>Mão única'))
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
    var portao = portoes.indexOf(n) >= 0;
    L.circleMarker(paraLatLng(reaPontos[n]), portao ?
        { radius: 5, color: '#0f172a', weight: 2, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 3.5, color: '#334155', weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Portão ' + n : n).addTo(grupoRea);
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
    "Setores do APP (AIP)": grupoSetores,
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
        '<div><span class="rea-linha"></span>REA</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Portão</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
