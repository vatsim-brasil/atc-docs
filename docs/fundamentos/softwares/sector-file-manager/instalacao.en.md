---
  title: Installation
  description: Installation track for the Sector File Manager, from the Vectors ATC Hub to the FIRs installed in EuroScope
  icon: material/download
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Installation

From download to installed FIRs, in five steps. Tick each one when done: the portal keeps your progress in this browser.

!!! info "What you need"
    - Windows 10 or newer, 64-bit.
    - [EuroScope installed](../euroscope/instalacao.en.md).
    - An [AeroNav](https://files.aero-nav.com/SBXX) account, the same one you would use to download the packages by hand.

<div class="vb-trilha" data-chave="sfm-instalacao" markdown>

<div class="vb-passo" markdown>

### Install the Vectors ATC Hub

The Sector File Manager is distributed through the **Vectors ATC Hub**, the program that installs, updates, repairs and removes the Vectors ATC Group programs.

Download **[VectorsATCHub-Setup.exe](https://github.com/VectorsATCGroup/vectors-atc-releases/releases/latest/download/VectorsATCHub-Setup.exe)** and run it.

It installs per user and **does not ask for administrator rights**. If Windows does not have Microsoft WebView2 yet, the installer adds it.

!!! warning "Do not use the old releases page"
    The original Sector File Manager repository stopped at version 1.2.0. New versions come out only through the Hub and the [vectors-atc-releases](https://github.com/VectorsATCGroup/vectors-atc-releases) catalogue.

</div>

<div class="vb-passo" markdown>

### Install the Sector File Manager through the Hub

Open the Hub and install the **EuroScope Sector File Manager**. From then on, the Hub keeps the program up to date, and the Hub updates itself.

</div>

<div class="vb-passo" markdown>

### Open the program for the first time

On first run, a wizard finds the **EuroScope installation** and the **sector files folder** on its own. Check the paths it shows before moving on.

!!! tip "Tip"
    Pick the language and theme in **Settings**. Switching language takes effect immediately, without a restart.

</div>

<div class="vb-passo" markdown>

### Sign in to your AeroNav account

Click **Authenticate**. A window opens with the official AeroNav page, isolated from the rest of the program. Sign in with your account, through VATSIM or Navigraph, as on the website.

The window closes by itself when the package list shows up. The program **never sees your password**: it only keeps the AeroNav session, for up to 30 days.

</div>

<div class="vb-passo" markdown>

### Install the FIRs

The dashboard shows the five Vatsim Brasil FIRs, with each one's available AIRAC. Click **Install** on the FIRs you will control.

The program downloads the package, takes a backup and applies the installation. If something fails midway, it rolls the operation back.

!!! tip "Install every FIR"
    With all five installed, you are ready to control in any FIR, and a last-minute switch will not catch you without the sector.

[:octicons-arrow-right-24: Usage](utilizacao.en.md){ .md-button .md-button--primary }

</div>

</div>

## Where the program keeps its files

Settings, the record of what is installed, backups and logs live in:

```text
%LOCALAPPDATA%\VectorsATCGroup\EuroScopeSectorFileManager
```

The program stores only technical data: installation paths, installed versions, theme and language. The AeroNav session lives in an isolated browser profile in the same folder.

## Uninstalling

Uninstall through the Hub, or run the installer again and choose **Uninstall**. Uninstalling deletes **the whole** folder above, including backups and the AeroNav session. The sector files installed in EuroScope stay where they are.

On a new installation, the program starts from scratch and shows the first-run wizard.
