---
title: Communication Examples
icon: material/microphone
---

--8<-- "includes/abreviacoes.md"

# Communication Examples

For practical purposes, below is an example of a complete flight, from the initial contact with Clearance Delivery, the ATC unit that issues the flight plan clearance, to the contact with Ground at the destination. Consider this example under normal conditions, without any adverse situations.

## :material-numeric-0-box: Preliminaries

<section markdown style="display: grid; grid-template-columns: 5fr 1fr">

<div markdown>
The flowchart alongside shows the sequence of ATC units involved in a typical flight. Communication begins with Clearance Delivery (**DEL**), which issues the flight plan clearance. Next, the pilot contacts Ground (**GND**) to request startup and pushback, as well as taxi to the departure runway. After that, the contact is transferred to the Tower (**TWR**), which clears the aircraft for takeoff. Once airborne, the pilot contacts Approach Control (**APP**) to receive instructions during the flight. Depending on the route, there may be a handoff to the Center (**CTR**). On approach to the destination, the pilot returns to **APP**, then to **TWR** for landing clearance, and finally to **GND** for taxi to the gate.

For practical purposes, we will simulate flight **GLO1489** between Brasília (SBBR) and Guarulhos (SBGR) airports. The communications are presented in Portuguese, English and Spanish, reflecting common practice, without specific phraseology for emergencies or other non-routine situations.

In addition, some supplementary information is available in remarks boxes, highlighting particularities or possible variations of the most common phraseology. Don't forget to check them!

!!! danger "Use of Spanish in phraseology"
    Spanish may only be used in airspace where it is authorised, either by DECEA or by the CAOPs (operational agreements) officially established between Vatsim Brasil and other divisions. By default, **the indiscriminate use of this language in routine aeronautical communication <u>is prohibited</u>**, even if both pilot and ATC are able to use it.

</div>

<div style="text-align: center;">
``` mermaid
flowchart TD
  DEL(DEL);
  DEL --> GND(GND);
  GND --> TWR(TWR);
  TWR --> APP(APP);
  APP --> CTR(CTR);
  CTR --> APP;
  APP --> TWR;
  TWR --> GND;
```
</div>

</section>

## :material-numeric-1-box: :flag_br: Tráfego / :flag_gb: Delivery / :flag_es: Autorización

### Flight Plan Clearance

The pilot initiates contact with Clearance Delivery to request the flight plan clearance. Before calling ATC, make sure you have received the current ATIS information for the aerodrome.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Tráfego Brasília, bom dia/boa tarde/boa noite. **GOL UNO QUATRO UNO NOVE**.
    </div>
    <div class="comms-atc" markdown>
      **GOL UNO QUATRO UNO NOVE**, Tráfego Brasília. Bom dia/Boa tarde/Boa noite. :material-information-outline:{ title="<em>The reply to the initial call, containing the aircraft callsign followed by the name of the ATS unit, is itself considered an invitation for the aircraft concerned to proceed with its message. (Art. 52, MCA 100-16)</em>" }
    </div>
    <div class="comms-pilot">
      Tráfego Brasília, **GOL UNO QUATRO UNO NOVE**, solicita autorização ATC, informação ATIS BRAVO.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, autorizado para o aeroporto de Guarulhos :material-information-outline:{ title="<em>Or SBGR, read letter by letter</em>" }. Rota do plano de voo. Nível de Voo TRÊS QUATRO ZERO. Pista em uso, DOIS NOVE ESQUERDA. Subida via saída GAXON DOIS ALFA, transição ENRUR. Transponder QUATRO ZERO TRÊS CINCO. Controle Brasília em UNO DOIS NOVE DECIMAL UNO CINCO. Coteje. :material-information-outline:{ title="<em>See item 3.2 of CIRCEA 100-53/2022.</em>" }
    </div>
    <div class="comms-pilot">
      Autorizado até o aeroporto de Guarulhos. Rota do plano de voo. Pista em uso, DOIS NOVE ESQUERDA. Subida via saída GAXON DOIS ALFA, transição ENRUR. Transponder QUATRO ZERO TRÊS CINCO. Controle Brasília em UNO DOIS NOVE DECIMAL UNO CINCO. **GOL UNO QUATRO UNO NOVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, cotejamento correto. Chame Solo Brasília em UNO DOIS UNO DECIMAL OITO ZERO.
    </div>
    <div class="comms-pilot">
      Chamará o solo Brasília em UNO DOIS UNO DECIMAL OITO ZERO, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Delivery, good morning/afternoon/evening. **GOL ONE FOUR ONE NINE**.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Brasília Delivery. Good Morning/Afternoon/Evening.
    </div>
    <div class="comms-pilot">
      Brasília Delivery, **GOL ONE FOUR ONE NINE**, request ATC clearance, information BRAVO.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, cleared to Guarulhos Airport. Flight plan route. Runway in use, TWO NINE LEFT. Climb via GAXON TWO ALFA departure, ENRUR transition. Squawk FOUR ZERO THREE FIVE. Brasília Control on ONE TWO NINE DECIMAL ONE FIVE. Read back.
    </div>
    <div class="comms-pilot">
      Cleared to Guarulhos Airport. Flight plan route. Runway in use, TWO NINE LEFT. Climb via GAXON TWO ALFA departure, ENRUR transition. Squawk FOUR ZERO THREE FIVE. Brasília Control on ONE TWO NINE DECIMAL ONE FIVE. **GOL ONE FOUR ONE NINE**.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, read back is correct. Call Brasília Ground on ONE TWO ONE DECIMAL EIGHT ZERO.
    </div>
    <div class="comms-pilot">
      Will call Brasília Ground on ONE TWO ONE DECIMAL EIGHT ZERO, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Autorización, buenos días/buenas tardes/buenas noches. **GOL UNO CUATRO UNO NUEVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Brasília Autorización. Buenos Días/Buenas Tardes/Buenas Noches.
    </div>
    <div class="comms-pilot">
      Brasília Autorización, **GOL UNO CUATRO UNO NUEVE**, solicita autorización ATC, información BRAVO.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, autorizado hasta el aeropuerto de Guarulhos. Ruta plan de vuelo. Pista en uso, DOS NUEVE IZQUIERDA. Ascienda vía salida normalizada GAXON DOS ALFA, transición ENRUR. Transponder CUATRO CERO TRÊS CINCO. Brasília Control en UNO DOS NUEVE DECIMAL UNO CINCO. Colacione.
    </div>
    <div class="comms-pilot">
      Autorizado hasta el aeropuerto de Guarulhos. Ruta plan de vuelo. Pista en uso, DOS NUEVE IZQUIERDA. Salida normalizada GAXON DOS ALFA, transición ENRUR. Transponder CUATRO CERO TRÊS CINCO. Brasília Control en UNO DOS NUEVE DECIMAL UNO CINCO. **GOL UNO CUATRO UNO NUEVE**
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, colación correctal Llame Brasília Tierra en UNO DOS UNO DECIMAL OCHO CERO.
    </div>
    <div class="comms-pilot">
      Llamará Brasília Tierra en UNO DOS UNO DECIMAL OCHO CERO, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. An aircraft in the **SUPER (J)** or **HEAVY (H)** wake turbulence category shall include the word **SUPER** or **PESADA / HEAVY** immediately after its callsign in the initial contact with the ATS unit.

        > :flag_br: Tráfego Brasília, bom dia. TAM OITO UNO TRÊS SETE **PESADA**. <br/>
        > :flag_gb: Brasília Delivery, good morning. TAM EIGHT ONE THREE SEVEN **HEAVY**. <br/>
        > :flag_es: Brasília Autorización, buenos días. TAM OCHO UNO TRES SIETE **PESADA**. <br/>

        It is not necessary to repeat the word **SUPER** or **PESADA / HEAVY** in subsequent communications.

    2. If you need to issue an **OMNI** departure, you can add initial climb instructions to the ATC clearance.

        > :flag_br: PAPA SIERRA CHARLIE NOVEMBER X-RAY, autorizado para Salvador. Rota do plano de voo. Pista em uso, UNO CINCO. **Subida via saída OMNI, mantenha proa da pista até CINCO MIL pés, após voe direto KONVI.** Transponder 4035. Controle São Paulo em UNO TRÊS DOIS DECIMAL UNO. Coteje. <br/>
        > :flag_gb: PAPA SIERRA CHARLIE NOVEMBER X-RAY, cleared to Salvador. Flight plan route. Runway in use, ONE FIVE. **Climb via OMNI departure, fly runway heading until FIVE THOUSAND feet, then fly direct KONVI.** Squawk 4035. Brasília Control on ONE TWO NINE DECIMAL ONE FIVE. Read back. <br/>
        > :flag_es: PAPA SIERRA CHARILE NOVEMBER X-RAY, autorizado para Salvador. Ruta plan de vuelo. Pista en uso, UNO CINCO. **Ascienda vía salida OMNI, mantenga rumbo de la pista hasta CINCO MIL pies, después vuele directo KONVI.** Transponder 4035. Brasília Control en UNO DOS NUEVE DECIMAL UNO CINCO. Colacione. <br/>

