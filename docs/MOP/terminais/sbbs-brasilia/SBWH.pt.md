---
title: SBWH - Belo Horizonte
tags:
  - Terminal
  - SBBS
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados gerais

| | |
| --- | --- |
| **TMA** | TMA Belo Horizonte |
| **Posição** | `SBWH_APP` |
| **Indicativo** | Controle Belo Horizonte |
| **Frequência** | **129.100** MHz[^pacote] |
| **Vigilância ATS** | Radar |
| **Aeródromos na TMA** | [SBCF](../../aerodromos/sbbs-brasilia/twr/SBCF.pt.md), [SBBH](../../aerodromos/sbbs-brasilia/twr/SBBH.pt.md), [SBLS](../../aerodromos/sbbs-brasilia/afis/SBLS.pt.md) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Use as abas acima: **Cartas Aeronáuticas** traz as cartas da TMA, **Cartas Visuais** traz as cartas visuais (REA/REH) da AISWEB, **Meteorologia** mostra o mapa meteorológico da área e **Tráfego VATSIM** abre o tráfego no aeródromo principal (SBCF).

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBWH?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-map-legend: Cartas Visuais"
    <div class="ccv-viewer" data-lang="pt">
    <ul class="ccv-lista">
    <li><a href="https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wh-belo-horizonte_rea_20240905.pdf" target="_blank" rel="noopener">CCV REA WH-Belo Horizonte</a></li>
    <li><a href="https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wh-belo-horizonte_reh_20240905.pdf" target="_blank" rel="noopener">CCV REH WH-Belo Horizonte</a></li>
    </ul>
    </div>

    Fonte: [AISWEB](https://aisweb.decea.mil.br/?i=cartas){ target="_blank" }.

=== ":material-weather-partly-cloudy: Meteorologia"
    <div class="tma-meteo" data-lat="-19.750" data-lon="-43.946" data-zoom="8" data-lang="pt"></div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBCF){ .md-button .btn-vatsim-custom target="_blank" }

## :material-map-outline: Mapa

Clique em um volume para ver os limites e a classe. Use o controle de camadas para trocar o mapa de fundo e ligar ou desligar os volumes.

