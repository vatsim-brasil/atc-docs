---
title: Introduction
icon: material/arrow-expand-vertical
---

--8<-- "includes/abreviacoes.md"

![Separation and Wake Turbulence Manual - Introduction](img/manual-separacao-intro.png)

#

## Overview

Separating aircraft is the reason air traffic control exists. Every other task revolves around it: clearing levels and routes, vectoring, adjusting speeds, coordinating with the adjacent unit and sequencing the runway. They share one goal: two aircraft must never get closer than a defined **minimum**.

These minima depend on what the controller knows about each aircraft. With ATS surveillance, the controller sees both on the screen and measures the distance between them. Without surveillance, the controller relies on levels, times and DME distances reported by the pilots. On the runway, the reference is what the tower sees. And on top of all this is **wake turbulence**: a large aircraft leaves behind air that a smaller aircraft cannot handle, and that calls for more space than collision avoidance alone.

This manual is for anyone who will control a position responsible for separation on Vatsim Brasil: tower (`TWR`), approach (`APP`) or centre (`CTR`). It shows which separation each flight receives, what the minima are and how to apply them on the network.

| Revision | Date       | Description        | Reviewer |
| -------- | ---------- | ------------------ | -------- |
| 10/2026  | 08/10/2026 | Manual created     | —        |

## About this Manual

The regulatory basis is **ICA 100-37**[^1]:

- Arts. 39 to 43 and Sections XI and XVI of Chapter III, for who receives separation, in which forms, and own separation in VMC;
- Sections XXVI to XXIX of Chapter III, for wake turbulence;
- Section III of Chapter IV, for vertical, lateral and longitudinal minima;
- Sections IV, V and XVI of Chapter V, for departures and arrivals in approach control;
- Sections XIV to XVI of Chapter VI, for runway separation;
- Subsections II and III of Section XVII of Chapter XI, for separation with ATS surveillance.

Cruising levels come from **ICA 100-12**[^2] and phraseology from **MCA 100-16**[^3].

Some parts of the manual are **technique**, not regulation: how to set up a climb through another aircraft's level, how to time wake turbulence in the tower, and rules of thumb for the screen. These parts are marked as good practice. When a good practice and ICA 100-37 seem to disagree, ICA 100-37 prevails.

## Scope

This manual covers:

- who receives separation in each airspace class, and the forms of separation;
- own separation in VMC and essential traffic information;
- vertical separation: minima, RVSM and the use of levels vacated by another aircraft;
- procedural horizontal separation: lateral, time-based and by DME or GNSS distance;
- horizontal separation with ATS surveillance;
- wake turbulence: categories, distance- and time-based minima, exemptions and cautions;
- separation at the aerodrome: on the runway, between departures, and between departures and arrivals;
- the corresponding phraseology, in Portuguese and English.

## Out of scope

The following are not part of this manual:

- separation in oceanic airspace, the Mach number technique and minima based on RNP, ADS-C or CPDLC, which are in the [Atlântico FIR MOP](../../../MOP/oceanico/atc/separacao.en.md);
- composite separation, time-based separation on final (TBS) and reduced radar minima, which depend on specific DECEA authorisation;
- operations on parallel runways, which have their own rules in Chapter VII of ICA 100-37;
- vectoring and speed control techniques used to achieve separation, which are in the [Vectoring and Sequencing Manual](../vetoracao-sequenciamento/index.en.md).

!!! warning "Important"
    Content intended for the flight simulation environment. In real-world operations, always use the current official publications, aeronautical charts and AIS and ATS channels.

## How to use this manual

1. Read **Separation Fundamentals** to learn who receives separation and in which forms it can be provided.
2. Read **Vertical Separation** and **Horizontal Separation** to learn the minima and when to use each.
3. Read **Wake Turbulence** to learn when the wake minimum replaces the normal minimum.
4. Read **Aerodrome Separation** if you will control a tower, or need to know what the tower expects from the APP.
5. Check the **Phraseology** whenever you are unsure what to say.
6. Go through the **Quick Checklist** before opening the position.

!!! tip "Further reading"
    This manual assumes the concepts in the [Airspace and ATS Services Manual](../espaco-aereo-servicos-ats/index.en.md): airspace classes, cruising levels and transition altitude. Separation with ATS surveillance is applied in practice through vectoring, covered in the [Vectoring and Sequencing Manual](../vetoracao-sequenciamento/index.en.md). What to agree with the adjacent unit to keep separation at the transfer is in the [Coordination and Transfer Manual](../coordenacao-transferencia/index.en.md).

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37) (*Air Traffic Services*): regulates in Brazil the Air Traffic Services provided for in ICAO Annex 11 and Doc 4444. Edition in force since 27/11/2025.
[^2]: [**ICA 100-12, Regras do Ar**](https://publicacoes.decea.mil.br/publicacao/ica-100-12) (*Rules of the Air*): sets out the rules of the air, including the cruising level tables in Annex IV. Edition approved by DECEA/DNOR1 Ordinance No. 1,536 of 31/10/2024.
[^3]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16) (*Air Traffic Phraseology*): sets the standards for air traffic phraseology. Edition approved by DECEA/DNOR1 Ordinance No. 1,716 of 28/04/2025.
