---
title: Voo de Volta (Não Controlado para Controlado)
icon: material/microphone-variant
---

--8<-- "includes/abreviacoes.md"

![Manual de Fraseologia para Voo Visual - Voo de Volta](img/manual-fraseologia-voo-visual-volta.png)

#

## :material-numeric-0-box: Preliminares

<section markdown style="display: grid; grid-template-columns: 5fr 2fr">

<div markdown>

Na volta, o sentido se inverte. O **PT-VBR** parte de **Ipatinga (SBIP)**, aeródromo não controlado atendido por estação aeronáutica, e regressa a **Pampulha (SBBH)**, aeródromo controlado, com cruzeiro em **6.500 pés**.

Como na ida, o **nível de transição está em 080** e todo o voo acontece abaixo dele, em altitude referenciada ao QNH.

É aqui que aparecem as duas situações mais cobradas em treinamento VFR: a **partida sem controle**, em que o piloto conduz a operação e apenas informa cada passo, e a **entrada no circuito de tráfego controlado**, em que a Torre autoriza, sequencia e organiza o fluxo.

</div>

<div style="text-align: center;">
``` mermaid
flowchart TD
  RDO(RÁDIO);
  RDO --> FIS(INFORMAÇÃO);
  FIS --> APP(CONTROLE);
  APP --> TWR(TORRE);
  TWR --> GND(SOLO);
```
</div>

</section>

## :material-numeric-1-box: :flag_br: Rádio / :flag_gb: Radio / :flag_es: Radio

### Partida com plano de voo visual

Na partida de aeródromo não controlado, o piloto anuncia cada fase e a estação responde com informações e ciência. Repare que não há autorização em nenhum momento.

=== ":flag_br: Português"
    <div class="comms-pilot">
      Rádio Ipatinga, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Rádio Ipatinga.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, iniciando o táxi, pista UNO DOIS, destino Pampulha, solicita informações.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente. Vento UNO TRÊS ZERO graus, ZERO CINCO nós. Ajuste de altímetro UNO ZERO UNO DOIS. Temperatura DOIS CINCO graus. Sem tráfego conhecido. Hora certa UNO OITO. Reporte no ponto de espera.
    </div>
    <div class="comms-pilot">
      Ciente, taxiando para o ponto de espera da pista UNO DOIS, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, no ponto de espera da pista UNO DOIS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, reporte alinhado para a decolagem.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, ingressa na cabeceira UNO DOIS, alinhado.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, vento UNO TRÊS ZERO graus, ZERO CINCO nós, reporte fora do solo.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, fora do solo aos DOIS DOIS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, atinge e mantém MEIA MIL E QUINHENTOS pés, rumo oeste, estimando Pampulha aos ZERO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente, chame Informação Brasília em UNO DOIS CINCO DECIMAL TRÊS.
    </div>

=== ":flag_gb: Inglês"
    <div class="comms-pilot">
      Ipatinga Radio, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Ipatinga Radio.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, commencing taxi, runway ONE TWO, destination Pampulha, request information.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger. Wind ONE THREE ZERO degrees, ZERO FIVE knots. Altimeter setting ONE ZERO ONE TWO. Temperature TWO FIVE degrees. No reported traffic. Time check ONE EIGHT. Report holding point.
    </div>
    <div class="comms-pilot">
      Roger, taxiing to holding point runway ONE TWO, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, holding point runway ONE TWO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, report lined up for departure.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, entering runway ONE TWO, lined up.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, wind ONE THREE ZERO degrees, ZERO FIVE knots, report airborne.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, airborne at TWO TWO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, reaching and maintaining SIX THOUSAND FIVE HUNDRED feet, westbound, estimating Pampulha at ZERO FIVE.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio roger, contact Brasília Information on ONE TWO FIVE DECIMAL THREE.
    </div>

