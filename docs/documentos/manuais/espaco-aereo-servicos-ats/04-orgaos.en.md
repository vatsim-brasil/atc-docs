---
title: ATS Units and Positions
icon: material/account-tie-hat
---

--8<-- "includes/abreviacoes.md"

# ATS Units and Positions

## ATS unit and network position

The previous chapter ended with a promise: to show how the Area Control Service, the Approach Control Service and the Aerodrome Control Service are distributed among the ATS units of Vatsim Brasil — ACC, APP, TWR. This chapter keeps that promise and adds the missing link: the operational position a controller actually connects on the network.

An ATS unit is a normative concept. Annex VII of ICA 100-12 defines the Air Traffic Services Unit — abbreviated "ATS unit" (*órgão ATS*) — as the "generic term meaning, as the case may be, an air traffic control unit or a flight information unit"[^2], and the Air Traffic Control Unit, in the same Annex VII of ICA 100-12, as the "generic term meaning, as the case may be, an Area Control Center, Approach Control or Aerodrome Control Tower"[^2]. It is ICA 100-37 and ICA 100-12 that say what each of these units is, what it provides and over which airspace it has authority.

A position, by contrast, is a VATSIM network convention, with no counterpart in ICA 100-37 or ICA 100-12: neither of them mentions logins, controller clients or callsign suffixes. What the network does is assign to each real unit — or to each function within a unit, as the next section shows — a connection suffix: `_CTR`, `_APP`, `_TWR`, `_GND`, `_DEL`. Connecting as `_TWR` is not the same as being the Tower — it means operating, on the network, the position that corresponds to the unit the next section defines.

## ACC, APP and TWR: the three control units

Annex VII of ICA 100-12 defines the three air traffic control units by what each one provides:

- **Area Control Center (ACC)** is, according to Annex VII of ICA 100-12, the "unit established to provide air traffic control service to controlled flights in control areas under its jurisdiction"[^2];
- **Approach Control (APP)** is, in the same Annex VII of ICA 100-12, the "unit established to provide air traffic control service to controlled flights arriving at, or departing from, one or more aerodromes"[^2];
- **Aerodrome Control Tower (TWR)** is, also in Annex VII of ICA 100-12, the "unit established to provide air traffic control service to aerodrome traffic"[^2].

ICA 100-37 already detailed, in the previous chapter, how these three relate to the three services: the Area Control Service is provided by an ACC or by a delegated APP (Art. 33 of ICA 100-37)[^1]; the Approach Control Service by an APP or by a delegated ACC or TWR (Art. 34 of ICA 100-37)[^1]; the Aerodrome Control Service by a delegated TWR (Art. 35 of ICA 100-37)[^1]. Delegation is the regulation's escape valve for operationally necessary arrangements — a single unit accumulating the functions of more than one service —, but the standard arrangement, and the one the table below assumes, is one unit per service.

## Two positions within the TWR itself

Not every network position corresponds to a distinct unit. Art. 509 of ICA 100-37 states that the functions of an Aerodrome Control Tower may be performed by different control positions, and lists three: the "TWR control position, normally responsible for operations on the runway and for aircraft flying within the area of responsibility of the Aerodrome Control Tower"; the "ground control position, normally responsible for traffic on the maneuvering area, with the exception of runways"; and the "traffic clearance position, normally responsible for issuing air traffic information and clearances to aircraft intending to take off"[^1].

The three are positions of a single unit — the TWR —, not three distinct ATS units. It is Art. 509 of ICA 100-37 itself that establishes this internal division of functions; it is the VATSIM network, not ICA 100-37 or ICA 100-12, that decides to turn each of them into a separate connection (`_DEL`, `_GND`, `_TWR`). Nothing in the Instruction requires three logins — technically, a single controller could hold all three positions, as happens in practice when Ground Control and Traffic Clearance are not connected. What changes in that case is not the jurisdiction — which remains the TWR's over the maneuvering area and aerodrome traffic —, but who, on the network, is on the other side of the microphone.

