---
title: Introduction
icon: material/radio-tower
---

--8<-- "includes/abreviacoes.md"

# Introduction

## Overview

Many Brazilian aerodromes have no control tower. At these aerodromes, the unit that talks to the pilot is the **RADIO**: the unit that provides the Aerodrome Flight Information Service, AFIS. The RADIO does not clear landings, does not clear take-offs and does not separate traffic. It gives the wind, the altimeter setting, the aerodrome conditions and the known traffic, receives the pilot's intentions and reports, and activates the Alerting Service when something goes wrong. The pilot makes the decisions.

It is the easiest position to open and one of the easiest to get wrong. Controllers coming from the tower tend to "clear" out of habit. Those coming from approach tend to vector. At the RADIO, neither exists. What exists is good information, at the right time, and the word **roger**.

This manual is for anyone who will open a RADIO position (`_R_TWR`) at Vatsim Brasil and for anyone who, at approach or the center, covers an AFIS aerodrome top-down. It covers what AFIS provides and what it does not, how to handle VFR and IFR arrivals and departures on the frequency, and what is specific to the network.

| Revision | Date       | Description         | Reviewer |
| -------- | ---------- | ------------------- | -------- |
| 11/2026  | 05/11/2026 | Manual created      | —        |

## About this Manual

The regulatory basis is **ICA 100-37**[^1]: Section V of Chapter VIII (Aerodrome Flight Information Service – AFIS, Arts. 782 to 791), Sections XX and XXI of Chapter III (instrument descent at an aerodrome provided with AFIS and operation at an uncontrolled aerodrome, Arts. 140 to 164) and Chapter IX (Alerting Service). Phraseology follows Section VI of **MCA 100-16**[^2], dedicated to AFIS (Arts. 153 to 158). The flight information zones come from **AIP-Brasil, ENR 2.2**[^3]. What is specific to the network follows the VATSIM **Global Controller Administration Policy (GCAP)**[^4] and **Code of Conduct**[^5].

When the real-world rule and network practice differ, the manual shows both and says which one applies at Vatsim Brasil. Passages on technique, which are not regulation, are marked as good practice.

## Scope

This manual covers:

- what AFIS is, who provides it, where (FIZ and the vicinity of the aerodrome) and what it does and does not provide;
- flight and traffic information on the frequency, and the relay of clearances from other units;
- arrival and departure of VFR and IFR flights at an AFIS aerodrome;
- the Alerting Service at the aerodrome;
- the RADIO position on the network: suffix, rating, top-down coverage, traffic frequency with no controller, and coordination with approach and the center;
- AFIS phraseology, in Portuguese and English.

## Out of scope

The following are not part of this manual:

- aerodrome control, which belongs to the tower: landing, take-off and taxi clearances, and runway separation;
- the traffic circuit in detail, which is in the [Traffic Circuit Manual](../manual-circuito-trafego/index.md);
- the en-route Flight Information Service, provided by the center, which appears in the [Airspace and ATS Manual](../espaco-aereo-servicos-ats/03-servicos.en.md);
- aeronautical telecommunications stations and the aerodrome AIS office;
- real-world AFIS operating hours.

!!! warning "Important"
    Content intended for the flight simulation environment. In real-world operations, always use the current official publications, aeronautical charts and AIS and ATS channels.

## How to use this manual

1. Read **AFIS Fundamentals** to learn what the RADIO provides and, above all, what it does not.
2. Read **Working the Frequency** to handle arrivals and departures, VFR and IFR.
3. Read **AFIS on the Network** before your first session: this is where VATSIM differs from the real world.
4. Check the **Phraseology** for transmissions in Portuguese and English.
5. Review the **Quick Checklist** before opening the position.

!!! tip "Further reading"
    The boundary between informing and controlling is in the [Airspace and ATS Manual](../espaco-aereo-servicos-ats/03-servicos.en.md#informing-is-not-controlling). The pilot's point of view, on a complete flight to a RADIO aerodrome, is in the [VFR Phraseology Manual](../fraseologia-voo-visual/voo-ida.en.md). The frequency and callsign of each RADIO are on the [aerodrome](../../../MOP/aerodromos/index.en.md) pages.

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulates in Brazil the Air Traffic Services provided for in ICAO Annex 11 and Doc 4444. Edition in force on 27/11/2025.
[^2]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): sets the air traffic phraseology standards. Edition approved by Portaria DECEA/DNOR1 n° 1.716, of 28/04/2025.
[^3]: [**AIP-Brasil, ENR 2.2, Other regulated airspace**](https://aisweb.decea.mil.br/?i=publicacoes&p=aip): lists the FIZ with limits, class, unit, callsign and frequency. Amendment of 01/10/2026.
[^4]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), version 2.0, of 15/08/2026: defines the network's control positions, the required ratings and the top-down principle.
[^5]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct): rules of conduct for pilots and controllers on the network.
