---
  title: Overview
  description: The four programs in a Vatsim Brasil controller's workstation and the order in which they connect
  icon: material/monitor-dashboard
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Controller Software

A Vatsim Brasil controller's workstation is made of four programs. Each one has a job, and they depend on each other: EuroScope connects you to the network, and the other three use that connection.

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **EuroScope**

    ---

    The radar screen. It shows the sector, the traffic and the flight plans, and it is where you assume, clear and hand off every aircraft.

    [:octicons-arrow-right-24: EuroScope](euroscope/index.en.md)

-   :material-headset:{ .lg .middle } **TrackAudio**

    ---

    The radio. It transmits and receives on your position's frequencies, with the push-to-talk (PTT) button.

    [:octicons-arrow-right-24: TrackAudio](trackaudio/index.en.md)

-   :material-weather-windy:{ .lg .middle } **vATIS**

    ---

    The ATIS. It builds the aerodrome information from the METAR and the runway in use and broadcasts it with a synthesized voice.

    [:octicons-arrow-right-24: vATIS](vatis/index.en.md)

-   :material-phone-classic:{ .lg .middle } **vacs**

    ---

    The telephone line. It connects you to the other controllers to coordinate by voice, with no typing in the chat.

    [:octicons-arrow-right-24: vacs](vacs/index.en.md)

</div>

## The connection order

The programs come up one at a time, always in the same order. Tap each step, or use the arrow keys, to see what happens in it.

<div class="vb-perfil" data-forma="degraus" markdown>

<section data-sigla="ES" data-nome="Open the profile" data-alt="0" markdown>

### 1. Open EuroScope with the right profile

Choose the `.prf` file of the FIR you will control: **solo** for `DEL`, `GND` and `TWR`, **radar** for `APP` and `CTR`.

To switch FIRs, close the program and open the new FIR's profile. Loading another sector with EuroScope open is not enough.

</section>

<section data-sigla="NET" data-nome="Connect to the network" data-alt="1" markdown>

### 2. Connect EuroScope to VATSIM

In the connection menu, choose `Connect` and fill in the position callsign (`SBCT_TWR`, for example), your name, CID, password, facility and rating. Leave `Server` on `AUTOMATIC`.

The network refuses a connection to a position above your rating. To just watch, use a callsign ending in `_OBS`.

</section>

<section data-sigla="FREQ" data-nome="Primary frequency" data-alt="2" markdown>

### 3. Set the primary frequency

In `OTHER SET` › *Voice Communications Setup*, set the position frequency as **primary** (`Prim`). The same window holds the *Controller ATIS* lines, which pilots read when they look up your position.

Without a primary frequency, pilots see your position on the network but do not know which frequency to call.

</section>

<section data-sigla="TA" data-nome="TrackAudio" data-alt="3" markdown>

### 4. Connect TrackAudio

With EuroScope connected, TrackAudio shows your callsign and the `CONNECT` button turns green. Click it and **tick** `RX` and `TX` on your frequency yourself: the program does not do it for you.

Without EuroScope connected, TrackAudio shows *"No VATSIM connection detected!"*.

</section>

<section data-sigla="G2G" data-nome="vacs" data-alt="4" markdown>

### 5. Connect vacs

Click **Connect** in vacs. It recognises your position from the callsign and the primary frequency and lights up the keys of online sectors, so you can call them.

With TrackAudio integration, the same PTT key serves both radio and line.

</section>

<section data-sigla="ATIS" data-nome="vATIS" data-alt="5" markdown>

### 6. Publish the ATIS, if needed

If the position is responsible for the ATIS, open the FIR profile in vATIS, choose the station and the preset for the runway in use, check the conditions and NOTAMs and click `CONNECT`.

The ATIS runway must match EuroScope and what was agreed with the other units.

</section>

<section data-sigla="ON" data-nome="Position open" data-alt="6" markdown>

### 7. Position open

Announce on the `ATC` channel that you opened the position and assume the traffic already in your area.

To close, go down the steps in **reverse order**: hand off the traffic, disconnect vATIS, vacs, TrackAudio and, last of all, EuroScope.

</section>

</div>

!!! tip "Tip"
    Follow the same order every time, like a cockpit checklist. The [connection checklist](sessao.en.md) has every step for you to tick.

## What you will find here

| Page | What it has |
| --- | --- |
| [Set up your workstation](preparacao.en.md) | Installation path for the four programs, with progress tracking |
| [Start up and shut down](sessao.en.md) | Connection checklist and fixes for the most common problems |
| [EuroScope](euroscope/index.en.md) | Installation, usage and command guide |
| [TrackAudio](trackaudio/index.en.md) | Installation and usage |
| [vATIS](vatis/index.en.md) | Installation, Vatsim Brasil profiles and usage |
| [vacs](vacs/index.en.md) | Installation, coordination calls and TrackAudio integration |
| [Software quiz](quiz.en.md) | Quick questions to check what you have learned |

## What you need

| Item | Note |
| --- | --- |
| A **Windows** computer | EuroScope runs only on Windows. The other three also have macOS and Linux versions. |
| Headset with microphone | A headset keeps the frequency audio from feeding back into the microphone. |
| A key or button for PTT | It can be on the keyboard, the mouse or a joystick. |
| VATSIM CID and password | All programs ask for the same credentials. vacs signs in through VATSIM login. |
| A stable connection | An internet drop ends both the voice session and the network connection. |
