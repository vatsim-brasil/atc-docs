---
title: Introduction
icon: material/radar
---

--8<-- "includes/abreviacoes.md"

![Vectoring and Sequencing Manual - Introduction](img/manual-vetoracao-intro.png)

#

## Overview

In procedural control, the controller knows where the aircraft is because the pilot reports it. With ATS surveillance, the controller sees the aircraft on the screen, and that changes what can be done: instead of waiting for the aircraft to reach a fix, the controller can **take it** where it needs to go, using headings, levels and speeds. That is vectoring.

In the approach phase, vectoring has a practical goal: to put arriving aircraft **in line on final, with the right spacing and minimum delay**. That is sequencing. To do it, the controller combines three tools: the track (headings and shortcuts), speed and, when nothing else works, holding.

This manual is for anyone who will control an approach (`APP`) or center (`CTR`) position at Vatsim Brasil and needs to vector safely: when it is allowed, how to do it, what to say on the frequency and how to build a sequence that works.

| Revision | Date       | Description         | Reviewer |
| -------- | ---------- | ------------------- | -------- |
| 10/2026  | 08/10/2026 | Manual created      | —        |

## About this Manual

The regulatory basis is **ICA 100-37**[^1]: Chapter XI (ATS Surveillance Service) for identification, vectoring and separation; Chapter V (Approach Control Service) for approach sequence, visual approach and expected approach time; and Sections XXXI to XXXIII of Chapter III for speed control and holding. Phraseology follows **MCA 100-16**[^2].

Some parts of the manual are **technique**, not regulation: turn geometry, recommended intercept distances and rules of thumb for spacing. These passages are marked as good practice. When a good practice and ICA 100-37 seem to disagree, ICA 100-37 prevails.

## Scope

This manual covers:

- aircraft identification and the start of the ATS surveillance service;
- vectoring: purposes, methods, responsibilities and termination;
- minimum separation with ATS surveillance and wake turbulence minima on approach;
- vectoring techniques to intercept a radial, a final approach course or a visual approach;
- horizontal and vertical speed control;
- arrival sequencing, from the approach sequence to the transfer to the tower;
- holding and expected approach time;
- the corresponding phraseology, in Portuguese and English.

## Out of scope

The following are not part of this manual:

- coordination between units and transfer of control, which will have their own manual;
- procedural separation (by time, DME distance or position report);
- time-based wake turbulence minima on the runway, which belong to aerodrome control;
- surveillance radar and precision radar (PAR) approaches, which DECEA restricts to specific cases in Brazil[^3];
- operations on parallel runways.

!!! warning "Important"
    Content intended for the flight simulation environment. In real-world operations, always use the current official publications, aeronautical charts and AIS and ATS channels.

## How to use this manual

1. Read **Vectoring Fundamentals** to learn when you may vector, what becomes your responsibility and which separation to apply.
2. Read **Vectoring Techniques** to take the aircraft where it needs to go, especially to the final approach.
3. Read **Speed Control** to learn the limits and the method of speed control.
4. Read **Sequencing** to put it all together: arrival order, spacing on final, holding and transfer to the tower.
5. Check the **Phraseology** whenever you are unsure what to say.
6. Review the **Quick Checklist** before opening an approach position.

!!! tip "Further reading"
    This manual assumes the concepts in the [Airspace and ATS Services Manual](../espaco-aereo-servicos-ats/index.en.md): airspace classes, TMA, CTR, levels and transition altitude. For using EuroScope (tags, `F1 + S`, `F1 + D`), see [EuroScope](../../../fundamentos/softwares/euroscope/index.en.md). The limits and procedures of each TMA are in the [Terminals](../../../MOP/terminais/index.en.md) section.

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37) (*Air Traffic Services*): regulates in Brazil the Air Traffic Services provided for in ICAO Annex 11 and Doc 4444. Edition in force since 27/11/2025.
[^2]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16) (*Air Traffic Phraseology*): establishes the air traffic phraseology standards. Edition approved by Portaria DECEA/DNOR1 n° 1.716, of 28/04/2025.
[^3]: **ICA 100-37, Arts. 1020 and 1023**: a surveillance radar approach is only authorized at the pilot's request or when no other published procedure is available, and PAR is performed in Brazil only by military aircraft.
