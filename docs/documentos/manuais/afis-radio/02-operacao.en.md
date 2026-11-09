---
title: Working the Frequency
icon: material/radio-handheld
---

--8<-- "includes/abreviacoes.md"

# Working the Frequency

## The rhythm of the frequency

At the tower, the controller leads: clears, instructs and waits for the readback. At the RADIO, the pilot leads. The pilot calls, says where they are and what they intend, and reports each phase. The RADIO answers with **roger**, adds what the pilot needs to know and requests the next report.

The MCA 100-16 examples for AFIS always follow the same pattern (Arts. 153 to 158)[^1]:

1. the pilot calls and identifies;
2. the RADIO answers with its own callsign;
3. the pilot gives origin, position, level and intention, or requests information;
4. the RADIO gives **roger** and the aerodrome information, and asks for intentions or a report;
5. the pilot reports each phase, and the RADIO acknowledges with roger, with traffic information when there is any.

## Aerodrome information

The RADIO's first answer to an arriving or departing aircraft is the aerodrome information. The items are in Art. 788 of ICA 100-37, detailed in [AFIS Fundamentals](01-fundamentos.en.md#what-the-radio-reports)[^2]. In the MCA 100-16 examples, it comes in roughly this order[^1]:

- **wind**, in degrees and knots, or "wind calm";
- **runway used by other aircraft**, when applicable;
- **altimeter setting** (QNH);
- **temperature**;
- **aerodrome conditions**: "aerodrome under visual conditions", "aerodrome under IMC" or "aerodrome below visual minima", with estimated ceiling and visibility when relevant;
- **aids out of service**, such as an NDB off the air, and obstacles on the movement area, such as machines beside the runway;
- **known traffic**, or "no reported traffic";
- **time check**, for those about to depart;
- and, for arrivals, **"advise intentions"**.

The RADIO does not assign the runway. It gives the runway and circuit other traffic is using. The pilot is expected to use that runway, but may choose another, provided they say so before entering the circuit or starting to taxi (Art. 158 of ICA 100-37)[^2].

!!! note "Good practice"
    On the network, start with the aerodrome METAR. If there is no METAR, use the one from the nearest aerodrome and tell the pilot so. "Estimated" ceiling and visibility make sense in the real world, where the operator looks out of the window. On VATSIM, give what the METAR says.

## Traffic information

Traffic information is the most valuable thing the RADIO has, because the pilot will use it to separate themselves. It says **who** the traffic is, **what** it is, **where** it is and **what** it will do. MCA 100-16 gives this example, for an arrival with two traffics (Art. 154)[^1]:

<div class="comms-atc">PT KST, Altamira Radio roger, wind calm, QNH 1012, temperature 22 degrees, aerodrome under visual conditions, CAVOK, traffic PT KLC on base leg runway 07 for touch and go, C172. Additional traffic PT-RPT, from Belém, 5 minutes out, northeast bound, crossing the field to join downwind leg runway 07, EMB110, passed flight level 050 descending to 1.000 feet. Advise intentions.</div>
<div class="comms-pilot">PT KST, roger, will join early downwind leg runway 07 for landing.</div>

Give the information when it changes the pilot's decision: on the initial call, when new traffic joins the circuit or calls on the frequency, and when two aircraft will converge on final or on the runway. The MCA 100-16 examples mark this point with "[traffic information]" after the roger, in the base leg and final reports (Arts. 154 and 155)[^1].

ICA 100-37 gives the pilot the rules to resolve the conflict: the aircraft on final approach normally has priority over the one in the circuit (Art. 159)[^2]. MCA 100-16 also shows traffic with priority, such as an aeromedical flight or an organ transport, and the pilot who, once informed, gives way (Art. 158, III)[^1].

!!! example "Example"
    A Cessna is on downwind for runway 12 for touch-and-go. A Seneca calls 10 minutes out, for landing. The RADIO tells the Seneca about the Cessna on the initial call and, when the Seneca reports downwind, tells the Cessna there is traffic behind it. The two decide the spacing. The RADIO does not tell either of them "number two".

