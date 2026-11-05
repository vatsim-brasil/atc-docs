---
title: Operação na Frequência
icon: material/radio-handheld
---

--8<-- "includes/abreviacoes.md"

# Operação na Frequência

## O ritmo da frequência

Na torre, o controlador conduz: autoriza, instrui e espera o cotejamento. Na RÁDIO, quem conduz é o piloto. Ele chama, informa onde está e o que pretende, e reporta cada fase. A RÁDIO responde com **ciente**, acrescenta o que o piloto precisa saber e pede o próximo reporte.

Os exemplos do MCA 100-16 para o AFIS seguem sempre o mesmo padrão[^1]:

1. o piloto chama e se identifica;
2. a RÁDIO responde com o próprio indicativo;
3. o piloto informa posição, nível ou altitude e intenção, ou pede informações;
4. a RÁDIO dá **ciente** e as informações do aeródromo, e pede um reporte;
5. o piloto reporta cada fase, e a RÁDIO dá ciente, com informação de tráfego quando houver.

## A informação do aeródromo

A primeira resposta da RÁDIO a uma aeronave que chega ou sai é a informação do aeródromo. Nos exemplos do MCA 100-16, ela traz, nesta ordem aproximada[^1]:

- **vento**, em graus e nós, ou "vento calmo";
- **ajuste de altímetro** (QNH);
- **temperatura**;
- **condições do aeródromo**: "aeródromo opera visual" ou "aeródromo em condições IFR", com teto e visibilidade estimados quando relevantes;
- **auxílios fora de serviço**, como um NDB fora do ar;
- **obstáculos e situações na área de movimento**, como máquinas ao lado da pista;
- **tráfego conhecido**, ou "não há tráfego conhecido";
- **hora certa**, para quem vai decolar.

A RÁDIO não designa a pista. Ela informa o vento e, se houver, a pista que os outros tráfegos estão usando. A escolha é do piloto, que a informa nos reportes ("perna do vento pista zero sete").

!!! note "Boa prática"
    Na rede, comece pelo METAR do aeródromo. Se não houver METAR, use o do aeródromo mais próximo e diga isso ao piloto. Teto e visibilidade "estimados" fazem sentido no mundo real, em que o operador olha pela janela. Na VATSIM, informe o que o METAR traz.

## Informação de tráfego

Informação de tráfego é o que a RÁDIO tem de mais valioso, porque o piloto vai usá-la para se separar sozinho. Ela diz **quem** é o tráfego, **onde** está e **o que** vai fazer: "Tráfego conhecido Xingu na perna do vento pista zero cinco"[^1].

Dê a informação quando ela muda a decisão do piloto: ao receber a chamada inicial, quando um tráfego novo entra no circuito ou chama na frequência, e quando duas aeronaves vão convergir na final ou na pista. Não há separação a garantir, mas há uma consciência situacional a construir.

!!! example "Exemplo"
    Um Cessna está na perna do vento da pista 12 para toque e arremetida. Um Sêneca chama 10 minutos fora, para pouso. A RÁDIO informa o Cessna ao Sêneca na chamada inicial e, quando o Sêneca reportar a perna do vento, informa ao Cessna que há um tráfego atrás dele. Os dois decidem o espaçamento. A RÁDIO não diz a nenhum dos dois que "prossiga número dois".

## Chegada VFR

O piloto chama com a posição, o nível ou altitude e a intenção. A RÁDIO dá a informação do aeródromo e pede o reporte de ingresso no circuito. Daí em diante, cada perna gera um reporte:

<div class="comms-pilot">Rádio Altamira, PT KST, procedente de Progresso, 10 minutos fora, radial 225, FL 075.</div>
<div class="comms-atc">PT KST, Rádio Altamira ciente, vento calmo, ajuste de altímetro uno zero uno dois, temperatura 22 graus, aeródromo opera visual, NDB Altamira fora do ar, não há tráfego conhecido. Informe na perna do vento.</div>
<div class="comms-pilot">PT KST ciente, reportará na perna do vento pista zero sete.</div>

Os reportes seguintes são perna do vento, perna base, final, no solo e pista livre. Na final, a RÁDIO repete o vento, se não houver outro tráfego a informar. No solo, pode pedir o reporte de pista livre[^1].

O circuito de tráfego padrão no aeródromo com AFIS tem uma subseção própria na ICA 100-37[^2]. Altitudes, pernas e ingresso estão no [Manual de Circuito de Tráfego](../manual-circuito-trafego/index.md).

## Saída VFR

O piloto chama ao iniciar o táxi, com a pista e o destino, e pede informações. A RÁDIO dá a informação do aeródromo, com tráfego conhecido e hora certa, e pede o reporte no ponto de espera. Os reportes seguintes são ponto de espera, ingressando na pista, alinhado e fora do solo[^1].

