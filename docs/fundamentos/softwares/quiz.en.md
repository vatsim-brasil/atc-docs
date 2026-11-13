---
  title: Software Quiz
  description: Quick questions about EuroScope, TrackAudio, vATIS and vacs
  icon: material/head-question-outline
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Software Quiz

Twelve questions about the controller workstation. It is not graded: it is for you to find out what to review before connecting.

<div class="vb-quiz" markdown>

<div class="vb-pergunta" data-resposta="2" markdown>

Which program must connect to the network first?

1. TrackAudio
2. EuroScope
3. vATIS

<div class="vb-explica" markdown>
**EuroScope** connects first. TrackAudio and vATIS depend on its connection. See [the connection order](index.en.md#the-connection-order).
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

You are going to control `SBCT_GND`. Which EuroScope profile do you open?

1. `radar`
2. Either one, they have the same tools
3. `solo`

<div class="vb-explica" markdown>
The **solo** profile is made for `DEL`, `RMP`, `GND` and `TWR`. **radar** is for `APP` and `CTR`.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

You were on `SBCT_TWR` and are going to open a position in another FIR. What do you do?

1. Close EuroScope and open the new FIR's profile
2. Load the new sector through `OPEN SCT`
3. Just change the callsign in the connection window

<div class="vb-explica" markdown>
Loading another sector with the program open is **not enough**. You must restart EuroScope with the new FIR's profile.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

You clicked `CONNECT` in TrackAudio and your frequency showed up. Can pilots hear you already?

1. Yes, TrackAudio enables the frequency on its own
2. No, you must tick `RX` and `TX` yourself
3. Only after you publish the ATIS

<div class="vb-explica" markdown>
TrackAudio **does not enable** frequencies on its own. Tick `RX` to listen and `TX` to transmit.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

The `TX` button turns orange. What does that mean?

1. A pilot is transmitting
2. The frequency has a problem
3. You are transmitting, with the PTT pressed

<div class="vb-explica" markdown>
Orange `TX` is **you** talking. When another station is transmitting, it is `RX` that turns orange.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

You are controlling `SBBS_CTR` and two pilots in distant parts of the FIR cannot hear each other. What do you turn on in TrackAudio?

1. `XC`, by right-clicking the `XCA` button
2. `SPK`
3. `XCA`, with a left click

<div class="vb-explica" markdown>
With several transceivers, each pilot hears only the nearest one. **XC** (right-click) couples the transceivers **of the same frequency**. **XCA** (left-click) joins **different** frequencies and should be used with care.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Which key assumes a traffic or accepts a handoff in EuroScope?

1. `F4`
2. `F3`
3. `F8`

<div class="vb-explica" markdown>
`F3` assumes. `F4` starts or rejects a handoff, and `F8` changes the cleared level. See the [command guide](euroscope/comandos.en.md).
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

You want to fix a wrong frequency in your FIR's vATIS profile. What do you do?

1. Edit the profile in `ATIS Configuration`
2. Delete the profile and create a new one
3. Open a suggestion in the portal repository

<div class="vb-explica" markdown>
Vatsim Brasil profiles **update themselves**, and local changes are overwritten at the next update. The fix goes to the [repository](https://github.com/vatsim-brasil/atc-docs).
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

The ATIS letter started flashing in vATIS. What happened?

1. A new METAR came out and the ATIS was updated
2. The ATIS disconnected
3. Another controller took over the station

<div class="vb-explica" markdown>
The letter flashes on every **update** from the METAR. Click it once to acknowledge it.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

In what order do you close the session?

1. EuroScope, TrackAudio, vacs, vATIS
2. vATIS, vacs, TrackAudio, EuroScope
3. It does not matter, as long as all are disconnected

<div class="vb-explica" markdown>
In **reverse** connection order: the ATIS first, then the line and the radio and, last of all, EuroScope. Before anything else, hand off the traffic.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

You click the `SBGR_TWR` key in vacs, but nobody is on Guarulhos Tower. `SBXP_APP` is online. What happens?

1. The call fails: the Tower is closed
2. It rings every controller in the FIR
3. It rings `SBXP_APP`, which covers the Tower through top-down

<div class="vb-explica" markdown>
vacs calls the **sector**, and the call goes to whoever covers it at the moment. See [how it works](vacs/index.en.md#how-it-works).
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

You answered a call in vacs and use the same key for radio and line. When do you start talking?

1. Right away, as soon as you click the key
2. When the call indicator turns green
3. After disconnecting TrackAudio

<div class="vb-explica" markdown>
Before green, the PTT can still **go out on frequency**. Wait for the green indicator or the call start sound.
</div>

</div>

</div>

Want to review? Go back to the [installation path](preparacao.en.md) or the [connection checklist](sessao.en.md).
