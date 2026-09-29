---
title: Outbound Flight (Controlled to Uncontrolled)
icon: material/microphone
---

--8<-- "includes/abreviacoes.md"

![Visual Flight Phraseology Manual - Outbound Flight](img/manual-fraseologia-voo-visual-ida.png)

#

## :material-numeric-0-box: Preliminaries

<section markdown style="display: grid; grid-template-columns: 5fr 2fr">

<div markdown>

The flowchart alongside shows the sequence of units involved in this flight. The aircraft departs from a controlled aerodrome, crosses controlled airspace, continues en route under the flight information service and lands at an uncontrolled aerodrome served by an aeronautical station.

For practical purposes, we will simulate the flight of **PT-VBR**, a Cessna 172, between **Pampulha (SBBH)** and **Ipatinga (SBIP)**, under visual flight rules, cruising at **7,500 ft**.

Assume the **transition level is 080**. The entire flight takes place below it, so the vertical reference is always **altitude in feet on QNH**, and flight level is never mentioned.

Communications are presented in Portuguese, English and Spanish. Additional notes and variations appear in remarks boxes at the end of each stage, and they are worth checking.

!!! danger "Use of Spanish in phraseology"
    Spanish should only be used in the airspaces where it is authorised, both by DECEA and by the CAOPs officially established between Vatsim Brasil and other divisions. By default, **indiscriminate use of this language in routine aeronautical communication <u>is prohibited</u>**, even if both pilot and ATC are able to use it.

</div>

<div style="text-align: center;">
``` mermaid
flowchart TD
  ATIS(ATIS);
  ATIS --> GND(GROUND);
  GND --> TWR(TOWER);
  TWR --> APP(CONTROL);
  APP --> FIS(INFORMATION);
  FIS --> RDO(RADIO);
```
</div>

</section>

## :material-numeric-1-box: :flag_br: Solo / :flag_gb: Ground / :flag_es: Tierra

### Engine start and taxi

Before calling Ground, listen to the ATIS and have the QNH, the runway in use and the information letter at hand. In visual flight, the initial contact already includes the position on the apron, the aircraft type, the flight rules and the destination.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Solo Pampulha, **PAPA TANGO VICTOR BRAVO ROMEO**, bom dia.
    </div>
    <div class="comms-atc" markdown>
      **PAPA TANGO VICTOR BRAVO ROMEO**, Solo Pampulha, bom dia. :material-information-outline:{ title="<em>A resposta à chamada inicial, contendo o indicativo de chamada da aeronave seguido do nome do órgão ATS, já será considerado um convite para que a aeronave em questão prossiga com a sua mensagem. (Art. 52, MCA 100-16)</em>" }
    </div>
    <div class="comms-pilot">
      Solo Pampulha, **PAPA TANGO VICTOR BRAVO ROMEO**, pátio da aviação geral, um Cessna 172, VFR para Ipatinga, informação ALFA, solicita acionamento e instruções de táxi.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Solo Pampulha, acionamento aprovado, táxi autorizado para o ponto de espera da pista UNO TRÊS via taxiway ALFA. Ajuste de altímetro UNO ZERO UNO TRÊS. Transponder QUATRO DOIS ZERO UNO. Próximo ao ponto de espera, chame a Torre Pampulha em UNO UNO OITO DECIMAL ZERO.
    </div>
    <div class="comms-pilot">
      Acionamento aprovado, táxi autorizado para o ponto de espera da pista UNO TRÊS via taxiway ALFA, ajuste de altímetro UNO ZERO UNO TRÊS, transponder QUATRO DOIS ZERO UNO, chamará a Torre Pampulha em UNO UNO OITO DECIMAL ZERO, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Pampulha Ground, **PAPA TANGO VICTOR BRAVO ROMEO**, good morning.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Pampulha Ground, good morning.
    </div>
    <div class="comms-pilot">
      Pampulha Ground, **PAPA TANGO VICTOR BRAVO ROMEO**, general aviation apron, a Cessna 172, VFR to Ipatinga, information ALFA, request startup and taxi instructions.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Ground, startup approved, taxi to holding point runway ONE THREE via taxiway ALFA. QNH ONE ZERO ONE THREE. Squawk FOUR TWO ZERO ONE. Approaching holding point, contact Pampulha Tower on ONE ONE EIGHT DECIMAL ZERO.
    </div>
    <div class="comms-pilot">
      Startup approved, taxi to holding point runway ONE THREE via taxiway ALFA, QNH ONE ZERO ONE THREE, squawk FOUR TWO ZERO ONE, will contact Pampulha Tower on ONE ONE EIGHT DECIMAL ZERO, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Pampulha Tierra, **PAPA TANGO VICTOR BRAVO ROMEO**, buenos días.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Pampulha Tierra, buenos días.
    </div>
    <div class="comms-pilot">
      Pampulha Tierra, **PAPA TANGO VICTOR BRAVO ROMEO**, plataforma de aviación general, un Cessna 172, VFR para Ipatinga, información ALFA, solicita puesta en marcha e instrucciones de rodaje.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Tierra, puesta en marcha aprobada, autorizado rodar al punto de espera de la pista UNO TRES vía calle ALFA. Ajuste de altímetro UNO CERO UNO TRES. Transponder CUATRO DOS CERO UNO. Próximo al punto de espera, llame Pampulha Torre en UNO UNO OCHO DECIMAL CERO.
    </div>
    <div class="comms-pilot">
      Puesta en marcha aprobada, autorizado rodar al punto de espera de la pista UNO TRES vía calle ALFA, ajuste de altímetro UNO CERO UNO TRES, transponder CUATRO DOS CERO UNO, llamará Pampulha Torre en UNO UNO OCHO DECIMAL CERO, **VICTOR BRAVO ROMEO**.
    </div>

