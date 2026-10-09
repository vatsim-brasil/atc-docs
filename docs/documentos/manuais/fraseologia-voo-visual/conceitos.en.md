---
title: Visual Flight Concepts
icon: material/book-open-variant
---

--8<-- "includes/abreviacoes.md"

# Visual Flight Concepts

## What changes in visual flight

In instrument flight, ATC guides the aircraft through published procedures, with detailed clearances and full readbacks. In visual flight the logic is reversed: the pilot **reports what they intend to do** and the ATS unit responds with a clearance, information or a simple acknowledgement, depending on the service provided in that airspace.

Three practical consequences show up on the radio:

1. **The pilot declares intentions.** Expressions such as "request landing instructions", "advise intentions" and "will join downwind" are the heart of VFR communication.
2. **Position replaces procedure.** With no SID and no STAR, the pilot determines their position by visual references, distance, radial or estimated time, and that is how they report it.
3. **Visual separation is the pilot's responsibility.** When ATC reports traffic, the expected response is to confirm whether or not it is in sight.

!!! danger "The golden rule of VFR"
    Maintaining visual conditions is the pilot's obligation. If the weather conditions no longer allow visual flight, **this must be reported immediately** to the ATS unit, together with the pilot's intentions.

## Units you will encounter on a visual flight

| Unit | :flag_br: Portuguese | :flag_gb: English | :flag_es: Spanish | What it does for VFR |
| --- | --- | --- | --- | --- |
| Clearance Delivery | TRÁFEGO (name) | (name) DELIVERY | (nombre) AUTORIZACIÓN | Issues the departure clearance, when the position exists |
| Ground Control | SOLO (name) | (name) GROUND | (nombre) TIERRA | Clears engine start and taxi |
| Control Tower | TORRE (name) | (name) TOWER | (nombre) TORRE | Clears takeoff and landing and organises the traffic circuit |
| Approach Control | CONTROLE (name) | (name) CONTROL | (nombre) CONTROL | Clears entry into, transit through and exit from the CTR and the TMA |
| Area Control Center | CENTRO (name) | (name) CENTER | (nombre) CENTRO | Handles VFR traffic in controlled airspace en route |
| Flight Information Service | INFORMAÇÃO (name) | (name) INFORMATION | (nombre) INFORMACIÓN | Provides flight and traffic information, without controlling |
| Aeronautical Station | RÁDIO (name) | (name) RADIO | (nombre) RADIO | Provides information at the uncontrolled aerodrome, without controlling |

!!! warning "INFORMATION and RADIO do not control"
    The flight information service operator **may not** use imperative verbs that imply air traffic control, such as "climb", "descend", "maintain", "cleared" or "deviate". They inform, relay conditions and respond with **ROGER**.

    When relaying a clearance issued by an ATC unit, they must make it clear who issued the clearance.

    > :flag_br: VICTOR BRAVO ROMEO, **autorizado pelo Centro Brasília** a subir e manter SETE MIL E QUINHENTOS pés. <br/>
    > :flag_gb: VICTOR BRAVO ROMEO, **cleared by Brasília Center** to climb and maintain SEVEN THOUSAND FIVE HUNDRED feet. <br/>
    > :flag_es: VICTOR BRAVO ROMEO, **autorizado por Brasília Centro** a ascender y mantener SIETE MIL QUINIENTOS pies. <br/>

## Callsign and abbreviation

General aviation aircraft normally use their own registration as the callsign, read letter by letter using the phonetic alphabet.

| Registration | Full callsign | Abbreviated callsign |
| --- | --- | --- |
| PT-VBR | PAPA TANGO VICTOR BRAVO ROMEO | VICTOR BRAVO ROMEO |
| PR-MKL | PAPA ROMEO MIKE KILO LIMA | MIKE KILO LIMA |
| PS-ABC | PAPA SIERRA ALFA BRAVO CHARLIE | ALFA BRAVO CHARLIE |

Practical rules:

1. On **initial contact** with each unit, always use the full callsign.
2. Once communication has been established, and provided there is **no possibility of confusion** with other traffic, the callsign may be abbreviated to at least the last three characters.
3. In practice, it is the ATS unit that initiates the abbreviation. If the controller keeps using the full callsign, keep using the full callsign.
4. In coordination between units, the callsign is **never** abbreviated.

## Structure of the initial contact

A well-made VFR initial contact answers four questions, in this order:

| Element | Example |
| --- | --- |
| Who I am calling | Ipatinga Radio |
| Who I am | PAPA TANGO VICTOR BRAVO ROMEO |
| Where I am | from Pampulha, TEN minutes out, southwest, SEVEN THOUSAND FIVE HUNDRED feet |
| What I want | request information |

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Rádio Ipatinga, **PAPA TANGO VICTOR BRAVO ROMEO**, um Cessna 172, procedente de Pampulha, DEZ minutos fora, a sudoeste, SETE MIL E QUINHENTOS pés, solicita informações.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Ipatinga Radio, **PAPA TANGO VICTOR BRAVO ROMEO**, a Cessna 172, from Pampulha, TEN minutes out, southwest, SEVEN THOUSAND FIVE HUNDRED feet, request information.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Ipatinga Radio, **PAPA TANGO VICTOR BRAVO ROMEO**, un Cessna 172, procedente de Pampulha, DIEZ minutos afuera, al suroeste, SIETE MIL QUINIENTOS pies, solicita información.
    </div>

!!! note "Two-step call"
    On busy frequencies it is common and recommended to split the initial contact into two steps: first only the unit and the callsign, and only after the ATS reply the full message. This avoids transmitting a long message over another aircraft.

