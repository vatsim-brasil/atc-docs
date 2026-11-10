---
title: Introdução
icon: material/helicopter
---

--8<-- "includes/abreviacoes.md"

# Introdução

## Apresentação

O helicóptero faz coisas que nenhum avião faz. Ele para no ar, decola de um pátio, pousa num heliponto no meio do aeródromo, voa devagar e baixo e segue corredores próprios por cima de rodovias e rios. Para o controlador, isso é ao mesmo tempo uma ajuda e uma armadilha. É uma ajuda porque o helicóptero se encaixa em brechas onde um avião não caberia. É uma armadilha porque o hábito de tratar tudo como avião leva a autorizações que não fazem sentido, ou a esquecer o sopro do rotor ao lado de um monomotor estacionado.

Este manual é para quem vai trabalhar com helicópteros na Vatsim Brasil, em cada rating:

- no **solo (GND, S1)**, que movimenta o helicóptero pela área de manobras;
- na **torre (TWR, S2)**, que autoriza pousos e decolagens, na pista e fora dela;
- no **controle de aproximação (APP, S3)**, que lida com os helicópteros nas Rotas Especiais de Helicópteros (REH), quando elas estão publicadas.

Ele trata do controle habitual: o helicóptero que chega, sai ou cruza um aeródromo controlado. No fim, comenta duas especialidades que aparecem na rede, as operações **offshore** e as de **segurança pública e aeromédicas**, com os limites que a VATSIM impõe a elas.

| Revisão | Data       | Descrição         | Revisor |
| ------- | ---------- | ----------------- | ------- |
| 11/2026 | 10/11/2026 | Criação do Manual | —       |

## Sobre este Manual

A base normativa é a **ICA 100-4**, Regras e Procedimentos Especiais de Tráfego Aéreo para Helicópteros[^1]. Ela traz as definições, as regras VFR do helicóptero, os procedimentos de aeródromo, as REH, a operação offshore e a fraseologia própria do helicóptero. A **ICA 100-37**[^2] completa com a esteira de turbulência, o sopro do rotor e as prioridades. O **MCA 100-16**[^3] dá a fraseologia geral; ele não tem uma seção de helicópteros, então as transmissões específicas vêm do Capítulo 7 da ICA 100-4.

O que é próprio da rede segue o **Código de Conduta**[^4], a **Política Global de Administração de Controladores (GCAP)**[^5] e a **Política de Operações Especiais**[^6] da VATSIM.

Quando a norma do mundo real e a prática da rede divergirem, o manual mostra as duas e diz qual vale na Vatsim Brasil. Trechos de técnica, que não são norma, aparecem marcados como boa prática.

## Escopo

Este manual cobre:

- o que muda no helicóptero para quem controla: pairado, táxi no solo, taxiamento aéreo, deslocamento aéreo, helipontos e áreas de pouso eventual;
- as regras VFR próprias do helicóptero, que são mais flexíveis que as do avião;
- o trabalho do GND e da TWR com helicópteros num aeródromo controlado;
- as REH e o que o APP faz com os helicópteros nelas, em termos gerais;
- as operações offshore e as de segurança pública e aeromédicas, e o que a VATSIM permite;
- a fraseologia, em português e inglês.

## Fora do escopo

Não fazem parte deste manual:

- as REH de cada terminal, com seus pontos, altitudes e frequências: estão nas páginas das [terminais](../../../MOP/terminais/index.pt.md) e nas AIC de cada região;
- a pilotagem do helicóptero e a homologação de helipontos, que são assunto da ANAC;
- a separação em geral, tratada no [Manual de Separação e Esteira de Turbulência](../separacao-esteira/index.md);
- o voo IFR de helicóptero em detalhe: para o controlador, ele é quase sempre um IFR comum de categoria A.

!!! warning "Importante"
    Conteúdo destinado ao ambiente de simulação de voo. Em operações reais, utilize sempre as publicações oficiais vigentes, as cartas aeronáuticas e os canais AIS e ATS.

## Como usar este manual

1. Leia **Fundamentos** para conhecer o vocabulário e o que o helicóptero pode fazer. Vale para todos os ratings.
2. Se você é **S1**, leia **Controle de Solo**.
3. Se você é **S2**, leia também **Torre de Controle**.
4. Se você é **S3**, leia também **APP e as REH**.
5. Todos devem ler **Operações Especiais** antes de atender um voo offshore, policial ou aeromédico.
6. Consulte a **Fraseologia** e revise o **Checklist Rápido** do seu rating antes de abrir a posição.

!!! tip "Leitura complementar"
    A esteira de turbulência e as categorias de peso estão no [Manual de Separação e Esteira de Turbulência](../separacao-esteira/04-esteira.pt.md). As REH de cada terminal estão nas páginas das [terminais](../../../MOP/terminais/index.pt.md), na camada de mapa REH e na caixa "Documentos de navegação visual".

[^1]: [**ICA 100-4, Regras e Procedimentos Especiais de Tráfego Aéreo para Helicópteros**](https://publicacoes.decea.mil.br/publicacao/ica-100-4): Portaria DECEA nº 109/DGCEA, de 21/07/2021, em vigor desde 02/08/2021.
[^2]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulamenta no Brasil os Serviços de Tráfego Aéreo previstos no Anexo 11 e no Doc 4444 da OACI. Edição com a 2ª alteração (Portaria DECEA/DNOR1 nº 2.197, de 18/08/2026), em vigor em 26/11/2026.
[^3]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): estabelece os padrões de fraseologia de tráfego aéreo. Edição com a alteração da Portaria DECEA/DNOR1 nº 2.193, de 11/08/2026, em vigor em 26/11/2026.
[^4]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct): regras de conduta de pilotos e controladores na rede. Revisão 2026.2.
[^5]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), versão 2.0, de 15/08/2026: define as posições de controle da rede, os ratings exigidos e o princípio top-down.
[^6]: [**VATSIM, Special Operations Policy**](https://cdn.vatsim.net/policy-documents/VATSIM-POL-Special_Operations_v5.0.pdf), versão 5.0, de 14/05/2026: define as operações militares, paramilitares e de agências governamentais e quem pode conduzi-las.
