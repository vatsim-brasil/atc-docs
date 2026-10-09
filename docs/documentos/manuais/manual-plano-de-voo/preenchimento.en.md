---
title: Filling in the FPL (Main fields)
icon: material/file-edit
---

# Filling in the FPL (Main fields)

This section covers the fields that normally **always** appear in a consistent FPL.

> Convention: whenever a field is “unknown” to the ICAO standard (no designator), it is customary to use **ZZZZ** and detail it in **ITEM 18** with the appropriate indicator (e.g. `DEP/`, `DEST/`, `ALTN/`, `TYP/`).

## ITEM 7 — Aircraft identification

Golden rule: **up to 7 characters**, alphanumeric, no hyphens/symbols.

| Situation | What to enter | Example |
|---|---|---|
| Commercial flight (airline) | ICAO telephony designator + flight number | `GLO1866`, `NGA213` |
| General aviation (registration) | Nationality/common mark + registration | `PTRBA`, `PRERR`, `N256GA` |
| Other official designator | According to the applicable registration | `FAB2506` |

**Important exception:** if the radiotelephony callsign **exceeds 7 characters**, fill in ITEM 7 with the registration and use `RMK/` in ITEM 18 to report the full callsign.

## ITEM 8 — Flight rules and type of flight

### Flight rules (1 letter)

| Code | Meaning |
|---|---|
| `I` | IFR (entire flight IFR) |
| `V` | VFR (entire flight VFR) |
| `Y` | IFR first, then changes to VFR |
| `Z` | VFR first, then changes to IFR |

### Type of flight (1 letter)

The type of flight depends on the context (e.g. general aviation, commercial, military). In simulation, it is common to see:

| Code | Typical use |
|---|---|
| `S` | Scheduled (airlines) |
| `N` | Non-scheduled (charter/general) |
| `G` | General aviation |
| `M` | Military |
| `X` | Other |

> Operational tip: on VATSIM, **`G` (general aviation)** and **`S` (airlines)** cover most cases.

## ITEM 9 — Number, type of aircraft and wake turbulence category

| Field | How to fill in | Example |
|---|---|---|
| Number | Quantity, when it is a **formation** | `2`, `4` |
| Aircraft type | ICAO designator (Doc 8643) | `B738`, `A320`, `E110` |
| No designator / specific military | Use `ZZZZ` and detail in ITEM 18 (`TYP/`) | `ZZZZ` + `TYP/KC130` |
| Wake turbulence | `J` SUPER, `H` HEAVY, `M` MEDIUM, `L` LIGHT | `M` |

## ITEM 10 — Equipment and capabilities

This field is divided into two blocks:

1) **COM/NAV/APP** (left side)
2) **Surveillance / Transponder** (right side)

### Safe shortcut (for simulation)

- If your aircraft has the “standard package” of radios/navigation for the route: use **`S`**
- If you want to explicitly indicate GNSS/RNAV for IFR: include **`G`**

> In real-world operations, ITEM 10 can get long. In simulation, what matters is consistency: the declared equipment must reflect what you intend to use.

## ITEM 13 — Departure aerodrome and time

| Field | How to fill in | Example |
|---|---|---|
| Departure | ICAO (4 letters). If none exists: `ZZZZ` + `DEP/` in ITEM 18 | `SBSP` |
| Time | **EOBT** (off-blocks) in UTC, 4 digits | `1435` |

## ITEM 15 — Speed, level and route

### Speed (up to 5)

| Format | Example | Note |
|---|---|---|
| `K####` | `K0650` | km/h |
| `N####` | `N0480` | knots |
| `M###` | `M082` | Mach |

### Level

| Format | Example | Note |
|---|---|---|
| `F###` | `F330` | flight level (FL) |
| `A###` | `A040` | altitude (hundreds of feet) |
| `VFR` | `VFR` | when the VFR flight does not follow the table and you detail it in `RMK/` |

### Route

- Use **ATS routes** (airways) when applicable.
- Use **`DCT`** for direct segments.
- If you use `Y` or `Z` (IFR/VFR change), the route must indicate the **change point(s)**.

## ITEM 16 — Destination, total EET and alternates

| Field | How to fill in | Example |
|---|---|---|
| Destination | ICAO (4 letters) or `ZZZZ` + `DEST/` in ITEM 18 | `SBBE` |
| Total EET | Total estimated elapsed time (HHMM), next to the destination | `0245` |
| Alternate 1/2 | ICAO (4 letters) or `ZZZZ` + `ALTN/` in ITEM 18 | `SBSL` / `SBTE` |

---