??? abstract "A few remarks..."

    1. At aerodromes that have a **DELIVERY** position, the VFR departure clearance is issued before taxi. In that case, Ground handles only engine start and taxi.

        > :flag_br: **PAPA TANGO VICTOR BRAVO ROMEO**, Tráfego Pampulha, autorizado saída VFR para Ipatinga, mantenha VFR, após a decolagem saída pela perna do vento à esquerda, transponder QUATRO DOIS ZERO UNO. Coteje. <br/>
        > :flag_gb: **PAPA TANGO VICTOR BRAVO ROMEO**, Pampulha Delivery, cleared VFR departure to Ipatinga, maintain VFR, after departure leave via left downwind, squawk FOUR TWO ZERO ONE. Read back. <br/>
        > :flag_es: **PAPA TANGO VICTOR BRAVO ROMEO**, Pampulha Autorización, autorizada salida VFR para Ipatinga, mantenga VFR, después del despegue salida por el tramo con viento en cola por la izquierda, transponder CUATRO DOS CERO UNO. Colacione. <br/>

    2. General aviation aircraft rarely need a pushback. When the parking position allows leaving under the aircraft's own power, request engine start only.

    3. If you intend to stay in the circuit for training, say so already on contact with Ground, because it changes the Tower's planning.

        > :flag_br: Solo Pampulha, **PAPA TANGO VICTOR BRAVO ROMEO**, pátio da aviação geral, um Cessna 172, **voo local no circuito de tráfego**, informação ALFA, solicita acionamento e instruções de táxi. <br/>
        > :flag_gb: Pampulha Ground, **PAPA TANGO VICTOR BRAVO ROMEO**, general aviation apron, a Cessna 172, **local flight in the traffic circuit**, information ALFA, request startup and taxi instructions. <br/>
        > :flag_es: Pampulha Tierra, **PAPA TANGO VICTOR BRAVO ROMEO**, plataforma de aviación general, un Cessna 172, **vuelo local en el circuito de tránsito**, información ALFA, solicita puesta en marcha e instrucciones de rodaje. <br/>

## :material-numeric-2-box: :flag_br: Torre / :flag_gb: Tower / :flag_es: Torre

### Takeoff and leaving the circuit

