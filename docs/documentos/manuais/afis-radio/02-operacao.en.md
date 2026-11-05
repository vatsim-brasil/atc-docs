---
title: Working the Frequency
icon: material/radio-handheld
---

--8<-- "includes/abreviacoes.md"

# Working the Frequency

## The rhythm of the frequency

At the tower, the controller leads: clears, instructs and waits for the readback. At the RADIO, the pilot leads. The pilot calls, says where they are and what they intend, and reports each phase. The RADIO answers with **roger**, adds what the pilot needs to know and requests the next report.

The MCA 100-16 examples for AFIS always follow the same pattern[^1]:

1. the pilot calls and identifies;
2. the RADIO answers with its own callsign;
3. the pilot gives position, level or altitude and intention, or requests information;
4. the RADIO gives **roger** and the aerodrome information, and requests a report;
5. the pilot reports each phase, and the RADIO acknowledges with roger, with traffic information when there is any.

## Aerodrome information

The RADIO's first answer to an arriving or departing aircraft is the aerodrome information. In the MCA 100-16 examples it includes, in roughly this order[^1]:

- **wind**, in degrees and knots, or "wind calm";
- **altimeter setting** (QNH);
- **temperature**;
- **aerodrome conditions**: "aerodrome under visual conditions" or "aerodrome under IFR conditions", with estimated ceiling and visibility when relevant;
- **aids out of service**, such as an NDB off the air;
- **obstacles and situations on the movement area**, such as machines beside the runway;
- **known traffic**, or "no traffic reported";
- **time check**, for those about to depart.

The RADIO does not assign the runway. It gives the wind and, if any, the runway other traffic is using. The choice is the pilot's, who states it in the reports ("downwind leg runway zero seven").

!!! note "Good practice"
    On the network, start with the aerodrome METAR. If there is no METAR, use the one from the nearest aerodrome and tell the pilot so. "Estimated" ceiling and visibility make sense in the real world, where the operator looks out of the window. On VATSIM, give what the METAR says.

## Traffic information

Traffic information is the most valuable thing the RADIO has, because the pilot will use it to separate themselves. It says **who** the traffic is, **where** it is and **what** it will do: "Known traffic is a Xingu on downwind leg runway zero five"[^1].

Give the information when it changes the pilot's decision: on the initial call, when new traffic joins the circuit or calls on the frequency, and when two aircraft will converge on final or on the runway. There is no separation to ensure, but there is situational awareness to build.

!!! example "Example"
    A Cessna is on downwind for runway 12 for touch-and-go. A Seneca calls 10 minutes out, for landing. The RADIO tells the Seneca about the Cessna on the initial call and, when the Seneca reports downwind, tells the Cessna there is traffic behind it. The two decide the spacing. The RADIO does not tell either of them "number two".

## VFR arrival

The pilot calls with position, level or altitude and intention. The RADIO gives the aerodrome information and requests a report on joining the circuit. From then on, each leg generates a report:

<div class="comms-pilot">Altamira Radio, PT KST, from Progresso, 10 minutes out, radial 225, FL 075.</div>
<div class="comms-atc">PT KST, Altamira Radio roger, wind calm, altimeter setting one zero one two, temperature 22 degrees, aerodrome under visual conditions, Altamira NDB out of service, no traffic reported. Report downwind leg.</div>
<div class="comms-pilot">PT KST roger, will report downwind leg runway zero seven.</div>

The following reports are downwind, base, final, on the ground and runway vacated. On final, the RADIO repeats the wind if there is no other traffic to report. On the ground, it may request the runway vacated report[^1].

The standard traffic circuit at an AFIS aerodrome has its own subsection in ICA 100-37[^2]. Altitudes, legs and joining are in the [Traffic Circuit Manual](../manual-circuito-trafego/index.md).

## VFR departure

