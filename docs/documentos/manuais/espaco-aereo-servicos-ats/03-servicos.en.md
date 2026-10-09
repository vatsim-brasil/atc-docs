---
title: Air Traffic Services
icon: material/headset
---

--8<-- "includes/abreviacoes.md"

# Air Traffic Services

## The air traffic services

Air Traffic Service is, first of all, a generic name. Item LXXXIV of Annex VII of ICA 100-12 defines the expression as the one that "applies, as the case may be, to the flight information, alerting, air traffic advisory and air traffic control services (area control, approach control or aerodrome control)"[^2]. These are four distinct services, not one, and none of them is provided automatically just because there is an ATS unit on the frequency — what is provided depends on the class of airspace in which the aircraft is operating, a subject already covered in the previous chapter.

ICA 100-37 itself confirms the list from the side of how the services are divided: Art. 28 lists the "Air Traffic Control Service, comprising the Area Control Service, the Approach Control Service and the Aerodrome Control Service", the "Flight Information Service" and the "Alerting Service"[^1]. The Air Traffic Advisory Service is left out of that list for an explicit reason, given in the sole paragraph of the same article: it "is not mentioned in this Section because it is planned as a transition to the implementation of the Air Traffic Control Service"[^1] — an absence in the wording, not in existence, as the previous chapter already noted when discussing Class F.

This chapter covers all four, in the order in which ICA 100-37 organizes them: control, flight information, alerting and, finally, advisory, whose temporary nature calls for separate treatment.

## Air Traffic Control Service

Annex VII of ICA 100-12 defines the Air Traffic Control Service by what it exists to prevent: a service provided for the purpose of "preventing collisions: between aircraft; and between aircraft and obstacles on the maneuvering area" and of "expediting and maintaining an orderly flow of air traffic"[^2]. ICA 100-37 details the same objective from the operational side — to provide the service, an ATC unit shall "have information on the intended movement of each aircraft, or variations thereof, and current data on the actual progress of each one", determine the relative positions of known aircraft, "issue clearances and information for the purpose of preventing collision between aircraft under its control and of expediting and maintaining an orderly flow of traffic" and coordinate these clearances with other units involved (Art. 30)[^1].

This objective has an explicit limit. Art. 93 of ICA 100-37 states that "the objectives of the Air Traffic Control Service do not include the prevention of collision with the ground", and the sole paragraph of the same article adds that this does not exempt the pilot from ensuring that the clearance received is safe in that respect, except when the IFR flight is being vectored[^1] — that is, when, "under vectoring", the controller assumes responsibility for the aircraft's navigation and transmits the necessary heading instructions and level changes (Art. 921 of ICA 100-37)[^1]. Vectoring itself is outside the scope of this manual, as the [introduction](index.en.md#fora-do-escopo) notes. Preventing collision between aircraft and organizing the flow — not preventing collision with terrain — is what the Air Traffic Control Service promises.

Art. 28 of ICA 100-37 divides the service into three, each provided by a different unit[^1]:

- **Area Control Service**, provided by an ACC or by an APP that has been delegated the responsibility of providing it within a given airspace (Art. 33)[^1];
- **Approach Control Service**, provided by an APP or by an ACC or TWR that has been delegated the responsibility (Art. 34)[^1];
- **Aerodrome Control Service**, provided by a TWR that has been delegated the responsibility of providing it within a given airspace (Art. 35)[^1].

How these three services are distributed among the Vatsim Brasil ATS units — ACC, APP, TWR — is the subject of the next chapter.

On the pilot's side, the counterpart of control is the clearance. ICA 100-12 requires that, "before operating a controlled flight, or a portion of a controlled flight", a clearance be obtained from the ATC unit, requested by submitting the Flight Plan (Art. 77)[^2]. It is this pair — a clearance issued on one side, required on the other — that distinguishes control from the other services covered below.

## Flight Information Service

The Flight Information Service has a different objective. Annex VII of ICA 100-12 defines it as the service "provided for the purpose of giving advice and information useful for the safe and efficient conduct of flights"[^2] — to advise and inform, not to decide on behalf of whoever is flying.

