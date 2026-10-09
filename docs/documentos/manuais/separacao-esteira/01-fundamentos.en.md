---
title: Separation Fundamentals
icon: material/arrow-split-horizontal
---

--8<-- "includes/abreviacoes.md"

![Separation and Wake Turbulence Manual - Fundamentals](img/manual-separacao-fundamentos.png)

#

## What separating means

To provide the Air Traffic Control Service, the ATC unit needs to know where each aircraft is and where it is going, determine their positions relative to each other, and issue clearances and information **to prevent collisions** and keep traffic flowing in an orderly way[^1]. Separation is the part of this that has a number: keeping at least a defined vertical, lateral or longitudinal distance between two aircraft. That number is the **separation minimum**.

The minimum is a floor, not a target. Two general rules apply to every minimum in this manual:

- **No clearance may reduce separation below the applicable minimum.** This applies to any manoeuvre you clear, not only the ones you planned[^2].
- **If the separation in use cannot be maintained, establish another before losing the first.** If two aircraft are separated by level and one needs to descend, horizontal separation must already exist when it leaves the level[^3].

When an equipment failure or degradation (navigation, communication, altimeter or another system) leaves the aircraft below the required performance, the crew must report it, and the controller switches to another type or minimum of separation[^4]. In exceptional circumstances, such as unlawful interference or navigation difficulties, apply separations **larger** than the minima[^5].

## Who receives separation

Control does not separate everyone from everyone. The obligation depends on the airspace class and on the flight rules of each aircraft[^6]:

| Class | Control separates |
| --- | --- |
| **A** and **B** | All flights from each other |
| **C** | IFR from IFR and IFR from VFR. Not VFR from VFR |
| **D** and **E** | IFR from IFR only |
| **F** | IFR from IFR, when practical and possible |
| Any class | IFR from special VFR, and special VFR from special VFR |

Where control does not separate, it informs. In class D, for example, an IFR and a VFR flight receive **traffic information** about each other, and it is up to the pilots to keep clear. The classes and the service each one receives are in the [Airspace and ATS Services Manual](../espaco-aereo-servicos-ats/02-classes.en.md).

!!! info "Aerodrome traffic"
    In the tower, besides what the class requires, separation between aircraft using the same runway follows specific runway and wake turbulence rules. They are in [Aerodrome Separation](05-aerodromo.en.md).

## Forms of separation

Separation can be provided in three forms[^7]:

| Form | How | Page |
| --- | --- | --- |
| **Vertical** | Different levels or altitudes | [Vertical Separation](02-vertical.en.md) |
| **Horizontal lateral** | Different routes, or different geographical areas | [Horizontal Separation](03-horizontal.en.md) |
| **Horizontal longitudinal** | A time or distance interval between aircraft on the same, opposite or crossing routes | [Horizontal Separation](03-horizontal.en.md) |

**One** of them is enough. Two aircraft 1,000 ft apart are separated, even if one is directly above the other. Two aircraft at the same level 5 NM apart, with ATS surveillance, are separated too.

There is also **composite separation**, which combines vertical separation with a horizontal one, using half of each minimum. It may only be applied where DECEA authorises it[^8] and is not used on the network.

### With or without ATS surveillance

Horizontal minima change a lot depending on whether the controller has ATS surveillance (radar, ADS-B or MLAT):

- **With surveillance**, you measure the distance between the targets on the screen. The normal minimum is **5 NM**.
- **Without surveillance**, separation is **procedural**. You rely on position reports, estimates and DME or GNSS distances reported by the pilot, and the minima are much larger: 10 to 15 minutes, or 20 NM.

On Vatsim Brasil, almost every APP and CTR position has surveillance, and procedural separation rarely appears over the continent. It still matters. It is the basis of oceanic control, it is what is left when a target disappears from the screen, and it explains rules that radar control inherited, such as the departure minima.

## Own separation in VMC

In classes **D** and **E**, a controlled flight may ask to **maintain its own separation** from another aircraft while remaining in visual meteorological conditions (VMC). When the other pilot agrees, control may authorise it[^9]. This also applies to IFR flights, and it is the exception to the rule of separating IFR from IFR[^10].

The conditions are[^9]:

- **daytime** only;
- only for **a specific portion of the flight**, during climb or descent, at **10,000 ft or below**;
- if VMC may not be maintained, you give an **alternative instruction**, in case the pilot cannot keep visual conditions during the authorisation;
- if conditions are deteriorating, the pilot reports **before** entering IMC and follows the alternative instruction.

During that portion, control does not apply separation between the two aircraft. The pilots keep clear of each other[^11].

> **PT ABC, traffic Boeing 737, 084 radial of Cuiabá VOR, climbing VMC until FL 140.**
>
> **GLO 1844, cleared to descend in VMC.**
>
> **FAB 2123, maintain own separation.**

Source: MCA 100-16[^16].

The visual approach with an instruction to **follow and maintain own separation** from the preceding aircraft is the most common case of this idea. It is in the [Vectoring and Sequencing Manual](../vetoracao-sequenciamento/04-sequenciamento.en.md#successive-visual-approaches).

## Essential traffic

**Essential traffic** is controlled traffic to which control should provide separation, but which, in relation to a given flight, is not or will not be separated from it by the minima[^12]. This happens precisely with own separation in VMC, or when a minimum has been lost.

Whenever two controlled flights are essential traffic to each other, inform both[^13]. The information contains[^14]:

- the direction of flight and the aircraft type;
- the **wake turbulence category**, but only if the other aircraft is in a **heavier** category than the one receiving the information;
- the level and one of the following: the estimated time over the reporting point nearest to where the levels will be crossed, the relative position by the clock and the distance, or the actual or estimated position.

A VFR flight is never essential traffic to another VFR flight, except in class B[^15].

[^1]: **ICA 100-37, Art. 30, items I to III**. See [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 39, § 8°**.
[^3]: **ICA 100-37, Art. 42**.
[^4]: **ICA 100-37, Art. 43 and sole paragraph**, and **Art. 337**.
[^5]: **ICA 100-37, Art. 41 and §§ 1° and 2°**.
[^6]: **ICA 100-37, Art. 39, items I to V and § 1°**.
[^7]: **ICA 100-37, Art. 39, § 2°, items I and II**, and **Art. 334**.
[^8]: **ICA 100-37, Art. 39, § 2°, item III, and § 3°**.
[^9]: **ICA 100-37, Art. 94 and § 1°**.
[^10]: **ICA 100-37, Art. 40**.
[^11]: **ICA 100-37, Art. 94, §§ 2° and 3°**.
[^12]: **ICA 100-37, Art. 114**.
[^13]: **ICA 100-37, Art. 115 and sole paragraph**.
[^14]: **ICA 100-37, Art. 116**.
[^15]: **ICA 100-37, Art. 114, § 4°**.
[^16]: **MCA 100-16, Art. 117**. See [MCA 100-16](https://publicacoes.decea.mil.br/publicacao/MCA-100-16).
