---
title: Separação Vertical
icon: material/arrow-up-down
---

--8<-- "includes/abreviacoes.md"

# Separação Vertical

## A forma mais simples

A separação vertical é a mais simples de aplicar e a que menos depende de equipamento. Basta que as aeronaves voem em níveis diferentes, com o altímetro ajustado da mesma forma. Em rota, isso significa ajustar 1013,2 hPa e voar no nível de voo atribuído[^1]. Abaixo da altitude de transição, todas usam o QNH e voam em altitudes.

Por isso ela é a primeira ferramenta de qualquer controlador. Se você não tem certeza de que duas aeronaves estão separadas lateral ou longitudinalmente, ponha-as em níveis diferentes.

## Mínimos

| Faixa | Mínimo | Fonte |
| --- | --- | --- |
| Abaixo do FL 290 | **1.000 pés** | [^2] |
| Do FL 290 ao FL 410, inclusive, entre aeronaves aprovadas RVSM | **1.000 pés** | [^2] [^3] |
| Do FL 290 ao FL 410, inclusive, se **alguma** das aeronaves não for aprovada RVSM | **2.000 pés** | [^2] [^4] |
| Acima do FL 410 | **2.000 pés** | [^2] |
| Na TMA, aplicada pelo APP | **1.000 pés** | [^5] |

Todos os níveis do FL 290 ao FL 410 nas FIR brasileiras são espaço aéreo RVSM[^3]. O normal, então, é 1.000 pés em toda a faixa de cruzeiro. A exceção é a aeronave **não aprovada RVSM**, que exige 2.000 pés de qualquer outra[^4].

### Como saber se a aeronave é RVSM

A aeronave aprovada RVSM tem a letra `W` no item 10 do plano de voo. Um piloto sem aprovação deve dizer **"negativo RVSM"** no contato inicial dentro do espaço aéreo RVSM, em todo pedido de mudança de nível e em todo cotejamento de autorização de nível[^6]. Se tiver dúvida, pergunte.

> **PT ART, confirme aprovação RVSM?**
>
> **\*PT ART, negativo RVSM.**