The Tower clears the takeoff and states how the aircraft should leave the traffic circuit. This is where VFR operations differ most from IFR, since there is no published departure procedure to follow.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Torre Pampulha, **PAPA TANGO VICTOR BRAVO ROMEO**, ponto de espera da pista UNO TRÊS, pronto para a decolagem.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Torre Pampulha, pista UNO TRÊS, decolagem autorizada, vento UNO TRÊS ZERO graus, ZERO OITO nós. Após a decolagem, saída pela perna do vento à esquerda, reporte livre do circuito.
    </div>
    <div class="comms-pilot">
      Decolagem autorizada, pista UNO TRÊS, saída pela perna do vento à esquerda, reportará livre do circuito, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, livre do circuito, rumo leste, subindo para SETE MIL E QUINHENTOS pés.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, decolado aos UNO DOIS, chame o Controle Belo Horizonte em UNO UNO NOVE DECIMAL UNO. Bom voo!
    </div>
    <div class="comms-pilot">
      Chamará o Controle Belo Horizonte em UNO UNO NOVE DECIMAL UNO, **VICTOR BRAVO ROMEO**. Obrigado e bom controle!
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Pampulha Tower, **PAPA TANGO VICTOR BRAVO ROMEO**, holding point runway ONE THREE, ready for departure.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Tower, runway ONE THREE, cleared for take-off, wind ONE THREE ZERO degrees, ZERO EIGHT knots. After departure, leave via left downwind, report clear of the circuit.
    </div>
    <div class="comms-pilot">
      Cleared for take-off, runway ONE THREE, leaving via left downwind, will report clear of the circuit, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, clear of the circuit, eastbound, climbing to SEVEN THOUSAND FIVE HUNDRED feet.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, airborne at ONE TWO, contact Belo Horizonte Control on ONE ONE NINE DECIMAL ONE. Have a good flight!
    </div>
    <div class="comms-pilot">
      Will contact Belo Horizonte Control on ONE ONE NINE DECIMAL ONE, **VICTOR BRAVO ROMEO**. Thanks and have a good control!
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Pampulha Torre, **PAPA TANGO VICTOR BRAVO ROMEO**, punto de espera de la pista UNO TRES, listo para despegar.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Torre, pista UNO TRES, autorizado despegue, viento UNO TRES CERO grados, CERO OCHO nudos. Después del despegue, salida por el tramo con viento en cola por la izquierda, reporte libre del circuito.
    </div>
    <div class="comms-pilot">
      Autorizado despegue, pista UNO TRES, salida por el tramo con viento en cola por la izquierda, reportará libre del circuito, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, libre del circuito, rumbo este, ascendiendo a SIETE MIL QUINIENTOS pies.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, en el aire a los UNO DOS, llame Belo Horizonte Control en UNO UNO NUEVE DECIMAL UNO. ¡Buen vuelo!
    </div>
    <div class="comms-pilot">
      Llamará Belo Horizonte Control en UNO UNO NUEVE DECIMAL UNO, **VICTOR BRAVO ROMEO**. ¡Gracias y buen control!
    </div>

??? abstract "A few remarks..."

    1. The Tower may make the departure conditional on existing traffic, keeping the aircraft in the circuit until there is room.

        > :flag_br: **VICTOR BRAVO ROMEO**, pista UNO TRÊS, decolagem autorizada, vento UNO TRÊS ZERO graus, ZERO OITO nós. **Mantenha o circuito, aguarde instruções para a saída.** <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, runway ONE THREE, cleared for take-off, wind ONE THREE ZERO degrees, ZERO EIGHT knots. **Remain in the circuit, standby for departure instructions.** <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, pista UNO TRES, autorizado despegue, viento UNO TRES CERO grados, CERO OCHO nudos. **Manténgase en el circuito, espere instrucciones para la salida.** <br/>

    2. It is also common for the Tower to restrict the altitude while the aircraft is within the CTR.

        > :flag_br: **VICTOR BRAVO ROMEO**, após a decolagem, saída em frente, **mantenha DOIS MIL pés ou abaixo até deixar a CTR**, reporte livre do circuito. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, after departure, straight out, **maintain TWO THOUSAND feet or below until leaving the CTR**, report clear of the circuit. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, después del despegue, salida en línea recta, **mantenga DOS MIL pies o inferior hasta abandonar la CTR**, reporte libre del circuito. <br/>

    3. If the takeoff is from an intersection, state it in the holding point report, exactly as in instrument flight.

    4. Wind with a speed of zero knots (00000KT) must be reported as **wind calm**.

## :material-numeric-3-box: :flag_br: Controle / :flag_gb: Control / :flag_es: Control

### Leaving the CTR and the TMA

