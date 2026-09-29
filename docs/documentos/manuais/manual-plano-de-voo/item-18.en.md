---
title: Item 18 (Other Information)
icon: material/information-outline
---

![Flight Plan Manual (FPL) - Item 18](img/manual-plano-de-voo-item-18.png)

#

ITEM 18 is where you “close the contract” of the plan: performance details, RNAV/PBN, special points and remarks.

**Quality rule:** use **only the prescribed indicators** (e.g. `STS/`, `PBN/`, `DEP/`, `DEST/`, `ALTN/`, `REG/`, `DOF/`, `EET/`, `RMK/`). Made-up indicators tend to break processing.

## Most used indicators (practical)

| Indicator | What it is for | Example |
|---|---|---|
| `DEP/` | Detail the departure location when ITEM 13 = `ZZZZ` | `DEP/FAZENDA X 12NM N SBSP` |
| `DEST/` | Detail the destination when ITEM 16 = `ZZZZ` | `DEST/HELIPONTO Y` |
| `ALTN/` | Detail the alternate when the alternate = `ZZZZ` | `ALTN/AERODROMO PRIVADO Z` |
| `TYP/` | Aircraft type when ITEM 9 = `ZZZZ` | `TYP/KC130` |
| `REG/` | Registration (when necessary) | `REG/PTRBA` |
| `DOF/` | Date of flight (YYMMDD format) | `DOF/260117` |
| `EET/` | Estimates to FIR boundaries/relevant points (when applicable) | `EET/SBAO0130` |
| `RMK/` | Remarks in plain language or required codes | `RMK/500FT AGL` |

## STS/ (special handling)

Use when the flight requires special handling by ATS (e.g. search and rescue, medical evacuation, calibration etc.).

Common examples:

- `STS/SAR`
- `STS/FLTCK`

> When the reason is not in the prescribed list, use `RMK/` to explain it.

## PBN/ (RNAV/RNP)

Indicates the RNAV/RNP specifications applicable to the flight, by code (e.g. RNAV 1, RNAV 2, RNAV 5, etc.).

In simulation, keep it simple and consistent with the aircraft and the route. If you are not familiar with PBN, prefer to keep **the plan consistent with what you will actually fly** (for example, an RNAV SID/STAR requires appropriate RNAV capability).

## Useful templates (copy and adapt)

### VFR below the table (RMK example)

| Field | Value |
|---|---|
| ITEM 15 | `VFR` |
| ITEM 18 | `RMK/500FT AGL` |

### Aerodrome without ICAO code (ZZZZ)

| Field | Value |
|---|---|
| ITEM 13 | `ZZZZ` |
| ITEM 18 | `DEP/LOCATION OR COORDINATES` |

---