## :material-numeric-2-box: :flag_br: Solo / :flag_gb: Ground / :flag_es: Tierra

This ATC unit is responsible for managing aircraft and vehicle traffic on the aerodrome manoeuvring area, in places such as aprons and taxiways. Contact with Ground usually takes place after the flight plan clearance has been issued by Clearance Delivery.

### Pushback and Startup

Pushback is the towing of the aircraft out of the gate or parking stand using a tug. Startup refers to the process of starting the aircraft engines.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Solo Brasília, **GOL UNO QUATRO UNO NOVE**, pátio UNO, posição UNO QUATRO, IFR para Guarulhos, solicita autorização para pushback e acionamento.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Solo Brasília, autorizado pushback e acionamento, chame pronto para o táxi.
    </div>
    <div class="comms-pilot">
      **GOL UNO QUATRO UNO NOVE**, autorizado pushback e acionamento, chamará pronto para o táxi.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Ground, **GOL ONE FOUR ONE NINE**, apron ONE, position ONE FOUR, IFR to Guarulhos, request clearance for pushback and startup.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Brasília Ground, cleared to pushback and startup, report ready for taxi.
    </div>
    <div class="comms-pilot">
      Cleared to pushback and startup, I will call when ready for taxi, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Tierra, **GOL UNO CUATRO UNO NUEVE**, plataforma UNO, posición UNO CUATRO, IFR para Guarulhos, listo para remolque y puesto en marcha.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Brasília Tierra, autorizado remolque y puesto en marcha, llame listo para rodar.
    </div>
    <div class="comms-pilot">
      Remolque y puesto en marcha aprobado, llamará listo para rodar, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. It is common to clear the aircraft to push back with a supplementary instruction, for example:
    
        1. the direction in which the tail should turn:

            > :flag_br: AZUL QUATRO UNO OITO SETE, Solo São Gonçalo, autorizado pushback e acionamento, **cauda para a esquerda**. <br/>
            > :flag_gb: AZUL FOUR ONE EIGHT SEVEN, São Gonçalo Ground, cleared to pushback and startup, **tail left**. <br/>
            > :flag_es: AZUL CUATRO UNO OCHO SIETE, São Gonçalo Tierra, autorizado remolque y puesto en marcha, **cola a la izquierda**. <br/>

        2. the location to which the pushback should be made:
  
            > :flag_br: VARIG OITO OITO NOVE OITO, Solo Confins, autorizado pushback e acionamento **na taxiway TANGO**. <br/>
            > :flag_gb: VARIG EIGHT EIGHT NINE EIGHT, Confins Ground, cleared to pushback and startup **on taxiway TANGO**. <br/>
            > :flag_es: VARIG OCHO OCHO NUEVE OCHO, Confins Tierra, autorizado remolque y puesto en marcha **en la calle TANGO**. <br/>

    2. When pushback is not required or unnecessary, only startup may be approved:

        > :flag_br: PAPA ROMEO INDIA MIKE OSCAR, Solo Marte, **autorizado acionamento**, chame pronto para o táxi. <br/>
        > :flag_gb: PAPA ROMEO INDIA MIKE OSCAR, Marte Ground, **cleared for startup**, report ready for taxi. <br/>
        > :flag_es: PAPA ROMEO INDIA MIKE OSCAR, Marte Tierra, **autorizado puesto en marcha**, llame listo para rodar. <br/>

### Taxi

