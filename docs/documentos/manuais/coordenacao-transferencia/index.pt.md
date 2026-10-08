---
title: Introdução
icon: material/swap-horizontal-bold
---

--8<-- "includes/abreviacoes.md"

![Manual de Coordenação e Transferência - Introdução](img/manual-coordenacao-intro.png)

#

## Apresentação

Nenhum controlador acompanha um voo do começo ao fim. A autorização sai do tráfego, o táxi é do solo, a decolagem é da torre, a subida é do controle, o cruzeiro é do centro, e a ordem se inverte na chegada. A cada fronteira, o voo muda de mãos, e o serviço precisa continuar como se não tivesse mudado. A coordenação é o que garante isso.

A ICA 100-37 define coordenação de tráfego aéreo como "a troca de informações com a finalidade de assegurar a continuidade da prestação dos serviços de tráfego aéreo"[^1]. A transferência é o momento em que essa troca se completa: a responsabilidade pelo controle, e depois a comunicação com o piloto, passam de um controlador para o outro.

Este manual é para quem vai controlar qualquer posição na Vatsim Brasil, do `DEL` ao `CTR`. Ele trata do que coordenar, quando, com quem e como transferir uma aeronave sem que ela fique, nem por um instante, sem alguém responsável por ela. Trata também do que é próprio da rede: a cobertura top-down, as posições vizinhas que abrem e fecham durante a sessão e as ferramentas do EuroScope.

| Revisão | Data       | Descrição         | Revisor |
| ------- | ---------- | ----------------- | ------- |
| 10/2026 | 08/10/2026 | Criação do Manual | —       |

## Sobre este Manual

A base normativa é a **ICA 100-37**[^2]: o Capítulo X (Coordenação) e a Subseção V da Seção XVII do Capítulo XI (transferência de controle com vigilância ATS). As mensagens de coordenação seguem o Anexo II do **MCA 100-16**[^3], e a fraseologia com o piloto, o Capítulo IV do mesmo manual. O que é próprio da rede segue a **Política Global de Administração de Controladores (GCAP)** da VATSIM[^4].

Quando a norma do mundo real e a prática da rede divergirem, o manual mostra as duas e diz qual vale na Vatsim Brasil. Trechos de técnica, que não são norma, aparecem marcados como boa prática.

## Escopo

Este manual cobre:

- o conceito de coordenação e as regras gerais que valem entre quaisquer órgãos ou posições;
- a transferência de controle e a transferência de comunicações, com e sem vigilância ATS;
- a coordenação entre cada par de órgãos: ACC e ACC, ACC e APP, APP e TWR, TWR e solo, e posições de um mesmo órgão;
- a coordenação de voos que entram ou saem do espaço aéreo controlado;
- a coordenação na rede: cobertura top-down, abertura e fechamento de posições, espaço aéreo sem controlador e ferramentas do EuroScope;
- as mensagens de coordenação e a fraseologia de transferência, em português e inglês.

## Fora do escopo

Não fazem parte deste manual:

- os pontos de transferência e os acordos específicos de cada órgão, que estão nos manuais operacionais e nas cartas de acordo operacional;
- a coordenação no espaço aéreo oceânico, que tem regras próprias no [MOP da FIR Atlântico](../../../MOP/oceanico/atc/coordenacao.pt.md);
- a coordenação com a meteorologia, a administração aeroportuária e as estações de telecomunicações;
- o gerenciamento de fluxo (CGNA) e as medidas de controle de fluxo.

!!! warning "Importante"
    Conteúdo destinado ao ambiente de simulação de voo. Em operações reais, utilize sempre as publicações oficiais vigentes, as cartas aeronáuticas e os canais AIS e ATS.

## Como usar este manual

1. Leia **Fundamentos da Coordenação** para fixar as regras que valem em qualquer fronteira.
2. Leia **Transferência de Controle** para saber como e quando uma aeronave muda de mãos.
3. Consulte **Coordenação entre Órgãos** para o que cada par de órgãos troca entre si.
4. Leia **Coordenação na Rede** antes da primeira sessão: é onde a VATSIM difere do mundo real.
5. Consulte a **Fraseologia** para as mensagens entre controladores e as instruções ao piloto.
6. Revise o **Checklist Rápido** antes de abrir uma posição.

!!! tip "Leitura complementar"
    Este manual pressupõe os órgãos e posições do [Manual de Espaço Aéreo e Serviços ATS](../espaco-aereo-servicos-ats/04-orgaos.pt.md). A transferência de aeronaves vetoradas e a passagem da final para a torre também aparecem no [Manual de Vetoração e Sequenciamento](../vetoracao-sequenciamento/index.pt.md). A cobertura top-down de cada TMA está na seção [Terminais](../../../MOP/terminais/index.pt.md).

[^1]: **ICA 100-37, Art. 814**.
[^2]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulamenta no Brasil os Serviços de Tráfego Aéreo previstos no Anexo 11 e no Doc 4444 da OACI. Edição em vigor em 27/11/2025.
[^3]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): estabelece os padrões de fraseologia de tráfego aéreo. Edição aprovada pela Portaria DECEA/DNOR1 n° 1.716, de 28/04/2025.
[^4]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), versão 2.0, de 15/08/2026: define as posições de controle da rede e o princípio top-down.
