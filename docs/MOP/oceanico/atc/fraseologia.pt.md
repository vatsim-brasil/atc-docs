---
title: Fraseologia e Mensagens
icon: material/microphone
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Consulta rápida. Explicações em português, fraseologia prioritariamente em inglês, que é a aplicação normal em operação oceânica internacional. O órgão atende nos dois idiomas[^1]; use português se a aeronave começar em português.

!!! warning "Modelos, não regras"
    As construções sem fonte oficial indicada são modelos de uso. Onde houver forma publicada, ela prevalece.

## Variáveis

`CALLSIGN` · `POSITION` · `TIME` · `LEVEL` · `MACH` · `NEXT POSITION` · `ESTIMATE` · `ENSUING POSITION` · `UNIT` · `FREQ`

Indicativo do órgão: **CENTRO ATLÂNTICO** e **ATLANTICO CENTER**[^1]. Número Mach 0.86 se transmite `MACH ZERO PONTO OITO MEIA` e `MACH ZERO POINT EIGHT SIX`[^2].

## Voz

| Situação                        | Modelo                                                                                              |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Chamada inicial do piloto       | `ATLANTICO CENTER, CALLSIGN, POSITION at TIME, LEVEL, MACH`                                          |
| Resposta                        | `CALLSIGN, ATLANTICO CENTER, roger. Maintain LEVEL and MACH. Report POSITION.`                        |
| Confirmar enlace                | `CALLSIGN, confirm CPDLC logon to SBAO.`                                                              |
| Sem enlace disponível           | `CALLSIGN, no datalink available. Position reports required.`                                         |
| **Reporte de posição**          | `CALLSIGN, POSITION at TIME, LEVEL, MACH, estimating NEXT POSITION at ESTIMATE, next ENSUING POSITION` |
| Solicitar reporte               | `CALLSIGN, report position.`                                                                          |
| Completar reporte               | `CALLSIGN, report time over POSITION, present Mach number, next position with estimate and ensuing position.` |
| Revisão de estimado             | `CALLSIGN, revised estimate NEXT POSITION at ESTIMATE.`                                               |
| Próximo ponto de reporte        | `CALLSIGN, next report at NEXT POSITION.`                                                             |
| Autorização de nível            | `CALLSIGN, cleared LEVEL.`                                                                            |
| Manutenção de Mach              | `CALLSIGN, maintain MACH.`                                                                            |
| Nível indisponível              | `CALLSIGN, unable LEVEL due traffic. Expect LEVEL at POSITION.`                                        |
| Transferência                   | `CALLSIGN, contact UNIT on FREQ.`                                                                     |
| Sem órgão à frente              | `CALLSIGN, no ATC available ahead. Report leaving the FIR.`                                            |

## RVSM

Forma oficial publicada, em português e inglês[^3].

| Situação                                    | Português                              | Inglês                             |
| ------------------------------------------- | -------------------------------------- | ---------------------------------- |
| Controlador confirma o estado de aprovação  | `CALLSIGN` CONFIRME APROVAÇÃO RVSM     | `CALLSIGN` CONFIRM RVSM APPROVED   |
| Piloto confirma                             | `CALLSIGN` AFIRMATIVO RVSM             | `CALLSIGN` AFFIRMATIVE RVSM        |
| Piloto reporta não aprovado                 | `CALLSIGN` NEGATIVO RVSM               | `CALLSIGN` NEGATIVE RVSM           |
| Turbulência impede manter o nível           | `CALLSIGN` NEGATIVO RVSM DEVIDO TURBULÊNCIA | `CALLSIGN` UNABLE RVSM DUE TURBULENCE |
| Equipamento degradado                       | `CALLSIGN` NEGATIVO RVSM DEVIDO EQUIPAMENTO | `CALLSIGN` UNABLE RVSM DUE EQUIPMENT |
| Piloto pode reassumir                       | `CALLSIGN` PRONTO PARA REASSUMIR RVSM  | `CALLSIGN` READY TO RESUME RVSM    |
| Controlador pede esse aviso                 | `CALLSIGN` INFORME PRONTO PARA REASSUMIR RVSM | `CALLSIGN` REPORT ABLE TO RESUME RVSM |

## CPDLC