<div class="comms-pilot">PT EEA, iniciando o táxi, pista zero cinco, destino Vitória, solicita informações.</div>
<div class="comms-atc">PT EEA, Rádio Usiminas ciente. Vento dois quatro zero graus, zero dois nós. Ajuste de altímetro uno zero dois uno. Observe máquinas no lado esquerdo da pista zero cinco. Tráfego conhecido Xingu na perna do vento pista zero cinco. Temperatura dois quatro. Hora certa 56. Reporte no ponto de espera.</div>

Repare no que o piloto diz no ponto de espera: "mantém posição, aguardando pouso do Xingu". Quem decide esperar é ele. A RÁDIO só deu a informação que tornou a decisão possível.

Depois da decolagem, o piloto reporta o nível ou altitude atingido e as estimativas. Se a rota entra em espaço aéreo controlado, a RÁDIO dá a frequência do órgão seguinte. O MCA 100-16 traz o exemplo de uma saída que entra na TMA: "ingressando Terminal, chame Controle Vitória em uno uno nove decimal oito, caso negativo, Torre Vitória em uno uno oito decimal uno"[^1].

!!! tip "Na prática"
    "Chame" não é transferência de controle. A RÁDIO não tinha o controle da aeronave e não tem o que transferir. Ela apenas indica quem o piloto deve chamar para entrar no espaço aéreo controlado, onde ele vai precisar de autorização.

## Chegada IFR

A ICA 100-37 tem uma seção para a descida por instrumentos em aeródromo provido de AFIS, com uma subseção para o voo em espaço aéreo controlado e outra para o voo fora dele. O aeródromo "deve possuir procedimento de aproximação IFR em vigor" (Art. 140)[^2].

O caso comum é o de uma aeronave IFR que desce sob controle do centro ou do APP até a FIZ:

1. Ainda com o centro, o piloto chama a RÁDIO e pede as condições do aeródromo. A RÁDIO informa o vento, o ajuste, a condição do aeródromo (visual ou IFR), o teto, a visibilidade, a temperatura e o tráfego conhecido.
2. O piloto avisa que chamará de novo quando autorizado pelo centro.
3. O piloto volta à RÁDIO informando a autorização recebida do centro e o nível que está cruzando.
4. A RÁDIO dá ciente e pede os reportes do procedimento: altitude de início do procedimento, afastamento, curva base ou de procedimento, aproximação final, MDA com o aeródromo à vista, no solo e pista livre[^1].

A autorização de descida e a de aproximação são do **centro** ou do **APP**. A RÁDIO não a repete como se fosse dela. Ela acompanha o procedimento e mantém o piloto informado sobre o tráfego, sobretudo o VFR que esteja no circuito.

## Saída IFR

A autorização de tráfego IFR é dada pelo órgão de controle que tem jurisdição sobre o espaço aéreo à frente, nunca pela RÁDIO. Quando a autorização vem pela frequência da RÁDIO, ela é uma retransmissão (Art. 788, VII)[^2], e a RÁDIO diz de onde ela partiu.

!!! note "Boa prática"
    Ao retransmitir, comece pelo órgão que autorizou e leia a autorização exatamente como recebida: "PT ABC, Controle Bauru autoriza...". O piloto coteja com a RÁDIO, e a RÁDIO confirma ao órgão de controle que a autorização foi entregue. Se o piloto pedir uma mudança, a RÁDIO não negocia: leva o pedido ao órgão que autorizou.

Depois da decolagem, a RÁDIO passa o piloto ao órgão de controle no ponto ou altitude combinados com ele. Ver [AFIS na Rede](03-rede.pt.md#coordenacao-com-o-app-e-o-centro).

## Aeronaves sem rádio

A ICA 100-37 tem uma subseção para a operação de aeronaves sem equipamento rádio ou com o rádio inoperante no aeródromo com AFIS[^2]. Na rede, o caso equivalente é o do piloto que opera **só por texto**, ou que não consegue transmitir na voz.

!!! note "Na rede"
    Responda por texto, na frequência da RÁDIO, com as mesmas informações que daria na voz. Para os outros pilotos, informe o tráfego de quem está só no texto como informaria qualquer outro tráfego: eles podem não estar lendo o canal de texto.

[^1]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16), Capítulo IV, Seção VI (Serviço de Informação de Voo de Aeródromo – AFIS), subseções Tráfego chegando, Tráfego saindo e Informação de tráfego. Os indicativos e as frequências dos exemplos são os do manual.
[^2]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Seção V do capítulo do Serviço de Informação de Voo (AFIS) e seção "Descida por instrumentos em aeródromo provido de AFIS". Edição em vigor em 27/11/2025.