=== ":flag_es: Espanhol"
    <div class="comms-pilot">
      Ipatinga Radio, **PAPA TANGO VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **PAPA TANGO VICTOR BRAVO ROMEO**, Ipatinga Radio.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, iniciando el rodaje, pista UNO DOS, destino Pampulha, solicita información.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido. Viento UNO TRES CERO grados, CERO CINCO nudos. Ajuste de altímetro UNO CERO UNO DOS. Temperatura DOS CINCO grados. Sin tráfico conocido. Hora UNO OCHO. Reporte en el punto de espera.
    </div>
    <div class="comms-pilot">
      Recibido, rodando al punto de espera de la pista UNO DOS, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, en el punto de espera de la pista UNO DOS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, reporte alineado para el despegue.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, ingresa en la cabecera UNO DOS, alineado.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, viento UNO TRES CERO grados, CERO CINCO nudos, reporte en el aire.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, en el aire a los DOS DOS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, alcanza y mantiene SEIS MIL QUINIENTOS pies, rumbo oeste, estimando Pampulha a los CERO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido, llame Brasília Información en UNO DOS CINCO DECIMAL TRES.
    </div>

??? abstract "Algumas observações..."

    1. Havendo tráfego conhecido, a estação o descreve com detalhe suficiente para que o piloto construa a própria separação.

        > :flag_br: **VICTOR BRAVO ROMEO**, Rádio Ipatinga ciente. Vento UNO TRÊS ZERO graus, ZERO CINCO nós. Ajuste de altímetro UNO ZERO UNO DOIS. **Tráfego conhecido é o PAPA SIERRA ROMEO ECHO TANGO, um Xingu, na perna do vento da pista UNO DOIS.** Reporte no ponto de espera. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, Ipatinga Radio roger. Wind ONE THREE ZERO degrees, ZERO FIVE knots. Altimeter setting ONE ZERO ONE TWO. **Known traffic is PAPA SIERRA ROMEO ECHO TANGO, a Xingu, on downwind leg runway ONE TWO.** Report holding point. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, Ipatinga Radio recibido. Viento UNO TRES CERO grados, CERO CINCO nudos. Ajuste de altímetro UNO CERO UNO DOS. **Tráfico conocido es el PAPA SIERRA ROMEO ECHO TANGO, un Xingu, en el tramo con viento en cola de la pista UNO DOS.** Reporte en el punto de espera. <br/>

    2. Quando o piloto decide aguardar por causa de outro tráfego, ele informa a decisão. A estação apenas toma ciência.

        > :flag_br: **VICTOR BRAVO ROMEO**, no ponto de espera, mantém posição, aguardando o pouso do Xingu. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, holding point, maintaining position, waiting for the Xingu landing. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, en el punto de espera, mantiene posición, esperando el aterrizaje del Xingu. <br/>

    3. A **hora certa** é fornecida pela estação porque, sem órgão de controle, o horário de decolagem reportado pelo piloto é o registro oficial do movimento.

## :material-numeric-2-box: :flag_br: Informação / :flag_gb: Information / :flag_es: Información

### Reporte de posição em rota

O contato com o serviço de informação de voo é breve e objetivo: quem sou, o que sou, de onde para onde, em que altitude, onde estou e qual o estimado.