Within controlled airspace, visual flight remains subject to clearance. Control maintains surveillance, provides traffic information and releases the aircraft when it leaves its airspace.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Controle Belo Horizonte, **PAPA TANGO VICTOR BRAVO ROMEO**, decolado de Pampulha, VFR para Ipatinga, passando QUATRO MIL pés, subindo para SETE MIL E QUINHENTOS pés.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Controle Belo Horizonte, contato radar, MEIA milhas a leste de Pampulha. Mantenha VFR, subida a seu critério para SETE MIL E QUINHENTOS pés. Reporte deixando a TMA Belo Horizonte.
    </div>
    <div class="comms-pilot">
      Mantém VFR, sobe a critério para SETE MIL E QUINHENTOS pés, reportará deixando a TMA, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, informação de tráfego, um Seneca, DOIS milhas à sua frente, mesmo rumo, MEIA MIL pés.
    </div>
    <div class="comms-pilot">
      Tráfego à vista, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, deixando a TMA Belo Horizonte, SETE MIL E QUINHENTOS pés.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, serviço radar terminado aos DOIS OITO. Autorizada a troca de frequência, chame Informação Brasília em UNO DOIS CINCO DECIMAL TRÊS.
    </div>
    <div class="comms-pilot">
      Chamará Informação Brasília em UNO DOIS CINCO DECIMAL TRÊS, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Belo Horizonte Control, **PAPA TANGO VICTOR BRAVO ROMEO**, airborne from Pampulha, VFR to Ipatinga, passing FOUR THOUSAND feet, climbing to SEVEN THOUSAND FIVE HUNDRED feet.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Belo Horizonte Control, radar contact, SIX miles east of Pampulha. Maintain VFR, climb at your discretion to SEVEN THOUSAND FIVE HUNDRED feet. Report leaving Belo Horizonte TMA.
    </div>
    <div class="comms-pilot">
      Maintaining VFR, climbing at own discretion to SEVEN THOUSAND FIVE HUNDRED feet, will report leaving the TMA, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, traffic information, a Seneca, TWO miles ahead of you, same direction, SIX THOUSAND feet.
    </div>
    <div class="comms-pilot">
      Traffic in sight, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, leaving Belo Horizonte TMA, SEVEN THOUSAND FIVE HUNDRED feet.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, radar service terminated at TWO EIGHT. Frequency change approved, contact Brasília Information on ONE TWO FIVE DECIMAL THREE.
    </div>
    <div class="comms-pilot">
      Will contact Brasília Information on ONE TWO FIVE DECIMAL THREE, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Belo Horizonte Control, **PAPA TANGO VICTOR BRAVO ROMEO**, despegado de Pampulha, VFR para Ipatinga, pasando CUATRO MIL pies, ascendiendo a SIETE MIL QUINIENTOS pies.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Belo Horizonte Control, contacto radar, SEIS millas al este de Pampulha. Mantenga VFR, ascenso a su discreción a SIETE MIL QUINIENTOS pies. Reporte abandonando la TMA Belo Horizonte.
    </div>
    <div class="comms-pilot">
      Mantiene VFR, asciende a discreción a SIETE MIL QUINIENTOS pies, reportará abandonando la TMA, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, información de tráfico, un Seneca, DOS millas adelante, misma dirección, SEIS MIL pies.
    </div>
    <div class="comms-pilot">
      Tráfico a la vista, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, abandonando la TMA Belo Horizonte, SIETE MIL QUINIENTOS pies.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, servicio radar terminado a los DOS OCHO. Autorizado el cambio de frecuencia, llame Brasília Información en UNO DOS CINCO DECIMAL TRES.
    </div>
    <div class="comms-pilot">
      Llamará Brasília Información en UNO DOS CINCO DECIMAL TRES, **VICTOR BRAVO ROMEO**.
    </div>

??? abstract "A few remarks..."

    1. When traffic information is provided, the expected response is straightforward: **traffic in sight** or **negative contact**. If the traffic is not in sight, ATC will provide another form of separation.

        > :flag_br: **VICTOR BRAVO ROMEO**, tráfego não avistado. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, negative contact. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, tráfico no a la vista. <br/>

    2. Termination of radar service follows the same standard as in instrument flight, detailed in the [Important Tips](../fraseologia-aeronautica/dicas.en.md) of the Aeronautical Phraseology Manual. Replace the minute with the actual termination time, read digit by digit.

    3. Not every visual flight leaves controlled airspace. On short flights, Control may hand the aircraft over directly to the destination Tower.

