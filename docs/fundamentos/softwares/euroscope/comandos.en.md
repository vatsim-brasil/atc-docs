---
  title: Command Guide
  description: EuroScope keyboard shortcuts and command-line commands, with a quiz on the main ones
  icon: material/keyboard-outline
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

## Practise the shortcuts

Six everyday situations. Pick the right shortcut for each one.

<div class="vb-quiz" markdown>

<div class="vb-pergunta" data-resposta="2" markdown>

The pilot called on your frequency and the traffic is white (related). Which key assumes it?

1. `F4`
2. `F3`
3. `F9`

<div class="vb-explica" markdown>
`F3` assumes the traffic or accepts the handoff. `F4` goes the other way: it starts or rejects a handoff.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

You cleared a climb to FL150. How do you record it on the tag?

1. `F5` + `150` + click the tag
2. `.qs 150`
3. `F8` + `150` + click the tag

<div class="vb-explica" markdown>
`F8` changes the **cleared level** (CFL). `F5` changes the final level of the flight plan, which is something else.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

You want to watch the distance between two crossing aircraft. Which command predicts the point of closest approach?

1. `F1 + S` (`.sep`)
2. `F1 + D` (`.distance`)
3. `F1 + F` (`.find`)

<div class="vb-explica" markdown>
`.sep` predicts the minimum distance between two aircraft. `.distance` shows the current distance to another aircraft or point.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

An aircraft called on the wrong frequency and you want it to call you. What do you use?

1. `.wallop`
2. `.contactme`, shortcut `HOME`
3. `.break`

<div class="vb-explica" markdown>
`.contactme` sends the pilot a text message asking for contact on your frequency. `.wallop` calls the supervisors.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

How do you add the SBKP METAR to the screen?

1. `.metar SBKP`
2. `F1 + M` and click the aerodrome
3. `F2` + `SBKP`

<div class="vb-explica" markdown>
`F2` followed by the ICAO code adds or removes METARs.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

You will need relief soon. How do you tell the other controllers without typing in the chat?

1. `.break`
2. `.nobreak`
3. `.showvis`

<div class="vb-explica" markdown>
`.break` changes the colour of your callsign for other controllers. `.nobreak` cancels it.
</div>

</div>

</div>

## Reference

For complete explanations, see the [EuroScope command-line reference](https://www.euroscope.hu/wp/command-line-reference/).