=== ":flag_br: Português"
    <div class="comms-pilot">
      Informação Brasília, **PAPA TANGO VICTOR BRAVO ROMEO**, um Cessna 172, VFR de Ipatinga para Pampulha, MEIA MIL E QUINHENTOS pés, DOIS ZERO milhas a oeste de Ipatinga, estimando Pampulha aos ZERO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Informação Brasília ciente. Sem tráfego conhecido na sua rota. Reporte DEZ minutos fora de Pampulha.
    </div>
    <div class="comms-pilot">
      Reportará DEZ minutos fora de Pampulha, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, DEZ minutos fora de Pampulha, MEIA MIL E QUINHENTOS pés.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Informação Brasília ciente. Ao ingressar no espaço aéreo controlado, chame o Controle Belo Horizonte em UNO UNO NOVE DECIMAL UNO.
    </div>
    <div class="comms-pilot">
      Chamará o Controle Belo Horizonte em UNO UNO NOVE DECIMAL UNO, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: Inglês"
    <div class="comms-pilot">
      Brasília Information, **PAPA TANGO VICTOR BRAVO ROMEO**, a Cessna 172, VFR from Ipatinga to Pampulha, SIX THOUSAND FIVE HUNDRED feet, TWO ZERO miles west of Ipatinga, estimating Pampulha at ZERO FIVE.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Information roger. No reported traffic on your route. Report TEN minutes out of Pampulha.
    </div>
    <div class="comms-pilot">
      Will report TEN minutes out of Pampulha, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, TEN minutes out of Pampulha, SIX THOUSAND FIVE HUNDRED feet.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Information roger. When entering controlled airspace, contact Belo Horizonte Control on ONE ONE NINE DECIMAL ONE.
    </div>
    <div class="comms-pilot">
      Will contact Belo Horizonte Control on ONE ONE NINE DECIMAL ONE, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Espanhol"
    <div class="comms-pilot">
      Brasília Información, **PAPA TANGO VICTOR BRAVO ROMEO**, un Cessna 172, VFR de Ipatinga para Pampulha, SEIS MIL QUINIENTOS pies, DOS CERO millas al oeste de Ipatinga, estimando Pampulha a los CERO CINCO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Información recibido. Sin tráfico conocido en su ruta. Reporte DIEZ minutos afuera de Pampulha.
    </div>
    <div class="comms-pilot">
      Reportará DIEZ minutos afuera de Pampulha, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, DIEZ minutos afuera de Pampulha, SEIS MIL QUINIENTOS pies.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Brasília Información recibido. Al ingresar en el espacio aéreo controlado, llame Belo Horizonte Control en UNO UNO NUEVE DECIMAL UNO.
    </div>
    <div class="comms-pilot">
      Llamará Belo Horizonte Control en UNO UNO NUEVE DECIMAL UNO, **VICTOR BRAVO ROMEO**.
    </div>

## :material-numeric-3-box: :flag_br: Controle / :flag_gb: Control / :flag_es: Control

### Ingresso na TMA e na CTR

O ingresso em espaço aéreo controlado depende de autorização. O piloto solicita, informando posição, altitude e intenção, e o Controle responde com o código transponder, a autorização e eventuais restrições.

