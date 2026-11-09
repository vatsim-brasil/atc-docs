---
title: AFIS Fundamentals
icon: material/information-outline
---

--8<-- "includes/abreviacoes.md"

# AFIS Fundamentals

## What AFIS is

ICA 100-37 defines the Aerodrome Flight Information Service, AFIS, as "a service whose purpose is to provide the information that ensures the efficient conduct of air traffic at aerodromes that do not have an ATC unit or whose ATC unit is outside its operating hours" (Art. 782)[^1].

It is normally provided by an ATS unit identified as **"RADIO"**, located at the aerodrome or remotely (Art. 783). That unit "provides the Flight Information Service and, additionally, the Alerting Service to all traffic operating on the movement area of the aerodrome and to all aircraft in flight in Class G airspace in its vicinity" (Art. 783, sole paragraph)[^1].

These are two services, and neither of them is control:

- **Flight information:** the information the pilot needs to operate at the aerodrome. The wind, the altimeter setting, the runway others are using, the known traffic and the aerodrome conditions.
- **Alerting:** notifying the appropriate units when an aircraft needs search and rescue, and assisting those units.

## Where AFIS is provided

AFIS is normally provided within a **Flight Information Zone (FIZ)**, published in AIP-Brasil, with a configuration defined by the characteristics and needs of the location (Art. 786)[^1]. Where no FIZ is published, the service is provided, in addition to the movement area, to all aircraft in flight in Class G below FL 145 and within a radius of 27 NM (50 km) of the aerodrome (Art. 787)[^1].

The FIZ are in ENR 2.2 of the AIP[^2]. All of them are **Class G**, but they vary widely in size:

| FIZ | Lateral limits | Vertical limits | Callsign |
| --- | --- | --- | --- |
| Araraquara | polygon | GND – 5000 FT | Araraquara Radio |
| Bacacheri | polygon | GND – 4500 FT | Bacacheri Radio |
| Caxias do Sul | polygon | GND – 5500 FT | Caxias Radio |
| Gavião Peixoto | polygon with 27 NM arcs | GND – 5500 FT | Gavião Radio |
| Noronha | 27 NM circle | GND – FL 145 | Noronha Radio |

Source: AIP-Brasil, ENR 2.2, amendment of 01/10/2026[^2].

A FIZ may lie **underneath a TMA**. In that case, flight within the FIZ is Class G, but above its ceiling the TMA's controlled airspace begins. The RADIO only provides service up to the ceiling of the FIZ.

## Who provides AFIS

The normal case is a RADIO at the aerodrome, but ICA 100-37 itself provides for other arrangements. At an uncontrolled aerodrome where an APP is based, AFIS is provided by that APP (Art. 784). An APP may also provide AFIS at another aerodrome, provided the aerodrome lies in a CTR under its jurisdiction, the DECEA Regional Organisation agrees, one controller is responsible for the AFIS of a single aerodrome, and a risk assessment shows the operation is feasible (Art. 785)[^1]. MCA 100-16 sums it up: the units that provide AFIS are **RDO, APP or TWR** (Art. 153)[^3].

The AIP shows all these arrangements:

| Arrangement | Example in the AIP | What changes |
| --- | --- | --- |
| RADIO at the aerodrome | Caxias do Sul FIZ, "RÁDIO CAXIAS" | Nothing: this is the case described in this manual |
| Remote RADIO (R-AFIS) | Noronha FIZ, "RÁDIO NORONHA", marked R-AFIS | The operator is somewhere else. For the pilot, the radiotelephony is the same |
| APP providing AFIS | Bacacheri FIZ, provided by Curitiba APP, with the callsign "RÁDIO BACACHERI" | The same unit provides control in the TMA and information in the FIZ |
| TWR providing AFIS | Maringá FIZ, "AFIS MARINGÁ", provided by the tower | The tower becomes AFIS outside its hours |

Source: AIP-Brasil, ENR 2.2[^2].

The arrangement does not change the service. If approach or the tower provides AFIS in a FIZ, they provide **information**, not control, while the aircraft is in the FIZ.

!!! note "On the network"
    At Vatsim Brasil, all these arrangements become the same thing: a `_R_TWR` position with a RADIO callsign, or approach covering the aerodrome top-down. Real-world hours do not apply. See [AFIS on the Network](03-rede.en.md).

## What the RADIO reports

Art. 788 of ICA 100-37 lists the basic items of information the AFIS unit provides to aircraft[^1]:

1. **Meteorological information** for landing and take-off, including SIGMET: surface wind and its significant variations, altimeter setting (QNH) rounded down to the nearest whole hectopascal, air temperature, visibility or RVR when below 10 km, significant weather in the take-off and approach sectors and, for IFR, the amount and base height of the lowest cloud layer.
2. **Information for the pilot to choose the runway**, besides the wind: the runway and traffic circuit used by other aircraft and, on the pilot's request, the runway length or the distance from an intersection to its end.
3. **Known aircraft, vehicles or persons** on or near the manoeuvring area, and aircraft operating nearby that may constitute a hazard.
4. **Aerodrome conditions**: works, irregular or damaged parts of the runways, water on the runway, parked aircraft, other temporary hazards such as birds, and lighting failures.
5. **Changes in the operational status of visual and non-visual aids**, when not included in the publications.
6. **VHF-DF information**, when the unit has the equipment.
7. **Messages, including clearances, received from other ATS units** for relay to the aircraft.
8. **Other information** that may contribute to safety.

