---
title: Circuito de Tráfego
icon: material/vector-square
---

--8<-- "includes/abreviacoes.md"

![Manual de Fraseologia para Voo Visual - Circuito de Tráfego](img/manual-fraseologia-voo-visual-circuito.png)

#

O circuito de tráfego é o retângulo voado ao redor da pista em uso. Ele existe para que todo mundo faça a mesma coisa, no mesmo lugar, na mesma altitude, tornando previsível o comportamento de cada aeronave.

Para o piloto VFR, o circuito é o momento em que a fonia fica mais densa e mais padronizada. Cada perna tem um reporte, e cada reporte tem uma resposta esperada.

## As pernas do circuito

O desenho abaixo reproduz o traçado que aparece nas cartas de aproximação visual: um hipódromo com a **pista em uso ao centro** e o sentido de voo indicado pelas setas. O exemplo é um **circuito à esquerda**, ou seja, todas as curvas são para a esquerda.

Repare em uma coisa que confunde muita gente: apenas a **final** e a **subida após a decolagem** correm sobre o eixo da pista, a linha que atravessa o circuito pelo meio. A **perna contra o vento** e a **perna do vento** são paralelas à pista, porém **deslocadas lateralmente**, uma para cada lado do eixo.

<div style="overflow-x: auto; margin: 1.5rem 0;">
<svg viewBox="0 0 820 420" width="100%" role="img" aria-labelledby="circ-titulo circ-desc" style="max-width: 820px; display: block; margin: 0 auto;">
  <title id="circ-titulo">Circuito de tráfego padrão à esquerda</title>
  <desc id="circ-desc">Hipódromo do circuito com a pista em uso ao centro. O eixo da pista atravessa o circuito e sustenta a final e a subida após a decolagem. As pernas contra o vento e do vento correm paralelas à pista, deslocadas para cada lado do eixo.</desc>

  <rect x="150" y="80" width="560" height="260" rx="90" ry="90" fill="none" stroke="currentColor" stroke-width="4"/>

  <line x1="150" y1="210" x2="710" y2="210" stroke="currentColor" stroke-width="3"/>
  <rect x="330" y="200" width="200" height="20" fill="var(--md-default-bg-color)" stroke="currentColor" stroke-width="3"/>

  <polygon points="432,333 450,340 432,347" fill="currentColor"/>
  <polygon points="428,73 410,80 428,87" fill="currentColor"/>
  <polygon points="703,168 710,150 717,168" fill="currentColor"/>
  <polygon points="143,252 150,270 157,252" fill="currentColor"/>
  <polygon points="282,203 300,210 282,217" fill="currentColor"/>
  <polygon points="602,203 620,210 602,217" fill="currentColor"/>

  <text x="430" y="62" font-size="17" text-anchor="middle" fill="currentColor">Perna do vento</text>
  <text x="430" y="368" font-size="17" text-anchor="middle" fill="currentColor">Perna contra o vento</text>
  <text x="752" y="210" font-size="17" text-anchor="middle" fill="currentColor" transform="rotate(-90 752 210)">Través</text>
  <text x="108" y="210" font-size="17" text-anchor="middle" fill="currentColor" transform="rotate(-90 108 210)">Perna base</text>

  <text x="238" y="192" font-size="17" text-anchor="middle" fill="currentColor">Final</text>
  <text x="430" y="250" font-size="15" text-anchor="middle" fill="currentColor" font-style="italic">pista em uso</text>
  <text x="612" y="192" font-size="15" text-anchor="middle" fill="currentColor" font-style="italic">subida após a decolagem</text>
</svg>
</div>

| Ordem | Perna | O que é | Reporte típico |
| --- | --- | --- | --- |
| 1 | Perna contra o vento | Paralela à pista, no mesmo sentido do pouso e da decolagem, deslocada lateralmente em relação ao eixo | Não há reporte de rotina |
| 2 | Través | Perpendicular à pista, na altura da cabeceira oposta, faz a transição para o lado do circuito | Não há reporte de rotina |
| 3 | Perna do vento | Paralela à pista, em sentido oposto ao do pouso, mais afastada do eixo | "perna do vento da pista UNO TRÊS" |
| 4 | Perna base | Perpendicular à pista, antes do alinhamento final | "perna base da pista UNO TRÊS" |
| 5 | Final | Sobre o prolongamento do eixo da pista, em descida para o pouso | "na final" |

!!! warning "Contra o vento não é o eixo da pista"
    No desenho, o eixo da pista é a linha reta que atravessa o circuito pelo meio. É sobre ela que ficam a **final** e a **subida após a decolagem**.

    A **perna contra o vento** é outra coisa: corre paralela à pista, no mesmo sentido, porém **deslocada** do eixo. É ela que fecha o hipódromo junto com a perna do vento, do lado oposto.

    Essa distinção importa na prática: quando a Torre manda "ingresse na perna contra o vento", ela não está mandando sobrevoar a pista.

!!! note "Curvas padrão"
    Sem publicação em contrário, o circuito é feito com **curvas à esquerda**. Qualquer circuito à direita é uma restrição local e será informado pelo ATC ou estará publicado na carta do aeródromo.

    A geometria detalhada, as altitudes e os critérios de sequenciamento estão no [Manual de Circuito de Tráfego](../manual-circuito-trafego/index.md).

