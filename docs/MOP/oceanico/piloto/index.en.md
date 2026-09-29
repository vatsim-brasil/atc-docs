---
title: Operating in the Atlântico FIR
icon: material/airplane-takeoff
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

What you need to do to cross the Atlântico FIR while working with the service provided by the `SBAO_FSS` position.

## What changes

In the Atlântico FIR **there is no radar surveillance**[^1]. The controller cannot see your aircraft: they know where you are because you told them. Three consequences:

1. **You are the source of information.** A late report is a gap in the controller's situational awareness.
2. **Separations are much larger**, measured in minutes and tens of miles.
3. **Nothing is immediate.** A level request depends on calculations based on estimates, not on a picture on a screen.

## Before the flight

- Plan along the ATS routes of the EUR/SAM corridor, or between the AORRA gates.
- Check your level in the applicable table, in [Structure and sectorization](../atc/estrutura.en.md#niveis-de-cruzeiro).
- **Plan your speed as a Mach number**, in item 15, in the format `M` plus three digits, for example `M082`[^2]. Mach is the basis of separation in this FIR.

### In the flight plan

Declare **only what your aircraft actually does**. Declaring something you are not going to use is worse than not declaring it.

| Where      | What                                             | Why                                          |
| ---------- | ------------------------------------------------ | -------------------------------------------- |
| Item 10    | `W` if RVSM approved                             | Allows 1,000 ft between FL 290 and FL 410    |
| Item 10    | `R` if PBN approved, with `PBN/` in item 18      | Basis of the 50 NM lateral separation        |
| Item 10    | `J5`, `J6` or `J7` if you have satellite CPDLC   | Enables the datalink                         |
| Item 10b   | `D1` if you have ADS-C                           | Enables automatic position reporting         |
| Item 18    | `SEL/` and the SELCAL code                       | Allows selective calling                     |
| Item 18    | `EET/SBAO` and the time to the FIR               | Helps calculate your entry estimate          |

Without RVSM, insert `STS/NONRVSM`. Without RNP 10, `RMK/NONRNP10`. In both cases the separation applied to you will be larger.

!!! info "In the simulation"
    Nothing on the network verifies certification, so the controller will confirm with you on first contact. **Answer honestly.** If your add-on has no CPDLC, say so: the controller will simply apply another minimum, and nobody is worse off.

### Datalink

If you have CPDLC, log on to **`SBAO`** between **10 and 25 minutes before** entering the FIR[^3]. Use exactly the same callsign and registration as in the flight plan, or the logon is rejected[^4]. Coming from a FIR with datalink, the connection usually transfers on its own; check it when crossing the boundary.

## Initial contact

Call on the frequency listed in [Structure and sectorization](../atc/estrutura.en.md#posicoes-na-vatsim). The unit is **ATLANTICO CENTER**, or **CENTRO ATLÂNTICO**.

```text
ATLANTICO CENTER, CALLSIGN, POSITION at TIME, LEVEL, MACH
```

Even under ADS-C, **send a CPDLC position message on entering the FIR**[^5]. When using CPDLC, **do not** perform a SELCAL check on first contact unless the controller asks for it[^6].

## Position reports

```text
CALLSIGN, POSITION at TIME, LEVEL, MACH,
estimating NEXT POSITION at ESTIMATE, next ENSUING POSITION
```

!!! example "Example"
    *"Atlantico Center, EXEMPLO 123, position NIMAX at 1412, flight level 370, Mach decimal 82, estimating KOSAX at 1448, next TEBRO."*

**When to report:** at compulsory reporting points, when crossing the FIR boundaries, whenever the controller asks, and in the AORRA every 10° of longitude[^7]. With ADS-C working, a voice report is not required unless requested[^8].

**Estimates:** advise whenever one changes by more than **2 minutes**[^9], due to wind, speed or a deviation.

```text
CALLSIGN, revised estimate NEXT POSITION at ESTIMATE
```

If the controller has assigned a Mach number, include it in the report and also in the first call after any frequency change[^10].

## Level and Mach

- Request well in advance: the controller recalculates separation with everyone on your route.
- With an assigned Mach, **request approval before changing it**. If it is unavoidable, due to turbulence, advise as soon as you do it[^11].
- If you cannot maintain the Mach during a climb or descent, say so when requesting[^12].
- In RVSM airspace, report reaching the cleared level[^13].

## SLOP

Standard practice in this FIR[^14]: offset **to the right only**, from the centerline, 1 NM or 2 NM, **never** more than 2 NM nor to the left. **No clearance or notification to the controller is required.** Reports continue to be based on the current clearance, not on the offset.

## Deviations and failures

If you cannot comply with the clearance, or maintain the required navigation accuracy, **advise immediately**[^15]. When requesting a weather deviation, state in one go the side, the distance and the expected time off route. When returning, report rejoining with a revised estimate.

| Failed   | What to do                                                                       |
| -------- | -------------------------------------------------------------------------------- |
| CPDLC    | Revert to voice starting with `CPDLC FAILURE`                                    |
| Logon    | Check callsign and registration, correct them, try again; if it persists, advise by voice[^4] |
| Voice    | Use CPDLC until it is restored                                                   |
| Everything | Apply the communication failure procedures of the Rules of the Air, keep a listening watch on the sector frequency and on 123.45 MHz, and transmit position and intentions[^16] |

Turbulence preventing you from maintaining level: `CALLSIGN, UNABLE RVSM DUE TURBULENCE`. Once recovered: `CALLSIGN, READY TO RESUME RVSM`.

## Transfer

- `CONTACT UNIT on FREQ`: change frequency **and make** the initial call.
- `MONITOR UNIT on FREQ`: change frequency **without** an initial call[^17].
- If the controller advises that there is no unit ahead, maintain the last cleared level and speed and proceed as per the flight plan.

## Summary

1. Plan with a Mach number and check your level.
2. Declare only the capabilities you will actually use.
3. Log on to `SBAO` 10 to 25 minutes before entering, if you have CPDLC.
4. Report with time, level, Mach, next point with estimate and the ensuing point.
5. Advise any change in estimate greater than 2 minutes.

[^1]: **AIP-Brasil, ENR 1.6**.
[^2]: **MCA 100-11, item 2.2.6.1**.
[^3]: **AIP-Brasil, ENR 3.5, items 9.2.1 and 9.2.2**.
[^4]: **AIP-Brasil, ENR 3.5, items 9.2.4 and 9.2.5**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.5.2.1**.
[^6]: **AIP-Brasil, ENR 3.5, item 9.5.1.2**.
[^7]: **ICA 100-37, Art. 173**, and **AIP-Brasil, ENR 3.5, item 8.8.2**.
[^8]: **ICA 100-37, Art. 179**, and **AIP-Brasil, ENR 3.5, item 9.5.2.2**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.5.2.5**.
[^10]: **ICA 100-37, Art. 180**.
[^11]: **ICA 100-37, Art. 375**.
[^12]: **ICA 100-37, Art. 376**.
[^13]: **AIP-Brasil, ENR 3.5, item 7.5.1**.
[^14]: **AIP-Brasil, ENR 3.5, item 7.9**.
[^15]: **AIP-Brasil, ENR 3.5, item 8.8.1**.
[^16]: **AIP-Brasil, ENR 1.1, item 4.1.1, and ENR 1.8, item 2.4.1**.
[^17]: **AIP-Brasil, ENR 3.5, items 9.4.1.5 and 9.4.1.6**.
