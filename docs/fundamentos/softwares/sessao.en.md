---
  title: Start Up and Shut Down
  description: Interactive checklist for connecting and disconnecting EuroScope, TrackAudio, vacs and vATIS, with fixes for the most common problems
  icon: material/clipboard-check-outline
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Start Up and Shut Down

Order matters: EuroScope connects first and disconnects last. Use this checklist every session. Your ticks are saved in this browser, and you can clear them for next time.

<div class="vb-checklist" data-chave="softwares-sessao" markdown>

### Before connecting

- [ ] I checked in the Sector File Manager that the sector files are on the current AIRAC.
- [ ] I opened EuroScope with the right FIR profile: `solo` for aerodrome, `radar` for APP and CTR.
- [ ] I checked the METAR (`F2`) and the runway in use according to the MOP.
- [ ] I checked the controller list to see who is already online.
- [ ] I put on my headset and tested the PTT.

### EuroScope

- [ ] I connected with the position callsign and my correct CID, facility and rating.
- [ ] I set the position frequency as primary (`Prim`).
- [ ] I filled in the *Controller ATIS* lines.

### TrackAudio

- [ ] The callsign showed at the top and I clicked `CONNECT`.
- [ ] I ticked `RX` and `TX` on my frequency.
- [ ] I turned on `XC` (right-click on `XCA`), if the position uses more than one transceiver.

### vacs

- [ ] I clicked **Connect** and the keys of online sectors lit up.
- [ ] The **Endpoint** dot is green, with TrackAudio integration on.

### vATIS (if the position has an ATIS)

- [ ] I chose the station and the preset for the runway in use.
- [ ] I checked the aerodrome conditions and NOTAMs left from the previous session.
- [ ] I clicked `CONNECT` and confirmed the letter.

### When closing

- [ ] I handed off the traffic or told pilots to monitor UNICOM (122.800).
- [ ] I announced on the `ATC` channel that I am disconnecting.
- [ ] I disconnected the ATIS in vATIS.
- [ ] I disconnected vacs.
- [ ] I disconnected TrackAudio.
- [ ] I disconnected EuroScope (`Disconnect`).

</div>

## When something goes wrong

??? failure "TrackAudio shows *No VATSIM connection detected!*"
    EuroScope is not connected to the network, or the connection dropped. Connect EuroScope first: TrackAudio detects the position on its own and the `CONNECT` button turns green.

??? failure "I hear nothing on the frequency"
    Check that `RX` is ticked on the frequency. Then, in TrackAudio's settings, check that the primary output is your headset. The `RX` button turns orange when someone is transmitting: if it lights up and you hear nothing, the problem is the audio output.

??? failure "Pilots cannot hear me"
    `TX` must be ticked, and the button turns orange while you press the PTT. If it does not change colour, review the PTT key in the settings. If it does, review the audio input (the microphone).

??? failure "Pilots on opposite sides of the area cannot hear each other"
    With several transceivers on the same frequency, each pilot hears only the nearest one. Turn on `XC`, by right-clicking the `XCA` button, to couple the transceivers.

??? failure "Voice dropped with *Callsign changed during an active session*"
    TrackAudio ends the voice session when the callsign changes in EuroScope or when the connection drops. Reconnect EuroScope if needed and click `CONNECT` in TrackAudio again, ticking `RX` and `TX`.

??? failure "The network refused the EuroScope connection"
    Check your CID, password, facility and rating. The network does not accept a position above your rating: with S1, only `_DEL`, `_GND` and `_OBS`.

??? failure "I switched FIRs and the sector looks wrong"
    Loading another sector with EuroScope open is not enough. Close the program and open the new FIR's profile.

??? failure "Nobody can call me on vacs"
    vacs recognises the position from the callsign and the primary frequency. Check both in EuroScope against the MOP. See more fixes in [vacs: usage](vacs/utilizacao.en.md#when-something-goes-wrong).

??? failure "I pressed PTT and went out on frequency instead of the line"
    With the same key for radio and vacs, wait for the call indicator to turn green before talking.

??? failure "The ATIS letter is flashing"
    A new METAR came out and vATIS updated the ATIS. Click the letter once to acknowledge the update.

## Going further

- [Your first session](../controlador/primeira-sessao.en.md), the controller checklist for the first connection;
- [EuroScope: usage](euroscope/utilizacao.en.md), with the control routine step by step;
- [TrackAudio: usage](trackaudio/utilizacao.en.md), with every button and indicator;
- [vATIS: usage](vatis/utilizacao.en.md), with preparing and maintaining the ATIS;
- [vacs: usage](vacs/utilizacao.en.md), with coordination calls.
