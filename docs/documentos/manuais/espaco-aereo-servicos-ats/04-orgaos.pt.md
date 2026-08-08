---
title: Órgãos ATS e Posições
icon: material/account-tie-hat
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Órgãos](img/manual-espaco-aereo-orgaos.png)

#

## Órgão ATS e posição na rede

O capítulo anterior terminou com uma promessa: mostrar como o Serviço de Controle de Área, o Serviço de Controle de Aproximação e o Serviço de Controle de Aeródromo se distribuem entre os órgãos ATS da rede Vatsim Brasil — ACC, APP, TWR. Este capítulo cumpre essa promessa e acrescenta o elo que faltava: a posição operacional que um controlador efetivamente conecta na rede.

Órgão ATS é conceito normativo. O Anexo VII da ICA 100-12 define o Órgão dos Serviços de Tráfego Aéreo — abreviado "órgão ATS" — como a "expressão genérica que se aplica, segundo o caso, a um órgão de controle de tráfego aéreo ou a um órgão de informação de voo"[^2], e o Órgão de Controle de Tráfego Aéreo, no mesmo Anexo VII da ICA 100-12, como a "expressão genérica que se aplica, segundo o caso, a um Centro de Controle de Área, Controle de Aproximação ou Torre de Controle de Aeródromo"[^2]. É a ICA 100-37 e a ICA 100-12 que dizem o que cada um desses órgãos é, o que presta e sobre qual espaço aéreo tem autoridade.

Posição, em contraste, é convenção da rede Vatsim Brasil, sem contrapartida na ICA 100-37 ou na ICA 100-12: nenhuma das duas menciona login, cliente de controle ou sufixo de indicativo. O que a rede faz é atribuir a cada órgão real — ou a cada função dentro de um órgão, como a próxima seção mostra — um sufixo de conexão: `_CTR`, `_APP`, `_TWR`, `_GND`, `_DEL`. Conectar `_TWR` não é o mesmo que ser a Torre — é operar, na rede, a posição que corresponde ao órgão que a próxima seção define.

## ACC, APP e TWR: os três órgãos de controle

O Anexo VII da ICA 100-12 define os três órgãos de controle de tráfego aéreo pelo que cada um presta:

- **Centro de Controle de Área (ACC)** é, segundo o Anexo VII da ICA 100-12, o "órgão estabelecido para prestar serviço de controle de tráfego aéreo aos voos controlados nas áreas de controle sob sua jurisdição"[^2];
- **Controle de Aproximação (APP)** é, no mesmo Anexo VII da ICA 100-12, o "órgão estabelecido para prestar serviço de controle de tráfego aéreo aos voos controlados que cheguem ou saiam de um ou mais aeródromos"[^2];
- **Torre de Controle de Aeródromo (TWR)** é, ainda no Anexo VII da ICA 100-12, o "órgão estabelecido para proporcionar serviço de controle de tráfego aéreo ao tráfego de aeródromo"[^2].

A ICA 100-37 já detalhou, no capítulo anterior, como esses três se relacionam com os três serviços: o Serviço de Controle de Área é prestado por um ACC ou por um APP delegado (Art. 33 da ICA 100-37)[^1]; o Serviço de Controle de Aproximação, por um APP ou por um ACC ou TWR delegado (Art. 34 da ICA 100-37)[^1]; o Serviço de Controle de Aeródromo, por uma TWR delegada (Art. 35 da ICA 100-37)[^1]. A delegação é a válvula de escape da norma para arranjos operacionalmente necessários — um único órgão acumulando funções de mais de um serviço —, mas o arranjo padrão, e o que a tabela a seguir assume, é um órgão para cada serviço.

## Duas posições dentro da própria TWR

Nem toda posição da rede corresponde a um órgão distinto. O Art. 509 da ICA 100-37 diz que as funções de uma Torre de Controle de Aeródromo podem ser realizadas por diferentes posições de controle, e lista três: a "posição controle TWR, normalmente responsável pelas operações na pista e por aeronaves que voam dentro da área de responsabilidade da Torre de Controle de Aeródromo"; a "posição controle solo, normalmente responsável pelo tráfego na área de manobra, com exceção das pistas"; e a "posição autorização de tráfego, normalmente responsável pela emissão de informações e autorizações de tráfego aéreo para as aeronaves que pretendam decolar"[^1].

