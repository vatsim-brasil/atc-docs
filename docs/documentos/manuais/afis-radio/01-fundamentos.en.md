---
title: AFIS Fundamentals
icon: material/information-outline
---

--8<-- "includes/abreviacoes.md"

# AFIS Fundamentals

## What AFIS is

The Aerodrome Flight Information Service, AFIS, is the Flight Information Service provided at the aerodrome itself. ICA 100-37 says it is normally provided by an ATS unit identified as **"RADIO"** (Art. 783) and defines what that unit provides: "the Flight Information Service and, additionally, the Alerting Service to all traffic operating on the movement area of the aerodrome and to all aircraft in flight in Class G airspace in its vicinity" (Art. 783, sole paragraph)[^1].

These are two services, and neither of them is control:

- **Flight information:** advice and information useful for the safe and efficient conduct of the flight. The wind, the altimeter setting, the aerodrome conditions, aids out of service and known traffic.
- **Alerting:** notifying the appropriate units when an aircraft needs search and rescue, and assisting those units.

## Where AFIS is provided

AFIS is normally provided within a **Flight Information Zone (FIZ)**, published in AIP-Brasil (Art. 786)[^1]. Where no FIZ is published, Art. 787 extends the service to the movement area and to all aircraft in flight in Class G below FL 145, within a radius of 27 NM (50 km) of the aerodrome[^1].

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

The normal case is a RADIO at the aerodrome. The AIP shows other arrangements, and all of them appear on the network:

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

## What the RADIO does not provide

ICA 100-37 is direct: within the FIZ "there is no provision of Air Traffic Control Service and, therefore, air traffic control clearances should not be expected" (Art. 786, § 1)[^1].

| The RADIO does | The RADIO does not |
| --- | --- |
| Gives the wind, altimeter setting, temperature and aerodrome conditions | Clear landing, take-off, touch-and-go, go-around or taxi |
| Gives the runway other traffic is using | Choose the pilot's runway |
| Gives known traffic: type, position, altitude and intention | Separate traffic or sequence arrivals |
| Requests reports: downwind, final, on the ground, runway vacated | Give headings, levels or speeds |
| Relays clearances from another unit, saying who issued them | Issue its own clearance |
| Activates the Alerting Service | Transfer control: there is no control to transfer |

The item that causes the most confusion is the relay. Among the basic items of information the RADIO transmits are "messages, including clearances, received from other ATS units for relay to the aircraft" (Art. 788, VII)[^1]. The only clearance that goes through the RADIO frequency is one from **another** unit, and the RADIO makes clear where it came from.

!!! danger "Roger, not cleared"
    The RADIO's answer to a report is **roger**. "Cleared to land" or "cleared for take-off" on the RADIO frequency are errors: they give the pilot a clearance that no one has the authority to issue. If the pilot asks for clearance, the RADIO gives the conditions and the known traffic, and the decision stays with the pilot.

## The pilot's responsibility

In the FIZ, collision avoidance is the pilot's job. ICA 100-37 dedicates an AFIS subsection to the responsibility of the pilot-in-command during approach, landing, take-off and ground movement (Art. 791)[^1]. The RADIO helps with information, but does not take on separation.

This also applies to IFR. Outside controlled airspace, an IFR aircraft receives no separation. The AIP makes this explicit for the Sorocaba FIZ, where the SDCO IFR procedure lies entirely in Class G: aircraft flying it "must provide their own separation" from other aircraft in the FIZ[^2].

## The Alerting Service

The Alerting Service is provided when the aircraft is receiving Air Traffic Control Service, when it has filed a Flight Plan and its departure has been notified to an ATS unit, or when it is known or suspected to be subject to unlawful interference (Art. 795)[^1]. The responsibility for starting the service in an emergency lies with the "TWR, APP or RDO (radio) that becomes aware of an emergency in VFR or IFR flight", which immediately notifies the corresponding ACC and ARCC (Art. 797)[^1].

For the RADIO, this means following each aircraft to the end: an aircraft that reported on final and did not report on the ground, or that took off and did not call the next unit, is a case for the Alerting Service.

!!! note "On the network"
    There is no ARCC on VATSIM. The practical equivalent is to ask the pilot, check whether they are still connected, and tell the approach or center that has jurisdiction around the aerodrome. Emergencies on the network follow the Code of Conduct: the pilot only declares an emergency under control, and ends the emergency if the controller asks[^3].

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Section V of the Flight Information Service chapter (AFIS) and the Alerting Service chapter. Edition in force on 27/11/2025.
[^2]: [**AIP-Brasil, ENR 2.2**](https://aisweb.decea.mil.br/?i=publicacoes&p=aip): FIZ table, amendment of 01/10/2026.
[^3]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item B6.
