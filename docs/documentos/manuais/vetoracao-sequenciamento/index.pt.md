---
title: Introdução
icon: material/radar
---

--8<-- "includes/abreviacoes.md"

# Introdução

## Apresentação

Num controle convencional, o controlador sabe onde a aeronave está porque o piloto informa. Já no controle com vigilância ATS, ele vê a aeronave na tela, e isso muda o que ele pode fazer: em vez de esperar a aeronave chegar a um fixo, pode **levá-la** até onde precisa, por meio de proas, níveis e velocidades. Isso é a vetoração.

Na aproximação, a vetoração tem um objetivo prático: pôr as aeronaves que chegam **em fila na final, com o espaçamento certo e o mínimo de atraso**. É o sequenciamento. Para isso, o controlador combina três ferramentas: a trajetória (proas e atalhos), a velocidade e, quando nada mais resolve, a espera.

Este manual é para quem vai controlar uma posição de aproximação (`APP`) ou de centro (`CTR`) na Vatsim Brasil e precisa saber vetorar com segurança: quando pode, como fazer, o que dizer na frequência e como montar uma sequência que funcione.

| Revisão | Data       | Descrição         | Revisor |
| ------- | ---------- | ----------------- | ------- |
| 10/2026 | 08/10/2026 | Criação do Manual | —       |

## Sobre este Manual

A base normativa é a **ICA 100-37**[^1]: o Capítulo XI (Serviço de Vigilância ATS) para identificação, vetoração e separação; o Capítulo V (Serviço de Controle de Aproximação) para ordem de aproximação, aproximação visual e hora estimada de aproximação; e as Seções XXXI a XXXIII do Capítulo III para ajuste de velocidade e espera. A fraseologia segue o **MCA 100-16**[^2].

Algumas partes do manual são **técnica**, e não norma: a geometria das curvas, as distâncias de interceptação recomendadas e as regras de bolso de espaçamento. Esses trechos aparecem marcados como boa prática. Quando uma boa prática e a ICA 100-37 parecerem divergir, vale a ICA 100-37.

## Escopo

Este manual cobre:

- a identificação da aeronave e o início do Serviço de Vigilância ATS;
- a vetoração: objetivos, métodos, responsabilidades e término;
- a separação mínima com vigilância ATS e os mínimos de esteira de turbulência na aproximação;
- as técnicas de vetoração para interceptar uma radial, um curso de aproximação final ou uma aproximação visual;
- o ajuste de velocidade horizontal e vertical;
- o sequenciamento das chegadas, da ordem de aproximação até a transferência para a torre;
- a espera e a hora estimada de aproximação;
- a fraseologia correspondente, em português e inglês.

## Fora do escopo

Não fazem parte deste manual:

- a coordenação entre órgãos e a transferência de controle, que estão no [Manual de Coordenação e Transferência](../coordenacao-transferencia/index.pt.md);
- a separação convencional (por tempo, distância DME ou reporte de posição), que está no [Manual de Separação e Esteira de Turbulência](../separacao-esteira/03-horizontal.pt.md);
- os mínimos de esteira de turbulência por tempo na pista, que pertencem ao controle de aeródromo e estão no [Manual de Separação e Esteira de Turbulência](../separacao-esteira/04-esteira.pt.md);
- as aproximações radar de vigilância e de precisão (PAR), que no Brasil o DECEA restringe a casos específicos[^3];
- as operações em pistas paralelas.

!!! warning "Importante"
    Conteúdo destinado ao ambiente de simulação de voo. Em operações reais, utilize sempre as publicações oficiais vigentes, as cartas aeronáuticas e os canais AIS e ATS.

## Como usar este manual

1. Leia **Fundamentos da Vetoração** para saber quando você pode vetorar, o que passa a ser sua responsabilidade e qual separação aplicar.
2. Leia **Técnicas de Vetoração** para levar a aeronave até onde precisa, em especial até a aproximação final.
3. Leia **Ajuste de Velocidade** para conhecer os limites e o método do controle de velocidade.
4. Leia **Sequenciamento** para juntar tudo: ordem de chegada, espaçamento na final, espera e transferência para a torre.
5. Consulte a **Fraseologia** sempre que tiver dúvida sobre o que dizer.
6. Revise o **Checklist Rápido** antes de abrir uma posição de aproximação.

!!! tip "Leitura complementar"
    Este manual pressupõe os conceitos do [Manual de Espaço Aéreo e Serviços ATS](../espaco-aereo-servicos-ats/index.pt.md): classes de espaço aéreo, TMA, CTR, níveis e altitude de transição. Para o uso do EuroScope (etiquetas, `F1 + S`, `F1 + D`), veja [EuroScope](../../../fundamentos/softwares/euroscope/index.pt.md). Os limites e procedimentos de cada TMA estão na seção [Terminais](../../../MOP/terminais/index.pt.md).

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulamenta no Brasil os Serviços de Tráfego Aéreo previstos no Anexo 11 e no Doc 4444 da OACI. Edição em vigor em 27/11/2025.
[^2]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): estabelece os padrões de fraseologia de tráfego aéreo. Edição aprovada pela Portaria DECEA/DNOR1 n° 1.716, de 28/04/2025.
[^3]: **ICA 100-37, Arts. 1020 e 1023**: a aproximação radar de vigilância só é autorizada a pedido do piloto ou na falta de outro procedimento publicado, e a PAR é realizada no Brasil somente por aeronaves militares.