Os níveis de cruzeiro do espaço aéreo RVSM e a regra de rumo estão no [Manual de Espaço Aéreo e Serviços ATS](../espaco-aereo-servicos-ats/05-regras.pt.md#espaco-aereo-rvsm).

!!! note "Na rede"
    Na VATSIM, quase todo jato voa com `W` no plano de voo, e os aviões leves e turbo-hélices raramente sobem ao FL 290. Mas aeronaves antigas, aeronaves militares e planos de voo mal preenchidos aparecem. Se um tráfego sem `W` pedir o FL 290 ou acima, aplique 2.000 pés ou mantenha-o abaixo do FL 290.

## Nível de cruzeiro

Os níveis de cruzeiro seguem a tabela da ICA 100-12 em função do rumo magnético, a menos que o ACC autorize outro nível ou que a carta de rota preveja algo diferente[^7]. Em aerovia de sentido único, todos os níveis podem ser usados[^8].

Ao decidir entre duas aeronaves que querem o mesmo nível:

- Quem **já está** no nível tem, normalmente, prioridade sobre quem o pede. Entre duas aeronaves no mesmo nível, a **da frente** tem prioridade[^9].
- Para aeronaves com o mesmo destino, atribua os níveis de cruzeiro, na medida do possível, na **ordem em que vão se aproximar**[^10]. Quem vai pousar primeiro deve estar mais baixo, para descer primeiro.

## Usar um nível que outra aeronave deixou

Uma aeronave pode ser autorizada a um nível ocupado por outra **depois que esta tiver reportado que o deixou**[^11]. Não basta a autorização para a outra descer, nem o alvo começar a se mover na tela: é preciso que ela tenha deixado o nível.

Essa regra tem três exceções. Nelas, você só autoriza o nível quando a aeronave que o deixou reportar que **já está em outro nível**, ou que está passando por um nível com a separação mínima[^12]:

- quando se sabe que há **turbulência forte**;
- quando a aeronave mais alta está fazendo uma **subida de cruzeiro**;
- quando a **diferença de desempenho** entre as duas pode levar a uma separação menor que a mínima.

No APP, a regra é a mesma. Com turbulência forte, a autorização fica suspensa até a aeronave que deixou o nível informar que já está em outro nível com a separação mínima[^13].

!!! example "Exemplo"
    Um B738 está no FL 160 e um C208, no FL 150. Você quer descer o C208 para o FL 140 e o B738 para o FL 150. O B738 só pode receber o FL 150 depois que o C208 reportar **livrando o FL 150**. Mas o B738 desce muito mais rápido que o C208. É a terceira exceção: espere o C208 informar que está mantendo o FL 140, ou que passou o FL 140 com folga, antes de autorizar o B738.

Com vigilância ATS, o modo C ou o ADS-B mostram o nível de cada aeronave. A ICA 100-37 define quando uma aeronave está **mantendo**, **livrando**, **cruzando** ou **atingindo** um nível pela leitura da tela. Os critérios estão no [Manual de Vetoração e Sequenciamento](../vetoracao-sequenciamento/01-fundamentos.pt.md#niveis-na-tela).

### Na espera

Num mesmo circuito de espera, aeronaves que descem com razões de descida bem diferentes podem perder a separação, mesmo uma partindo de cima e a outra de baixo. Se for preciso, dê uma **razão máxima de descida** para a de cima e uma **razão mínima** para a de baixo[^14].

## Cruzar o nível de outra aeronave

Para uma aeronave subir ou descer **através** do nível de outra, a separação vertical precisa ser trocada por uma horizontal durante o cruzamento.

- **Com vigilância ATS**, basta manter os 5 NM entre os alvos durante todo o cruzamento.
- **Sem vigilância**, use os mínimos longitudinais para aeronaves subindo ou descendo, que estão em [Separação Horizontal](03-horizontal.pt.md#subindo-ou-descendo).

!!! note "Boa prática"
    Quando a mudança de nível é grande, autorize a aeronave primeiro até o nível **adjacente** ao da outra, com uma restrição de horário, de fixo ou de distância DME para seguir adiante. A própria ICA 100-37 sugere isso para garantir a separação mínima no momento do cruzamento[^15].

    > **TAM 3246, suba para FL 090 até 15 NM do VOR Campinas.**

## Restrições de nível

A forma mais segura de garantir a separação vertical num ponto é dizer **onde** a aeronave tem de estar acima ou abaixo de um nível. Você também pode autorizar a mudança de nível num horário, num local ou com uma razão vertical especificada[^16].

> **ABJ 9203, cruze NEROK no FL 240 ou abaixo.**
>
> **TAM 3506, autorizado para KONSO FL 180, cruze VOR Santa Cruz no FL 120 ou acima.**

Restrições de razão de subida e de descida estão em [Ajuste de Velocidade](../vetoracao-sequenciamento/03-velocidade.pt.md#ajuste-de-velocidade-vertical), no Manual de Vetoração e Sequenciamento.

[^1]: **ICA 100-37, Art. 322**. Ver [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 323**.
[^3]: **AIP-Brasil, ENR 2.2, itens 1.1 e 1.3**.
[^4]: **AIP-Brasil, ENR 2.2, item 1.6**.
[^5]: **ICA 100-37, Art. 432**.
[^6]: **AIP-Brasil, ENR 2.2, item 1.8.1**, e **MCA 100-16, Arts. 48 e 76**. Ver [MCA 100-16](https://publicacoes.decea.mil.br/publicacao/MCA-100-16).
[^7]: **ICA 100-37, Art. 325**, e **ICA 100-12, Art. 142 e Anexo IV**. Ver [ICA 100-12](https://publicacoes.decea.mil.br/publicacao/ica-100-12).
[^8]: **ICA 100-37, Art. 326**.
[^9]: **ICA 100-37, Art. 329 e parágrafo único**.
[^10]: **ICA 100-37, Art. 328**.
[^11]: **ICA 100-37, Art. 330**.
[^12]: **ICA 100-37, Art. 330, incisos I a III, e Art. 331**.
[^13]: **ICA 100-37, Art. 433 e parágrafo único**.
[^14]: **ICA 100-37, Art. 332**.
[^15]: **ICA 100-37, Art. 364, § 2°**, e **Art. 373, parágrafo único**. Fraseologia do **MCA 100-16, Art. 118**.
[^16]: **ICA 100-37, Art. 327**. Fraseologia do **MCA 100-16, Art. 92**.
