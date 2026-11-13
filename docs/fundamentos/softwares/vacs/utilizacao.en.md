---
  title: Usage
  description: How to make and receive coordination calls in vacs, with conferences, the telephone page and the radio
  icon: material/phone-in-talk
---

--8<-- "includes/abreviacoes.md"

# Usage

This page walks through vacs in a control session: connecting, calling, answering, conferencing and closing. It assumes the [installation](instalacao.en.md) is already done.

## Connecting

``` mermaid
flowchart LR
    A[EuroScope connected<br/>and primary frequency] --> B[TrackAudio<br/>connected]
    B --> C[Connect<br/>in vacs]
    C --> D[Keys for online<br/>sectors active]
```

1. Connect the position in [EuroScope](../euroscope/utilizacao.en.md#connecting-to-the-network) and set the primary frequency. Without it, vacs does not recognise your station.
2. Connect [TrackAudio](../trackaudio/utilizacao.en.md), if you use radio integration.
3. In vacs, click **Connect**.

## The screen

The main screen is made of **direct access keys**, one per sector. The layout comes from the Vatsim Brasil dataset: in tabs, on the bottom bar, or on a map (*GEO*). A key is **clickable** when the sector is online in vacs and on the network.

Besides the keys, you will use:

| Button | What it does |
| --- | --- |
| **PRIO** | Makes the next call a priority call |
| **CONF** | Invites another sector to the current call |
| **PLAY BACK** and **SAY AGAIN** | Replay the transmissions received on the radio |
| **RADIO PRIO** | Gives the radio priority and mutes the line microphone |
| **END** | Hangs up, on the bottom bar |
| Telephone | Opens the directory, recent calls and the dial pad, on the right side |

The indicator in the top-left corner shows the line state: **orange** calling or ringing, **green** connected.

## Making a call

1. **Prepare the message** before calling.
2. Click the sector key. The call rings whoever covers that sector now, including through top-down.
3. Wait for the indicator to turn **green** (or the call start sound) and talk.
4. When done, click **END**.

!!! warning "Do not talk before green"
    With the same key for radio and line, pressing the PTT right after the call connects can **transmit on frequency**. Wait for the green indicator.

If nobody answers, the key flashes red and the top bar shows **REMOTE TARGET DID NOT ANSWER**. An unanswered call ends on its own after 60 seconds.

### Which station you are calling from

If you cover more than one sector, such as an APP covering the TMA towers, vacs picks the call's source station on its own. To choose another one:

- **one click** on one of your sectors sets the source for the **next** call only (light orange);
- **a double click** fixes the source (dark orange) until you click again.

### Priority call

For urgent coordination, click **PRIO** and then the sector key. On the other side, the call shows with a yellow border and a different ring. Use it only when the coordination cannot wait.

## Receiving a call

When someone calls, the calling sector's key **flashes dark green** and the ring sounds. Click it to answer, or use the **Accept first call** shortcut.

- If more than one call is ringing, choose which to answer.
- A conference shows as **CONF** on the key.
- There is no reject button: if you cannot answer, let it ring, and the caller gets a no-answer notice.
- Answering a second call hangs up the current one. You can change this in **Settings › Call**, with **End active call on accept**.

## Conference

To add a third sector to a call in progress:

1. Click **CONF**. It flashes dark blue.
2. Click the key of the sector you want to invite.

Whoever added the third participant is the **leader**. Only the leader invites and removes participants, and if the leader leaves, the conference ends for everyone. Other participants leave with **END** without dropping the call. A conference holds up to eight controllers.

## The telephone page

The telephone button, on the right, opens four sections:

| Section | What it is for |
| --- | --- |
| **Dir.** | Directory: every controller connected to vacs, including those without a key on your screen. Search and click **Call**. |
| **Call List** | Recent calls: green for received, blue for made, a red X for those that did not connect. |
| **Dial Pad** | Calls a controller by CID. |
| **Ign.** | List of ignored CIDs, which do not ring for you. |

## Radio and replay

With TrackAudio integration, the vacs **Radio** page shows your frequencies, with `Rx` and `Tx` and the **CPL** and **FAST CPL** couplings. It is a shortcut to TrackAudio, which remains your radio.

- **RADIO PRIO**: while on, the line microphone is muted, so you can talk on the radio without the call hearing you. It turns off by itself at the end of each call.
- **PLAY BACK**: lists the transmissions received on the radio so you can hear them again. Turn on **Enable radio playback** in the advanced settings first. It works on Windows and Linux, not on macOS.
- **SAY AGAIN**: replays the last transmission received. Useful when a pilot talked over the line.

Line calls are not recorded.

## How to talk on the line

Messages between units follow Annex II of MCA 100-16:

- when answering, say your unit's name and "go ahead" or "stand by";
- prepare the message before calling and check you are talking to the right unit;
- when there is no read-back, confirm with "roger".

| Who | Message |
| --- | --- |
| SECTOR 1 | "Transfer BRA 4177, passing FL 160, south of Campinas, requesting direct Bonsucesso." |
| SECTOR 2 | "Direct Bonsucesso approved, contact on 129,75." |
| SECTOR 1 | "Roger, will call on 129,75." |

More models for estimates, requests and transfers are in the [Phraseology of the Coordination and Transfer Manual](../../../documentos/manuais/coordenacao-transferencia/05-fraseologia.en.md#messages-between-units).

## Closing

1. End any calls in progress with **END**.
2. Disconnect vacs before disconnecting TrackAudio and EuroScope.

## When something goes wrong

??? failure "The sector key is grey"
    The sector is offline, or its controller is not connected to vacs. Look for them in the directory (**Dir.**). If they are not there, coordinate through the chat.

??? failure "Other controllers cannot call me"
    vacs did not recognise your position. Check that you connected with the MOP callsign and primary frequency. If they are correct, the position may be missing from the dataset: let the Vatsim Brasil team know.

??? failure "The call connects and drops, or never connects"
    A firewall, antivirus or VPN may block the direct connection. Turn on **Always relay calls** in **Settings › Call**.

??? failure "Shortcuts do not work with EuroScope in focus"
    On Windows, if EuroScope or TrackAudio run as administrator, run vacs as administrator too, or none of them.

??? failure "The Endpoint dot is yellow"
    TrackAudio is open but not connected to voice. Click `CONNECT` in TrackAudio.

??? failure "The other controller hears an echo"
    vacs has no echo cancellation. Use a headset instead of a speaker.

## Learn more

- [Official vacs documentation](https://docs.vacs.network);
- [Server status](https://status.vacs.network);
- [Brazil's sector dataset](https://github.com/vacs-project/vacs-data/tree/main/dataset/SB), in the vacs-data repository.
