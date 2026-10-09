---
title: Introduction
icon: material/swap-horizontal-bold
---

--8<-- "includes/abreviacoes.md"

# Introduction

## Overview

No controller follows a flight from start to finish. The clearance comes from delivery, the taxi belongs to ground, the take-off to the tower, the climb to approach, the cruise to the center, and the order is reversed on arrival. At each boundary the flight changes hands, and the service must continue as if it had not. Coordination is what makes sure of that.

ICA 100-37 defines air traffic coordination as "the exchange of information for the purpose of ensuring the continuity of the provision of air traffic services"[^1]. The transfer is the moment that exchange is completed: responsibility for control, and then communication with the pilot, pass from one controller to the other.

This manual is for anyone who will control any position at Vatsim Brasil, from `DEL` to `CTR`. It covers what to coordinate, when, with whom, and how to transfer an aircraft without it being left, even for a moment, with no one responsible for it. It also covers what is specific to the network: top-down coverage, neighbouring positions that open and close during the session, and the EuroScope tools.

| Revision | Date       | Description         | Reviewer |
| -------- | ---------- | ------------------- | -------- |
| 10/2026  | 08/10/2026 | Manual created      | —        |

## About this Manual

The regulatory basis is **ICA 100-37**[^2]: Chapter X (Coordination) and Subsection V of Section XVII of Chapter XI (transfer of control with ATS surveillance). Coordination messages follow Annex II of **MCA 100-16**[^3], and phraseology with the pilot follows Chapter IV of the same manual. What is specific to the network follows the VATSIM **Global Controller Administration Policy (GCAP)**[^4].

When the real-world rule and network practice differ, the manual shows both and says which one applies at Vatsim Brasil. Passages on technique, which are not regulation, are marked as good practice.

## Scope

This manual covers:

- the concept of coordination and the general rules that apply between any units or positions;
- transfer of control and transfer of communications, with and without ATS surveillance;
- coordination between each pair of units: ACC and ACC, ACC and APP, APP and TWR, TWR and ground, and positions of the same unit;
- coordination of flights entering or leaving controlled airspace;
- coordination on the network: top-down coverage, opening and closing positions, unstaffed airspace and EuroScope tools;
- coordination messages and transfer phraseology, in Portuguese and English.

## Out of scope

The following are not part of this manual:

- the transfer points and specific agreements of each unit, which are in the operations manuals and the letters of agreement;
- coordination in oceanic airspace, which has its own rules in the [Atlântico FIR MOP](../../../MOP/oceanico/atc/coordenacao.en.md);
- coordination with meteorology, airport management and telecommunications stations;
- air traffic flow management (CGNA) and flow control measures.

!!! warning "Important"
    Content intended for the flight simulation environment. In real-world operations, always use the current official publications, aeronautical charts and AIS and ATS channels.

## How to use this manual

1. Read **Coordination Fundamentals** to learn the rules that apply at any boundary.
2. Read **Transfer of Control** to learn how and when an aircraft changes hands.
3. Check **Coordination between Units** for what each pair of units exchanges.
4. Read **Coordination on the Network** before your first session: this is where VATSIM differs from the real world.
5. Check the **Phraseology** for messages between controllers and instructions to the pilot.
6. Review the **Quick Checklist** before opening a position.

!!! tip "Further reading"
    This manual assumes the units and positions in the [Airspace and ATS Services Manual](../espaco-aereo-servicos-ats/04-orgaos.en.md). The transfer of vectored aircraft and the handover from final to the tower also appear in the [Vectoring and Sequencing Manual](../vetoracao-sequenciamento/index.en.md). The top-down coverage of each TMA is in the [Terminals](../../../MOP/terminais/index.en.md) section.

[^1]: **ICA 100-37, Art. 814**.
[^2]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37) (*Air Traffic Services*): regulates in Brazil the Air Traffic Services provided for in ICAO Annex 11 and Doc 4444. Edition in force since 27/11/2025.
[^3]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16) (*Air Traffic Phraseology*): establishes the air traffic phraseology standards. Edition approved by Portaria DECEA/DNOR1 n° 1.716, of 28/04/2025.
[^4]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), version 2.0, of 15/08/2026: defines the network's control positions and the top-down principle.
