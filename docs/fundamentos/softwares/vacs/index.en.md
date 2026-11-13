---
  title: Overview
  description: vacs, the telephone line between VATSIM controllers for voice coordination
  icon: material/phone-classic
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# vacs

[vacs](https://vacs.network) is the telephone line between controllers: a **ground-to-ground** (G2G) voice communication system for VATSIM. With it, you call the neighbouring unit and coordinate by voice, as in real control centres, instead of typing in the chat.

It is a free, open-source project maintained by the [vacs-project](https://github.com/vacs-project/vacs) team, with versions for Windows, macOS and Linux.

## How it works

- **You call a sector, not a person.** Each key on the screen stands for a sector. The call rings whoever is covering that sector at the moment, including through [top-down](../../../documentos/manuais/coordenacao-transferencia/04-rede.en.md#top-down-coverage).
- **Your position is recognised from your connection.** vacs identifies your station from the callsign, primary frequency and facility type you connected with in EuroScope.
- **Login is through VATSIM.** You sign in with VATSIM Connect, and vacs never sees your password.
- **Audio goes straight between controllers**, peer to peer, with no voice server in the middle.
- **It talks to TrackAudio.** With radio integration, one PTT key serves both the radio and the line, and vacs shows your frequencies and records what you receive so you can replay it.

## At Vatsim Brasil

Brazil's sectors and positions are set up in the vacs data repository, [vacs-data](https://github.com/vacs-project/vacs-data/tree/main/dataset/SB), in the `SB` folder. It covers all five FIRs: **Amazônica** (SBAZ), **Brasília** (SBBS), **Curitiba** (SBCW), **Recife** (SBRE) and **Atlântico** (SBAO), with centres, approaches, towers and ground positions.

!!! warning "Connect with the right callsign and frequency"
    If your connection's callsign or frequency do not match the dataset, vacs does not recognise your position, and other controllers cannot call you. Always use the callsigns and frequencies in the [MOP](../../../MOP/aerodromos/index.en.md).

Found a missing sector or a wrong frequency? Let the Vatsim Brasil team know. Fixes are made in the vacs-data repository.

## A call, step by step

Tap each point, or use the arrow keys, to follow a call from start to finish.

<div class="vb-perfil" data-forma="voo" markdown>

<section data-sigla="1" data-nome="Pick the sector" data-alt="0" markdown>

### Pick the sector

On the vacs screen, each sector is a **direct access key**. It is clickable only when the sector is online, both in vacs and on the network.

Before calling, **prepare the message**: aircraft callsign, point, time, level. The line is for short messages.

</section>

<section data-sigla="2" data-nome="Call" data-alt="1" markdown>

### Call

Click the sector key. The call goes to whoever covers that sector now: if the Tower is offline, it rings the Approach covering it.

For urgent coordination, turn on **PRIO** before clicking. The other controller sees a yellow border and hears a different ring.

</section>

<section data-sigla="3" data-nome="Ringing" data-alt="2" markdown>

### The other side answers

On the other side, your sector key flashes green and the ring sounds. They answer by clicking it.

If nobody answers, the call ends on its own and **REMOTE TARGET DID NOT ANSWER** shows in the top bar.

</section>

<section data-sigla="4" data-nome="Coordinate" data-alt="2" markdown>

### Coordinate

When the indicator in the top-left corner turns **green**, the line is open. Talk with the line PTT and keep it short. An estimate, following the MCA 100-16 model:

> "Estimate VRG 3256, Cuiabá to Guarulhos, FL 330, VARGA at 55."

The receiver acknowledges with "roger" or reads the data back.

</section>

<section data-sigla="5" data-nome="Hang up" data-alt="0" markdown>

### Hang up

Click **END**, on the bottom bar. Then enter what was agreed on the EuroScope tag, so everyone sees the same information.

</section>

</div>

## Guides

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Installation**

    ---

    Step-by-step installation, login and setup of audio, PTT and TrackAudio integration.

    [:octicons-arrow-right-24: Installation](instalacao.en.md)

-   :material-phone-in-talk:{ .lg .middle } **Usage**

    ---

    Making and receiving calls, conferences, the telephone page, the radio and fixing common problems.

    [:octicons-arrow-right-24: Usage](utilizacao.en.md)

</div>

## Line, chat or tag?

| Tool | Use it for |
| --- | --- |
| EuroScope tag (`F4` / `F3`) | Routine handoffs that need no conversation |
| **vacs** | Coordination that needs an answer: level requests, releases, restrictions, non-standard traffic, emergencies |
| Private chat | Messages that can wait, or when the other controller is not on vacs |
| `ATC` channel | Announcements to everyone, such as opening and closing positions |