As três são posições de um único órgão — a TWR —, não três órgãos ATS distintos. É o próprio Art. 509 da ICA 100-37 quem estabelece essa divisão interna de funções; é a rede Vatsim Brasil, não a ICA 100-37 ou a ICA 100-12, quem decide transformar cada uma delas em uma conexão separada (`_DEL`, `_GND`, `_TWR`). Nada na Instrução exige que sejam três logins — poderiam, tecnicamente, ser um só controlador acumulando as três posições, como acontece na prática quando o Controle de Solo e a Autorização de Tráfego não estão conectados. O que muda, nesse caso, não é a jurisdição — que continua sendo da TWR sobre a área de manobras e o tráfego de aeródromo —, mas quem, na rede, está do outro lado do microfone.

## Tabela de correspondência

A tabela abaixo relaciona cada órgão ATS tratado neste capítulo — os três de controle e os dois que **não** controlam — ao espaço aéreo em que ele tipicamente opera e à posição da rede que lhe corresponde, quando há uma: o Centro de Informação de Voo não tem posição própria, e a coluna registra isso na sua linha. Quando um órgão se subdivide internamente, a coluna "Posição interna" indica qual função está em jogo, com os nomes que o Art. 686 da ICA 100-37 usa para as três posições que o Art. 509 da mesma Instrução institui: o Art. 509 as descreve — "posição controle TWR", "posição controle solo" e "posição autorização de tráfego" — e o Art. 686 as chama pelo nome, na ordem de precedência para a autorização do Plano de Voo: "Autorização de Tráfego", "Controle de Solo" e "Torre de Controle"[^1]. São as mesmas três posições em ambos os artigos. A coluna fica vazia nas demais linhas porque a ICA 100-37 nomeia posições internas apenas para a TWR — para os outros órgãos ela fala genericamente em "posições de controle" e em "setores de controle" de um mesmo órgão, sem nomeá-los (Art. 852)[^1]. Note que "Torre de Controle de Aeródromo (TWR)" se repete em três linhas: é o mesmo órgão nas três, não três órgãos diferentes.

| Órgão ATS | Posição interna | Posição Vatsim Brasil | Espaço aéreo típico | Serviço prestado |
| --- | --- | --- | --- | --- |
| Centro de Controle de Área (ACC) | — | `_CTR` | CTA, UTA e demais porções da FIR | Controle de área |
| Controle de Aproximação (APP) | — | `_APP` | TMA e CTR\* | Controle de aproximação |
| Torre de Controle de Aeródromo (TWR) | Torre de Controle | `_TWR` | ATZ e CTR\* | Controle de aeródromo |
| Torre de Controle de Aeródromo (TWR) | Controle de Solo | `_GND` | Área de manobras | Controle de aeródromo |
| Torre de Controle de Aeródromo (TWR) | Autorização de Tráfego | `_DEL` | Pátio | Controle de aeródromo |
| Órgão ATS identificado como "RÁDIO" (AFIS) | — | `_R_TWR` | FIZ, ou Classe G nas imediações do aeródromo | Informação de voo e alerta — **sem controle** |
| Órgão de informação de voo (FIC) | — | sem posição própria na rede | FIR fora do espaço aéreo controlado† | Informação de voo e alerta — **sem controle** |

\* **A CTR aparece em duas linhas de propósito.** Qual dos dois órgãos tem jurisdição sobre uma CTR varia por localidade: o Art. 34 da ICA 100-37 admite que o Serviço de Controle de Aproximação seja prestado por um APP ou por um ACC ou TWR ao qual tenha sido delegada a atribuição[^1] — e é essa delegação, publicada por aeródromo, que decide o caso. Isso não contraria o Art. 37, citado na seção seguinte: em cada CTR concreta, **um só** dos dois a tem. Qual deles, naquele aeródromo, está na AIP-Brasil e na seção [**Manuais Operacionais**](../../../MOP/aerodromos/index.pt.md) do portal.

