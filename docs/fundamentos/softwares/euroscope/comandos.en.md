---
  title: Command Guide
---

--8<-- "includes/abreviacoes.md"

# Command Guide

This guide gathers the main keyboard shortcuts and command-line commands of **EuroScope**.

## Main shortcuts

| Key | Parameters | Action |
|---|---|---|
| `F2` | Four-letter ICAO code | Adds or removes METARs. |
| `F3` | Click on the aircraft tag | Assumes tracking of the aircraft or accepts a handoff. |
| `F4` | Click on the aircraft tag | Drops tracking, refuses a handoff or initiates a handoff. |
| `F5` | Altitude in hundreds + click on the tag | Changes the final altitude, as per the flight plan. |
| `F6` | None | Displays the flight strip of the current aircraft. |
| `F7` | None | Cycles through the open radar displays. |
| `F8` | Altitude in hundreds + click on the tag | Changes the temporary (cleared) altitude. |
| `F9` | Click on the tag | Automatically assigns a squawk code. |
| `F9` | Four-digit code + click on the tag | Manually assigns the given squawk code. |
| `F9` | `V`, `R` or `T` + click on the tag | Sets the communication type: voice, receive only or text. |
| `F11` | None | Zooms the radar in. |
| `F12` | None | Zooms the radar out. |

## Commands accessed with the `F1` key

| Keys | Command | Parameters | Action |
|---|---|---|---|
| `F1 + A` | `.am` | Click on the aircraft tag | Amends the flight plan. |
| `F1 + C` | `.chat` | Click on the aircraft tag | Opens the chat window. |
| `F1 + D` | `.distance` | Click on one aircraft and then on another aircraft or point | Continuously displays the updated distance between an aircraft and another aircraft or point. |
| `F1 + F` | `.find` | Type an aircraft or fix | Displays a line from the center of the screen to the given point. |
| `F1 + P` | `.point` | Controller identifier + click on the aircraft tag | Highlights the aircraft on the specified controller's screen, performing a *point out*. |
| `F1 + S` | `.sep` | Click on the tags of two aircraft | Continuously displays the predicted point of closest approach between the aircraft. |
| `F1 + 0` | - | None | Closes the current ASR view. |
| `F1 + 1` to `F1 + 9` | - | None | Opens the ASR views predefined in the general settings. |

## Command-line commands

- `.break`

Changes the color of your callsign, as displayed to other controllers, to indicate that you need a break or relief.

```text
.break
```

- `.center`

Centers the current radar view on a fix or aircraft.

```text
.center FIX_OR_AIRCRAFT
```

- `.contactme`

Sends a text message to the pilot requesting contact on the current frequency.

```text
.contactme
```

Shortcut: `HOME`.

- `.nobreak`

Cancels the previous `.break` command.

```text
.nobreak
```

- `.qs`

Changes the content of the aircraft's *scratchpad*.

```text
.qs CONTENT
```

Shortcut: `INS`.

- `.rings`

Displays range rings around a center point, specifying the spacing in miles and the number of rings.

```text
.rings CENTER SPACING COUNT
```

Running the command without parameters removes the rings:

```text
.rings
```

- `.showvis`

Displays the area in which VATSIM aircraft information is visible.

```text
.showvis
```

- `.vis`

Sets up to four centers for the VATSIM visibility area.

```text
.vis FIX1 FIX2 FIX3 FIX4
```

- `.vis1`, `.vis2`, `.vis3` and `.vis4`

Individually sets each center of the VATSIM visibility area.

```text
.vis1 FIX
.vis2 FIX
.vis3 FIX
.vis4 FIX
```

- `.wallop`

Sends a message to all connected supervisors.

```text
.wallop MESSAGE
```

## Reference

For complete explanations, see the [EuroScope command-line reference](https://www.euroscope.hu/wp/command-line-reference/).
