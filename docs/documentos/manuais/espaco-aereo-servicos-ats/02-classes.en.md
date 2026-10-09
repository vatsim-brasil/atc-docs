---
title: Airspace Classes
icon: material/format-list-group
---

--8<-- "includes/abreviacoes.md"

# Airspace Classes

## Why classes exist

The previous chapter answers where you are: FIR, CTA, TMA, CTR, ATZ. The class answers a different question — what applies there. These are independent things: a TMA is an airspace structure; the class of that TMA is a separate attribute, published separately. This chapter deals with the second — what each letter means.

Art. 21 of ICA 100-37 classifies ATS airspaces "alphabetically", from A to G[^1]. Each letter fixes three things at once:

- **who may fly there** — IFR flights only, or IFR and VFR flights;
- **who is separated from whom** — whether the ATC unit provides separation and between which types of flight;
- **what the unit provides** — Air Traffic Control Service, Air Traffic Advisory Service, Flight Information Service, traffic information, or a combination of these.

The alphabetical order is not decorative: it is a scale of restrictiveness. The sole paragraph of Art. 23 of ICA 100-37 states that "Class B airspace shall be considered less restrictive than Class A airspace; Class C less restrictive than Class B, and so on"[^1]. Class A is the most restrictive; G, the least restrictive.

Art. 22 of ICA 100-37 refers the requirements of each class to Annex II of the same Instruction[^1] — speed limit, radiocommunication and subjection to ATC clearance. That is the table reproduced later in this chapter.

Two cross-readings of ICA 100-37 itself confirm the matrix and help to memorize it:

- Art. 29 lists to whom the Air Traffic Control Service is provided: "all IFR flights in Class A, B, C, D and E airspaces", "all VFR flights in Class B, C and D airspaces", all Special VFR flights and all aerodrome traffic at controlled aerodromes[^1];
- § 1 of Art. 114 says that "ATC is required to provide separation between IFR flights in Class A to E airspace, and between IFR and VFR flights in Classes B and C", and § 2 adds that "ATC is not required to provide separation between VFR flights, except within Class B airspace"[^1].

## The seven classes

The text below follows Art. 21 of ICA 100-37, item by item[^1].

### Class A

- **only IFR flights** are permitted;
- all flights are provided with **Air Traffic Control Service**;
- **they are separated from each other**.

There is no VFR flight in Class A. Since all flights there are IFR and all are separated from each other, Art. 21 does not provide for traffic information as a service of the class — separation already takes care of it.

### Class B

- **IFR and VFR flights** are permitted;
- all flights are provided with **Air Traffic Control Service**;
- **they are separated from each other**.

"Separated from each other" here covers every combination: IFR from IFR, IFR from VFR and VFR from VFR. Class B is the only airspace in which ATC separates VFR from VFR — § 2 of Art. 114 of ICA 100-37 explicitly makes an exception for Class B from the general rule that separation between VFR flights is not required[^1].

### Class C

- **IFR and VFR flights** are permitted;
- all flights are provided with **Air Traffic Control Service**;
- **IFR flights are separated from other IFR flights and from VFR flights**;
- **VFR flights are separated only from IFR flights** and receive traffic information in respect of other VFR flights and, in addition, traffic avoidance advice, when requested by the pilot.

This is the first class in which separation stops being universal. A VFR flight in Class C is separated from IFR, but not from another VFR: in respect of the latter, it receives traffic information, and traffic avoidance advice comes only if the pilot asks for it.

### Class D

- **IFR and VFR flights** are permitted;
- all flights are provided with **Air Traffic Control Service**;
- **IFR flights are separated from other IFR flights** and receive traffic information in respect of VFR flights and, in addition, traffic avoidance advice, when requested by the pilot;
- **VFR flights receive only traffic information** in respect of all other flights and traffic avoidance advice, when requested by the pilot.

Point of attention: in Class D a VFR flight **is still a controlled flight** — it receives Air Traffic Control Service (sub-item b of item IV), is recorded as such in Annex II and is among the VFR flights listed in Art. 29, II of ICA 100-37[^1]. What it does **not** receive is separation: neither from IFR nor from another VFR. The "only" in sub-item d refers to what it receives in terms of separation and information, not to the existence of the control service.

### Class E

- **IFR and VFR flights** are permitted;
- Air Traffic Control Service is provided **only to IFR flights**, and **these are separated from other IFR flights**;
- **all flights receive traffic information, when practicable**.

