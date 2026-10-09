---
title: Horizontal Separation
icon: material/arrow-left-right
---

--8<-- "includes/abreviacoes.md"

# Horizontal Separation

## Lateral and longitudinal

Horizontal separation keeps aircraft apart in the horizontal plane, and has two forms[^1]:

- **Lateral**: the aircraft are on **different routes**, or over **different geographical locations**.
- **Longitudinal**: the aircraft are on the same, opposite or crossing routes, with a **time or distance interval** between them.

This page first covers **procedural** separation, based on position reports, estimates and distances reported by the pilot. Separation **with ATS surveillance**, measured on the screen, is at the end of the page, and it is the one you will use most of the time on the network.

!!! info "When procedural separation appears on the network"
    Procedural separation is hardly used at the continental positions of Vatsim Brasil, because they have surveillance. It appears in oceanic control, when a target disappears from the screen, and in the departure minima, which the tower and the APP use even with radar. Read this part to understand the logic, and use it when surveillance is not available.

## Lateral separation

### By geographical locations

The simplest method: one aircraft reports being over one point and the other over another point, and the two locations are clearly different. The position may be determined visually or by reference to a navigation aid[^2].

### By diverging routes

Two aircraft on routes diverging from the same aid or point are laterally separated when[^3]:

| Navigation | Condition |
| --- | --- |
| **VOR** | Radials diverging by at least **15°**, and at least one aircraft **15 NM** or more from the VOR |
| **NDB** | Tracks to or from the NDB diverging by at least **30°**, and at least one aircraft **15 NM** or more from the NDB |
| **GNSS**, or **VOR** and **GNSS** | Tracks diverging by **15° to 135°**, and at least one aircraft **15 NM** from the common point, from FL 010 to FL 190, or **23 NM**, from FL 200 to FL 600 |

On **opposite** or **crossing** routes this is not enough. Establish vertical separation **before** the aircraft are within 15 NM of the aid or of the crossing point[^4].

Before using GNSS-based separation, confirm that the aircraft is navigating by GNSS and is not flying a lateral offset (SLOP)[^5]. Do not use GNSS separation if the pilot reports a loss of RAIM[^6].

### On published procedures

Aircraft departing or arriving on published procedures (SID, STAR, IAC) are laterally separated when the distance between the tracks is at least[^7]:

| Combination | Distance |
| --- | --- |
| RNAV 1 with RNAV 1, RNP 1, RNP APCH or RNP AR APCH | **7 NM** |
| RNP 1, RNP APCH or RNP AR APCH with each other | **5 NM** |

They are also separated when the protection areas of the tracks do not overlap.

### In turns

If an aircraft's route includes a turn that will cause lateral separation to be lost, establish **another** separation before the aircraft starts the turn[^8]. Remember that a **fly-by** turn may begin up to 20 NM before the waypoint and cut inside it. In a **flyover** turn, the aircraft overflies the waypoint and only then turns, ending up outside the turn[^8].

## Longitudinal separation

### What "same route" means

For longitudinal separation, the angular difference between the routes defines the case[^9]:

| Case | Angular difference |
| --- | --- |
| **Same route** | Less than 45°, or more than 315° |
| **Opposite routes** | More than 135° and less than 225° |
| **Crossing routes** | All other cases: 45° to 135°, and 225° to 315° |

### Watch the faster aircraft behind

The longitudinal minimum applies all the time, not only when you check it. If the following aircraft is **faster** than the preceding one, the distance between them decreases. When separation is about to reach the minimum, adjust speed to maintain it[^10].

### Time-based

Time-based separation uses position reports and estimates, and is what you use without surveillance and without DME.

| Situation | Minimum | Source |
| --- | --- | --- |
| Same level, same route | **15 min** | [^11] |
| Same level, same route, with aids that allow position and speed to be determined continuously | **10 min** | [^11] |
| Same level, same route, preceding aircraft **20 kt** or more faster (TAS) | **5 min** | [^11] |
| Same level, same route, preceding aircraft **40 kt** or more faster (TAS) | **3 min** | [^11] |
| Same level, crossing routes, at the crossing point | **15 min**, or **10 min** with aids | [^12] |
| Opposite routes, without lateral separation | Vertical from **10 min before** to **10 min after** the estimated crossing | [^13] |

The 5 and 3 minute minima only apply between aircraft that departed from the same aerodrome, between en-route aircraft that reported over the same point, or between a departure and an en-route aircraft that has already reported a point that ensures separation where the departure will join the route[^11].

On opposite routes, if it can be **positively** determined that the aircraft have passed each other, the 10 minutes after the crossing are no longer required[^13].

### Climbing or descending

When one aircraft climbs or descends **through** another aircraft's level without vertical separation:

| Situation | Minimum | Source |
| --- | --- | --- |
| Same route | **15 min** | [^14] |
| Same route, with aids that allow frequent determination of position and speed | **10 min** | [^14] |
| Same route, with the level change started within 10 min of the second aircraft reporting over a reporting point | **5 min** | [^14] |
| Crossing routes | **15 min**, or **10 min** with aids | [^15] |

### DME or GNSS distance

With DME or GNSS, distances reported by the pilots replace time. Both aircraft must be using the **same DME station**, a DME and a waypoint at the same location, or the **same waypoint**, and flying directly to or from it[^16]. Keep direct VHF voice communication with both while applying this separation[^17]. If both have area navigation, ask specifically for the **GNSS distance**[^18].

