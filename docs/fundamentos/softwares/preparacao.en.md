---
  title: Set Up Your Workstation
  description: Installation path for EuroScope, TrackAudio, vATIS and vacs, from download to your first test as an observer
  icon: material/map-marker-path
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Set Up Your Workstation

From installation to your first test, in ten steps. Each one sums up the essentials and points to the program's full guide. Mark the steps as you finish them: the portal saves your progress in this browser.

!!! info "How long does it take?"
    An afternoon is enough. The slowest parts are downloading the sector files and adjusting the audio.

<div class="vb-trilha" data-chave="softwares" markdown>

<div class="vb-passo" markdown>

### Check what you need

- A **Windows** computer: EuroScope has no macOS or Linux version.
- A headset with microphone.
- A free key or button for push-to-talk (PTT).
- Your **CID** and **VATSIM password**. All programs ask for the same credentials.

</div>

<div class="vb-passo" markdown>

### Install EuroScope

Download the installer from the [EuroScope website](https://www.euroscope.hu), under `Installation`, and follow the steps as usual.

!!! danger "Recommended version"
    Install version **3.2.3.2**, available [on this page](https://www.euroscope.hu/wp/2024/06/09/v3-2-2-3-and-v3-2-3-2-with-token-authentication-update/).

[:octicons-arrow-right-24: EuroScope installation](euroscope/instalacao.en.md){ .md-button }

</div>

<div class="vb-passo" markdown>

### Install the sector files

Vatsim Brasil sector files are installed and updated with the **Sector File Manager**, which you install through the [Vectors ATC Hub](https://github.com/VectorsATCGroup/vectors-atc-releases/releases/latest/download/VectorsATCHub-Setup.exe). Sign in with your AeroNav account and click **Install** on the FIRs you will control.

[:octicons-arrow-right-24: Sector files](euroscope/instalacao.en.md#install-the-sector-file-manager){ .md-button }

!!! warning "The profile dialog did not show up?"
    Untick `Auto load last profile on startup` and open EuroScope again.

</div>

<div class="vb-passo" markdown>

### Get to know the two profiles

Each FIR has two profile files (`.prf`):

| Profile | Positions | Use |
| --- | --- | --- |
| `solo` | `DEL`, `RMP`, `GND` and `TWR` | Shows the aerodrome and the ground tags |
| `radar` | `APP` and `CTR` | Shows the control area and the radar targets |

Open the `solo` profile of your aerodrome's FIR and explore the screen without connecting: menus, lists, zoom with `F11` and `F12`.

[:octicons-arrow-right-24: The main screen](euroscope/utilizacao.en.md#the-main-screen){ .md-button }

</div>

<div class="vb-passo" markdown>

### Install TrackAudio

Download the latest version from [TrackAudio on GitHub](https://github.com/pierr3/TrackAudio/releases), in the **Assets** section of the latest release. On Windows, the file ends in `.exe`.

[:octicons-arrow-right-24: TrackAudio installation](trackaudio/instalacao.en.md){ .md-button }

</div>

<div class="vb-passo" markdown>

### Set up audio and PTT

In TrackAudio's settings (the gear in the top-left corner):

- enter your VATSIM CID and password;
- choose the **primary** output (the headset), the **secondary** output (the speaker) and the **input** (the microphone);
- set the **PTT** key or button.

!!! tip "Tip"
    Pick a PTT you can reach without letting go of the mouse. You will press it hundreds of times per session.

</div>

<div class="vb-passo" markdown>

### Install vATIS and import the profiles

Download vATIS from the [official website](https://vatis.app). When it opens, click `Import` in the profile window and select your FIR's `.json` file. Vatsim Brasil keeps one profile per FIR, with stations, runway presets and contractions already set up.

[:octicons-arrow-right-24: Vatsim Brasil profiles](vatis/instalacao.en.md#vatsim-brasil-profiles){ .md-button }

!!! warning "Do not edit the profile"
    The profiles update themselves, and local changes are overwritten. To fix something, open a suggestion in the portal repository.

</div>

<div class="vb-passo" markdown>

### Fill in your details in vATIS

Open the profile, click `User Settings` and fill in your name, CID, password and rating. Click `Save`.

</div>

<div class="vb-passo" markdown>

### Install vacs

Download vacs from the [releases page](https://github.com/vacs-project/vacs/releases/latest), install it and sign in with **Login via VATSIM**. In **Settings › Transmit**, choose **Push-to-Talk** and turn on the **TrackAudio** integration: the same key will serve both radio and line.

!!! warning "One key, one owner"
    With integration on, remove the PTT key from TrackAudio and keep it only in vacs. The two programs cannot use the same key at the same time.

[:octicons-arrow-right-24: vacs installation](vacs/instalacao.en.md){ .md-button }

</div>

<div class="vb-passo" markdown>

### Run a test as an observer

Before your first real session, check that everything talks to each other:

1. In EuroScope, connect with an `_OBS` callsign (for example, `SBGR_OBS`).
2. Open TrackAudio: the callsign shows at the top and the `CONNECT` button turns green.
3. Connect and add the frequency of an online position with the `+` button. Tick only `RX` and listen.
4. Disconnect TrackAudio and then EuroScope.

If you heard the frequency, your workstation is ready.

[:octicons-arrow-right-24: Connection checklist](sessao.en.md){ .md-button .md-button--primary }

</div>

</div>

## Still have questions?

??? question "Can I use macOS or Linux?"
    TrackAudio and vATIS run on all three systems, but EuroScope is Windows only. On macOS or Linux it needs a virtual machine or a compatibility layer, and this guide does not cover those setups.

??? question "Do I need vATIS every session?"
    Only when your position is responsible for the aerodrome ATIS. Even so, it is worth installing it from the start to get to know the program calmly.

??? question "What about AFV (Audio for VATSIM)?"
    TrackAudio replaces the old AFV client for controllers. Use TrackAudio.
