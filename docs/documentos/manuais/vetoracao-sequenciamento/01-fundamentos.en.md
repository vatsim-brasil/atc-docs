---
title: Vectoring Fundamentals
icon: material/compass-outline
---

--8<-- "includes/abreviacoes.md"

![Vectoring and Sequencing Manual - Fundamentals](img/manual-vetoracao-fundamentos.png)

#

## Identify before vectoring

No vectoring starts without identification. Before providing the ATS surveillance service, the controller must **establish the identification** of the aircraft and **inform the pilot**. That identification must be maintained until the end of the service[^1]. If it is lost, the pilot must also be informed[^2].

The most common methods with secondary surveillance radar (SSR) and ADS-B are[^3]:

| Method | How to do it |
| --- | --- |
| Identification on the tag | The tag shows the aircraft's callsign, or a discrete code that has already been verified. |
| Code change | Assign a code to the pilot and watch the change on the screen. |
| `IDENT` activation | Request `IDENT` and watch the response. The function should only be activated at the controller's request. |
| Identification transfer | The previous controller hands over the aircraft already identified. |

A discrete code can only be used as the basis for identification **after it has been verified**: confirm that the code selected by the pilot is the one assigned[^4]. On the network, this means confirming that the tag is correlated with the right flight plan, not just that there is a tag on the screen.

When two targets are very close together or are making similar movements, use more than one method until any doubt is removed[^5].

### Informing the position

When you identify the aircraft, inform its position. The exceptions are identifications made by transfer, by the pilot's own position report, by a departure observed within 1 NM of the end of the runway, or by the Mode S, ADS-B or discrete code tag, when the position on the screen is consistent with the flight plan[^6]. The position may be given in relation to a well-known point, by bearing and distance from a navigation aid or fix, or as the distance from touchdown when the aircraft is on final[^7].

> **TAM 3501, radar contact, 40 miles South of Brasília, descend to FL 070, expect ILS Z approach runway 29L.**

While the ATS surveillance service is being provided, the pilot is **exempt from reporting position** at compulsory reporting points and only reports where ATC requests[^8].

## What vectoring is

Vectoring means giving the aircraft **headings and levels** instead of the route it would fly on its own. ICA 100-37 is direct about what this implies[^9]:

!!! danger "Under vectoring, navigation is yours"
    "Whenever an aircraft is under vectoring, the Air Traffic Control Service shall be provided and **the controller shall be responsible for the navigation of the aircraft**, transmitting to it the heading instructions and level changes that become necessary."

The most serious consequence concerns obstacle clearance. Outside vectoring, the Air Traffic Control Service does not include the prevention of collision with the ground, and the pilot must check that the clearance is safe in that respect. **Under vectoring, that check is no longer the pilot's**[^10]. A vectored pilot may not even know the exact position of the aircraft and therefore cannot verify the safe altitude. It is up to the controller to issue clearances that ensure obstacle clearance **at all times**, until the point where the pilot resumes own navigation[^11].

### When to vector

Vectoring serves six purposes[^12]:

1. to establish separation;
2. to guide the aircraft in carrying out special procedures;
3. to obtain an operational advantage for ATC or for the aircraft, such as a more efficient sequence or a shorter track;
4. to steer the aircraft around weather or wake turbulence;
5. to correct significant route deviations;
6. to meet a pilot's request, when possible.

Vectoring for its own sake is not one of them. Whenever the published route (SID, STAR, airway) solves the problem, prefer it. The workload is lower for both sides, and a communication failure does not leave the aircraft without a heading to fly.

## Minimum vectoring altitude

Since obstacle clearance becomes yours, every heading must come with a safe altitude **for the area the aircraft will overfly**. ICA 100-37 requires the controller to always have complete and up-to-date information on the minimum flight altitudes in the area, the lowest usable levels and the minimum altitudes of procedures based on vectoring[^13].

In TMAs that have the chart, this information is on the **ATCSMAC** (ATC Surveillance Minimum Altitude Chart), published by DECEA on AISWEB. It divides the TMA into sectors, each with its minimum vectoring altitude. Where there is no ATCSMAC, use the most conservative reference among the MSA on the IAC and the minimum altitudes on the en-route and area charts.

