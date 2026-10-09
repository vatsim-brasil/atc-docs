---
title: TAF
icon: material/weather-rainy
---

--8<-- "includes/abreviacoes.md"

# TAF

## Definition

TAF (Terminal Aerodrome Forecast) is an encoded weather forecast for a specific aerodrome, focused on conditions relevant to aviation operations.

## Message structure

A TAF is encoded as follows:

| Type    | Location   | Date/time | Validity    | Initial Forecast            | Maximum and Minimum Temperature | Forecast Changes                                                                                    | Supplementary Information |
| :------ | :--------- | :-------- | :---------- | :-------------------------- | :-------------------------- | :-------------------------------------------------------------------------------------------------- | :------------------------ |
| `TAF`   | `SBGL`     | `012004Z` | `0200/0306` | `14007KT 9999 +SHRA SCT020` | `TN25/0208Z TX33/0217Z`     | `BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB` | `RMK PHI`                 |

<!-- A TAF normally contains:

- **Location**
- **Issue (UTC)**
- **Validity** (window)
- **Base condition**
- **Change groups**: `BECMG`, `TEMPO`, `PROBxx`, `FM` (when applicable)
- **Temperatures**: `TX..` / `TN..` (when provided)
- **RMK**: remarks

!!! warning "Operational"
    For decision-making, focus on the **worst case within the relevant window** (especially `TEMPO` and `PROB`). -->

---

## Description of each group

### Type

> `[TAF] SBGL 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Weather forecast.

The first word is always `TAF`, indicating the message type.

---

### TAF Amendment or Correction

> `TAF [COR] SBGL 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> TAF correction.

If a TAF is amended with new information, the term `AMD` (amendment) is inserted immediately after the message type. If the TAF is corrected because of incorrect information, a correction message will be issued containing the word `COR` immediately after the message type.

---

### Location

> `TAF [SBGL] 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Galeão Aerodrome (SBGL).

The four-letter ICAO code identifies the aerodrome to which the forecast refers. Further details on ICAO codes can be found on the [METAR/SPECI](../metar-speci) page.

---

### Date and Time of Issue

> `TAF SBGL [012004Z] 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Issued on the 1st of the month at 20:04 UTC.

This group indicates the day of the month and the time the forecast was issued in UTC, in 24-hour format, followed by the letter `Z`.

!!! example "Examples"

    - `291200Z`: issued on the 29th of the current month at 1200Z;
    - `040800Z`: issued on the 4th of the current month at 0800Z;
    - `150530Z`: issued on the 15th of the current month at 0530Z;
    - `011500Z`: issued on the 1st of the current month at 1500Z;
    - `312027Z`: issued on the 31st of the current month at 2027Z.

---

### Validity Period

> `TAF SBGL 012004Z [0200/0306] 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Valid from 00:00 UTC on the 2nd to 06:00 UTC on the 3rd (30 hours).

The TAF validity period is indicated by two four-digit groups separated by a slash (`/`). The first group indicates the day of the month and the UTC hour at which validity begins, and the second group indicates the day of the month and the UTC hour at which validity ends.

!!! example "Examples"

    - `2912/3018`: valid from the 29th at 12:00 UTC to the 30th at 18:00 UTC;
    - `0406/0506`: valid from the 4th at 06:00 UTC to the 5th at 06:00 UTC;
    - `1500/1606`: valid from the 15th at 00:00 UTC to the 16th at 06:00 UTC;
    - `0112/0212`: valid from the 1st at 12:00 UTC to the 2nd at 12:00 UTC;
    - `3118/0200`: valid from the 31st at 18:00 UTC to the 2nd at 00:00 UTC.

---

### Initial (Base) Forecast

> `TAF SBGL 012004Z 0200/0306 [14007KT 9999 SCT020] TN25/0208Z TX33/0217Z BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Initial forecast of wind from 140° at 7 knots, visibility greater than 10 km, scattered clouds at 2000 feet.

This group describes the weather conditions expected at the beginning of the TAF validity period. It includes information on wind, visibility, cloud cover and other relevant weather phenomena.

It is interpreted according to the same rules as the METAR/SPECI, as described [here](../metar-speci).

---

### Maximum and Minimum Temperatures

> `TAF SBGL 012004Z 0200/0306 14007KT 9999 SCT020 [TN25/0208Z TX33/0217Z] BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB RMK PHI`<br/>
> Minimum temperature of 25°C at 08:00 UTC on the 2nd and maximum of 33°C at 17:00 UTC on the 2nd.

