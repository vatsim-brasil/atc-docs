---
title: Serviços de Tráfego Aéreo
icon: material/headset
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Serviços](img/manual-espaco-aereo-servicos.png)

#

## Os serviços de tráfego aéreo

Serviço de Tráfego Aéreo é, antes de mais nada, um nome genérico. O item LXXXIV do Anexo VII da ICA 100-12 define a expressão como a que "se aplica, segundo o caso, aos serviços de informação de voo, alerta, assessoramento de tráfego aéreo, controle de tráfego aéreo (controle de área, controle de aproximação ou controle de aeródromo)"[^2]. São quatro serviços distintos, não um só, e nenhum deles é prestado automaticamente pelo simples fato de existir um órgão ATS na frequência — o que se presta depende da classe do espaço aéreo em que a aeronave está operando, matéria já tratada no capítulo anterior.

A própria ICA 100-37 confirma a lista pelo lado da divisão dos serviços: o Art. 28 enumera o "Serviço de Controle de Tráfego Aéreo, compreendendo o Serviço de Controle de Área, o Serviço de Controle de Aproximação e o Serviço de Controle de Aeródromo", o "Serviço de Informação de Voo" e o "Serviço de Alerta"[^1]. O Serviço de Assessoramento de Tráfego Aéreo fica de fora dessa lista por uma razão explícita, dada no parágrafo único do próprio artigo: ele "não é mencionado nesta Seção em virtude de ser planejado como uma transição à implementação do Serviço de Controle de Tráfego Aéreo"[^1] — ausência de redação, não de existência, como o capítulo anterior já registrou ao tratar da Classe F.

Este capítulo trata dos quatro, na ordem em que a ICA 100-37 os organiza: controle, informação de voo, alerta e, por fim, o assessoramento, cuja natureza temporária pede um tratamento à parte.

## Serviço de Controle de Tráfego Aéreo

O Anexo VII da ICA 100-12 define o Serviço de Controle de Tráfego Aéreo pelo que ele existe para evitar: um serviço prestado com a finalidade de "prevenir colisões: entre aeronaves; e entre aeronaves e obstáculos na área de manobras" e de "acelerar e manter ordenado o fluxo de tráfego aéreo"[^2]. A ICA 100-37 detalha o mesmo objetivo do lado operacional — para proporcionar o serviço, um órgão ATC deverá "dispor de informação sobre o movimento intencional de cada aeronave, ou variações do mesmo, e de dados atuais sobre a progressão real de cada uma delas", determinar as posições relativas entre as aeronaves conhecidas, "emitir autorizações e informações com a finalidade de prevenir colisão entre aeronaves sob seu controle e de acelerar e manter um fluxo de tráfego ordenado" e coordenar essas autorizações com outros órgãos envolvidos (Art. 30)[^1].