Taxi is the movement of the aircraft from its original parking stand to the departure runway, or vice versa, using the aerodrome's taxiways and aprons.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Solo Brasília, **GOL UNO QUATRO UNO NOVE**, pronto para o táxi.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Solo Brasília, táxi autorizado para o ponto de espera da pista DOIS NOVE ESQUERDA via taxiways LIMA MEIA, KILO, UNIFORM e ZULU. Ajuste de altímetro, UNO ZERO UNO TRÊS.
    </div>
    <div class="comms-pilot">
      Táxi autorizado para o ponto de espera, pista DOIS NOVE ESQUERDA, via taxiways LIMA MEIA, KILO, UNIFORM e ZULU, ajuste de altímetro 1013. **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Ground, **GOL ONE FOUR ONE NINE**, ready for taxi.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Brasília Ground, cleared to taxi to holding point, runway TWO NINE LEFT, via taxiways LIMA FOUR, KILO, UNIFORM and ZULU. QNH ONE ZERO ONE THREE.
    </div>
    <div class="comms-pilot">
      Cleared to taxi to holding point, runway TWO NINE LEFT, via taxiways LIMA FOUR, KILO, UNIFORM and ZULU, QNH ONE ZERO ONE THREE. **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Tierra, **GOL UNO CUATRO UNO NUEVE**, listo para rodar.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Brasília Tierra, autorizado rodar al punto de espera, pista DOS NUEVE IZQUIERDA, vía calles LIMA SEIS, KILO, UNIFORM y ZULU. QNH UNO CERO UNO TRES.
    </div>
    <div class="comms-pilot">
      Autorizado rodar al punto de espera, pista DOS NUEVE IZQUIERDA, vía calles LIMA SEIS, KILO, UNIFORM y ZULU. QNH UNO CERO UNO TRES. **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. The aircraft may take off from a runway intersection instead of using the full runway length. When issuing the taxi clearance, Ground will state the intersection to be used for takeoff.
    
        > :flag_br: FORÇA AÉREA DOIS UNO ZERO UNO, Solo Confins, táxi autorizado para o ponto de espera da pista UNO MEIA, **interseção CHARLIE UNO**, via taxiways TANGO, ECHO, MIKE e CHARLIE ONE. Ajuste de altímetro, UNO ZERO UNO TRÊS. <br/>
        > :flag_gb: AIR FORCE TWO ONE ZERO ONE, Confins Ground, cleared to taxi to holding point, runway ONE SIX, **CHARLIE ONE intersection**, via taxiways TANGO, ECHO, MIKE and CHARLIE ONE. QNH ONE ZERO ONE THREE. <br/>
        > :flag_es: FUERZA AEREA DOS UNO CERO UNO, Confins Tierra, autorizado rodar al punto de espera, pista UNO SEIS, **intersección CHARLIE UNO**, vía calles LIMA SEIS, KILO, UNIFORM y ZULU. QNH UNO CERO UNO TRES. <br/>

    2. Occasionally, for flow control purposes, ATC may instruct the aircraft to hold position at a given point during taxi:

        > :flag_br: PAPA SIERRA TANGO ALFA ROMEO, **mantenha posição antes da taxiway ALFA**. <br/>
        > :flag_gb: PAPA SIERRA TANGO ALFA ROMEO, **hold position before taxiway ALFA**. <br/>
        > :flag_es: PAPA SIERRA TANGO ALFA ROMEO, **mantenga posición afuera de la calle ALFA**. <br/>

        In this case, the pilot shall hold position on the current taxiway before reaching its intersection with taxiway ALFA.

### Transfer to Tower

Upon reaching the holding point, the pilot will be transferred to the Tower to receive clearance to enter the runway and take off.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Solo Brasília, **GOL UNO QUATRO UNO NOVE**, no ponto de espera da pista DOIS NOVE ESQUERDA.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, chame a Torre Brasília em UNO UNO OITO DECIMAL UNO. Bom voo!
    </div>
    <div class="comms-pilot">
      Chamará Torre Brasília em UNO UNO OITO DECIMAL UNO, **GOL UNO QUATRO UNO NOVE**. Obrigado e bom controle!
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Ground, **GOL ONE FOUR ONE NINE**, on holding point of runway TWO NINE LEFT.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, contact Brasília Tower on ONE ONE EIGHT DECIMAL ONE. Have a good flight!
    </div>
    <div class="comms-pilot">
      Will contact Brasília Tower on ONE ONE EIGHT DECIMAL ONE, **GOL ONE FOUR ONE NINE**. Thanks and have a good control!
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Tierra, **GOL UNO CUATRO UNO NUEVE**, en el punto de espera de la pista DOS NUEVE IZQUIERDA.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, llame Torre Brasília en UNO UNO OCHO DECIMAL UNO. ¡Buen vuelo!
    </div>
    <div class="comms-pilot">
      Llamará Torre Brasília en UNO UNO OCHO DECIMAL UNO, **GOL UNO CUATRO UNO NUEVE**. ¡Gracias y buen control!
    </div>

??? abstract "Some remarks..."

    1. For intersection takeoffs, it is advisable to state in the transmission to ATC the intersection at which the aircraft is at the holding point.

        > :flag_br: Solo Brasília, **GOL UNO QUATRO UNO NOVE**, no ponto de espera da pista DOIS NOVE ESQUERDA, **interseção ZULU**. <br/>
        > :flag_gb: Brasília Ground, **GOL ONE FOUR ONE NINE**, on holding point of runway TWO NINE LEFT, **ZULU intersection**. <br/>
        > :flag_es: Brasília Tierra, **GOL UNO CUATRO UNO NUEVE**, en el punto de espera de la pista DOS NUEVE IZQUIERDA, **intersección ZULU**. <br/>

## :material-numeric-3-box: :flag_br: Torre / :flag_gb: Tower / :flag_es: Torre

### Takeoff Clearance