This group provides the minimum (`TN`) and maximum (`TX`) temperatures expected during the TAF validity period, together with the times at which these temperatures are forecast to occur.

Immediately after the code `TN` or `TX` comes the temperature in degrees Celsius, followed by a slash (`/`) and the day of the month and UTC hour at which the temperature is expected.

??? example "Examples"

    - `TN18/1812Z TX24/1818Z`: minimum temperature of 18°C at 12:00 UTC on the 18th and maximum of 24°C at 18:00 UTC on the 18th;
    - `TN21/3008Z TX36/3018Z`: minimum temperature of 21°C at 08:00 UTC on the 30th and maximum of 36°C at 18:00 UTC on the 30th;
    - `TN23/2924Z TX34/2918Z`: minimum temperature of 23°C at 24:00 UTC on the 29th and maximum of 34°C at 18:00 UTC on the 29th.

---

### Forecast Changes

> `TAF SBGL 012004Z 0200/0306 14007KT 9999 SCT020 TN25/0208Z TX33/0217Z [BECMG 0200/0202 33005KT BECMG 0206/0208 23005KT TEMPO 0220/0302 15010KT 4000 TSRA BKN017 FEW030CB] RMK PHI`<br/>
> Forecast changes...

Given the dynamic nature of the weather, a TAF may include groups indicating expected changes in weather conditions during the validity period. The main groups are:

| Group    | Description                                                                                        |
| :------  | :------------------------------------------------------------------------------------------------  |
| `BECMG`  | Indicates a **permanent** change that will occur **gradually**.                                    |
| `FM`     | Indicates a **permanent** change that will occur **immediately**.                                  |
| `TEMPO`  | Indicates a **temporary** change that will occur for a limited period within the TAF validity.     |
| `PROB30` | Indicates a **temporary or permanent** change with a **30% probability**.                          |
| `PROB40` | Indicates a **temporary or permanent** change with a **40% probability**.                          |

The table below helps to better understand the dynamics of these changes:

| Period      | Forecast                                                                |
| :---------: | :---------------------------------------------------------------------: |
| Day 02, 00Z | **Start of Gradual Change**<br/>`BECMG`                                 |
| Day 02, 01Z | ...                                                                     |
| Day 02, 02Z | **Conditions after the Gradual Change**<br/>`33005KT`                   |
| Day 02, 03Z | ...                                                                     |
| Day 02, 04Z | ...                                                                     |
| Day 02, 05Z | ...                                                                     |
| Day 02, 06Z | **Start of Gradual Change**<br/>`BECMG`                                 |
| Day 02, 07Z | ...                                                                     |
| Day 02, 08Z<br><span style="color:#349beb;font-weight:bold;font-size:0.6rem;">MIN TEMP - 25°C</span> | **Conditions after the Gradual Change**<br/>`23005KT`  |
| Day 02, 09Z | ...                                                                     |
| Day 02, 10Z | ...                                                                     |
| Day 02, 11Z | ...                                                                     |
| Day 02, 12Z | ...                                                                     |
| Day 02, 13Z | ...                                                                     |
| Day 02, 14Z | ...                                                                     |
| Day 02, 15Z | ...                                                                     |
| Day 02, 16Z | ...                                                                     |
| Day 02, 17Z<br><span style="color:red;font-weight:bold;font-size:0.6rem;">MAX TEMP - 33°C</span> | ...                                                  |
| Day 02, 18Z | ...                                                                     |
| Day 02, 19Z | ...                                                                     |
| Day 02, 20Z | **Start of Temporary Condition**<br/>`TEMPO 0220/0302 15010KT 4000`     |
| Day 02, 21Z | ...                                                                     |
| Day 02, 22Z | ...                                                                     |
| Day 02, 23Z | ...                                                                     |
| Day 03, 00Z | ...                                                                     |
| Day 03, 01Z | ...                                                                     |
| Day 03, 02Z | **End of Temporary Condition**<br/>Return to the last steady condition  |
| Day 03, 03Z | ...                                                                     |
| Day 03, 04Z | ...                                                                     |
| Day 03, 05Z | ...                                                                     |

---

## Practical TAF Examples

