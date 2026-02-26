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

> WSBZ21 SBBS 051430
> *Sigmet Geral emitido pelo Brasil, com número de boletim 21. Dissemimado pela FIR Brasília, no dia 05 às 1430z.*

O cabeçalho do SIGMET não costuma constar nas mensagens SIGMET, mas quando presente contém as seguintes informações:

- **Tipo da Mensagem:** código de 2 letras que indica o tipo da mensagem. No caso do SIGMET geral, o código é "WS". Para o SIGMET de cinza vulcânica, o código é "VA" ou "WV". Para o SIGMET de ciclone tropical, o código é "TC".
- **Indicativo da Estação Emissora:** código de 2 letras que identifica o país ou território emissor do SIGMET. A lista de códigos para países e territórios pode ser vista no [Glossário](../glossario/#codigos-de-paises-e-territorios-no-padrao-do-sigmet).
- **Número Identificador do Boletim:** número interno de boletim. Não é relevante para a simulação.
- **FIR disseminadora:** código da FIR que está disseminando o SIGMET.
- **Data e Hora de Emissão:** data e hora em que o SIGMET foi emitido, no formato DDHHMMz, onde DD é o dia do mês, HH é a hora em formato 24h e MM são os minutos.

### Corpo da Mensagem

> SBBS SIGMET 17 VALID 151930/152330 SBBS - SBBS BRASILIA FIR EMBD TS FCST WI S1724 W05407 - S1737 W05355 - S2044 W05102 - S1648 W04733 - S1557 W04333 - S1538 W04406 - S1320 W04534 - S1200 W04654 - S1020 W04719 - S1017 W04741 - S0944 W04758 - S0937 W04822 - S0950 W04852 - S1013 W04902 - S1031 W05105 - S1211 W05303 - S1258 W05330 - S1434 W05338 - S1643 W05306 - S1724 W05407 TOP FL480 STNR NC=
> *SIGMET número 17, válido de 15 às 1930z até 15 às 2330z, para a FIR Brasília, relativo a tempestade embebida (EMBD TS) prevista (FCST) dentro (WI) da área delimitada pelas coordenadas apresentadas, com topo (TOP) no FL480, estacionária (STNR) e sem mudança significativa prevista (NC=).*

#### FIR atingida

A primeira informação do SIGMET é o código da FIR atingida, isto é, a que FIR que será afetada pelo fenômeno meteorológico. No exemplo, o código da FIR é `SBBS`, que corresponde à FIR Brasília.

#### Número do SIGMET

O número do SIGMET é um número sequencial que é incrementado a cada novo SIGMET emitido para a mesma FIR. No exemplo, o número do SIGMET é `17`, indicando que este é o 17º SIGMET emitido para a FIR Brasília.

#### Período de validade

O período de validade do SIGMET é indicado por um intervalo de tempo no formato DDHHMM/DDHHMM, onde o primeiro DDHHMM indica o início da validade e o segundo DDHHMM indica o término da validade. No exemplo, o período de validade é de 15 às 1930z até 15 às 2330z.

