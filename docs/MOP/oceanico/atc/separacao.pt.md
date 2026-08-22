---
title: Separação, Rotas e Desvios
icon: material/arrow-split-vertical
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Sem radar, a separação não é observada: é **calculada e protegida**.

!!! danger "Leia antes de aplicar qualquer número"
    Nenhuma mínima desta página vale isolada. Cada uma depende de capacidade declarada **e confirmada**, de tipo de rota e de meio de comunicação. Aplicar valor menor sem a condição satisfeita é reduzir separação sem base.

## Tabela de decisão

Pergunte na ordem e pare na primeira linha cuja condição esteja satisfeita. **Quando mais de uma linha se aplicar, prevalece a maior mínima.**

| Condição                                                                         | Mínima                      | Fonte       |
| --------------------------------------------------------------------------------- | --------------------------- | ----------- |
| Ambas RVSM, entre o FL 290 e o FL 410, em níveis diferentes                       | **1.000 pés**               | [^1] [^2]   |
| Alguma sem RVSM, ou RVSM suspenso por turbulência severa                          | **2.000 pés**               | [^3] [^4]   |
| Ambas RNP 10, rotas paralelas ou que não se interceptam                           | **50 NM** laterais          | [^5]        |
| Alguma sem certificação RNP 10                                                    | **100 NM** laterais         | [^6]        |
| Mesma rota e nível, técnica do número Mach, precedente com Mach igual ou maior    | **10 minutos**              | [^7] [^8]   |
| Mesma rota e nível, técnica do número Mach, precedente mais veloz                 | **9 a 5 minutos**, ver tabela | [^7]      |
| Mesma rota e nível, técnica do número Mach, **seguinte** mais veloz               | **10 minutos + compensação** | [^9]       |
| Mesma rota e sentido, distância RNAV com leituras de um ponto comum               | **80 NM**                   | [^10] [^8]  |
| Mesma rota e nível, sem técnica do número Mach                                    | **15 minutos**              | [^11]       |
| Rotas que se cruzam, mesmo nível                                                  | **15 minutos** na interseção | [^12]      |
| Rotas opostas, sem separação lateral                                              | Vertical de **10 minutos antes até 10 depois** do cruzamento estimado | [^13] |
| Subindo ou descendo cruzando o nível de outra, mesma rota                         | **15 minutos**              | [^14]       |

A mínima de **10 minutos** substitui os 15 quando os auxílios permitem determinar continuamente posições e velocidades[^11] [^12] [^14].

## Separação vertical

| Faixa                                | Mínima                                                     |
| ------------------------------------ | ---------------------------------------------------------- |
| Abaixo do FL 290                     | 1.000 pés                                                  |
| Entre o FL 290 e o FL 410, inclusive | 2.000 pés, ou **1.000 pés onde se aplica RVSM**            |
| Acima do FL 410                      | 2.000 pés                                                  |

Todo o espaço entre o FL 290 e o FL 410 da FIR é RVSM[^2], então **1.000 pés é a regra na faixa de cruzeiro, desde que ambas sejam aprovadas RVSM**.

**Cruzamento de níveis.** Uma aeronave pode ser autorizada a nível previamente ocupado depois que a outra reportar tê-lo liberado, **exceto** com turbulência forte, subida de cruzeiro, ou diferença de desempenho que possa reduzir a mínima[^15].

## Separação lateral

A mínima publicada para o corredor EUR/SAM é **50 NM** entre aeronaves RNAV certificadas RNP 10[^5], e **100 NM** para quem não é certificado[^6]. É esse o valor a usar.

Para rotas que se cruzam, o ponto de separação lateral segue a especificação de navegação: RNAV 10 (RNP 10) 50 NM, RNP 4 23 NM, RNP 2 15 NM[^16].

!!! warning "As mínimas reduzidas exigem PBCS"
    A ICA 100-37 prevê 23 NM condicionada a `RCP 240`, `RSP 180` e contrato de evento ADS-C[^17]. **Enquanto a AIP não publicar essas mínimas para o corredor, aplique 50 NM.**