??? info "`SBGR 022200Z 0300/0406 00000KT 9999 FEW020 TN19/0308Z TX25/0316Z PROB30 0300/0303 02005KT 7000 RA BKN020 BECMG 0305/0307 SCT010 TEMPO 0308/0311 33008KT 6000 RA BKN009 BECMG 0312/0314 30008KT SCT030 BECMG 0315/0317 BKN030 FEW045TCU TEMPO 0317/0322 6000 TSRA SCT010 BKN020 FEW045CB BECMG 0322/0324 02005KT 8000 RA BKN020 BECMG 0402/0404 NSW BKN008 RMK PGN`"

    - `SBGR`: Guarulhos Aerodrome.
    - `022200Z`: Issued on the 2nd at 22:00 UTC.
    - `0300/0406`: Valid from the 3rd at 00:00 UTC to the 4th at 06:00 UTC.
    - `00000KT 9999 FEW020`: Initial condition of calm wind, visibility greater than 10 km, few clouds at 2000 feet.
    - `TN19/0308Z`: Minimum temperature of 19°C at 08:00 UTC on the 3rd.
    - `TX25/0316Z`: Maximum temperature of 25°C at 16:00 UTC on the 3rd.
    - `PROB30 0300/0303 02005KT 7000 RA BKN020`: 30% probability of wind from 020° at 5 knots, visibility of 7000 metres, moderate rain and broken clouds at 2000 feet between 00:00 and 03:00 UTC on the 3rd.
    - `BECMG 0305/0307 SCT010`: Gradual change to scattered clouds at 1000 feet between 05:00 and 07:00 UTC on the 3rd.
    - `TEMPO 0308/0311 33008KT 6000 RA BKN009`: Temporary condition of wind from 330° at 8 knots, visibility of 6000 metres, moderate rain and broken clouds at 900 feet between 08:00 and 11:00 UTC on the 3rd.
    - `BECMG 0312/0314 30008KT SCT030`: Gradual change to wind from 300° at 8 knots and scattered clouds at 3000 feet between 12:00 and 14:00 UTC on the 3rd.
    - `BECMG 0315/0317 BKN030 FEW045TCU`: Gradual change to broken clouds at 3000 feet and few clouds at 4500 feet with towering cumulus between 15:00 and 17:00 UTC on the 3rd.
    - `TEMPO 0317/0322 6000 TSRA SCT010 BKN020 FEW045CB`: Temporary condition of visibility of 6000 metres, thunderstorm with moderate rain, scattered clouds at 1000 feet, broken clouds at 2000 feet and few clouds at 4500 feet with cumulonimbus between 17:00 and 22:00 UTC on the 3rd.
    - `BECMG 0322/0324 02005KT 8000 RA BKN020`: Gradual change to wind from 020° at 5 knots, visibility of 8000 metres, moderate rain and broken clouds at 2000 feet between 22:00 and 24:00 UTC on the 3rd.
    - `BECMG 0402/0404 NSW BKN008`: Gradual change to no significant weather and broken clouds at 800 feet between 02:00 and 04:00 UTC on the 4th.
    - `RMK PGN`: Additional remark.

??? info "`TAF LEMD 051700Z 0518/0624 23015KT 9999 SCT020 TX10/0615Z TN06/0607Z TEMPO 0518/0521 4000 RA SHRA FEW030TCU TEMPO 0518/0605 23018G30KT PROB30 TEMPO 0522/0608 BKN010 PROB40 TEMPO 0609/0613 VRB05KT TEMPO 0610/0618 RA SHRA BKN014 FEW030TCU PROB40 TEMPO 0614/0619 23015G27KT`"

    - `LEMD`: Madrid-Barajas Aerodrome.
    - `051700Z`: Issued on the 5th at 17:00 UTC.
    - `0518/0624`: Valid from the 5th at 18:00 UTC to the 6th at 24:00 UTC.
    - `23015KT 9999 SCT020`: Initial condition of wind from 230° at 15 knots, visibility greater than 10 km and scattered clouds at 2000 feet.
    - `TX10/0615Z`: Maximum temperature of 10°C at 15:00 UTC on the 6th.
    - `TN06/0607Z`: Minimum temperature of 6°C at 07:00 UTC on the 6th.
    - `TEMPO 0518/0521 4000 RA SHRA FEW030TCU`: Temporary condition of visibility of 4000 metres, moderate rain showers, and few clouds at 3000 feet with towering cumulus between 18:00 and 21:00 UTC on the 5th.
    - `TEMPO 0518/0605 23018G30KT`: Temporary condition of wind from 230° at 18 knots with gusts up to 30 knots between 18:00 UTC on the 5th and 05:00 UTC on the 6th.
    - `PROB30 TEMPO 0522/0608 BKN010`: 30% probability of broken clouds at 1000 feet between 22:00 UTC on the 5th and 08:00 UTC on the 6th.
    - `PROB40 TEMPO 0609/0613 VRB05KT`: 40% probability of variable wind at 5 knots between 09:00 and 13:00 UTC on the 6th.
    - `TEMPO 0610/0618 RA SHRA BKN014 FEW030TCU`: Temporary condition of moderate rain, moderate rain showers, broken clouds at 1400 feet and few clouds at 3000 feet with towering cumulus between 10:00 and 18:00 UTC on the 6th.
    - `PROB40 TEMPO 0614/0619 23015G27KT`: 40% probability of wind from 230° at 15 knots with gusts up to 27 knots between 14:00 and 19:00 UTC on the 6th.

