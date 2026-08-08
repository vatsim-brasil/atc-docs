---
title: Checklist Rápido
icon: material/checkbox-marked-circle-outline
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Checklist](img/manual-espaco-aereo-checklist.png)

#

## Antes de conectar

- [ ] Sei em qual FIR, TMA, CTR ou ATZ minha posição opera
- [ ] Sei qual a classe do espaço aéreo sob minha responsabilidade
- [ ] Sei quem está online acima e abaixo de mim
- [ ] Confirmei a **altitude de transição** do aeródromo na carta (IAC ou SID) — é a referência da **subida**
- [ ] Determinei o **nível de transição** com o QNH do momento — é a referência da **descida**
- [ ] Li as instruções locais na seção Manuais Operacionais

## Estou nesta classe — o que devo?

Tabela derivada da matriz de classes do Art. 21 da ICA 100-37 e do Anexo II, já reproduzidas no [capítulo de Classes de Espaço Aéreo](02-classes.pt.md#tabela-consolidada-anexo-ii-da-ica-100-37).

| Classe | Voos permitidos | Exijo autorização ATC | Exijo radiocomunicação | Quem separo | O que informo |
| --- | --- | --- | --- | --- | --- |
| **A** | Somente IFR | Sim | Bilateral contínua | Todos os voos entre si | Não se aplica — a separação já cobre todo o tráfego |
| **B** | IFR e VFR | Sim, do IFR e do VFR | Bilateral contínua, do IFR e do VFR | Todos os voos entre si — IFR de IFR, IFR de VFR e VFR de VFR | Não se aplica — a separação já cobre todo o tráfego |
| **C** | IFR e VFR | Sim, do IFR e do VFR | Bilateral contínua, do IFR e do VFR | IFR de IFR e de VFR — não separo VFR de VFR | O VFR recebe informação de tráfego sobre outros VFR, e aviso para evitar tráfego se solicitado pelo piloto |
| **D** | IFR e VFR | Sim, do IFR e do VFR | Bilateral contínua, do IFR e do VFR | Apenas IFR de IFR — o VFR não é separado de nada | Todos recebem informação de tráfego sobre os demais voos, e aviso para evitar tráfego se solicitado pelo piloto |
| **E** | IFR e VFR | Sim do IFR; **não** do VFR | Bilateral contínua do IFR; **não** exigida do VFR | Apenas IFR de IFR — o VFR não é separado | Todos recebem informação de tráfego quando possível; o VFR recebe também o Serviço de Informação de Voo |
| **F** | IFR e VFR | Não, de nenhum dos dois | Bilateral contínua do IFR; **não** exigida do VFR | IFR de IFR, quando possível — é assessoramento, não separação plena | Serviço de Informação de Voo a todos os voos, quando solicitado pelo piloto* |
| **G** | IFR e VFR | Não, de nenhum dos dois | Bilateral contínua do IFR; **não** exigida do VFR | Não aplicável — nenhuma separação | Serviço de Informação de Voo, quando possível e solicitado pelo piloto |

As colunas "Exijo autorização ATC" e "Exijo radiocomunicação" reproduzem as duas últimas colunas do Anexo II da ICA 100-37, condensando as linhas IFR e VFR de cada classe em uma só. Onde as duas linhas divergem — Classes E, F e G —, a divergência está explicitada na célula. Ver as notas de leitura do [capítulo de Classes de Espaço Aéreo](02-classes.pt.md#tabela-consolidada-anexo-ii-da-ica-100-37), em especial a que trata da linha **D / VFR**.

\* Na Classe F vale para os dois tipos de voo: o Art. 21, VI, *c*, da ICA 100-37 enuncia o Serviço de Informação de Voo para **todos** os voos da classe, "quando solicitado pelo piloto". O Anexo II da mesma Instrução registra essa condição só na linha do VFR e a omite na linha do IFR; é divergência de redação, resolvida pelo Art. 21. Ver [capítulo de Classes de Espaço Aéreo, seção Classe F](02-classes.pt.md#classe-f).

## Mínimos VMC de bolso

Versão condensada da Tabela 1 do Art. 104 da ICA 100-12, reproduzida no [capítulo de Regras de Voo e Níveis](05-regras.pt.md#minimos-vmc).

| Altitude | Classes | Visibilidade em voo | Distância de nuvens |
| --- | --- | --- | --- |
| 3.050 m (10.000 pés) AMSL ou acima | B, C, D, E, F, G | 8 km | 1.500 m horizontal / 300 m (1.000 pés) vertical |
| Abaixo de 3.050 m (10.000 pés) e acima de 900 m (3.000 pés) AMSL, ou acima de 300 m (1.000 pés) sobre o terreno — o que for maior | B, C, D, E, F, G | 5 km | 1.500 m horizontal / 300 m (1.000 pés) vertical |
| A 900 m (3.000 pés) AMSL ou abaixo, ou 300 m (1.000 pés) sobre o terreno — o que for maior | B, C, D, E | 5 km | 1.500 m horizontal / 300 m (1.000 pés) vertical |
| Mesma faixa acima | F, G | 5 km | Livre de nuvens e avistando o solo |

A Classe A não aparece nesta tabela: só admite voo IFR, logo não há mínimo VMC a cumprir ali. Quando a altitude de transição do aeródromo for inferior a 3.050 m (10.000 pés) AMSL, use o FL 100 em lugar de 10.000 pés como referência da primeira faixa.

## Qual órgão faz o quê

Versão condensada da tabela de correspondência do [capítulo de Órgãos ATS e Posições](04-orgaos.pt.md#tabela-de-correspondencia).

| Órgão ATS | Posição interna | Posição VATSIM | Espaço aéreo típico |
| --- | --- | --- | --- |
| Centro de Controle de Área (ACC) | — | `_CTR` | CTA, UTA e demais porções da FIR |
| Controle de Aproximação (APP) | — | `_APP` | TMA e CTR* |
| Torre de Controle de Aeródromo (TWR) | Torre de Controle | `_TWR` | ATZ e CTR* |
| Torre de Controle de Aeródromo (TWR) | Controle de Solo | `_GND` | Área de manobras |
| Torre de Controle de Aeródromo (TWR) | Autorização de Tráfego | `_DEL` | Pátio |
| Órgão ATS identificado como "RÁDIO" (AFIS) | — | `_R_TWR` | FIZ, ou Classe G nas imediações do aeródromo |

\* A CTR aparece nas duas linhas porque a jurisdição sobre ela **varia por localidade**: em um aeródromo é do APP, em outro da TWR, conforme a delegação prevista no Art. 34 da ICA 100-37. Em cada CTR concreta ela é de um só dos dois, como manda o Art. 37 da mesma Instrução. Qual dos dois, naquele aeródromo, está na AIP-Brasil e na seção **Manuais Operacionais**.

As linhas 3 a 5 são posições internas de um único órgão — a TWR —, não três órgãos diferentes. A posição RÁDIO **não presta controle**: presta Serviço de Informação de Voo e Serviço de Alerta, e ali não se emitem autorizações de controle. Ver o capítulo de Órgãos ATS e Posições para o detalhamento da jurisdição de cada uma.

## Onde buscar o dado local

!!! tip "Na rede (Vatbrz)"
    Este checklist não substitui a carta. Limites laterais e verticais, altitude de transição e classe aplicada mudam por aeródromo e por ciclo AIRAC. A fonte é sempre a AIP, a carta e a seção **Manuais Operacionais** do portal.
