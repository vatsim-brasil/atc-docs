---
title: Operação na Frequência
icon: material/radio-handheld
---

--8<-- "includes/abreviacoes.md"

# Operação na Frequência

## O ritmo da frequência

Na torre, o controlador conduz: autoriza, instrui e espera o cotejamento. Na RÁDIO, quem conduz é o piloto. Ele chama, informa onde está e o que pretende, e reporta cada fase. A RÁDIO responde com **ciente**, acrescenta o que o piloto precisa saber e pede o próximo reporte.

Os exemplos do MCA 100-16 para o AFIS seguem sempre o mesmo padrão (Arts. 153 a 158)[^1]:

1. o piloto chama e se identifica;
2. a RÁDIO responde com o próprio indicativo;
3. o piloto informa procedência, posição, nível e intenção, ou pede informações;
4. a RÁDIO dá **ciente** e a informação do aeródromo, e pede as intenções ou um reporte;
5. o piloto reporta cada fase, e a RÁDIO dá ciente, com informação de tráfego quando houver.

## A informação do aeródromo

A primeira resposta da RÁDIO a uma aeronave que chega ou sai é a informação do aeródromo. Os elementos estão no Art. 788 da ICA 100-37, detalhados em [Fundamentos do AFIS](01-fundamentos.pt.md#o-que-a-radio-informa)[^2]. Nos exemplos do MCA 100-16, ela vem nesta ordem aproximada[^1]:

- **vento**, em graus e nós, ou "vento calmo";
- **pista utilizada por outras aeronaves**, quando for o caso;
- **ajuste de altímetro** (QNH);
- **temperatura**;
- **condições do aeródromo**: "aeródromo opera visual", "aeródromo em condições IFR" ou "aeródromo abaixo dos mínimos visuais", com teto e visibilidade estimados quando relevantes;
- **auxílios fora de serviço**, como um NDB fora do ar, e obstáculos na área de movimento, como máquinas ao lado da pista;
- **tráfego conhecido**, ou "não há tráfego conhecido";
- **hora certa**, para quem vai decolar;
- e, para quem chega, **"informe intenções"**.

A RÁDIO não designa a pista. Ela informa a pista e o circuito que os outros tráfegos estão usando. Espera-se que o piloto use essa pista, mas ele pode escolher outra, desde que avise antes de entrar no circuito ou iniciar o táxi (Art. 158 da ICA 100-37)[^2].

!!! note "Boa prática"
    Na rede, comece pelo METAR do aeródromo. Se não houver METAR, use o do aeródromo mais próximo e diga isso ao piloto. Teto e visibilidade "estimados" fazem sentido no mundo real, em que o operador olha pela janela. Na VATSIM, informe o que o METAR traz.

## Informação de tráfego

Informação de tráfego é o que a RÁDIO tem de mais valioso, porque o piloto vai usá-la para se separar sozinho. Ela diz **quem** é o tráfego, **o que** é, **onde** está e **o que** vai fazer. O MCA 100-16 traz este exemplo, para uma chegada com dois tráfegos (Art. 154)[^1]:

<div class="comms-atc">PT KST, Rádio Altamira ciente, vento calmo, QNH 1012, temperatura 22 graus, aeródromo opera visual, CAVOK, tráfego é o PT KLC na perna base da pista 07 para toque e arremetida, C172. Tráfego adicional é o PT-RPT, procedente de Belém, 5 minutos fora, rumo noroeste, cruzando o campo para ingresso na perna do vento da pista 07, EMB110, passou nível 050 descendo para 1.000 pés. Informe intenções.</div>
<div class="comms-pilot">PT KST, ciente, ingressará no início da perna do vento da pista 07 para pouso.</div>

Dê a informação quando ela muda a decisão do piloto: ao receber a chamada inicial, quando um tráfego novo entra no circuito ou chama na frequência, e quando duas aeronaves vão convergir na final ou na pista. Os exemplos do MCA 100-16 marcam esse ponto com "[informação de tráfego]" depois do ciente, nos reportes de perna base e de final (Arts. 154 e 155)[^1].

A ICA 100-37 dá ao piloto as regras para resolver o conflito: a aeronave na aproximação final tem, normalmente, prioridade sobre a que está no circuito (Art. 159)[^2]. O MCA 100-16 mostra também tráfegos com prioridade, como um aeromédico ou um transporte de órgão, e o piloto que, informado, cede a passagem (Art. 158, III)[^1].

!!! example "Exemplo"
    Um Cessna está na perna do vento da pista 12 para toque e arremetida. Um Sêneca chama 10 minutos fora, para pouso. A RÁDIO informa o Cessna ao Sêneca na chamada inicial e, quando o Sêneca reportar a perna do vento, informa ao Cessna que há um tráfego atrás dele. Os dois decidem o espaçamento. A RÁDIO não diz a nenhum dos dois que "prossiga número dois".

## Chegada VFR

O piloto chama com a procedência, a posição, o nível e a intenção. A RÁDIO dá a informação do aeródromo e pede as intenções. Daí em diante, cada perna gera um reporte (Art. 154 do MCA 100-16)[^1]:

<div class="comms-pilot">PT KST, procedente de Progresso, 10 minutos fora, radial 225, FL 075.</div>
<div class="comms-atc">PT KST, Rádio Altamira ciente, vento calmo, pista utilizada por outras aeronaves é a 07, ajuste de altímetro ou QNH 1012, temperatura 22 graus, aeródromo opera visual, teto estimado 1.500 pés, visibilidade 5.000 metros devido fumaça, NDB Altamira fora do ar. Informe intenções.</div>
<div class="comms-pilot">PT KST, ciente, reportará na perna do vento da pista 07.</div>

Os reportes seguintes são perna do vento, perna base, final e no solo com pista livre. Na perna base, o piloto reporta também o trem de pouso baixado e travado, como pede o Art. 791 da ICA 100-37[^2].

**Ingresso no circuito.** O ingresso preferencial é pelo setor da perna contra o vento (Art. 154 da ICA 100-37). Em aeródromo com AFIS, como a comunicação bilateral é compulsória, o piloto pode também ingressar alinhado com o início da perna do vento, no ponto médio da perna do vento a 45°, ou alinhado com a perna base, depois de se assegurar, junto à RÁDIO, de que não haverá conflito (Art. 163). Sem outros tráfegos e com a tripulação familiarizada com o aeródromo, o VFR pode ingressar direto na reta final, e o IFR pode fazer uma aproximação direta (Art. 164)[^2]. O MCA 100-16 tem um exemplo de ingresso pela final longa (Art. 155)[^1].

As altitudes e o desenho do circuito estão no [Manual de Circuito de Tráfego](../manual-circuito-trafego/index.md).

## Saída VFR

O piloto chama ao iniciar o táxi, com a pista e o destino, e pede informações. A RÁDIO dá a informação do aeródromo, com tráfego conhecido e hora certa, e pede o reporte no ponto de espera. Os reportes seguintes são ponto de espera, ingressando na pista, alinhado e fora do solo (Art. 156 do MCA 100-16)[^1].

<div class="comms-pilot">PT EEA, iniciando o táxi, pista 05, destino Vitória, solicita informações.</div>
<div class="comms-atc">PT EEA, Rádio Usiminas ciente. Vento 240 graus, 2 nós. Ajuste do altímetro 1021. Observe máquinas no lado esquerdo da pista 05. Tráfego conhecido PS-RET, um Xingu na perna do vento pista 05, e AZUL 4218, procedente de Belo Horizonte, um ATR72, passou nível 060 em descida para o procedimento RNP Y pista 23, 08 minutos para o início do procedimento. Temperatura 24. Hora certa 56. Reporte no ponto de espera.</div>

Repare no que o piloto diz no ponto de espera: "mantém posição, aguardando pouso do Xingu". Quem decide esperar é ele. A RÁDIO só deu a informação que tornou a decisão possível.

Depois da decolagem, o piloto reporta o nível atingido e as estimativas. Se a rota entra em espaço aéreo controlado, a RÁDIO dá a frequência do órgão seguinte: "ingressando Terminal, chame Controle Vitória em 119,8, caso negativo, Torre Vitória em 118,1"[^1].

!!! tip "Na prática"
    "Chame" não é transferência de controle. A RÁDIO não tinha o controle da aeronave e não tem o que transferir. Ela apenas indica quem o piloto deve chamar para entrar no espaço aéreo controlado, onde ele vai precisar de autorização.

## Chegada IFR

A ICA 100-37 tem uma seção para a descida por instrumentos em aeródromo provido de AFIS, que "deve possuir procedimento de aproximação IFR em vigor" (Art. 140)[^2]:

- **Em espaço aéreo controlado**, a aeronave obtém do órgão ATC a autorização para descer até o nível mínimo do espaço aéreo controlado, segue para o procedimento e transmite na frequência da RÁDIO os níveis ou altitudes e as fases do procedimento que for atingindo (Art. 141).
- **Fora do espaço aéreo controlado**, não há autorização a obter: a aeronave define o nível mínimo de descida pelos critérios do Art. 142, executa o procedimento e transmite as mesmas informações na frequência da RÁDIO (Art. 142)[^2].

O MCA 100-16 traz duas situações, ambas com a aeronave descendo sob o Centro Amazônico (Art. 153)[^1]:

1. Ainda com o centro, o piloto chama a RÁDIO e pede as condições do aeródromo. A RÁDIO informa o vento, a pista utilizada por outras aeronaves, o ajuste, a condição do aeródromo, a visibilidade, o teto e a temperatura.
2. O piloto avisa o procedimento que vai executar, e a RÁDIO pede que ele reporte quando liberado pelo centro.
3. O piloto volta à RÁDIO: "autorizado pelo Centro, passando FL 120 IMC". A RÁDIO dá ciente e o ajuste de altímetro.
4. A RÁDIO pede os reportes do procedimento. No procedimento convencional: altitude de início, afastamento, curva base ou de procedimento, aproximação final e MDA com o aeródromo à vista. No procedimento RNAV: cada fixo (CZ009, CZ011, CZ012). Na final, o piloto reporta o trem baixado e travado.
5. A RÁDIO dá o vento e pede os reportes de no solo e de pista livre.

A autorização de descida é do **centro** ou do **APP**. A RÁDIO não a repete como se fosse dela. Ela acompanha o procedimento e mantém o piloto informado sobre o tráfego, sobretudo o VFR que esteja no circuito. O exemplo do MCA 100-16 faz isso para um IFR em procedimento RNP: "operação IFR, camada mais baixa a 600 pés, tráfego PT KLN é um Cessna 182, decolado há 2 minutos subindo para FL 060, radial 337, reporte iniciando procedimento" (Art. 158)[^1].

## Saída IFR

A autorização de tráfego IFR é dada pelo órgão de controle que tem jurisdição sobre o espaço aéreo à frente, nunca pela RÁDIO. Quando a autorização vem pela frequência da RÁDIO, ela é uma retransmissão (Art. 788, VII, da ICA 100-37)[^2], e a RÁDIO diz de onde ela partiu: "após cruzamento do FL 040, autorizado pelo Centro a subir em rota, reporte cruzando o FL 040 para o Centro Amazônico, frequência 123,95" (Art. 158 do MCA 100-16)[^1].

No exemplo de saída IFR do MCA 100-16 (Art. 157)[^1], o piloto chama ao iniciar o táxi, informando a saída que vai executar ("irá executar a saída RNAV AGIL 1A"). A RÁDIO dá a informação do aeródromo com hora certa, pede os reportes no ponto de espera, alinhado e fora do solo, e depois o reporte passando o primeiro fixo da saída. Só então passa o piloto ao centro: "chame agora o Centro Amazônico em 124,55, alternando 134,15".

!!! note "Boa prática"
    Ao retransmitir, leia a autorização exatamente como recebida, começando por quem autorizou. O piloto coteja com a RÁDIO, e a RÁDIO confirma ao órgão de controle que a autorização foi entregue. Se o piloto pedir uma mudança, a RÁDIO não negocia: leva o pedido ao órgão que autorizou.

Ver também [Coordenação com o APP e o centro](03-rede.pt.md#coordenacao-com-o-app-e-o-centro).

## Aeródromo abaixo dos mínimos

A RÁDIO não fecha o aeródromo. Ela informa as condições, e a decisão é do piloto. No exemplo do MCA 100-16, a RÁDIO informa "aeródromo abaixo dos mínimos visuais, visibilidade estimada 2.000 metros, teto 600 pés, informe intenções", o piloto decide seguir para a alternativa, e a RÁDIO pede o reporte "5 minutos fora de Aeroxingu" (Art. 158, II)[^1].

## Aeronaves sem rádio

A ICA 100-37 proíbe a operação de aeronaves sem rádio, ou com o rádio inoperante, em aeródromos com AFIS. As exceções são o voo de translado, o voo agrícola e os planadores e aeronaves de aeroclubes e centros de instrução sediados no aeródromo, sempre com coordenação prévia e em horários que não prejudiquem o tráfego (Art. 789)[^2].

!!! note "Na rede"
    O caso equivalente na VATSIM é o do piloto que opera **só por texto**. Responda por texto, na frequência da RÁDIO, com as mesmas informações que daria na voz. Para os outros pilotos, informe o tráfego de quem está só no texto como informaria qualquer outro tráfego: eles podem não estar lendo o canal de texto.

[^1]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): Seção VI, Serviço de Informação de Voo de Aeródromo – AFIS (Arts. 153 a 158). Edição aprovada pela Portaria DECEA/DNOR1 n° 1.716, de 28/04/2025. Os indicativos e as frequências dos exemplos são os do manual.
[^2]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Capítulo III, Seções XX e XXI (Arts. 140 a 164), e Capítulo VIII, Seção V (Arts. 782 a 791). Edição em vigor em 27/11/2025.
