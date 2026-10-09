---
title: SIGMET
icon: material/alert-circle
---

--8<-- "includes/abreviacoes.md"

# SIGMET

## Definition

SIGMET is a message concerning the occurrence or expected occurrence of certain en-route weather phenomena (icing, cyclone, thunderstorm and turbulence) and other atmospheric phenomena (volcanic ash, radioactive cloud and volcano) that may affect the safety of flight operations, and the development of these phenomena in time and space.

## SIGMET Types

By definition, there are three types of SIGMET:

- **Volcanic Ash SIGMET** (VA SIGMET or WV SIGMET): message concerning the occurrence or expected occurrence of volcanic ash;
- **Tropical Cyclone SIGMET** (TC SIGMET): message concerning the occurrence or expected occurrence of tropical cyclones;
- **SIGMET for any other weather phenomenon** (WS SIGMET) that may affect the safety of flight operations, except phenomena related to volcanic ash and tropical cyclones, namely: thunderstorm (TS), turbulence (TURB), icing (ICE), mountain waves (MTW), duststorm (DS), sandstorm (SS) or radioactive cloud (RDOACT CLD)

## Structure of a SIGMET

```
WSBZ21 SBBS 051430
SBBS SIGMET 17 VALID 151930/152330 SBBS - SBBS BRASILIA FIR EMBD TS FCST WI S1724 W05407 - S1737 W05355 - S2044 W05102 - S1648 W04733 - S1557 W04333 - S1538 W04406 - S1320 W04534 - S1200 W04654 - S1020 W04719 - S1017 W04741 - S0944 W04758 - S0937 W04822 - S0950 W04852 - S1013 W04902 - S1031 W05105 - S1211 W05303 - S1258 W05330 - S1434 W05338 - S1643 W05306 - S1724 W05407 TOP FL480 STNR NC=
```

### Header

> WSBZ21 SBBS 051430<br/>
> *General SIGMET issued by Brazil, with bulletin number 21. Disseminated by Brasília FIR, on the 5th at 1430z.*

The SIGMET header does not usually appear in SIGMET messages, but when present it contains the following information:

- **Message Type:** 2-letter code indicating the message type. For a general SIGMET, the code is "WS". For a volcanic ash SIGMET, the code is "VA" or "WV". For a tropical cyclone SIGMET, the code is "TC".
- **Issuing Station Indicator:** 2-letter code identifying the country or territory issuing the SIGMET. The list of country and territory codes can be found in the [Glossary](../glossario/#country-and-territory-codes-in-sigmet-format).
- **Bulletin Identification Number:** internal bulletin number. Not relevant for simulation.
- **Disseminating FIR:** code of the FIR disseminating the SIGMET.
- **Date and Time of Issue:** date and time at which the SIGMET was issued, in the format DDHHMMz, where DD is the day of the month, HH is the hour in 24-hour format and MM is the minutes.

### Message Body

> SBBS SIGMET 17 VALID 151930/152330 SBBS - SBBS BRASILIA FIR EMBD TS FCST WI S1724 W05407 - S1737 W05355 - S2044 W05102 - S1648 W04733 - S1557 W04333 - S1538 W04406 - S1320 W04534 - S1200 W04654 - S1020 W04719 - S1017 W04741 - S0944 W04758 - S0937 W04822 - S0950 W04852 - S1013 W04902 - S1031 W05105 - S1211 W05303 - S1258 W05330 - S1434 W05338 - S1643 W05306 - S1724 W05407 TOP FL480 STNR NC=<br/>
> *SIGMET number 17, valid from the 15th at 1930z to the 15th at 2330z, for Brasília FIR, concerning embedded thunderstorms (EMBD TS) forecast (FCST) within (WI) the area bounded by the coordinates given, with top (TOP) at FL480, stationary (STNR) and no significant change expected (NC=).*

#### Location indicator of the reference FIR or CTA

> SBBS<br/>
> *Brasília FIR*

The first item of the SIGMET is the code of the FIR to which the SIGMET information refers, that is, the FIR that will be affected by the weather phenomenon. In the example, the FIR code is `SBBS`, which corresponds to Brasília FIR.

#### Message identification and sequence number

> SIGMET 17<br/>
> *SIGMET number: 17*

The SIGMET number is a sequence number that is incremented with each new SIGMET issued for the same FIR. In the example, the SIGMET number is `17`, indicating that this is the 17th SIGMET issued for Brasília FIR.

#### Validity period

> VALID 151930/152330<br/>
> *Valid from the 15th at 1930z to the 15th at 2330z.*

The SIGMET validity period is indicated by a time interval in the format DDHHMM/DDHHMM, where the first DDHHMM indicates the start of validity and the second DDHHMM indicates the end of validity. In the example, the validity period is from the 15th at 1930z to the 15th at 2330z.

#### Originating Meteorological Centre indicator

> SBBS -<br/>
> *Meteorological centre: Brasília FIR*

The originating Meteorological Centre is the FIR that made the observation or forecast of the weather phenomenon. In the example, the originating Meteorological Centre is that of Brasília FIR, indicated by the code `SBBS`.

#### Location indicator and name for which the information is issued

> SBBS BRASILIA FIR<br/>
> *Reference FIR: Brasília FIR*

The location indicator and name for which the information is issued is the reference FIR or CTA for which the SIGMET is issued. In the example, the SIGMET is issued for Brasília FIR, indicated by the code `SBBS` and the name "BRASILIA FIR".

#### Description of the weather phenomenon

> EMBD TS<br/>
> *Weather phenomenon: embedded thunderstorm*

Description of the weather phenomenon, using the abbreviations presented in the [Glossary](../glossario/#fenomenos-sigmet).

#### Type of Information

> FCST<br/>
> *Type of information: forecast*

Type of information provided. There are two options for this item:

- **OBS:** information based on observation;
- **FCST:** information based on forecast.

#### Location

> WI S1724 W05407 - S1737 W05355 - S2044 W05102 - S1648 W04733 - S1557 W04333 - S1538 W04406 - S1320 W04534 - S1200 W04654 - S1020 W04719 - S1017 W04741 - S0944 W04758 - S0937 W04822 - S0950 W04852 - S1013 W04902 - S1031 W05105 - S1211 W05303 - S1258 W05330 - S1434 W05338 - S1643 W05306 - S1724 W05407<br/>
> *Coordinates bounding the area affected by the weather phenomenon.*

Location of the weather phenomenon, expressed as a series of latitudes and longitudes in degrees and minutes.

The area affected by the weather phenomenon can be presented in several ways:

1. **Point:** the area is represented by a point, indicated by a single coordinate;

> `N2020 W07005`<br/>
> `N48 E010`<br/>
> `S60 W160`<br/>
> `S0530 E16530`<br/>

2. **Reference Position:** the area is represented by a reference relative to a point or a line, expressed in terms of cardinal position (N, S, E, W);

| Relative to a point | Relative to several points   | Relative to a line                                                  |
|---------------------|------------------------------|---------------------------------------------------------------------|
| `N OF N50`          | `N OF N1515 AND W OF E17530` | `N OF LINE S2520 W11510 – S2520 W12010`                             |
| `S OF N5430`        | `S OF N45 AND N OF N40`      | `SW OF LINE N50 W005 – N60 W020`                                    |
| `N OF S10`          | `N OF S45 AND E OF W155`     | `SW OF LINE N50 W020 – N45 E010 AND NE OF LINE N45 W020 – N40 E010` |
| `S OF S4530`        | 
| `W OF W155`         |
| `E OF W45`          |
| `W OF E15540`       |
| `E OF E09015`       |

3. **Polygon:** the area is bounded by a series of coordinates forming a polygon;

> `WI N6030 E02550 – N6055 E02500 – N6050 E02630 – N6030 E02550`

4. **Line Width:** the area is represented by a line and a width;

> `APRX 50KM WID LINE BTN N64 W017 – N60 W010 – N57 E010`

5. **FIR/UIR/CTA:** the area is the entire referenced FIR, UIR or CTA;

> `ENTIRE FIR`<br/>
> `ENTIRE UIR`<br/>
> `ENTIRE FIR/UIR`<br/>
> `ENTIRE CTA`<br/>

6. **Circular Area:** the area is represented by a circle, indicated by a centre point and a radius.

> `WI 400KM OF TC CENTRE`<br/>
> `WI 250NM OF TC CENTRE`<br/>
> `WI 30KM OF N6030 E02550`<br/>

#### Level or Altitude

Indication of the altitude of the weather phenomenon, expressed as an altitude or flight level. It can be given in several ways:

1. **Altitude or Flight Level:** indicates the altitude of the phenomenon or the band in which it occurs (base-top), given in feet or metres, or a flight level indicated by "FL" followed by three digits in hundreds of feet;
2. **Top:** indicates the altitude of the top of the weather phenomenon, indicated by "TOP" followed by a flight level or altitude;

| Altitude or Flight Level | Altitude or Flight Level Band     | Top               |
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

#### Movement of the Phenomenon

Indication of the movement or expected movement of the weather phenomenon (direction and speed) in relation to the cardinal, intercardinal or secondary intercardinal points, or stationary.

> `MOV SE`<br/>
> `MOV NNW`<br/>
> `MOV E 40KMH`<br/>
> `MOV E 20KT`<br/>
> `MOV WSW 20KT`<br/>
> `STNR`

#### Changes in Intensity

Indication of changes in the intensity of the weather phenomenon, using the following abbreviations:

* `INTSF`: intensifying;
* `WKN`: weakening;
* `NC`: no significant change expected.

#### Forecast Time

Indication of the forecast time of occurrence of the phenomenon.

> `FCST AT 2200Z`

#### Forecast Position of the Tropical Cyclone

Forecast position of the centre of the tropical cyclone, indicated by coordinates.

> `TC CENTRE PSN N1030 E16015`<br/>
> `TC CENTRE PSN N1015 E15030 CB`<br/>

## Practical SIGMET Examples

??? info "`SBBS SIGMET 24 VALID 052330/060330 SBBS - SBBS BRASILIA FIR EMBD TS FCST WI S1833 W04539 - S1631 W04230 - S1538 W04406 - S1502 W04426 - S1430 W04448 - S1322 W04533 - S1544 W04844 - S1833 W04539 TOP FL470 STNR NC=`"

    - `SBBS`: Reference FIR, Brasília FIR
    - `SIGMET 24`: SIGMET number
    - `VALID 052330/060330`: valid from the 5th at 2330z to the 6th at 0330z
    - `SBBS -`: Originating Meteorological Centre, Brasília FIR
    - `SBBS BRASILIA FIR`: Location for which the information is issued, Brasília FIR
    - `EMBD TS`: weather phenomenon, embedded thunderstorm
    - `FCST`: type of information, forecast
    - `WI S1833 W04539 - S1631 W04230 - (...)`: location of the weather phenomenon, area bounded by a polygon formed by the coordinates given
    - `TOP FL470`: top of the weather phenomenon, FL470
    - `STNR`: stationary phenomenon
    - `NC=`: no significant change expected

??? info "`SBAO SIGMET 31 VALID 052330/060330 SBAO - SBAO ATLANTICO FIR SEV ICE FCST WI S1948 W03822 - S2221 W03535 - S2736 W03716 - S3324 W03607 - S3422 W03516 - S3416 W03353 - S3204 W03219 - S2853 W03250 - S2524 W03125 - S2408 W03054 - S2151 W02959 - S1623 W03509 - S1548 W03640 - S1618 W03702 - S1841 W03815 - S1852 W03740 - S1947 W03821 - S1948 W03822 FL120/220 STNR NC=`"

    - `SBAO`: Reference FIR, Atlântico FIR
    - `SIGMET 31`: SIGMET number
    - `VALID 052330/060330`: valid from the 5th at 2330z to the 6th at 0330z
    - `SBAO -`: Originating Meteorological Centre, Atlântico FIR
    - `SBAO ATLANTICO FIR`: Location for which the information is issued, Atlântico FIR
    - `SEV ICE`: weather phenomenon, severe icing
    - `FCST`: type of information, forecast
    - `WI S1948 W03822 - S2221 W03535 - (...)`: location of the weather phenomenon, area bounded by a polygon formed by the coordinates given
    - `FL120/220`: altitude band of the weather phenomenon, between FL120 and FL220
    - `STNR`: stationary phenomenon
    - `NC=`: no significant change expected
