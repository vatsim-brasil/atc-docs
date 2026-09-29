---
title: Checklists
icon: material/format-list-checks
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Checklists for use during the session. Each item points to the chapter in which the subject is covered in full.

## Opening the position { #abertura-da-posicao }

### Authorization

- [ ] Listed on the VATSIM Brasil ATC Roster
- [ ] Hold a **C1** rating or higher
- [ ] Hold the **Tier 2 "Oceanic Positions"** endorsement

Details in [Preparation and opening, Authorization](abertura.en.md#autorizacao).

### Client and sector

- [ ] **SBAO** sector package installed and on the current AIRAC cycle
- [ ] **Radar** profile loaded, not the ground profile
- [ ] EuroScope restarted, if the previous position was in another FIR
- [ ] Visibility points distributed across the extent of the sector
- [ ] Screen range showing the entry and exit points of the main route

### Connection and audio

- [ ] Correct position callsign, as per [the positions table](estrutura.en.md#posicoes-na-vatsim)
- [ ] Primary frequency matching the position
- [ ] TrackAudio connected **after** EuroScope
- [ ] `RX` and `TX` manually enabled on the position's frequency
- [ ] `XCA` enabled on the position's frequency
- [ ] Unused frequencies removed from the interface

### Datalink

- [ ] Logon code checked: `SBAO` for the general position
- [ ] Datalink integration connected and message window visible
- [ ] If unavailable, decided that the session will be run by voice and reports

### Publishing the position

- [ ] *Controller information* filled in, at most four lines of 76 characters, in English
- [ ] Expected disconnection time stated
- [ ] Indication of procedural control without radar surveillance
- [ ] Datalink status stated

### Before announcing

- [ ] Online adjacent units identified
- [ ] Opening coordinated with each connected adjacent unit
- [ ] Traffic already inside the FIR surveyed
- [ ] Position report obtained from each aircraft without a record
- [ ] Split plan defined, if another rated controller is available

## Receiving each aircraft

- [ ] **Identification** confirmed
- [ ] **Route** checked against the sector, with reporting points recognized
- [ ] **Level** compatible with the applicable table
- [ ] **Mach number** declared or obtained from the pilot
- [ ] **Capabilities** checked: `W` for RVSM, `R` for PBN, `D1` for ADS-C, `SEL/` for SELCAL
- [ ] Entry **estimate** confirmed, by coordination, by `EET/` or by the pilot
- [ ] **Communication** established, with the means in use identified
- [ ] **Conflicts** assessed against the whole picture before accepting
- [ ] **Record** opened with the estimate for the next point

Details in [Flight plan and capabilities](plano-de-voo.en.md) and [Operational flow](fluxo.en.md).

## Monitoring

With each report received, or every 15 minutes:

- [ ] **Position** updated, with exact time
- [ ] Next-point **estimate** revised
- [ ] **Separation** recalculated for all affected pairs
- [ ] Pending **requests** answered
- [ ] **Coordination** done, if anything already passed to the adjacent unit has changed
- [ ] **Record** updated

Warning signs that require immediate action:

- [ ] Expected report that did not arrive
- [ ] Estimate revised by more than 2 minutes
- [ ] ADS-C event notification for lateral deviation, altitude deviation or vertical rate
- [ ] Aircraft reporting inability to maintain level, Mach or navigation accuracy

## Transfer

- [ ] Transfer-point **estimate** calculated and updated
- [ ] **Coordination** sent early enough
- [ ] **Acceptance** obtained from the next unit, or conditions renegotiated
- [ ] **Updated information** confirmed: level, Mach, route and capabilities
- [ ] **Instruction to the pilot** issued, with `CONTACT` or `MONITOR` as appropriate
- [ ] **Datalink** transferred, or logon redone, or connection terminated
- [ ] **Record** closed with the time over the transfer point

If the next unit is not online:

- [ ] Pilot told that there is no ATS unit connected ahead
- [ ] Information for calling the unit ahead provided
- [ ] Last position, level and Mach recorded
- [ ] Service ended explicitly

## Closing the position

- [ ] **Advance notice** to adjacent units and to aircraft on frequency
- [ ] Closing **coordination** with each connected adjacent unit
- [ ] **Transfer** of all traffic that can still be handed off
- [ ] **Check** of aircraft that will be left without service, with explicit instructions to each one
- [ ] **If another position of the FIR is online**, handover of the complete traffic list, with position, level, Mach, estimate and communication status
- [ ] **Closing the connections**: datalink, TrackAudio and ATC client, in this order
- [ ] **Disconnection** only after confirming that no aircraft is left awaiting a reply

!!! tip "On the network (Vatbrz)"
    Announce the closure at least 15 minutes in advance. In a FIR where crossing time is measured in hours, a pilot who loses the unit without notice may be left without a reference for a long time.