† **Esta célula é leitura deste manual, não texto de norma.** A ICA 100-37 nomeia o Centro de Informação de Voo – FIC (Arts. 758 e 856-A)[^1], mas em nenhum momento delimita o espaço aéreo sob sua responsabilidade, como faz para o ACC, o APP e a TWR. O valor da célula é inferência a partir de três dispositivos da própria Instrução: o Art. 15, para o qual "Regiões de Informação de Voo são as partes do espaço aéreo onde são providos os Serviços de Informação de Voo e de Alerta"[^1]; o Art. 38, que atribui esses dois serviços ao "órgão ATS que tenha jurisdição no espaço aéreo considerado"[^1]; e o Art. 37, segundo o qual "somente um órgão de controle de tráfego aéreo terá jurisdição sobre um determinado espaço aéreo"[^1] — donde a porção da FIR que sobra fora das áreas e zonas de controle. Onde há órgão de controle, é ele quem presta também informação de voo e alerta, pelo mesmo Art. 38.

**As duas últimas linhas são os órgãos que não controlam**, e é por isso que estão aqui: um controlador que assume uma delas precisa saber que a autoridade que ela carrega é diferente.

- O órgão ATS identificado como **"RÁDIO"** é quem normalmente presta o AFIS — o Serviço de Informação de Voo de Aeródromo (Art. 783 da ICA 100-37)[^1]. O parágrafo único do mesmo artigo define exatamente o que ele presta: "Esse órgão ATS presta o Serviço de Informação de Voo e, adicionalmente, o Serviço de Alerta a todo o tráfego em operação na área de movimento do aeródromo e a todas as aeronaves em voo no espaço aéreo Classe G nas imediações do mesmo"[^1]. O AFIS é normalmente prestado dentro de uma Zona de Informação de Voo – FIZ, divulgada na AIP-Brasil (Art. 786)[^1]; onde não houver FIZ publicada, o Art. 787 estende o serviço à área de movimento e a todas as aeronaves em voo em Classe G abaixo do FL 145 e num raio de 27 NM (50 km) do aeródromo[^1]. Na FIZ "não há prestação de Serviço de Controle de Tráfego Aéreo e, por isso, não devem ser esperadas autorizações de controle de tráfego aéreo" (Art. 786, § 1°)[^1]. Na rede Vatsim Brasil, essas posições usam o sufixo `_R_TWR` — o `_R_` é a marca de RÁDIO, e o sufixo `_TWR` é apenas o formato de conexão, não uma Torre de Controle; as páginas de cada aeródromo na seção [**Manuais Operacionais**](../../../MOP/aerodromos/index.pt.md) trazem o indicativo e a frequência.
- O **órgão de informação de voo** é uma categoria própria, e não um tipo de órgão de controle: o Anexo VII da ICA 100-12 define órgão ATS como a "expressão genérica que se aplica, segundo o caso, a um órgão de controle de tráfego aéreo **ou a um órgão de informação de voo**"[^2]. A ICA 100-37 nomeia um desses órgãos ao lado do ACC — o Centro de Informação de Voo – FIC (Arts. 758 e 856-A)[^1]. Na rede Vatsim Brasil não há posição própria para ele: em espaço aéreo fora das áreas de controle, quem responde é o órgão que tiver jurisdição, pelo Art. 38 da ICA 100-37[^1] — na prática, o `_CTR` conectado.

Na fonia, esses dois órgãos são os que o [Manual de Fraseologia para Voo Visual](../fraseologia-voo-visual/conceitos.pt.md) identifica como **INFORMAÇÃO** e **RÁDIO**, e cuja regra ele resume em uma linha: informam, transmitem condições e respondem com CIENTE — não controlam.

