---
title: Fundamentos da Separação
icon: material/arrow-split-horizontal
---

--8<-- "includes/abreviacoes.md"

# Fundamentos da Separação

## O que é separar

Para prestar o Serviço de Controle de Tráfego Aéreo, o órgão ATC precisa saber onde está cada aeronave e para onde ela vai, determinar a posição de uma em relação à outra e emitir autorizações e informações **para prevenir colisões** e manter o tráfego fluindo em ordem[^1]. Separar é a parte disso que tem número: manter entre duas aeronaves, no mínimo, uma distância vertical, lateral ou longitudinal definida pela norma. Esse número é o **mínimo de separação**.

O mínimo é um piso, não uma meta. Duas regras gerais valem para todos os mínimos deste manual:

- **Nenhuma autorização pode reduzir a separação abaixo do mínimo aplicável.** Isso vale para qualquer manobra que você autorize, e não só para as que você planejou[^2].
- **Se a separação em uso não puder ser mantida, estabeleça outra antes de perder a primeira.** Se duas aeronaves estão separadas por nível e uma precisa descer, a separação horizontal já deve existir quando ela deixar o nível[^3].

Quando uma falha ou degradação de equipamento (navegação, comunicação, altímetro ou outro sistema) deixa a aeronave abaixo do desempenho exigido, a tripulação deve avisar, e o controlador passa a usar outro tipo ou outro mínimo de separação[^4]. Em circunstâncias excepcionais, como interferência ilícita ou dificuldade de navegação, aplique separações **maiores** que os mínimos[^5].

## Quem recebe separação

O controle não separa todo mundo de todo mundo. A obrigação depende da classe do espaço aéreo e das regras de voo de cada aeronave[^6]:

| Classe | O controle separa |
| --- | --- |
| **A** e **B** | Todos os voos entre si |
| **C** | IFR de IFR e IFR de VFR. VFR de VFR, não |
| **D** e **E** | Só IFR de IFR |
| **F** | IFR de IFR, se for prático e possível |
| Qualquer classe | IFR de VFR especial, e VFR especial de VFR especial |

Onde o controle não separa, ele informa. Na classe D, por exemplo, um IFR e um VFR recebem **informação de tráfego** um sobre o outro, e cabe aos pilotos se manterem afastados. As classes e o serviço que cada uma recebe estão no [Manual de Espaço Aéreo e Serviços ATS](../espaco-aereo-servicos-ats/02-classes.pt.md).

!!! info "Tráfego de aeródromo"
    Na torre, além do que a classe exige, a separação entre aeronaves que usam a mesma pista segue regras próprias de pista e de esteira de turbulência. Elas estão em [Separação no Aeródromo](05-aerodromo.pt.md).

## As formas de separação

A separação pode ser dada de três formas[^7]:

| Forma | Como | Página |
| --- | --- | --- |
| **Vertical** | Níveis ou altitudes diferentes | [Separação Vertical](02-vertical.pt.md) |
| **Horizontal lateral** | Rotas diferentes, ou áreas geográficas diferentes | [Separação Horizontal](03-horizontal.pt.md) |
| **Horizontal longitudinal** | Um intervalo de tempo ou distância entre aeronaves na mesma rota, em rotas opostas ou que se cruzam | [Separação Horizontal](03-horizontal.pt.md) |

Basta **uma** delas. Duas aeronaves com 1.000 pés de diferença estão separadas, mesmo se uma estiver exatamente acima da outra. Duas aeronaves no mesmo nível a 5 NM uma da outra, com vigilância ATS, também estão.

Existe ainda a **separação composta**, que combina a vertical com uma horizontal usando metade de cada mínimo. Ela só pode ser aplicada onde o DECEA autorizar[^8] e não é usada na rede.

### Com ou sem vigilância ATS

Os mínimos horizontais mudam muito conforme o controlador tenha ou não vigilância ATS (radar, ADS-B ou MLAT):

- **Com vigilância**, você mede a distância entre os alvos na tela. O mínimo normal é de **5 NM**.
- **Sem vigilância**, a separação é **convencional**. Você depende de reportes de posição, estimados e distâncias DME ou GNSS informados pelo piloto, e os mínimos são muito maiores: 10 a 15 minutos, ou 20 NM.