## Correspondence table { #tabela-de-correspondencia }

The table below relates each ATS unit covered in this chapter — the three control units and the two that do **not** control — to the airspace in which it typically operates and to the network position that corresponds to it, when there is one: the Flight Information Center has no position of its own, and the column records this in its row. When a unit is subdivided internally, the "Internal position" column indicates which function is involved, using the names Art. 686 of ICA 100-37 gives to the three positions that Art. 509 of the same Instruction establishes: Art. 509 describes them — "TWR control position", "ground control position" and "traffic clearance position" — and Art. 686 calls them by name, in order of precedence for the Flight Plan clearance: "Traffic Clearance" (*Autorização de Tráfego*), "Ground Control" (*Controle de Solo*) and "Control Tower" (*Torre de Controle*)[^1]. They are the same three positions in both articles. The column is empty in the other rows because ICA 100-37 names internal positions only for the TWR — for the other units it speaks generically of "control positions" and "control sectors" of the same unit, without naming them (Art. 852)[^1]. Note that "Aerodrome Control Tower (TWR)" repeats in three rows: it is the same unit in all three, not three different units.

Two caveats about the "Network position" column. First: the suffixes `_CTR`, `_APP`, `_TWR`, `_GND` and `_DEL` are a convention of the **whole VATSIM network**, as the previous section noted — not a Brazilian invention. What is specific to **Vatsim Brasil** in this table is the `_R_TWR` of the RÁDIO positions, whose `_R_` marker is local, and the absence of a position for the Flight Information Center. Second: "CTR" carries two meanings in this manual — the `_CTR` suffix, which is the ACC position, and the Control Zone, which is airspace. In the airspace column the Control Zone is written out in full, so the two are not confused.

| ATS unit | Internal position | Network position | Typical airspace | Service provided |
| --- | --- | --- | --- | --- |
| Area Control Center (ACC) | — | `_CTR` | CTA, UTA and other portions of the FIR | Area control |
| Approach Control (APP) | — | `_APP` | TMA and Control Zone\* | Approach control |
| Aerodrome Control Tower (TWR) | Control Tower | `_TWR` | ATZ and Control Zone\* | Aerodrome control |
| Aerodrome Control Tower (TWR) | Ground Control | `_GND` | Maneuvering area | Aerodrome control |
| Aerodrome Control Tower (TWR) | Traffic Clearance | `_DEL` | Apron | Aerodrome control |
| ATS unit identified as "RÁDIO" (AFIS) | — | `_R_TWR` | FIZ, or Class G in the vicinity of the aerodrome | Flight information and alerting — **no control** |
| Flight information unit (FIC) | — | no network position of its own | FIR outside controlled airspace† | Flight information and alerting — **no control** |

\* **The Control Zone appears in two rows on purpose.** Which of the two units has jurisdiction over a CTR varies by location: Art. 34 of ICA 100-37 allows the Approach Control Service to be provided by an APP or by an ACC or TWR to which the function has been delegated[^1] — and it is this delegation, published per aerodrome, that decides the case. This does not contradict Art. 37, cited in the following section: in each actual CTR, **only one** of the two has it. Which one, at that aerodrome, is in the AIP-Brasil and in the portal's [**Operational Manuals**](../../../MOP/aerodromos/index.en.md) section.

† **This cell is this manual's reading, not regulatory text.** ICA 100-37 names the Flight Information Center – FIC (Arts. 758 and 856-A)[^1], but at no point delimits the airspace under its responsibility, as it does for the ACC, the APP and the TWR. The cell's value is an inference from three provisions of ICA 100-37 itself: Art. 15, under which "Flight Information Regions are the portions of airspace where Flight Information and Alerting Services are provided"[^1]; Art. 38, which assigns these two services to the "ATS unit having jurisdiction in the airspace concerned"[^1]; and Art. 37, under which "only one air traffic control unit shall have jurisdiction over a given airspace"[^1] — hence the portion of the FIR left over outside the control areas and zones. Where there is a control unit, it is the one that also provides flight information and alerting, under the same Art. 38.