ICA 100-37 establishes to whom it is provided: to all aircraft operating in airspace under Brazilian jurisdiction that maintain two-way communication with an ATS unit, or that request it (Art. 741)[^1]. The minimum content includes SIGMET and AIRMET, information on volcanic ash cloud activity, on the release into the atmosphere of radioactive material or toxic chemicals, on changes in the operational status of navigation aids and aerodromes, on unmanned free balloons and any other information "considered important for the safety of air navigation" (Art. 744)[^1]. Added to this are the reported or forecast weather conditions at the departure, destination and alternate aerodromes, and information on collision hazards for aircraft operating in Classes C, D, E, F and G — with the caveat that this information "includes only known aircraft" and is "sometimes inaccurate or incomplete" (Art. 745)[^1]. For VFR flights in particular, the service also includes information on weather conditions along the route that may make flight under visual flight rules impracticable (Art. 747)[^1].

None of this replaces the pilot. Art. 742 of ICA 100-37 explicitly states that the Flight Information Service "does not exempt the pilot from their responsibilities, and it is solely up to the pilot to make any decision regarding changes to the Flight Plan and other measures that seem appropriate for the greater safety of the flight"[^1]. And when the same unit provides both flight information and air traffic control at the same time, control takes precedence (Art. 743)[^1] — confirmation, from the regulatory side, that these are services of a different nature, not two names for the same thing.

## Alerting Service

Annex VII of ICA 100-12 defines the Alerting Service as the service "provided to notify appropriate organizations regarding aircraft in need of search and rescue aid, and to assist such organizations as required"[^2] — it is the service that triggers search and rescue, not the one that prevents the accident.

Unlike control and flight information, the Alerting Service does not depend on the class of airspace. Art. 32 of ICA 100-37 requires that it — together with the Flight Information Service — be provided "in all Flight Information Regions under Brazilian jurisdiction"[^1], and Art. 38 assigns its provision to the ATS unit that has jurisdiction over the airspace concerned[^1]. What triggers it is one of three conditions, set out in Art. 795 of ICA 100-37: the aircraft "is receiving the Air Traffic Control Service"; or "has filed a Flight Plan and its departure has been notified to an ATS unit"; or "is known or suspected to be the subject of unlawful interference"[^1].

The responsibility for initiating the service in an emergency falls on whoever first becomes aware of it. Art. 797 of ICA 100-37 assigns this responsibility to the "TWR, APP or RDO (radio) that becomes aware of an emergency in VFR or IFR flight", with the duty to immediately notify the corresponding ACC and ARCC[^1]. If a destination aerodrome without an ATS unit does not confirm the arrival of an aircraft that filed a Flight Plan, it is up to the ATS unit that notified the departure to inform the ACC (Art. 796)[^1] — and, in this case, with no ATS unit at the destination, the Alerting Service is only provided "if requested by the pilot, the operator or any other person", except for the situations in Arts. 797 and 798 (Art. 796, sole paragraph)[^1].

## Air Traffic Advisory Service

The Air Traffic Advisory Service is the fourth service, and the previous chapter already covered it in depth when describing Class F. Art. 778 of ICA 100-37 explains that it exists to make "information on collision hazards more effective than through the mere provision of the Flight Information Service", and it is provided to aircraft conducting IFR flights in advisory airspace or on advisory routes — Class F[^1]. It does not provide the same degree of safety as control, because the traffic information available to the ATS unit there "may be incomplete" (Art. 779)[^1], and for that reason the Flight Plan and its changes are not subject to clearance: the unit only suggests, by means of traffic information and traffic avoidance advice, and the pilot decides (Art. 780)[^1].

What this chapter adds is what Class F already signals: this is a transitional measure. Art. 21 § 2 of ICA 100-37 classifies the use of the Air Traffic Advisory Service as "a temporary measure until such time as it can be replaced by the Air Traffic Control Service"[^1] — which is also why Art. 28, when dividing the Air Traffic Services in the earlier section of this chapter, does not include it.

