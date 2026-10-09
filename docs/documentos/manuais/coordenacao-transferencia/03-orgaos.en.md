---
title: Coordination between Units
icon: material/sitemap-outline
---

--8<-- "includes/abreviacoes.md"

# Coordination between Units

## How to read this page

Each pair of units exchanges different information, because each needs different things from the other. The tables below list what ICA 100-37 requires to be passed in each direction. On the network, much of this already arrives through the tag and the flight plan. Coordinate in the chat **what the tag does not show**: flight plan changes, delays, holds, missed approaches and restrictions.

## Between ACCs, and between sectors of an ACC

The flight plan information needed for coordination passes from one unit to the next **as the flight progresses**, sufficiently in advance for the accepting unit to analyse it[^1]. Between sectors of the same unit, exchange information on[^2]:

- every aircraft transferred from one position to another;
- aircraft operating **near the boundary** between sectors that may affect traffic in the neighbouring sector;
- aircraft whose control has been delegated to another position, and the others affected by that delegation.

When part of an area is so narrow that there is no time to control the traffic crossing it, the units may agree on a **direct transfer** between the two units at either end, informing the intermediate unit[^3].

> **ACC-CW:** "Estimate VRG 3256, Cuiabá to Guarulhos, FL 330, VARGA at 55."

## Between ACC and APP

### Who decides what

| The ACC | Source |
| --- | --- |
| Specifies the **take-off time**, when needed to coordinate the departure with its traffic or to separate aircraft on the same route. If it does not, the APP may do so | [^4] |
| Specifies the **clearance expiry time**, if a delayed departure could interfere with traffic. If the APP sets its own, it can never be later than the ACC's | [^4] |
| When weather conditions require an approach sequence, clears arrivals to **holding points**, with holding instructions and an expected approach time | [^4] |

### What the ACC tells the APP

| Information | Source |
| --- | --- |
| Identification, type and point of departure of arrivals | [^5] |
| Proposed level and estimated time over the holding fix, or the actual time if the aircraft is transferred after reaching the fix | [^5] |
| Expected approach time given to the aircraft | [^5] |
| That the aircraft has been cleared to contact the APP, or has been transferred, with time and conditions if necessary | [^5] |
| Expected delay to departures due to congestion | [^5] |

Arrival information is sent **at least 15 minutes before** the estimated time of arrival and revised whenever necessary[^6].

### What the APP tells the ACC

| Information | Source |
| --- | --- |
| Lowest level available at the holding point that can be made available to the ACC | [^7] |
| Average interval between successive approaches | [^7] |
| Revision of the expected approach time when the one calculated by the APP differs by **5 minutes** or more | [^7] |
| Time of arrival over the holding point when it differs by **3 minutes** or more from the calculated one | [^7] |
| IFR cancellations that affect the holding levels or expected approach times of other aircraft | [^7] |
| Take-off times from aerodromes without a TWR | [^7] |
| Delays and overdue aircraft | [^7] |
| **Missed approaches** | [^7] |

> **APP-SN:** "Lowest level available at STM VOR, FL 070."
>
> **ACC-BL:** "Roger, TAM 3235 descending to FL 070."

## Between APP and TWR

### Who decides what

| Rule | Source |
| --- | --- |
| The APP retains control of arrivals until they have been transferred and are in communication with the TWR | [^8] |
| After coordinating with the TWR, the APP may release arrivals to **visual holding points**, where they remain until further clearance from the TWR | [^9] |
| The APP may authorize the TWR to clear a take-off, provided the TWR observes separation from arrivals | [^10] |
| The TWR only relays a **special VFR** clearance after obtaining it from the APP | [^11] |

The third rule is the **departure release**. In a TMA with arrivals, the tower does not let an IFR flight take off without the APP knowing and agreeing, because the departure will enter the airspace where the arrivals are.

### What the TWR tells the APP

| Information | Source |
| --- | --- |
| Landing and take-off times | [^12] |
| That the first aircraft in the sequence is in communication with the TWR, in sight, and is likely to land | [^12] |
| Delays and overdue aircraft | [^12] |
| Aircraft that are essential traffic for the APP's aircraft | [^12] |

### What the APP tells the TWR

| Information | Source |
| --- | --- |
| Expected time and proposed level of arrival over the aerodrome, **at least 15 minutes before** landing, when flight time allows. For aerodromes less than 15 minutes' flight away, as early as possible | [^13] |
| That it has cleared the aircraft to contact the TWR and that the TWR will take over control | [^13] |
| Expected delays to take-offs due to congestion | [^13] |
| The arrival sequence and the instructions and restrictions given to the arrivals | [^14] |

> **APP-RF:** "PT ITU with landing priority, ambulance aircraft number 1 on approach, PT CTA number 2."
>
> **TWR-RF:** "Roger, PT ITU number 1, PT CTA number 2."

## Between TWR and ground

The transfer between tower and ground follows the points on the previous page: after vacating the runway, on arrival, and at the holding point, on departure. Agree between the two positions anything that differs, such as a runway crossing during taxi or an intermediate holding position. See [TWR and ground](02-transferencia.en.md#twr-and-ground).

[^1]: **ICA 100-37, Art. 824**. See [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 852**.
[^3]: **ICA 100-37, Art. 836**.
[^4]: **ICA 100-37, Art. 838, items II to VI and sole paragraph**.
[^5]: **ICA 100-37, Art. 842**.
[^6]: **ICA 100-37, Art. 843**.
[^7]: **ICA 100-37, Art. 841**.
[^8]: **ICA 100-37, Art. 844**.
[^9]: **ICA 100-37, Art. 845**.
[^10]: **ICA 100-37, Art. 846**.
[^11]: **ICA 100-37, Art. 847**.
[^12]: **ICA 100-37, Art. 850**.
[^13]: **ICA 100-37, Art. 851 and sole paragraph**.
[^14]: **ICA 100-37, Art. 996**.