Takeoff clearance is issued by the Tower after the pilot reports at the runway holding point. The clearance includes the runway in use, wind conditions and any additional instructions required.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Torre Brasília, **GOL UNO QUATRO UNO NOVE**, ponto de espera, pista DOIS NOVE ESQUERDA, pronto para decolagem.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Torre Brasília, pista DOIS NOVE ESQUERDA, decolagem autorizada, vento DOIS OITO ZERO GRAUS, ZERO NOVE NÓS. :material-information-outline:{ title="Any supplementary instruction follows immediately after this." }
    </div>
    <div class="comms-pilot">
      Decolagem autorizada, pista DOIS NOVE ESQUERDA, **GOL UNO QUATRO UNO NOVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, decolado aos ZERO CINCO, chame o Controle Brasília em UNO UNO NOVE DECIMAL DOIS.
    </div>
    <div class="comms-pilot">
      Chamará o Controle Brasília em UNO UNO NOVE DECIMAL DOIS, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Tower, **GOL ONE FOUR ONE NINE**, holding point, runway TWO NINE LEFT, ready for takeoff.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Brasília Tower, runway TWO NINE LEFT, cleared for take-off. Wind TWO EIGHT ZERO DEGREES, ZERO NINE KNOTS.
    </div>
    <div class="comms-pilot">
      Cleared for take-off, runway TWO NINE LEFT, **GOL ONE FOUR ONE NINE**.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, airborne at ZERO FIVE, contact Brasília Control on ONE ONE NINE DECIMAL TWO.
    </div>
    <div class="comms-pilot">
      Contact Brasília Control on ONE ONE NINE DECIMAL TWO, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasilia Torre, **GOL UNO CUATRO UNO NUEVE**, punto de espera, pista DOS NUEVE IZQUIERDA, listo para despegar.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Brasília Torre, pista DOS NUEVE IZQUIERDA, autorizado despegue, viento DOS OCHO CERO grados, CERO NUEVE nudos.
    </div>
    <div class="comms-pilot">
      Autorizado despegue, pista DOS NUEVE IZQUIERDA, **GOL UNO CUATRO UNO NUEVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, en el aire a los CERO CINCO, llame el Brasília Control en UNO UNO NUEVE DECIMAL DOS.
    </div>
    <div class="comms-pilot">
      Llamará el Brasília Control en UNO UNO NUEVE DECIMAL DOS, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. Routinely, to expedite departure and arrival sequencing, the Tower may instruct an aircraft to **line up and wait** on the runway, in which case the pilot must enter the runway, line up the aircraft and wait for a subsequent takeoff clearance.

        > :flag_br: PAPA ROMEO ECHO ZULU ZULU, Torre Recife, pista UNO OITO, alinha e mantém. <br/>
        > :flag_gb: PAPA ROMEO ECHO ZULU ZULU, Recife Tower, runway ONE EIGHT, line up and wait. <br/>
        > :flag_es: PAPA ROMEO ECHO ZULU ZULU, Recife Torre, pista UNO OITO, alinéese y mantenga. <br/>

    2. At some airports, the Tower may issue additional instructions with the takeoff clearance, such as an initial heading to be maintained after takeoff, the next frequency to be contacted, or other relevant information.

        > :flag_br: AZUL CONECTA CINCO DOIS CINCO SETE, Torre Fortaleza, pista UNO TRÊS, decolagem autorizada, vento UNO CINCO ZERO GRAUS, CINCO NÓS. **Após a decolagem, mantenha a proa da pista subindo para SETE MIL pés.** <br/>
        > :flag_gb: AZUL CONECTA FIVE TWO FIVE SEVEN, Fortaleza Tower, runway ONE THREE, cleared for takeoff, wind ONE FIVE ZERO DEGREES, FIVE KNOTS. **After takeoff, maintain runway heading climbing to SEVEN THOUSAND FEET.** <br/>
        > :flag_es: AZUL CONECTA CINCO DOS CINCO SIETE, Fortaleza Torre, pista UNO TRES, autorizado despegar, viento UNO CINCO CERO GRADOS, CINCO NUDOS. **Después del despegue, mantenga el rumbo de la pista en ascenso a SIETE MIL PIES.** <br/><br/>

        > :flag_br: TAM TRÊS ZERO ZERO DOIS, Torre São Paulo, pista UNO SETE DIREITA, decolagem autorizada, vento DOIS ZERO ZERO GRAUS, UNO DOIS NÓS. **Após a decolagem, chame o Controle São Paulo em UNO DOIS MEIA DECIMAL SETE CINCO. Bom voo!** <br/>
        > :flag_gb: TAM THREE ZERO ZERO TWO, São Paulo Tower, runway ONE SEVEN RIGHT, cleared for takeoff, wind TWO ZERO ZERO DEGREES, ONE TWO KNOTS. **After takeoff, contact São Paulo Control on ONE TWO SIX DECIMAL SEVEN FIVE. Have a good flight!** <br/>
        > :flag_es: TAM TRES CERO CERO DOS, Torre São Paulo, pista UNO SIETE DERECHA, autorizado despegar, viento DOS CERO CERO GRADOS, UNO DOS NUDOS. **Después del despegue, llame el São Paulo Control en UNO DOS SEIS DECIMAL SIETE CINCO. ¡Buen vuelo!** <br/>

    3. Some towers will not state the takeoff time at the moment of transfer. Check the aerodrome's MOP for more details.

    4. Some towers transfer the aircraft to Approach Control together with the takeoff clearance (as in the example above), eliminating the need for contact after takeoff. Check the aerodrome's MOP for more details.

    5. A wind speed of zero knots (00000KT) shall be reported as **wind calm**.

## :material-numeric-4-box: :flag_br: Controle / :flag_gb: Control / :flag_es: Control

### Initial contact after takeoff

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Controle Brasília, **GOL UNO QUATRO UNO NOVE**, decolando pista DOIS NOVE ESQUERDA, passando CINCO MIL PÉS, saída GAXON DOIS ALFA, transição ENRUR.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE** Controle Brasília, contato radar após a decolagem, suba via GAXON DOIS ALFA para o nível de voo TRÊS MEIA ZERO.
    </div>
    <div class="comms-pilot">
      Sobe via saída para o nível TRÊS MEIA ZERO, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Control, **GOL ONE FOUR ONE NINE**, airborne runway TWO NINE LEFT, passing FIVE THOUSAND FEET, GAXON TWO ALFA departure, ENRUR transition.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE** Brasília Control, radar contact on departure, climb via GAXON TWO ALFA to flight level THREE SIX ZERO.
    </div>
    <div class="comms-pilot">
      Climb via departure to flight level THREE SIX ZERO, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Control, **GOL UNO CUATRO UNO NUEVE**, despegado de la pista DOS NUEVE IZQUIERDA, pasando CINCO MIL PIES, salida normalizada GAXON DOS ALFA, transición ENRUR.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Brasília Control, contacto radar en el despegue, ascienda vía GAXON DOS ALFA a nivel TRES SEIS CERO.
    </div>
    <div class="comms-pilot">
      Asciende vía salida a nivel TRES SEIS CERO, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. When saying "Climb via SID to (level)", the controller is instructing the aircraft to climb to the cleared level following the lateral profile of the SID and complying with the level and speed restrictions published on the departure procedure chart.
    
    2. However, the controller may cancel climb restrictions published on the departure procedure chart. The controller may cancel specific restrictions or clear the climb without restrictions.
    
        1. If **all altitude <u>or</u> speed restrictions** are cancelled, the phraseology will be:

            > :flag_br: SURINAM DOIS QUATRO DOIS, Controle Belém, contato radar após a decolagem, suba via saída ILMET UNO para o nível de voo TRÊS MEIA ZERO, **canceladas as restrições de altitude/velocidade**. <br/>
            > :flag_gb: SURINAM TWO FOUR TWO, Belém Control, radar contact on departure, climb via ILMET ONE departure to flight level THREE SIX ZERO, **Cancel altitude/speed restrictions**. <br/>
            > :flag_es: SURINAM DOS CUATRO DOS,  Belém Control, contacto radar en el despegue, ascienda vía salida ILMET UNO al nivel TRES SEIS CERO, **canceladas las restricciones de altitud/velocidad**. <br/>

        2. If an altitude <u>or</u> speed restriction **at specific point(s)** is cancelled, the phraseology will be:

            > :flag_br: SURINAM DOIS QUATRO DOIS, Controle Belém, contato radar após a decolagem, suba via saída ILMET UNO para o nível de voo TRÊS MEIA ZERO, **cancelada a restrição de altitude/velocidade em ILMET**. <br/>
            > :flag_gb: SURINAM TWO FOUR TWO, Belém Control, radar contact on departure, climb via ILMET ONE departure to flight level THREE SIX ZERO, **Cancel altitude/speed restriction at ILMET**. <br/>
            > :flag_es: SURINAM DOS CUATRO DOS,  Belém Control, contacto radar en el despegue, ascienda vía salida ILMET UNO al nivel TRES SEIS CERO, **canceladas la restricción de altitud/velocidad en ILMET**. <br/>

        3. If all restrictions on the entire procedure are cancelled, the phraseology will be:

            > :flag_br: SURINAM DOIS QUATRO DOIS, Controle Belém, contato radar após a decolagem, suba **sem restrições** para o nível de voo TRÊS MEIA ZERO. <br/>
            > :flag_gb: SURINAM TWO FOUR TWO, Belém Control, radar contact on departure, climb **without restrictions** to flight level THREE SIX ZERO. <br/>
            > :flag_es: SURINAM DOS CUATRO DOS,  Belém Control, contacto radar en el despegue, ascienda **sin restricciones** al nivel TRES SEIS CERO. <br/>

            Or alternatively:

            > :flag_br: SURINAM DOIS QUATRO DOIS, Controle Belém, contato radar após a decolagem, suba via saída ILMET UNO para o nível de voo TRÊS MEIA ZERO, **canceladas as restrições de altitude e velocidade**. <br/>
            > :flag_gb: SURINAM TWO FOUR TWO, Belém Control, radar contact on departure, climb via ILMET ONE departure to flight level THREE SIX ZERO, **Cancel altitude and speed restrictions**. <br/>
            > :flag_es: SURINAM DOS CUATRO DOS,  Belém Control, contacto radar en el despegue, ascienda vía salida ILMET UNO al nivel TRES SEIS CERO, **canceladas las restricciones de altitud y velocidad**. <br/>
            