Class E is the boundary: IFR is controlled and separated from other IFR; VFR is not controlled, needs neither ATC clearance nor continuous two-way communication, and both receive traffic information only *when practicable*. Art. 115 of ICA 100-12 says the same from the pilot's side: in Class E, F and G ATS airspaces, "VFR flights are not subject to air traffic control clearance, receiving from ATS units only flight information and alerting services"[^2].

### Class F { #classe-f }

- **IFR and VFR flights** are permitted;
- **Air Traffic Advisory Service** is provided **only to IFR flights**;
- **all flights receive Flight Information Service, when requested by the pilot**.

In practice, the operational response is asymmetric, and that is how it should be read at the position: **to an IFR flight in Class F, provide Flight Information Service without waiting for it to ask** — it is continuously on your frequency; **to a VFR flight, provide it when it requests**.

The reason lies in two articles that add up, and the difference between the two Annex II rows is the exact record of this:

- sub-item *c* of item VI of Art. 21 of ICA 100-37 sets a **floor**: "all flights receive Flight Information Service, when requested by the pilot"[^1]. No flight in the class goes without the service if it asks;
- Art. 741 of ICA 100-37 **adds** to that floor: Flight Information Service "shall be provided to all aircraft operating in the airspace under the jurisdiction of Brazil that: I - maintain two-way communication with an ATS unit; **or** II - it is requested by the pilot"[^1]. These are two alternative entry doors, not cumulative ones.

Now look at the radiocommunication column of Annex II for this class: the **F / IFR** row requires "Continuous two-way"; the **F / VFR** row records "No"[^1]. The IFR flight, by requirement of the class itself, is permanently in two-way communication with the ATS unit — it enters through item I of Art. 741 and receives the service without asking. The VFR flight has no such requirement — it enters through item II, upon request. That is why Annex II writes "1) Air Traffic Advisory Service; and 2) Flight Information Service" in the IFR row, without condition, and "Flight Information Service, when requested" in the VFR row[^1]. The two cells state the same rule applied to two different situations; there is no contradiction between them, nor between them and Art. 21.

!!! warning "Do not read the condition in Art. 21 of ICA 100-37 as a ceiling"
    "When requested by the pilot" guarantees the service to whoever asks — it does not **deny** it to whoever did not ask. Treating the condition as a ceiling for an IFR flight in Class F would mean withholding SIGMET, AIRMET, changes in the condition of aerodromes and navigation aids, and the collision hazard information of item II of Art. 745[^1] from an aircraft that is on frequency the whole time. Art. 741, I, exists precisely to prevent that reading.

A caveat in the interest of honesty, so the reader does not generalize: Annex II does **not** derive its entire services column from the radiocommunication column. In Class G the IFR row also requires "Continuous two-way", and yet item VII of Art. 21 of ICA 100-37 makes the service conditional on "when practicable and requested by the pilot"[^1] — there it is the article itself that sets the condition, for availability reasons that NOTE 1 of Annex II spells out. And in Class E the VFR row does not require radio and still receives Flight Information Service without condition[^1]. The reasoning above explains Class F, which is the case in question; it is not a universal key for reading the Annex.

There is no Air Traffic Control Service in Class F. Annex II records the separation for the class as "IFR from IFR, **when practicable**"[^1] — and Art. 779 of ICA 100-37 explains why: Air Traffic Advisory Service "does not afford the same degree of safety nor can it assume the same responsibilities as the Air Traffic Control Service with respect to the prevention of collisions, since the information on traffic in that area available to the ATS unit may be incomplete"[^1]. Item I of Art. 780 adds that, under this service, the Flight Plan and changes to it are not subject to clearances, "since the ATS unit will only provide advice by means of traffic information and traffic avoidance advice"[^1].

### Class G { #classe-g }

- **IFR and VFR flights** are permitted, receiving **only Flight Information Service, when practicable and requested by the pilot**.

There is no control, no advisory service, and Annex II records the separation for the class as "not applicable"[^1]. NOTE 1 of Annex II itself warns that "the provision of Flight Information Service in Class G depends on a number of operational and infrastructure factors, such as traffic demand and coverage area"[^1] — hence the "when practicable".

