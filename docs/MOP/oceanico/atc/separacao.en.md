---
title: Separation, Routes and Deviations
icon: material/arrow-split-vertical
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Without radar, separation is not observed: it is **calculated and protected**.

!!! danger "Read before applying any number"
    No minimum on this page stands on its own. Each one depends on a declared **and confirmed** capability, on the type of route and on the means of communication. Applying a smaller value without the condition being met is reducing separation without grounds.

## Decision table

Ask in order and stop at the first row whose condition is met. **When more than one row applies, the largest minimum prevails.**

| Condition                                                                         | Minimum                     | Source      |
| --------------------------------------------------------------------------------- | --------------------------- | ----------- |
| Both RVSM, between FL 290 and FL 410, at different levels                         | **1,000 ft**                | [^1] [^2]   |
| Either non-RVSM, or RVSM suspended due to severe turbulence                       | **2,000 ft**                | [^3] [^4]   |
| Both RNP 10, parallel or non-intersecting routes                                  | **50 NM** lateral           | [^5]        |
| Either without RNP 10 certification                                               | **100 NM** lateral          | [^6]        |
| Same route and level, Mach number technique, preceding aircraft at equal or higher Mach | **10 minutes**        | [^7] [^8]   |
| Same route and level, Mach number technique, preceding aircraft faster            | **9 to 5 minutes**, see table | [^7]      |
| Same route and level, Mach number technique, **following** aircraft faster        | **10 minutes + compensation** | [^9]      |
| Same route and direction, RNAV distance with readings from a common point         | **80 NM**                   | [^10] [^8]  |
| Same route and level, without Mach number technique                               | **15 minutes**              | [^11]       |
| Crossing routes, same level                                                       | **15 minutes** at the intersection | [^12] |
| Opposite routes, without lateral separation                                       | Vertical from **10 minutes before to 10 minutes after** the estimated passing | [^13] |
| Climbing or descending through the level of another aircraft, same route          | **15 minutes**              | [^14]       |

The **10-minute** minimum replaces the 15 minutes when navigation aids allow positions and speeds to be determined continuously[^11] [^12] [^14].

## Vertical separation

| Band                                 | Minimum                                                    |
| ------------------------------------ | ---------------------------------------------------------- |
| Below FL 290                         | 1,000 ft                                                   |
| Between FL 290 and FL 410, inclusive | 2,000 ft, or **1,000 ft where RVSM applies**               |
| Above FL 410                         | 2,000 ft                                                   |

All of the FIR's airspace between FL 290 and FL 410 is RVSM[^2], so **1,000 ft is the rule in the cruise band, provided both aircraft are RVSM approved**.

**Crossing levels.** An aircraft may be cleared to a level previously occupied once the other aircraft has reported vacating it, **except** in severe turbulence, cruise climb, or a performance difference that could reduce the minimum[^15].

## Lateral separation

The published minimum for the EUR/SAM corridor is **50 NM** between RNAV aircraft certified RNP 10[^5], and **100 NM** for those not certified[^6]. That is the value to use.

For crossing routes, the lateral separation point follows the navigation specification: RNAV 10 (RNP 10) 50 NM, RNP 4 23 NM, RNP 2 15 NM[^16].

!!! warning "Reduced minima require PBCS"
    ICA 100-37 provides for 23 NM conditioned on `RCP 240`, `RSP 180` and an ADS-C event contract[^17]. **Until the AIP publishes these minima for the corridor, apply 50 NM.**

On receiving information of a navigation failure or degradation, apply another type or minimum of separation; minima based on RNAV distance no longer apply[^18].

## Mach number technique

Jet aircraft on the same route maintain specified Mach numbers to ensure longitudinal spacing[^19]. It requires that they have reported the **same common point** and follow the same route or continuously diverging routes[^20].

### Preceding aircraft faster

| Mach difference   | Minimum separation |
| :---------------: | :----------------: |
| 0 or 0.01         | 10 minutes         |
| 0.02              | 9 minutes          |
| 0.03              | 8 minutes          |
| 0.04              | 7 minutes          |
| 0.05              | 6 minutes          |
| 0.06 or more      | 5 minutes          |

!!! example "Example"
    Preceding aircraft at Mach 0.83, following at Mach 0.78. A difference of 0.05 in favour of the preceding aircraft: the minimum drops from 10 to **6 minutes**[^21].

### Following aircraft faster

The spacing at the entry point must be **increased**: add **1 minute for every 0.01 of Mach difference**, within 600 NM between the entry and exit points[^9].

| ATS route | Points            | Distance | Multiplier |
| :-------: | :---------------: | :------: | :--------: |
| UZ51      | `DAKAP` and `MOVGA` | 517 NM | 1x         |
| UN741     | `JOBER` and `NANIK` | 493 NM | 1x         |
| UN866     | `MAGNO` and `DEKON` | 475 NM | 1x         |
| UN873     | `VUNOK` and `TASIL` | 449 NM | 1x         |
| UN857     | `UTRAM` and `ERETU` | 431 NM | 1x         |
| UL206     | `BUGAT` and `KODOS` | 340 NM | 1x         |

!!! example "Example"
    On UZ51 via `DAKAP`, preceding aircraft at Mach 0.82 and following at Mach 0.84. A difference of 0.02, multiplier 1x: add 2 minutes to the 10. **12 minutes** are required at the entry point[^22].

Consulting the pilot about a speed adjustment is permitted, but should not be routine[^23].