## :material-numeric-4-box: :flag_br: Informação / :flag_gb: Information / :flag_es: Información

### En-route flight under the flight information service

Outside controlled airspace, the pilot operates under the flight information service. Here there are no clearances, only information. The pilot reports position and intentions, and the operator responds with conditions, known traffic and acknowledgement.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Informação Brasília, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Informação Brasília.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, um Cessna 172, VFR de Pampulha para Ipatinga, SETE MIL E QUINHENTOS pés, no través de João Monlevade, estimando Ipatinga aos QUATRO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Informação Brasília ciente. Tráfego conhecido é o PAPA TANGO KILO SIERRA ALFA, um EMB 110, VFR de Ipatinga para Pampulha, MEIA MIL E QUINHENTOS pés, rumo oposto, estimando João Monlevade aos TRÊS OITO. Reporte DEZ minutos fora de Ipatinga.
    </div>
    <div class="comms-pilot">
      Ciente do tráfego, reportará DEZ minutos fora de Ipatinga, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, DEZ minutos fora de Ipatinga.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Informação Brasília ciente, chame Rádio Ipatinga em UNO DOIS MEIA DECIMAL TRÊS.
    </div>
    <div class="comms-pilot">
      Chamará Rádio Ipatinga em UNO DOIS MEIA DECIMAL TRÊS, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Brasília Information, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Brasília Information.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, a Cessna 172, VFR from Pampulha to Ipatinga, SEVEN THOUSAND FIVE HUNDRED feet, abeam João Monlevade, estimating Ipatinga at FOUR FIVE.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Information roger. Known traffic is PAPA TANGO KILO SIERRA ALFA, an EMB 110, VFR from Ipatinga to Pampulha, SIX THOUSAND FIVE HUNDRED feet, opposite direction, estimating João Monlevade at THREE EIGHT. Report TEN minutes out of Ipatinga.
    </div>
    <div class="comms-pilot">
      Roger the traffic, will report TEN minutes out of Ipatinga, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, TEN minutes out of Ipatinga.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Information roger, contact Ipatinga Radio on ONE TWO SIX DECIMAL THREE.
    </div>
    <div class="comms-pilot">
      Will contact Ipatinga Radio on ONE TWO SIX DECIMAL THREE, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Brasília Información, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Brasília Información.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, un Cessna 172, VFR de Pampulha para Ipatinga, SIETE MIL QUINIENTOS pies, al través de João Monlevade, estimando Ipatinga a los CUATRO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Información recibido. Tráfico conocido es el PAPA TANGO KILO SIERRA ALFA, un EMB 110, VFR de Ipatinga para Pampulha, SEIS MIL QUINIENTOS pies, dirección opuesta, estimando João Monlevade a los TRES OCHO. Reporte DIEZ minutos afuera de Ipatinga.
    </div>
    <div class="comms-pilot">
      Recibido el tráfico, reportará DIEZ minutos afuera de Ipatinga, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, DIEZ minutos afuera de Ipatinga.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Información recibido, llame Ipatinga Radio en UNO DOS SEIS DECIMAL TRES.
    </div>
    <div class="comms-pilot">
      Llamará Ipatinga Radio en UNO DOS SEIS DECIMAL TRES, **VICTOR BRAVO ROMEO**.
    </div>

??? abstract "A few remarks..."

    1. En-route level changes outside controlled airspace are the pilot's decision. The operator only acknowledges them.

        > :flag_br: **VICTOR BRAVO ROMEO**, descendo para CINCO MIL E QUINHENTOS pés devido nuvens. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, descending to FIVE THOUSAND FIVE HUNDRED feet due to clouds. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, descendiendo a CINCO MIL QUINIENTOS pies debido a nubes. <br/><br/>
        > :flag_br: **VICTOR BRAVO ROMEO**, Informação Brasília ciente. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, Brasília Information roger. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, Brasília Información recibido. <br/>

    2. Weather deviations are reported, not requested.

        > :flag_br: **VICTOR BRAVO ROMEO**, desviando à direita devido formação. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, right deviation due weather. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, desviando a la derecha debido a formación. <br/>

    3. If the flight needs to re-enter controlled airspace, the operator provides the frequency to be contacted.

        > :flag_br: **VICTOR BRAVO ROMEO**, ao ingressar no espaço aéreo controlado, chame o Controle Belo Horizonte em UNO UNO NOVE DECIMAL UNO. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, when entering controlled airspace, contact Belo Horizonte Control on ONE ONE NINE DECIMAL ONE. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, al ingresar en el espacio aéreo controlado, llame Belo Horizonte Control en UNO UNO NUEVE DECIMAL UNO. <br/>

