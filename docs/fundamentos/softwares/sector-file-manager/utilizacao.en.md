---
  title: Usage
  description: How to keep the Vatsim Brasil sector files current with the Sector File Manager, every AIRAC
  icon: material/folder-sync
---

--8<-- "includes/abreviacoes.md"

# Usage

This page shows the Sector File Manager day to day: checking the AIRAC, updating the FIRs and solving common problems. It starts from the point where the [installation](instalacao.en.md) is done.

## The routine before every session

``` mermaid
flowchart LR
    A[EuroScope<br/>closed] --> B[Open the<br/>Sector File Manager]
    B --> C{Any FIR<br/>with Update?}
    C -- Yes --> D[Click<br/>Update]
    C -- No --> E[Open EuroScope]
    D --> E
```

1. **Close EuroScope.** The program should not replace files EuroScope is using.
2. Open the Sector File Manager and wait for the session check (**Checking saved session…**).
3. If any FIR shows **Update**, click it.
4. Open EuroScope in the FIR's profile.

## The dashboard

Each FIR shows on its own line, with:

| Information | What it means |
| --- | --- |
| Installed AIRAC | The cycle of the sector on your machine, read from the `.sct` file EuroScope loads |
| Available AIRAC | The newest package published on AeroNav |
| **Install** | The FIR is not installed yet |
| **Update** | There is a package newer than the installed one |

The dashboard shows what is installed even before you sign in to AeroNav. To see what is new and download it, you must be authenticated.

### Issues within a cycle

When the team fixes a package within the same AIRAC, it comes out as a new issue. The dashboard shows the first issue as `2608` and the following ones as `2608/2`, `2608/3`. A new issue also shows as **Update**: install it, even if the cycle is the same.

## What the update changes

| The update replaces | The update keeps |
| --- | --- |
| Sector (`.sct` and `.ese`), ASR, NavData, alias and the package's vATIS settings | The `solo` and `radar` profiles (`.prf`) and your customisations in the `Settings/SOLO` and `Settings/RADAR` folders |
| `login_profiles.txt`, `VoiceChannels.txt` and `AircraftPerformance.txt` | Plugins and files you created that are not part of the package |

!!! warning "Edited one of those three files?"
    Hand edits to `login_profiles.txt`, `VoiceChannels.txt` and `AircraftPerformance.txt` are lost on update. The automatic backup keeps the previous version.

## The AeroNav session

- The sign-in is kept for up to **30 days**, in an isolated browser profile.
- If AeroNav ends the session earlier, the dashboard asks you to sign in again. Click **Authenticate**, sign in, and the operation carries on.
- **Logout** deletes the saved session. Use it on a shared computer.

## Settings

In **Settings**:

| Option | What it does |
| --- | --- |
| Language | Portuguese or English. The switch takes effect immediately. |
| Theme | Light or dark |
| **Updates** | Turns the check for a new program version at startup on or off, and has the **Check now** button |

When a new program version is out, it shows the release notes and the **Update now** button, and a banner stays under the title bar until you update. The update is downloaded, verified and installed on its own, and the program reopens. The [Vectors ATC Hub](instalacao.en.md#install-the-vectors-atc-hub) also keeps the program current.

The Sector File Manager opens a single window: launching the program again brings the open window to the front. Closing the main window quits the program.

## When something goes wrong

??? failure "The dashboard says the session expired"
    AeroNav ended the session. Click **Authenticate** and sign in again.

??? failure "EuroScope still shows the old AIRAC"
    EuroScope was open during the update, or you opened a profile from another folder. Close EuroScope, check on the dashboard that the FIR is on the new AIRAC and open the profile from the folder the program uses.

??? failure "The update was interrupted midway"
    Nothing changes in your installation: the change is applied only when everything is ready. Open the program and click **Update** again.

??? failure "I lost an edit to a package file"
    Package files are replaced on update. The previous version is in the backup, in the program folder (`%LOCALAPPDATA%\VectorsATCGroup\EuroScopeSectorFileManager`).

??? failure "Another problem"
    Logs are in `logs\app-*.log`, in the program folder. They do not store addresses, cookies or passwords, and can be attached to your report on the project's [issues page](https://github.com/VectorsATCGroup/euroscope-sector-file-manager/issues).

## Learn more

- [Sector File Manager repository](https://github.com/VectorsATCGroup/euroscope-sector-file-manager), with the version history in `CHANGELOG.md`;
- [Vectors ATC Hub and version catalogue](https://github.com/VectorsATCGroup/vectors-atc-releases);
- [FIR packages on AeroNav](https://files.aero-nav.com/SBXX).
