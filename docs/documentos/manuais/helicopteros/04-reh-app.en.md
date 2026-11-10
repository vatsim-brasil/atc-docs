---
title: Approach and REH
icon: material/map-marker-path
---

--8<-- "includes/abreviacoes.md"

# Approach and REH

## What an REH is

In terminal areas with a lot of helicopter traffic, DECEA publishes **Helicopter Special Routes (REH)**. The ICA 100-4 says they may be set up "according to the volume and complexity of air traffic, [...] to organise helicopter traffic within a CTR/TMA" (item 5.4.1)[^1].

The VFR circulation AICs describe an REH as a VFR route shaped like a corridor, based on visual references on the ground (highways, rivers, bridges, stadiums), laid out so as not to interfere with IFR procedures or with local traffic at the main aerodromes. The corridor is usually **1 NM wide**, half on each side of the centreline[^2]. An REH is not the same as an REA, the Aircraft Special Route, which serves aeroplanes and helicopters and is 3 NM wide. A helicopter may use an REA if it meets that route's requirements[^2].

## Where REH are published

Each terminal area with REH has:

- a VFR circulation **AIC**, with the general rules, the description of each route and the coordinates of the points;
- the **CCV REH** charts (Visual Corridor Charts), with the route drawings;
- any procedures in the **AIP** and in the aerodromes' **VAC**.

On the portal, each terminal area's REH are on the [terminal](../../../MOP/terminais/index.en.md) page: the REH map layer and the "Visual navigation documents" box, with links to the AICs and charts. Before opening an APP with REH, open that page.

## Helicopter rules on an REH

The rules below apply on any REH. The values for each route (altitudes, points, frequencies) are in the terminal area's publication.

| Rule | Source |
| --- | --- |
| With an REH in place, the helicopter flies, in principle, inside it, at the levels or altitudes set for its direction of flight | ICA 100-4, item 5.4.2[^1] |
| The helicopter keeps the route's reference points **on its right**, unless the AIP says otherwise | ICA 100-4, item 5.4.3[^1] |
| VFR flight, in continuous visual contact with the ground | VFR circulation AIC[^2] |
| The REH minimum altitudes do not relieve the pilot of keeping clear of obstacles | VFR circulation AIC[^2] |
| Without visual conditions, the pilot turns back, lands elsewhere or asks ATC for clearance to continue, including changing to IFR | VFR circulation AIC[^2] |
| The helicopter does not cross a runway centreline or IFR paths without an ATC clearance | VFR circulation AIC[^2] |

Some REH are **compulsory**: the helicopter leaves them only in an emergency or with an ATS clearance. Others are **recommended**, usually in class G, and entering controlled airspace still requires a clearance[^2].

## Control or information?

The airspace class of each REH segment is in the publication, and may differ from the class of the surrounding terminal area[^2]. That class tells you what APP provides:

| Segment class | What APP does |
| --- | --- |
| **C or D** (controlled) | Clears the entry, controls the helicopter and provides the separation and traffic information of that class |
| **G** (uncontrolled) | No control and no ATS surveillance service. The helicopter talks on the published coordination frequency and only gets flight information and alerting, if it asks |

What each class gives a VFR flight is in the [Airspace and ATS Services Manual](../espaco-aereo-servicos-ats/index.md). What matters here is not to "control" a helicopter in class G: there, it decides on its own.

## APP tasks

### Before opening the position

- Know which REH run through your terminal area, where they cross the finals and IFR departures, and at which points the helicopter moves from your frequency to a tower's.
- Know the altitudes by direction of flight. They are what separates two helicopters flying opposite ways.

### Identification and transponder

The AICs for terminal areas with REH usually make the transponder mandatory throughout the area, including class G, and set a code for helicopters flying between places without an ATS unit[^2]. When the helicopter enters controlled airspace, give it its own code and identify it like any other traffic.

### The standard report

To keep the frequency clear, the AICs ask for a short first call, with the addressee, registration, route, position, altitude and direction of travel[^2]. A typical report is:

> "Control, PR-HEL, helicopter route ALFA, overhead the BRIDGE, 1,500 feet, northbound."

If the pilot calls with less than that, ask for what is missing before clearing them.

### Entry and crossing

A helicopter entering controlled airspace along an REH needs a clearance. The clearance gives the route, altitude and next reporting point. Where the REH crosses a final or an IFR departure path, the helicopter needs a clearance to cross.

!!! note "Good practice"
    If the final is busy, have the helicopter hold over the last visual point before the crossing, and clear the crossing right after the landing or take-off. It is quicker than taking it off the route.

### Traffic information

Two helicopters flying opposite ways on the same REH are at different altitudes and each on the right of the centreline. Even so, tell each about the other. Also tell a helicopter passing close to a final about the traffic on it, and a VFR aeroplane crossing an REH about the helicopters on it.

### Coordination with the tower

An REH that enters a CTR or ATZ moves to the tower frequency at a defined point. Coordinate with the tower before transferring, as you would for any VFR arrival. The transfer is at the published point, not in the middle of the corridor.

## On the network

APP is an **S3** position under the GCAP, with a maximum range of 150 NM[^3]. With the tower and ground offline, APP covers both under the top-down principle (GCAP 4.6)[^3], including helicopter landings and take-offs at the terminal area's aerodromes.

Many helicopter pilots on the network do not know the REH. Some practical rules:

- if the pilot does not have the chart, point them to the terminal page on the portal, which shows the REH on the map;
- if they cannot follow the REH, clear a direct route to a visual point, away from finals and IFR departures, at an altitude that does not conflict with them;
- in class G with no controller online, the published coordination frequency becomes the network traffic frequency: the Code of Conduct requires the designated frequency or, where there is none, 122.800 (item B5)[^4].

!!! warning "Overload"
    The GCAP lets an overloaded controller reduce the service, for example by withdrawing top-down cover from an aerodrome (item 4.6(d))[^3]. It does not allow ignoring helicopters already on the frequency. Vatsim Brasil policy cites "refusing service to traffic present" as conduct that harms the division's reputation[^5].

[^1]: [**ICA 100-4, Special Air Traffic Rules and Procedures for Helicopters**](https://publicacoes.decea.mil.br/publicacao/ica-100-4): item 5.4 (REH). Portaria DECEA nº 109/DGCEA, of 21/07/2021.
[^2]: VFR circulation AICs for terminal areas with REH, such as [**AIC N 29/26**](https://publicacoes.decea.mil.br/publicacao/aic-n-2926) (items 2.1, 3 and 4): definitions of REH, REA, compulsory and recommended routes, airspace classes, transponder and radio calls. Each terminal area's values are in its own AIC.
[^3]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), version 2.0, of 15/08/2026: items 4.6 and 4.6(d). Maximum ranges: [**Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item C8.
[^4]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item B5.
[^5]: [**Vatsim Brasil, Division Policy**](https://vatsim.com.br/documentos), item 3.6.
