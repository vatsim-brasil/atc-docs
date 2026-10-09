---
title: Transfer of Control
icon: material/transfer-right
---

--8<-- "includes/abreviacoes.md"

# Transfer of Control

## With ATS surveillance

Where ATS surveillance is available, transfer of control must be carried out whenever the aircraft passes from one unit or sector to another that also provides it, **so that the service is not interrupted**[^1]. ICA 100-37 provides two ways of doing this.

### Transfer without prior coordination

When secondary radar or ADS-B shows the aircraft with tags, the transfer between adjacent positions or units may be carried out **without prior coordination**, provided that[^2]:

1. the updated flight plan of the aircraft, including the transponder code, is passed to the accepting controller **before** the transfer;
2. the aircraft appears on the accepting controller's screen before the transfer and is identified, preferably before the initial call;
3. the controllers can talk to each other **instantly**, at any time;
4. the transfer points and other conditions are set in specific instructions or in a letter of agreement;
5. those instructions provide that the accepting controller may end this type of transfer at any time, normally with prior coordination;
6. the accepting controller is informed of **any level, speed or vector instruction** that changes the expected progress of the flight at the transfer point.

This is what the network does with the tag transfer in EuroScope. The flight plan and code already circulate on the network, the aircraft appears on the screen of whoever will receive it, and the chat is always available. Condition 6 is the one that fails most often: **what is not on the tag must be said**. If you gave a heading, a speed or a level different from what is expected at the transfer point, enter it on the tag and, if it does not fit, tell them in the chat.

Separation between aircraft about to be transferred in this way must take into account all technical and operational circumstances. If the conditions are no longer met, go back to transfer with coordination until the situation is resolved[^3].

### Transfer with coordination

When the conditions above do not apply, the transfer may be carried out provided that[^4]:

1. identification has been transferred to the accepting controller, or established directly by them;
2. the controllers can talk to each other instantly;
3. separation from other controlled flights meets the minima set for transfer between those sectors or units;
4. the accepting controller is informed of the level, speed or vector instructions applicable at the transfer point;
5. **the transferring controller maintains communication with the aircraft until the accepting controller agrees** to take over the ATS Surveillance Service.

After that, the aircraft is instructed to change frequency, and responsibility passes to the accepting controller[^4].

### Transferring identification

Identification transfer should only begin when the aircraft is already within the accepting controller's surveillance coverage[^5]. On the network, the correlated tag takes care of this. Without it, the transferring controller may give the transponder code or the position relative to a point both can see on the screen, or ask the pilot for an `IDENT` or a code change for the accepting controller to observe. These last two methods require prior agreement, because the indication on the screen is brief[^6].

### The accepting controller confirms

After identifying the aircraft, the accepting controller informs the transferring controller that it has **established contact and maintains identification**. If necessary, it also gives the frequency and transponder code[^7]. Without surveillance, the rule is the same: the accepting controller notifies that it has established contact and assumed control, unless otherwise agreed[^8].

## Transfer of communications

| Situation | When to tell the pilot to change frequency |
| --- | --- |
| Separation with ATS surveillance | **Immediately after** the accepting controller agrees to take over control[^9] |
| Procedural separation | **5 minutes before** the expected time at the common boundary of the areas[^10] |

!!! warning "Never before acceptance"
    With surveillance, the frequency change comes **after** acceptance, not before. A pilot who calls a position that has not yet accepted the transfer ends up on a frequency where nobody is responsible for them. If acceptance does not come, coordinate in the chat and, meanwhile, keep the aircraft on your frequency and away from the boundary.

Notice that the aircraft has been instructed to call the accepting controller is only required when the units have agreed to it[^11].

## Handing over to a unit without surveillance

If the next sector or unit will provide **procedural separation**, you must hand over the aircraft already separated by that method. Establish procedural separation **before** the aircraft reaches the boundary of your area or leaves surveillance coverage[^12]. Being 5 NM from the other traffic is not enough: the next controller does not see the screen and needs levels, times or DME distances they can apply.

## Who hands over to whom, and when