**The last two rows are the units that do not control**, and that is why they are here: a controller who takes one of them needs to know that the authority it carries is different.

- The ATS unit identified as **"RÁDIO"** is the one that normally provides AFIS — the Aerodrome Flight Information Service (Art. 783 of ICA 100-37)[^1]. The sole paragraph of the same article defines exactly what it provides: "This ATS unit provides the Flight Information Service and, additionally, the Alerting Service to all traffic operating on the movement area of the aerodrome and to all aircraft in flight in Class G airspace in its vicinity"[^1]. AFIS is normally provided within a Flight Information Zone – FIZ, published in the AIP-Brasil (Art. 786)[^1]; where no FIZ is published, Art. 787 extends the service to the movement area and to all aircraft in flight in Class G below FL 145 and within a radius of 27 NM (50 km) of the aerodrome[^1]. In the FIZ "no Air Traffic Control Service is provided and, therefore, air traffic control clearances should not be expected" (Art. 786, § 1)[^1]. At Vatsim Brasil, these positions use the `_R_TWR` suffix — the `_R_` is the RÁDIO marker, and the `_TWR` suffix is only the connection format, not a Control Tower; the pages for each aerodrome in the [**Operational Manuals**](../../../MOP/aerodromos/index.en.md) section give the callsign and frequency.
- The **flight information unit** is a category of its own, not a type of control unit: Annex VII of ICA 100-12 defines ATS unit as the "generic term meaning, as the case may be, an air traffic control unit **or a flight information unit**"[^2]. ICA 100-37 names one such unit alongside the ACC — the Flight Information Center – FIC (Arts. 758 and 856-A)[^1]. At Vatsim Brasil there is no position of its own for it: in airspace outside the control areas, the unit that answers is the one with jurisdiction, under Art. 38 of ICA 100-37[^1] — in practice, the connected `_CTR`.

On the radio, these two units are the ones the [VFR Phraseology Manual](../fraseologia-voo-visual/conceitos.en.md) identifies as **INFORMAÇÃO** and **RÁDIO**, and whose rule it sums up in one line: they inform, pass on conditions and answer with CIENTE (roger) — they do not control.

The "typical airspace" column still mixes two registers worth separating. For the ACC, the APP and the TWR's "Control Tower" row, it indicates jurisdiction over airspace as ICA 100-37 and ICA 100-12 define it: UTA, CTA and TMA are the three kinds of Control Area, in the division established by items I, II and III of Art. 17 of ICA 100-37[^1]; a CTR is, according to Annex VII of ICA 100-12, "controlled airspace extending upwards from the surface of the earth to a specified upper limit"[^2]; and an ATZ is the airspace around an aerodrome with "special requirements for the protection of traffic", according to Art. 19 of ICA 100-37[^1] — all already covered in chapter 01. For the "Ground Control" and "Traffic Clearance" rows — the other two internal positions of the same TWR —, it indicates the physical area of the aerodrome where each one usually operates: the Maneuvering Area, defined by Annex VII of ICA 100-12 as the "part of an aerodrome to be used for the take-off, landing and taxiing of aircraft, excluding aprons"[^2], is Ground Control's jurisdiction — but only "with the exception of runways", according to Art. 509 of ICA 100-37[^1], which remain with the Control Tower position; and the Apron, which the same Annex VII of ICA 100-12 defines as a "defined area (...) intended to accommodate aircraft for purposes of loading or unloading passengers, mail or cargo, fueling, parking or maintenance"[^2], is where Traffic Clearance normally talks to the aircraft, before it requests push-back or taxi.

## Jurisdiction