### Flow control during climb

During the climb to cruise level, the controller may issue flow control instructions, such as a temporary level restriction, a speed, a heading to be maintained or a direct routing to a specific fix, among others.

=== ":flag_br: Portuguese"
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, autorizado direto KONVI, suba e mantenha o nível UNO DOIS ZERO.
    </div>
    <div class="comms-pilot">
      Autorizado direto KONVI, sobe restrito ao nível UNO DOIS ZERO, **GOL UNO QUATRO UNO NOVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, continue subida para o nível de voo TRÊS MEIA ZERO, mantenha DOIS CINCO ZERO NÓS até o nível de voo UNO SETE ZERO.
    </div>
    <div class="comms-pilot">
      Continua subida para o nível de voo TRÊS MEIA ZERO, mantém DOIS CINCO ZERO NÓS até o nível de voo UNO SETE ZERO, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, fly direct KONVI, climb restricted to flight level ONE TWO ZERO.
    </div>
    <div class="comms-pilot">
      Fly direct KONVI, climb restricted to flight level ONE TWO ZERO, **GOL ONE FOUR ONE NINE**.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, continue climb to flight level THREE SIX ZERO, maintain TWO FIVE ZERO KNOTS until flight level ONE SEVEN ZERO.
    </div>
    <div class="comms-pilot">
      Continuing climb to flight level THREE SIX ZERO, maintaining TWO FIVE ZERO KNOTS until flight level ONE SEVEN ZERO, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, autorizado directo KONVI, ascienda restringido al nivel UNO DOS CERO.
    </div>
    <div class="comms-pilot">
      Autorizado directo KONVI, asciendiendo para el nivel UNO DOS CERO, **GOL UNO CUATRO UNO NUEVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, continúe ascenso al nivel de vuelo TRES SEIS CERO, mantenga DOS CINCO CERO NUDOS hasta el nivel de vuelo UNO SIETE CERO.
    </div>
    <div class="comms-pilot">
      Continúa ascenso al nivel de vuelo TRES SEIS CERO, manteniendo DOS CINCO CERO NUDOS hasta el nivel de vuelo UNO SIETE CERO, **GOL UNO CUATRO UNO NUEVE**.
    </div>

### Transfer to the next unit

When leaving Approach Control, the pilot will be transferred to the next ATC unit responsible for the flight in that phase of the route, which is the Center.

!!! note "Important"
    Not every flight will be transferred to the Center. On shorter flights, for example, Approach Control may be the last ATC unit contacted before the transfer to the coordination frequency.
    
    Additionally, in some cases, the Approach Control serving the departure airport may transfer the aircraft directly to the Approach Control of the destination airport, if the two are adjacent.

=== ":flag_br: Portuguese"
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, chame Centro Brasília em UNO DOIS MEIA DECIMAL SETE CINCO.
    </div>
    <div class="comms-pilot">
      Chamará o Centro Brasília, UNO DOIS MEIA DECIMAL SETE CINCO, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, call Brasília Center on ONE TWO SIX DECIMAL SEVEN FIVE.
    </div>
    <div class="comms-pilot">
      Call Brasília Center, ONE TWO SIX DECIMAL SEVEN FIVE, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, llame Centro Brasília en UNO DOS SEIS DECIMAL SIETE CINCO.
    </div>
    <div class="comms-pilot">
      Llamará Centro Brasília en UNO DOS SEIS DECIMAL SIETE CINCO, **GOL UNO CUATRO UNO NUEVE**.
    </div>

## :material-numeric-5-box: :flag_br: Centro / :flag_gb: Center / :flag_es: Centro

### Initial call

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Centro Brasília, **GOL UNO QUATRO UNO NOVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Centro Brasília, acione identificação, suba e mantenha o nível TRÊS MEIA ZERO.
    </div>
    <div class="comms-pilot">
      Acionou identificação, sobe e mantém o nível TRÊS MEIA ZERO. **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Center, **GOL ONE FOUR ONE NINE**.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Brasília Center, squawk ident, climb and maintain flight level THREE SIX ZERO.
    </div>
    <div class="comms-pilot">
      Squawk ident, climb and maintain flight level THREE SIX ZERO. **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Centro, **GOL UNO CUATRO UNO NUEVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Brasília Centro, identifique, ascienda y mantenga nivel TRES SEIS CERO.
    </div>
    <div class="comms-pilot">
      Identificado, asciende y mantiene nivel TRES SEIS CERO. **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    "Squawk ident" refers to using the IDENT button on the aircraft transponder, which causes the aircraft's target to be highlighted on the controller's radar display, making it easier to identify. The primary purpose of this procedure during a transfer between ATC units is to indicate to the transferring controller that the aircraft has established two-way radio contact with the new ATC unit, thus completing the transfer process.

    If another means of confirming the transfer is available, the accepting controller may choose not to request squawk ident.

### Reaching cruise level

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Centro Brasília, **GOL UNO QUATRO UNO NOVE**, nível de voo TRÊS MEIA ZERO.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Centro Brasília ciente, mantenha a sua navegação.
    </div>
    <div class="comms-pilot">
      Mantém a navegação, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Center, **GOL ONE FOUR ONE NINE**, flight level THREE SIX ZERO.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Brasília Center roger, maintain own navigation.
    </div>
    <div class="comms-pilot">
      Maintain own navigation, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Centro, **GOL UNO CUATRO UNO NUEVE**, nivel de vuelo TRES SEIS CERO.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Brasília Centro recibido, mantenga su navegación.
    </div>
    <div class="comms-pilot">
      Mantenga la navegación, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    Even when the pilot is under radar surveillance service, regulations require the pilot to report to ATC upon reaching the cleared cruise level.

### Descent Procedure Instruction

Since the STAR usually begins in the Center's airspace, the Center is responsible for stating the arrival to be flown.

