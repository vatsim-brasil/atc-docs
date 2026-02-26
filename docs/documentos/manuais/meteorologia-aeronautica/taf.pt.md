---
title: TAF
icon: material/weather-rainy
---

--8<-- "includes/abreviacoes.md"

![Manual de Meteorologia - TAF](img/manual-meteorologia-taf.png)

#

## Definição

TAF (Terminal Aerodrome Forecast) é uma previsão meteorológica codificada para um aeródromo específico, focada em condições relevantes para operações de aviação.

## Estrutura da mensagem

Um TAF será codificado da seguinte forma:

| Tipo    | Localidade | Data/hora | Validade    | Previsão Inicial            | Temperatura Máxima e Mínima | Mudanças de Previsão                                                                                | Informações Suplementares |
| :------ | :--------- | :-------- | :---------- | :-------------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------- | :------------------------ |
| `TAF`   | `SBGL`     | `012004Z` | `0200/0306` | `14007KT 9999 +SHRA SCT020` | `TN25/0208Z TX33/0217Z`     | `BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB` | `RMK PHI`                 |

<!-- TAF normalmente contém:

- **Localidade**
- **Emissão (UTC)**
- **Validade** (janela)
- **Condição base**
- **Grupos de mudança**: `BECMG`, `TEMPO`, `PROBxx`, `FM` (quando aplicável)
- **Temperaturas**: `TX..` / `TN..` (quando fornecidas)
- **RMK**: observações

!!! warning "Operacional"
    Para decisão, foque no **pior caso dentro da janela relevante** (especialmente `TEMPO` e `PROB`). -->

---

## Descrição de cada grupo

### Tipo

> `[TAF] SBGL 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Previsão meteorológica.

A palavra inicial é sempre `TAF`, indicando o tipo de mensagem.

---

### Emenda ou Correção de TAF

> `TAF [COR] SBGL 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Correção do TAF.

Caso um TAF seja emendado com novas informações, o termo `AMD` (amendment) será inserido logo após o tipo da mensagem. Já se o TAF for corrigido em alguma informação errada, uma mensagem de correção será emitida e nela constará a palavra `COR` logo após o tipo da mensagem.

---

### Localidade

> `TAF [SBGL] 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Aeródromo do Galeão (SBGL).

O código ICAO de quatro letras identifica o aeródromo onde a observação foi realizada. Maiores detalhes sobre códigos ICAO podem ser vistos na página [METAR/SPECI](../metar-speci).

---

### Data e Hora da Emissão

> `TAF SBGL [012004Z] 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Emitido no dia 1º do mês às 20:04 UTC.

Este grupo indica o dia do mês e a hora da emissão da previsão em UTC, em formato 24 horas, seguido pela letra `Z`.

!!! example "Exemplos"

    - `291200Z`: observação realizada no dia 29 do mês atual às 1200Z;
    - `040800Z`: observação realizada no dia 4 do mês atual às 0800Z;
    - `150530Z`: observação realizada no dia 15 do mês atual às 0530Z;
    - `011500Z`: observação realizada no dia 1º do mês atual às 1500Z;
    - `312027Z`: observação realizada no dia 31 do mês atual às 2027Z.

---

### Período de Validade

> `TAF SBGL 012004Z [0200/0306] 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Válido de 00:00 UTC do dia 2 até 06:00 UTC do dia 3 (30 horas).

O período de validade do TAF é indicado por dois grupos de quatro dígitos separados por uma barra (`/`). O primeiro grupo indica o dia do mês e a hora UTC de início da validade, e o segundo grupo indica o dia do mês e a hora UTC de término da validade.

!!! example "Exemplos"

    - `2912/3018`: válido do dia 29 às 12:00 UTC até o dia 30 às 18:00 UTC;
    - `0406/0506`: válido do dia 4 às 06:00 UTC até o dia 5 às 06:00 UTC;
    - `1500/1606`: válido do dia 15 às 00:00 UTC até o dia 16 às 06:00 UTC;
    - `0112/0212`: válido do dia 1º às 12:00 UTC até o dia 2 às 12:00 UTC;
    - `3118/0200`: válido do dia 31 às 18:00 UTC até o dia 2 às 00:00 UTC.

---

### Previsão Inicial (Base)

> `TAF SBGL 012004Z 0200/0306 [14007KT 9999 SCT020] TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Previsão inicial de vento de 140° a 7 nós, visibilidade superior a 10 km, nuvens esparsas a 2000 pés.