## :material-numeric-5-box: :flag_br: Rádio / :flag_gb: Radio / :flag_es: Radio

### Arrival at the uncontrolled aerodrome

At an aerodrome served by an aeronautical station, the pilot requests information, receives the conditions and **states their intentions**. The station does not clear landings, does not sequence and does not separate traffic. The pilot decides, based on the information received.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Rádio Ipatinga, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Rádio Ipatinga.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, um Cessna 172, procedente de Pampulha, DEZ minutos fora, a sudoeste, SETE MIL E QUINHENTOS pés, solicita informações.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente. Vento UNO TRÊS ZERO graus, ZERO MEIA nós, pista utilizada por outras aeronaves é a UNO DOIS, ajuste de altímetro UNO ZERO UNO DOIS, temperatura DOIS QUATRO graus, aeródromo opera visual, CAVOK. Tráfego conhecido é o PAPA TANGO KILO LIMA CHARLIE, um Cessna 182, na perna do vento da pista UNO DOIS para toque e arremetida. Informe intenções.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO** ciente, ingressará no início da perna do vento da pista UNO DOIS para pouso.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, reporte na perna do vento.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Ipatinga Radio, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Ipatinga Radio.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, a Cessna 172, from Pampulha, TEN minutes out, southwest, SEVEN THOUSAND FIVE HUNDRED feet, request information.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger. Wind ONE THREE ZERO degrees, ZERO SIX knots, runway ONE TWO is being used by other aircraft, altimeter setting ONE ZERO ONE TWO, temperature TWO FOUR degrees, aerodrome under visual conditions, CAVOK. Known traffic is PAPA TANGO KILO LIMA CHARLIE, a Cessna 182, on downwind leg runway ONE TWO for touch and go. Advise intentions.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO** roger, will join early downwind leg runway ONE TWO for landing.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, report downwind leg.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Ipatinga Radio, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Ipatinga Radio.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, un Cessna 172, procedente de Pampulha, DIEZ minutos afuera, al suroeste, SIETE MIL QUINIENTOS pies, solicita información.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido. Viento UNO TRES CERO grados, CERO SEIS nudos, la pista utilizada por otras aeronaves es la UNO DOS, ajuste de altímetro UNO CERO UNO DOS, temperatura DOS CUATRO grados, aeródromo en condiciones visuales, CAVOK. Tráfico conocido es el PAPA TANGO KILO LIMA CHARLIE, un Cessna 182, en el tramo con viento en cola de la pista UNO DOS para toque y despegue. Informe intenciones.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO** recibido, ingresará al inicio del tramo con viento en cola de la pista UNO DOS para aterrizar.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, reporte en el tramo con viento en cola.
    </div>

??? abstract "A few remarks..."

    1. The runway reported by the aeronautical station is the **runway being used by other aircraft**, not an assigned runway. The final choice belongs to the pilot in command, who must take into account the wind, existing traffic and aircraft performance.

    2. If the aerodrome is below visual minima, the station reports the condition and leaves the decision to the pilot.

        > :flag_br: **VICTOR BRAVO ROMEO**, vento ZERO OITO ZERO graus, ZERO SETE nós, ajuste de altímetro UNO ZERO UNO DOIS, temperatura TRÊS DOIS graus, **aeródromo abaixo dos mínimos visuais, visibilidade estimada DOIS MIL metros, teto MEIA ZERO ZERO pés**, informe intenções. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, wind ZERO EIGHT ZERO degrees, ZERO SEVEN knots, altimeter setting ONE ZERO ONE TWO, temperature THREE TWO degrees, **aerodrome below visual minima, estimated visibility TWO THOUSAND meters, ceiling SIX HUNDRED feet**, advise intentions. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, viento CERO OCHO CERO grados, CERO SIETE nudos, ajuste de altímetro UNO CERO UNO DOS, temperatura TRES DOS grados, **aeródromo por debajo de los mínimos visuales, visibilidad estimada DOS MIL metros, techo SEIS CERO CERO pies**, informe intenciones. <br/><br/>
        > :flag_br: **VICTOR BRAVO ROMEO** ciente, irá prosseguir para a alternativa Governador Valadares. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO** roger, will proceed to alternate Governador Valadares. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO** recibido, procederá al alternativo Governador Valadares. <br/>

    3. When no aeronautical station is on the air, reports are still made, as blind transmissions, on the aerodrome frequency. Announce your position and intentions on each leg, even without a reply.