=== ":flag_br: Portuguese"
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, prepare a chegada SANPA UNO ALFA, prevista aproximação ILS YANKEE para pista UNO ZERO DIREITA em Guarulhos.
    </div>
    <div class="comms-pilot">
      Prepara a chegada SANPA UNO ALFA, prevista aproximação ILS YANKEE para pista UNO ZERO DIREITA em Guarulhos, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, plan the SANPA UNO ALFA arrival, expect ILS YANKEE approach for runway ONE ZERO RIGHT at Guarulhos.
    </div>
    <div class="comms-pilot">
      Plan SANPA UNO ALFA arrival, expect ILS YANKEE approach for runway ONE ZERO RIGHT at Guarulhos, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, prepare la llegada SANPA UNO ALFA, espere aproximación ILS YANKEE para pista UNO CERO DERECHA en Guarulhos.
    </div>
    <div class="comms-pilot">
      Prepara la llegada SANPA UNO ALFA, esperando aproximación ILS YANKEE para pista UNO CERO DERECHA en Guarulhos, **GOL UNO CUATRO UNO NUEVE**.
    </div>

### Ready for descent

Any change of altitude in controlled airspace requires prior ATC clearance. The pilot must report when at the optimum point to begin the descent in order to receive the necessary clearance.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Centro Brasília, **GOL UNO QUATRO UNO NOVE**, ideal de descida.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, desça via SANPA UNO ALFA para o nível DOIS CINCO ZERO.
    </div>
    <div class="comms-pilot">
      Desce via SANPA UNO ALFA para o nível DOIS CINCO ZERO. **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Center, **GOL ONE FOUR ONE NINE**, ready for descent.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, descend via SANPA UNO ALFA to flight level TWO FIVE ZERO.
    </div>
    <div class="comms-pilot">
      Descend via SANPA UNO ALFA to flight level TWO FIVE ZERO. **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Centro, **GOL UNO CUATRO UNO NUEVE**, listo para descenso.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, descienda vía SANPA UNO ALFA al nivel DOS CINCO CERO.
    </div>
    <div class="comms-pilot">
      Descienda vía SANPA UNO ALFA al nivel DOS CINCO CERO. **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. It is common for ATC to clear descents to intermediate levels before the final descent level in order to optimise the air traffic flow. If ATC instructs the aircraft to descend to a new level, it will say:

        > :flag_br: AMERICAN NOVE MEIA ZERO, continue descida, nível de voo UNO UNO ZERO. <br/>
        > :flag_gb: AMERICAN NINE FIVE ZERO, continue descent, flight level ONE ONE ZERO. <br/>
        > :flag_es: AMERICAN NUEVE CINCO CERO, continue descenso, nivel de vuelo UNO UNO CERO. <br/>

### Transfer to the next unit

On reaching the boundary of the Center's airspace, the pilot will be transferred to the next ATC unit responsible for the flight in that phase of the route, which is Approach Control.

=== ":flag_br: Portuguese"
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, chame o Controle São Paulo em UNO DOIS NOVE DECIMAL QUATRO CINCO.
    </div>
    <div class="comms-pilot">
      Chamará o Controle São Paulo em UNO DOIS NOVE DECIMAL QUATRO CINCO, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, contact São Paulo Control on ONE TWO NINE DECIMAL FOUR FIVE.
    </div>
    <div class="comms-pilot">
      Will contact São Paulo Control on ONE TWO NINE DECIMAL FOUR FIVE, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, llame ahora São Paulo Control en UNO DOS NUEVE DECIMAL CUATRO CINCO.
    </div>
    <div class="comms-pilot">
      Llamará São Paulo Control en UNO DOS NUEVE DECIMAL CUATRO CINCO, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    The transfer may be made at any time before the airspace boundary, provided that the pilot is within communication range of the next controller.

## :material-numeric-6-box: :flag_br: Controle / :flag_gb: Control / :flag_es: Control

### Initial Contact

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Controle São Paulo, **GOL UNO QUATRO UNO NOVE**, descendo via SANPA UNO ALFA.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Controle São Paulo, acione identificação, desça via SANPA UNO ALFA para o nível de voo UNO UNO ZERO, prevista aproximação ILS YANKEE para pista UNO ZERO DIREITA.
    </div>
    <div class="comms-pilot">
      Desce via SANPA UNO ALFA para o nível UNO UNO ZERO, aguarda ILS YANKEE UNO ZERO DIREITA, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      São Paulo Control, **GOL ONE FOUR ONE NINE**, descending via SANPA UNO ALFA.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE** São Paulo Control, squawk ident, descend via SANPA UNO ALFA to flight level ONE ONE ZERO, expect ILS YANKEE approach for runway ONE ZERO RIGHT.
    </div>
    <div class="comms-pilot">
      Descend via SANPA ONE ALFA to flight level ONE ONE ZERO, expect ILS YANKEE ONE ZERO RIGHT, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      São Paulo Control, **GOL UNO CUATRO UNO NUEVE**, en descenso vía SANPA UNO ALFA.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, São Paulo Control, identifique, descienda vía SANPA UNO ALFA al nivel de vuelo UNO UNO CERO, espere aproximación ILS YANKEE para pista UNO CERO DERECHA.
    </div>
    <div class="comms-pilot">
      Descenso vía SANPA UNO ALFA al nivel UNO UNO CERO, esperando ILS YANKEE UNO CERO DERECHA, **GOL UNO CUATRO UNO NUEVE**.
    </div>

### Flow Control during Descent

During the descent to the approach level, the controller may issue flow control instructions, such as a temporary level restriction, a speed, a heading to be maintained or a direct routing to a specific fix, among others.

=== ":flag_br: Portuguese"
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, autorizado direto SANPA, desça e mantenha o nível UNO ZERO ZERO.
    </div>
    <div class="comms-pilot">
      Autorizado direto SANPA, desce restrito ao nível UNO ZERO ZERO, **GOL UNO QUATRO UNO NOVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, reduza para DOIS ZERO ZERO NÓS, desça e mantenha MEIA MIL PÉS, Q N H UNO ZERO UNO QUATRO.
    </div>
    <div class="comms-pilot">
      Reduz para DOIS ZERO ZERO NÓS, desce e mantém MEIA MIL PÉS, Q N H UNO ZERO UNO QUATRO, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-atc"> 
      **GOL ONE FOUR ONE NINE**, fly direct SANPA, descend restricted to flight level ONE ZERO ZERO.
    </div>
    <div class="comms-pilot">
      Fly direct SANPA, descend restricted to flight level ONE ZERO ZERO, **GOL ONE FOUR ONE NINE**.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, reduce to TWO ZERO ZERO KNOTS, descend and maintain SIX THOUSAND FEET, Q N H ONE ZERO ONE FOUR.
    </div>
    <div class="comms-pilot">
      Reduce to TWO ZERO ZERO KNOTS, descend and maintain SIX THOUSAND FEET, Q N H ONE ZERO ONE FOUR, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, vuela directo SANPA, descienda restringido al nivel de vuelo UNO CERO CERO.
    </div>
    <div class="comms-pilot">
      Vuelo directo SANPA, descienda restringido al nivel de vuelo UNO CERO CERO, **GOL UNO CUATRO UNO NUEVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, reduzca a DOS CERO CERO NUDOS, descienda y mantenga SEIS MIL PIES, Q N H UNO CERO UNO CUATRO.
    </div>
    <div class="comms-pilot">
      Reduzca a DOS CERO CERO NUDOS, descienda y mantenga SEIS MIL PIES, Q N H UNO CERO UNO CUATRO, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. Flow control instructions during descent follow the same logic as flow control instructions during climb, as explained earlier.

    2. When descent is cleared to an altitude below the transition level, the QNH will be given by the controller.