A camada **Corredores visuais (REA)** mostra as 25 REA e os portões dos aeródromos. Linha cheia magenta: rota **recomendada** (classe D, autorização do APP antes de entrar); tracejada azul: rota **obrigatória** em classe G, com coordenação em FCA. Clique em um trecho para ver os rumos, as altitudes e o contato. Detalhes em [Corredores visuais (REA)](#corredores-visuais-rea).

A camada **Rotas de helicópteros (REH)** (23 rotas) fica desligada por padrão. Linha cheia é trecho classe D, tracejada é classe G, e os trechos em laranja são recomendados; os nomes aparecem com mais zoom. Ver [Helicópteros (REH)](#helicopteros-reh).

<div class="fir-map-top">
    <div id="mapa-tma" class="mapa"></div>
</div>

## :material-layers-outline: Volumes

| Volume | Limites | Classe |
| --- | --- | :---: |
| Belo Horizonte 2 | 4100 FT – 5500 FT | <span class="classe-badge classe-c">C</span> |
| Belo Horizonte 1 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> |
| CTR Belo Horizonte | GND – 5500 FT | <span class="classe-badge classe-c">C</span> |
| CTR Confins | GND – 5500 FT | <span class="classe-badge classe-d">D</span> |
| ATZ Belo Horizonte (Pampulha) | GND – 4500 FT | — |
| ATZ Confins | GND – 4500 FT | — |
| ATZ Lagoa Santa | GND – 4500 FT | — |

## :material-headset: Órgãos ATC

| Código | Abrev. | Indicativo de Chamada | Frequência | Observações |
| --- | --- | --- | --- | --- |
| **SBWH_APP** | `WH` | Controle Belo Horizonte | **129.100** |  |
| **SBBH_TWR** | `TBH` | Torre Belo Horizonte | **118.000** |  |
| **SBCF_TWR** | `TCF` | Torre Confins | **118.200** |  |
| **SBLS_R_TWR** | `RLS` | Rádio Lagoa Santa | **122.850** |  |

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
        g0["<span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_NE_CTR</span><span style='display:inline-block;margin:0 6px;padding:8px 14px;border:2px solid rgb(138,86,201);background:var(--md-mermaid-node-bg-color);color:var(--md-mermaid-label-fg-color)'>SBBS_SE_CTR</span>"]:::grpctr
        p1["SBBS_E_CTR"]:::ctr
        p2["SBWH_APP"]:::app
        p3["SBBH_TWR"]:::twr
        p4["SBCF_TWR"]:::twr
        p5["SBLS_R_TWR"]:::twr
        a0(["TMA Belo Horizonte"]):::esp --> p2
        a1(["CTR Belo Horizonte<br>ATZ Belo Horizonte (Pampulha)"]):::esp --> p3
        a2(["CTR Confins<br>ATZ Confins"]):::esp --> p4
        a3(["ATZ Lagoa Santa"]):::esp --> p5
        g0 --> p0
        p1 --> g0
        p2 --> p1
        p3 --> p2
        p4 --> p2
        p5 --> p2
        classDef esp stroke-dasharray:4 3
        classDef twr stroke:#2e9e5b,stroke-width:2px
        classDef app stroke:#2f7fd1,stroke-width:2px
        classDef ctr stroke:#8a56c9,stroke-width:2px
        classDef grpctr fill:none,stroke:#8a56c9,stroke-dasharray:4 3
    ```

## :material-airplane: Circulação VFR

!!! abstract "Documentos de navegação visual"
    - **Circular:** [AIC N 27/26 – Circulação VFR na TMA-BH](https://publicacoes.decea.mil.br/publicacao/aic-n-2726){ target="_blank" } (substitui a AIC N 20/24)
    - **Circular:** [AIC N 25/26 – Projeto TMA BH: alterações no espaço aéreo da TMA-BH e procedimentos em aeroportos associados](https://publicacoes.decea.mil.br/publicacao/aic-n-2526){ target="_blank" }
    - **Carta visual – Rotas de aeronaves (REA):** [CCV REA WH-Belo Horizonte](https://aisweb.decea.mil.br/cartas/visuais/rea/ccv-rea-wh-belo-horizonte_rea_20240905.pdf){ target="_blank" }
    - **Carta visual – Rotas de helicópteros (REH):** [CCV REH WH-Belo Horizonte](https://aisweb.decea.mil.br/cartas/visuais/reh/ccv-reh-wh-belo-horizonte_reh_20240905.pdf){ target="_blank" }

    As cartas estão embutidas na aba **Cartas Visuais** em **Informações Úteis**; as do AISWEB ainda são de SET 2024, anteriores à AIC N 27/26. Os dados desta seção vêm da AIC N 27/26[^aic2726].

### Camadas da TMA e quem atende o VFR

| Espaço | Limites | Classe | VFR |
| --- | --- | :---: | --- |
| **Belo Horizonte 1** | 5500 FT – FL195 | <span class="classe-badge classe-c">C</span> até FL145, <span class="classe-badge classe-a">A</span> acima | Acima de 5500 pés, só dentro das REA (ou com autorização do APP) |
| **Belo Horizonte 2** | 4100 FT – 5500 FT | <span class="classe-badge classe-c">C</span> | Nas REA e REH |
| **CTR Belo Horizonte** | GND – 5500 FT | <span class="classe-badge classe-c">C</span> | Nas REA e REH; entrada e saída pelos portões |
| **CTR Confins** | GND – 5500 FT | <span class="classe-badge classe-d">D</span> | Nas REA e REH; fora das REH, só com contato prévio com o APP |
| Projeção da TMA | Abaixo da Belo Horizonte 1, fora das CTR e ATZ | <span class="classe-badge classe-g">G</span> | Até **5500 pés**, salvo nos corredores com outra altitude; coordenação em FCA |

- **Corredores com classe própria:** a classe de cada trecho de REA e REH é a do corredor, e não a do volume em que ele passa. As REA são de dois tipos:
    - **Recomendadas** (classe D): ALFA a JULIET, perto dos aeródromos. O piloto chama o APP **antes de entrar** e só entra autorizado.
    - **Obrigatórias** (classe G): KILO a YANKEE, na periferia. Coordenação em FCA, sem vigilância ATS; o APP pode ser só monitorado.
- **No mundo real**, o VFR fala com o APP-BH em **120.200** (primária) ou **128.550** (secundária), que também dão FIS e QNH.
- **No pacote**, só existe `SBWH_APP` (**129.100**), que atende todo o VFR das REA e REH controladas. O piloto chama a posição **on-line**, não a frequência do mundo real. Sem o APP, quem assume é a próxima posição na [cobertura](#cobertura-top-down).
- Nas REA e REH classe D, o APP separa **IFR de VFR** e dá **informação de tráfego** entre VFR. Nos trechos classe G não há serviço de vigilância.

### Regras gerais para o VFR

- **Corredores compulsórios acima de 5500 pés:** o VFR acima de 5500 pés fica dentro das REA, salvo autorização do APP. Na projeção da TMA (classe G), é proibido voar acima de 5500 pés fora dos corredores que publicam outra altitude.
- **Direita do eixo:** avião e helicóptero voam à **direita** do eixo do corredor, deixando as referências visuais à esquerda. Todas as REA são de mão dupla, exceto ALFA e CHARLIE, cujo sentido depende da pista de SBBH ([inversão de fluxo](#inversao-de-fluxo-em-sbbh)).
- **Largura:** REA com **3 NM** (1,5 NM para cada lado); ALFA entre CLUBE e INTERSEÇÃO e toda a CHARLIE com **1 NM**; REH com **0,28 NM** (250 m para cada lado).
- **Helicóptero** pode usar as REA, se cumprir as exigências delas. **Avião não usa REH.**
- **Altitudes:** a máxima separa o VFR do IFR acima e deve ser obedecida nas áreas controladas. A mínima é a altitude livre de obstáculos do trecho; abaixo dela, a responsabilidade é do piloto. Mudanças de altitude ficam sempre dentro dos limites do corredor.
- **Reporte:** ao cruzar um portão ou posição, o piloto reporta na frequência do órgão ATC ou da FCA do trecho.
- **Plano de voo:** quem decola de aeródromo controlado põe `REA` no item 15 e os corredores no item 18 (ex.: `ALFA, BRAVO, OSCAR`). Quem vem de aeródromo sem órgão ATS informa ao APP as REA ou REH que vai usar antes de entrar no espaço controlado.
- **Esperas:** o APP pode mandar o VFR esperar sobre referências visuais das REA e REH para espaçar a entrada nas CTR e na TMA.
- **IMC:** sem condições de seguir em VMC, o avião volta e pousa no aeródromo de partida ou no mais próximo, ou pede mudança para IFR ao APP. Helicóptero numa REH classe D **para em voo pairado** e avisa o APP na hora.
- **QNH:** ATIS de SBBH (**127.450**) ou SBCF (**127.850**); sem ATIS, pedir ao APP.
- **Transponder** ligado (modo A/C ou S) e **rádio VHF** obrigatórios nas REA e REH e em toda a projeção da TMA. Faróis acesos são recomendados.

Sem código do ATC, o VFR vindo de fora da TMA ou de aeródromo sem órgão ATS usa o código do destino:

| Destino | Código |
| --- | :---: |
| SBBH | **2011** |
| SBCF | **2012** |
| SBLS | **2013** |
| Outros aeródromos nas CTR Belo Horizonte e Confins | **2014** |
| Treinamento em SNLG | **0300** |
| Helicóptero só na classe G (inclusive REA e REH classe G) | **0100** |
| Demais casos | **2000** |

### Corredores visuais (REA)

As 25 REA da TMA. Altitudes em pés (QNH), no formato **máxima / mínima**; nas áreas controladas, a máxima deve ser obedecida. O rumo vale para o sentido de ida / volta. Classe D: rota **recomendada**, com autorização do APP antes de entrar. Classe G: rota **obrigatória**, com coordenação na FCA.

| REA | Trecho | Rumos | Altitudes | Classe · contato |
| :---: | :--- | :---: | :--- | :--- |
| **ALFA** | SINUOSO ⇄ FLORES | 128° / 308° | 4500 / 4400 | D · APP-BH 120.200 |
|  | FLORES ⇄ CLUBE | 109° / 289° | 4500 / 4300 | D · APP-BH 120.200 |
|  | CLUBE ⇄ INTERSEÇÃO | 086° / 266° | 4500 / 4300 | D · APP-BH 120.200 |
| **BRAVO** | IBIRITÉ ⇄ CLUBE | 023° / 203° | 5600 / 4500 | D · APP-BH 120.200 |
| **CHARLIE** | IBIRITÉ ⇄ VALLOUREC | 068° / 248° | 5600 / 4600 | D · APP-BH 120.200 |
|  | VALLOUREC ⇄ PAZ | 052° / 232° | 5000 / 4500 | D · APP-BH 120.200 |
| **DELTA** | MINA ⇄ SÍTIOS | 093° / 273° | 4900 / 4700 | D · APP-BH 120.200 |
|  | SÍTIOS ⇄ UNIÃO | 092° / 272° | 5000 / 4700 | D · APP-BH 120.200 |
|  | UNIÃO ⇄ CONDOMÍNIO | 095° / 275° | 5500 / 4700 | D · APP-BH 120.200 |
| **ECHO** | UNIÃO ⇄ JABOTICATUBAS | 346° / 166° | 5000 / 4800 | D · APP-BH 120.200 |
|  | JABOTICATUBAS ⇄ TREVO | 336° / 156° | 5000 / 4500 | D · APP-BH 120.200 |
|  | TREVO ⇄ BALDIM | 346° / 166° | 5000 / 4500 | D · APP-BH 120.200 |
|  | BALDIM ⇄ JEQUITIBÁ | 010° / 190° | 5500 / 4500 | D · APP-BH 120.200 |
| **FOXTROT** | TREVO ⇄ PONTE | 231° / 051° | 4500 / 4300 | D · APP-BH 120.200 |
| **GOLF** | JABOTICATUBAS ⇄ PONTE | 278° / 098° | 4500 / 4300 | D · APP-BH 120.200 |
| **HOTEL** | GARÇAS ⇄ ANDIROBA | 097° / 277° | 4500 / 4200 | D · APP-BH 120.200 |
|  | ANDIROBA ⇄ CAMPINHO | 115° / 295° | 4400 / 4200 | D · APP-BH 120.200 |
| **INDIA** | FORTUNA ⇄ SETE LAGOAS | 083° / 263° | 5000 / 4200 | D · APP-BH 120.200 |
| **JULIET** | ARAÇAÍ ⇄ IVECO | 188° / 008° | 5500 / 3500 | D · APP-BH 120.200 |
| **KILO** | ARDÓSIA ⇄ FORTUNA | 175° / 355° | 6000 / 4000 | G · FCA Norte 120.425 |
|  | FORTUNA ⇄ GARÇAS | 188° / 008° | 5500 / 4000 | G · FCA Norte 120.425 |
|  | GARÇAS ⇄ SINUOSO | 192° / 012° | 5500 / 4200 | G · FCA Sul 122.550 |
|  | SINUOSO ⇄ REPRESA | 190° / 010° | 5500 / 5200 | G · FCA Sul 122.550 |
| **LIMA** | SINUOSO ⇄ ITAÚNA | 244° / 064° | 5500 / 4700 | G · FCA Sul 122.550 |
|  | ITAÚNA ⇄ REPRESA | 135° / 315° | 6000 / 5000 | G · FCA Sul 122.550 |
|  | REPRESA ⇄ MOEDA | 147° / 327° | 6000 / 5500 | G · FCA Sul 122.550 |
| **MIKE** | GERAIS ⇄ MOEDA | 073° / 253° | 6500 / 4500 | G · FCA Sul 122.550 |
|  | MOEDA ⇄ ITABIRITO | 092° / 272° | 6500 / 5700 | G · FCA Sul 122.550 |
|  | ITABIRITO ⇄ SANTA BÁRBARA | 075° / 255° | 6200 / 6000 | G · FCA Sul 122.550 |
|  | SANTA BÁRBARA ⇄ CONDOMÍNIO | 028° / 208° | 6200 / 4200 | G · FCA Norte 120.425 |
|  | CONDOMÍNIO ⇄ ITABIRA | 094° / 274° | 7000 / 4700 | G · FCA Norte 120.425 |
|  | ITABIRA ⇄ AREAL | 097° / 277° | 7000 / 4500 | G · FCA Norte 120.425 |
| **NOVEMBER** | CONDOMÍNIO ⇄ MONLEVADE | 152° / 322° | 7000 / 4700 | G · FCA Norte 120.425 |
|  | MONLEVADE ⇄ SANTA BÁRBARA | 268° / 088° | 6200 / 5000 | G · FCA Norte 120.425 |
| **OSCAR** | CACHOEIRAS ⇄ ITABIRITO | 339° / 159° | 6500 / 5700 | G · FCA Sul 122.550 |
|  | ITABIRITO ⇄ CHAPÉU | 334° / 154° | 6000 / 5700 | G · FCA Sul 122.550 |
|  | CHAPÉU ⇄ IBIRITÉ | 329° / 149° | 6000 / 5600 | G · FCA Sul 122.550 |
| **PAPA** | IBIRITÉ ⇄ FEIJÃO | 231° / 051° | 6000 / 5500 | G · FCA Sul 122.550 |
|  | FEIJÃO ⇄ MOEDA | 183° / 003° | 6000 / 5500 | G · FCA Sul 122.550 |
|  | MOEDA ⇄ JECEABA | 186° / 006° | 6500 / 5000 | G · FCA Sul 122.550 |
| **QUEBEC** | CHAPÉU ⇄ FEIJÃO | 283° / 103° | 6000 / 5600 | G · FCA Sul 122.550 |
|  | FEIJÃO ⇄ REPRESA | 280° / 100° | 6000 / 5700 | G · FCA Sul 122.550 |
|  | REPRESA ⇄ ITAGUARA | 243° / 063° | 6000 / 5000 | G · FCA Sul 122.550 |
| **ROMEU** | GARÇAS ⇄ GRANJAS | 246° / 066° | 6000 / 4000 | G · FCA Sul 122.550 |
|  | GRANJAS ⇄ SINUOSO | 118° / 298° | 5500 / 4000 | G · FCA Sul 122.550 |
| **SIERRA** | PAPAGAIOS ⇄ FORTUNA | 134° / 314° | 6000 / 4000 | G · FCA Norte 120.425 |
| **TANGO** | FORTUNA ⇄ PARAOPEBA | 032° / 212° | 6000 / 4000 | G · FCA Norte 120.425 |
|  | PARAOPEBA ⇄ FISCAL | 029° / 209° | 6000 / 4000 | G · FCA Norte 120.425 |
| **UNIFORM** | PARAOPEBA ⇄ ARAÇAÍ | 086° / 266° | 6000 / 4000 | G · FCA Norte 120.425 |
|  | ARAÇAÍ ⇄ JEQUITIBÁ | 101° / 281° | 6000 / 4000 | G · FCA Norte 120.425 |
|  | JEQUITIBÁ ⇄ LAPINHA | 103° / 283° | 7000 / 4500 | G · FCA Norte 120.425 |
|  | LAPINHA ⇄ CONCEIÇÃO | 103° / 283° | 7000 / 6300 | G · FCA Norte 120.425 |
| **VICTOR** | FISCAL ⇄ ARAÇAÍ | 178° / 358° | 6000 / 3600 | G · FCA Norte 120.425 |
| **WHISKEY** | PRES. JUSCELINO ⇄ PIRAPAMA | 172° / 352° | 6000 / 3500 | G · FCA Norte 120.425 |
|  | PIRAPAMA ⇄ JEQUITIBÁ | 181° / 001° | 6000 / 3500 | G · FCA Norte 120.425 |
| **X-RAY** | ELEFANTE ⇄ JEQUITIBÁ | 245° / 065° | 7000 / 5200 | G · FCA Norte 120.425 |
| **YANKEE** | MANOEL ⇄ SANTA BÁRBARA | 345° / 165° | 6200 / 4900 | G · FCA Norte 120.425 |
|  | SANTA BÁRBARA ⇄ UNIÃO | 350° / 170° | 5500 / 4900 | G · FCA Norte 120.425 |

O que cada corredor faz e onde estão as armadilhas:

- **ALFA** e **CHARLIE** são as entradas e saídas de SBBH pelo oeste e sudoeste, com **sentido reversível** conforme a pista ([inversão de fluxo](#inversao-de-fluxo-em-sbbh)). A ALFA vem de SINUOSO (rio Paraopeba) pela Várzea das Flores até o portão INTERSEÇÃO; a CHARLIE vem de IBIRITÉ pela Vallourec até o portão PAZ. Ambas cruzam por cima o grande fluxo de helicópteros das REH ARENA, CEASA, CENTRAL, CHAMINÉ e PRATES; não desça abaixo da mínima, nem em espera. Na RWY 13, o avião da ALFA mantém a proa do Mineirinho para entrar no circuito.
- **BRAVO** liga IBIRITÉ a CLUBE e alimenta a ALFA. SINUOSO, IBIRITÉ e CLUBE são *hot spots* onde várias rotas convergem.
- **DELTA** sai de SBBH pelo portão MINA para leste pela BR-381 até CONDOMÍNIO (Itabira). **Não serve para planejar a chegada a SBBH**: na volta, o piloto pede o uso ao APP antes de UNIÃO ou CONDOMÍNIO, por causa da aproximação da RWY 34 de SBCF.
- **ECHO** é **exclusiva** das chegadas e saídas de SBCF e SBLS, de UNIÃO pelo vale do Taquaraçu até Jaboticatubas, Baldim e Jequitibá. Não ultrapasse a máxima (fluxo das RWY 16/34 de SBCF). JABOTICATUBAS concentra voos de experiência e treinamento de SBLS e SNLG.
- **FOXTROT** (TREVO) e **GOLF** (JABOTICATUBAS) chegam ao portão PONTE de SBCF pelo norte e pelo leste; **HOTEL** chega ao portão CAMPINHO (SBCF e SBLS) pelo oeste, desde GARÇAS. Espere instruções de espera por causa das RWY 16/34 de SBCF. Atenção à SBR 879 (GND – 3500 pés) perto da GOLF, avisada pelo APP quando ativa.
- **INDIA** (FORTUNA – Sete Lagoas) e **JULIET** (ARAÇAÍ – IVECO) cobrem o noroeste, também sob o fluxo de SBCF.
- **Anel em classe G:** KILO (oeste, de ARDÓSIA à represa do Rio Manso), LIMA, PAPA e QUEBEC (sudoeste), MIKE e OSCAR (sul, pela Serra da Moeda e Itabirito), NOVEMBER e YANKEE (leste, Santa Bárbara e Monlevade), SIERRA, TANGO, UNIFORM, VICTOR, WHISKEY e X-RAY (norte). Elas levam o VFR até as entradas das recomendadas: para ALFA, HOTEL e INDIA, chamar o APP antes de SINUOSO, GARÇAS e FORTUNA; para BRAVO e CHARLIE, antes de IBIRITÉ; para DELTA, antes de CONDOMÍNIO ou UNIÃO; para ECHO e JULIET, antes de JEQUITIBÁ e ARAÇAÍ.
- **Áreas condicionadas perto dos corredores:** SBR 327 Serra da Moeda (GND – 7000 pés) junto à MIKE, OSCAR, PAPA e QUEBEC; SBD 387 Brumadinho sob a LIMA e a QUEBEC; SBR 817 e SBR 318 perto de CACHOEIRAS (OSCAR); SBR 388 Pará de Minas junto à ROMEU e à SIERRA.

### Inversão de fluxo em SBBH

A circulação de aviões a oeste e sudoeste de SBBH usa as REA **ALFA** e **CHARLIE** como corredores reversíveis: o sentido depende da pista em uso, salvo autorização diferente do APP. Quem vai para SBBH chama o APP **antes de SINUOSO ou IBIRITÉ** para receber a autorização de entrada. A pista em uso está no ATIS de SBBH.

| Pista SBBH | Entrada | Saída | Contato com o APP |
| :---: | :--- | :--- | :--- |
| **13** | Portão INTERSEÇÃO (ALFA) | Portão PAZ (CHARLIE), com autorização | Antes de SINUOSO ou IBIRITÉ |
| **31** | Portão PAZ (CHARLIE) | Portão INTERSEÇÃO (ALFA), com autorização | Antes de IBIRITÉ |

A Torre informa o sentido do fluxo às saídas, e o APP às chegadas.

### Portões dos aeródromos

A entrada e a saída das CTR e ATZ são **pelos portões**, salvo instrução diferente do ATC.

| Aeródromo | Portões REA (aviões) | Portões REH (helicópteros) |
| :---: | :--- | :--- |
| **SBBH** | INTERSEÇÃO (chegada RWY 13, saída RWY 31) · PAZ (chegada RWY 31, saída RWY 13) · MINA | CEASA · CIDADE ADM · ETE · MATRIZ STA LUZIA · PARQUE |
| **SBCF** | CAMPINHO · PONTE | LAGOA DOS MARES · PONTE · VILLE |
| **SBLS** | CAMPINHO · JABOTICATUBAS | LAGOA · OLHOS |

**SBBH.** O avião chega pela ALFA ou pela CHARLIE, conforme a pista, ou pela DELTA (com as restrições acima).

- Decolagem da **RWY 13**: curva à direita para o portão PAZ, ou à esquerda na proa da posição RIO para a DELTA.
- Decolagem da **RWY 31**: curva à esquerda para o portão INTERSEÇÃO, ou à direita para o portão MINA, dentro da ATZ, para a DELTA.
- Quem decola ou está no circuito de SBBH e vai para o leste pode ser autorizado **direto MINA**, mantendo a altitude de tráfego até sair da ATZ.
- Helicópteros chegam e saem pelas REH CEASA (portões CEASA e PARQUE), CIPÓ e LESTE (MATRIZ STA LUZIA), CONFINS (CIDADE ADM) e NORTE (ETE), sujeitos ao tráfego de SBBH. No portão, o helicóptero precisa de autorização do APP para seguir para SBBH.

**SBCF e SBLS.** O avião usa as REA ECHO, FOXTROT, GOLF e HOTEL, sempre com autorização prévia do APP; na saída, o APP normalmente o orienta para essas mesmas REA.

- Helicóptero de ou para SBCF pelo **oeste, sudoeste e sul**: REH CONFINS ou NEVES, com transferência para a Torre Confins perto do portão LAGOA DOS MARES. Na saída, chama o APP ao passar por esse portão.
- Pelo **leste, nordeste e sudeste**: REH PONTE ou VILLE, com transferência perto dos portões PONTE ou VILLE.
- Para SBLS e a cidade de Lagoa Santa pelo leste: REH LAGOA, aguardando instruções do APP para passar à Rádio Lagoa Santa.
- Não sobrevoar os tanques de combustível nem os terminais de passageiros de SBCF.
- Na CTR Confins, voo fora das REH só com contato prévio com o APP. A nordeste de SBLS há voos militares de experiência e treinamento, perto das REH CIPÓ, JABOTICATUBAS, LAGOA, PONTE e VILLE.

### Espaço não controlado sob a TMA (FCA)

Na classe G sob a TMA e nas REA e REH classe G, a coordenação entre aeronaves é feita nas frequências de coordenação (FCA):

| FCA | Frequência | Onde |
| :--- | :---: | :--- |
| **Norte** | 120.425 | Metade norte da TMA: REA SIERRA, TANGO, UNIFORM, VICTOR, WHISKEY, X-RAY, YANKEE, NOVEMBER, a KILO ao norte de GARÇAS e a MIKE de SANTA BÁRBARA a AREAL |
| **Sul** | 122.550 | Metade sul da TMA: REA LIMA, OSCAR, PAPA, QUEBEC, ROMEU, a KILO ao sul de GARÇAS e a MIKE de GERAIS a SANTA BÁRBARA |

- A troca de FCA acontece em **GARÇAS** (KILO) e **SANTA BÁRBARA** (MIKE, YANKEE e NOVEMBER); a AIC recomenda monitorar a próxima FCA 1 minuto antes. SNLG e SNPA têm FCA própria.
- Na VATSIM as FCA não existem como posição: sem ATC on-line, o piloto usa a **UNICOM 122.800**. Com o APP on-line, o VFR na classe G pode pedir informação de voo na frequência dele.

### Helicópteros (REH)

- As 23 **REH** formam a malha de helicópteros sobre Belo Horizonte, Contagem, Betim, Nova Lima e a região de Confins, quase toda entre **3400 e 5000 pés**, com 250 m de semilargura. São de mão dupla, e o piloto mantém a direita do eixo. O traçado completo está na camada **Rotas de helicópteros (REH)** do [mapa](#mapa), com altitudes e contato por trecho.
- **Obrigatórias classe D:** o piloto **notifica** o APP ao entrar e mantém escuta até sair. **Obrigatórias classe G:** coordenação em FCA (ESMERALDAS, JABOTICATUBAS, NOVA LIMA, OESTE, RAPOSOS, SETE LAGOAS e SUL têm trechos em classe G).
- **Recomendadas** (autorização do APP **antes** de entrar): CEASA, CONFINS, LAGOA, PONTE, SABARÁ e VILLE inteiras, e os trechos SABARÁ – CAETÉ (CAETÉ), MATRIZ STA LUZIA – RAVENA (LESTE), VERA CRUZ – LAGOA DOS MARES (NEVES) e ETE – VERA CRUZ (NORTE). Sem autorização, o helicóptero volta para a origem ou mantém a posição.
- A **SABARÁ** não serve para planejamento de voo. CAETÉ, CEASA, CONFINS, LESTE, NORTE e SABARÁ passam pelos setores de aproximação da RWY 31 e de decolagem da RWY 13 de SBBH; o APP pode mandar esperar, sobretudo com decolagens lentas da 13.
- A CEASA entre PEDREIRA e PARQUE depende do tráfego de SBBH. Perto do PARQUE e no centro-sul de BH há muitos voos locais (imprensa, segurança pública) e drones a baixa altura; o APP pode dar instruções alternativas.
- **Hot spot GARAGEM** (CENTRAL, CHAMINÉ, PRATES e SETE LAGOAS) e cruzamento sob as REA ALFA, BRAVO e CHARLIE: o avião voa acima, a 4300–5600 pés.
- Entre GALPÕES e HARAS, a mínima de **4100 pés** é obrigatória (presídio abaixo).

### Outras regras

- Em VMC, aplica-se separação composta de 2,5 NM ou 500 FT entre IFR em procedimento RNP das RWY 13/31 de SBBH e aviões ou helicópteros VFR nas REA e REH.
- Proibida a operação de aeronaves sem rádio em SBCF.
- SBLS: contato compulsório com o Controle Belo Horizonte ao entrar na TMA; manter-se na ATZ e não estender a perna base (RWY 13) nem atrasar a curva (RWY 31) além da posição BOSQUE, por causa de SBCF.

### Fraseologia

No contato, o piloto é breve e informa destinatário, matrícula, corredor, portão ou posição, altitude e sentido[^aic2726]. Rota recomendada, pedindo para entrar:

```
Controle Belo Horizonte, PR-MWN, REA ROMEU, posição SINUOSO, mantendo 5500 pés, solicita ingresso na REA ALFA.
```

REH obrigatória classe D, notificando a entrada:

```
Controle Belo Horizonte, PR-MWN, REH SUL, posição BH SHOPPING, mantendo 4400 pés, proa PARQUE.
```

Na classe G, na FCA (UNICOM na VATSIM):

```
Coordenação, PR-MWN, REA OSCAR, posição IBIRITÉ, mantendo 6000 pés, proa CHAPÉU, após ITABIRITO.
```

## :material-note-text-outline: Observações

- Belo Horizonte 1 é classe A entre FL145 e FL195 e classe C entre 5500 FT e FL145. Os setores 05 e 06 do APP são as finais de SBBH e SBCF.
- A CTR Belo Horizonte exclui a CTR Confins.
- SBLS é aeródromo militar (PAMALS); a aviação civil depende de autorização do diretor do PAMALS.
- As ATZs não têm classe publicada na AIP (ENR 2.2).
- No pacote, o APP Belo Horizonte não é setorizado: `SBWH_APP` cobre toda a TMA.
- O Projeto TMA-BH (AIC N 25/26) revisa as SID, STAR, IAC, REA e REH da TMA a partir da AIRAC de 26 NOV 2026. O mapa mostra os contornos do pacote de setores.

---

Voltar para a [visão geral das terminais](index.pt.md) da FIR Brasília.

[^pacote]: Frequência no pacote de setores da VATSIM Brasil.
[^aic2726]: [AIC N 27/26](https://publicacoes.decea.mil.br/publicacao/aic-n-2726){ target="_blank" }, itens 2 a 5 e Anexos A e B.

<!--
Daqui pra baixo, é o mapa. Contornos extraídos do pacote SBBS (setores TMA_* e CTR_*), em [longitude, latitude].
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
    .reh-rotulo { background: #0f766e; color: #fff; border: 0; font-weight: 600; font-size: 10px; padding: 0 4px; box-shadow: none }
    .reh-rotulo::before { display: none }
    .reh-zoom-baixo .reh-rotulo { display: none }
    .rea-zoom-baixo .rea-rotulo, .rea-zoom-medio .rea-rotulo-trecho { display: none }
    .mapa-legenda .rea-linha { display: inline-block; width: 18px; height: 0; border-top: 3px solid #c026d3; vertical-align: middle; margin-right: 6px }
    .mapa-legenda .rea-linha.g { border-top: 3px dashed #0284c7 }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 1", "posicao": "SBWH_APP", "freq": "129.100", "lim": "5500 FT – FL195", "classe": "A/C", "link": "", "contorno": [[-43.266908, -20.206404], [-43.4576, -20.4966], [-43.9047, -20.5654], [-43.969076, -20.54265], [-44.4974, -20.3533], [-44.6949, -19.8], [-44.7775, -19.569], [-44.6146, -19.1277], [-44.353616, -18.988162], [-44.3214, -18.9709], [-43.951268, -18.949964], [-43.692, -18.9348], [-43.1142, -19.6081], [-43.1373, -20.0084], [-43.266908, -20.206404]]},
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 2", "posicao": "SBWH_APP", "freq": "129.100", "lim": "4100 FT – 5500 FT", "classe": "C", "link": "", "contorno": [[-44.3793, -19.2945], [-44.2396, -19.225], [-43.9432, -19.166], [-43.4868, -19.5018], [-43.5229, -19.9021], [-43.7936, -20.1036], [-43.9467, -20.0488], [-43.9806, -19.9293], [-44.3038, -19.9772], [-44.4276, -19.5236], [-44.3793, -19.2945]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "CTR Confins", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 5500 FT", "classe": "D", "link": "", "contorno": [[-43.7636, -19.6104], [-43.8163, -19.7746], [-43.9881, -19.8107], [-44.1995, -19.5813], [-43.9659, -19.39], [-43.7636, -19.6104]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "CTR Belo Horizonte", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 5500 FT", "classe": "C", "link": "", "contorno": [[-43.7636, -19.6104], [-43.6578, -19.7253], [-43.7524, -19.9447], [-43.8544, -19.9932], [-43.9475, -19.9796], [-43.9592, -19.9384], [-44.1801, -19.8593], [-44.1995, -19.5813], [-43.9881, -19.8107], [-43.8163, -19.7746], [-43.7636, -19.6104]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "ATZ Confins", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.912222, -19.620833], [-43.935278, -19.64], [-43.939722, -19.652222], [-43.93, -19.662778], [-43.899167, -19.696389], [-43.951667, -19.738333], [-44.083056, -19.596389], [-43.973889, -19.509722], [-43.888889, -19.601667], [-43.912222, -19.620833]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "ATZ Belo Horizonte (Pampulha)", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.891667, -19.813056], [-43.856944, -19.840833], [-43.881667, -19.911111], [-43.928056, -19.917778], [-44.009444, -19.892222], [-44.0425, -19.859722], [-44.017778, -19.789444], [-43.974722, -19.786944], [-43.891667, -19.813056]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "ATZ Lagoa Santa", "posicao": "SBLS_R_TWR", "freq": "122.850", "lim": "GND – 4500 FT", "classe": "—", "link": "", "contorno": [[-43.912222, -19.620833], [-43.863611, -19.632778], [-43.8575, -19.6625], [-43.863611, -19.679444], [-43.93, -19.662778], [-43.939722, -19.652222], [-43.935278, -19.64], [-43.912222, -19.620833]]}
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

// Corredores visuais (REA), REH e portões da AIC N 27/26 (Anexos A e B); gerado de bhgen/emit.py
const reaTrechos = [{"rota": "ALFA", "de": "SINUOSO", "para": "FLORES", "rumos": "128° / 308°", "max": "4500", "min": "4400", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "ALFA", "de": "FLORES", "para": "CLUBE", "rumos": "109° / 289°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "ALFA", "de": "CLUBE", "para": "INTERSEÇÃO", "rumos": "086° / 266°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "BRAVO", "de": "IBIRITÉ", "para": "CLUBE", "rumos": "023° / 203°", "max": "5600", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CHARLIE", "de": "IBIRITÉ", "para": "VALLOUREC", "rumos": "068° / 248°", "max": "5600", "min": "4600", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "CHARLIE", "de": "VALLOUREC", "para": "PAZ", "rumos": "052° / 232°", "max": "5000", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200", "rev": true}, {"rota": "DELTA", "de": "MINA", "para": "SÍTIOS", "rumos": "093° / 273°", "max": "4900", "min": "4700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "DELTA", "de": "SÍTIOS", "para": "UNIÃO", "rumos": "092° / 272°", "max": "5000", "min": "4700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "DELTA", "de": "UNIÃO", "para": "CONDOMÍNIO", "rumos": "095° / 275°", "max": "5500", "min": "4700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "UNIÃO", "para": "JABOTICATUBAS", "rumos": "346° / 166°", "max": "5000", "min": "4800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "JABOTICATUBAS", "para": "TREVO", "rumos": "336° / 156°", "max": "5000", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "TREVO", "para": "BALDIM", "rumos": "346° / 166°", "max": "5000", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ECHO", "de": "BALDIM", "para": "JEQUITIBÁ", "rumos": "010° / 190°", "max": "5500", "min": "4500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "FOXTROT", "de": "TREVO", "para": "PONTE", "rumos": "231° / 051°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "GOLF", "de": "JABOTICATUBAS", "para": "PONTE", "rumos": "278° / 098°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "HOTEL", "de": "GARÇAS", "para": "ANDIROBA", "rumos": "097° / 277°", "max": "4500", "min": "4200", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "HOTEL", "de": "ANDIROBA", "para": "CAMPINHO", "rumos": "115° / 295°", "max": "4400", "min": "4200", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "INDIA", "de": "FORTUNA", "para": "SETE LAGOAS", "rumos": "083° / 263°", "max": "5000", "min": "4200", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "JULIET", "de": "ARAÇAÍ", "para": "IVECO", "rumos": "188° / 008°", "max": "5500", "min": "3500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "KILO", "de": "ARDÓSIA", "para": "FORTUNA", "rumos": "175° / 355°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "KILO", "de": "FORTUNA", "para": "GARÇAS", "rumos": "188° / 008°", "max": "5500", "min": "4000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "KILO", "de": "GARÇAS", "para": "SINUOSO", "rumos": "192° / 012°", "max": "5500", "min": "4200", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "KILO", "de": "SINUOSO", "para": "REPRESA", "rumos": "190° / 010°", "max": "5500", "min": "5200", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "LIMA", "de": "SINUOSO", "para": "ITAÚNA", "rumos": "244° / 064°", "max": "5500", "min": "4700", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "LIMA", "de": "ITAÚNA", "para": "REPRESA", "rumos": "135° / 315°", "max": "6000", "min": "5000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "LIMA", "de": "REPRESA", "para": "MOEDA", "rumos": "147° / 327°", "max": "6000", "min": "5500", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "MIKE", "de": "GERAIS", "para": "MOEDA", "rumos": "073° / 253°", "max": "6500", "min": "4500", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "MIKE", "de": "MOEDA", "para": "ITABIRITO", "rumos": "092° / 272°", "max": "6500", "min": "5700", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "MIKE", "de": "ITABIRITO", "para": "SANTA BÁRBARA", "rumos": "075° / 255°", "max": "6200", "min": "6000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "MIKE", "de": "SANTA BÁRBARA", "para": "CONDOMÍNIO", "rumos": "028° / 208°", "max": "6200", "min": "4200", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "MIKE", "de": "CONDOMÍNIO", "para": "ITABIRA", "rumos": "094° / 274°", "max": "7000", "min": "4700", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "MIKE", "de": "ITABIRA", "para": "AREAL", "rumos": "097° / 277°", "max": "7000", "min": "4500", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "NOVEMBER", "de": "CONDOMÍNIO", "para": "MONLEVADE", "rumos": "152° / 322°", "max": "7000", "min": "4700", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "NOVEMBER", "de": "MONLEVADE", "para": "SANTA BÁRBARA", "rumos": "268° / 088°", "max": "6200", "min": "5000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "OSCAR", "de": "CACHOEIRAS", "para": "ITABIRITO", "rumos": "339° / 159°", "max": "6500", "min": "5700", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "OSCAR", "de": "ITABIRITO", "para": "CHAPÉU", "rumos": "334° / 154°", "max": "6000", "min": "5700", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "OSCAR", "de": "CHAPÉU", "para": "IBIRITÉ", "rumos": "329° / 149°", "max": "6000", "min": "5600", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "PAPA", "de": "IBIRITÉ", "para": "FEIJÃO", "rumos": "231° / 051°", "max": "6000", "min": "5500", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "PAPA", "de": "FEIJÃO", "para": "MOEDA", "rumos": "183° / 003°", "max": "6000", "min": "5500", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "PAPA", "de": "MOEDA", "para": "JECEABA", "rumos": "186° / 006°", "max": "6500", "min": "5000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "QUEBEC", "de": "CHAPÉU", "para": "FEIJÃO", "rumos": "283° / 103°", "max": "6000", "min": "5600", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "QUEBEC", "de": "FEIJÃO", "para": "REPRESA", "rumos": "280° / 100°", "max": "6000", "min": "5700", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "QUEBEC", "de": "REPRESA", "para": "ITAGUARA", "rumos": "243° / 063°", "max": "6000", "min": "5000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "ROMEU", "de": "GARÇAS", "para": "GRANJAS", "rumos": "246° / 066°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "ROMEU", "de": "GRANJAS", "para": "SINUOSO", "rumos": "118° / 298°", "max": "5500", "min": "4000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "SIERRA", "de": "PAPAGAIOS", "para": "FORTUNA", "rumos": "134° / 314°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "TANGO", "de": "FORTUNA", "para": "PARAOPEBA", "rumos": "032° / 212°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "TANGO", "de": "PARAOPEBA", "para": "FISCAL", "rumos": "029° / 209°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "UNIFORM", "de": "PARAOPEBA", "para": "ARAÇAÍ", "rumos": "086° / 266°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "UNIFORM", "de": "ARAÇAÍ", "para": "JEQUITIBÁ", "rumos": "101° / 281°", "max": "6000", "min": "4000", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "UNIFORM", "de": "JEQUITIBÁ", "para": "LAPINHA", "rumos": "103° / 283°", "max": "7000", "min": "4500", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "UNIFORM", "de": "LAPINHA", "para": "CONCEIÇÃO", "rumos": "103° / 283°", "max": "7000", "min": "6300", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "VICTOR", "de": "FISCAL", "para": "ARAÇAÍ", "rumos": "178° / 358°", "max": "6000", "min": "3600", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "WHISKEY", "de": "PRES. JUSCELINO", "para": "PIRAPAMA", "rumos": "172° / 352°", "max": "6000", "min": "3500", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "WHISKEY", "de": "PIRAPAMA", "para": "JEQUITIBÁ", "rumos": "181° / 001°", "max": "6000", "min": "3500", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "X-RAY", "de": "ELEFANTE", "para": "JEQUITIBÁ", "rumos": "245° / 065°", "max": "7000", "min": "5200", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "YANKEE", "de": "MANOEL", "para": "SANTA BÁRBARA", "rumos": "345° / 165°", "max": "6200", "min": "4900", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "YANKEE", "de": "SANTA BÁRBARA", "para": "UNIÃO", "rumos": "350° / 170°", "max": "5500", "min": "4900", "rec": false, "esp": "G · FCA Norte 120.425"}];
const reaPontos = {"SINUOSO": [-44.3777, -19.86028], "FLORES": [-44.16558, -19.91388], "CLUBE": [-44.06085, -19.90563], "INTERSEÇÃO": [-44.00546, -19.87845], "IBIRITÉ": [-44.06083, -20.02024], "VALLOUREC": [-44.00194, -19.96444], "PAZ": [-43.96412, -19.89829], "MINA": [-43.84316, -19.81759], "SÍTIOS": [-43.68472, -19.76306], "UNIÃO": [-43.57951, -19.7233], "CONDOMÍNIO": [-43.38608, -19.66157], "JABOTICATUBAS": [-43.7475, -19.51861], "TREVO": [-43.84248, -19.43555], "BALDIM": [-43.93034, -19.32554], "JEQUITIBÁ": [-43.97581, -19.14602], "PONTE": [-43.91136, -19.56008], "GARÇAS": [-44.40997, -19.69866], "ANDIROBA": [-44.23025, -19.64991], "CAMPINHO": [-44.05762, -19.65458], "FORTUNA": [-44.44912, -19.56517], "SETE LAGOAS": [-44.25988, -19.46129], "ARAÇAÍ": [-44.24858, -19.20102], "IVECO": [-44.20264, -19.35798], "ARDÓSIA": [-44.63941, -19.22192], "REPRESA": [-44.29743, -20.17927], "ITAÚNA": [-44.57747, -20.07602], "MOEDA": [-44.05358, -20.33296], "GERAIS": [-44.22464, -20.47008], "ITABIRITO": [-43.77831, -20.23046], "SANTA BÁRBARA": [-43.4125, -19.95833], "ITABIRA": [-43.21108, -19.60185], "AREAL": [-43.12876, -19.57912], "MONLEVADE": [-43.15192, -19.83796], "CACHOEIRAS": [-43.51011, -20.4883], "CHAPÉU": [-43.93266, -20.10702], "FEIJÃO": [-44.12694, -20.14167], "JECEABA": [-43.98497, -20.53546], "ITAGUARA": [-44.48667, -20.39194], "GRANJAS": [-44.55174, -19.8457], "PAPAGAIOS": [-44.75207, -19.45479], "PARAOPEBA": [-44.40275, -19.27768], "FISCAL": [-44.37014, -18.96132], "LAPINHA": [-43.76139, -19.10889], "CONCEIÇÃO": [-43.41528, -19.04889], "PRES. JUSCELINO": [-44.12087, -18.87619], "PIRAPAMA": [-44.03914, -19.00268], "ELEFANTE": [-43.76091, -18.91956], "MANOEL": [-43.19924, -20.21384]};
const rehTrechos = [{"rota": "ARENA", "de": "ARENA MRV", "para": "INTERLOGOS", "rumos": "148° / 328°", "max": "4300", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "ARENA", "de": "INTERLOGOS", "para": "ESTRELA", "rumos": "150° / 330°", "max": "4400", "min": "4300", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "ARENA", "de": "ESTRELA", "para": "BH SHOPPING", "rumos": "138° / 318°", "max": "4600", "min": "4300", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CAETÉ", "de": "SABARÁ", "para": "CAETÉ", "rumos": "115° / 295°", "max": "4300", "min": "4100", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CAETÉ", "de": "CAETÉ", "para": "RAVENA", "rumos": "336° / 156°", "max": "4600", "min": "4500", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CAETÉ", "de": "RAVENA", "para": "VELHAS", "rumos": "016° / 196°", "max": "4500", "min": "4100", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CAPIM BRANCO", "de": "CAPIM BRANCO", "para": "VERA CRUZ", "rumos": "174° / 354°", "max": "3900", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CEASA", "de": "PEDREIRA", "para": "CEASA", "rumos": "146° / 326°", "max": "4000", "min": "3800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CEASA", "de": "CEASA", "para": "PRATES", "rumos": "127° / 307°", "max": "4000", "min": "3800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CEASA", "de": "PRATES", "para": "PARQUE", "rumos": "130° / 310°", "max": "4000", "min": "3800", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "FLORES", "para": "GARAGEM", "rumos": "120° / 300°", "max": "4100", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "GARAGEM", "para": "ARENA MRV", "rumos": "120° / 300°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "ARENA MRV", "para": "MATER DEI", "rumos": "109° / 289°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CENTRAL", "de": "MATER DEI", "para": "PARQUE", "rumos": "111° / 291°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CHAMINÉ", "de": "ESMERALDAS", "para": "GARAGEM", "rumos": "161° / 341°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CHAMINÉ", "de": "GARAGEM", "para": "CHAMINÉ", "rumos": "138° / 318°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CHAMINÉ", "de": "CHAMINÉ", "para": "VALLOUREC", "rumos": "153° / 333°", "max": "4000", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "MATRIZ STA LUZIA", "para": "VELHAS", "rumos": "041° / 221°", "max": "3600", "min": "3500", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "VELHAS", "para": "ESTÂNCIA", "rumos": "338° / 158°", "max": "3600", "min": "3400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "ESTÂNCIA", "para": "ROCHEDO", "rumos": "301° / 121°", "max": "3500", "min": "3400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CIPÓ", "de": "ROCHEDO", "para": "MINERADORA", "rumos": "270° / 090°", "max": "3500", "min": "3400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "CONFINS", "de": "CIDADE ADM", "para": "GALO", "rumos": "013° / 193°", "max": "3500", "min": "3500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "CONFINS", "de": "GALO", "para": "LAGOA DOS MARES", "rumos": "357° / 177°", "max": "3500", "min": "3500", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "ESMERALDAS", "de": "PEDREIRA", "para": "ESMERALDAS", "rumos": "324° / 144°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "ESMERALDAS", "de": "ESMERALDAS", "para": "CHALÉS", "rumos": "017° / 197°", "max": "4000", "min": "3900", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "HARAS", "de": "GALPÕES", "para": "HARAS", "rumos": "019° / 199°", "max": "4100", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "HARAS", "de": "HARAS", "para": "CAPIM BRANCO", "rumos": "019° / 199°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "JABOTICATUBAS", "de": "VELHAS", "para": "JABOTICATUBAS", "rumos": "050° / 230°", "max": "4100", "min": "3400", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "LAGOA", "de": "OLHOS", "para": "LAGOA", "rumos": "082° / 262°", "max": "3600", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "LAGOA", "de": "LAGOA", "para": "VELHAS", "rumos": "098° / 278°", "max": "3600", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "LESTE", "de": "MATRIZ STA LUZIA", "para": "RAVENA", "rumos": "141° / 321°", "max": "4500", "min": "4100", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "LESTE", "de": "RAVENA", "para": "VIADUTO", "rumos": "095° / 275°", "max": "4500", "min": "4400", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NEVES", "de": "ESMERALDAS", "para": "GALPÕES", "rumos": "068° / 248°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NEVES", "de": "GALPÕES", "para": "VERA CRUZ", "rumos": "063° / 243°", "max": "3900", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NEVES", "de": "VERA CRUZ", "para": "LAGOA DOS MARES", "rumos": "086° / 266°", "max": "3800", "min": "3700", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "ETE", "para": "VERA CRUZ", "rumos": "352° / 172°", "max": "3900", "min": "3600", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "VERA CRUZ", "para": "HARAS", "rumos": "324° / 144°", "max": "3900", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "HARAS", "para": "PEDÁGIO", "rumos": "324° / 144°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "PEDÁGIO", "para": "CAPIM BRANCO", "rumos": "080° / 260°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NORTE", "de": "CAPIM BRANCO", "para": "MINERADORA", "rumos": "089° / 269°", "max": "3800", "min": "3500", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NOVA LIMA", "de": "BH SHOPPING", "para": "NOVA LIMA", "rumos": "122° / 302°", "max": "4700", "min": "4600", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "NOVA LIMA", "de": "NOVA LIMA", "para": "RIO ACIMA", "rumos": "166° / 346°", "max": "4700", "min": "3800", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "OESTE", "de": "LAGOA PETROBRÁS", "para": "VALLOUREC", "rumos": "083° / 263°", "max": "4100", "min": "3800", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "OESTE", "de": "VALLOUREC", "para": "INTERLOGOS", "rumos": "085° / 265°", "max": "4100", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "OESTE", "de": "INTERLOGOS", "para": "PARQUE", "rumos": "082° / 262°", "max": "4200", "min": "4100", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "PONTE", "de": "ESTÂNCIA", "para": "PONTE", "rumos": "208° / 028°", "max": "3500", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "PRATES", "de": "GARAGEM", "para": "PRATES", "rumos": "104° / 284°", "max": "4000", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "RAPOSOS", "de": "HELICENTRO", "para": "NOVA LIMA", "rumos": "081° / 261°", "max": "5000", "min": "5000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "RAPOSOS", "de": "NOVA LIMA", "para": "RAPOSOS", "rumos": "088° / 268°", "max": "4300", "min": "3800", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "RAPOSOS", "de": "RAPOSOS", "para": "CAETÉ", "rumos": "086° / 266°", "max": "4300", "min": "4300", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "SABARÁ", "de": "NOVA LIMA", "para": "SABARÁ", "rumos": "047° / 227°", "max": "4300", "min": "3900", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "SABARÁ", "de": "SABARÁ", "para": "RAVENA", "rumos": "048° / 228°", "max": "4500", "min": "4300", "rec": true, "esp": "D · APP-BH 120.200"}, {"rota": "SETE LAGOAS", "de": "GARAGEM", "para": "PEDREIRA", "rumos": "008° / 188°", "max": "4000", "min": "3700", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "SETE LAGOAS", "de": "PEDREIRA", "para": "GALPÕES", "rumos": "007° / 187°", "max": "4000", "min": "3900", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "SETE LAGOAS", "de": "GALPÕES", "para": "CHALÉS", "rumos": "350° / 170°", "max": "4000", "min": "3900", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "SETE LAGOAS", "de": "CHALÉS", "para": "PEDÁGIO", "rumos": "001° / 181°", "max": "4000", "min": "3900", "rec": false, "esp": "G · FCA Norte 120.425"}, {"rota": "SUL", "de": "HELICENTRO", "para": "BH SHOPPING", "rumos": "035° / 215°", "max": "5000", "min": "5000", "rec": false, "esp": "G · FCA Sul 122.550"}, {"rota": "SUL", "de": "BH SHOPPING", "para": "PARQUE", "rumos": "037° / 217°", "max": "4400", "min": "4200", "rec": false, "esp": "D · APP-BH 120.200"}, {"rota": "VILLE", "de": "VILLE", "para": "VELHAS", "rumos": "123° / 303°", "max": "3700", "min": "3400", "rec": true, "esp": "D · APP-BH 120.200"}];
const rehPontos = {"ARENA MRV": [-44.01611, -19.93083], "INTERLOGOS": [-43.98131, -19.95386], "ESTRELA": [-43.96778, -19.96333], "BH SHOPPING": [-43.94528, -19.97306], "SABARÁ": [-43.81444, -19.895], "CAETÉ": [-43.67083, -19.89833], "RAVENA": [-43.77194, -19.80972], "VELHAS": [-43.79778, -19.61389], "CAPIM BRANCO": [-44.14056, -19.55083], "VERA CRUZ": [-44.05361, -19.6975], "PEDREIRA": [-44.09333, -19.86917], "CEASA": [-44.04972, -19.89583], "PRATES": [-43.98863, -19.90994], "PARQUE": [-43.93306, -19.92611], "FLORES": [-44.16558, -19.91388], "GARAGEM": [-44.07779, -19.92386], "MATER DEI": [-43.9575, -19.92694], "ESMERALDAS": [-44.17278, -19.825], "CHAMINÉ": [-44.02389, -19.94722], "VALLOUREC": [-44.00194, -19.96444], "MATRIZ STA LUZIA": [-43.85056, -19.77028], "ESTÂNCIA": [-43.90722, -19.50972], "ROCHEDO": [-44.00772, -19.49602], "MINERADORA": [-44.09167, -19.53], "CIDADE ADM": [-43.94889, -19.78417], "GALO": [-43.95694, -19.74167], "LAGOA DOS MARES": [-43.99472, -19.66861], "CHALÉS": [-44.19, -19.67694], "GALPÕES": [-44.12222, -19.77639], "HARAS": [-44.13229, -19.65261], "JABOTICATUBAS": [-43.7475, -19.51861], "OLHOS": [-43.91008, -19.64869], "LAGOA": [-43.89351, -19.63914], "VIADUTO": [-43.67667, -19.78083], "ETE": [-44.00583, -19.77361], "PEDÁGIO": [-44.22194, -19.60139], "NOVA LIMA": [-43.85778, -19.98583], "RIO ACIMA": [-43.78056, -20.08083], "LAGOA PETROBRÁS": [-44.11444, -20.02583], "PONTE": [-43.91143, -19.56004], "HELICENTRO": [-43.96222, -20.04722], "RAPOSOS": [-43.80806, -19.96361], "VILLE": [-43.9041, -19.59583]};
const portoes = {"REA": {"INTERSEÇÃO": "SBBH", "PAZ": "SBBH", "MINA": "SBBH", "CAMPINHO": "SBCF/SBLS", "PONTE": "SBCF", "JABOTICATUBAS": "SBLS"}, "REH": {"CEASA": "SBBH", "CIDADE ADM": "SBBH", "ETE": "SBBH", "MATRIZ STA LUZIA": "SBBH", "PARQUE": "SBBH", "LAGOA DOS MARES": "SBCF", "PONTE": "SBCF", "VILLE": "SBCF", "LAGOA": "SBLS", "OLHOS": "SBLS"}};
var corRec = '#c026d3', corObr = '#0284c7', corReh = '#0f766e', corRehRec = '#b45309';
var grupoRea = L.featureGroup();
var reaRotuladas = {};
reaTrechos.forEach(function (t) {
    var a = paraLatLng(reaPontos[t.de]), b = paraLatLng(reaPontos[t.para]);
    var cor = t.rec ? corRec : corObr;
    L.polyline([a, b], { color: cor, weight: 4, opacity: 0.9, dashArray: t.rec ? null : '8 6' })
        .bindPopup('<b>REA ' + t.rota + '</b><br>' + t.de + ' ⇄ ' + t.para + '<br>Rumos: ' + t.rumos +
            '<br>Máx. / mín. (ft): ' + t.max + ' / ' + t.min + '<br>' + t.esp +
            (t.rec ? '<br>Recomendada: autorização do APP antes de entrar' : '<br>Obrigatória') +
            (t.rev ? '<br>Sentido conforme a pista de SBBH' : ''))
        .addTo(grupoRea);
    // Um rótulo por corredor no trecho do meio; os demais trechos só com zoom maior
    var trechosRea = reaTrechos.filter(function (x) { return x.rota === t.rota; });
    var principal = trechosRea[Math.floor((trechosRea.length - 1) / 2)] === t;
    L.marker([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2], { opacity: 0, interactive: false, icon: L.divIcon({ className: '', iconSize: [0, 0] }) })
        .bindTooltip(t.rota, { permanent: true, direction: 'center', className: principal ? 'rea-rotulo' : 'rea-rotulo rea-rotulo-trecho' })
        .addTo(grupoRea);
});
Object.keys(reaPontos).forEach(function (n) {
    var portao = portoes.REA[n];
    L.circleMarker(paraLatLng(reaPontos[n]), portao ?
        { radius: 5, color: '#0f172a', weight: 2, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 3.5, color: '#334155', weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Portão ' + n + ' (' + portao + ')' : n).addTo(grupoRea);
});

var grupoReh = L.featureGroup();
var rehRotuladas = {};
rehTrechos.forEach(function (t) {
    var linha = [paraLatLng(rehPontos[t.de]), paraLatLng(rehPontos[t.para])];
    var classeG = t.esp.charAt(0) === 'G';
    L.polyline(linha, { color: t.rec ? corRehRec : corReh, weight: 2.5, opacity: 0.9, dashArray: classeG ? '5 4' : null })
        .bindPopup('<b>REH ' + t.rota + '</b><br>' + t.de + ' ⇄ ' + t.para + '<br>Rumos: ' + t.rumos +
            '<br>Máx. / mín. (ft): ' + t.max + ' / ' + t.min + '<br>' + t.esp +
            (t.rec ? '<br>Recomendada: autorização do APP antes de entrar' : '<br>Obrigatória'))
        .addTo(grupoReh);
    // Um rótulo por REH, no primeiro trecho, só com zoom maior
    if (!rehRotuladas[t.rota]) {
        rehRotuladas[t.rota] = true;
        L.marker([(linha[0][0] + linha[1][0]) / 2, (linha[0][1] + linha[1][1]) / 2], { opacity: 0, interactive: false, icon: L.divIcon({ className: '', iconSize: [0, 0] }) })
            .bindTooltip(t.rota, { permanent: true, direction: 'center', className: 'reh-rotulo' })
            .addTo(grupoReh);
    }
});
Object.keys(rehPontos).forEach(function (n) {
    var portao = portoes.REH[n];
    L.circleMarker(paraLatLng(rehPontos[n]), portao ?
        { radius: 4, color: '#0f172a', weight: 1.5, fillColor: '#facc15', fillOpacity: 1 } :
        { radius: 2.5, color: corReh, weight: 1.5, fillColor: '#ffffff', fillOpacity: 1 })
        .bindTooltip(portao ? 'Portão ' + n + ' (' + portao + ')' : n).addTo(grupoReh);
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
    "Corredores visuais (REA)": grupoRea,
    "Rotas de helicópteros (REH)": grupoReh
}).addTo(mapa);

// Rótulos dos corredores só com zoom suficiente para não embolar
function detalheRea() {
    elemento.classList.toggle('rea-zoom-baixo', mapa.getZoom() < 8);
    elemento.classList.toggle('rea-zoom-medio', mapa.getZoom() < 10);
    elemento.classList.toggle('reh-zoom-baixo', mapa.getZoom() < 11);
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
        '<div><span class="rea-linha"></span>REA recomendada</div>' +
        '<div><span class="rea-linha g"></span>REA obrigatória (G)</div>' +
        '<div><span style="background:#facc15;border-radius:50%"></span>Portão</div>';
    return div;
};
legenda.addTo(mapa);

})();
</script>