Não traduza livremente elementos padronizados: o Brasil adota o conjunto de mensagens do Doc 10037 (GOLD) da OACI[^4]. Texto livre só quando não houver mensagem padronizada apropriada[^5].

Forma oficial publicada[^6]:

| Situação                            | Português                                                              | Inglês                                                            |
| ----------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Falha de conexão                    | Falha na CPDLC. Desconecte CPDLC e faça conexão com `UNIT`.             | CPDLC failure. Disconnect CPDLC then logon to `UNIT`.               |
| Falha do enlace, seguir por voz     | Falha na CPDLC. Continue por voz.                                        | CPDLC failure. Continuing on voice.                                 |
| Falha do sistema de solo            | Todas as aeronaves, falha na CPDLC. Desconecte CPDLC. Continue por voz.  | All stations CPDLC failure. Disconnect CPDLC. Continue on voice.    |
| Restabelecimento                    | Todas aeronaves reassumam a operação CPDLC normal. Faça conexão com `UNIT`. | All stations resume normal CPDLC operations. Logon to `UNIT`.    |
| Transferência automática falhou     | Falha de transferência automática CPDLC. Ao entrar na área do `UNIT` desconecte CPDLC e faça conexão com `UNIT`. | Automatic transfer of CPDLC failed. When entering `UNIT` area disconnect CPDLC then logon to `UNIT`. |
| Correção de mensagem                | Desconsidere mensagem (tipo) CPDLC, break (autorização corrigida).       | Disregard CPDLC (tipo) message, break (autorização corrigida).      |
| Suspender solicitações              | `CALLSIGN` pare o envio de solicitações CPDLC até que seja informado.    | `CALLSIGN` stop sending CPDLC requests until advised.               |

Sem resposta a uma mensagem após período razoável, a estrutura prevista é `WHEN CAN WE EXPECT (solicitação já enviada)`[^7].

## Coordenação

| Situação              | Modelo                                                                                     |
| --------------------- | -------------------------------------------------------------------------------------------- |
| Estimado de entrega   | `CALLSIGN, POSITION at ESTIMATE, LEVEL, MACH, route ROUTE, RVSM, RNP 10, ADS-C and CPDLC active, SELCAL ABCD` |
| Aceitação             | `CALLSIGN accepted at LEVEL.`                                                                |
| Renegociação          | `CALLSIGN unable LEVEL due traffic. Available LEVEL or estimate TIME.`                        |
| Estimado revisado     | `CALLSIGN revised estimate POSITION at ESTIMATE.`                                             |
| Desvio                | `CALLSIGN deviating right of track due weather, up to 30 miles, revised estimate POSITION at ESTIMATE.` |
| Tráfego conflitante   | `Traffic CALLSIGN and CALLSIGN, same route, LEVEL, estimated POSITION at ESTIMATE and ESTIMATE.` |
| Falha de comunicação  | `CALLSIGN last contact TIME, last confirmed position POSITION, LEVEL, MACH, no contact since.` |

## O que evitar

| Evite                                                       | Por quê                                                 |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| Tratar a apresentação ADS-C como contato radar               | Não há vigilância radar, e induz o piloto a erro         |
| Instrução de proa como vetoração                             | A CPDLC não é usada para vetorações[^8]                  |
| Traduzir elementos padronizados de CPDLC                     | O conjunto de mensagens é padronizado[^4]                |
| Usar a frequência HF publicada como se fosse sintonizável    | É referência aeronáutica, não canal de voz da rede       |
| Cheque de SELCAL no primeiro contato de aeronave em CPDLC    | Não deve ser feito nesse momento, salvo solicitação[^9]  |

[^1]: **AIP-Brasil, ENR 2.1**, e **MCA 100-16, Art. 37**.
[^2]: **MCA 100-16, Art. 27 e Tabela 6**.
[^3]: **AIP-Brasil, ENR 2.2, item 1.13**.
[^4]: **AIP-Brasil, ENR 3.5, item 9.1.1**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.4.1.2**.
[^6]: **MCA 100-16, Arts. 197 a 205**.
[^7]: **AIP-Brasil, ENR 3.5, item 9.4.1.11**.
[^8]: **AIP-Brasil, ENR 3.5, item 9.1.6**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.5.1.2**.
