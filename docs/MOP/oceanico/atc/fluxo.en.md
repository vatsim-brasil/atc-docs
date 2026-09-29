---
title: Operational Flow and Reports
icon: material/airplane
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

What happens to an aircraft from entry to transfer, and how to keep the record that replaces the radar screen.

## Entry by transfer

This is the normal case: the previous unit is online and coordinates the handoff.

### What the coordination must include

| Element                | What for                              |
| ---------------------- | ------------------------------------- |
| Identification         | Basis of the record                   |
| Entry point            | Where it crosses the boundary         |
| **Estimate over the point** | Basis of the separation calculation |
| Level                  | Vertical separation                   |
| **Mach number**        | Mach number technique                 |
| Route after entry      | Following points and adjacent unit at exit |
| Capabilities           | RVSM, RNP 10, ADS-C, CPDLC and SELCAL |
| Communication means    | How the aircraft is being worked      |

### Flow

1. **Check** each element of the table above.
2. **Analyse the flight plan** as described in [Flight plan and capabilities](plano-de-voo.en.md).
3. **Look for conflicts** with aircraft already in the FIR, **before** accepting.
4. **Accept or renegotiate.** Being unable to accept under the proposed conditions is normal: ask for another level, another Mach or another time over the entry point[^1].
5. **Confirm the datalink.** Coming from a FIR with datalink, the connection transfers by itself; if it did not, the pilot logs on again to `SBAO`[^2].
6. **Establish communication** and confirm identification, position, time, level and Mach.
7. **Open the record** with the estimate for the next point.

!!! warning "Do not accept without complete coordination"
    An aircraft must not enter another unit's airspace without completed coordination[^3]. Whoever crosses the boundary without it is, for a few minutes, nobody's responsibility.

## Entry without ATC online { #entrada-sem-atc-online }

The most frequent case on the network: the aircraft has flown for hours without any unit connected and there is no record.

1. **Identify** it by callsign and filed flight plan.
2. **Assume nothing** from the flight plan.
3. **Ask for a complete position report.**
4. **Confirm** the route, level and Mach it is actually flying.
5. **Confirm the capabilities** and request the logon, if applicable.
6. **Assess conflicts** now with real data.
7. **Establish the service**: identify the unit, confirm the level and Mach to maintain and define the next reporting point.

!!! tip "On the network (Vatbrz)"
    When opening the position, do this with **all** aircraft already inside the FIR, one by one, before issuing any clearance.

## Position reports { #reportes-de-posicao }

The report is what replaces the screen. Composing and transmitting it is the pilot's responsibility[^4].

### Format

```text
CALLSIGN, POSITION, TIME, LEVEL, MACH, NEXT POSITION and ESTIMATE, ENSUING POSITION
```

The six normative elements are identification, position, time, level (including the level being crossed and the cleared level, if different), next position with time, and the ensuing significant point[^5]. **The Mach number is always included whenever one has been assigned**[^6].

!!! example "Example"
    Fictitious callsign and fixes.

    *"Atlantico Center, EXEMPLO 123, position NIMAX at 1412, flight level 370, Mach decimal 82, estimating KOSAX at 1448, next TEBRO."*

    Record: `NIMAX` at `1412`, FL 370, Mach 0.82, `KOSAX` at `1448`, then `TEBRO`. The `1448` estimate becomes the basis for separation with anyone else crossing `KOSAX`.

### When it is required

| Situation                                                                    |
| ---------------------------------------------------------------------------- |
| Over compulsory reporting points, or as soon as possible after passing them[^7] |
| When crossing the lateral limits of the FIR[^7]                             |
| When requested by the ATS unit[^7]                                          |
| On routes without compulsory points: after the first 30 minutes, then every hour[^7] |
| On entering the FIR, via CPDLC, even with ADS-C[^8]                         |
| In the AORRA, every 10° of longitude[^9]                                    |

### When it is waived

With ADS-C active and working, voice reports are not required unless requested[^10]. **The waiver holds only while the data keeps arriving:** the moment ADS-C fails, reports are required again and it is up to you to tell the pilot[^11].

!!! info "Wind and temperature are not part of it"
    They appear in the meteorological block of an ADS-C report and in a Special AIREP, not in the routine position report. Do not ask for them.

### Estimates

A **revision of more than 2 minutes** requires action[^12]. When you receive one, immediately recalculate every pair that depended on the previous estimate.

!!! example "Example"
    `EXEMPLO 123` had reported `KOSAX` at `1448` and now reports `1455`. That is 7 minutes. If another aircraft was planned over `KOSAX` at `1500` with 10 minutes of separation, the minimum has been compromised and requires immediate action.

### Report that did not arrive

Control must **not** be based on the assumption that the estimate was met. Take immediate action to obtain the report if there is any bearing on another aircraft[^13].

1. Note the time at which the report was expected.
2. Call the aircraft; with no answer, try SELCAL and the other means.
3. **Treat the aircraft as possibly being anywhere** between the last confirmed report and the projected position, and keep other traffic clear of that band.
4. Request an on-demand ADS-C contract or a CPDLC message.
5. Tell the adjacent unit that the estimate is uncertain.

## Progress record

Keep, for each aircraft:

- [ ] last reported point, with exact time;
- [ ] current level and cleared level, if different;
- [ ] assigned Mach number;
- [ ] next point and current estimate;
- [ ] ensuing point;
- [ ] communication means and confirmed capabilities.

!!! tip "On the network (Vatbrz)"
    Use the tag fields and lists of the profile distributed in the sector package. What is on the screen survives a reconnection; what is on paper does not.

## Leaving the FIR

1. **Calculate the estimate** for the transfer point and revise it when the picture changes.
2. **Coordinate** early enough for the adjacent unit to analyse it[^14].
3. **Wait for acceptance**, adjusting before the boundary if it indicates other conditions[^1].
4. **Instruct the aircraft** with `CONTACT` or `MONITOR`, as appropriate[^15].
5. **Handle the datalink**: automatic transfer if the next unit also uses it, otherwise terminate the connection[^2].
6. **Close the record** with the time over the transfer point.

### When the next unit is not online { #quando-o-proximo-orgao-nao-esta-online }

1. Tell the pilot that there is no ATS unit connected ahead.
2. Instruct them to try to contact the following unit at least 5 minutes before the estimate over the fix, transmitting identification, origin, destination, route, level, transponder code, RVSM status and estimate[^16].
3. Record the last position, level and Mach.
4. **End the service explicitly.** The pilot needs to know they no longer have a responsible unit.

[^1]: **ICA 100-37, Art. 825**.
[^2]: **AIP-Brasil, ENR 3.5, item 9.2.3**.
[^3]: **ICA 100-37, Art. 822**.
[^4]: **ICA 100-37, Arts. 171 and 172**.
[^5]: **ICA 100-37, Art. 178**.
[^6]: **ICA 100-37, Art. 180**.
[^7]: **ICA 100-37, Art. 173**.
[^8]: **AIP-Brasil, ENR 3.5, item 9.5.2.1**.
[^9]: **AIP-Brasil, ENR 3.5, item 8.8.2**.
[^10]: **ICA 100-37, Art. 179**, and **AIP-Brasil, ENR 3.5, item 9.5.2.2**.
[^11]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.2**.
[^12]: **AIP-Brasil, ENR 3.5, item 9.5.2.5**.
[^13]: **ICA 100-37, Art. 174**.
[^14]: **ICA 100-37, Art. 824**.
[^15]: **AIP-Brasil, ENR 3.5, items 9.4.1.5 and 9.4.1.6**.
[^16]: **AIP-Brasil, ENR 1.8, item 2.3.3.1.2**.