??? info "`TAF SBCT 052100Z 0600/0624 09005KT 8000 SCT020 TN16/0609Z TX27/0617Z PROB30 0600/0606 BKN001 FM060600 09006KT 9999 BKN012 PROB30 0606/0612 BKN002 FM061200 09005KT 8000 BKN030 PROB30 0612/0618 BKN009 FM061800 09006KT 9999 BKN010 PROB30 0618/0622 BKN009 RMK PDE`"

    - `SBCT`: Curitiba Aerodrome.
    - `052100Z`: Issued on the 5th at 21:00 UTC.
    - `0600/0624`: Valid from the 6th at 00:00 UTC to the 6th at 24:00 UTC.
    - `09005KT 8000 SCT020`: Initial condition of wind from 090° at 5 knots, visibility of 8000 metres and scattered clouds at 2000 feet.
    - `TN16/0609Z`: Minimum temperature of 16°C at 09:00 UTC on the 6th.
    - `TX27/0617Z`: Maximum temperature of 27°C at 17:00 UTC on the 6th.
    - `PROB30 0600/0606 BKN001`: 30% probability of broken clouds at 100 feet between 00:00 and 06:00 UTC on the 6th.
    - `FM060600 09006KT 9999 BKN012`: Immediate change from 06:00 UTC on the 6th to wind from 090° at 6 knots, visibility greater than 10 km and broken clouds at 1200 feet.
    - `PROB30 0606/0612 BKN002`: 30% probability of broken clouds at 200 feet between 06:00 and 12:00 UTC on the 6th.
    - `FM061200 09005KT 8000 BKN030`: Immediate change from 12:00 UTC on the 6th to wind from 090° at 5 knots, visibility of 8000 metres and broken clouds at 3000 feet.
    - `PROB30 0612/0618 BKN009`: 30% probability of broken clouds at 900 feet between 12:00 and 18:00 UTC on the 6th.
    - `FM061800 09006KT 9999 BKN010`: Immediate change from 18:00 UTC on the 6th to wind from 090° at 6 knots, visibility greater than 10 km and broken clouds at 1000 feet.
    - `PROB30 0618/0622 BKN009`: 30% probability of broken clouds at 900 feet between 18:00 and 22:00 UTC on the 6th.
    - `RMK PDE`: Additional remark.

??? info "`TAF SLLP 052200Z 0600/0624 08006KT 9999 SCT015 FEW017CB TX16/0619Z TN04/0610Z BECMG 0603/0607 3000 BCFG FEW002 BKN010 BECMG 0612/0615 14010KT 9999 NSW SCT015 PROB30 TEMPO 0619/0622 TS BKN017 FEW020CB`"

    - `SLLP`: El Alto Aerodrome (La Paz, Bolivia).
    - `052200Z`: Issued on the 5th at 22:00 UTC.
    - `0600/0624`: Valid from the 6th at 00:00 UTC to the 6th at 24:00 UTC.
    - `08006KT 9999 SCT015 FEW017CB`: Initial condition of wind from 080° at 6 knots, visibility greater than 10 km, scattered clouds at 1500 feet and few clouds at 1700 feet with cumulonimbus.
    - `TX16/0619Z`: Maximum temperature of 16°C at 19:00 UTC on the 6th.
    - `TN04/0610Z`: Minimum temperature of 4°C at 10:00 UTC on the 6th.
    - `BECMG 0603/0607 3000 BCFG FEW002 BKN010`: Gradual change to visibility of 3000 metres with fog patches, few clouds at 200 feet and broken clouds at 1000 feet between 03:00 and 07:00 UTC on the 6th.
    - `BECMG 0612/0615 14010KT 9999 NSW SCT015`: Gradual change to wind from 140° at 10 knots, visibility greater than 10 km with no significant weather and scattered clouds at 1500 feet between 12:00 and 15:00 UTC on the 6th.
    - `PROB30 TEMPO 0619/0622 TS BKN017 FEW020CB`: 30% probability of thunderstorm, broken clouds at 1700 feet and few clouds at 2000 feet with cumulonimbus between 19:00 and 22:00 UTC on the 6th.