### Approach Clearance

To begin the approach, the pilot must receive clearance from Approach Control.

=== ":flag_br: Portuguese"
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE** autorizado ILS YANKEE para pista UNO ZERO DIREITA, reporte estabilizado no localizador.
    </div>
    <div class="comms-pilot">
      Autorizado ILS YANKEE para pista UNO ZERO DIREITA, reportará estabilizado no localizador, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE** cleared ILS YANKEE for runway ONE ZERO RIGHT, report established.
    </div>
    <div class="comms-pilot">
      Cleared ILS YANKEE for runway ONE ZERO RIGHT, will report established, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE** autorizado ILS YANKEE para pista UNO CERO DERECHA, reporte establecido en el localizador.
    </div>
    <div class="comms-pilot">
      Autorizado ILS YANKEE para pista UNO CERO DERECHA, reportará establecido en el localizador, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. Since the definition of "established" may vary between different aircraft types and operators, the pilot is responsible for determining when the aircraft is established on the approach.
    2. For visual approaches, the clearance will be given for the visual approach, and the pilot must report when actually in visual contact with the field.

### Transfer to Tower

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Estabilizado no localizador da pista UNO ZERO DIREITA, **GOL UNO QUATRO UNO NOVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, chame a Torre Guarulhos em UNO UNO OITO DECIMAL QUATRO. Bom pouso!
    </div>
    <div class="comms-pilot">
      UNO UNO OITO DECIMAL QUATRO, obrigado, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Established on localizer, runway ONE ZERO RIGHT, **GOL ONE FOUR ONE NINE**.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, contact Guarulhos Tower on ONE ONE EIGHT DECIMAL FOUR. Have a good landing!
    </div>
    <div class="comms-pilot">
      ONE ONE EIGHT DECIMAL FOUR, thank you, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Establecido en el localizador, pista UNO CERO DERECHA, **GOL UNO CUATRO UNO NUEVE**.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, llame Torre Guarulhos en UNO UNO OCHO DECIMAL CUATRO. ¡Buen aterrizaje!
    </div>
    <div class="comms-pilot">
      UNO UNO OCHO DECIMAL CUATRO, gracias, **GOL UNO CUATRO UNO NUEVE**.
    </div>

## :material-numeric-7-box: :flag_br: Torre / :flag_gb: Tower / :flag_es: Torre

### Initial Contact

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Torre Guarulhos, **GOL UNO QUATRO UNO NOVE**, final, pista UNO ZERO DIREITA.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Torre Guarulhos, pista UNO ZERO DIREITA, pouso autorizado, vento ZERO NOVE ZERO graus, ZERO OITO nós.
    </div>
    <div class="comms-pilot">
      Pouso autorizado, pista UNO ZERO DIREITA, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Guarulhos Tower, **GOL ONE FOUR ONE NINE** on final, runway ONE ZERO RIGHT.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Guarulhos Tower, runway ONE ZERO RIGHT, cleared to land, wind ZERO NINE ZERO degrees, ZERO EIGHT knots.
    </div>
    <div class="comms-pilot">
      Cleared to land, runway ONE ZERO RIGHT, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Guarulhos Torre, **GOL UNO CUATRO UNO NUEVE**, final, pista UNO CERO DERECHA.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Guarulhos Torre, pista UNO CERO DERECHA, autorizado aterrizar, viento CERO NUEVE CERO grados, CERO OCHO nudos.
    </div>
    <div class="comms-pilot">
      Autorizado aterrizar, pista UNO CERO DERECHA, **GOL UNO CUATRO UNO NUEVE**.
    </div>

