---
title: Communications and Surveillance
icon: material/satellite-uplink
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Here, communication and surveillance are the same subject: you know where the aircraft is because it told you, through the same means you use to reply. **Losing the means of communication means losing surveillance.**

## Hierarchy of means

| Order | Means  | Function                                                 |
| ----- | ------ | -------------------------------------------------------- |
| 1     | ADS-C  | Automatic position and route conformance                 |
| 2     | CPDLC  | Clearances, instructions and reports by text             |
| 3     | Voice  | Secondary means, and primary for those without datalink  |
| 4     | SELCAL | Selective calling to recover a silent aircraft           |

ADS-C and CPDLC are the **primary means** of the Atlântico ACC, with HF as secondary[^1].

## ADS-C

!!! danger "ADS-C is not radar"
    The data is **dependent** and **automatic**: it comes from the aircraft itself, with the accuracy of its own system, at discrete intervals. There is no independent return, no continuous update, no vectoring. Treating it as a radar screen leads to separation decisions that the data source cannot support.

Contracts established in the Atlântico FIR[^2]:

| Type          | Trigger                                                  |
| ------------- | -------------------------------------------------------- |
| **Periodic**  | Every 15 minutes                                         |
| **Event**     | Reporting points                                         |
| **Event**     | Lateral deviation of 5 NM                                |
| **Event**     | Altitude deviation of 200 ft                             |
| **Event**     | Vertical rate of plus or minus 2,000 ft per minute       |
| **Demand**    | Operational need                                         |

Event contracts are what turn ADS-C into a conformance tool: any route departure, level deviation or start of climb triggers a notification without you having to ask.

**Even under ADS-C, the pilot must send a CPDLC position message on entering the FIR**[^3]. Estimates only need to be updated if they change by more than 2 minutes[^4].

**If ADS-C fails**, the pilot is normally not alerted by the onboard equipment[^5]. On receiving the failure notification: inform the pilot, require reports by CPDLC or voice and re-establish the applicable minima[^6].

## CPDLC

### Logon

The published identifier is **`SBAO`**[^7]. Codes for the split sectors are in [Structure and sectorization](estrutura.en.md#posicoes-na-vatsim).

| Situation                         | Rule                                                                         |
| --------------------------------- | ---------------------------------------------------------------------------- |
| When to log on                    | **Between 10 and 25 minutes** before entering the FIR[^8]                    |
| Departing within the airspace     | Before take-off[^8]                                                          |
| Coming from a FIR with datalink   | Automatic transfer; the crew checks it when crossing the boundary[^9]        |
| Logon rejected                    | Callsign and registration must be identical to those in the flight plan[^10] |

### Rules of use

| Rule                                                                      | Source |
| ------------------------------------------------------------------------- | ------ |
| Whoever speaks by CPDLC gets a CPDLC reply; by voice, a voice reply       | [^11]  |
| Every dialogue must be closed                                             | [^11]  |
| **A voice clearance prevails over a CPDLC clearance**                     | [^12]  |
| Free text only when no standard message exists; avoid long messages       | [^13]  |
| CPDLC is not used for vectoring                                           | [^14]  |
| `MONITOR`: changes frequency **without** an initial call                  | [^15]  |
| `CONTACT`: changes frequency **and makes** an initial call                | [^15]  |

**If CPDLC fails**, revert to voice starting with `CPDLC FAILURE`, or `ALL STATIONS CPDLC FAILURE` if the failure is in the ground system. Pending messages are considered not delivered and dialogues start over[^16]. Full phraseology in [Phraseology and messages](fraseologia.en.md#cpdlc).

## Voice

On the network, voice takes place on the position's VHF channel, as per [Structure and sectorization](estrutura.en.md#posicoes-na-vatsim). The initial contact needs to establish three things:

1. **Identification**: aircraft and unit callsigns.
2. **Situation**: position, time, level and, if assigned, speed. The assigned speed is included in the initial call after any frequency change[^17].
3. **Capability**: whether there is an active datalink and whether there is SELCAL.

!!! info "Real world and simulation"
    This manual does **not** claim that VATSIM audio reproduces HF propagation, coverage or degradation. Treat the channel for what it is: a stable voice channel associated with the position.

## SELCAL

A four-letter code, mandatory in item 18 preceded by `SEL/`[^18]. Two practical rules:

1. **Do not perform a SELCAL check on the first contact of an aircraft on CPDLC**, unless you request it[^19].
2. **Use SELCAL to recover an aircraft that does not respond**, along with 121.5 MHz, company frequency, air-to-air frequency and other crews[^20].

!!! info "Real world and simulation"
    There is no onboard decoder on the network: the check is a radiotelephony convention. If the pilot does not recognize the procedure, do not insist; agree on a continuous listening watch on the frequency and carry on.

## When the primary means fails

**Separation cannot depend on a means that no longer exists.**

| Lost    | What to do                                                                          |
| ------- | ----------------------------------------------------------------------------------- |
| ADS-C   | Require reports by CPDLC or voice and re-establish the applicable minima[^6]        |
| CPDLC   | Revert to voice with `CPDLC FAILURE` and restart pending dialogues[^16]             |
| Voice   | Use CPDLC to maintain flight safety until it is restored[^21]                       |
| Both    | Apply the [contingencies](coordenacao.en.md#perda-completa-de-comunicacao) flow     |

[^1]: **AIP-Brasil, ENR 3.5, items 8.3.1 and 9.5.1.3**.
[^2]: **AIP-Brasil, ENR 3.5, item 9.5.2.3**.
[^3]: **AIP-Brasil, ENR 3.5, item 9.5.2.1**.
[^4]: **AIP-Brasil, ENR 3.5, item 9.5.2.5**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.1**.
[^6]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.2**.
[^7]: **AIP-Brasil, ENR 3.5, item 9.2.1**.
[^8]: **AIP-Brasil, ENR 3.5, item 9.2.2**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.2.3**.
[^10]: **AIP-Brasil, ENR 3.5, items 9.2.4 and 9.2.5**.
[^11]: **AIP-Brasil, ENR 3.5, item 9.4.1.3**.
[^12]: **AIP-Brasil, ENR 3.5, item 9.4.1.7**.
[^13]: **AIP-Brasil, ENR 3.5, items 9.4.1.1 and 9.4.1.2**.
[^14]: **AIP-Brasil, ENR 3.5, item 9.1.6**.
[^15]: **AIP-Brasil, ENR 3.5, items 9.4.1.5 and 9.4.1.6**.
[^16]: **AIP-Brasil, ENR 3.5, items 9.4.4.2 to 9.4.4.5**.
[^17]: **ICA 100-37, Art. 180**.
[^18]: **MCA 100-11, item 2.2.8.1.12**, and **AIP-Brasil, ENR 3.5, item 9.4.3.2**.
[^19]: **AIP-Brasil, ENR 3.5, item 9.5.1.2**.
[^20]: **ICA 100-37, Art. 268**.
[^21]: **AIP-Brasil, ENR 3.5, item 9.1.4**.
