---
title: Vertical Separation
icon: material/arrow-up-down
---

--8<-- "includes/abreviacoes.md"

![Separation and Wake Turbulence Manual - Vertical Separation](img/manual-separacao-vertical.png)

#

## The simplest form

Vertical separation is the simplest to apply and the one that depends least on equipment. The aircraft only need to fly at different levels with their altimeters set the same way. En route, that means setting 1013.2 hPa and flying the assigned flight level[^1]. Below the transition altitude, everyone uses the QNH and flies altitudes.

That is why it is every controller's first tool. If you are not sure two aircraft are laterally or longitudinally separated, put them at different levels.

## Minima

| Band | Minimum | Source |
| --- | --- | --- |
| Below FL 290 | **1,000 ft** | [^2] |
| FL 290 to FL 410 inclusive, between RVSM-approved aircraft | **1,000 ft** | [^2] [^3] |
| FL 290 to FL 410 inclusive, if **either** aircraft is not RVSM-approved | **2,000 ft** | [^2] [^4] |
| Above FL 410 | **2,000 ft** | [^2] |
| In the TMA, applied by the APP | **1,000 ft** | [^5] |

All levels from FL 290 to FL 410 in the Brazilian FIRs are RVSM airspace[^3]. The norm is therefore 1,000 ft throughout the cruising band. The exception is the **non-RVSM-approved** aircraft, which requires 2,000 ft from any other[^4].

### How to tell whether an aircraft is RVSM

An RVSM-approved aircraft has the letter `W` in item 10 of the flight plan. A pilot without approval must say **"negative RVSM"** on initial contact within RVSM airspace, in every level change request and in every readback of a level clearance[^6]. If in doubt, ask.

> **PT ART, confirm RVSM approved?**
>
> **\*PT ART, negative RVSM.**

The cruising levels of RVSM airspace and the course rule are in the [Airspace and ATS Services Manual](../espaco-aereo-servicos-ats/05-regras.en.md#rvsm-airspace).

!!! note "On the network"
    On VATSIM, almost every jet files `W` in the flight plan, and light aircraft and turboprops rarely climb to FL 290. But older aircraft, military aircraft and poorly filed flight plans do show up. If traffic without `W` requests FL 290 or above, apply 2,000 ft or keep it below FL 290.

## Cruising level

Cruising levels follow the ICA 100-12 table according to magnetic track, unless the ACC authorises another level or the en-route chart provides otherwise[^7]. On one-way airways, all levels may be used[^8].

When deciding between two aircraft that want the same level:

- The aircraft **already at** the level normally has priority over the one requesting it. Between two aircraft at the same level, the **preceding** one has priority[^9].
- For aircraft bound for the same destination, assign cruising levels, as far as possible, in the **order in which they will make their approach**[^10]. The one landing first should be lower, so it descends first.

## Using a level vacated by another aircraft

An aircraft may be cleared to a level previously occupied by another **after the latter has reported vacating it**[^11]. The clearance for the other aircraft to descend is not enough, nor is the target starting to move on the screen: it must have left the level.

There are three exceptions to this rule. In them, you only clear the level when the aircraft that vacated it reports that it is **already at another level**, or passing a level with the minimum separation[^12]:

- when **severe turbulence** is known to exist;
- when the higher aircraft is making a **cruise climb**;
- when the **difference in performance** between the two may lead to less than the minimum separation.

In the APP the rule is the same. With severe turbulence, the clearance is withheld until the aircraft that vacated the level reports being at another level with the minimum separation[^13].

!!! example "Example"
    A B738 is at FL 160 and a C208 at FL 150. You want to descend the C208 to FL 140 and the B738 to FL 150. The B738 may only receive FL 150 after the C208 reports **leaving FL 150**. But the B738 descends much faster than the C208. That is the third exception: wait for the C208 to report maintaining FL 140, or having passed FL 140 with margin, before clearing the B738.

With ATS surveillance, Mode C or ADS-B shows each aircraft's level. ICA 100-37 defines when an aircraft is **maintaining**, **vacating**, **passing** or **reaching** a level from the screen readout. The criteria are in the [Vectoring and Sequencing Manual](../vetoracao-sequenciamento/01-fundamentos.en.md#levels-on-the-screen).

### In the hold

In the same holding pattern, aircraft descending at very different rates can lose separation, even with one starting above the other. If necessary, give a **maximum rate of descent** to the higher one and a **minimum rate** to the lower one[^14].

## Crossing another aircraft's level

For an aircraft to climb or descend **through** another aircraft's level, vertical separation must be replaced by horizontal separation during the crossing.

- **With ATS surveillance**, keep 5 NM between the targets throughout the crossing.
- **Without surveillance**, use the longitudinal minima for climbing or descending aircraft, in [Horizontal Separation](03-horizontal.en.md#climbing-or-descending).

!!! note "Good practice"
    When the level change is large, first clear the aircraft to the level **adjacent** to the other's, with a time, fix or DME restriction to continue. ICA 100-37 itself suggests this to ensure the minimum separation at the moment of crossing[^15].

    > **TAM 3246, climb to FL 090 until 15 miles from Campinas VOR.**

## Level restrictions

The safest way to ensure vertical separation at a point is to say **where** the aircraft must be above or below a level. You may also clear the level change at a specified time, place or vertical rate[^16].

> **ABJ 9203, cross NEROK at FL 240 or below.**
>
> **TAM 3506, cleared to KONSO FL 180, cross Santa Cruz VOR at FL 120 or above.**

Rate of climb and descent restrictions are in [Speed Control](../vetoracao-sequenciamento/03-velocidade.en.md#vertical-speed-control), in the Vectoring and Sequencing Manual.

[^1]: **ICA 100-37, Art. 322**. See [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 323**.
[^3]: **AIP-Brasil, ENR 2.2, items 1.1 and 1.3**.
[^4]: **AIP-Brasil, ENR 2.2, item 1.6**.
[^5]: **ICA 100-37, Art. 432**.
[^6]: **AIP-Brasil, ENR 2.2, item 1.8.1**, and **MCA 100-16, Arts. 48 and 76**. See [MCA 100-16](https://publicacoes.decea.mil.br/publicacao/MCA-100-16).
[^7]: **ICA 100-37, Art. 325**, and **ICA 100-12, Art. 142 and Annex IV**. See [ICA 100-12](https://publicacoes.decea.mil.br/publicacao/ica-100-12).
[^8]: **ICA 100-37, Art. 326**.
[^9]: **ICA 100-37, Art. 329 and sole paragraph**.
[^10]: **ICA 100-37, Art. 328**.
[^11]: **ICA 100-37, Art. 330**.
[^12]: **ICA 100-37, Art. 330, items I to III, and Art. 331**.
[^13]: **ICA 100-37, Art. 433 and sole paragraph**.
[^14]: **ICA 100-37, Art. 332**.
[^15]: **ICA 100-37, Art. 364, § 2°**, and **Art. 373, sole paragraph**. Phraseology from **MCA 100-16, Art. 118**.
[^16]: **ICA 100-37, Art. 327**. Phraseology from **MCA 100-16, Art. 92**.