Two rules of ICA 100-37 settle the question of how far each position extends. Art. 37 of ICA 100-37 is direct: "Only one air traffic control unit shall have jurisdiction over a given airspace"[^1]. Art. 36 of ICA 100-37 closes the other side: "A controlled aircraft shall be under the control of only one air traffic control unit"[^1].

Notice what the two articles say and what they do not. They set a **ceiling**, not a floor: "only one" means *at most* one, not *at least* one. There is no overlap of authority — never two control units over the same airspace, never two over the same controlled aircraft. But airspace without any air traffic control unit does exist, and it is the rule in [Class G](02-classes.en.md#classe-g), where the Air Traffic Control Service is not provided — as the *Top-down coverage* section, below, discusses again. The same principle of exclusivity applies to the Flight Information Service and the Alerting Service: Art. 38 of ICA 100-37 assigns their provision to the "ATS unit having jurisdiction in the airspace concerned"[^1] — and these two services, unlike control, exist throughout the FIR (Art. 32 of ICA 100-37)[^1].

This jurisdiction has two dimensions — lateral and vertical —, and Art. 839 of ICA 100-37 names them separately when dealing with the boundary between ACC and APP: transfer of control of arriving aircraft takes place "when crossing the lateral limit of the TMA at the established reporting points" or "when crossing the vertical limit of the TMA"[^1]. Lateral is the geographic boundary — where a TMA, a CTR or an ATZ ends on the map; vertical is the level or altitude at which one unit's jurisdiction gives way to another's. The actual limits of each FIR, TMA, CTR and ATZ — the numbers — are published in the AIP-Brasil and on the charts, as already noted in chapter 01; ICA 100-37 sets the principle, not the coordinate.

Nor is jurisdiction presumed: Art. 822 of ICA 100-37 prohibits "an aircraft under the control of one unit, or control position, from entering airspace under the jurisdiction of another unit, or control position, before coordination has been completed"[^1]. Crossing the boundary without prior coordination is not just a lapse in etiquette — it is the aircraft operating, for a moment, under nobody's responsibility.

## *Top-down* coverage

What ICA 100-37 and ICA 100-12 do not provide for — because it is not the subject of either — is what happens when a real-world unit simply has nobody connected on the network at that moment. This gap is resolved by a VATSIM network convention — of the whole network, not of Vatsim Brasil —, with no basis in ICA 100-37 or ICA 100-12: *top-down* coverage.

The idea is simple: if the higher position in the chain is connected and the lower one is not, the higher one informally takes responsibility for the lower one's airspace. A CTR connected with no APP or TWR below it covers the TMA, the CTR — in the sense of Control Zone — and the ATZ of the aerodromes in that airspace; an APP connected without a TWR covers the tower. The practical consequence, on the pilot's side, is that they call a single frequency from start to finish — that of the highest position connected — without needing to know in advance which intermediate positions exist or are empty at that moment.

It bears repeating: this is an operational convenience of the simulation, not an ICA 100-37 rule. In real life, airspace without a designated unit does not become automatically covered by whoever is "above" it — ICA 100-37 resolves the absence differently, assigning the Flight Information Service and the Alerting Service to the unit having jurisdiction, under the aforementioned Art. 38[^1], rather than opening a coverage exception.

## Transfer between units

A complete flight typically passes through all the **control positions** in the table — the first five rows —, in the order in which ICA 100-37 regulates coordination between them: for departure, from Traffic Clearance to the Area Control Center; for arrival, the reverse path. The last two rows, which do not control, are outside this chain.

On departure, the pilot calls Traffic Clearance, Ground Control or the Control Tower "in the order of precedence presented" for the Flight Plan clearance (Art. 686 of ICA 100-37)[^1]; once that clearance is obtained, they call the Ground Control or Control Tower position, "in this order of precedence", for push-back, engine start and taxi clearances (Art. 687 of ICA 100-37)[^1]. After takeoff, Art. 849 of ICA 100-37 requires control to be transferred from the TWR to the APP "immediately after takeoff" or, when this does not occur earlier, "before [the aircraft] enter instrument meteorological conditions"[^1]. From APP to ACC, Art. 840 of ICA 100-37 sets the transfer of departing aircraft when crossing the lateral or vertical limit of the TMA, or at a point and time previously agreed between the units[^1].

On arrival, the chain runs in reverse. Art. 839 of ICA 100-37 sets the transfer from ACC to APP when crossing the lateral or vertical limit of the TMA, or at a point agreed between the units[^1]; Art. 844 of ICA 100-37 keeps control with the APP "until [the aircraft] are transferred to the TWR and are in communication with it"[^1], a transfer which, under Art. 848 of ICA 100-37, takes place when the aircraft is "in the vicinity of the aerodrome" and able to complete the approach and landing by visual reference, or has already landed[^1]; and, within the TWR itself, Art. 853 of ICA 100-37 passes the aircraft from the Tower position to Ground Control after it "receives from 'Tower' the landing time and clearance to vacate the runway in use"[^1]. Coordination between positions of the same unit follows its own rule, separate from coordination between distinct units, according to Art. 852 of ICA 100-37[^1].

On arrival only, ICA 100-37 itself provides a shortcut: VFR flights may be transferred directly between ACC and TWR, bypassing the APP, provided this is coordinated with it — as stated, each in its own Subsection, by the sole paragraph of Art. 839 and the sole paragraph of Art. 848, both of ICA 100-37[^1]. There is no equivalent provision for departure: neither Art. 840 nor Art. 849 of ICA 100-37 has a paragraph with this shortcut[^1] — on departure, the complete chain, link by link, is the rule, without the exception that arrival allows. The sequence described above is therefore the typical path; the only documented deviation is the VFR arrival.

### Transfer chain at a glance

<figure>
<svg viewBox="0 0 720 240" role="img" aria-label="Chain of control units, from DEL to CTR, with the airspace of each link and the direction of top-down coverage. The non-controlling positions, RÁDIO and flight information, are not part of this chain" style="max-width:100%;height:auto">
  <style>
    .or-bg  { fill: var(--md-default-bg-color); }
    .or-box { fill: #e3f2fd; stroke: #1565c0; stroke-width: 1.5; }
    .or-ttl { fill: #0d47a1; font: 600 14px "Ubuntu Sans", sans-serif; text-anchor: middle; }
    .or-sub { fill: #37474f; font: 400 11px "Ubuntu Sans", sans-serif; text-anchor: middle; }
    .or-arw { stroke: #546e7a; stroke-width: 2; fill: none; marker-end: url(#or-head); }
    .or-td  { fill: #546e7a; font: 400 11px "Ubuntu Sans", sans-serif; }
    .or-hd  { fill: #546e7a; }
    @media (prefers-color-scheme: dark) {
      .or-box { fill: #102a43; stroke: #64b5f6; }
      .or-ttl { fill: #90caf9; } .or-sub { fill: #cfd8dc; }
      .or-arw { stroke: #b0bec5; } .or-td { fill: #b0bec5; } .or-hd { fill: #b0bec5; }
    }
    [data-md-color-scheme="slate"] .or-box { fill: #102a43; stroke: #64b5f6; }
    [data-md-color-scheme="slate"] .or-ttl { fill: #90caf9; }
    [data-md-color-scheme="slate"] .or-sub { fill: #cfd8dc; }
    [data-md-color-scheme="slate"] .or-arw { stroke: #b0bec5; }
    [data-md-color-scheme="slate"] .or-td  { fill: #b0bec5; }
    [data-md-color-scheme="slate"] .or-hd  { fill: #b0bec5; }
    [data-md-color-scheme="default"] .or-box { fill: #e3f2fd; stroke: #1565c0; }
    [data-md-color-scheme="default"] .or-ttl { fill: #0d47a1; }
    [data-md-color-scheme="default"] .or-sub { fill: #37474f; }
    [data-md-color-scheme="default"] .or-arw { stroke: #546e7a; }
    [data-md-color-scheme="default"] .or-td  { fill: #546e7a; }
    [data-md-color-scheme="default"] .or-hd  { fill: #546e7a; }
  </style>
  <defs>
    <marker id="or-head" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path class="or-hd" d="M 0 0 L 10 5 L 0 10 z"/>
    </marker>
  </defs>
  <rect class="or-bg" x="0" y="0" width="720" height="240"/>
  <text class="or-td" x="360" y="26" text-anchor="middle">Top-down coverage (network convention, reverse direction)</text>
  <path class="or-arw" d="M 640 40 L 80 40"/>
  <rect class="or-box" x="20" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="80" y="112">DEL</text>
  <text class="or-sub" x="80" y="134">Apron</text>
  <rect class="or-box" x="160" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="220" y="112">GND</text>
  <text class="or-sub" x="220" y="134">Maneuvering area</text>
  <rect class="or-box" x="300" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="360" y="110">TWR</text>
  <text class="or-sub" x="360" y="128">ATZ and</text>
  <text class="or-sub" x="360" y="142">Control Zone</text>
  <rect class="or-box" x="440" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="500" y="110">APP</text>
  <text class="or-sub" x="500" y="128">TMA and</text>
  <text class="or-sub" x="500" y="142">Control Zone</text>
  <rect class="or-box" x="580" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="640" y="110">CTR</text>
  <text class="or-sub" x="640" y="128">CTA, UTA and</text>
  <text class="or-sub" x="640" y="142">rest of the FIR</text>
  <path class="or-arw" d="M 140 120 L 158 120"/>
  <path class="or-arw" d="M 280 120 L 298 120"/>
  <path class="or-arw" d="M 420 120 L 438 120"/>
  <path class="or-arw" d="M 560 120 L 578 120"/>
</svg>
<figcaption>Normal sequence of an IFR flight between the <strong>control</strong> units. In the diagram, <code>CTR</code> appears only once and names the ACC's network position; the Control Zone is written out in full, so as not to confuse the two meanings of the acronym. <em>Top-down</em> coverage runs in the reverse direction: the higher position answers for the airspace of the lower ones that are not connected. The non-controlling positions — RÁDIO (AFIS) and flight information — are left out of the diagram on purpose: they neither receive nor transfer control, because there is no control to transfer. It follows, as this manual's reading and not as regulatory text, that a flight departing from an aerodrome with AFIS enters the chain at the link of the control unit having jurisdiction over the airspace ahead, not at the TWR — there is no TWR there, and the RÁDIO unit has nothing to transfer.</figcaption>
</figure>

!!! tip "On the network (Vatbrz)"
    Before connecting, check who is already online. If the CTR is connected and you take the APP, part of the airspace that was under *top-down* coverage becomes yours — and the transfer of traffic already on frequency needs to be coordinated, not presumed.

## Callsigns

This chapter dealt with jurisdiction and airspace — who has authority over what, and how far. It did not deal with radiotelephony: how each unit identifies itself on the air is the subject of another manual. The [VFR Phraseology Manual](../fraseologia-voo-visual/conceitos.en.md) already gathers, in a single table, the callsign of each unit in Portuguese, English and Spanish; the [Aeronautical Phraseology Manual](../fraseologia-aeronautica/index.en.md) shows these callsigns in use, in complete communication examples. For "what it is called", start there — this chapter answered "who it is" and "how far it goes".

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37) (*Air Traffic Services*): regulates in Brazil the Air Traffic Services provided for in ICAO Annex 11 and Doc 4444. Edition in force on 27 Nov 2025.
[^2]: [**ICA 100-12, Regras do Ar**](https://publicacoes.decea.mil.br/publicacao/ica-100-12) (*Rules of the Air*): sets out the rules applicable to the operation of aircraft in Brazilian airspace. Edition in force on 28 Nov 2024.