| Situation | Minimum | Source |
| --- | --- | --- |
| Same level, same route | **20 NM** | [^19] |
| Same level, same route, preceding aircraft **20 kt** or more faster (TAS) | **10 NM** | [^20] |
| Same level, routes crossing at less than 90°, with distances from the same point at the crossing | **20 NM**, or **10 NM** with 20 kt | [^21] |
| Climbing or descending, same route, **one of them maintaining level** | **10 NM** | [^22] |
| Opposite routes, after the crossing is **confirmed** | **10 NM** to climb or descend through the other's level | [^23] |

The distance must be checked with **simultaneous** readings from both aircraft, at frequent intervals[^19].

## Departures

The ICA 100-37 departure minima complement the previous ones and apply between aircraft that have just taken off[^24]:

| Situation | Minimum | Source |
| --- | --- | --- |
| Routes diverging by at least **45°** immediately after take-off, so that lateral separation exists | **1 min** | [^25] |
| Same route, with the preceding aircraft **40 kt** or more faster | **2 min** | [^26] |
| Same route, the following aircraft climbing through the preceding aircraft's level without vertical separation | **5 min** | [^27] |

For the 2 minute minimum, the speed difference during the climb may be better estimated from IAS than from TAS[^26].

Separation between a departure and an arrival at the same aerodrome is in [Aerodrome Separation](05-aerodromo.en.md#departures-and-arrivals).

## With ATS surveillance

With ATS surveillance, horizontal separation no longer depends on reports and is measured on the screen.

| Situation | Minimum | Source |
| --- | --- | --- |
| Separation with PSR, SSR, ADS-B or MLAT | **5 NM** | [^28] |
| In the TMA or CTR, if only en-route radar is available | **10 NM** | [^28] |
| Wake turbulence, if larger than the radar minimum | See [Wake Turbulence](04-esteira.en.md#with-ats-surveillance) | [^29] |

The rules of application are:

- The distance is measured between the **centres of the targets**. The edges must never touch or overlap without vertical separation[^30].
- The minima only apply between **identified** aircraft, when identification is likely to be maintained[^31].
- A departure may be separated by the surveillance minima from take-off, if it is likely to be identified within **1 NM** of the end of the runway[^32].
- The surveillance minima **do not** apply between aircraft in the **same hold**. Separate them vertically[^33].
- If a controlled flight not yet identified enters your airspace, keep the identified aircraft separated from **all** targets on the screen until you identify it or establish procedural separation[^34].
- If control will pass to a sector or unit that only provides **procedural** separation, establish that separation **before** the aircraft reaches the limit of your airspace or leaves surveillance coverage[^35].

How to measure and keep the 5 NM with vectors and speed is in the [Vectoring and Sequencing Manual](../vetoracao-sequenciamento/01-fundamentos.en.md#separation-with-ats-surveillance).

!!! tip "In EuroScope"
    `F1 + D` (`.distance`) shows the updated distance between an aircraft and another aircraft or point. `F1 + S` (`.sep`) predicts the point of closest approach between two aircraft. Use the latter **before** clearing a climb or descent through another aircraft's level. See [Commands](../../../fundamentos/softwares/euroscope/comandos.en.md).

[^1]: **ICA 100-37, Art. 334**, and **Art. 39, § 2°, item II**. See [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 341**.
[^3]: **ICA 100-37, Art. 342, § 1°, and Table 2**.
[^4]: **ICA 100-37, Art. 343**.
[^5]: **ICA 100-37, Art. 344**.
[^6]: **ICA 100-37, Art. 346**.
[^7]: **ICA 100-37, Art. 349**.
[^8]: **ICA 100-37, Art. 338 and §§ 1° and 2°**.
[^9]: **ICA 100-37, Art. 360**.
[^10]: **ICA 100-37, Art. 357 and sole paragraph**.
[^11]: **ICA 100-37, Art. 362**.
[^12]: **ICA 100-37, Art. 363**.
[^13]: **ICA 100-37, Art. 366**.
[^14]: **ICA 100-37, Art. 364, § 1°**.
[^15]: **ICA 100-37, Art. 365**.
[^16]: **ICA 100-37, Arts. 367 and 368, caput and § 1°**.
[^17]: **ICA 100-37, Art. 368, § 2°**.
[^18]: **ICA 100-37, Art. 369**.
[^19]: **ICA 100-37, Art. 370**.
[^20]: **ICA 100-37, Art. 371**.
[^21]: **ICA 100-37, Art. 372**.
[^22]: **ICA 100-37, Art. 373**.
[^23]: **ICA 100-37, Art. 374**.
[^24]: **ICA 100-37, Art. 434**.
[^25]: **ICA 100-37, Art. 435**.
[^26]: **ICA 100-37, Art. 436 and sole paragraph**.
[^27]: **ICA 100-37, Art. 437 and sole paragraph**.
[^28]: **ICA 100-37, Art. 953 and §§ 1° and 2°**.
[^29]: **ICA 100-37, Art. 956**.
[^30]: **ICA 100-37, Arts. 948 and 949**.
[^31]: **ICA 100-37, Art. 946**.
[^32]: **ICA 100-37, Art. 951**.
[^33]: **ICA 100-37, Art. 952**.
[^34]: **ICA 100-37, Art. 950**.
[^35]: **ICA 100-37, Art. 947**.