Ao receber informação de falha ou degradação de navegação, aplique outro tipo ou mínimo de separação; os mínimos baseados em distância RNAV deixam de valer[^18].

## Técnica do número Mach

Aeronaves a jato na mesma rota mantêm números Mach especificados para garantir espaçamento longitudinal[^19]. Exige que tenham reportado o **mesmo ponto comum** e sigam a mesma rota ou rotas continuamente divergentes[^20].

### Precedente mais veloz

| Diferença de Mach | Separação mínima |
| :---------------: | :--------------: |
| 0 ou 0,01         | 10 minutos       |
| 0,02              | 9 minutos        |
| 0,03              | 8 minutos        |
| 0,04              | 7 minutos        |
| 0,05              | 6 minutos        |
| 0,06 ou mais      | 5 minutos        |

!!! example "Exemplo"
    Precedente em Mach 0.83, seguinte em Mach 0.78. Diferença de 0,05 a favor da precedente: a mínima cai de 10 para **6 minutos**[^21].

### Seguinte mais veloz

O espaçamento no ponto de entrada precisa ser **aumentado**: some **1 minuto a cada 0,01 de diferença de Mach**, dentro de 600 NM entre os pontos de entrada e saída[^9].

| Rota ATS | Pontos            | Distância | Multiplicador |
| :------: | :---------------: | :-------: | :-----------: |
| UZ51     | `DAKAP` e `MOVGA` | 517 NM    | 1x            |
| UN741    | `JOBER` e `NANIK` | 493 NM    | 1x            |
| UN866    | `MAGNO` e `DEKON` | 475 NM    | 1x            |
| UN873    | `VUNOK` e `TASIL` | 449 NM    | 1x            |
| UN857    | `UTRAM` e `ERETU` | 431 NM    | 1x            |
| UL206    | `BUGAT` e `KODOS` | 340 NM    | 1x            |

!!! example "Exemplo"
    Na UZ51 via `DAKAP`, precedente em Mach 0.82 e seguinte em Mach 0.84. Diferença de 0,02, multiplicador 1x: some 2 minutos aos 10. Exigem-se **12 minutos** no ponto de entrada[^22].

Consultar o piloto sobre ajuste de velocidade é facultado, mas não deve ser rotina[^23].

## Perda de capacidade

| Perdeu                     | Efeito                                             | Ação                                          |
| -------------------------- | -------------------------------------------------- | --------------------------------------------- |
| Aprovação RVSM             | Vertical volta a 2.000 pés                          | Reposicionar níveis antes de infringir[^3]    |
| Precisão de navegação      | Laterais e distância RNAV deixam de valer           | Aplicar outro tipo ou mínimo[^18]             |
| ADS-C                      | Sem posição automática                              | Exigir reportes e restabelecer mínimos[^24]   |
| Número Mach atribuído      | A técnica deixa de sustentar a mínima reduzida      | Voltar a 10 ou 15 minutos                     |

**Separação de emergência.** Se durante uma emergência não for possível assegurar a separação horizontal, pode excepcionalmente ser usada **metade da mínima vertical**: 500 pés onde se aplicam 1.000, e 1.000 pés onde se aplicam 2.000[^25]. As tripulações precisam ser informadas de que ela está sendo aplicada, de qual é o valor, e receber informação de tráfego essencial[^26].

## Conflitos perto do limite da FIR

1. **Calcule a separação no ponto de transferência**, não onde a aeronave está.
2. **Coordene antes de agir**[^27].
3. **Resolva do seu lado**: ajuste nível, Mach ou horário antes da entrega.
4. Se o adjacente estiver offline, resolva integralmente dentro da sua jurisdição.

## SLOP

O deslocamento estratégico lateral **está em vigor na FIR Atlântico** e é prática padrão dos pilotos[^28]:

- deslocamento **somente à direita**, em três posições: eixo, 1 NM ou 2 NM;
- **nunca** além de 2 NM, **nunca** à esquerda;
- sem capacidade automática, voa-se no eixo;
- **não exige autorização ATC e não precisa ser avisado**;
- os reportes continuam baseados na autorização vigente, não no deslocamento.

