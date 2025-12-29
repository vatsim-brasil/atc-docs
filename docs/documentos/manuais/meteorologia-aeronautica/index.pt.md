---
title: Introdução
icon: material/weather-cloudy
---

--8<-- "includes/abreviacoes.md"

![Manual de Meteorologia - Introdução](img/manual-fraseologia-intro.png)

#

## Apresentação

Este manual está consolidado de forma **operacional, informativo e completo**, com foco em **leitura e interpretação de METAR, SPECI, TAF e NOTAM** a partir de fontes oficiais do DECEA (principalmente **AISWEB** e **REDEMET**).

| Revisão | Data       | Descrição                      | Revisor             |
| ------- | ---------- | ------------------------------ | ------------------- |
| 12/2025 | 29/12/2025 | Adaptação ao Portal ATC        | 930847              |

!!! note "Objetivo operacional"
    Padronizar a interpretação de mensagens meteorológicas e avisos aeronáuticos, reduzindo ambiguidade, melhorando consciência situacional e suportando tomada de decisão (planejamento, alternados, mínimos, tendência e risco convectivo).

## Sobre este Manual

Este manual foi criado de acordo com os tópicos relacionados nos documentos oficiais do DECEA e ICAO que tratam sobre meteorologia aeronáutica, mensagens OPMET (METAR, SPECI, TAF) e NOTAM.

É importantíssimo a leitura constante dos documentos oficiais e a consulta às fontes primárias (AISWEB e REDEMET).

### Documentos de Referência

Este manual baseia-se nos seguintes documentos oficiais:

- **ICAO Annex 3 - Meteorological Service for International Air Navigation**: estabelece os padrões e práticas recomendadas para serviços meteorológicos aeronáuticos.
- **DECEA - Publicações Meteorológicas**: documentos oficiais do DECEA sobre meteorologia aeronáutica e mensagens OPMET.
- **AISWEB**: sistema oficial de informações aeronáuticas do DECEA para consulta de NOTAM e informações publicadas.
- **REDEMET**: rede de meteorologia do DECEA para consulta de mensagens OPMET (METAR, SPECI, TAF).

!!! tip "Dica"
    Consulte sempre as fontes oficiais (AISWEB e REDEMET) para informações atualizadas e precisas.

## Visão geral (fluxo operacional)

### Fontes e papéis (visão prática)

| Tipo | Conteúdo | Uso primário |
| :--- | :------- | :----------- |
| METAR | Observação de aeródromo (superfície) | Situação "agora" |
| SPECI | Observação especial (mudança significativa) | Atualização crítica entre METARs |
| TAF | Previsão terminal | Tendência por janela de validade |
| NOTAM | Avisos operacionais | Mudanças/alertas (pistas, auxílios, procedimentos, restrições etc.) |

#### Onde consultar (DECEA)

- **REDEMET**: mensagens OPMET (METAR/SPECI/TAF, entre outras).
- **AISWEB**: NOTAM e informações aeronáuticas publicadas.

### Rotina de briefing (padrão)

1. **NOTAM (AISWEB)**
   - Validade (B/C), escopo (A/Q), impacto em pista, auxílios, procedimentos.
2. **METAR/SPECI (REDEMET)**
   - Vento (inclui rajadas/variação), visibilidade/RVR, fenômenos, teto, QNH.
3. **TAF (REDEMET)**
   - Janela de operação: pior caso por grupos **TEMPO**, **PROB**, **BECMG**, **FM**.
4. **Decisão operacional**
   - Mínimos, alternados, combustível, janela de decolagem/chegada, risco convectivo.

!!! note "Regra de ouro"
    **METAR manda no "agora".**  
    **TAF manda na tendência**, mas sempre confronte com atualização recente (SPECI, radar/satélite, tendência local).

### Heurísticas rápidas (sem "achismo")

- Se **T/Td** próximos (diferença pequena), aumente atenção para **BR/FG** e queda de visibilidade.
- Se houver **TS** (trovoada), trate como risco operacional (CB/rajadas/cisalhamento).
- Se houver **BKN/OVC baixo**, pense em **teto** (impacta IFR, aproximação, alternado).
- Se houver **VRB**, **xxxVyyy**, **G** (rajadas), pense em componente de vento cruzado, aproximação instável e variação de pista em uso.

    !!! info "Notações de vento"
        - **VRB**: Vento variável (sem direção predominante, geralmente quando velocidade < 3 kt).
        - **xxxVyyy**: Variação de direção do vento. Exemplo: `180V240` significa que o vento varia entre 180° e 240°. Indica instabilidade na direção do vento.
        - **G**: Rajadas (gusts). Exemplo: `25015G25KT` significa vento de 250° a 15 kt com rajadas de até 25 kt. Indica variação súbita e significativa na velocidade do vento.

## Como usar este manual

- Comece por **Visão geral** (acima) para entender o fluxo operacional.
- Vá para **METAR e SPECI** para decodificação e exemplos.
- Em seguida **TAF** para leitura de previsão terminal e grupos de mudança.
- Use **NOTAM** para compreender estrutura, significados e impacto operacional.
- Use o **Checklist** para rotina de briefing.
- Consulte o **Glossário** para abreviaturas e termos técnicos.

## Escopo

Este manual refere-se à interpretação operacional de mensagens meteorológicas e avisos aeronáuticos para voos em condições normais. Para situações adversas, emergências ou casos específicos, consulte a regulamentação específica, AIP, cartas e instruções do operador.

!!! warning "Importante"
    Este manual não substitui regulamentos, AIP, cartas, RBAC/ICA/ICAO, nem instruções do operador. É um guia de apoio operacional.

---