## VFR arrival

The pilot calls with origin, position, level and intention. The RADIO gives the aerodrome information and asks for intentions. From then on, each leg generates a report (Art. 154 of MCA 100-16)[^1]:

<div class="comms-pilot">PT KST, from Progresso, 10 minutes out, radial 225, FL 075.</div>
<div class="comms-atc">PT KST, Altamira Radio roger, wind calm, runway 07 is being used by other aircraft, altimeter setting or QNH 1012, temperature 22 degrees, aerodrome under visual conditions, estimated ceiling 1.500 feet, visibility 5.000 meters due smoke, Altamira NDB out of service. Advise intentions.</div>
<div class="comms-pilot">PT KST, roger, will report downwind leg runway 07.</div>

The following reports are downwind, base, final and on the ground with runway vacated. On base leg, the pilot also reports the landing gear down and locked, as Art. 791 of ICA 100-37 requires[^2].

**Joining the circuit.** The preferred join is via the upwind leg sector (Art. 154 of ICA 100-37). At an AFIS aerodrome, since two-way communication is mandatory, the pilot may also join aligned with the start of the downwind leg, at the midpoint of the downwind leg at 45°, or aligned with the base leg, after making sure with the RADIO that there will be no conflict (Art. 163). With no other traffic and a crew familiar with the aerodrome, VFR may join straight in on final, and IFR may fly a straight-in approach (Art. 164)[^2]. MCA 100-16 has an example of a join via long final (Art. 155)[^1].

The circuit altitudes and layout are in the [Traffic Circuit Manual](../manual-circuito-trafego/index.md).

## VFR departure

The pilot calls when starting to taxi, with the runway and destination, and requests information. The RADIO gives the aerodrome information, with known traffic and time check, and requests a report at the holding point. The following reports are holding point, entering the runway, lined up and airborne (Art. 156 of MCA 100-16)[^1].

<div class="comms-pilot">PT EEA, commencing taxi runway 05 destination Vitoria, request information.</div>
<div class="comms-atc">PT EEA, Usiminas Radio roger. Wind 240 degrees, 2 knots. Altimeter setting 1021. Observe machines on the left side of runway 05. Traffic known PS-RET, is a Xingu on downwind leg runway 05 and AZUL 4218, coming from Belo Horizonte, an ATR72, passed level 060 descending for the RNP Y runway 23 procedure, 08 minutes to start the procedure. Temperature 24. Time check 56. Report holding point.</div>

Note what the pilot says at the holding point: "maintain position, waiting for Xingu landing". The pilot is the one who decides to wait. The RADIO only gave the information that made the decision possible.

After take-off, the pilot reports the level reached and the estimates. If the route enters controlled airspace, the RADIO gives the frequency of the next unit: "entering Terminal, contact Vitória Control 119,8, if negative, Vitoria Tower 118,1"[^1].

!!! tip "In practice"
    "Contact" is not a transfer of control. The RADIO did not have control of the aircraft and has nothing to transfer. It only tells the pilot whom to call to enter controlled airspace, where a clearance will be needed.

## IFR arrival

ICA 100-37 has a section on instrument descent at an aerodrome provided with AFIS, which "must have an IFR approach procedure in force" (Art. 140)[^2]:

- **In controlled airspace**, the aircraft obtains from the ATC unit clearance to descend to the minimum level of controlled airspace, proceeds to the procedure and transmits on the RADIO frequency the levels or altitudes and the procedure phases as it reaches them (Art. 141).
- **Outside controlled airspace**, there is no clearance to obtain: the aircraft determines the minimum descent level using the criteria of Art. 142, flies the procedure and transmits the same information on the RADIO frequency (Art. 142)[^2].

MCA 100-16 gives two situations, both with the aircraft descending under Amazônico Center (Art. 153)[^1]:

1. Still with the center, the pilot calls the RADIO and requests the aerodrome conditions. The RADIO gives the wind, the runway used by other aircraft, the setting, the aerodrome condition, the visibility, the ceiling and the temperature.
2. The pilot states the procedure to be flown, and the RADIO asks them to report when cleared by the center.
3. The pilot comes back to the RADIO: "cleared by Center, passing FL 120 IMC". The RADIO gives roger and the altimeter setting.
4. The RADIO requests the procedure reports. On a conventional procedure: initial altitude, outbound, base or procedure turn, final approach and MDA with the aerodrome in sight. On an RNAV procedure: each fix (CZ009, CZ011, CZ012). On final, the pilot reports the gear down and locked.
5. The RADIO gives the wind and requests the on the ground and runway vacated reports.

The descent clearance belongs to the **center** or **approach**. The RADIO does not repeat it as if it were its own. It follows the procedure and keeps the pilot informed about traffic, especially VFR traffic in the circuit. The MCA 100-16 example does this for an IFR aircraft on an RNP procedure: "IFR operation, lowest layer at 600 feet, PT KLN traffic is a Cessna 182, departed 2 minutes ago climbing to FL 060, radial 337, report starting procedure" (Art. 158)[^1].

## IFR departure

The IFR clearance is issued by the control unit with jurisdiction over the airspace ahead, never by the RADIO. When the clearance comes through the RADIO frequency, it is a relay (Art. 788, VII, of ICA 100-37)[^2], and the RADIO says where it came from: "after passing FL 040, cleared by the Center to climb en route, report passing FL 040 to the Amazônico Center, frequency 123,95" (Art. 158 of MCA 100-16)[^1].

In the MCA 100-16 IFR departure example (Art. 157)[^1], the pilot calls when starting to taxi, stating the departure to be flown ("I will execute SID RNAV AGIL 1A"). The RADIO gives the aerodrome information with a time check, requests the holding point, lined up and airborne reports, and then the report passing the first fix of the departure. Only then does it send the pilot to the center: "contact now Amazônico Center 124,55, if negative, 134,15".

!!! note "Good practice"
    When relaying, read the clearance exactly as received, starting with who issued it. The pilot reads back to the RADIO, and the RADIO confirms to the control unit that the clearance was delivered. If the pilot asks for a change, the RADIO does not negotiate: it takes the request to the unit that issued the clearance.

See also [Coordination with approach and the center](03-rede.en.md#coordination-with-approach-and-the-center).

## Aerodrome below minima

The RADIO does not close the aerodrome. It gives the conditions, and the decision is the pilot's. In the MCA 100-16 example, the RADIO reports "aerodrome below visual minima, estimated visibility 2.000 meters, ceiling 600 feet, advise intentions", the pilot decides to proceed to the alternate, and the RADIO requests a report "5 minutes out of Aeroxingu" (Art. 158, II)[^1].

## Aircraft without radio

ICA 100-37 prohibits the operation of aircraft without radio, or with the radio inoperative, at AFIS aerodromes. The exceptions are ferry flights, agricultural flights, and gliders and aircraft of flying clubs and training centres based at the aerodrome, always with prior coordination and at times that do not disrupt traffic (Art. 789)[^2].

!!! note "On the network"
    The equivalent case on VATSIM is the pilot who operates **text only**. Reply by text, on the RADIO frequency, with the same information you would give on voice. For the other pilots, report the text-only aircraft as you would any other traffic: they may not be reading the text channel.

[^1]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): Section VI, Aerodrome Flight Information Service – AFIS (Arts. 153 to 158). Edition as amended by Portaria DECEA/DNOR1 nº 2.193, of 11/08/2026, in force on 26/11/2026. The callsigns and frequencies in the examples are those of the manual.
[^2]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Chapter III, Sections XX and XXI (Arts. 140 to 164), and Chapter VIII, Section V (Arts. 782 to 791). Edition with the 2nd amendment (Portaria DECEA/DNOR1 nº 2.197, of 18/08/2026), in force on 26/11/2026.
