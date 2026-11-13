---
  title: Installation
  description: Step-by-step installation of vacs, from download to TrackAudio integration
  icon: material/download
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Installation

From download to your first connection, in eight steps. Mark each one when done: the portal saves your progress in this browser.

<div class="vb-trilha" data-chave="vacs-instalacao" markdown>

<div class="vb-passo" markdown>

### Download the latest version

Go to the [vacs releases page](https://github.com/vacs-project/vacs/releases/latest) and, in the **Assets** section of the release marked **Latest**, download the file for your system. If the list is collapsed, click **Show all assets**.

| System | File |
| --- | --- |
| Windows | `..._x64-setup.exe` |
| macOS (Apple Silicon) | `..._aarch64.dmg` |
| macOS (Intel) | `..._x64.dmg` |
| Linux | `..._amd64.deb` (Debian and Ubuntu), `...x86_64.rpm` (Fedora, RHEL and openSUSE) or `..._amd64.AppImage` |

The **Download latest** button on the [vacs website](https://vacs.network) leads to the same place.

</div>

<div class="vb-passo" markdown>

### Install

=== "Windows"

    Run the installer and follow the steps.

=== "macOS"

    Open the `.dmg` and copy vacs to the **Applications** folder, or install it with Homebrew:

    ```text
    brew install --cask vacs-project/tap/vacs
    ```

    macOS builds are not signed yet. If the system says the app is damaged, run in Terminal:

    ```text
    sudo xattr -rd com.apple.quarantine /Applications/vacs.app
    ```

    macOS also asks for the **Input Monitoring** and **Accessibility** permissions for keyboard shortcuts.

=== "Linux"

    Install your system's package:

    ```text
    sudo apt install ./vacs_..._amd64.deb
    sudo dnf install ./vacs-...x86_64.rpm
    ```

    For the AppImage, make it executable with `chmod +x`. On Wayland, global shortcuts depend on the desktop portal.

vacs updates itself: when a new version is out, **UPDATE AVAILABLE** shows in the top bar.

</div>

<div class="vb-passo" markdown>

### Sign in with your VATSIM account

On the login screen, click **Login via VATSIM** and sign in. vacs receives only your CID, never your password.

</div>

<div class="vb-passo" markdown>

### Choose the audio devices

In **Settings › Audio**:

| Field | What to choose |
| --- | --- |
| **Headset / Output Device** | The headset, the same as in TrackAudio |
| **Microphone / Input Device** | The microphone |
| **Speaker / Notification Device** | Optional: a speaker for rings and clicks, so you hear calls even with the headset off |

Adjust the **Output**, **Input**, **Click Volume** and **Chime Volume** levels. The **Input** meter should stay green while you talk.

!!! warning "Use a headset"
    vacs has no echo cancellation. With a speaker, the other controller hears their own voice back.

</div>

<div class="vb-passo" markdown>

### Set up PTT and TrackAudio integration

Open **Settings › Transmit**. The recommended setup:

| Field | Value |
| --- | --- |
| **CALL MIC MODE** | **Push-to-Talk (PTT)**, with the key you already use for the radio |
| **RADIO INTEGRATION** | **TrackAudio** |
| **Radio PTT** | Leave empty to use the same key as the line |

That way, one key serves both radio and line: during a call it talks to the other controller; otherwise it transmits on frequency through TrackAudio.

!!! danger "Remove the key from TrackAudio"
    With integration on, do **not** keep the same key set as PTT in TrackAudio. The two programs will fight over the transmission.

The dot next to **Endpoint** shows the integration state:

| Colour | Meaning |
| --- | --- |
| Green | Connected to TrackAudio, ready |
| Blue | Transmitting on the radio |
| Yellow | TrackAudio is open but not connected to VATSIM voice |
| Grey | Not ready yet |
| Red | Connection error |

If you prefer separate keys for radio and line, choose a different **Radio PTT**.

</div>

<div class="vb-passo" markdown>

### Set up the shortcuts

In **Settings › Hotkeys**, all shortcuts are optional:

| Action | What it does |
| --- | --- |
| **Accept first call** | Answers the first ringing call |
| **End active call** | Hangs up the current call |
| **Toggle RADIO PRIO** | Turns radio priority over the line on or off |
| **SAY AGAIN** | Replays the last transmission received on the radio |

!!! tip "Tip"
    Use the **same key** for *Accept first call* and *End active call*: it answers when a call rings and hangs up when a call is in progress.

!!! warning "Windows and administrator mode"
    If EuroScope or TrackAudio run as administrator, vacs shortcuts do not work while their window has focus. Run all three the same way: all as administrator or none.

</div>

<div class="vb-passo" markdown>

### Review the call options

In **Settings › Call**, the defaults suit most people. Worth knowing:

- **Enable priority calls**: lets you make and receive **PRIO** calls.
- **Use default call sources**: picks the source station of your calls automatically.
- **End active call on accept**: answering a second call hangs up the current one.
- **Always relay calls**: routes audio through the vacs server. Turn it on if you use a VPN or calls connect and drop.
- **Ring sounds**: replaces the rings with **WAV** files of 0.1 to 30 seconds.

</div>

<div class="vb-passo" markdown>

### Connect for the first time

In your next session, with the position connected in EuroScope and the primary frequency set, click **Connect** in vacs. Keys for online sectors become clickable, and you show up for the other controllers.

[:octicons-arrow-right-24: Usage](utilizacao.en.md){ .md-button .md-button--primary }

</div>

</div>

## Where the files are

Settings are kept in `.toml` files. The **Open Config** button, under **Settings › Miscellaneous**, opens the folder:

| System | Folder |
| --- | --- |
| Windows | `%APPDATA%\app.vacs.vacs-client\` |
| macOS | `~/Library/Application Support/app.vacs.vacs-client/` |
| Linux | `~/.config/app.vacs.vacs-client/` |

Close vacs before editing the files by hand: the program rewrites `audio.toml` and `client.toml` and undoes your changes.