!!! tip "A carta manda"
    O retângulo acima é o padrão teórico. Na prática, o traçado real vem publicado na **VAC** do aeródromo, que também define as altitudes mínimas do circuito e os pontos de notificação visual.

    Dois exemplos de como isso varia:

    | Aeródromo | Altitudes mínimas no circuito | Observação |
    | --- | --- | --- |
    | Pampulha, SBBH, RWY 13/31 | CAT A e B: 3.900 pés, CAT C: 4.200 pés | Pontos de notificação MINEIRÃO, PAZ, ESPERANÇA e RIO |
    | Goiânia, SBGO, RWY 14/32 | CAT A e B: 3.500 pés, CAT C: 3.700 pés, CAT D e E: 4.200 pés | Hipódromos separados para aviões e helicópteros, estes a 3.200 pés |

    Sempre confira a carta vigente antes de voar ou controlar.

## Formas de ingressar no circuito

O piloto informa a intenção e o ATC confirma ou altera. As opções mais comuns:

| Ingresso | Quando usar | Como informar |
| --- | --- | --- |
| Início da perna do vento | Chegando pelo lado do circuito | "ingressará no início da perna do vento da pista UNO DOIS" |
| Ponto médio da perna do vento | Chegando pelo través do aeródromo | "ingressará no ponto médio da perna do vento da pista UNO DOIS" |
| Perna base | Chegando pelo setor da base | "ingressará na perna base da pista UNO DOIS" |
| Final longa | Chegando alinhado com a pista | "reportará na final longa da pista UNO DOIS" |
| Aproximação direta | Autorizada pelo ATC para agilizar o fluxo | "autorizada aproximação direta, pista UNO UNO" |
| Cruzamento do campo | Chegando pelo lado oposto ao do circuito | "para cruzamento do aeródromo" |

!!! tip "Escolha antes de chamar"
    Decida a forma de ingresso **antes** de apertar o PTT. O ATC precisa saber por onde você vai entrar para sequenciar o restante do tráfego, e a resposta "não sei" custa caro em frequência.

## O ciclo de reportes

A dinâmica é sempre a mesma, e ela se repete a cada volta no circuito.

=== ":flag_br: Português"
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

=== ":flag_gb: Inglês"
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

=== ":flag_es: Espanhol"
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

??? abstract "Algumas observações..."

    1. O reporte de perna do vento inclui a pista, porque em aeródromos com mais de uma pista essa é a informação que localiza a aeronave. Nas pernas seguintes a pista já está subentendida, mas repeti-la não é erro.

    2. Quando o circuito é à direita, isso entra no reporte de posição:

        > :flag_br: Torre Recife, **VICTOR BRAVO ROMEO**, base pela direita, pista UNO OITO. <br/>
        > :flag_gb: Recife Tower, **VICTOR BRAVO ROMEO**, right hand base, runway ONE EIGHT. <br/>
        > :flag_es: Recife Torre, **VICTOR BRAVO ROMEO**, tramo base por la derecha, pista UNO OCHO. <br/>

    3. É prática consagrada informar o trem de pouso baixado e travado no reporte de perna base ou de final, especialmente em aeronaves de trem retrátil e em aeródromos operados por **RÁDIO**.

        > :flag_br: **VICTOR BRAVO ROMEO**, perna base da pista UNO DOIS, trem de pouso baixado e travado. <br/>
        > :flag_gb: **VICTOR BRAVO ROMEO**, base leg runway ONE TWO, landing gear down and locked. <br/>
        > :flag_es: **VICTOR BRAVO ROMEO**, tramo base de la pista UNO DOS, tren de aterrizaje abajo y asegurado. <br/>

    4. O ATC pode antecipar a autorização de pouso já no reporte de perna base, se a pista estiver livre e a sequência estiver definida. Isso é normal e não dispensa o reporte de final.

## Saída do circuito após a decolagem

Ao decolar, a aeronave já está no circuito. Para deixá-lo, é preciso instrução do ATC e, em regra, um reporte de que o circuito ficou para trás.

=== ":flag_br: Português"

    | Situação | Fraseologia |
    | --- | --- |
    | Saída em frente | "VICTOR BRAVO ROMEO, após a decolagem, saída em frente, reporte livre do circuito." |
    | Saída pela perna do vento | "VICTOR BRAVO ROMEO, após a decolagem, saída pela perna do vento à esquerda, reporte livre do circuito." |
    | Saída com curva imediata | "VICTOR BRAVO ROMEO, após a decolagem, curva à direita, reporte livre do circuito." |
    | Reporte do piloto | "VICTOR BRAVO ROMEO, livre do circuito, rumo leste, subindo para SETE MIL E QUINHENTOS pés." |

=== ":flag_gb: Inglês"

    | Situation | Phraseology |
    | --- | --- |
    | Straight out departure | "VICTOR BRAVO ROMEO, after departure, straight out, report clear of the circuit." |
    | Departure via downwind | "VICTOR BRAVO ROMEO, after departure, leave via left downwind, report clear of the circuit." |
    | Departure with immediate turn | "VICTOR BRAVO ROMEO, after departure, turn right, report clear of the circuit." |
    | Pilot report | "VICTOR BRAVO ROMEO, clear of the circuit, eastbound, climbing to SEVEN THOUSAND FIVE HUNDRED feet." |

=== ":flag_es: Espanhol"

    | Situación | Fraseología |
    | --- | --- |
    | Salida en línea recta | "VICTOR BRAVO ROMEO, después del despegue, salida en línea recta, reporte libre del circuito." |
    | Salida por el tramo con viento en cola | "VICTOR BRAVO ROMEO, después del despegue, salida por el tramo con viento en cola por la izquierda, reporte libre del circuito." |
    | Salida con viraje inmediato | "VICTOR BRAVO ROMEO, después del despegue, vire a la derecha, reporte libre del circuito." |
    | Reporte del piloto | "VICTOR BRAVO ROMEO, libre del circuito, rumbo este, ascendiendo a SIETE MIL QUINIENTOS pies." |

---
