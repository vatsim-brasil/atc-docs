---
title: SIGMET
icon: material/alert-circle
---

--8<-- "includes/abreviacoes.md"

![Manual de Fraseologia - SIGMET](img/manual-meteorologia-notam.png)

#

## Definição

SIGMET é uma mensagem relativa à ocorrência ou previsão de determinados fenômenos meteorológicos (gelo, ciclone, trovoada e turbulência) em rota e de outros fenômenos na atmosfera (cinzas vulcânicas, nuvem radioativa e vulcão) que possam afetar a segurança das operações aéreas, e evolução desses fenômenos no tempo e no espaço.

## Tipos de SIGMET

Por definição, existem três tipos de SIGMET:

- **SIGMET de Cinza Vulcânica** (VA SIGMET ou WV SIGMET): mensagem relativa à ocorrência ou previsão de cinzas vulcânicas;
- **SIGMET de Ciclone Tropical** (TC SIGMET): mensagem relativa à ocorrência ou previsão de ciclones tropicais;
- **SIGMET para qualquer outro fenômeno meteorológico** (WS SIGMET) que possa afetar a segurança das operações aéreas, exceto os fenômenos relacionados a cinzas vulcânicas e ciclones tropicais, sendo eles: tempestade (TS), turbulência (TURB), gelo (ICE), ondas de montanha (MTW), tempestade de poeira (DS), tempestade de areia (SS) ou nuvem radioativa (RDOACT CLD)

## Estrutura de um SIGMET

```
WSBZ21 SBBS 051430
SBBS SIGMET 17 VALID 151930/152330 SBBS - SBBS BRASILIA FIR EMBD TS FCST WI S1724 W05407 - S1737 W05355 - S2044 W05102 - S1648 W04733 - S1557 W04333 - S1538 W04406 - S1320 W04534 - S1200 W04654 - S1020 W04719 - S1017 W04741 - S0944 W04758 - S0937 W04822 - S0950 W04852 - S1013 W04902 - S1031 W05105 - S1211 W05303 - S1258 W05330 - S1434 W05338 - S1643 W05306 - S1724 W05407 TOP FL480 STNR NC=
```

### Cabeçalho

> WSBZ21 SBBS 051430<br/>
> *Sigmet Geral emitido pelo Brasil, com número de boletim 21. Dissemimado pela FIR Brasília, no dia 05 às 1430z.*

O cabeçalho do SIGMET não costuma constar nas mensagens SIGMET, mas quando presente contém as seguintes informações:

