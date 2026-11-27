---
  title: Overview
  description: The Sector File Manager, the program that installs and updates the Vatsim Brasil sector files in EuroScope
  icon: material/folder-sync
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Sector File Manager

The [EuroScope Sector File Manager](https://github.com/VectorsATCGroup/euroscope-sector-file-manager) installs and updates the Vatsim Brasil sector files in EuroScope in one click. It downloads each FIR's official package from [AeroNav](https://files.aero-nav.com/SBXX), takes a backup, applies the change and keeps your settings.

It is a free, open-source program (Apache 2.0 licence), maintained by [Vectors ATC Group](https://github.com/VectorsATCGroup), an independent group of VATSIM controllers. It runs on Windows only, like EuroScope.

## Why use it

Without it, updating the sector every AIRAC is manual work: go to AeroNav, download each FIR's package, unpack it and copy the files to the right folder without wiping your profiles and customisations. A file copied to the wrong place, or a copy interrupted midway, leaves EuroScope with a broken sector.

The Sector File Manager does all of this at once, safely:

- **Downloads only from the official AeroNav.** The program does not redistribute files: the package comes from the same source you would use by hand.
- **Takes a backup before changing anything.** The installation is prepared in a temporary area and applied only if everything succeeds. If something fails, it rolls the operation back.
- **Keeps what is yours.** Your customisations in the `Settings` folder, plugins and files you created stay where they are.
- **Shows each FIR's AIRAC.** The dashboard compares the installed cycle with the one available on AeroNav.
- **Speaks Portuguese.** The interface comes in Portuguese and English, with light and dark themes.

## The FIRs

The dashboard shows the five Vatsim Brasil FIRs:

| FIR | Name |
| --- | --- |
| `SBAO` | Atlântico |
| `SBAZ` | Amazônica |
| `SBBS` | Brasília |
| `SBCW` | Curitiba |
| `SBRE` | Recife |

## The update cycle

Tap each point, or use the arrow keys, to follow an update from start to finish.

<div class="vb-perfil" data-forma="voo" markdown>

<section data-sigla="AIRAC" data-nome="New cycle" data-alt="0" markdown>

### A new AIRAC comes out

An AIRAC cycle starts every 28 days, and the Vatsim Brasil team publishes the updated FIR packages on AeroNav.

Fixes within the same cycle come out as a new issue of the package. The dashboard shows these issues as `2608/2`; the first issue of the cycle shows simply as `2608`.

</section>

<section data-sigla="SFM" data-nome="Open the program" data-alt="1" markdown>

### Open the Sector File Manager

With **EuroScope closed**, open the program. It checks the AeroNav session and reads the installed AIRAC straight from the `.sct` file EuroScope loads.

</section>

<section data-sigla="UPD" data-nome="Update" data-alt="2" markdown>

### Click Update

If the AeroNav package is newer than the installed one, the FIR shows **Update**. Click it.

The program downloads the official package, takes the backup and prepares the change in a temporary area.

</section>

<section data-sigla="OK" data-nome="Applied" data-alt="1" markdown>

### The change is applied

Only when everything is ready do the new files replace the old ones, all at once. If the download or the copy fails midway, nothing changes in your installation.

</section>

<section data-sigla="ES" data-nome="Open EuroScope" data-alt="0" markdown>

### Open EuroScope

Open EuroScope in the FIR's profile and check the AIRAC of the loaded sector. Ready for the session.

</section>

</div>

## Guides

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Installation**

    ---

    Track for installing through the Vectors ATC Hub, signing in to AeroNav and the first installation of the FIRs.

    [:octicons-arrow-right-24: Installation](instalacao.en.md)

-   :material-folder-sync:{ .lg .middle } **Usage**

    ---

    The dashboard, updating every AIRAC, what is kept, the settings and fixes for common problems.

    [:octicons-arrow-right-24: Usage](utilizacao.en.md)

</div>

!!! info "Independent project"
    The Sector File Manager is not a program by VATSIM, AeroNav, Navigraph or EuroScope. Questions and problems with the program go to the project's [issues page](https://github.com/VectorsATCGroup/euroscope-sector-file-manager/issues). Errors in the sector content, such as a wrong frequency or procedure, go to the Vatsim Brasil team.