=== ":flag_br: Português"
    <div class="comms-pilot">
      Controle Belo Horizonte, **PAPA TANGO VICTOR BRAVO ROMEO**, um Cessna 172, VFR de Ipatinga para Pampulha, MEIA MIL E QUINHENTOS pés, DOIS CINCO milhas a nordeste de Pampulha, solicita ingresso na TMA para pouso em Pampulha.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Controle Belo Horizonte, transponder QUATRO DOIS ZERO TRÊS.
    </div>
    <div class="comms-pilot">
      Transponder QUATRO DOIS ZERO TRÊS, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, contato radar, DOIS CINCO milhas a nordeste de Pampulha. Autorizado ingresso na TMA Belo Horizonte, mantenha VFR, desça para QUATRO MIL E QUINHENTOS pés, Q N H UNO ZERO UNO TRÊS.
    </div>
    <div class="comms-pilot">
      Autorizado ingresso na TMA, mantém VFR, desce para QUATRO MIL E QUINHENTOS pés, Q N H UNO ZERO UNO TRÊS, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, informação de tráfego, um ATR 72 em aproximação para Confins, TRÊS milhas ao norte, MEIA MIL pés em descida.
    </div>
    <div class="comms-pilot">
      Tráfego à vista, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, chame a Torre Pampulha em UNO UNO OITO DECIMAL ZERO.
    </div>
    <div class="comms-pilot">
      Chamará a Torre Pampulha em UNO UNO OITO DECIMAL ZERO, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: Inglês"
    <div class="comms-pilot">
      Belo Horizonte Control, **PAPA TANGO VICTOR BRAVO ROMEO**, a Cessna 172, VFR from Ipatinga to Pampulha, SIX THOUSAND FIVE HUNDRED feet, TWO FIVE miles northeast of Pampulha, request TMA entry for landing at Pampulha.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Belo Horizonte Control, squawk FOUR TWO ZERO THREE.
    </div>
    <div class="comms-pilot">
      Squawk FOUR TWO ZERO THREE, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, radar contact, TWO FIVE miles northeast of Pampulha. Cleared to enter Belo Horizonte TMA, maintain VFR, descend to FOUR THOUSAND FIVE HUNDRED feet, Q N H ONE ZERO ONE THREE.
    </div>
    <div class="comms-pilot">
      Cleared to enter the TMA, maintaining VFR, descending to FOUR THOUSAND FIVE HUNDRED feet, Q N H ONE ZERO ONE THREE, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, traffic information, an ATR 72 on approach to Confins, THREE miles north, SIX THOUSAND feet descending.
    </div>
    <div class="comms-pilot">
      Traffic in sight, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, contact Pampulha Tower on ONE ONE EIGHT DECIMAL ZERO.
    </div>
    <div class="comms-pilot">
      Will contact Pampulha Tower on ONE ONE EIGHT DECIMAL ZERO, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Espanhol"
    <div class="comms-pilot">
      Belo Horizonte Control, **PAPA TANGO VICTOR BRAVO ROMEO**, un Cessna 172, VFR de Ipatinga para Pampulha, SEIS MIL QUINIENTOS pies, DOS CINCO millas al noreste de Pampulha, solicita ingreso a la TMA para aterrizar en Pampulha.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Belo Horizonte Control, transponder CUATRO DOS CERO TRES.
    </div>
    <div class="comms-pilot">
      Transponder CUATRO DOS CERO TRES, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, contacto radar, DOS CINCO millas al noreste de Pampulha. Autorizado el ingreso a la TMA Belo Horizonte, mantenga VFR, descienda a CUATRO MIL QUINIENTOS pies, Q N H UNO CERO UNO TRES.
    </div>
    <div class="comms-pilot">
      Autorizado el ingreso a la TMA, mantiene VFR, desciende a CUATRO MIL QUINIENTOS pies, Q N H UNO CERO UNO TRES, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, información de tráfico, un ATR 72 en aproximación a Confins, TRES millas al norte, SEIS MIL pies en descenso.
    </div>
    <div class="comms-pilot">
      Tráfico a la vista, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, llame Pampulha Torre en UNO UNO OCHO DECIMAL CERO.
    </div>
    <div class="comms-pilot">
      Llamará Pampulha Torre en UNO UNO OCHO DECIMAL CERO, **VICTOR BRAVO ROMEO**.
    </div>

??? abstract "Algumas observações..."

    1. O Controle pode negar ou condicionar o ingresso por volume de tráfego. Nesse caso, a aeronave deve permanecer fora do espaço aéreo controlado.

        > :flag_br: **VICTOR BRAVO ROMEO**, mantenha fora da TMA Belo Horizonte, aguarde autorização para o ingresso. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, remain outside Belo Horizonte TMA, standby for entry clearance. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, manténgase fuera de la TMA Belo Horizonte, espere autorización para el ingreso. <br/>

    2. É comum o Controle definir um ponto de notificação visual para o ingresso na CTR. Consulte a carta do aeródromo e informe o ponto no reporte.

        > :flag_br: **VICTOR BRAVO ROMEO**, autorizado ingresso na CTR Belo Horizonte via Lagoa da Pampulha, mantenha DOIS MIL E QUINHENTOS pés ou abaixo, reporte sobre o ponto. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, cleared to enter Belo Horizonte CTR via Pampulha Lake, maintain TWO THOUSAND FIVE HUNDRED feet or below, report over the point. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, autorizado el ingreso a la CTR Belo Horizonte vía Laguna de Pampulha, mantenga DOS MIL QUINIENTOS pies o inferior, reporte sobre el punto. <br/>

## :material-numeric-4-box: :flag_br: Torre / :flag_gb: Tower / :flag_es: Torre

### Entrada no circuito de tráfego

Este é o contato mais importante da chegada. O piloto informa posição, altitude e o que deseja. A Torre responde com a autorização para o circuito, a pista em uso, o vento, o ajuste de altímetro e o reporte esperado.