A coluna "espaço aéreo típico" ainda mistura dois registros que vale separar. Para o ACC, o APP e a linha "Torre de Controle" da TWR, ela indica jurisdição sobre espaço aéreo tal como a ICA 100-37 e a ICA 100-12 o definem: UTA, CTA e TMA são as três espécies de Área de Controle, na divisão que os incisos I, II e III do Art. 17 da ICA 100-37 estabelecem[^1]; CTR é, segundo o Anexo VII da ICA 100-12, o "espaço aéreo controlado que se estende do solo até um limite superior especificado"[^2]; e ATZ é o entorno de aeródromo com "requisitos especiais para proteção do tráfego", conforme o Art. 19 da ICA 100-37[^1] — todos já tratados no capítulo 01. Para as linhas "Controle de Solo" e "Autorização de Tráfego" — as outras duas posições internas da mesma TWR —, ela indica a área física do aeródromo onde cada uma costuma operar: a Área de Manobras, definida pelo Anexo VII da ICA 100-12 como "parte do aeródromo destinada ao pouso, decolagem e táxi de aeronaves, excluídos os pátios"[^2], é a jurisdição do Controle de Solo — mas somente "com exceção das pistas", segundo o Art. 509 da ICA 100-37[^1], que continuam com a posição Torre de Controle; e o Pátio, que o mesmo Anexo VII da ICA 100-12 define como "área definida (...) destinada a abrigar as aeronaves para fins de embarque ou desembarque de passageiros, carga ou descarga, reabastecimento, estacionamento ou manutenção"[^2], é onde a Autorização de Tráfego normalmente fala com a aeronave, antes de esta solicitar push-back ou táxi.

## Jurisdição

Duas regras da ICA 100-37 fecham a questão de até onde vai cada posição. O Art. 37 da ICA 100-37 é direto: "Somente um órgão de controle de tráfego aéreo terá jurisdição sobre um determinado espaço aéreo"[^1]. O Art. 36 da ICA 100-37 fecha o outro lado: "Uma aeronave controlada deverá estar sob controle de somente um órgão de controle de tráfego aéreo"[^1].

