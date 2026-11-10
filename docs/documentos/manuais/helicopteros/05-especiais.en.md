---
title: Special Operations
icon: material/shield-star-outline
---

--8<-- "includes/abreviacoes.md"

# Special Operations

Two specialities come up often among the network's helicopters: **offshore** operations, supporting oil platforms, and **public safety and air ambulance** operations. This page shows what the rules say about each and what VATSIM allows.

## Offshore operations

### In the real world

**Offshore airspace** is the airspace set aside for operations supporting oil exploration in the oil basins. It starts **12 NM** from the coast and runs to the lateral limits of the FIR. Each basin's class and procedures are in a dedicated publication (ICA 100-4, items 1.3 and 6.2)[^1].

The general criteria, valid for every basin, are in the ICA 100-4 (chapter 6)[^1]:

| Rule | Item |
| --- | --- |
| A full flight plan is mandatory between the mainland and the platforms | 6.1.1 |
| The landing message at the platform is mandatory. Without an ATS unit, the platform radio operator sends it | 6.1.2 and 6.1.3 |
| The helicopter stays in contact with the responsible ATS unit at all times | 6.1.4 |
| At night, platforms are used only to evacuate the sick or seriously injured, or in an emergency threatening the environment, the platform, people or shipping | 6.3 |
| The altimeter setting is the pilot's responsibility | 6.4 |
| Over the sea, only within coverage of a certified aid or with RNAV | 6.5 |
| Mode A/C transponder mandatory. In some basins, ADS-B as well | 6.6 |
| Flow measures are preferably applied on the ground, before take-off | 6.7 |

An IFR flight to a platform needs an IFR-certified helideck. If the platform's helideck is not IFR, the flight plan may show the departure aerodrome itself as destination, with "RMK/LDG (platform name), CASO VFR" in item 18. On the way back, the alternate must be on the mainland (item 6.8)[^1].

### What the controller does

For the mainland controller, an offshore flight is an ordinary flight until it leaves the terminal area:

- **GND and TWR:** treat the departure like any helicopter's. Check that the flight plan is filed and that the destination is a platform or the aerodrome itself, with the platform in item 18.
- **APP and centre:** follow the helicopter to the edge of their airspace. Beyond 12 NM it enters offshore airspace, and the service depends on the class published for the basin.
- **On the way back:** the helicopter arrives as a flight from the sea, along the route or point the basin's publication provides. Sequence it with the coastal aerodrome's traffic.

### On the network

VATSIM's rules say nothing about oil platforms. Since the network uses the rules and procedures of the place being simulated[^2], the ICA 100-4 applies, with two practical adaptations:

- **There is no platform radio operator.** The landing message becomes the pilot's report: ask them to report the landing before leaving the frequency, or to sign off when they reach the platform.
- **There is no offshore unit in the package.** Beyond APP's range, the helicopter goes to the centre, if online. With nobody online, the pilot uses the network traffic frequency, 122.800 (Code of Conduct item B5)[^2].

The Special Operations Policy covers ships and platforms with their own ATC, but only for special operations organisations, and requires an agreement with the division[^3]. A civil helicopter flying to a platform does not need that.

## Public safety and air ambulance

### In the real world

Brazilian rules give these flights **priority**. The ICA 100-37 take-off sequence is (Art. 601)[^4]:

1. aircraft on an air defence mission;
2. aircraft on a military operation (war or internal security mission);
3. aircraft carrying, or about to carry, a seriously ill or injured person, a vital organ or radiopharmaceuticals;
4. aircraft on a SAR operation or engaged in public safety operations;
5. aircraft carrying the President of the Republic;
6. aircraft on a military exercise;
7. all other aircraft.

On arrival the order changes little: gliders first, then air ambulance, then SAR and public safety (Art. 608)[^4]. Public safety aircraft are those defined by ANAC in RBAC 90, and the priority applies **only** while they are engaged in a public safety operation (Art. 3, XXXI, and sole paragraph of Art. 601)[^4]. A police helicopter on a positioning flight has no priority.

The ICA 100-4 also lets these helicopters use **occasional landing areas**, always in VMC and in two-way radio contact with the ATC unit, if the flight is under control (item 2.4.6)[^1].

### On the network

This is where the real world and VATSIM differ most.

**Police, public safety, SAR and firefighting** are restricted operations. The Code of Conduct says military, paramilitary or civilian government agency operations "must be authorized and conducted by an approved Virtual Special Operations Association (VSOA)" (item A13(b))[^2]. The list of restricted activities includes search and rescue and firefighting, fixed or rotary wing[^3]. A pilot who does not belong to a VSOA may not simulate a police operation or a search and rescue.

**Routine air ambulance** flights are not on the list. The Special Operations Policy only restricts medical flights in disasters and humanitarian operations, from ships, after a SAR operation, and to airports that accept relief flights only[^3]. A patient transfer between hospitals can be flown by any pilot.

**Nobody can demand priority.** The Code of Conduct says no flight may declare itself to have priority over another, and that pilots may declare an emergency only when under ATC, ending it immediately if the controller asks (item B6)[^2]. It also forbids simulating a hijack, including with code 7500, and recreating real disasters (items B6 and A17)[^2].

What this means for the controller:

| Situation | What to do |
| --- | --- |
| VSOA flight, with the organisation's website in the flight plan remarks | Legitimate. Handle it as a special operation and accommodate it whenever you can[^3] |
| "Police" helicopter without a VSOA | Handle it as an ordinary civil helicopter. Do not apply public safety priority |
| Routine air ambulance | Handle it normally. The Art. 601 priority may be given at the controller's discretion, workload permitting. The pilot cannot demand it |
| Emergency declared | Handle it as an emergency. If it disrupts operations, ask the pilot to end it |
| Pilot insists on a restricted operation | Explain the rule politely. If they carry on, call a network supervisor |

!!! note "Recognising a VSOA flight"
    The Special Operations Policy requires VSOA flights to put the organisation's website in the flight plan remarks, precisely so that ATC and VATSIM can identify them (item 8.5)[^3]. Without it, treat the flight as civil.

[^1]: [**ICA 100-4, Special Air Traffic Rules and Procedures for Helicopters**](https://publicacoes.decea.mil.br/publicacao/ica-100-4): item 1.3 (definitions), item 2.4.6 (occasional landing area) and chapter 6 (offshore). Portaria DECEA nº 109/DGCEA, of 21/07/2021.
[^2]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct): Purpose (local rules), items A13(b), A17, B5 and B6. Revision 2026.2.
[^3]: [**VATSIM, Special Operations Policy**](https://cdn.vatsim.net/policy-documents/VATSIM-POL-Special_Operations_v5.0.pdf), version 5.0, of 14/05/2026: items 4 (definitions), 6 (restricted activities), 8.5 (flight plan identification), 9.3 (ATC accommodation) and 10 (ships and platforms).
[^4]: [**ICA 100-37, Air Traffic Services**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Art. 3, XXXI, and Arts. 601 and 608 (priorities). Edition with the 2nd amendment (Portaria DECEA/DNOR1 nº 2.197, of 18/08/2026), in force on 26/11/2026.