ICA 100-37 points out the limit of what the RADIO knows: the AFIS unit "only disseminates known information, sometimes reported by the pilots themselves who are operating at or near the location" (Art. 786, § 2)[^1].

## What the RADIO does not provide

ICA 100-37 is direct: in the FIZ "there is no provision of Air Traffic Control Service and, therefore, air traffic control clearances should not be expected" (Art. 786, § 1)[^1].

| The RADIO does | The RADIO does not |
| --- | --- |
| Gives the wind, altimeter setting, temperature and aerodrome conditions | Clear landing, take-off, touch-and-go, go-around or taxi |
| Gives the runway and circuit other traffic is using | Choose the pilot's runway |
| Gives known traffic: type, position, altitude and intention | Separate traffic or sequence arrivals |
| Requests reports: downwind, final, on the ground, runway vacated | Give headings, levels or speeds |
| Relays clearances from another unit, saying who issued them | Issue its own clearance |
| Activates the Alerting Service | Transfer control: there is no control to transfer |

The item that causes the most confusion is the relay (Art. 788, VII). The only clearance that goes through the RADIO frequency is one from **another** unit, and the RADIO makes clear where it came from. In the MCA 100-16 examples, the RADIO says "cleared by the Center" before the clearance (Art. 158)[^3].

!!! danger "Roger, not cleared"
    The RADIO's answer to a report is **roger**. "Cleared to land" or "cleared for take-off" on the RADIO frequency are errors: they give the pilot a clearance that no one has the authority to issue. If the pilot asks for clearance, the RADIO gives the conditions and the known traffic, and the decision stays with the pilot.

## The pilot's responsibility

In the FIZ, the pilot decides. ICA 100-37 gives the pilot clear obligations:

- **Listening watch:** anyone operating in airspace where AFIS is provided keeps a listening watch on the unit's frequency (Art. 145)[^1].
- **Reports:** on approach, landing, ground movement and departure, the pilot reports to the RADIO the IFR procedure to be flown and the phases and altitudes reached, the chosen runway before entering the circuit or starting to taxi, critical positions while taxiing and in the circuit, landing and take-off times and, on base leg or IFR final approach, the landing gear down and locked (Art. 791)[^1].
- **Choice of runway:** the pilot is expected to use the runway most used by other traffic. The pilot has "final authority and responsibility for the safe operation of the aircraft" and may choose another runway, provided they report the intention to the RADIO before entering the circuit or starting to taxi (Art. 158)[^1].
- **Coordination between pilots:** the pilot stays alert to other VFR and IFR traffic, reports their intentions to the RADIO and coordinates their manoeuvres with other traffic where needed (Art. 152)[^1].

This also applies to IFR. Outside controlled airspace, an IFR aircraft receives no separation. The AIP makes this explicit for the Sorocaba FIZ, where the SDCO IFR procedure lies entirely in Class G: aircraft flying it "must provide their own separation" from other aircraft in the FIZ[^2].

## The Alerting Service

The Alerting Service is provided to every aircraft receiving Air Traffic Control Service, that has filed a Flight Plan and had its departure notified to an ATS unit, or that is known or suspected to be subject to unlawful interference (Art. 795)[^1]. The responsibility for starting the service in an emergency lies with the "TWR, APP or RDO (radio) that becomes aware of an emergency in VFR or IFR flight", which immediately notifies the corresponding ACC and ARCC (Art. 797)[^1].

For the RADIO, this means following each aircraft to the end: an aircraft that reported on final and did not report on the ground, or that took off and did not call the next unit, is a case for the Alerting Service.

!!! note "On the network"
    There is no ARCC on VATSIM. The practical equivalent is to ask the pilot, check whether they are still connected, and tell the approach or center that has jurisdiction around the aerodrome. Emergencies on the network follow the Code of Conduct: the pilot only declares an emergency under control, and ends the emergency if the controller asks[^4].

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Chapter III, Sections XX and XXI (Arts. 140 to 164); Chapter VIII, Section V (AFIS, Arts. 782 to 791); Chapter IX (Alerting Service). Edition in force on 27/11/2025.
[^2]: [**AIP-Brasil, ENR 2.2**](https://aisweb.decea.mil.br/?i=publicacoes&p=aip): FIZ table, amendment of 01/10/2026.
[^3]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): Section VI, Aerodrome Flight Information Service – AFIS (Arts. 153 to 158). Edition approved by Portaria DECEA/DNOR1 n° 1.716, of 28/04/2025.
[^4]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item B6.