Repare no que os dois artigos dizem e no que não dizem. Eles fixam um **teto**, não um piso: "somente um" é *no máximo* um, e não *pelo menos* um. Não há sobreposição de autoridade — nunca dois órgãos de controle sobre o mesmo espaço aéreo, nunca dois sobre a mesma aeronave controlada. Mas espaço aéreo sem nenhum órgão de controle de tráfego aéreo existe, e é a regra na [Classe G](02-classes.pt.md#classe-g), onde não se presta o Serviço de Controle de Tráfego Aéreo — como a seção *Cobertura top-down*, adiante, volta a tratar. O mesmo princípio de exclusividade vale para o Serviço de Informação de Voo e o Serviço de Alerta: o Art. 38 da ICA 100-37 atribui a sua prestação ao "órgão ATS que tenha jurisdição no espaço aéreo considerado"[^1] — e esses dois serviços, ao contrário do controle, existem em toda a FIR (Art. 32 da ICA 100-37)[^1].

Essa jurisdição tem duas dimensões — lateral e vertical —, e o Art. 839 da ICA 100-37 as nomeia separadamente ao tratar da fronteira entre ACC e APP: a transferência de controle das aeronaves que chegam ocorre "ao cruzarem o limite lateral da TMA nos pontos de notificação estabelecidos" ou "ao cruzarem o limite vertical da TMA"[^1]. Lateral é a fronteira geográfica — onde uma TMA, uma CTR ou uma ATZ termina no mapa; vertical é o nível ou altitude em que a jurisdição de um órgão cede lugar à de outro. Os limites concretos de cada FIR, TMA, CTR e ATZ — os números — são publicados na AIP-Brasil e nas cartas, como já registrado no capítulo 01; a ICA 100-37 fixa o princípio, não a coordenada.

Jurisdição também não se presume: o Art. 822 da ICA 100-37 veda que "uma aeronave sob controle de um órgão, ou posição de controle, adentre em espaço aéreo sob jurisdição de outro órgão, ou posição de controle, sem que antes tenha sido completada a coordenação"[^1]. Cruzar a fronteira sem coordenação prévia não é apenas falha de etiqueta — é a aeronave operando, por um instante, sob a responsabilidade de ninguém.

## Cobertura *top-down*

O que a ICA 100-37 e a ICA 100-12 não preveem — porque não é assunto de nenhuma das duas — é o que acontece quando um órgão do mundo real simplesmente não tem ninguém conectado na rede naquele momento. Essa lacuna é resolvida por uma convenção da rede Vatsim Brasil, sem base na ICA 100-37 ou na ICA 100-12: a cobertura *top-down*.

A ideia é simples: se a posição superior da cadeia está conectada e a inferior não está, a superior assume, informalmente, a responsabilidade pelo espaço aéreo da inferior. Um CTR conectado sem nenhum APP ou TWR abaixo dele cobre a TMA, a CTR — no sentido de Zona de Controle — e a ATZ dos aeródromos daquele espaço; um APP conectado sem TWR cobre a torre. A consequência prática, do lado do piloto, é que ele chama uma única frequência do início ao fim — a da posição mais alta que estiver conectada — sem precisar saber, de antemão, quais posições intermediárias existem ou estão vazias naquele momento.

Vale repetir: isso é conveniência operacional da simulação, não uma regra da ICA 100-37. Na vida real, um espaço aéreo sem órgão designado não passa a ser coberto automaticamente por quem estiver "acima" dele — a ICA 100-37 resolve a ausência de outra forma, atribuindo o Serviço de Informação de Voo e o Serviço de Alerta ao órgão que tiver jurisdição, pelo já citado Art. 38[^1], e não abrindo uma exceção de cobertura.

## Transferência entre órgãos

Um voo completo passa, tipicamente, por todas as **posições de controle** da tabela — as cinco primeiras linhas —, na ordem em que a ICA 100-37 regula a coordenação entre elas: para a partida, da Autorização de Tráfego até o Centro de Controle de Área; para a chegada, o caminho inverso. As duas últimas linhas, que não controlam, ficam fora dessa cadeia.

Na partida, o piloto chama a Autorização de Tráfego, o Controle de Solo ou a Torre de Controle "na ordem de precedência apresentada", para a autorização do Plano de Voo (Art. 686 da ICA 100-37)[^1]; obtida essa autorização, chama a posição Controle de Solo ou Torre de Controle, "nesta ordem de precedência", para as autorizações de push-back, acionamento dos motores e início do táxi (Art. 687 da ICA 100-37)[^1]. Depois da decolagem, o Art. 849 da ICA 100-37 manda transferir o controle da TWR ao APP "imediatamente após a decolagem" ou, quando isso não ocorrer antes, "antes que [as aeronaves] entrem em condições meteorológicas de voo por instrumentos"[^1]. Do APP para o ACC, o Art. 840 da ICA 100-37 fixa a transferência das aeronaves que partem ao cruzarem o limite lateral ou vertical da TMA, ou num ponto e horário previamente acordados entre os órgãos[^1].

Na chegada, a cadeia se percorre ao contrário. O Art. 839 da ICA 100-37 fixa a transferência do ACC ao APP ao cruzar o limite lateral ou vertical da TMA, ou em ponto acordado entre os órgãos[^1]; o Art. 844 da ICA 100-37 mantém o controle com o APP "até que [as aeronaves] sejam transferidas à TWR e estejam em comunicação com a mesma"[^1], transferência que, pelo Art. 848 da ICA 100-37, ocorre quando a aeronave estiver "nas vizinhanças do aeródromo" em condições de completar a aproximação e o pouso por referência visual, ou já tiver pousado[^1]; e, dentro da própria TWR, o Art. 853 da ICA 100-37 passa a aeronave da posição Torre para o Controle de Solo depois de esta "receber da 'Torre' a hora de pouso, autorização para deixar a pista em uso"[^1]. A coordenação entre posições de um mesmo órgão segue regra própria, à parte da coordenação entre órgãos distintos, conforme o Art. 852 da ICA 100-37[^1].

Só na chegada, a própria ICA 100-37 prevê um atalho: voos VFR podem ser transferidos diretamente entre ACC e TWR, sem passar pelo APP, desde que em coordenação com este — é o que dizem, cada um em sua Subseção, o parágrafo único do Art. 839 e o parágrafo único do Art. 848, ambos da ICA 100-37[^1]. Não há dispositivo equivalente para a partida: nem o Art. 840 nem o Art. 849 da ICA 100-37 trazem parágrafo com esse atalho[^1] — na partida, a cadeia completa, elo por elo, é a regra, sem a exceção que a chegada admite. O encadeamento descrito acima é, portanto, o percurso típico; o desvio documentado é só o da chegada VFR.

### Cadeia de transferência, em um olhar

<figure>
<svg viewBox="0 0 720 240" role="img" aria-label="Cadeia dos órgãos de controle, de DEL a CTR, com o espaço aéreo de cada elo e o sentido da cobertura top-down. As posições que não controlam, RÁDIO e informação de voo, não integram esta cadeia" style="max-width:100%;height:auto">
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
  <text class="or-td" x="360" y="26" text-anchor="middle">Cobertura top-down (convenção de rede, sentido inverso)</text>
  <path class="or-arw" d="M 640 40 L 80 40"/>
  <rect class="or-box" x="20" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="80" y="112">DEL</text>
  <text class="or-sub" x="80" y="134">Pátio</text>
  <rect class="or-box" x="160" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="220" y="112">GND</text>
  <text class="or-sub" x="220" y="134">Área de manobras</text>
  <rect class="or-box" x="300" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="360" y="110">TWR</text>
  <text class="or-sub" x="360" y="128">ATZ e Zona</text>
  <text class="or-sub" x="360" y="142">de Controle</text>
  <rect class="or-box" x="440" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="500" y="110">APP</text>
  <text class="or-sub" x="500" y="128">TMA e Zona</text>
  <text class="or-sub" x="500" y="142">de Controle</text>
  <rect class="or-box" x="580" y="88" width="120" height="64" rx="4"/>
  <text class="or-ttl" x="640" y="110">CTR</text>
  <text class="or-sub" x="640" y="128">CTA, UTA e</text>
  <text class="or-sub" x="640" y="142">restante da FIR</text>
  <path class="or-arw" d="M 140 120 L 158 120"/>
  <path class="or-arw" d="M 280 120 L 298 120"/>
  <path class="or-arw" d="M 420 120 L 438 120"/>
  <path class="or-arw" d="M 560 120 L 578 120"/>
</svg>
<figcaption>Encadeamento normal de um voo IFR entre os órgãos de <strong>controle</strong>. No diagrama, <code>CTR</code> aparece uma única vez e nomeia a posição de rede do ACC; a Zona de Controle está escrita por extenso, para não confundir os dois sentidos da sigla. A cobertura <em>top-down</em> percorre o sentido inverso: a posição superior responde pelo espaço aéreo das inferiores que não estiverem conectadas. As posições que não controlam — RÁDIO (AFIS) e informação de voo — ficam fora do diagrama de propósito: elas não recebem nem transferem controle, porque não há controle a transferir. Segue-se daí, como leitura deste manual e não como texto de norma, que um voo saindo de um aeródromo com AFIS entra na cadeia no elo do órgão de controle que tiver jurisdição sobre o espaço aéreo à frente, e não na TWR — ali não há TWR, e o órgão RÁDIO nada tem a transferir.</figcaption>
</figure>

!!! tip "Na rede (Vatbrz)"
    Antes de conectar, confira quem já está online. Se o CTR está conectado e você assume o APP, parte do espaço aéreo que estava sob cobertura *top-down* passa a ser sua — e a transferência dos tráfegos já em frequência precisa ser coordenada, não presumida.

## Indicativos de chamada

Este capítulo tratou de jurisdição e espaço aéreo — quem tem autoridade sobre o quê, e até onde. Ele não tratou de fonia: como cada órgão se identifica no ar é assunto de outro manual. O [Manual de Fraseologia para Voo Visual](../fraseologia-voo-visual/conceitos.pt.md) já reúne, em uma única tabela, o indicativo de chamada de cada órgão em português, inglês e espanhol; o [Manual de Fraseologia Aeronáutica](../fraseologia-aeronautica/index.pt.md) mostra esses indicativos em uso, em exemplos completos de comunicação. Para o "como se chama", comece por lá — este capítulo respondeu ao "quem é" e ao "até onde vai".

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulamenta no Brasil os Serviços de Tráfego Aéreo previstos no Anexo 11 e no Doc 4444 da OACI. Edição em vigor em 27/11/2025.
[^2]: [**ICA 100-12, Regras do Ar**](https://publicacoes.decea.mil.br/publicacao/ica-100-12): estabelece as regras aplicáveis à operação de aeronaves no espaço aéreo brasileiro. Edição em vigor em 28/11/2024.

---
