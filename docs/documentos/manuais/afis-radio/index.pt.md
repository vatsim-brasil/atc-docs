---
title: Introdução
icon: material/radio-tower
---

--8<-- "includes/abreviacoes.md"

# Introdução

## Apresentação

Boa parte dos aeródromos brasileiros não tem torre de controle. Nesses aeródromos, quem fala com o piloto é a **RÁDIO**: o órgão que presta o Serviço de Informação de Voo de Aeródromo, o AFIS. A RÁDIO não autoriza pouso, não autoriza decolagem e não separa tráfego. Ela informa o vento, o ajuste de altímetro, as condições do aeródromo e o tráfego conhecido, recebe as intenções e os reportes do piloto e aciona o Serviço de Alerta quando algo dá errado. Quem decide é o piloto.

É a posição mais fácil de abrir e uma das mais fáceis de fazer errado. Quem vem da torre tende a "autorizar" por hábito. Quem vem do APP tende a vetorar. Na RÁDIO, nenhuma das duas coisas existe. O que existe é informação boa, na hora certa, e a palavra **ciente**.

Este manual é para quem vai abrir uma posição RÁDIO (`_R_TWR`) na Vatsim Brasil e para quem, no APP ou no centro, cobre um aeródromo com AFIS por top-down. Ele trata do que o AFIS presta e do que não presta, de como conduzir chegadas e saídas VFR e IFR na frequência, e do que é próprio da rede.

| Revisão | Data       | Descrição         | Revisor |
| ------- | ---------- | ----------------- | ------- |
| 11/2026 | 05/11/2026 | Criação do Manual | —       |

## Sobre este Manual

A base normativa é a **ICA 100-37**[^1]: a Seção V do Capítulo VIII (Serviço de Informação de Voo de Aeródromo – AFIS, Arts. 782 a 791), as Seções XX e XXI do Capítulo III (descida por instrumentos em aeródromo provido de AFIS e operação em aeródromo não controlado, Arts. 140 a 164) e o Capítulo IX (Serviço de Alerta). A fraseologia segue a Seção VI do **MCA 100-16**[^2], dedicada ao AFIS (Arts. 153 a 158). As zonas de informação de voo vêm da **AIP-Brasil, ENR 2.2**[^3]. O que é próprio da rede segue a **Política Global de Administração de Controladores (GCAP)**[^4] e o **Código de Conduta**[^5] da VATSIM.

Quando a norma do mundo real e a prática da rede divergirem, o manual mostra as duas e diz qual vale na Vatsim Brasil. Trechos de técnica, que não são norma, aparecem marcados como boa prática.

## Escopo

Este manual cobre:

- o que é o AFIS, quem o presta, onde (FIZ e imediações do aeródromo) e o que ele presta e não presta;
- a informação de voo e de tráfego na frequência, e a retransmissão de autorizações de outros órgãos;
- a chegada e a saída de voos VFR e IFR em aeródromo com AFIS;
- o Serviço de Alerta no aeródromo;
- a posição RÁDIO na rede: sufixo, rating, cobertura top-down, frequência de tráfego sem controlador e coordenação com o APP e o centro;
- a fraseologia do AFIS, em português e inglês.

## Fora do escopo

Não fazem parte deste manual:

- o controle de aeródromo, que é da torre: autorizações de pouso, decolagem e táxi, e a separação na pista;
- o circuito de tráfego em detalhe, que está no [Manual de Circuito de Tráfego](../manual-circuito-trafego/index.md);
- o Serviço de Informação de Voo em rota, prestado pelo centro, que aparece no [Manual de Espaço Aéreo e Serviços ATS](../espaco-aereo-servicos-ats/03-servicos.pt.md);
- as estações de telecomunicações aeronáuticas e a sala AIS de aeródromo;
- os horários de funcionamento do AFIS no mundo real.

!!! warning "Importante"
    Conteúdo destinado ao ambiente de simulação de voo. Em operações reais, utilize sempre as publicações oficiais vigentes, as cartas aeronáuticas e os canais AIS e ATS.

## Como usar este manual

1. Leia **Fundamentos do AFIS** para saber o que a RÁDIO presta e, principalmente, o que ela não presta.
2. Leia **Operação na Frequência** para conduzir chegadas e saídas, VFR e IFR.
3. Leia **AFIS na Rede** antes da primeira sessão: é onde a VATSIM difere do mundo real.
4. Consulte a **Fraseologia** para as transmissões em português e inglês.
5. Revise o **Checklist Rápido** antes de abrir a posição.

!!! tip "Leitura complementar"
    A fronteira entre informar e controlar está no [Manual de Espaço Aéreo e Serviços ATS](../espaco-aereo-servicos-ats/03-servicos.pt.md#o-que-informar-nao-e-controlar). O ponto de vista do piloto, num voo completo até um aeródromo com RÁDIO, está no [Manual de Fraseologia para Voo Visual](../fraseologia-voo-visual/voo-ida.pt.md). A frequência e o indicativo de cada RÁDIO estão nas páginas dos [aeródromos](../../../MOP/aerodromos/index.pt.md).

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulamenta no Brasil os Serviços de Tráfego Aéreo previstos no Anexo 11 e no Doc 4444 da OACI. Edição em vigor em 27/11/2025.
[^2]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): estabelece os padrões de fraseologia de tráfego aéreo. Edição aprovada pela Portaria DECEA/DNOR1 n° 1.716, de 28/04/2025.
[^3]: [**AIP-Brasil, ENR 2.2, Outros espaços aéreos regulamentados**](https://aisweb.decea.mil.br/?i=publicacoes&p=aip): traz as FIZ com limites, classe, órgão, indicativo de chamada e frequência. Emenda de 01/10/2026.
[^4]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), versão 2.0, de 15/08/2026: define as posições de controle da rede, os ratings exigidos e o princípio top-down.
[^5]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct): regras de conduta de pilotos e controladores na rede.
