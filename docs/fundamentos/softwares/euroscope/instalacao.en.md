---
  title: Installation
---

--8<-- "includes/abreviacoes.md"

![Fundamentals - Euroscope - Installation](img/head-euroscope-instalacao.png)

## Download

!!! info "Information"
    Euroscope is only available for *Microsoft Windows*.

1. Go to the [Euroscope website](https://www.euroscope.hu) and open the downloads page by clicking `Installation` on the top bar.

![](img/es1.png){ : style="border:2px solid #999" }

2. Click the link available in the "Download" section to download EuroScope. Once downloaded, follow the installer steps as usual.

![](img/es2.png){ : style="border:2px solid #999" }

!!! danger "Attention!"
    We recommend installing version **3.2.3.2**, which can be found [at this link](https://www.euroscope.hu/wp/2024/06/09/v3-2-2-3-and-v3-2-3-2-with-token-authentication-update/).

!!! warning "A tip!"
    We strongly recommend reading the Euroscope manual, which can easily be found on the website under `Documentation` > `Download User's Guide`.

## *Sectorfiles* and Configuration Files

VATSIM Brasil sector files and profiles are published on **[Aeronav GNG](https://files.aero-nav.com/SBXX)**. The division recommends installing and updating them with the **[EuroScope Sector File Manager](https://github.com/VectorsATCGroup/euroscope-sector-file-manager)**, a free tool developed by **[Vectors ATC Group](https://vectorsatcgroup.com)**.

<figure markdown>
[![Vectors ATC Group](https://raw.githubusercontent.com/VectorsATCGroup/euroscope-sector-file-manager/main/assets/vectors-logo-dark.png#only-light){ width="240" }![Vectors ATC Group](https://raw.githubusercontent.com/VectorsATCGroup/euroscope-sector-file-manager/main/assets/vectors-logo-white.png#only-dark){ width="240" }](https://vectorsatcgroup.com)
</figure>

The app downloads each FIR package straight from Aeronav, takes a backup and applies the update without deleting your `Settings` folder or your custom files. If anything fails, the installation is rolled back.

!!! info "Requirements"
    Windows 10 or later (64-bit), EuroScope installed and an Aeronav account.

1. Download `VectorsEuroScopeSectorFileManager-Setup.exe` from the [releases page](https://github.com/VectorsATCGroup/euroscope-sector-file-manager/releases/latest) and run it. It installs for your user only and does not ask for administrator rights.
2. On first run, the app finds your EuroScope installation and sector files folder.
3. Sign in to your Aeronav account in the window that opens. Sign-in happens on the official Aeronav page and is remembered for next time.
4. The dashboard lists each FIR (SBAO, SBAZ, SBBS, SBCW and SBRE) with the installed and available AIRAC. Click `Install` or `Update` on the FIRs you control.

!!! tip "Tip"
    Open the app at each new AIRAC cycle to keep your sector files current. It also tells you when a new version of the app itself is out.

??? question "Can the app see my password?"
    No. Sign-in happens on the official Aeronav, VATSIM and Navigraph pages, in an isolated browser window. The app does not read or store your password and sends no data to any server. Details are in the [project repository](https://github.com/VectorsATCGroup/euroscope-sector-file-manager#privacy-first-by-design).

??? question "Can I install without the app?"
    Yes. Download the FIR package from [Aeronav GNG](https://files.aero-nav.com/SBXX), unzip it and copy the files into the EuroScope sector files folder, taking care not to overwrite your `Settings` folder.

### Opening the profile

When EuroScope starts, choose the profile (`.prf`) for the FIR and the position you are going to control.

!!! warning "Attention!"
    If the profile dialog box does not appear, the `Auto load last profile on startup` option is checked. Uncheck the option and open Euroscope again.

??? question "What is the difference between the `radar` profile and the `solo` profile?"
    The `solo` profile contains a color scheme and tags optimized for controlling the `DEL`, `RMP`, `GND` and `TWR` positions.

    The `radar` profile, on the other hand, is optimized for the `APP` and `CTR` positions.

!!! info "An important note"
    If you want to change position and the new one is in a different FIR, you must restart Euroscope and open the correct profile for the new position. Simply loading the new sector/ASR is not enough.
