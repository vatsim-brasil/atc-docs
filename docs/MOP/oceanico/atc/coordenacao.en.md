---
title: Coordination and Contingencies
icon: material/swap-horizontal
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

In procedural airspace, coordination carries more weight than in radar airspace, because the accepting unit has no way of checking on its own what it has received.

## Coordination format

Always use the same sequence. It covers what is required[^1] and fits on one line.

```text
CALLSIGN | POINT | ESTIMATE | LEVEL | MACH | ROUTE | CAPABILITIES | COMMS
```

!!! example "Example"
    **Outbound:** *"EXEMPLO 123, KOSAX at 1448, flight level 370, Mach decimal 82, route direct TEBRO, RVSM and RNP 10, ADS-C and CPDLC active, SELCAL AB-CD."*

    **Acceptance:** *"EXEMPLO 123 accepted at flight level 370."*

    **Renegotiation:** *"EXEMPLO 123 unable flight level 370 due traffic. Available flight level 350 or estimate KOSAX 1500."*

## When to coordinate

Whenever something already passed to the adjacent unit changes:

| Trigger                            | What to pass                                      |
| ---------------------------------- | ------------------------------------------------- |
| Revised estimate                   | New estimate and reason                           |
| Level change                       | New level and point at which it will be level     |
| Mach change                        | New Mach and its effect on the estimate           |
| Route changed                      | New route, new exit point, new estimates          |
| Weather deviation                  | Side, extent, duration and revised estimate       |
| Emergency                          | Nature, intentions and assistance required        |
| Communication failure              | Last contact, last confirmed position, level and Mach |
| Conflicting traffic                | Identification, position, level and track         |
| Position change on the network     | Who takes over, from when, and each traffic       |

An aircraft must not enter another unit's airspace without coordination having been completed[^2].

## Between FIR positions

When the FIR is operating split, the positions exchange flight plan and control information on everything being transferred and on everything operating near the internal boundary[^3]. Treat the internal boundary as a FIR boundary.

- **When opening** a split: the incoming controller receives the complete list of traffic passing into their area.
- **When closing**: the outgoing controller hands over the same list and confirms that the other position has received each one.

## Contingencies

### The sequence, always the same

**Identify → Confirm → Protect separation → Establish an alternative means → Coordinate → Record → Normalize or transfer.**

Protecting separation comes **before** re-establishing communication. It does not depend on it.

### Action table

| Situation                        | Immediate action                                                              | Effect on separation                         |
| -------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------- |
| **Loss of CPDLC**                | Revert to voice with `CPDLC FAILURE`; pending dialogues start over[^4]        | Datalink-dependent minima no longer apply    |
| **Loss of ADS-C**                | Inform the pilot (their equipment does not warn them) and require reports[^5] | Re-establish minima without ADS-C            |
| **Voice failure**                | Try secondary frequencies and 121.5 MHz[^6]; use CPDLC in the interim[^7]     | Increase separation with those affected      |
| **SELCAL failure**               | Agree on a continuous listening watch on the frequency and carry on           | None: it is a calling aid                    |
| **Total loss of communication**  | Exhaust 121.5 MHz, SELCAL, company frequency, air-to-air 123.45 MHz and other crews[^6] [^8] | See below                  |
| **Navigation degradation**       | Increase the frequency of reports                                             | Another type or minimum; RNAV no longer applies[^9] |
| **Cannot maintain level or Mach** | Find out what it can maintain and for how long                               | Vertical goes back to 2,000 ft; Mach no longer reduces[^10] |
| **Urgent weather deviation**     | Pass conflicting traffic, offer a free level, then deal with the lateral part | See [Separation](separacao.en.md#desvios)    |
| **Declared emergency**           | Confirm intentions, clear levels and route, give every assistance[^11]        | Emergency separation if necessary[^12]       |
| **No declared capabilities**     | Confirm what it can actually do and require a report at every point           | Larger minima: 2,000 ft, 100 NM, no Mach reduction |
| **Pilot disconnects**            | Record the time and last position; notify whoever was expecting it            | Release the protected airspace               |
| **Controller reconnects**        | Do not assume the previous picture: rebuild it and ask everyone for a report  | Reconfirm pending coordinations              |
| **Overload**                     | Split, or coordinate greater spacing on handover                              | **Never improvise smaller minima**           |
| **Adjacent leaves without coordinating** | Take over up to the jurisdiction limit and treat each exit as an offline unit | Resolve conflicts inside the FIR      |
| **Conflict detected late**       | **Go vertical first**, pass traffic to both, then speed or route              | Emergency if nothing else works[^12]         |

### Complete loss of communication { #perda-completa-de-comunicacao }

In addition to the table above:

1. **Treat the aircraft as possibly being at any point** between its last confirmed position and its projected one, and keep all other traffic clear of that band and level.
2. Instruct other aircraft to attempt contact on the air-to-air frequency **123.45 MHz**, designated for flights in remote and oceanic areas out of range of VHF stations[^8].
3. Inform all adjacent units and the next unit along the route.

!!! warning "Emergency phases"
    The **Uncertainty Phase (INCERFA)** begins 30 minutes after the time communication was expected, or after the first unsuccessful attempt, whichever comes first[^13]. It drops to 15 minutes for flights of up to 1 hour[^14]. **ALERFA** and **DETRESFA** follow if attempts continue to be unsuccessful[^15].

### Emergency with ADS-C

An equipped aircraft may activate the ADS-C emergency mode. On receiving the report, **acknowledge it by the most appropriate means** and give every possible assistance[^11].

[^1]: **ICA 100-37, Arts. 814, 818 and 824**.
[^2]: **ICA 100-37, Art. 822**.
[^3]: **ICA 100-37, Art. 852**.
[^4]: **AIP-Brasil, ENR 3.5, items 9.4.4.2 to 9.4.4.5**.
[^5]: **AIP-Brasil, ENR 3.5, items 9.5.2.6.1 and 9.5.2.6.2**.
[^6]: **ICA 100-37, Arts. 267 and 268**.
[^7]: **AIP-Brasil, ENR 3.5, item 9.1.4**.
[^8]: **AIP-Brasil, ENR 1.1, item 4.1.1**.
[^9]: **ICA 100-37, Arts. 337 and 382**.
[^10]: **AIP-Brasil, ENR 2.2, items 1.6 and 1.13**.
[^11]: **ICA 100-37, Arts. 1088 to 1090**.
[^12]: **ICA 100-37, Arts. 270 and 271**.
[^13]: **ICA 100-37, Art. 804**.
[^14]: **ICA 100-37, Art. 805**.
[^15]: **ICA 100-37, Arts. 807 and 808**.