Na Vatsim Brasil, quase toda posição de APP e de CTR tem vigilância, e a separação convencional aparece pouco no continente. Mesmo assim, ela continua importante. Ela é a base do controle oceânico, é o que sobra quando um alvo some da tela e explica regras que o controle radar herdou, como os mínimos de partida.

## Própria separação em VMC

Nas classes **D** e **E**, um voo controlado pode pedir para **manter a própria separação** em relação a outra aeronave, permanecendo em condições meteorológicas visuais (VMC). Quando o outro piloto concorda, o controle pode autorizar[^9]. Isso vale também para IFR, e é a exceção prevista à regra de separar IFR de IFR[^10].

As condições são[^9]:

- só **de dia**;
- só para **uma parte específica do voo**, na subida ou na descida, a **10.000 pés ou abaixo**;
- se houver risco de não manter VMC, você dá uma **instrução alternativa**, para o caso de o piloto não conseguir manter as condições visuais durante a autorização;
- se as condições estiverem piorando, o piloto avisa **antes** de entrar em IMC e cumpre a instrução alternativa.

Durante esse trecho, o controle não aplica separação entre as duas aeronaves. Os pilotos é que se mantêm afastados um do outro[^11].

> **PT ABC, tráfego Boeing 737, na radial 084 do VOR Cuiabá, subindo VMC até FL 140.**
>
> **GLO 1844, autorizado descida em VMC.**
>
> **FAB 2123, mantenha sua própria separação.**

Fonte: MCA 100-16[^16].

A aproximação visual com instrução de **seguir e manter a própria separação** da aeronave da frente é o caso mais comum dessa ideia. Ela está no [Manual de Vetoração e Sequenciamento](../vetoracao-sequenciamento/04-sequenciamento.pt.md#aproximacoes-visuais-em-sequencia).

## Tráfego essencial

**Tráfego essencial** é o tráfego controlado a que o controle deveria dar separação, mas que, em relação a um certo voo, não está ou não estará separado dele pelos mínimos[^12]. Isso acontece justamente na própria separação em VMC, ou quando um mínimo foi perdido.

Sempre que dois voos controlados forem tráfego essencial um para o outro, informe ambos[^13]. A informação contém[^14]:

- a direção do voo e o tipo da aeronave;
- a **categoria de esteira de turbulência**, mas só se a outra aeronave for de categoria **mais pesada** do que a que recebe a informação;
- o nível e uma das seguintes informações: a hora estimada no ponto de notificação mais próximo de onde os níveis vão se cruzar, a posição relativa pelo relógio e a distância, ou a posição real ou estimada.

Um voo VFR nunca é tráfego essencial para outro VFR, a não ser na classe B[^15].

[^1]: **ICA 100-37, Art. 30, incisos I a III**. Ver [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 39, § 8°**.
[^3]: **ICA 100-37, Art. 42**.
[^4]: **ICA 100-37, Art. 43 e parágrafo único**, e **Art. 337**.
[^5]: **ICA 100-37, Art. 41 e §§ 1° e 2°**.
[^6]: **ICA 100-37, Art. 39, incisos I a V e § 1°**.
[^7]: **ICA 100-37, Art. 39, § 2°, incisos I e II**, e **Art. 334**.
[^8]: **ICA 100-37, Art. 39, § 2°, inciso III, e § 3°**.
[^9]: **ICA 100-37, Art. 94 e § 1°**.
[^10]: **ICA 100-37, Art. 40**.
[^11]: **ICA 100-37, Art. 94, §§ 2° e 3°**.
[^12]: **ICA 100-37, Art. 114**.
[^13]: **ICA 100-37, Art. 115 e parágrafo único**.
[^14]: **ICA 100-37, Art. 116**.
[^15]: **ICA 100-37, Art. 114, § 4°**.
[^16]: **MCA 100-16, Art. 117**. Ver [MCA 100-16](https://publicacoes.decea.mil.br/publicacao/MCA-100-16).