=== ":flag_br: Português"
    <div class="comms-pilot">
      Torre Pampulha, **PAPA TANGO VICTOR BRAVO ROMEO**, UNO ZERO milhas a nordeste do aeródromo, QUATRO MIL E QUINHENTOS pés, solicita instruções para pouso.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Torre Pampulha, autorizado para o circuito de tráfego, pista UNO TRÊS, vento UNO TRÊS ZERO graus, UNO ZERO nós, ajuste de altímetro UNO ZERO UNO TRÊS, reporte perna do vento.
    </div>
    <div class="comms-pilot">
      Autorizado para o circuito de tráfego, pista UNO TRÊS, ajuste de altímetro UNO ZERO UNO TRÊS, reportará perna do vento, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, perna do vento da pista UNO TRÊS.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, avistado, é o número DOIS para o pouso, siga o Cessna na perna base, reporte perna base.
    </div>
    <div class="comms-pilot">
      Tráfego à vista, é o número DOIS, reportará perna base, **VICTOR BRAVO ROMEO**.
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

=== ":flag_gb: Inglês"
    <div class="comms-pilot">
      Pampulha Tower, **PAPA TANGO VICTOR BRAVO ROMEO**, ONE ZERO miles northeast of the aerodrome, FOUR THOUSAND FIVE HUNDRED feet, request landing instructions.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Tower, cleared to traffic pattern, runway ONE THREE, wind ONE THREE ZERO degrees, ONE ZERO knots, QNH ONE ZERO ONE THREE, report downwind leg.
    </div>
    <div class="comms-pilot">
      Cleared to traffic pattern, runway ONE THREE, QNH ONE ZERO ONE THREE, will report downwind leg, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, downwind leg runway ONE THREE.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, I have you in sight, number TWO for landing, follow the Cessna on base leg, report base leg.
    </div>
    <div class="comms-pilot">
      Traffic in sight, number TWO, will report base leg, **VICTOR BRAVO ROMEO**.
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

=== ":flag_es: Espanhol"
    <div class="comms-pilot">
      Pampulha Torre, **PAPA TANGO VICTOR BRAVO ROMEO**, UNO CERO millas al noreste del aeródromo, CUATRO MIL QUINIENTOS pies, solicita instrucciones para aterrizar.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Torre, autorizado al circuito de tránsito, pista UNO TRES, viento UNO TRES CERO grados, UNO CERO nudos, ajuste de altímetro UNO CERO UNO TRES, reporte tramo con viento en cola.
    </div>
    <div class="comms-pilot">
      Autorizado al circuito de tránsito, pista UNO TRES, ajuste de altímetro UNO CERO UNO TRES, reportará tramo con viento en cola, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      **VICTOR BRAVO ROMEO**, tramo con viento en cola de la pista UNO TRES.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, a la vista, es el número DOS para aterrizar, siga al Cessna en el tramo base, reporte tramo base.
    </div>
    <div class="comms-pilot">
      Tráfico a la vista, es el número DOS, reportará tramo base, **VICTOR BRAVO ROMEO**.
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

