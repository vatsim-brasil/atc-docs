---
title: Operational Overview
icon: material/eye
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

## The position

`SBAO_FSS` represents the Atlântico ACC. The `_FSS` suffix identifies an oceanic position under the network convention and requires a minimum rating of **C1**[^1].

| Portion of the airspace         | Class | Service                                               |
| ------------------------------- | ----- | ----------------------------------------------------- |
| Above FL 245 (Atlântico UIR)    | `A`   | Air traffic control, flight information and alerting  |
| Below FL 145                    | `G`   | Flight information and alerting, no control           |

In practice, traffic is almost entirely long-haul IFR at cruising level, therefore in Class `A`, where all flights are separated from one another.

## What changes compared to a continental ACC

| Continental resource       | In the Atlântico FIR                                                     |
| -------------------------- | ------------------------------------------------------------------------ |
| Radar surveillance         | **Does not exist.** The FIR is not included in the published coverage[^2] |
| Direct VHF over the whole area | **Does not exist.** The unit's published frequencies are HF[^3]      |
| Voice as the primary means | **Reversed.** ADS-C and CPDLC are the primary means, HF is secondary[^4]  |
| Vectoring                  | **Not applicable.** CPDLC is not used for vectoring[^5]                   |
| 5 NM separation            | **Not applicable.** Minima are procedural, in minutes and tens of NM      |

The Atlântico FIR is expressly excepted from the two rules that apply in the other Brazilian FIRs: here CPDLC is not a means supplementary to voice, and it is used even without an ATS surveillance service[^6].

## The three questions

Everything the controller does answers one of these:

1. **Where is the aircraft?** ADS-C when available, position report when not. See [Communications](controle.en.md) and [Operational flow](fluxo.en.md).
2. **How do I talk to it?** CPDLC primary, voice secondary, SELCAL to recover whoever has gone quiet. See [Communications](controle.en.md).
3. **Is it separated?** Calculation based on estimates, levels and Mach number. See [Separation](separacao.en.md).

!!! danger "The error does not show itself"
    In radar airspace, a developing conflict becomes visible on the screen. Here, an outdated estimate produces a wrong mental picture that stays wrong until the next report. Keeping the record up to date is not bureaucracy, it is the surveillance tool.

## The session cycle

| Step                                     | Page                                                  |
| ---------------------------------------- | ----------------------------------------------------- |
| Check boundaries, sectors and frequencies | [Structure and sectorization](estrutura.en.md)       |
| Prepare, connect and open                | [Preparation and opening](abertura.en.md)             |
| Receive the aircraft and check the plan  | [Flight plan](plano-de-voo.en.md)                     |
| Establish communication                  | [Communications and surveillance](controle.en.md)     |
| Monitor and record progress              | [Operational flow](fluxo.en.md)                       |
| Separate, handle requests and deviations | [Separation, routes and deviations](separacao.en.md)  |
| Coordinate, transfer and handle failures | [Coordination and contingencies](coordenacao.en.md)   |

!!! tip "On the network (Vatbrz)"
    Few aircraft, each one for a long time. A Europe/Southeast Brazil flight occupies the position for more than two hours. Plan the session around duration, not volume, and state your expected logoff time in the *controller information*.

[^1]: **VATSIM, GCAP v2.0, item 6.3**.
[^2]: **AIP-Brasil, ENR 1.6, items 3 and 4**.
[^3]: **AIP-Brasil, ENR 2.1**.
[^4]: **AIP-Brasil, ENR 3.5, items 8.3.1 and 9.5.1.3**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.1.6**.
[^6]: **AIP-Brasil, ENR 3.5, items 9.1.3 and 9.1.5**.