For details on to whom it is provided, what it guarantees and why the Flight Information Service reaches IFR and VFR flights in different ways in Class F, see [Airspace Classes, Class F section](02-classes.en.md#classe-f).

## Which service in which class

The table below cross-references the four services with the seven airspace classes. The **Air Traffic Control** and **Air Traffic Advisory** columns follow the matrix in Annex II of ICA 100-37[^1], already reproduced in the previous chapter; the **Flight Information** and **Alerting** columns follow the articles that establish the scope of those two services, not Annex II. The reason lies in the nature of the Annex: it lists the services that *define* each class, not all the services provided there. Reading the matrix as if it exhausted the services provided is the mistake this table exists to prevent. The breakdown by type of flight (IFR/VFR), the separation and the traffic information accompanying each cell are in the [consolidated table in chapter 02](02-classes.en.md#tabela-consolidada-anexo-ii-da-ica-100-37).

| Class | Air Traffic Control | Flight Information | Air Traffic Advisory | Alerting |
| --- | --- | --- | --- | --- |
| **A** | Yes | Yes | No | Yes |
| **B** | Yes | Yes | No | Yes |
| **C** | Yes | Yes | No | Yes |
| **D** | Yes | Yes | No | Yes |
| **E** | Yes, IFR only | Yes — and it is the service Annex II assigns to VFR flights in this class | No | Yes |
| **F** | No | Yes — to IFR flights without the need to request it; to VFR flights, when requested\* | Yes, IFR only | Yes |
| **G** | No | Yes — Annex II assigns it to both types of flight, "when possible and requested by the pilot" | No | Yes |

\* The asymmetry in Class F is the application of Art. 741 of ICA 100-37, above: IFR flights are required by Annex II to maintain continuous two-way communication, and therefore receive the Flight Information Service under subsection I, without having to request it; VFR flights have no such obligation — the radio communication column of the F / VFR row reads "No" — and receive it under subsection II, upon request[^1]. Art. 21, subsection VI, letter *c* of the same Instruction guarantees the common floor: any flight in the class that requests it receives it[^1]. Details in [Airspace Classes, Class F section](02-classes.en.md#classe-f).

Notes on reading the table:

- **Why the Flight Information column is "Yes" in every class.** The service is not exclusive to the classes in which Annex II names it. Art. 32 of ICA 100-37 requires the Flight Information and Alerting Services to be provided "in all Flight Information Regions under Brazilian jurisdiction"[^1] — and, under Art. 19, sole paragraph, of the same Instruction, Control Areas, Control Zones and ATZs lie *within* the FIR[^1]. Art. 741 confirms this from the recipient's side: the service is provided to all aircraft in airspace under Brazilian jurisdiction that maintain two-way communication with an ATS unit or that request it[^1]. And Art. 743 presupposes exactly this coexistence: when a unit provides both at the same time, control takes precedence over flight information[^1] — precedence between simultaneous services, not the exclusion of one of them.
- **The content confirms the scope.** Art. 745, subsection II, of ICA 100-37 includes in the Flight Information Service information on collision hazards for aircraft operating in Classes C, D, E, F and G[^1]; and the information in Art. 744 — SIGMET and AIRMET, volcanic ash, changes in the status of navigation aids and aerodromes, unmanned free balloons — is not restricted by class[^1]. A flight in Class A receives SIGMET through the Flight Information Service, not through the Air Traffic Control Service.
- **What changes between classes, then, is not whether the service exists, but its role.** In Classes A to D the service that defines the class is control, and flight information accompanies it; in Classes E (VFR), F and G flight information is what the pilot has, because there is no control to turn to. That difference is what the Air Traffic Control column records.
- In Classes C and D, Annex II of ICA 100-37 lists "traffic information" as a specific item for VFR flights — an element of information built into the class's own Air Traffic Control Service, and distinct from the Flight Information Service discussed in the notes above[^1]. See the consolidated table and the notes in chapter 02 for the exact wording for each class.
- The Alerting Service, like flight information, is not conditioned on the airspace class — same Art. 32[^1] — and is triggered whenever one of the three conditions of Art. 795 of ICA 100-37 is met[^1], covered in the previous section.
- For the breakdown by type of flight (IFR/VFR) within each class — including the separation provided — see the [consolidated table in chapter 02](02-classes.en.md#tabela-consolidada-anexo-ii-da-ica-100-37).

## Informing is not controlling

!!! danger "Informing is not controlling"
    The Flight Information Service does **not** separate aircraft and does **not** issue clearances. Whoever provides only flight information does not use verbs that imply control — "climb", "descend", "maintain", "cleared". They inform, pass on conditions and respond with **CIENTE** (*roger*).

    When relaying a clearance issued by an ATC unit, they must make it clear who issued the clearance.

The basis for this rule lies in the very definition of the two services, side by side in Annex VII of ICA 100-12: the Air Traffic Control Service exists to "prevent collisions" and to "expedite and maintain an orderly flow of air traffic"[^2], which it does by issuing "clearances and information for the purpose of preventing collision between aircraft under its control and of expediting and maintaining an orderly flow of traffic" (Art. 30, III, of ICA 100-37)[^1]; the Flight Information Service exists to "give useful advice and information"[^2]. The contrast becomes even clearer in Section IX of ICA 100-37, titled "Clearances and instructions from ATC units": it is by means of clearances **and instructions** that ATC units provide the separation required in each class (Art. 39)[^1] — a tool the regulation reserves for the control unit. No article of ICA 100-37 grants the Flight Information Service the power to issue clearances or to separate aircraft — that competence belongs to the Air Traffic Control Service (Art. 30, III, and Art. 39, both of ICA 100-37)[^1].

The most concrete case of this boundary is AFIS, the Aerodrome Flight Information Service, normally provided by an ATS unit identified as "RÁDIO" (Art. 783 of ICA 100-37)[^1]. ICA 100-37 itself warns: within the Flight Information Zone (FIZ) where AFIS is provided, "there is no provision of Air Traffic Control Service and, therefore, air traffic control clearances should not be expected" (Art. 786, § 1)[^1]. What the RÁDIO unit transmits to aircraft includes, among the basic items of information, "messages, including clearances, received from other ATS units for relay to the aircraft" (Art. 788, VII)[^1] — in other words, the only clearance that goes over the RÁDIO frequency is a clearance from another unit, merely relayed. It is exactly this relay that the box above calls for: making it clear who issued the clearance, because the one speaking is not the one who cleared.

This box reinforces, with the regulatory basis, what the [VFR Phraseology Manual](../fraseologia-voo-visual/conceitos.en.md) already practices on the radio.

!!! tip "On the network (Vatbrz)"
    Not every position connected to the network provides the Air Traffic Control Service. The control positions — `_DEL`, `_GND`, `_TWR`, `_APP` and `_CTR` — provide it to the four recipients listed in Art. 29 of ICA 100-37: all IFR flights in Classes A, B, C, D and E; all VFR flights in Classes B, C and D; all Special VFR flights; and all aerodrome traffic at controlled aerodromes[^1]. Note that only the first two subsections are defined by class — Special VFR and aerodrome traffic at a controlled aerodrome are included for what they are, not for where they are, and the ATZ, incidentally, has no class at all (NOTE 2 of Annex II)[^1]. **RÁDIO** positions (`_R_TWR`), which operate AFIS, do not provide it: in the FIZ "there is no provision of Air Traffic Control Service and, therefore, air traffic control clearances should not be expected" (Art. 786, § 1)[^1].

    And even at a control position the scope has limits. Outside controlled airspace — in Class F or G under *top-down* coverage, for example — what you provide to the pilot is information, not control. Recognizing this boundary is what separates a valid instruction from one you had no authority to issue.

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37) (*Air Traffic Services*): regulates in Brazil the Air Traffic Services provided for in ICAO Annex 11 and Doc 4444. Edition in force since 27 Nov 2025.
[^2]: [**ICA 100-12, Regras do Ar**](https://publicacoes.decea.mil.br/publicacao/ica-100-12) (*Rules of the Air*): establishes the rules applicable to the operation of aircraft in Brazilian airspace. Edition in force since 28 Nov 2024.