??? abstract "Algumas observações..."

    1. A Torre pode determinar o lado do circuito no momento da autorização, o que é frequente em aeródromos com restrições de sobrevoo.

        > :flag_br: **VICTOR BRAVO ROMEO**, faça aproximação pela direita, pista ZERO DOIS, vento ZERO QUATRO ZERO graus, UNO ZERO nós, ajuste de altímetro UNO ZERO UNO QUATRO, reporte perna base. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, make right hand approach, runway ZERO TWO, wind ZERO FOUR ZERO degrees, ONE ZERO knots, QNH ONE ZERO ONE FOUR, report base leg. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, efectúe aproximación por la derecha, pista CERO DOS, viento CERO CUATRO CERO grados, UNO CERO nudos, ajuste de altímetro UNO CERO UNO CUATRO, reporte tramo base. <br/>

    2. Quando a aeronave chega alinhada com a pista, a Torre pode autorizar a aproximação direta e economizar todo o circuito.

        > :flag_br: **VICTOR BRAVO ROMEO**, autorizada aproximação direta, pista UNO TRÊS, vento UNO CINCO ZERO graus, UNO CINCO nós, Q N H UNO ZERO UNO TRÊS, reporte final. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, cleared straight in approach, runway ONE THREE, wind ONE FIVE ZERO degrees, ONE FIVE knots, Q N H ONE ZERO ONE THREE, report final. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, autorizada aproximación directa, pista UNO TRES, viento UNO CINCO CERO grados, UNO CINCO nudos, Q N H UNO CERO UNO TRES, reporte final. <br/>

    3. Se a pista ainda estiver ocupada, a autorização de pouso não sai no contato de final.

        > :flag_br: **VICTOR BRAVO ROMEO**, pista UNO TRÊS, continue aproximação, aguarde pista livre, vento UNO TRÊS ZERO graus, UNO ZERO nós. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, runway ONE THREE, continue approach, standby for runway vacated, wind ONE THREE ZERO degrees, ONE ZERO knots. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, pista UNO TRES, continúe aproximación, espere pista libre, viento UNO TRES CERO grados, UNO CERO nudos. <br/>

## :material-numeric-5-box: Após o pouso

Depois do toque, a Torre informa a hora de pouso, a saída da pista e a transferência para o Solo.

=== ":flag_br: Português"
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, pousado aos ZERO CINCO, livre à esquerda na taxiway BRAVO, ao livrar chame o Solo Pampulha em UNO DOIS UNO DECIMAL MEIA.
    </div>
    <div class="comms-pilot">
      Livre à esquerda na BRAVO, chamará o Solo Pampulha em UNO DOIS UNO DECIMAL MEIA, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      Solo Pampulha, **PAPA TANGO VICTOR BRAVO ROMEO**, livrou a pista UNO TRÊS na BRAVO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Solo Pampulha, táxi autorizado para o pátio da aviação geral via taxiway BRAVO.
    </div>
    <div class="comms-pilot">
      Táxi autorizado para o pátio da aviação geral via taxiway BRAVO, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_gb: Inglês"
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, landed at ZERO FIVE, vacate left on taxiway BRAVO, when vacated contact Pampulha Ground on ONE TWO ONE DECIMAL SIX.
    </div>
    <div class="comms-pilot">
      Vacating left on BRAVO, will contact Pampulha Ground on ONE TWO ONE DECIMAL SIX, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      Pampulha Ground, **PAPA TANGO VICTOR BRAVO ROMEO**, vacated runway ONE THREE at BRAVO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Ground, taxi to the general aviation apron via taxiway BRAVO.
    </div>
    <div class="comms-pilot">
      Taxi to the general aviation apron via taxiway BRAVO, **VICTOR BRAVO ROMEO**.
    </div>

=== ":flag_es: Espanhol"
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, aterrizado a los CERO CINCO, salga por la izquierda en la calle BRAVO, al salir llame Pampulha Tierra en UNO DOS UNO DECIMAL SEIS.
    </div>
    <div class="comms-pilot">
      Sale por la izquierda en BRAVO, llamará Pampulha Tierra en UNO DOS UNO DECIMAL SEIS, **VICTOR BRAVO ROMEO**.
    </div>
    <div class="comms-pilot">
      Pampulha Tierra, **PAPA TANGO VICTOR BRAVO ROMEO**, salió de la pista UNO TRES en BRAVO.
    </div>
    <div class="comms-atc">
      **VICTOR BRAVO ROMEO**, Pampulha Tierra, autorizado rodar a la plataforma de aviación general vía calle BRAVO.
    </div>
    <div class="comms-pilot">
      Autorizado rodar a la plataforma de aviación general vía calle BRAVO, **VICTOR BRAVO ROMEO**.
    </div>

!!! tip "Voo completo"
    Com a ida e a volta, você percorreu todos os órgãos que um voo visual pode encontrar no Brasil. O que sobra são as variações, e é exatamente disso que trata a próxima página.

---