- **Tipo da Mensagem:** código de 2 letras que indica o tipo da mensagem. No caso do SIGMET geral, o código é "WS". Para o SIGMET de cinza vulcânica, o código é "VA" ou "WV". Para o SIGMET de ciclone tropical, o código é "TC".
- **Indicativo da Estação Emissora:** código de 2 letras que identifica o país ou território emissor do SIGMET. A lista de códigos para países e territórios pode ser vista no [Glossário](../glossario/#codigos-de-paises-e-territorios-no-padrao-do-sigmet).
- **Número Identificador do Boletim:** número interno de boletim. Não é relevante para a simulação.
- **FIR disseminadora:** código da FIR que está disseminando o SIGMET.
- **Data e Hora de Emissão:** data e hora em que o SIGMET foi emitido, no formato DDHHMMz, onde DD é o dia do mês, HH é a hora em formato 24h e MM são os minutos.

### Corpo da Mensagem

> SBBS SIGMET 17 VALID 151930/152330 SBBS - SBBS BRASILIA FIR EMBD TS FCST WI S1724 W05407 - S1737 W05355 - S2044 W05102 - S1648 W04733 - S1557 W04333 - S1538 W04406 - S1320 W04534 - S1200 W04654 - S1020 W04719 - S1017 W04741 - S0944 W04758 - S0937 W04822 - S0950 W04852 - S1013 W04902 - S1031 W05105 - S1211 W05303 - S1258 W05330 - S1434 W05338 - S1643 W05306 - S1724 W05407 TOP FL480 STNR NC=<br/>
> *SIGMET número 17, válido de 15 às 1930z até 15 às 2330z, para a FIR Brasília, relativo a tempestade embebida (EMBD TS) prevista (FCST) dentro (WI) da área delimitada pelas coordenadas apresentadas, com topo (TOP) no FL480, estacionária (STNR) e sem mudança significativa prevista (NC=).*

#### Indicador da localidade da FIR ou CTA de referência

> SBBS<br/>
> *FIR Brasília*

A primeira informação do SIGMET é o código da FIR a que refere a informação SIGMET, isto é, a que FIR que será afetada pelo fenômeno meteorológico. No exemplo, o código da FIR é `SBBS`, que corresponde à FIR Brasília.

#### Identificação da informação e número sequencial

> SIGMET 17<br/>
> *Número do SIGMET: 17*

O número do SIGMET é um número sequencial que é incrementado a cada novo SIGMET emitido para a mesma FIR. No exemplo, o número do SIGMET é `17`, indicando que este é o 17º SIGMET emitido para a FIR Brasília.

#### Período de validade

> VALID 151930/152330<br/>
> *Válido de 15 às 1930z até 15 às 2330z.*

O período de validade do SIGMET é indicado por um intervalo de tempo no formato DDHHMM/DDHHMM, onde o primeiro DDHHMM indica o início da validade e o segundo DDHHMM indica o término da validade. No exemplo, o período de validade é de 15 às 1930z até 15 às 2330z.

#### Indicador do Centro Meteorológico originador

> SBBS -<br/>
> *Centro mmeteorológico: FIR Brasília*

O Centro Meteorológico originador é a FIR que realizou a observação ou previsão do fenômeno meteorológico. No exemplo, o Centro Meteorológico originador é o da FIR Brasília, indicada pelo código `SBBS`.

#### Indicador de localidade e nome para a qual se expede a informação

> SBBS BRASILIA FIR<br/>
> *FIR de referência: FIR Brasília*

O indicador de localidade e nome para a qual se expede a informação é a FIR ou CTA de referência para a qual o SIGMET é emitido. No exemplo, o SIGMET é emitido para a FIR Brasília, indicada pelo código `SBBS` e pelo nome "BRASILIA FIR".

#### Descrição do fenômeno meteorológico

> EMBD TS<br/>
> *Fenômeno meteorológico: tempestade embutida*

Descrição do fenômeno meteorológico, utilizando as abreviaturas apresentadas no [Glossário](../glossario/#fenomenos-sigmet).

#### Tipo da Informação

> FCST<br/>
> *Tipo da informação: previsão*

Tipo da informação fornecida. Há duas opções para essa informação:

- **OBS:** informação baseada em observação;
- **FCST:** informação baseada em previsão.

#### Localização

> WI S1724 W05407 - S1737 W05355 - S2044 W05102 - S1648 W04733 - S1557 W04333 - S1538 W04406 - S1320 W04534 - S1200 W04654 - S1020 W04719 - S1017 W04741 - S0944 W04758 - S0937 W04822 - S0950 W04852 - S1013 W04902 - S1031 W05105 - S1211 W05303 - S1258 W05330 - S1434 W05338 - S1643 W05306 - S1724 W05407<br/>
> *Coordenadas que delimitam a área afetada pelo fenômeno meteorológico.*

Localização do fenômeno meteorológico, expresso numa série de informações indicadas por latitudes e longitudes, em graus e minutos.

A apresentação da área afetada pelo fenômeno meteorológico pode ser feita de algumas formas:

1. **Ponto:** a área é representada por um ponto, indicado por uma única coordenada;

> `N2020 W07005`<br/>
> `N48 E010`<br/>
> `S60 W160`<br/>
> `S0530 E16530`<br/>

2. **Posição de Referência:** a área é representada por uma referência relativa a um ponto ou uma linha, expressa em função da posição cardeal (N, S, E, W);

| Relativo a um ponto | Relativo a vários pontos     | Relativo a uma linha                                                |
|---------------------|------------------------------|---------------------------------------------------------------------|
| `N OF N50`          | `N OF N1515 AND W OF E17530` | `N OF LINE S2520 W11510 – S2520 W12010`                             |
| `S OF N5430`        | `S OF N45 AND N OF N40`      | `SW OF LINE N50 W005 – N60 W020`                                    |
| `N OF S10`          | `N OF S45 AND E OF W155`     | `SW OF LINE N50 W020 – N45 E010 AND NE OF LINE N45 W020 – N40 E010` |
| `S OF S4530`        | 
| `W OF W155`         |
| `E OF W45`          |
| `W OF E15540`       |
| `E OF E09015`       |

3. **Polígono:** a área é delimitada por uma série de coordenadas que formam um polígono;

> `WI N6030 E02550 – N6055 E02500 – N6050 E02630 – N6030 E02550`

4. **Largura de uma Linha:** a área é representada por uma linha e uma largura;

> `APRX 50KM WID LINE BTN N64 W017 – N60 W010 – N57 E010`

5. **FIR/UIR/CTA:** a área é a FIR, UIR ou CTA inteira referenciada;

> `ENTIRE FIR`<br/>
> `ENTIRE UIR`<br/>
> `ENTIRE FIR/UIR`<br/>
> `ENTIRE CTA`<br/>

6. **Área Circular:** a área é representada por um círculo, indicado por um ponto central e um raio.

> `WI 400KM OF TC CENTRE`<br/>
> `WI 250NM OF TC CENTRE`<br/>
> `WI 30KM OF N6030 E02550`<br/>

#### Nível ou Altitude

Indicação da altitude do fenômeno meteorológico, expresso em altitude ou nível de voo.  Pode ser realizada de algumas formas:

1. **Altitude ou Nível de Voo:** indica a altitude do fenômeno ou a faixa de sua ocorrência (piso-teto) indicada em pés ou metros ou nível de voo indicado por "FL" seguido de três dígitos em centenas de pés;
2. **Topo:** indica a altitude do topo do fenômeno meteorológico, indicada por "TOP" seguido de um nível de voo ou altitude;

| Altitude ou Nível de Voo | Faixa de Altitude ou Nível de Voo | Topo              |
|--------------------------|-----------------------------------|-------------------|
| `FL180`                  | `SFC/FL070`                       | `TOP FL390`       |
| `3000M`                  | `SFC/3000M`                       | `TOP ABV FL100`   |
| `8000FT`                 | `SFC/10000FT`                     | `TOP ABV 9000FT`  |
|                          | `FL050/FL080`                     | `TOP ABV 10000FT` |
|                          | `ABV FL250`                       | `TOP FL500`       |
|                          | `ABV 7000FT`                      | `TOP BLW FL450`   |
|                          | `2000/3000M`                      |                   |
|                          | `2000/3000M`                      |                   |
|                          | `6000/12000FT`                    |                   |
|                          | `2000M/FL150`                     |                   |
|                          | `10000FT/FL250`                   |                   |

#### Movimento do Fenômeno

Indicação do movimento ou do movimento esperado do fenômeno meteorológico (direção e velocidade) em relação aos pontos cardeais, colaterais ou subcolaterais ou estacionário.

> `MOV SE`<br/>
> `MOV NNW`<br/>
> `MOV E 40KMH`<br/>
> `MOV E 20KT`<br/>
> `MOV WSW 20KT`<br/>
> `STNR`

#### Mudanças de Intensidade

Indicação de mudanças de intensidade do fenômeno meteorológico, utilizando as seguintes abreviaturas:

* `INTSF`: intensificando-se;
* `WKN`: enfraquecendo-se;
* `NC`: sem mudança significativa prevista.

#### Hora Prevista

Indicaçlão do horário previsto de ocorrência do fenômeno.

> `FCST AT 2200Z`

#### Posição Prevista do Ciclone Tropical

Posição prevista do centro do ciclone tropical, indicada por coordenadas.

> `TC CENTRE PSN N1030 E16015`<br/>
> `TC CENTRE PSN N1015 E15030 CB`<br/>

## Exemplos Práticos de Sigmet

??? info "`SBBS SIGMET 24 VALID 052330/060330 SBBS - SBBS BRASILIA FIR EMBD TS FCST WI S1833 W04539 - S1631 W04230 - S1538 W04406 - S1502 W04426 - S1430 W04448 - S1322 W04533 - S1544 W04844 - S1833 W04539 TOP FL470 STNR NC=`"

    - `SBBS`: FIR de Referência, FIR Brasília
    - `SIGMET 24`: número do SIGMET
    - `VALID 052330/060330`: válido de 05 às 2330z até 06 às 0330z
    - `SBBS -`: Centro Meteorológico originador, FIR Brasília
    - `SBBS BRASILIA FIR`: Localidade para a qual se expede a informação, FIR Brasília
    - `EMBD TS`: fenômeno meteorológico, tempestade embutida
    - `FCST`: tipo da informação, previsão
    - `WI S1833 W04539 - S1631 W04230 - (...)`: localização do fenômeno meteorológico, área delimitada por um polígono formado pelas coordenadas apresentadas
    - `TOP FL470`: topo do fenômeno meteorológico, FL470
    - `STNR`: fenômeno estacionário
    - `NC=`: sem mudança significativa prevista

??? info "`SBAO SIGMET 31 VALID 052330/060330 SBAO - SBAO ATLANTICO FIR SEV ICE FCST WI S1948 W03822 - S2221 W03535 - S2736 W03716 - S3324 W03607 - S3422 W03516 - S3416 W03353 - S3204 W03219 - S2853 W03250 - S2524 W03125 - S2408 W03054 - S2151 W02959 - S1623 W03509 - S1548 W03640 - S1618 W03702 - S1841 W03815 - S1852 W03740 - S1947 W03821 - S1948 W03822 FL120/220 STNR NC=`"

    - `SBAO`: FIR de Referência, FIR Atlântico
    - `SIGMET 31`: número do SIGMET
    - `VALID 052330/060330`: válido de 05 às 2330z até 06 às 0330z
    - `SBAO -`: Centro Meteorológico originador, FIR Atlântico
    - `SBAO ATLANTICO FIR`: Localidade para a qual se expede a informação, FIR Atlântico
    - `SEV ICE`: fenômeno meteorológico, gelo severo
    - `FCST`: tipo da informação, previsão
    - `WI S1948 W03822 - S2221 W03535 - (...)`: localização do fenômeno meteorológico, área delimitada por um polígono formado pelas coordenadas apresentadas
    - `FL120/220`: faixa de altitude do fenômeno meteorológico, entre FL120 e FL220
    - `STNR`: fenômeno estacionário
    - `NC=`: sem mudança significativa prevista