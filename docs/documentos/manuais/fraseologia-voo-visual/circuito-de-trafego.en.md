---
title: Traffic Circuit
icon: material/vector-square
---

--8<-- "includes/abreviacoes.md"

# Traffic Circuit

The traffic circuit is the rectangle flown around the runway in use. It exists so that everyone does the same thing, in the same place, at the same altitude, making each aircraft's behaviour predictable.

For the VFR pilot, the circuit is where radio communication becomes densest and most standardised. Each leg has a report, and each report has an expected response.

## The circuit legs

The drawing below reproduces the layout shown on visual approach charts: a racetrack with the **runway in use in the centre** and the direction of flight indicated by the arrows. The example is a **left-hand circuit**, meaning all turns are to the left.

Note one thing that confuses many people: only the **final** and the **climb after takeoff** run along the runway centreline, the line that crosses the middle of the circuit. The **upwind leg** and the **downwind leg** are parallel to the runway, but **laterally offset**, one on each side of the centreline.

<div style="overflow-x: auto; margin: 1.5rem 0;">
<svg viewBox="0 0 820 420" width="100%" role="img" aria-labelledby="circ-titulo circ-desc" style="max-width: 820px; display: block; margin: 0 auto;">
  <title id="circ-titulo">Standard left-hand traffic circuit</title>
  <desc id="circ-desc">Circuit racetrack with the runway in use in the centre. The runway centreline crosses the circuit and carries the final and the climb after takeoff. The upwind and downwind legs run parallel to the runway, offset to each side of the centreline.</desc>

  <rect x="150" y="80" width="560" height="260" rx="90" ry="90" fill="none" stroke="currentColor" stroke-width="4"/>

  <line x1="150" y1="210" x2="710" y2="210" stroke="currentColor" stroke-width="3"/>
  <rect x="330" y="200" width="200" height="20" fill="var(--md-default-bg-color)" stroke="currentColor" stroke-width="3"/>

  <polygon points="432,333 450,340 432,347" fill="currentColor"/>
  <polygon points="428,73 410,80 428,87" fill="currentColor"/>
  <polygon points="703,168 710,150 717,168" fill="currentColor"/>
  <polygon points="143,252 150,270 157,252" fill="currentColor"/>
  <polygon points="282,203 300,210 282,217" fill="currentColor"/>
  <polygon points="602,203 620,210 602,217" fill="currentColor"/>

  <text x="430" y="62" font-size="17" text-anchor="middle" fill="currentColor">Downwind leg</text>
  <text x="430" y="368" font-size="17" text-anchor="middle" fill="currentColor">Upwind leg</text>
  <text x="752" y="210" font-size="17" text-anchor="middle" fill="currentColor" transform="rotate(-90 752 210)">Crosswind</text>
  <text x="108" y="210" font-size="17" text-anchor="middle" fill="currentColor" transform="rotate(-90 108 210)">Base leg</text>

  <text x="238" y="192" font-size="17" text-anchor="middle" fill="currentColor">Final</text>
  <text x="430" y="250" font-size="15" text-anchor="middle" fill="currentColor" font-style="italic">runway in use</text>
  <text x="612" y="192" font-size="15" text-anchor="middle" fill="currentColor" font-style="italic">climb after takeoff</text>
</svg>
</div>

| Order | Leg | What it is | Typical report |
| --- | --- | --- | --- |
| 1 | Upwind leg | Parallel to the runway, in the same direction as landing and takeoff, laterally offset from the centreline | No routine report |
| 2 | Crosswind | Perpendicular to the runway, abeam the opposite threshold, provides the transition to the circuit side | No routine report |
| 3 | Downwind leg | Parallel to the runway, in the direction opposite to landing, further from the centreline | "downwind leg runway ONE THREE" |
| 4 | Base leg | Perpendicular to the runway, before final alignment | "base leg runway ONE THREE" |
| 5 | Final | On the extended runway centreline, descending to land | "on final" |

!!! warning "Upwind is not the runway centreline"
    In the drawing, the runway centreline is the straight line that crosses the middle of the circuit. The **final** and the **climb after takeoff** lie along it.

    The **upwind leg** is something else: it runs parallel to the runway, in the same direction, but **offset** from the centreline. Together with the downwind leg, on the opposite side, it closes the racetrack.

    This distinction matters in practice: when the Tower says "join the upwind leg", it is not telling you to fly over the runway.

!!! note "Standard turns"
    Unless otherwise published, the circuit is flown with **left turns**. Any right-hand circuit is a local restriction and will be advised by ATC or published on the aerodrome chart.

    The detailed geometry, altitudes and sequencing criteria are in the [Traffic Circuit Manual](../manual-circuito-trafego/index.md).

!!! tip "The chart rules"
    The rectangle above is the theoretical standard. In practice, the actual layout is published on the aerodrome's **VAC**, which also defines the minimum circuit altitudes and the visual reporting points.

    Two examples of how this varies:

    | Aerodrome | Minimum circuit altitudes | Remarks |
    | --- | --- | --- |
    | Pampulha, SBBH, RWY 13/31 | CAT A and B: 3,900 ft, CAT C: 4,200 ft | Reporting points MINEIRÃO, PAZ, ESPERANÇA and RIO |
    | Goiânia, SBGO, RWY 14/32 | CAT A and B: 3,500 ft, CAT C: 3,700 ft, CAT D and E: 4,200 ft | Separate racetracks for aeroplanes and helicopters, the latter at 3,200 ft |

    Always check the current chart before flying or controlling.

## Ways to join the circuit

The pilot reports their intention and ATC confirms or amends it. The most common options:

| Entry | When to use | How to report |
| --- | --- | --- |
| Start of the downwind leg | Arriving from the circuit side | "will join at the beginning of downwind leg runway ONE TWO" |
| Midpoint of the downwind leg | Arriving abeam the aerodrome | "will join at midpoint of downwind leg runway ONE TWO" |
| Base leg | Arriving from the base sector | "will join base leg runway ONE TWO" |
| Long final | Arriving aligned with the runway | "will report on long final runway ONE TWO" |
| Straight-in approach | Cleared by ATC to expedite the flow | "cleared straight in approach, runway ONE ONE" |
| Crossing the field | Arriving from the side opposite the circuit | "for crossing the aerodrome" |

!!! tip "Choose before you call"
    Decide how you will join **before** pressing the PTT. ATC needs to know where you will enter in order to sequence the rest of the traffic, and an "I don't know" answer is costly on the frequency.

## The reporting cycle

The dynamic is always the same, and it repeats on every lap of the circuit.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, perna do vento da pista UNO TRÊS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, avistado, reporte perna base.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, perna base da pista UNO TRÊS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, reporte na final.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, na final.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, pista UNO TRÊS, pouso autorizado, vento UNO TRÊS ZERO graus, UNO ZERO nós.
    </div>
    <div class="comms-pilot">
      Pouso autorizado, pista UNO TRÊS, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, downwind leg runway ONE THREE.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, I have you in sight, report base leg.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, base leg runway ONE THREE.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, report on final.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, on final.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, runway ONE THREE, cleared to land, wind ONE THREE ZERO degrees, ONE ZERO knots.
    </div>
    <div class="comms-pilot">
      Cleared to land, runway ONE THREE, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, tramo con viento en cola de la pista UNO TRES.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, a la vista, reporte tramo base.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, tramo base de la pista UNO TRES.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, reporte en final.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, en final.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, pista UNO TRES, autorizado a aterrizar, viento UNO TRES CERO grados, UNO CERO nudos.
    </div>
    <div class="comms-pilot">
      Autorizado a aterrizar, pista UNO TRES, **VICTOR BRAVO ROMEO**.
    </div>

??? abstract "A few remarks..."

    1. The downwind report includes the runway, because at aerodromes with more than one runway that is the information that locates the aircraft. On the following legs the runway is already implied, but repeating it is not an error.

    2. When the circuit is right-hand, this goes into the position report:

        > :flag_br: Torre Recife, **VICTOR BRAVO ROMEO**, base pela direita, pista UNO OITO. <br/>
        > :flag_gb: Recife Tower, **VICTOR BRAVO ROMEO**, right hand base, runway ONE EIGHT. <br/>
        > :flag_es: Recife Torre, **VICTOR BRAVO ROMEO**, tramo base por la derecha, pista UNO OCHO. <br/>

    3. It is established practice to report the landing gear down and locked in the base leg or final report, especially in retractable-gear aircraft and at aerodromes served by a **RADIO** station.

        > :flag_br: **VICTOR BRAVO ROMEO**, perna base da pista UNO DOIS, trem de pouso baixado e travado. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, base leg runway ONE TWO, landing gear down and locked. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, tramo base de la pista UNO DOS, tren de aterrizaje abajo y asegurado. <br/>

    4. ATC may issue the landing clearance early, at the base leg report, if the runway is clear and the sequence is established. This is normal and does not remove the need for the final report.

## Leaving the circuit after takeoff

On takeoff, the aircraft is already in the circuit. To leave it, an ATC instruction is required and, as a rule, a report that the circuit has been left behind.

=== ":flag_br: Portuguese"

    | Situação | Fraseologia |
    | --- | --- |
    | Saída em frente | "VICTOR BRAVO ROMEO, após a decolagem, saída em frente, reporte livre do circuito." |
    | Saída pela perna do vento | "VICTOR BRAVO ROMEO, após a decolagem, saída pela perna do vento à esquerda, reporte livre do circuito." |
    | Saída com curva imediata | "VICTOR BRAVO ROMEO, após a decolagem, curva à direita, reporte livre do circuito." |
    | Reporte do piloto | "VICTOR BRAVO ROMEO, livre do circuito, rumo leste, subindo para SETE MIL E QUINHENTOS pés." |

=== ":flag_gb: English"

    | Situation | Phraseology |
    | --- | --- |
    | Straight out departure | "VICTOR BRAVO ROMEO, after departure, straight out, report clear of the circuit." |
    | Departure via downwind | "VICTOR BRAVO ROMEO, after departure, leave via left downwind, report clear of the circuit." |
    | Departure with immediate turn | "VICTOR BRAVO ROMEO, after departure, turn right, report clear of the circuit." |
    | Pilot report | "VICTOR BRAVO ROMEO, clear of the circuit, eastbound, climbing to SEVEN THOUSAND FIVE HUNDRED feet." |

=== ":flag_es: Spanish"

    | Situación | Fraseología |
    | --- | --- |
    | Salida en línea recta | "VICTOR BRAVO ROMEO, después del despegue, salida en línea recta, reporte libre del circuito." |
    | Salida por el tramo con viento en cola | "VICTOR BRAVO ROMEO, después del despegue, salida por el tramo con viento en cola por la izquierda, reporte libre del circuito." |
    | Salida con viraje inmediato | "VICTOR BRAVO ROMEO, después del despegue, vire a la derecha, reporte libre del circuito." |
    | Reporte del piloto | "VICTOR BRAVO ROMEO, libre del circuito, rumbo este, ascendiendo a SIETE MIL QUINIENTOS pies." |

---
