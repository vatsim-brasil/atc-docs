---
title: AFIS on the Network
icon: material/access-point-network
---

--8<-- "includes/abreviacoes.md"

# AFIS on the Network

## The RADIO position

At Vatsim Brasil, AFIS is provided by positions with the suffix **`_R_TWR`**, such as `SBBU_R_TWR` (Bauru Radio) and `SBTT_R_TWR` (Tabatinga Radio). The `_R_` marks the RADIO and is a Vatsim Brasil convention. The `_TWR` is just the connection type: the VATSIM Code of Conduct lists the suffixes accepted on the network, and none of them is for AFIS[^1].

Three practical consequences:

- **Rating:** under the GCAP table, `_TWR` positions require the **S2** rating (Aerodrome Controller)[^2]. Opening a RADIO requires the same rating as a tower.
- **Approved positions:** only approved positions and frequencies may be opened (Code of Conduct item C6)[^1]. Use the callsign and frequency from the aerodrome page in the MOP.
- **Range:** the maximum range of a tower position is 50 NM (item C8)[^1]. That is more than the 27 NM radius of AFIS with no published FIZ.

!!! note "Do not confuse"
    The Brazilian RADIO is neither of the two similarly named GCAP positions. The **Flight Service Station** (`_FSS`) provides en-route information and advisory service and requires C1[^2]. The **Radio Operator** (`_RDO`) works alongside a controller, receiving position reports and relaying that controller's instructions, and is only online with that associated controller[^2]. The aerodrome RADIO provides AFIS on its own.

## Where the RADIOS are

The pages of AFIS aerodromes are in the `afis` folder of each FIR, in the [Aerodromes](../../../MOP/aerodromos/index.en.md) section, tagged **Não-Controlado**. The "ATC Units" table on each page gives the position, the abbreviation, the callsign and the frequency. The table note says when AFIS is provided by another unit, as in Bauru, where AFIS is provided by Bauru APP (`SBWU_APP`) on the same frequency.

The [terminal area](../../../MOP/terminais/index.en.md) pages list the aerodromes of each TMA and, in the top-down coverage diagram, show which position each RADIO falls back on.

## Real-world hours

In the real world, many units change with the time of day: the tower that becomes AFIS overnight, the approach that closes and leaves a FIZ in place of the TMA, the RADIO that only operates on weekdays. The MOP pages record this as "In the real world".

On the network, the position in the sector package applies, at any time. If the aerodrome has a tower in the package, it is a tower. If it has a RADIO, it is a RADIO.

## Top-down coverage

The GCAP establishes that VATSIM positions cover the airspace and positions below them when those are not staffed. This is the top-down principle. It applies to positions providing control service, and the division may extend it to other positions (GCAP 4.6 and 4.6(a))[^2]. At Vatsim Brasil, RADIOS are part of the coverage: in each TMA's diagram, the `_R_TWR` sits below the APP, and the APP sits below the center.

With the RADIO disconnected, the position above provides the Flight Information Service in the FIZ[^3]. The arrangement has a real-world parallel: at an uncontrolled aerodrome where an APP is based, the APP itself provides AFIS (Art. 784 of ICA 100-37)[^4]. This has an effect that catches many people out:

!!! warning "Top-down does not turn the FIZ into controlled airspace"
    The approach or center covering an AFIS aerodrome provides **information** within the FIZ, not control. There is no landing or take-off clearance to give. The controller above uses RADIO phraseology at the aerodrome, with their own callsign, and resumes control when the aircraft enters controlled airspace.

With no one connected, either directly or top-down, pilots use the network traffic frequency. The Code of Conduct requires monitoring the designated frequency in airspace with no controller, and using 122.800 where there is no specific frequency[^1].

!!! note "Real world and network"
    In the real world, outside AFIS hours the pilot uses the unit's own frequency as the air-to-air coordination frequency (FCA), and at an aerodrome with no ATS unit uses the FCA from the AIP or, if there is none, 123.45 MHz (Arts. 147 and 148 of ICA 100-37)[^4]. On VATSIM the Code of Conduct applies: the network traffic frequency is 122.800.

## Opening and closing the position

When you open the RADIO, someone was probably covering the aerodrome top-down. Tell the approach or center, ask about traffic already in the FIZ or arriving, and only then start answering calls.

When closing, do the reverse: tell whoever will cover, and tell the pilots on the frequency whom they will talk to from then on. If no one will cover, say that the aerodrome is left without an ATS unit and that the traffic frequency becomes the network one.

These steps follow the same pattern as the handover between any positions, covered in the [Coordination and Transfer Manual](../coordenacao-transferencia/04-rede.en.md).

## Coordination with approach and the center

The RADIO neither receives nor transfers control, because there is no control to transfer. A flight departing an AFIS aerodrome enters the control chain at the unit with jurisdiction over the airspace ahead, not at the tower. What the RADIO coordinates with that unit is information:

| Situation | What the RADIO coordinates |
| --- | --- |
| IFR about to depart | Requests the clearance from the control unit, relays it to the pilot and reports the departure |
| IFR about to arrive | Receives notice from the control unit and gives local traffic that may conflict with the approach |
| VFR leaving the FIZ into controlled airspace | Gives the pilot the frequency of the next unit. No coordination needed, because the pilot will request the clearance |
| Aircraft did not report on the ground, or did not call the next unit | Notifies the surrounding unit, as it would for the Alerting Service |

!!! note "Good practice"
    If the approach or center prefers to talk directly to the IFR about to depart, agree on this when opening the position and tell the pilot on which frequency to get the clearance. What must not happen is the pilot receiving two different clearances, one from each frequency.

## ATIS

The Code of Conduct only allows voice ATIS at aerodromes that have ATIS in the real world, always with a text version in English (item C7(a))[^1]. Some AFIS aerodromes have ATIS in the package, such as `SBBU_ATIS`. If the aerodrome has ATIS, the aerodrome information may quote the information letter, but known traffic is still given on the frequency.

[^1]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), items B5, C4, C6, C7(a) and C8.
[^2]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), version 2.0, of 15/08/2026: items 4.5(e), 4.5(j), 4.6, 6.3 and 6.6.
[^3]: Page of the [São Paulo TMA](../../../MOP/terminais/sbcw-curitiba/SBXP.en.md), in the Terminal Areas section: "With the FIZ position disconnected, `SBXP_APP` (or the position covering it) provides the flight information service in it."
[^4]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Chapter III, Section XXI. Edition in force on 27/11/2025.