??? info "`TAF SBRJ 052147Z 0600/0612 29005KT 8000 SCT020 TN25/0609Z TX27/0612Z TEMPO 0600/0603 5000 RA SCT014 BECMG 0609/0611 6000 DZ SCT014 RMK PGA`"

    - `SBRJ`: Santos-Dumont Aerodrome (Rio de Janeiro).
    - `052147Z`: Issued on the 5th at 21:47 UTC.
    - `0600/0612`: Valid from the 6th at 00:00 UTC to the 6th at 12:00 UTC.
    - `29005KT 8000 SCT020`: Initial condition of wind from 290° at 5 knots, visibility of 8000 metres and scattered clouds at 2000 feet.
    - `TN25/0609Z`: Minimum temperature of 25°C at 09:00 UTC on the 6th.
    - `TX27/0612Z`: Maximum temperature of 27°C at 12:00 UTC on the 6th.
    - `TEMPO 0600/0603 5000 RA SCT014`: Temporary condition of visibility of 5000 metres, moderate rain and scattered clouds at 1400 feet between 00:00 and 03:00 UTC on the 6th.
    - `BECMG 0609/0611 6000 DZ SCT014`: Gradual change to visibility of 6000 metres, drizzle and scattered clouds at 1400 feet between 09:00 and 11:00 UTC on the 6th.
    - `RMK PGA`: Additional remark.



<!-- ## Groups (how to think about them)

| Group | Operational idea | Typical risk |
| :--- | :---------------- | :----------- |
| `BECMG` | gradually changes to a new condition | transition window |
| `TEMPO` | temporary fluctuation | "intermittent deterioration" |
| `PROB30/40` | probability | conservative planning |
| `FM` | change "from" | scenario break |

---

## Library of real examples (REDEMET)

### TAF SBSP (Congonhas) — with TS/CB in a TEMPO window

```text
TAF SBSP 290900Z 2912/2924 05002KT CAVOK TX34/2918Z TN23/2924Z
BECMG 2912/2914 36005KT
BECMG 2915/2917 25004KT
TEMPO 2919/2921 TS SCT035 FEW050CB
BECMG 2921/2923 17004KT CAVOK
RMK PHG=
```

**Operational reading:**

CAVOK base, but there is a TEMPO window with TS and CB (2919–2921Z).

Plan the arrival/departure to avoid the window, or with an alternate/margins.

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

**Operational reading:**

The risk here is concentrated in the PROB40 TEMPO TSRA window (2917–2920Z).

In conservative operations, treat PROB40 as a "real" risk for planning.

### TAF SBBP (with gradual changes)

```text
TAF SBBP 180800Z 1812/1824 14010KT 9999 SCT030 TN18/1812Z TX24/1818Z
BECMG 1812/1814 13008KT FEW025
RMK PGE=
```

### TAF SBSC (simple / improving to CAVOK)

```text
TAF SBSC 092100Z 1000/1012 VRB03KT 9999 SCT020 TN24/1007Z TX30/1012Z
BECMG 1009/1011 CAVOK
RMK PFP=
```

---

## Guided interpretations — selected examples

### 1) Short window, high impact (TS + CB)

If there is:

```text
TEMPO .... TS ... FEW...CB
```

**Operationally:**

The TEMPO window may coincide with the final approach.

Consider: tactical delay, an alternate with more stable conditions, fuel for holding.

### 2) BECMG + wind

When a BECMG changes the wind significantly, assess:

- crosswind component,
- runway in use,
- impact of gusts and variation.

---

## Common TAF mistakes

- Reading only the base condition and ignoring TEMPO/PROB.
- Not aligning the TAF window with your actual ETA (UTC).
- Assuming that "CAVOK in the TAF" eliminates risk: TS may appear as TEMPO/PROB. -->