??? abstract "Some remarks..."

    1. If the controller is unable to clear the aircraft to land on initial contact because the runway is occupied or due to other restrictions, the phraseology will be:

        > :flag_br: **AVIANCA MEIA ZERO ZERO DOIS**, Torre São Paulo, pista UNO SETE DIREITA, continue aproximação, aguarde pista livre, vento ZERO NOVE ZERO graus, ZERO OITO nós. <br/>
        > :flag_gb: **AVIANCA SIX ZERO ZERO TWO**, São Paulo Tower, runway ONE SEVEN RIGHT, continue approach, standby for runway vacated, wind ZERO NINE ZERO degrees, ZERO EIGHT knots. <br/>
        > :flag_es: **AVIANCA SEIS CERO CERO DOS**, São Paulo Torre, pista UNO SIETE DERECHA, continúe aproximación, espere pista libre, viento CERO NUEVE CERO grados, CERO OCHO nudos. <br/>

        To which the pilot reads back: <br/>

        > :flag_br: Continua aproximação, aguarda pista livre, **AVIANCA MEIA ZERO ZERO DOIS**. <br/>
        > :flag_gb: Continuing approach, standby for runway vacated, **AVIANCA SIX ZERO ZERO TWO**. <br/>
        > :flag_es: Continúa aproximación, espere pista libre, **AVIANCA SEIS CERO CERO DOS**. <br/>

    2. The tower controller may provide additional information, such as weather conditions, traffic information or landing sequence.

        > :flag_br: **PASSAREDO DOIS DOIS UNO MEIA**, Torre Guarulhos, pista UNO ZERO DIREITA, pouso autorizado, vento ZERO NOVE ZERO graus, ZERO OITO nós. **Atenção para decolagem de um B777, pista UNO ZERO ESQUERDA.**<br/>
        > :flag_gb: **PASSAREDO TWO TWO ONE SIX**, Guarulhos Tower, runway ONE ZERO RIGHT, cleared to land, wind ZERO NINE ZERO degrees, ZERO EIGHT knots. **Caution with traffic departing, B777, runway ONE ZERO LEFT.**<br/>
        > :flag_es: **PASSAREDO DOS DOS UNO SEIS**, Guarulhos Torre, pista UNO CERO DERECHA, autorizado aterrizar, viento CERO NUEVE CERO grados, CERO OCHO nudos. **Atención con despegue de un B777, pista UNO CERO IZQUIERDA.**<br/>

        > :flag_br: **VARIG OITO NOVE OITO**, Torre Galeão, pista UNO CINCO, pouso autorizado, vento UNO DOIS ZERO graus, UNO SETE nós. **Atenção para possibilidade tesoura de vento na curta final.** <br/>
        > :flag_gb: **VARIG EIGHT NINE EIGHT**, Galeão Tower, runway ONE FIVE, cleared to land, wind ONE TWO ZERO degrees, ONE SEVEN knots. **Caution for possible windshear on short final.** <br/>
        > :flag_es: **VARIG OCHO NUEVE OCHO**, Galeão Torre, pista UNO CINCO, autorizado aterrizar, viento UNO DOS CERO grados, UNO SIETE nudos. **Atención por posible cizalladura en final corta.** <br/>

        > :flag_br: **AZUL QUATRO DOIS UNO TRÊS**, Torre Aracaju, pista UNO DOIS, pouso autorizado, vento ZERO SEIS ZERO graus, UNO DOIS nós. **Pista molhada.** <br/>
        > :flag_gb: **AZUL FOUR TWO ONE THREE**, Aracaju Tower, runway ONE TWO, cleared to land, wind ZERO SIX ZERO degrees, ONE TWO knots. **Runway wet.** <br/>
        > :flag_es: **AZUL CUATRO DOS UNO TRES**, Aracaju Torre, pista UNO DOS, autorizado aterrizar, viento CERO SEIS CERO grados, UNO DOS nudos. **Pista mojada.** <br/>

    3. The tower controller may issue other instructions to be carried out immediately after landing, such as holding position on the runway, reporting when vacating, or vacating via a specific taxiway.

        > :flag_br: **FORÇA AÉREA DOIS QUATRO ZERO QUATRO**, Torre Brasília, pista UNO UNO ESQUERDA, pouso autorizado, vento UNO NOVE ZERO graus, ZERO QUATRO nós. **Após o pouso, mantenha posição na pista.** <br/>
        > :flag_gb: **FORÇA AÉREA TWO FOUR ZERO FOUR**, Brasília Tower, runway ONE ONE LEFT, cleared to land, wind ONE NINE ZERO degrees, ZERO FOUR knots. **After landing, hold position on runway.** <br/>
        > :flag_es: **FUERZA AÉREA DOS CUATRO CERO CUATRO**, Brasília Torre, pista UNO UNO IZQUIERDA, autorizado aterrizar, viento UNO NUEVE CERO grados, CERO CUATRO nudos. **Después de aterrizar, mantenga posición en la pista.** <br/>

        > :flag_br: **TAM TRÊS ZERO DOIS UNO**, Torre Confins, pista UNO MEIA, pouso autorizado, vento UNO UNO ZERO graus, UNO TRÊS nós. **Após o pouso, livre na taxiway FOXTROT UNO.** <br/>
        > :flag_gb: **TAM THREE ZERO TWO ONE**, Confins Tower, runway ONE SIX, cleared to land, wind ONE ONE ZERO degrees, ONE THREE knots. **After landing, vacate on taxiway FOXTROT ONE.** <br/>
        > :flag_es: **TAM TRES CERO DOS UNO**, Confins Torre, pista UNO SEIS, autorizado aterrizar, viento UNO UNO CERO grados, UNO TRES nudos. **Después de aterrizar, salga en calle de rodaje FOXTROT UNO.** <br/>

### After landing

=== ":flag_br: Portuguese"
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, taxie via BRAVO BRAVO, autorizado cruzamento da pista UNO ZERO ESQUERDA, ao livrar na LIMA chame o Solo Guarulhos em UNO DOIS NOVE DECIMAL SETE.
    </div>
    <div class="comms-pilot">
      Taxi via BRAVO BRAVO, autorizado cruzamento da pista UNO ZERO ESQUERDA, chamará o Solo Guarulhos em UNO DOIS NOVE DECIMAL SETE ao livrar na LIMA, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, taxi via BRAVO BRAVO, cleared to cross runway ONE ZERO LEFT, when vacating at LIMA contact Guarulhos Ground on ONE TWO NINE DECIMAL SEVEN.
    </div>
    <div class="comms-pilot">
      Taxi via BRAVO BRAVO, cleared to cross runway ONE ZERO LEFT, will contact Guarulhos Ground on ONE TWO NINE DECIMAL SEVEN when vacating at LIMA, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, taxi vía BRAVO BRAVO, autorizado cruce de pista UNO CERO IZQUIERDA, al salir en LIMA llame a Guarulhos Tierra en UNO DOS NUEVE DECIMAL SIETE.
    </div>
    <div class="comms-pilot">
      Taxi vía BRAVO BRAVO, autorizado cruce de pista UNO CERO IZQUIERDA, llamará a Guarulhos Tierra en UNO DOS NUEVE DECIMAL SIETE al salir en LIMA, **GOL UNO CUATRO UNO NUEVE**.
    </div>

## :material-numeric-8-box: :flag_br: Solo / :flag_gb: Ground / :flag_es: Tierra

### Initial contact

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Solo Guarulhos, **GOL UNO QUATRO UNO NOVE** livrou a pista UNO ZERO ESQUERDA na LIMA.
    </div>
    <div class="comms-atc">
      **GOL UNO QUATRO UNO NOVE**, Solo Guarulos, autorizado taxi para o Pátio QUATRO via taxiways ALFA, INDIA, YANKEE QUATRO, YANKEE QUATRO WISKEY, posição QUATRO ZERO TRÊS.
    </div>
    <div class="comms-pilot">
      Autorizado taxi para o Pátio QUATRO via taxiways ALFA, INDIA, YANKEE QUATRO, YANKEE QUATRO WISKEY, posição QUATRO ZERO TRÊS, **GOL UNO QUATRO UNO NOVE**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Guarulhos Ground, **GOL ONE FOUR ONE NINE** vacated runway ONE ZERO LEFT at LIMA.
    </div>
    <div class="comms-atc">
      **GOL ONE FOUR ONE NINE**, Guarulhos Ground, taxi to Apron FOUR via taxiways ALFA, INDIA, YANKEE FOUR, YANKEE FOUR WISKEY, stand FOUR ZERO THREE.
    </div>
    <div class="comms-pilot">
      Taxi to Apron FOUR via taxiways ALFA, INDIA, YANKEE FOUR, YANKEE FOUR WISKEY, stand FOUR ZERO THREE, **GOL ONE FOUR ONE NINE**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Guarulhos Tierra, **GOL UNO CUATRO UNO NUEVE** salió de pista UNO CERO IZQUIERDA en LIMA.
    </div>
    <div class="comms-atc">
      **GOL UNO CUATRO UNO NUEVE**, Guarulhos Tierra, taxi al Plataforma CUATRO vía calles de rodaje ALFA, INDIA, YANKEE CUATRO, YANKEE CUATRO WISKEY, posición CUATRO CERO TRES.
    </div>
    <div class="comms-pilot">
      Taxi al Plataforma CUATRO vía calles de rodaje ALFA, INDIA, YANKEE CUATRO, YANKEE CUATRO WISKEY, posición CUATRO CERO TRES, **GOL UNO CUATRO UNO NUEVE**.
    </div>