!!! warning "Below the MSA, only with the right chart"
    The MSA on the IAC is a **safe** altitude within 25 NM of the navigation aid. It is not the minimum vectoring altitude. Vectoring below the MSA is only safe with the ATCSMAC (or equivalent) at hand. Without it, keep the aircraft at or above the MSA until it is established on a published procedure.

When the pilot asks to deviate around weather below the published minimum safe altitude, responsibility for obstacle clearance **goes back to the pilot**. The phraseology makes this explicit: the controller informs the minimum altitude and approves the deviation[^14].

## Start, limits and termination

### Start

The start of vectoring is marked by the controller informing that the aircraft is **under vectoring**[^15]. If the first vector takes the aircraft off an established route, also inform **the purpose** of the vector. When the heading given could create a hazard if communication is lost, also specify **the limit** of the vector[^16].

> **TAM 3205, vectoring for ILS final approach runway 29L, turn left heading 240.**
>
> **TAM 3456, vectoring for sequencing, turn left heading 285, limit three minutes to resume own navigation direct NIMTO.**

### Methods

There are six ways to give a vector[^17]:

| Method | Example |
| --- | --- |
| Direction of turn and final heading | "turn right heading 070" |
| Heading to fly | "fly heading 150" |
| Maintain the current heading | "maintain present heading" |
| Direction and number of degrees, when the aircraft's heading is not known and there is no time to obtain it | "turn 30 degrees left" |
| Heading to leave a navigation aid the aircraft is over | "leave BUENO heading 240" |
| Start and stop of turn, when the aircraft's heading instruments are unreliable | "turn right... stop turn" |

With the number-of-degrees method, before the manoeuvres ask the pilot to make **all turns at rate one** and to comply with the instructions **immediately** on receipt[^17].

### Geographical limits

- Except during a transfer of control, **do not vector within 2.5 NM of the boundary** of your airspace. If the applicable separation minimum is greater than 5 NM, the minimum distance becomes **half of that separation**[^18].
- **Do not vector controlled flights outside controlled airspace**, except in an emergency, to avoid weather (informing the pilot) or at the pilot's request[^19].
- Whenever possible, vector along tracks on which the pilot can monitor their own position using navigation aids. This reduces the assistance needed and mitigates a possible failure of the surveillance system[^20].

### During vectoring

While the aircraft is under vectoring, you must[^21]:

1. assign an altitude to maintain, respecting all restrictions;
2. bring the aircraft back into controlled airspace compatible with its destination;
3. give a heading that intercepts the desired radial or track **at a distance that ensures the interception**;
4. give advance notice if, for any reason, the aircraft must leave radar coverage and the pilot has to resume navigation from a given point;
5. keep the pilot informed of the aircraft's position.

### Termination

When vectoring ends, instruct the pilot to **resume own navigation**. If the vectors have taken the aircraft away from the assigned route, also inform its position and give the necessary instructions[^22].

> **TAM 3702, 50 miles Southeast of Campo Grande VOR, resume own navigation, heading Urubupungá VOR.**

On approach, there is no need to inform the termination of the ATS surveillance service when the aircraft makes a **visual approach** or is vectored **to the final approach track**[^23]. Vectoring for an ILS ends when the aircraft intercepts the final approach course and the glide path[^24].

## Separation with ATS surveillance

### Minima

| Situation | Minimum | Source |
| --- | --- | --- |
| Horizontal separation with PSR, SSR, ADS-B or MLAT | **5 NM** | [^25] |
| Only en-route radar available in the TMA or CTR | **10 NM** | [^25] |
| Vertical separation applied by an APP | **1,000 ft** | [^26] |
| Aircraft holding over the same fix | **The radar minimum does not apply**: separate vertically | [^27] |

The distance is measured **between the centers of the targets**. Under no circumstances may the edges of the targets touch or overlap without vertical separation[^28]. Radar minima only apply between **identified** aircraft whose identification is likely to be maintained[^29]. A departure may be separated by radar from take-off, provided it is likely to be identified within 1 NM of the end of the runway[^30].

!!! info "Reduced minima"
    A reduction below 5 NM is only permitted in accordance with a specific DECEA publication[^31], and in the real world it exists only in designated areas. On the network, apply 5 NM unless the TMA's MOP authorizes another value.

### Levels on the screen

Based on pressure-altitude, an aircraft is considered to be[^32]:

| Situation | Criterion (outside RVSM airspace) |
| --- | --- |
| **Maintaining** the level | Within ±300 ft of the assigned level |
| **Vacating** the level | Has moved more than 300 ft in the expected direction |
| **Passing** a level when climbing or descending | Has gone more than 300 ft beyond it, in the expected direction |
| **Reaching** the cleared level | Has been within ±300 ft for three updates or 15 seconds, whichever is greater |

In RVSM airspace, the tolerance is ±200 ft. An aircraft may only be cleared to a level occupied by another **after the other has reported vacating it**. In severe turbulence, only after it has reported being at the new level[^33].

### Wake turbulence

In the approach and departure phases, and en route below FL 240, apply the wake turbulence minima **when they are greater than 5 NM**[^34]:

| Leading | Following | Minimum |
| --- | --- | --- |
| SUPER (`J`) | HEAVY (`H`) | **6 NM** |
| SUPER (`J`) | MEDIUM (`M`) | **7 NM** |
| SUPER (`J`) | LIGHT (`L`) | **8 NM** |
| HEAVY (`H`) | HEAVY (`H`) | **4 NM** |
| HEAVY (`H`) | MEDIUM (`M`) | **5 NM** |
| HEAVY (`H`) | LIGHT (`L`) | **6 NM** |
| MEDIUM (`M`) | LIGHT (`L`) | **5 NM** |

These minima apply when the following aircraft is flying behind the leading one, or crossing behind it, **at the same altitude or less than 1,000 ft below**, and when both use the same runway or parallel runways less than 760 m apart[^35]. The category of each type is in ICAO Doc 8643 and appears in the flight plan (`A320/M`, `B77W/H`, `A388/J`). SUPER and HEAVY aircraft must include "super" or "heavy" in the initial call[^36].

!!! tip "In practice"
    The minimum that applies is always **the greater** of the radar minimum and the wake turbulence minimum. A `B77W` followed by an `A320` on final calls for 5 NM for wake turbulence. This matches the radar minimum, and even so there is no margin for compression. An `A320` followed by a `C172` calls for 5 NM for wake turbulence, and a `B77W` followed by a `C172`, 6 NM.

[^1]: **ICA 100-37, Art. 906**. See [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 907**.
[^3]: **ICA 100-37, Arts. 909 and 910**.
[^4]: **ICA 100-37, Art. 911**.
[^5]: **ICA 100-37, Art. 914**.
[^6]: **ICA 100-37, Art. 917, item I**.
[^7]: **ICA 100-37, Art. 918**.
[^8]: **ICA 100-37, Art. 920**.
[^9]: **ICA 100-37, Art. 921**.
[^10]: **ICA 100-37, Art. 93, sole paragraph**.
[^11]: **ICA 100-37, Art. 922 and its § 2°**.
[^12]: **ICA 100-37, Art. 924**.
[^13]: **ICA 100-37, Art. 934**.
[^14]: **MCA 100-16, Art. 117**. See [MCA 100-16](https://publicacoes.decea.mil.br/publicacao/MCA-100-16).
[^15]: **ICA 100-37, Art. 923**.
[^16]: **ICA 100-37, Art. 927**.
[^17]: **ICA 100-37, Art. 925 and sole paragraph**.
[^18]: **ICA 100-37, Art. 928**.
[^19]: **ICA 100-37, Art. 929**.
[^20]: **ICA 100-37, Art. 926**.
[^21]: **ICA 100-37, Art. 930**.
[^22]: **ICA 100-37, Art. 933**.
[^23]: **ICA 100-37, Art. 940**.
[^24]: **ICA 100-37, Art. 1008**.
[^25]: **ICA 100-37, Art. 953 and its § 2°**.
[^26]: **ICA 100-37, Art. 432**.
[^27]: **ICA 100-37, Art. 952**.
[^28]: **ICA 100-37, Arts. 948 and 949**.
[^29]: **ICA 100-37, Art. 946**.
[^30]: **ICA 100-37, Art. 951**.
[^31]: **ICA 100-37, Art. 954**.
[^32]: **ICA 100-37, Arts. 897 to 901**.
[^33]: **ICA 100-37, Art. 433**.
[^34]: **ICA 100-37, Arts. 956 and 959, Table 11**.
[^35]: **ICA 100-37, Art. 960**.
[^36]: **ICA 100-37, Arts. 206 and 208**.