## Altitudes, the detail that causes the most errors in VFR

VFR cruising levels end in 500 feet, and that is exactly where pronunciation tends to slip. What determines how it is read is the aircraft's position relative to the **transition level**.

!!! note "Convention adopted in this manual"
    All examples assume an aerodrome whose **transition level is 080**. In other words, everything below it is **altitude**, referenced to QNH, and only above it does the reference become **flight level**, referenced to QNE 1013.

    The transition level varies by aerodrome and by the day's pressure. Check the current value before flying or controlling.

### Below the transition level: altitude

The aircraft flies at an altitude, referenced to QNH, and the correct unit is **feet**, never flight level. Here the plain reading in thousands and hundreds is accepted, which is the established form in visual operations.

| Altitude | :flag_br: Portuguese | :flag_gb: English | :flag_es: Spanish |
| --- | --- | --- | --- |
| 1,500 ft | UNO MIL E QUINHENTOS PÉS | ONE THOUSAND FIVE HUNDRED FEET | UN MIL QUINIENTOS PIES |
| 4,500 ft | QUATRO MIL E QUINHENTOS PÉS | FOUR THOUSAND FIVE HUNDRED FEET | CUATRO MIL QUINIENTOS PIES |
| 6,500 ft | MEIA MIL E QUINHENTOS PÉS | SIX THOUSAND FIVE HUNDRED FEET | SEIS MIL QUINIENTOS PIES |
| 7,500 ft | SETE MIL E QUINHENTOS PÉS | SEVEN THOUSAND FIVE HUNDRED FEET | SIETE MIL QUINIENTOS PIES |
| 5,000 ft | CINCO MIL PÉS | FIVE THOUSAND FEET | CINCO MIL PIES |

That is why the example flight in this manual, which cruises at 7,500 and 6,500 feet, never says "flight level".

### Above the transition level: flight level

The reference becomes the **flight level**, transmitted **digit by digit** and always with **three digits**. The leading zero **is part of the level and must be pronounced**.

| Flight level | :flag_br: Portuguese | :flag_gb: English | :flag_es: Spanish |
| --- | --- | --- | --- |
| FL 055 | nível de voo ZERO CINCO CINCO | flight level ZERO FIVE FIVE | nivel de vuelo CERO CINCO CINCO |
| FL 070 | nível de voo ZERO SETE ZERO | flight level ZERO SEVEN ZERO | nivel de vuelo CERO SIETE CERO |
| FL 095 | nível de voo ZERO NOVE CINCO | flight level ZERO NINE FIVE | nivel de vuelo CERO NUEVE CINCO |
| FL 120 | nível de voo UNO DOIS ZERO | flight level ONE TWO ZERO | nivel de vuelo UNO DOS CERO |

!!! danger "Classic mistake: dropping the leading zero"
    Saying "flight level SEVEN ZERO" for FL 070 is wrong and ambiguous, because it opens the door to confusion with FL 700. Always say all three digits: **ZERO SEVEN ZERO**.

!!! tip "The digit-by-digit rule also applies to weather"
    Cloud heights, visibility and RVR always follow **Art. 32 of MCA 100-16**, digit by digit, regardless of the transition level. A 600 ft ceiling is **MEIA ZERO ZERO PÉS** in Portuguese, and a visibility of 700 metres is **SETE ZERO ZERO METROS**.

    If an altitude in feet needs to be transmitted in the strict Art. 32 form, it is also given digit by digit: 7,500 ft becomes **SETE CINCO ZERO ZERO PÉS**, and 3,400 ft becomes **TRÊS QUATRO ZERO ZERO PÉS**.

    Note also that Portuguese breaks the number into digits while English groups it into thousands and hundreds. They are different logics, and mixing the two is one of the most common bad habits on the network.

## Essential circuit vocabulary

| :flag_br: Portuguese | :flag_gb: English | :flag_es: Spanish |
| --- | --- | --- |
| Perna contra o vento | Upwind leg | Tramo contra el viento |
| Través | Crosswind leg | Tramo con viento cruzado |
| Perna do vento | Downwind leg | Tramo con viento en cola |
| Perna base | Base leg | Tramo base |
| Final | Final | Final |
| Final longa | Long final | Final larga |
| Aproximação direta | Straight in approach | Aproximación directa |
| Cruzamento do campo | Crossing the field | Cruce del campo |
| Livre do circuito | Clear of the circuit | Libre del circuito |
| Toque e arremetida | Touch and go | Toque y despegue |
| Pouso completo | Full stop landing | Aterrizaje completo |
| Arremeta em frente | Go around straight ahead | Frustre aproximación en línea recta |
| Arremeta e circule | Go around and circle | Frustre aproximación y circule |
| Alongue a perna do vento | Extend downwind leg | Extienda el tramo con viento en cola |
| Faça 360 graus pela direita | Make a three sixty turn right | Efectúe un viraje de 360 grados por la derecha |
| Trem de pouso baixado e travado | Landing gear down and locked | Tren de aterrizaje abajo y asegurado |
| No solo aos DOIS CINCO | On the ground at TWO FIVE | En tierra a los DOS CINCO |
| Pista livre | Runway vacated | Pista libre |
| Informe intenções | Advise intentions | Informe intenciones |
| A seu critério | At your discretion | A su discreción |
| Ciente | Roger | Recibido |

!!! tip "Further reading"
    The regulatory basis for the services mentioned on this page (what control is, what flight information is, and why INFORMAÇÃO and RÁDIO stations do not control traffic) is in the [Airspace and ATS Services Manual](../espaco-aereo-servicos-ats/03-servicos.en.md).

---