Este grupo descreve as condições meteorológicas esperadas no início do período de validade do TAF. Inclui informações sobre vento, visibilidade, cobertura de nuvens e outros fenômenos meteorológicos relevantes.

Sua interpretação seguem as mesmas regras do METAR/SPECI, conforme descrito [aqui](../metar-speci).

---

### Temperaturas Máxima e Mínima

> `TAF SBGL 012004Z 0200/0306 14007KT 9999 SCT020 [TN25/0208Z TX33/0217Z] BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Temperatura mínima de 25°C às 08:00 UTC do dia 2 e máxima de 33°C às 17:00 UTC do dia 2.

Este grupo fornece as temperaturas mínima (`TN`) e máxima (`TX`) esperadas durante o período de validade do TAF, juntamente com os horários em que essas temperaturas são previstas para ocorrer.

Logo após o código `TN` ou `TX`, temos a temperatura em graus Celsius, seguida por uma barra (`/`) e o dia do mês e hora UTC em que a temperatura é esperada.

??? example "Exemplos"

    - `TN18/1812Z TX24/1818Z`: temperatura mínima de 18°C às 12:00 UTC do dia 18 e máxima de 24°C às 18:00 UTC do dia 18;
    - `TN21/3008Z TX36/3018Z`: temperatura mínima de 21°C às 08:00 UTC do dia 30 e máxima de 36°C às 18:00 UTC do dia 30;
    - `TN23/2924Z TX34/2918Z`: temperatura mínima de 23°C às 24:00 UTC do dia 29 e máxima de 34°C às 18:00 UTC do dia 29.

---

### Mudanças de Previsão

> `TAF SBGL 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z [BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB] RMK PHI`<br/>
> Mudanças previstas...

Dada a natureza dinâmica do tempo, o TAF pode incluir grupos que indicam mudanças esperadas nas condições meteorológicas durante o período de validade. Os principais grupos são:

| Grupo    | Descrição                                                                                          |
| :------  | :------------------------------------------------------------------------------------------------  |
| `BECMG`  | Indica uma mudança **definitiva**, que ocorrerá de forma **gradual**.                              |
| `FM`     | Indica uma mudança **definitiva**, que ocorrerá de forma **imediata**.                             |
| `TEMPO`  | Indica uma mudança **temporária**, que ocorrerá por um período limitado dentro da validade do TAF. |
| `PROB30` | Indica uma mudança **temporária ou definitiva** com **probabilidade de 30%**.                      |
| `PROB40` | Indica uma mudança **temporária ou definitiva** com **probabilidade de 40%**.                      |

A tabela abaixo permite entender melhor a dinâmica dessas mudanças:

| Período     | Previsão                                                                |
| :---------: | :---------------------------------------------------------------------: |
| Dia 02, 00Z | **Início de Mudança Gradual**<br/>`BECMG`                               |
| Dia 02, 01Z | ...                                                                     |
| Dia 02, 02Z | **Estado após a Mudança Gradual**<br/>`33005KT`                         |
| Dia 02, 03Z | ...                                                                     |
| Dia 02, 04Z | ...                                                                     |
| Dia 02, 05Z | ...                                                                     |
| Dia 02, 06Z | **Início de Mudança Gradual**<br/>`BECMG`                               |
| Dia 02, 07Z | ...                                                                     |
| Dia 02, 08Z<br><span style="color:#349beb;font-weight:bold;font-size:0.6rem;">TEMP MIN - 25°C</span> | **Estado após a Mudança Gradual**<br/>`23005KT`  |
| Dia 02, 09Z | ...                                                                     |
| Dia 02, 10Z | ...                                                                     |
| Dia 02, 11Z | ...                                                                     |
| Dia 02, 12Z | ...                                                                     |
| Dia 02, 13Z | ...                                                                     |
| Dia 02, 14Z | ...                                                                     |
| Dia 02, 15Z | ...                                                                     |
| Dia 02, 16Z | ...                                                                     |
| Dia 02, 17Z<br><span style="color:red;font-weight:bold;font-size:0.6rem;">TEMP MÁX - 33°C</span> | ...                                                  |
| Dia 02, 18Z | ...                                                                     |
| Dia 02, 19Z | ...                                                                     |
| Dia 02, 20Z | **Início de Condição Temporária**<br/>`TEMPO 0220/0302 15010KT 4000`    |
| Dia 02, 21Z | ...                                                                     |
| Dia 02, 22Z | ...                                                                     |
| Dia 02, 23Z | ...                                                                     |
| Dia 03, 00Z | ...                                                                     |
| Dia 03, 01Z | ...                                                                     |
| Dia 03, 02Z | **Fim de Condição Temporária**<br/>Retorno à última condição estável    |
| Dia 03, 03Z | ...                                                                     |
| Dia 03, 04Z | ...                                                                     |
| Dia 03, 05Z | ...                                                                     |

---

## Exemplos Práticos de TAF

??? info "`SBGR 022200Z 0300/0406 00000KT 9999 FEW020 TN19/0308Z TX25/0316Z PROB30 0300/0303 02005KT 7000 RA BKN020 BECMG 0305/0307 SCT010 TEMPO 0308/0311 33008KT 6000 RA BKN009 BECMG 0312/0314 30008KT SCT030 BECMG 0315/0317 BKN030 FEW045TCU TEMPO 0317/0322 6000 TSRA SCT010 BKN020 FEW045CB BECMG 0322/0324 02005KT 8000 RA BKN020 BECMG 0402/0404 NSW BKN008 RMK PGN`"

    - `SBGR`: Aeródromo de Guarulhos.
    - `022200Z`: Emitido no dia 2 às 22:00 UTC.
    - `0300/0406`: Válido do dia 3 às 00:00 UTC até o dia 4 às 06:00 UTC.
    - `00000KT 9999 FEW020`: Condição inicial de vento calmo, visibilidade superior a 10 km, nuvens esparsas a 2000 pés.
    - `TN19/0308Z`: Temperatura mínima de 19°C às 08:00 UTC do dia 3.
    - `TX25/0316Z`: Temperatura máxima de 25°C às 16:00 UTC do dia 3.
    - `PROB30 0300/0303 02005KT 7000 RA BKN020`: Probabilidade de 30% de vento de 020° a 5 nós, visibilidade de 7000 metros, chuva moderada e céu nublado a 2000 pés entre 00:00 e 03:00 UTC do dia 3.
    - `BECMG 0305/0307 SCT010`: Mudança gradual para nuvens esparsas a 1000 pés entre 05:00 e 07:00 UTC do dia 3.
    - `TEMPO 0308/0311 33008KT 6000 RA BKN009`: Condição temporária de vento de 330° a 8 nós, visibilidade de 6000 metros, chuva moderada e céu nublado a 900 pés entre 08:00 e 11:00 UTC do dia 3.
    - `BECMG 0312/0314 30008KT SCT030`: Mudança gradual para vento de 300° a 8 nós e nuvens esparsas a 3000 pés entre 12:00 e 14:00 UTC do dia 3.
    - `BECMG 0315/0317 BKN030 FEW045TCU`: Mudança gradual para céu nublado a 3000 pés e nuvens esparsas a 4500 pés com torre de cumulus entre 15:00 e 17:00 UTC do dia 3.
    - `TEMPO 0317/0322 6000 TSRA SCT010 BKN020 FEW045CB`: Condição temporária de visibilidade de 6000 metros, tempestade com chuva moderada, nuvens esparsas a 1000 pés, céu nublado a 2000 pés e nuvens esparsas a 4500 pés com cumulonimbus entre 17:00 e 22:00 UTC do dia 3.
    - `BECMG 0322/0324 02005KT 8000 RA BKN020`: Mudança gradual para vento de 020° a 5 nós, visibilidade de 8000 metros, chuva moderada e céu nublado a 2000 pés entre 22:00 e 24:00 UTC do dia 3.
    - `BECMG 0402/0404 NSW BKN008`: Mudança gradual para ausência de fenômenos significativos e céu nublado a 800 pés entre 02:00 e 04:00 UTC do dia 4.
    - `RMK PGN`: Observação adicional.

??? info "`TAF LEMD 051700Z 0518/0624 23015KT 9999 SCT020 TX10/0615Z TN06/0607Z TEMPO 0518/0521 4000 RA SHRA FEW030TCU TEMPO 0518/0605 23018G30KT PROB30 TEMPO 0522/0608 BKN010 PROB40 TEMPO 0609/0613 VRB05KT TEMPO 0610/0618 RA SHRA BKN014 FEW030TCU PROB40 TEMPO 0614/0619 23015G27KT`"

    - `LEMD`: Aeródromo de Madrid-Barajas.
    - `051700Z`: Emitido no dia 5 às 17:00 UTC.
    - `0518/0624`: Válido do dia 5 às 18:00 UTC até o dia 6 às 24:00 UTC.
    - `23015KT 9999 SCT020`: Condição inicial de vento de 230° a 15 nós, visibilidade superior a 10 km e nuvens esparsas a 2000 pés.
    - `TX10/0615Z`: Temperatura máxima de 10°C às 15:00 UTC do dia 6.
    - `TN06/0607Z`: Temperatura mínima de 6°C às 07:00 UTC do dia 6.
    - `TEMPO 0518/0521 4000 RA SHRA FEW030TCU`: Condição temporária de visibilidade de 4000 metros, pancadas de chuva moderada, e nuvens esparsas a 3000 pés com torre de cumulus entre 18:00 e 21:00 UTC do dia 5.
    - `TEMPO 0518/0605 23018G30KT`: Condição temporária de vento de 230° a 18 nós com rajadas de até 30 nós entre 18:00 UTC do dia 5 e 05:00 UTC do dia 6.
    - `PROB30 TEMPO 0522/0608 BKN010`: Probabilidade de 30% de céu nublado a 1000 pés entre 22:00 UTC do dia 5 e 08:00 UTC do dia 6.
    - `PROB40 TEMPO 0609/0613 VRB05KT`: Probabilidade de 40% de vento variável a 5 nós entre 09:00 e 13:00 UTC do dia 6.
    - `TEMPO 0610/0618 RA SHRA BKN014 FEW030TCU`: Condição temporária de chuva moderada, pancadas de chuva moderada, céu nublado a 1400 pés e nuvens esparsas a 3000 pés com torre de cumulus entre 10:00 e 18:00 UTC do dia 6.
    - `PROB40 TEMPO 0614/0619 23015G27KT`: Probabilidade de 40% de vento de 230° a 15 nós com rajadas de até 27 nós entre 14:00 e 19:00 UTC do dia 6.

??? info "`TAF SBCT 052100Z 0600/0624 09005KT 8000 SCT020 TN16/0609Z TX27/0617Z PROB30 0600/0606 BKN001 FM060600 09006KT 9999 BKN012 PROB30 0606/0612 BKN002 FM061200 09005KT 8000 BKN030 PROB30 0612/0618 BKN009 FM061800 09006KT 9999 BKN010 PROB30 0618/0622 BKN009 RMK PDE`"

    - `SBCT`: Aeródromo de Curitiba.
    - `052100Z`: Emitido no dia 5 às 21:00 UTC.
    - `0600/0624`: Válido do dia 6 às 00:00 UTC até o dia 6 às 24:00 UTC.
    - `09005KT 8000 SCT020`: Condição inicial de vento de 090° a 5 nós, visibilidade de 8000 metros e nuvens esparsas a 2000 pés.
    - `TN16/0609Z`: Temperatura mínima de 16°C às 09:00 UTC do dia 6.
    - `TX27/0617Z`: Temperatura máxima de 27°C às 17:00 UTC do dia 6.
    - `PROB30 0600/0606 BKN001`: Probabilidade de 30% de céu nublado a 100 pés entre 00:00 e 06:00 UTC do dia 6.
    - `FM060600 09006KT 9999 BKN012`: Mudança imediata a partir das 06:00 UTC do dia 6 para vento de 090° a 6 nós, visibilidade superior a 10 km e céu nublado a 1200 pés.
    - `PROB30 0606/0612 BKN002`: Probabilidade de 30% de céu nublado a 200 pés entre 06:00 e 12:00 UTC do dia 6.
    - `FM061200 09005KT 8000 BKN030`: Mudança imediata a partir das 12:00 UTC do dia 6 para vento de 090° a 5 nós, visibilidade de 8000 metros e céu nublado a 3000 pés.
    - `PROB30 0612/0618 BKN009`: Probabilidade de 30% de céu nublado a 900 pés entre 12:00 e 18:00 UTC do dia 6.
    - `FM061800 09006KT 9999 BKN010`: Mudança imediata a partir das 18:00 UTC do dia 6 para vento de 090° a 6 nós, visibilidade superior a 10 km e céu nublado a 1000 pés.
    - `PROB30 0618/0622 BKN009`: Probabilidade de 30% de céu nublado a 900 pés entre 18:00 e 22:00 UTC do dia 6.
    - `RMK PDE`: Observação adicional.

??? info "`TAF SLLP 052200Z 0600/0624 08006KT 9999 SCT015 FEW017CB TX16/0619Z TN04/0610Z BECMG 0603/0607 3000 BCFG FEW002 BKN010 BECMG 0612/0615 14010KT 9999 NSW SCT015 PROB30 TEMPO 0619/0622 TS BKN017 FEW020CB`"

    - `SLLP`: Aeródromo El Alto (La Paz, Bolívia).
    - `052200Z`: Emitido no dia 5 às 22:00 UTC.
    - `0600/0624`: Válido do dia 6 às 00:00 UTC até o dia 6 às 24:00 UTC.
    - `08006KT 9999 SCT015 FEW017CB`: Condição inicial de vento de 080° a 6 nós, visibilidade superior a 10 km, nuvens esparsas a 1500 pés e nuvens esparsas a 1700 pés com cumulonimbus.
    - `TX16/0619Z`: Temperatura máxima de 16°C às 19:00 UTC do dia 6.
    - `TN04/0610Z`: Temperatura mínima de 4°C às 10:00 UTC do dia 6.
    - `BECMG 0603/0607 3000 BCFG FEW002 BKN010`: Mudança gradual para visibilidade de 3000 metros com nevoeiro baixo, nuvens esparsas a 200 pés e céu nublado a 1000 pés entre 03:00 e 07:00 UTC do dia 6.
    - `BECMG 0612/0615 14010KT 9999 NSW SCT015`: Mudança gradual para vento de 140° a 10 nós, visibilidade superior a 10 km sem fenômenos significativos e nuvens esparsas a 1500 pés entre 12:00 e 15:00 UTC do dia 6.
    - `PROB30 TEMPO 0619/0622 TS BKN017 FEW020CB`: Probabilidade de 30% de tempestade, céu nublado a 1700 pés e nuvens esparsas a 2000 pés com cumulonimbus entre 19:00 e 22:00 UTC do dia 6.

??? info "`TAF SBRJ 052147Z 0600/0612 29005KT 8000 SCT020 TN25/0609Z TX27/0612Z TEMPO 0600/0603 5000 RA SCT014 BECMG 0609/0611 6000 DZ SCT014 RMK PGA`"

    - `SBRJ`: Aeródromo Santos-Dumont (Rio de Janeiro).
    - `052147Z`: Emitido no dia 5 às 21:47 UTC.
    - `0600/0612`: Válido do dia 6 às 00:00 UTC até o dia 6 às 12:00 UTC.
    - `29005KT 8000 SCT020`: Condição inicial de vento de 290° a 5 nós, visibilidade de 8000 metros e nuvens esparsas a 2000 pés.
    - `TN25/0609Z`: Temperatura mínima de 25°C às 09:00 UTC do dia 6.
    - `TX27/0612Z`: Temperatura máxima de 27°C às 12:00 UTC do dia 6.
    - `TEMPO 0600/0603 5000 RA SCT014`: Condição temporária de visibilidade de 5000 metros, chuva moderada e nuvens esparsas a 1400 pés entre 00:00 e 03:00 UTC do dia 6.
    - `BECMG 0609/0611 6000 DZ SCT014`: Mudança gradual para visibilidade de 6000 metros, chuvisco e nuvens esparsas a 1400 pés entre 09:00 e 11:00 UTC do dia 6.
    - `RMK PGA`: Observação adicional.



<!-- ## Grupos (como pensar)

| Grupo | Ideia operacional | Risco típico |
| :--- | :---------------- | :----------- |
| `BECMG` | muda gradualmente para nova condição | janela de transição |
| `TEMPO` | flutuação temporária | "piora intermitente" |
| `PROB30/40` | probabilidade | planejamento conservador |
| `FM` | mudança "a partir de" | quebra de cenário |

---

## Biblioteca de exemplos reais (REDEMET)

### TAF SBSP (Congonhas) — com TS/CB em janela TEMPO

```text
TAF SBSP 290900Z 2912/2924 05002KT CAVOK TX34/2918Z TN23/2924Z
BECMG 2912/2914 36005KT
BECMG 2915/2917 25004KT
TEMPO 2919/2921 TS SCT035 FEW050CB
BECMG 2921/2923 17004KT CAVOK
RMK PHG=
```

**Leitura operacional:**

Base CAVOK, mas existe uma janela TEMPO com TS e CB (2919–2921Z).

Planeje chegada/saída evitando a janela, ou com alternado/margens.

### TAF SBGR (Guarulhos) — PROB/TEMPO TSRA

```text
TAF SBGR 290900Z 2912/3018 35005KT CAVOK TN21/3008Z TX36/3018Z
BECMG 2915/2917 32005KT FEW035
PROB40 TEMPO 2917/2920 TSRA SCT025 FEW045CB
BECMG 2920/2922 10005KT
BECMG 3006/3008 08002KT
BECMG 3008/3010 08002KT SCT015
...
RMK PHG=
```

**Leitura operacional:**

O risco aqui está concentrado na janela PROB40 TEMPO TSRA (2917–2920Z).

Em operação conservadora, trate PROB40 como risco "real" para planejamento.

### TAF SBBP (com mudanças graduais)

```text
TAF SBBP 180800Z 1812/1824 14010KT 9999 SCT030 TN18/1812Z TX24/1818Z
BECMG 1812/1814 13008KT FEW025
RMK PGE=
```

### TAF SBSC (simples / melhora para CAVOK)

```text
TAF SBSC 092100Z 1000/1012 VRB03KT 9999 SCT020 TN24/1007Z TX30/1012Z
BECMG 1009/1011 CAVOK
RMK PFP=
```

---

## Interpretações guiadas — exemplos selecionados

### 1) Janela curta, alto impacto (TS + CB)

Se houver:

```text
TEMPO .... TS ... FEW...CB
```

**Operacionalmente:**

A janela TEMPO pode coincidir com aproximação final.

Considere: atraso tático, alternado com melhor estabilidade, combustível para holding.

### 2) BECMG + vento

Quando o BECMG muda vento significativamente, avalie:

- componente cruzado,
- pista em uso,
- impacto de rajadas e variação.

---

## Erros comuns em TAF

- Ler apenas a condição base e ignorar TEMPO/PROB.
- Não alinhar janela TAF com seu ETA real (UTC).
- Assumir que "CAVOK no TAF" elimina risco: TS pode aparecer como TEMPO/PROB. -->