Esse objetivo tem um limite explícito. O Art. 93 da ICA 100-37 registra que "os objetivos do Serviço de Controle de Tráfego Aéreo não incluem a prevenção de colisão com o solo", e o parágrafo único do mesmo artigo acrescenta que isso não isenta o piloto de assegurar que a autorização recebida é segura nesse aspecto, exceto quando o voo IFR estiver sendo vetorado[^1] — isto é, quando, "sob vetoração", o controlador assume a responsabilidade pela navegação da aeronave e lhe transmite as orientações de proa e as mudanças de nível necessárias (Art. 921 da ICA 100-37)[^1]. A vetoração em si está fora do escopo deste manual, como o [índice](index.pt.md#fora-do-escopo) registra. Prevenir colisão entre aeronaves e organizar o fluxo — não prevenir colisão com o terreno — é o que o Serviço de Controle de Tráfego Aéreo promete.

O Art. 28 da ICA 100-37 divide o serviço em três, cada um prestado por um órgão diferente[^1]:

- **Serviço de Controle de Área**, prestado por um ACC ou por um APP ao qual tenha sido delegada a atribuição de prestá-lo dentro de determinado espaço aéreo (Art. 33)[^1];
- **Serviço de Controle de Aproximação**, prestado por um APP ou por um ACC ou TWR ao qual tenha sido delegada a atribuição (Art. 34)[^1];
- **Serviço de Controle de Aeródromo**, prestado por uma TWR à qual tenha sido delegada a atribuição de prestá-lo dentro de determinado espaço aéreo (Art. 35)[^1].

Como esses três serviços se distribuem entre os órgãos ATS da Vatsim Brasil — ACC, APP, TWR — é assunto do próximo capítulo.

Do lado do piloto, a contrapartida do controle é a autorização. A ICA 100-12 exige que, "antes de realizar um voo controlado, ou uma parte de um voo controlado", seja obtida a autorização do órgão ATC, solicitada mediante a apresentação do Plano de Voo (Art. 77)[^2]. É esse par — autorização emitida de um lado, exigida do outro — que distingue o controle dos demais serviços tratados a seguir.

## Serviço de Informação de Voo

O Serviço de Informação de Voo tem outro objetivo. O Anexo VII da ICA 100-12 o define como o serviço "prestado com a finalidade de proporcionar avisos e informações úteis para a realização segura e eficiente dos voos"[^2] — avisar e informar, não decidir por quem voa.

A ICA 100-37 fixa a quem ele se presta: a todas as aeronaves evoluindo no espaço aéreo sob jurisdição do Brasil que mantenham comunicação bilateral com um órgão ATS, ou que o solicitem (Art. 741)[^1]. O conteúdo mínimo inclui SIGMET e AIRMET, informação sobre atividade de nuvens de cinza vulcânica, sobre lançamento na atmosfera de material radioativo ou substância química tóxica, sobre mudanças na condição operacional dos auxílios à navegação e dos aeródromos, sobre balões livres não tripulados e qualquer outra informação "consideradas importantes para a segurança da navegação aérea" (Art. 744)[^1]. A isso soma-se a condição meteorológica reportada ou prevista nos aeródromos de partida, destino e alternativa, e a informação sobre risco de colisão para aeronaves que operem nas Classes C, D, E, F e G — com a ressalva de que essa informação "inclui somente as aeronaves conhecidas" e é "algumas vezes imprecisa ou incompleta" (Art. 745)[^1]. Para o voo VFR em particular, o serviço ainda inclui informação sobre condições meteorológicas ao longo da rota onde a condução do voo sob as regras de voo visual possa se tornar impraticável (Art. 747)[^1].

Nada disso substitui o piloto. O Art. 742 da ICA 100-37 é explícito ao dizer que o Serviço de Informação de Voo "não isenta o piloto de suas responsabilidades e somente a ele compete tomar qualquer decisão no tocante a alterações no Plano de Voo e demais medidas que lhe parecerem convenientes para a maior segurança do voo"[^1]. E quando um mesmo órgão presta, ao mesmo tempo, informação de voo e controle de tráfego aéreo, é o controle que tem precedência (Art. 743)[^1] — confirmação, pelo lado normativo, de que são serviços de natureza diferente, não dois nomes para a mesma coisa.

## Serviço de Alerta

O Anexo VII da ICA 100-12 define o Serviço de Alerta como o serviço "prestado para notificar os órgãos apropriados a respeito das aeronaves que necessitem de ajuda de busca e salvamento e para auxiliar tais órgãos no que for necessário"[^2] — é o serviço que aciona a busca e salvamento, não o que evita o acidente.

Diferente do controle e da informação de voo, o Serviço de Alerta não depende da classe do espaço aéreo. O Art. 32 da ICA 100-37 determina que ele — junto com o Serviço de Informação de Voo — seja proporcionado "em todas as Regiões de Informação de Voo sob jurisdição do Brasil"[^1], e o Art. 38 atribui a sua prestação ao órgão ATS que tenha jurisdição no espaço aéreo considerado[^1]. O que o aciona é uma entre três condições, fixadas pelo Art. 795 da ICA 100-37: a aeronave "receber o Serviço de Controle de Tráfego Aéreo"; ou "apresentar Plano de Voo e sua decolagem tenha sido notificada a um órgão ATS"; ou "se saiba ou se suspeite que esteja sendo objeto de interferência ilícita"[^1].

A responsabilidade de iniciar o serviço numa emergência recai sobre quem primeiro toma conhecimento dela. O Art. 797 da ICA 100-37 atribui essa responsabilidade à "TWR, APP ou RDO (rádio) que tomar conhecimento de uma emergência em voo VFR ou IFR", com o dever de notificar imediatamente o ACC e o ARCC correspondentes[^1]. Se um aeródromo de destino sem órgão ATS não confirmar a chegada de uma aeronave que apresentou Plano de Voo, cabe ao órgão ATS que notificou a decolagem informar o ACC (Art. 796)[^1] — e, nesse caso, sem órgão ATS no destino, o Serviço de Alerta só é prestado "caso solicitado pelo piloto, pelo explorador ou qualquer outra pessoa", ressalvadas as situações dos Arts. 797 e 798 (Art. 796, parágrafo único)[^1].

## Serviço de Assessoramento de Tráfego Aéreo

O Serviço de Assessoramento de Tráfego Aéreo é o quarto serviço, e o capítulo anterior já tratou dele com profundidade ao descrever a Classe F. O Art. 778 da ICA 100-37 explica que ele existe para tornar "a informação sobre perigos de colisão mais eficaz do que mediante a simples prestação do Serviço de Informação de Voo", e é proporcionado às aeronaves que efetuarem voos IFR em espaços aéreos ou rotas de assessoramento — a Classe F[^1]. Não confere o mesmo grau de segurança do controle, porque as informações relativas ao tráfego de que dispõe o órgão ATS ali "podem ser incompletas" (Art. 779)[^1], e por isso o Plano de Voo e suas mudanças não estão sujeitos a autorização: o órgão só sugere, por meio de informações de tráfego e avisos para evitar tráfego, e o piloto decide (Art. 780)[^1].

O que este capítulo acrescenta é o que a Classe F já sinaliza: trata-se de uma medida transitória. O § 2° do Art. 21 da ICA 100-37 classifica a utilização do Serviço de Assessoramento de Tráfego Aéreo como "uma medida temporária até o momento em que puder ser substituída pelo Serviço de Controle de Tráfego Aéreo"[^1] — é por isso, inclusive, que o Art. 28, ao dividir os Serviços de Tráfego Aéreo na seção anterior deste capítulo, não o inclui.

Para o detalhamento de a quem se presta, o que garante e por que o Serviço de Informação de Voo chega ao IFR e ao VFR de maneiras diferentes na Classe F, ver [Classes de Espaço Aéreo, seção Classe F](02-classes.pt.md#classe-f).

## Qual serviço em qual classe

A tabela abaixo cruza os quatro serviços com as sete classes de espaço aéreo. As colunas de **Controle de Tráfego Aéreo** e de **Assessoramento de Tráfego Aéreo** seguem a matriz do Anexo II da ICA 100-37[^1], já reproduzida no capítulo anterior; as colunas de **Informação de Voo** e de **Alerta** seguem os artigos que fixam o alcance desses dois serviços, e não o Anexo II. A razão está na natureza do Anexo: ele lista os serviços que *definem* cada classe, não todos os que ali se prestam. Ler a matriz como se ela esgotasse os serviços prestados é o erro que esta tabela existe para evitar. O detalhamento por tipo de voo (IFR/VFR), a separação e a informação de tráfego que acompanham cada célula estão na [tabela consolidada do capítulo 02](02-classes.pt.md#tabela-consolidada-anexo-ii-da-ica-100-37).

| Classe | Controle de Tráfego Aéreo | Informação de Voo | Assessoramento de Tráfego Aéreo | Alerta |
| --- | --- | --- | --- | --- |
| **A** | Sim | Sim | Não | Sim |
| **B** | Sim | Sim | Não | Sim |
| **C** | Sim | Sim | Não | Sim |
| **D** | Sim | Sim | Não | Sim |
| **E** | Sim, somente para o IFR | Sim — e é o serviço que o Anexo II atribui ao voo VFR da classe | Não | Sim |
| **F** | Não | Sim — ao voo IFR sem necessidade de solicitação; ao voo VFR, quando solicitado\* | Sim, somente para o IFR | Sim |
| **G** | Não | Sim — o Anexo II o atribui aos dois tipos de voo, "quando possível e solicitado pelo piloto" | Não | Sim |

\* A assimetria na Classe F é a aplicação do Art. 741 da ICA 100-37, acima: o voo IFR é obrigado, pelo Anexo II, a manter comunicação bilateral contínua, e por isso recebe o Serviço de Informação de Voo pelo inciso I, sem precisar solicitar; o voo VFR não tem essa obrigação — a coluna de radiocomunicação da linha F / VFR registra "Não" — e o recebe pelo inciso II, mediante solicitação[^1]. A alínea *c* do inciso VI do Art. 21 da mesma Instrução garante o piso comum: qualquer voo da classe que solicitar recebe[^1]. Detalhamento em [Classes de Espaço Aéreo, seção Classe F](02-classes.pt.md#classe-f).

Notas de leitura da tabela:

- **Por que a coluna de Informação de Voo é "Sim" em todas as classes.** O serviço não é privativo das classes em que o Anexo II o nomeia. O Art. 32 da ICA 100-37 determina que os Serviços de Informação de Voo e de Alerta sejam proporcionados "em todas as Regiões de Informação de Voo sob jurisdição do Brasil"[^1] — e, pelo Art. 19, parágrafo único, da mesma Instrução, as Áreas de Controle, as Zonas de Controle e as ATZ ficam *dentro* da FIR[^1]. O Art. 741 confirma pelo lado do destinatário: o serviço é proporcionado a todas as aeronaves no espaço aéreo sob jurisdição do Brasil que mantenham comunicação bilateral com um órgão ATS ou que o solicitem[^1]. E o Art. 743 pressupõe exatamente a coexistência: quando um órgão presta os dois ao mesmo tempo, o controle tem precedência sobre a informação de voo[^1] — precedência entre serviços simultâneos, não exclusão de um deles.
- **O conteúdo confirma o alcance.** O inciso II do Art. 745 da ICA 100-37 inclui no Serviço de Informação de Voo a informação sobre risco de colisão para aeronaves que operem nas Classes C, D, E, F e G[^1]; e as informações do Art. 744 — SIGMET e AIRMET, cinzas vulcânicas, mudanças na condição dos auxílios à navegação e dos aeródromos, balões livres não tripulados — não têm recorte por classe[^1]. Um voo em Classe A recebe SIGMET pelo Serviço de Informação de Voo, não pelo Serviço de Controle de Tráfego Aéreo.
- **O que muda entre as classes, então, não é a existência do serviço, e sim o seu papel.** Nas Classes A a D o serviço que define a classe é o controle, e a informação de voo o acompanha; nas Classes E (VFR), F e G a informação de voo é o que o piloto tem, porque não há controle a que recorrer. É essa diferença que a coluna de Controle de Tráfego Aéreo registra.
- Nas Classes C e D, o Anexo II da ICA 100-37 lista "informação de tráfego" como item específico para o voo VFR — um elemento de informação embutido no próprio Serviço de Controle de Tráfego Aéreo da classe, e distinto do Serviço de Informação de Voo tratado nas notas acima[^1]. Ver a tabela consolidada e as notas do capítulo 02 para o texto exato de cada classe.
- O Serviço de Alerta, como a informação de voo, não é condicionado à classe do espaço aéreo — mesmo Art. 32[^1] —, e é acionado sempre que se cumprir uma das três condições do Art. 795 da ICA 100-37[^1], tratadas na seção anterior.
- Para o detalhamento por tipo de voo (IFR/VFR) dentro de cada classe — inclusive a separação provida —, ver a [tabela consolidada do capítulo 02](02-classes.pt.md#tabela-consolidada-anexo-ii-da-ica-100-37).

## O que informar não é controlar

!!! danger "Informar não é controlar"
    O Serviço de Informação de Voo **não** separa aeronaves e **não** emite autorizações. Quem presta apenas informação de voo não usa verbos que impliquem controle — "suba", "desça", "mantenha", "autorizado". Ele informa, transmite condições e responde com **CIENTE**.

    Quando retransmite uma autorização emitida por um órgão ATC, deve deixar claro de quem partiu a autorização.

A base dessa regra está na própria definição dos dois serviços, lado a lado no Anexo VII da ICA 100-12: o Serviço de Controle de Tráfego Aéreo existe para "prevenir colisões" e "acelerar e manter ordenado o fluxo de tráfego aéreo"[^2], o que ele faz emitindo "autorizações e informações com a finalidade de prevenir colisão entre aeronaves sob seu controle e de acelerar e manter um fluxo de tráfego ordenado" (Art. 30, III, da ICA 100-37)[^1]; o Serviço de Informação de Voo existe para "proporcionar avisos e informações úteis"[^2]. O contraste fica ainda mais claro na Seção IX da ICA 100-37, intitulada "Autorizações e instruções dos órgãos ATC": é por meio de autorizações **e instruções** que os órgãos ATC provêm a separação exigida em cada classe (Art. 39)[^1] — um instrumento que a norma reserva ao órgão de controle. Nenhum artigo da ICA 100-37 atribui ao Serviço de Informação de Voo o poder de emitir autorização ou de separar aeronaves — essa competência pertence ao Serviço de Controle de Tráfego Aéreo (Art. 30, III, e Art. 39, ambos da ICA 100-37)[^1].

O caso mais concreto dessa fronteira é o AFIS, o Serviço de Informação de Voo de Aeródromo, normalmente prestado por um órgão ATS identificado como "RÁDIO" (Art. 783 da ICA 100-37)[^1]. A própria ICA 100-37 avisa: dentro da Zona de Informação de Voo (FIZ) onde o AFIS é prestado, "não há prestação de Serviço de Controle de Tráfego Aéreo e, por isso, não devem ser esperadas autorizações de controle de tráfego aéreo" (Art. 786, § 1°)[^1]. O que o órgão RÁDIO transmite às aeronaves inclui, entre os elementos básicos de informação, "mensagens, incluindo autorizações, recebidas de outros órgãos ATS para retransmissão à aeronave" (Art. 788, VII)[^1] — ou seja, a única autorização que passa pela frequência do RÁDIO é uma autorização de outro órgão, apenas retransmitida. É exatamente essa retransmissão que o bloco acima cobra: deixar claro de quem partiu a autorização, porque quem fala não é quem autorizou.

Este bloco reforça, com a base normativa, o que o [Manual de Fraseologia para Voo Visual](../fraseologia-voo-visual/conceitos.pt.md) já pratica na fonia.

!!! tip "Na rede (Vatbrz)"
    Nem toda posição conectada na rede presta Serviço de Controle de Tráfego Aéreo. As posições de controle — `_DEL`, `_GND`, `_TWR`, `_APP` e `_CTR` — prestam-no aos quatro destinatários que o Art. 29 da ICA 100-37 relaciona: todos os voos IFR nas Classes A, B, C, D e E; todos os voos VFR nas Classes B, C e D; todos os voos VFR Especiais; e todo o tráfego de aeródromo nos aeródromos controlados[^1]. Repare que só os dois primeiros incisos são recortados por classe — o VFR Especial e o tráfego de aeródromo em aeródromo controlado entram pelo que são, não por onde estão, e a ATZ, aliás, não tem classe alguma (NOTA 2 do Anexo II)[^1]. As posições **RÁDIO** (`_R_TWR`), que operam o AFIS, não prestam: na FIZ "não há prestação de Serviço de Controle de Tráfego Aéreo e, por isso, não devem ser esperadas autorizações de controle de tráfego aéreo" (Art. 786, § 1°)[^1].

    E mesmo em uma posição de controle o alcance tem limite. Fora do espaço aéreo controlado — em Classe F ou G sob cobertura *top-down*, por exemplo — o que você presta ao piloto é informação, não controle. Reconhecer essa fronteira é o que separa uma instrução válida de uma instrução que você não tinha autoridade para emitir.

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulamenta no Brasil os Serviços de Tráfego Aéreo previstos no Anexo 11 e no Doc 4444 da OACI. Edição em vigor em 27/11/2025.
[^2]: [**ICA 100-12, Regras do Ar**](https://publicacoes.decea.mil.br/publicacao/ica-100-12): estabelece as regras aplicáveis à operação de aeronaves no espaço aéreo brasileiro. Edição em vigor em 28/11/2024.