!!! warning "O SLOP não aparece como desvio"
    Uma aeronave em SLOP reporta o mesmo fixo que reportaria no eixo. Até 2 NM não é erro de navegação e não deve ser questionado. O que exige atenção é o desvio lateral de **5 NM**, que dispara o contrato de evento ADS-C[^29].

## Desvios

### Aeronave incapaz de cumprir a autorização

Se não puder seguir a autorização, ou manter a precisão de navegação exigida, o ATC deve ser **imediatamente** informado[^30]. Ao receber:

1. **Identifique** o que ela não consegue cumprir.
2. **Confirme** a intenção concreta: que nível, que rumo, por quanto tempo.
3. **Proteja a separação** antes que a mínima anterior seja infringida.
4. **Coordene** com o adjacente afetado e **registre**.

### Desvio meteorológico

1. Receba a solicitação com lado e distância pretendida.
2. Avalie o tráfego na faixa lateral e nos níveis adjacentes.
3. **Autorize com limite explícito**: quantas milhas, por quanto tempo, com instrução de reportar o retorno.
4. **Reavalie a separação longitudinal**, porque o desvio muda os estimados.
5. Peça o estimado revisado e coordene com o adjacente.

Turbulência severa afetando a manutenção de nível gera `UNABLE RVSM DUE TURBULENCE`[^31] e leva a considerar a suspensão do RVSM na área[^4].

### Conflito entre desvio e tráfego

Nesta ordem: **nível** primeiro, que é a solução mais rápida e verificável; depois **ajuste de Mach**; depois **limitar a extensão lateral** autorizada; e informação de tráfego às duas aeronaves quando nada resolver por completo.

Exija reporte explícito do **retorno ao eixo** com estimado revisado. Até lá, mantenha a proteção estabelecida.

[^1]: **ICA 100-37, Art. 323**.
[^2]: **AIP-Brasil, ENR 2.2, item 1.1**.
[^3]: **AIP-Brasil, ENR 2.2, itens 1.3 e 1.6**.
[^4]: **AIP-Brasil, ENR 3.5, item 7.8.1**, e **ENR 2.2, item 1.12**.
[^5]: **AIP-Brasil, ENR 3.5, item 6.4.1.1**.
[^6]: **AIP-Brasil, ENR 3.5, item 6.2.2**.
[^7]: **ICA 100-37, Art. 378**, e **CIRCEA 100-66, Art. 6° e Tabela 1**.
[^8]: **AIP-Brasil, ENR 3.5, item 6.4.2.1**.
[^9]: **CIRCEA 100-66, Arts. 7° e 8°**.
[^10]: **ICA 100-37, Arts. 386 e 387**.
[^11]: **ICA 100-37, Art. 362**.
[^12]: **ICA 100-37, Art. 363**.
[^13]: **ICA 100-37, Art. 366**.
[^14]: **ICA 100-37, Arts. 364 e 365**.
[^15]: **ICA 100-37, Arts. 330 e 331**.
[^16]: **ICA 100-37, Art. 353, Tabela 4**.
[^17]: **ICA 100-37, Art. 350, Tabela 3**.
[^18]: **ICA 100-37, Arts. 337 e 382**.
[^19]: **CIRCEA 100-66, Art. 4°, inciso VI**.
[^20]: **ICA 100-37, Art. 377**.
[^21]: **CIRCEA 100-66, Quadro 1**.
[^22]: **CIRCEA 100-66, Quadro 3**.
[^23]: **CIRCEA 100-66, Art. 10**.
[^24]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.2**.
[^25]: **ICA 100-37, Art. 270**.
[^26]: **ICA 100-37, Art. 271**.
[^27]: **ICA 100-37, Art. 822**.
[^28]: **AIP-Brasil, ENR 3.5, itens 7.9.1 a 7.9.3.8**.
[^29]: **AIP-Brasil, ENR 3.5, item 9.5.2.3**.
[^30]: **AIP-Brasil, ENR 3.5, item 8.8.1**.
[^31]: **AIP-Brasil, ENR 2.2, item 1.13**.