### ACC and APP

| Flow | The transfer takes place | Source |
| --- | --- | --- |
| Arrivals | When crossing the lateral limit of the TMA at the reporting points, when crossing the vertical limit, or at an agreed point from which the APP can take over | [^13] |
| Departures | When crossing the lateral limit of the TMA at the reporting points, when crossing the vertical limit, or at an agreed point from which the ACC can take over | [^14] |
| Arriving VFR flights | May be transferred directly from the ACC to the TWR, in coordination with the APP | [^15] |

The APP may issue clearances to any aircraft transferred to it by the ACC **without notifying the ACC**[^16].

### APP and TWR

| Flow | The transfer takes place | Source |
| --- | --- | --- |
| Arrivals | When the aircraft is in the vicinity of the aerodrome and the approach and landing can be completed by visual reference, or when it has landed | [^17] |
| Departures | Immediately after take-off, or before the aircraft enters instrument meteorological conditions | [^18] |

The APP retains control of arrivals **until they have been transferred and are in communication with the TWR**[^19]. With surveillance, it remains responsible for separation between successive aircraft on final, unless the local procedure transfers that responsibility to the tower[^20]. Send the aircraft to the tower at a point where the landing clearance can still be given in time[^21]. See also [Sequencing, On final](../vetoracao-sequenciamento/04-sequenciamento.en.md#on-final).

### TWR and ground

| Flow | The transfer takes place | Source |
| --- | --- | --- |
| Arrivals | After the tower gives the landing time and the clearance to vacate the runway and change to ground, or at another agreed position on the manoeuvring area. The pilot only changes frequency after vacating the runway | [^22] |
| Departures | At position 2 (holding point), or at another agreed position on the manoeuvring area | [^23] |

## In EuroScope

| Action | How |
| --- | --- |
| Start the transfer | `F4` on the tag and choose the next controller |
| Accept a transfer | `F3` on the tag |
| Reject an incoming transfer | `F4` on the tag |
| Alert a neighbour without transferring (*point out*) | `F1 + P` (`.point`) with the controller identifier |
| Record level, heading and speed | Tag fields, or `F8` for the level |

The routine for each transfer:

1. **Before the boundary**, check that what is on the tag is what you cleared.
2. **Transfer** with `F4`, sufficiently in advance for the accepting controller to analyse it.
3. **Wait for acceptance.** If there is no reply, call in the chat.
4. **Tell the pilot to change** frequency only after acceptance.
5. If the accepting controller requests a change, **apply it before** handing over the traffic.

See the full list of shortcuts in [EuroScope Commands](../../../fundamentos/softwares/euroscope/comandos.en.md).

[^1]: **ICA 100-37, Art. 969**. See [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 970**.
[^3]: **ICA 100-37, Art. 971 and sole paragraph**.
[^4]: **ICA 100-37, Art. 972 and sole paragraph**.
[^5]: **ICA 100-37, Art. 915**.
[^6]: **ICA 100-37, Art. 916, items II, VI, VII and VIII, and § 5°**.
[^7]: **ICA 100-37, Art. 974 and sole paragraph**.
[^8]: **ICA 100-37, Art. 835**.
[^9]: **ICA 100-37, Art. 833**.
[^10]: **ICA 100-37, Art. 832**.
[^11]: **ICA 100-37, Art. 834**.
[^12]: **ICA 100-37, Arts. 939 and 947**.
[^13]: **ICA 100-37, Art. 839**.
[^14]: **ICA 100-37, Art. 840**.
[^15]: **ICA 100-37, Art. 839, sole paragraph**.
[^16]: **ICA 100-37, Art. 838, item I**.
[^17]: **ICA 100-37, Art. 848**.
[^18]: **ICA 100-37, Art. 849**.
[^19]: **ICA 100-37, Art. 844**.
[^20]: **ICA 100-37, Art. 1005**.
[^21]: **ICA 100-37, Art. 1007**.
[^22]: **ICA 100-37, Art. 853 and sole paragraph**.
[^23]: **ICA 100-37, Art. 854**.
