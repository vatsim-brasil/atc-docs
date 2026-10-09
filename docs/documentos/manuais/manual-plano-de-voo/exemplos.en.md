---
title: Practical examples
icon: material/book-open-page-variant
---

# Practical examples

The examples below are designed for **simulation** (VATSIM) and serve as a consistency reference.

## Example 1 — Local VFR (low height)

| Item | Entry | Comment |
|---:|---|---|
| 7 | `PTABC` | Registration (up to 7) |
| 8 | `V/G` | VFR / General Aviation |
| 9 | `1/C172/L` | 1 aircraft, type, wake category |
| 10 | `S/C` | Standard + transponder as applicable |
| 13 | `SBSP 1400` | Departure + EOBT (UTC) |
| 15 | `VFR` | Outside the table → detail in RMK |
| 16 | `SBSP 0045` | Local + total duration |
| 18 | `RMK/1500FT AGL LOCAL` | Height/location detail |
| 19 | (when required) | Usually omitted in simulation |

## Example 2 — Domestic IFR (with airways)

| Item | Entry | Comment |
|---:|---|---|
| 7 | `GLO1866` | Airline + number |
| 8 | `I/S` | IFR / Scheduled |
| 9 | `1/B738/M` | B738, medium wake category |
| 10 | `SG/C` | S + GNSS (when applicable) |
| 13 | `SBGR 2230` | Departure + EOBT |
| 15 | `N0475 F350 DCT ...` | Speed, level, route |
| 16 | `SBRJ 0055 SBSP SBGL` | Destination+EET + alternates |
| 18 | `DOF/260117` | Date of flight |

> In the route, replace `...` with the actual fixes/airways from your planning (e.g. SimBrief/Navigraph).

## “Form” template (to copy)

Fill it in and keep it as a personal checklist:

| Field | Value |
|---|---|
| Aircraft (ITEM 7) | `_______` |
| IFR/VFR + Type (ITEM 8) | `_______` |
| Type + WTC (ITEM 9) | `_______` |
| Equipment (ITEM 10) | `_______` |
| Departure + EOBT (ITEM 13) | `_______` |
| Speed/Level/Route (ITEM 15) | `_______` |
| Destination+EET+ALTN (ITEM 16) | `_______` |
| Other information (ITEM 18) | `_______` |

---