This does not mean a total absence of traffic information. Item II of Art. 745 of ICA 100-37 includes in the Flight Information Service information regarding "collision hazards to aircraft operating in Class C, D, E, F and G airspaces", with the caveat, in the sole paragraph, that it "includes only known aircraft" and is "sometimes inaccurate or incomplete"[^1].

## Consolidated table — Annex II of ICA 100-37 { #tabela-consolidada-anexo-ii-da-ica-100-37 }

The table below reproduces Annex II of ICA 100-37[^1], which Art. 22 points to as the source of the flight requirements in each class.

| Class | Type of flight | Separation provided | Services and information provided | Speed limit | Radiocommunication | ATC clearance |
| --- | --- | --- | --- | --- | --- | --- |
| **A** | IFR | All aircraft | Air Traffic Control Service | Not applicable | Continuous two-way | Yes |
| **B** | IFR | All aircraft | Air Traffic Control Service | Not applicable | Continuous two-way | Yes |
| **B** | VFR | All aircraft | Air Traffic Control Service | **380 kt IAS** | Continuous two-way | Yes |
| **C** | IFR | IFR from IFR<br>IFR from VFR | Air Traffic Control Service | Not applicable | Continuous two-way | Yes |
| **C** | VFR | VFR from IFR | 1) Air Traffic Control Service for separation from IFR; and<br>2) VFR/VFR traffic information and traffic avoidance advice, when requested by the pilot | **250 kt IAS** below 3,050 m (10,000 ft) AMSL | Continuous two-way | Yes |
| **D** | IFR | IFR from IFR | 1) Air Traffic Control Service; and<br>2) traffic information about VFR flights (and traffic avoidance advice, when requested by the pilot) | **250 kt IAS** below 3,050 m (10,000 ft) AMSL | Continuous two-way | Yes |
| **D** | VFR | Not applicable | 1) Air Traffic Control Service; and<br>2) traffic information between IFR/VFR and VFR/VFR flights (and traffic avoidance advice, when requested by the pilot) | **250 kt IAS** below 3,050 m (10,000 ft) AMSL | Continuous two-way | Yes |
| **E** | IFR | IFR from IFR | 1) Air Traffic Control Service; and<br>2) traffic information about VFR flights when practicable | **250 kt IAS** below 3,050 m (10,000 ft) AMSL | Continuous two-way | Yes |
| **E** | VFR | Not applicable | 1) Flight Information Service; and<br>2) traffic information, when practicable | **250 kt IAS** below 3,050 m (10,000 ft) AMSL | No | No |
| **F** | IFR | IFR from IFR, when practicable | 1) Air Traffic Advisory Service; and<br>2) Flight Information Service | **250 kt IAS** below 3,050 m (10,000 ft) AMSL | Continuous two-way | No |
| **F** | VFR | Not applicable | Flight Information Service, when requested | **250 kt IAS** below 3,050 m (10,000 ft) AMSL | No | No |
| **G** | IFR | Not applicable | Flight Information Service, when practicable and requested by the pilot | **250 kt IAS** below 3,050 m | Continuous two-way | No |
| **G** | VFR | Not applicable | Flight Information Service, when practicable and requested by the pilot | **250 kt IAS** below 3,050 m | No | No |

Notes on reading the table:

- **How to read the blank cells of Annex II.** The rule works in one direction only: **when a cell in the VFR row is blank, it repeats the value of the cell above, within the same class** — or, in some cases, the cell is merged vertically across the two rows, with the same effect. The converse is not true: not every repeated value appears blank. The speed limit in the **D / VFR** row, for example, is the same as in the D / IFR row and yet is written out in both. That a blank means repetition, and not omission, the Annex itself demonstrates by contrast: where the VFR flight **really differs** from the IFR one, the value is always written, as in Class E, whose VFR row shows "No" both for radiocommunication and for subjection to ATC clearance. In the table above the inherited values were written in both rows, for direct reading — by column: **separation** in Classes B and G; **services** in Classes B and G (in G the cell is actually merged and covers IFR and VFR with the same text); **radiocommunication** in Classes B, C and D; **speed limit** in Classes E, F and G; and **ATC clearance** in Classes B, C, D, F and G.
- The radiocommunication and ATC clearance columns of the **D / VFR** row are an application of that convention: Annex II leaves them blank because they repeat the D / IFR row. The reading adopted — continuous two-way and subject to ATC clearance — has, besides the structure of the Annex itself, independent confirmation in two provisions of ICA 100-12: Art. 111, according to which "for VFR flights in Class B, C and D airspaces, aircraft shall be equipped with means to establish radiotelephony communications with the appropriate ATC unit"[^2]; and Art. 115, which exempts from ATC clearance only VFR flights in Classes E, F and G[^2].
- In Class F, both rows show Flight Information Service with different wording — without condition in **F / IFR**, "when requested" in **F / VFR** — and the difference is coherent, not an inconsistency. It follows the radiocommunication column of the same class: the IFR flight is required to maintain continuous two-way communication and therefore receives the service without asking, under item I of Art. 741 of ICA 100-37; the VFR flight has no such obligation and receives it upon request, under item II of the same article[^1]. Sub-item *c* of item VI of Art. 21 of the same Instruction guarantees the floor — any flight in the class that requests it receives it[^1]. See the [Class F section](#classe-f) above. Here, unlike the D / VFR case, there is no blank cell: they are two filled cells, each correct for its type of flight.
- In Class G, Annex II records the limit as "250 kt IAS below 3,050 m", without the conversion to feet that accompanies the other classes. It is the same 10,000 ft AMSL.
- "Continuous two-way" (*Bilateral contínua*), in the radiocommunication column, means continuous two-way communication with the appropriate ATC unit.

## Speed limits for VFR flight { #limites-de-velocidade-para-o-voo-vfr }

This section changes source: the table below is from **ICA 100-12**, not from Annex II of ICA 100-37 covered in the previous section. ICA 100-12 addresses the same subject from the Rules of the Air side. Art. 127 refers to its Table 2, which sets, for flight under visual flight rules[^2]:

| Airspace class | Speed limit |
| --- | --- |
| **B** | 380 kt |
| **C, D, E, F, G** | 250 kt IAS if flying below 3,050 m (10,000 ft) AMSL<br>380 kt IAS if flying at or above 3,050 m (10,000 ft) AMSL |

The sole paragraph of Art. 127 adds that, when the height of the transition altitude is lower than 3,050 m (10,000 ft) AMSL, FL 100 shall be used instead of 10,000 ft[^2]. Class A does not appear in the table because VFR flight is not allowed there.

## Two rules that catch beginners

!!! warning "A Control Zone is not Class E"
    § 1 of Art. 21 of ICA 100-37 prohibits classifying Control Zones as Class E.[^1]

!!! note "Vertically adjacent airspaces"
    When two ATS airspaces are one above the other, a flight at the common level complies with the requirements of, and is provided with the services of, the **less restrictive** class. For this purpose, Class B is less restrictive than A, C less than B, and so on.[^1]

## Pilot responsibility

Art. 24 of ICA 100-37 closes the classification Section with the counterpart of everything that came before: "the pilot in command of an aircraft in VFR or IFR flight shall provide their own separation from other aircraft, if flying in an airspace class in which the ATC unit is not responsible for providing this type of separation"[^1].

ICA 100-12 says the same from the visual flight side. Art. 116 assigns to the pilot in command of an aircraft in VFR flight the responsibility to "provide their own separation from obstacles and other aircraft by visual means, except in Class B airspace, where separation between aircraft is the responsibility of ATC"[^2].

It is the same idea that the [VFR Phraseology Manual](../fraseologia-voo-visual/conceitos.en.md) states as a principle: visual separation is the pilot's responsibility, and that is why the expected response to traffic information is to say whether or not the traffic is in sight. Reading the class matrix is, from the controller's point of view, knowing exactly where that responsibility passes to the other side of the radio.

The caveat applies to both sides: Art. 32 of ICA 100-12 recalls that the rules "do not relieve the pilot in command of the responsibility to take the best action to avoid a collision", and that vigilance on board shall be exercised "regardless of the flight rules or the class of airspace"[^2].

## Air traffic advisory is a temporary measure

§ 2 of Art. 21 of ICA 100-37 classifies Air Traffic Advisory Service — the Class F service — as transitional: "the use of Air Traffic Advisory Service is considered a temporary measure until such time as it can be replaced by Air Traffic Control Service"[^1].

That is why Art. 28 of ICA 100-37, when listing the Air Traffic Services, does not include it, and records in the sole paragraph that advisory service "is not mentioned in this Section because it is planned as a transition to the implementation of Air Traffic Control Service"[^1].

## The matrix at a glance

<figure>
<svg viewBox="0 0 700 300" role="img" aria-label="Matrix of airspace classes A to G against VFR flights permitted, Air Traffic Control Service, separation provided and traffic information" style="max-width:100%;height:auto">
  <style>
    .cl-bg   { fill: var(--md-default-bg-color); }
    .cl-hd   { fill: #263238; font: 600 14px "Ubuntu Sans", sans-serif; text-anchor: middle; }
    .cl-rw   { fill: #263238; font: 400 12px "Ubuntu Sans", sans-serif; }
    .cl-cell { fill: #eceff1; stroke: #90a4ae; stroke-width: 1; }
    .cl-on   { fill: #2e7d32; }
    .cl-part { fill: #f9a825; }
    .cl-off  { fill: #607d8b; }
    .cl-key  { fill: #546e7a; font: 400 11px "Ubuntu Sans", sans-serif; }
    @media (prefers-color-scheme: dark) {
      .cl-hd { fill: #eceff1; } .cl-rw { fill: #eceff1; }
      .cl-cell { fill: #2b303b; stroke: #546e7a; } .cl-off { fill: #90a4ae; }
      .cl-on { fill: #66bb6a; } .cl-part { fill: #ffca28; } .cl-key { fill: #b0bec5; }
    }
    [data-md-color-scheme="slate"] .cl-hd { fill: #eceff1; }
    [data-md-color-scheme="slate"] .cl-rw { fill: #eceff1; }
    [data-md-color-scheme="slate"] .cl-cell { fill: #2b303b; stroke: #546e7a; }
    [data-md-color-scheme="slate"] .cl-off { fill: #90a4ae; }
    [data-md-color-scheme="slate"] .cl-on { fill: #66bb6a; }
    [data-md-color-scheme="slate"] .cl-part { fill: #ffca28; }
    [data-md-color-scheme="slate"] .cl-key { fill: #b0bec5; }
    [data-md-color-scheme="default"] .cl-hd { fill: #263238; }
    [data-md-color-scheme="default"] .cl-rw { fill: #263238; }
    [data-md-color-scheme="default"] .cl-cell { fill: #eceff1; stroke: #90a4ae; }
    [data-md-color-scheme="default"] .cl-off { fill: #607d8b; }
    [data-md-color-scheme="default"] .cl-on { fill: #2e7d32; }
    [data-md-color-scheme="default"] .cl-part { fill: #f9a825; }
    [data-md-color-scheme="default"] .cl-key { fill: #546e7a; }
  </style>
  <rect class="cl-bg" x="0" y="0" width="700" height="300"/>

  <text class="cl-rw" x="20" y="48">Airspace class</text>
  <text class="cl-hd" x="277" y="48">A</text>
  <text class="cl-hd" x="337" y="48">B</text>
  <text class="cl-hd" x="397" y="48">C</text>
  <text class="cl-hd" x="457" y="48">D</text>
  <text class="cl-hd" x="517" y="48">E</text>
  <text class="cl-hd" x="577" y="48">F</text>
  <text class="cl-hd" x="637" y="48">G</text>

  <text class="cl-rw" x="20" y="82">VFR flights permitted</text>
  <rect class="cl-cell" x="260" y="60" width="34" height="34" rx="4"/>
  <rect class="cl-off" x="269" y="75" width="16" height="4" rx="2"/>
  <rect class="cl-cell" x="320" y="60" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="337" cy="77" r="9"/>
  <rect class="cl-cell" x="380" y="60" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="397" cy="77" r="9"/>
  <rect class="cl-cell" x="440" y="60" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="457" cy="77" r="9"/>
  <rect class="cl-cell" x="500" y="60" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="517" cy="77" r="9"/>
  <rect class="cl-cell" x="560" y="60" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="577" cy="77" r="9"/>
  <rect class="cl-cell" x="620" y="60" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="637" cy="77" r="9"/>

  <text class="cl-rw" x="20" y="124">Air Traffic Control</text>
  <text class="cl-rw" x="20" y="138">Service (ATC)</text>
  <rect class="cl-cell" x="260" y="110" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="277" cy="127" r="9"/>
  <rect class="cl-cell" x="320" y="110" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="337" cy="127" r="9"/>
  <rect class="cl-cell" x="380" y="110" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="397" cy="127" r="9"/>
  <rect class="cl-cell" x="440" y="110" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="457" cy="127" r="9"/>
  <rect class="cl-cell" x="500" y="110" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="517,118 526,134 508,134"/>
  <rect class="cl-cell" x="560" y="110" width="34" height="34" rx="4"/>
  <rect class="cl-off" x="569" y="125" width="16" height="4" rx="2"/>
  <rect class="cl-cell" x="620" y="110" width="34" height="34" rx="4"/>
  <rect class="cl-off" x="629" y="125" width="16" height="4" rx="2"/>

  <text class="cl-rw" x="20" y="182">Separation provided</text>
  <rect class="cl-cell" x="260" y="160" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="277" cy="177" r="9"/>
  <rect class="cl-cell" x="320" y="160" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="337" cy="177" r="9"/>
  <rect class="cl-cell" x="380" y="160" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="397,168 406,184 388,184"/>
  <rect class="cl-cell" x="440" y="160" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="457,168 466,184 448,184"/>
  <rect class="cl-cell" x="500" y="160" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="517,168 526,184 508,184"/>
  <rect class="cl-cell" x="560" y="160" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="577,168 586,184 568,184"/>
  <rect class="cl-cell" x="620" y="160" width="34" height="34" rx="4"/>
  <rect class="cl-off" x="629" y="175" width="16" height="4" rx="2"/>

  <text class="cl-rw" x="20" y="232">Traffic information</text>
  <rect class="cl-cell" x="260" y="210" width="34" height="34" rx="4"/>
  <rect class="cl-off" x="269" y="225" width="16" height="4" rx="2"/>
  <rect class="cl-cell" x="320" y="210" width="34" height="34" rx="4"/>
  <rect class="cl-off" x="329" y="225" width="16" height="4" rx="2"/>
  <rect class="cl-cell" x="380" y="210" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="397,218 406,234 388,234"/>
  <rect class="cl-cell" x="440" y="210" width="34" height="34" rx="4"/>
  <circle class="cl-on" cx="457" cy="227" r="9"/>
  <rect class="cl-cell" x="500" y="210" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="517,218 526,234 508,234"/>
  <rect class="cl-cell" x="560" y="210" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="577,218 586,234 568,234"/>
  <rect class="cl-cell" x="620" y="210" width="34" height="34" rx="4"/>
  <polygon class="cl-part" points="637,218 646,234 628,234"/>

  <circle class="cl-on" cx="26" cy="266" r="6"/>
  <text class="cl-key" x="38" y="270">Applies in full</text>
  <polygon class="cl-part" points="196,260 202,270 190,270"/>
  <text class="cl-key" x="208" y="270">Applies in part or conditionally</text>
  <rect class="cl-off" x="452" y="264" width="14" height="4" rx="2"/>
  <text class="cl-key" x="472" y="270">Does not apply</text>
  <text class="cl-key" x="20" y="290">IFR flights are permitted in all seven classes.</text>
</svg>
<figcaption>Green: applies in full, to all flights in the class. Amber: applies only to some of the flights, or conditionally. Gray: does not apply. The full normative wording is in Art. 21 of ICA 100-37. In the traffic information row: in Classes A and B, Art. 21 does not provide for it as a service of the class, because all flights are separated from each other; in Class C it covers only VFR flights, and only in respect of other VFR flights; in Classes F and G it comes conditionally, through the Air Traffic Advisory Service or the Flight Information Service.</figcaption>
</figure>

!!! tip "On the network (Vatbrz)"
    The airspace class changes what you owe the pilot. In Class C you separate IFR from VFR; in Class D you do not separate VFR from anyone, you only give traffic information. Before taking a position, know which class it operates in — the information is in the AIP and in the [**Operational Manuals**](../../../MOP/aerodromos/index.en.md) section of the portal.

!!! note "Which class applies where"
    ICA 100-37 defines what each class means. **Which** class applies to each portion of Brazilian airspace is published in AIP-Brasil, section ENR 1.4, and may change with each AIRAC cycle. Always check [AISWEB](https://aisweb.decea.mil.br/) for the current data.

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37) (*Air Traffic Services*): regulates in Brazil the Air Traffic Services set out in ICAO Annex 11 and Doc 4444. Edition in force since 27 Nov 2025.
[^2]: [**ICA 100-12, Regras do Ar**](https://publicacoes.decea.mil.br/publicacao/ica-100-12) (*Rules of the Air*): establishes the rules applicable to the operation of aircraft in Brazilian airspace. Edition in force since 28 Nov 2024.