## Loss of capability

| Lost                       | Effect                                             | Action                                        |
| -------------------------- | -------------------------------------------------- | --------------------------------------------- |
| RVSM approval              | Vertical returns to 2,000 ft                        | Reassign levels before the minimum is infringed[^3] |
| Navigation accuracy        | Lateral and RNAV distance minima no longer apply    | Apply another type or minimum[^18]            |
| ADS-C                      | No automatic position                               | Require reports and re-establish minima[^24]  |
| Assigned Mach number       | The technique no longer supports the reduced minimum | Return to 10 or 15 minutes                   |

**Emergency separation.** If, during an emergency, horizontal separation cannot be ensured, **half the vertical minimum** may exceptionally be used: 500 ft where 1,000 ft applies, and 1,000 ft where 2,000 ft applies[^25]. Flight crews must be informed that it is being applied and of its value, and must receive essential traffic information[^26].

## Conflicts near the FIR boundary

1. **Calculate separation at the transfer point**, not where the aircraft is now.
2. **Coordinate before acting**[^27].
3. **Resolve it on your side**: adjust level, Mach or time before the handoff.
4. If the adjacent unit is offline, resolve it entirely within your own jurisdiction.

## SLOP

Strategic lateral offset **is in effect in the Atlântico FIR** and is standard pilot practice[^28]:

- offset **to the right only**, in three positions: centerline, 1 NM or 2 NM;
- **never** beyond 2 NM, **never** to the left;
- without automatic offset capability, the aircraft flies the centerline;
- **it does not require ATC clearance and does not need to be reported**;
- reports remain based on the current clearance, not on the offset.

!!! warning "SLOP does not show up as a deviation"
    An aircraft applying SLOP reports the same fix it would report on the centerline. Up to 2 NM is not a navigation error and should not be questioned. What deserves attention is a lateral deviation of **5 NM**, which triggers the ADS-C event contract[^29].

## Deviations { #desvios }

### Aircraft unable to comply with the clearance

If it cannot follow the clearance, or maintain the required navigation accuracy, ATC must be informed **immediately**[^30]. On receiving the report:

1. **Identify** what it cannot comply with.
2. **Confirm** the concrete intention: which level, which heading, for how long.
3. **Protect separation** before the previous minimum is infringed.
4. **Coordinate** with the affected adjacent unit and **record** it.

### Weather deviation

1. Receive the request with the intended side and distance.
2. Assess traffic in the lateral band and at adjacent levels.
3. **Clear it with an explicit limit**: how many miles, for how long, with an instruction to report back on route.
4. **Reassess longitudinal separation**, because the deviation changes the estimates.
5. Request the revised estimate and coordinate with the adjacent unit.

Severe turbulence affecting level keeping triggers `UNABLE RVSM DUE TURBULENCE`[^31] and leads to considering suspension of RVSM in the area[^4].

### Conflict between a deviation and traffic

In this order: **level** first, which is the fastest and most verifiable solution; then a **Mach adjustment**; then **limiting the lateral extent** cleared; and traffic information to both aircraft when nothing resolves it completely.

Require an explicit report of the **return to the centerline** with a revised estimate. Until then, keep the established protection.

[^1]: **ICA 100-37, Art. 323**.
[^2]: **AIP-Brasil, ENR 2.2, item 1.1**.
[^3]: **AIP-Brasil, ENR 2.2, items 1.3 and 1.6**.
[^4]: **AIP-Brasil, ENR 3.5, item 7.8.1**, and **ENR 2.2, item 1.12**.
[^5]: **AIP-Brasil, ENR 3.5, item 6.4.1.1**.
[^6]: **AIP-Brasil, ENR 3.5, item 6.2.2**.
[^7]: **ICA 100-37, Art. 378**, and **CIRCEA 100-66, Art. 6° and Table 1**.
[^8]: **AIP-Brasil, ENR 3.5, item 6.4.2.1**.
[^9]: **CIRCEA 100-66, Arts. 7° and 8°**.
[^10]: **ICA 100-37, Arts. 386 and 387**.
[^11]: **ICA 100-37, Art. 362**.
[^12]: **ICA 100-37, Art. 363**.
[^13]: **ICA 100-37, Art. 366**.
[^14]: **ICA 100-37, Arts. 364 and 365**.
[^15]: **ICA 100-37, Arts. 330 and 331**.
[^16]: **ICA 100-37, Art. 353, Table 4**.
[^17]: **ICA 100-37, Art. 350, Table 3**.
[^18]: **ICA 100-37, Arts. 337 and 382**.
[^19]: **CIRCEA 100-66, Art. 4°, item VI**.
[^20]: **ICA 100-37, Art. 377**.
[^21]: **CIRCEA 100-66, Chart 1** (*Quadro 1*).
[^22]: **CIRCEA 100-66, Chart 3** (*Quadro 3*).
[^23]: **CIRCEA 100-66, Art. 10**.
[^24]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.2**.
[^25]: **ICA 100-37, Art. 270**.
[^26]: **ICA 100-37, Art. 271**.
[^27]: **ICA 100-37, Art. 822**.
[^28]: **AIP-Brasil, ENR 3.5, items 7.9.1 to 7.9.3.8**.
[^29]: **AIP-Brasil, ENR 3.5, item 9.5.2.3**.
[^30]: **AIP-Brasil, ENR 3.5, item 8.8.1**.
[^31]: **AIP-Brasil, ENR 2.2, item 1.13**.