## :material-numeric-6-box: Traffic circuit and landing

From joining to touchdown, each leg generates a report. At an uncontrolled aerodrome, the reports allow other traffic to build their own situational awareness.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, perna do vento da pista UNO DOIS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, o KILO LIMA CHARLIE está na perna base da pista UNO DOIS para toque e arremetida. Reporte perna base.
    </div>
    <div class="comms-pilot">
      Ciente do tráfego, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, perna base da pista UNO DOIS, trem de pouso baixado e travado, tráfego à vista.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, na final.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, vento UNO TRÊS ZERO graus, ZERO MEIA nós, reporte no solo.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, no solo aos QUATRO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, reporte pista livre.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, pista livre.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, downwind leg runway ONE TWO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, KILO LIMA CHARLIE is on base leg runway ONE TWO for touch and go. Report base leg.
    </div>
    <div class="comms-pilot">
      Roger the traffic, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, base leg runway ONE TWO, landing gear down and locked, traffic in sight.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, on final.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, wind ONE THREE ZERO degrees, ZERO SIX knots, report on the ground.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, on the ground at FOUR FIVE.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, report runway vacated.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, runway vacated.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, tramo con viento en cola de la pista UNO DOS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, el KILO LIMA CHARLIE está en el tramo base de la pista UNO DOS para toque y despegue. Reporte tramo base.
    </div>
    <div class="comms-pilot">
      Recibido el tráfico, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, tramo base de la pista UNO DOS, tren de aterrizaje abajo y asegurado, tráfico a la vista.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, en final.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, viento UNO TRES CERO grados, CERO SEIS nudos, reporte en tierra.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, en tierra a los CUATRO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, reporte pista libre.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, pista libre.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido.
    </div>

!!! danger "Never say this on an aeronautical station"
    Expressions such as **cleared to land**, **cleared for take-off**, **cleared to join** and **number TWO for landing** imply air traffic control and **may not** be used by a **RADIO** station. If you are staffing the position, inform and acknowledge, never clear.

## :material-numeric-7-box: Taxi and closing

After vacating the runway, the pilot reports where they intend to park and closes the flight plan.

=== ":flag_br: Portuguese"
    <div class="comms-pilot">
      Rádio Ipatinga, **VICTOR BRAVO ROMEO**, taxiando para o pátio da aviação geral, solicita encerramento do plano de voo.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, plano de voo encerrado aos QUATRO SETE.
    </div>
    <div class="comms-pilot">
      Ciente, obrigado e boa tarde, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: English"
    <div class="comms-pilot">
      Ipatinga Radio, **VICTOR BRAVO ROMEO**, taxiing to the general aviation apron, request flight plan closure.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, flight plan closed at FOUR SEVEN.
    </div>
    <div class="comms-pilot">
      Roger, thank you and good afternoon, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Spanish"
    <div class="comms-pilot">
      Ipatinga Radio, **VICTOR BRAVO ROMEO**, rodando a la plataforma de aviación general, solicita cierre del plan de vuelo.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, plan de vuelo cerrado a los CUATRO SIETE.
    </div>
    <div class="comms-pilot">
      Recibido, gracias y buenas tardes, **VICTOR BRAVO ROMEO**.
    </div>

!!! tip "Do not invent requests"
    As in instrument flight, avoid requests not provided for in the regulations, such as "request shutdown and disembarkation". Report only what is operationally relevant.

---
