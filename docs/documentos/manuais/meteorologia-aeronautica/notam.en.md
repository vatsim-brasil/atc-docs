---
title: NOTAM
icon: material/alert-circle
---

--8<-- "includes/abreviacoes.md"

![Phraseology Manual - NOTAM](img/manual-meteorologia-notam.png)

#

## What is a NOTAM?

A NOTAM is an official notice used to report **temporary changes** or **critical information** affecting operations, such as:

- closed runways/intersections,
- unavailable navigation aids,
- changed procedures,
- airspace restrictions,
- obstacles and lighting,
- special operations (events, flow, etc.).

!!! tip "Operational"
    NOTAMs are part of "non-meteorological operational risk", but they frequently **interact** with weather:
    - low visibility + contaminated runway/works
    - low ceiling + unavailable navaid
    - CB/TS + restricted RNAV/ILS procedure

---

## Structure (mind map)

Most common fields:

- **Q)**: classification/scope (Q code), FIR, vertical limits and area
- **A)**: location (aerodrome/area)
- **B)**: start (UTC)
- **C)**: end (UTC) (or `PERM`)
- **D)**: schedule (when applicable)
- **E)**: main text (what changes / what is unavailable)
- **F)/G)**: levels (when applicable)

> Aeronautical abbreviations vary; use the AIP/GEN and official lists. See [References](referencias.en.md).

---

## Lookup (AISWEB)

- NOTAM page (AISWEB): basic queries and "latest NOTAMs issued".
- NOTAMs for an aerodrome also appear on the aerodrome page (AISWEB).

---

## Real examples (AISWEB and DECEA documents)

### List of "latest NOTAMs issued" (sample)

> Example of how AISWEB lists the number, location and date/time (summarised format).

```text
E7505/25 SBRJ E 29/12/25 12:29
E7504/25 SBRJ E 29/12/25 12:28
E7503/25 SBRJ E 29/12/25 12:28
E7502/25 SBRJ E 29/12/25 11:31
E7501/25 SBRJ E 29/12/25 11:30
E7500/25 SBRJ E 29/12/25 11:30
B2878/25 SBRJ B 29/12/25 08:49
```

### NOTAM with "Q) / A) / B) / C) / E)" (example from a DECEA report)

```text
SBRJ B3118/24 NOTAMN
Q) SBRE/QPFCA/IV/NBO/AE/000/999/1632S03906W005
A) SBTV - PORTO SEGURO/TERRAVISTA,BA
B) 21/12/24 00:00 - C) 06/01/25 23:59 UTC
E) PROC CTL FLUXO ACT ACFT TKOF DE SBTV COM DEST A SBXP (TMA-SP) ...
```

**Operational reading:**

Quickly identify: what, where, when, and how it has an impact.

Field E) is the "heart" (restriction/procedure).

---

## Reading pattern (quick check)

1. **Validity (B/C)**: is it in effect for your time?
2. **Location (A)**: does it affect your aerodrome/route/area?
3. **Text (E)**: does it affect the runway, approach, minima, taxi, departure, SID/STAR?
4. **Mitigation**: change procedure, change window, select an alternate, rebrief.

---

## Common mistakes

- Ignoring the time (UTC) and applying a NOTAM outside its validity.
- Skimming and missing details (closed intersection, partial restriction, daily window DLY).
- Not cross-checking NOTAMs with METAR/TAF: degraded weather + operational restriction amplifies risk.