The pilot calls when starting to taxi, with the runway and destination, and requests information. The RADIO gives the aerodrome information, with known traffic and time check, and requests a report at the holding point. The following reports are holding point, entering the runway, lined up and airborne[^1].

<div class="comms-pilot">PT EEA, commencing taxi runway zero five, destination Vitória, request information.</div>
<div class="comms-atc">PT EEA, Usiminas Radio roger. Wind two four zero degrees, zero two knots. Altimeter setting one zero two one. Observe machines on the left side of runway zero five. Known traffic is a Xingu on downwind leg runway zero five. Temperature two four. Time check 56. Report on holding point.</div>

Note what the pilot says at the holding point: "maintain position, waiting for Xingu landing". The pilot is the one who decides to wait. The RADIO only gave the information that made the decision possible.

After take-off, the pilot reports the level or altitude reached and the estimates. If the route enters controlled airspace, the RADIO gives the frequency of the next unit. MCA 100-16 gives the example of a departure entering the TMA: "entering Terminal, call Vitória Control one one nine decimal eight, if negative, Vitória Tower one one eight decimal one"[^1].

!!! tip "In practice"
    "Call" is not a transfer of control. The RADIO did not have control of the aircraft and has nothing to transfer. It only tells the pilot whom to call to enter controlled airspace, where a clearance will be needed.

## IFR arrival

ICA 100-37 has a section on instrument descent at an aerodrome provided with AFIS, with one subsection for flight in controlled airspace and another for flight outside it. The aerodrome "must have an IFR approach procedure in force" (Art. 140)[^2].

The common case is an IFR aircraft descending under the control of the center or approach down to the FIZ:

1. Still with the center, the pilot calls the RADIO and requests the aerodrome conditions. The RADIO gives the wind, the setting, the aerodrome condition (visual or IFR), the ceiling, the visibility, the temperature and the known traffic.
2. The pilot says they will call again when cleared by the center.
3. The pilot comes back to the RADIO giving the clearance received from the center and the level being passed.
4. The RADIO gives roger and requests the procedure reports: initial procedure altitude, outbound, base or procedure turn, final approach, MDA with the aerodrome in sight, on the ground and runway vacated[^1].

The descent and approach clearances belong to the **center** or **approach**. The RADIO does not repeat them as if they were its own. It follows the procedure and keeps the pilot informed about traffic, especially VFR traffic in the circuit.

## IFR departure

The IFR clearance is issued by the control unit with jurisdiction over the airspace ahead, never by the RADIO. When the clearance comes through the RADIO frequency, it is a relay (Art. 788, VII)[^2], and the RADIO says where it came from.

!!! note "Good practice"
    When relaying, start with the unit that issued the clearance and read it exactly as received: "PT ABC, Bauru Control clears...". The pilot reads back to the RADIO, and the RADIO confirms to the control unit that the clearance was delivered. If the pilot asks for a change, the RADIO does not negotiate: it takes the request to the unit that issued the clearance.

After take-off, the RADIO sends the pilot to the control unit at the point or altitude agreed with it. See [AFIS on the Network](03-rede.en.md#coordination-with-approach-and-the-center).

## Aircraft without radio

ICA 100-37 has a subsection on the operation of aircraft without radio equipment or with the radio inoperative at an AFIS aerodrome[^2]. On the network, the equivalent case is the pilot who operates **text only**, or who cannot transmit on voice.

!!! note "On the network"
    Reply by text, on the RADIO frequency, with the same information you would give on voice. For the other pilots, report the text-only aircraft as you would any other traffic: they may not be reading the text channel.

[^1]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16), Chapter IV, Section VI (Aerodrome Flight Information Service – AFIS), subsections on arriving traffic, departing traffic and traffic information. The callsigns and frequencies in the examples are those of the manual.
[^2]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Section V of the Flight Information Service chapter (AFIS) and the section on instrument descent at an aerodrome provided with AFIS. Edition in force on 27/11/2025.
