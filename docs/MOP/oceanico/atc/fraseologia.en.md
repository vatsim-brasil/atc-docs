---
title: Phraseology and Messages
icon: material/microphone
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Quick reference. Phraseology is given primarily in English, which is the normal practice in international oceanic operations. The unit works in both languages[^1]; use Portuguese if the aircraft starts in Portuguese.

!!! warning "Templates, not rules"
    Constructions without an indicated official source are usage templates. Where a published form exists, it takes precedence.

## Variables

`CALLSIGN` · `POSITION` · `TIME` · `LEVEL` · `MACH` · `NEXT POSITION` · `ESTIMATE` · `ENSUING POSITION` · `UNIT` · `FREQ`

Unit callsign: **CENTRO ATLÂNTICO** and **ATLANTICO CENTER**[^1]. Mach number 0.86 is transmitted as `MACH ZERO PONTO OITO MEIA` and `MACH ZERO POINT EIGHT SIX`[^2].

## Voice

| Situation                       | Template                                                                                              |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Pilot's initial call            | `ATLANTICO CENTER, CALLSIGN, POSITION at TIME, LEVEL, MACH`                                          |
| Reply                           | `CALLSIGN, ATLANTICO CENTER, roger. Maintain LEVEL and MACH. Report POSITION.`                        |
| Confirm datalink                | `CALLSIGN, confirm CPDLC logon to SBAO.`                                                              |
| No datalink available           | `CALLSIGN, no datalink available. Position reports required.`                                         |
| **Position report**             | `CALLSIGN, POSITION at TIME, LEVEL, MACH, estimating NEXT POSITION at ESTIMATE, next ENSUING POSITION` |
| Request a report                | `CALLSIGN, report position.`                                                                          |
| Complete a report               | `CALLSIGN, report time over POSITION, present Mach number, next position with estimate and ensuing position.` |
| Revised estimate                | `CALLSIGN, revised estimate NEXT POSITION at ESTIMATE.`                                               |
| Next reporting point            | `CALLSIGN, next report at NEXT POSITION.`                                                             |
| Level clearance                 | `CALLSIGN, cleared LEVEL.`                                                                            |
| Mach maintenance                | `CALLSIGN, maintain MACH.`                                                                            |
| Level unavailable               | `CALLSIGN, unable LEVEL due traffic. Expect LEVEL at POSITION.`                                        |
| Transfer                        | `CALLSIGN, contact UNIT on FREQ.`                                                                     |
| No unit ahead                   | `CALLSIGN, no ATC available ahead. Report leaving the FIR.`                                            |

## RVSM

Official published form, in Portuguese and English[^3].

| Situation                                   | Portuguese                             | English                            |
| ------------------------------------------- | -------------------------------------- | ---------------------------------- |
| Controller confirms approval status         | `CALLSIGN` CONFIRME APROVAÇÃO RVSM     | `CALLSIGN` CONFIRM RVSM APPROVED   |
| Pilot confirms                              | `CALLSIGN` AFIRMATIVO RVSM             | `CALLSIGN` AFFIRMATIVE RVSM        |
| Pilot reports not approved                  | `CALLSIGN` NEGATIVO RVSM               | `CALLSIGN` NEGATIVE RVSM           |
| Turbulence prevents maintaining the level   | `CALLSIGN` NEGATIVO RVSM DEVIDO TURBULÊNCIA | `CALLSIGN` UNABLE RVSM DUE TURBULENCE |
| Degraded equipment                          | `CALLSIGN` NEGATIVO RVSM DEVIDO EQUIPAMENTO | `CALLSIGN` UNABLE RVSM DUE EQUIPMENT |
| Pilot can resume                            | `CALLSIGN` PRONTO PARA REASSUMIR RVSM  | `CALLSIGN` READY TO RESUME RVSM    |
| Controller requests that notice             | `CALLSIGN` INFORME PRONTO PARA REASSUMIR RVSM | `CALLSIGN` REPORT ABLE TO RESUME RVSM |

## CPDLC { #cpdlc }

Do not freely translate standardized elements: Brazil adopts the message set of ICAO Doc 10037 (GOLD)[^4]. Use free text only when no appropriate standardized message exists[^5].

Official published form[^6]:

| Situation                           | Portuguese                                                               | English                                                             |
| ----------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Connection failure                  | Falha na CPDLC. Desconecte CPDLC e faça conexão com `UNIT`.             | CPDLC failure. Disconnect CPDLC then logon to `UNIT`.               |
| Datalink failure, continue on voice | Falha na CPDLC. Continue por voz.                                        | CPDLC failure. Continuing on voice.                                 |
| Ground system failure               | Todas as aeronaves, falha na CPDLC. Desconecte CPDLC. Continue por voz.  | All stations CPDLC failure. Disconnect CPDLC. Continue on voice.    |
| Restoration                         | Todas aeronaves reassumam a operação CPDLC normal. Faça conexão com `UNIT`. | All stations resume normal CPDLC operations. Logon to `UNIT`.    |
| Automatic transfer failed           | Falha de transferência automática CPDLC. Ao entrar na área do `UNIT` desconecte CPDLC e faça conexão com `UNIT`. | Automatic transfer of CPDLC failed. When entering `UNIT` area disconnect CPDLC then logon to `UNIT`. |
| Message correction                  | Desconsidere mensagem (tipo) CPDLC, break (autorização corrigida).       | Disregard CPDLC (type) message, break (corrected clearance).        |
| Suspend requests                    | `CALLSIGN` pare o envio de solicitações CPDLC até que seja informado.    | `CALLSIGN` stop sending CPDLC requests until advised.               |

If a message goes unanswered after a reasonable period, the prescribed structure is `WHEN CAN WE EXPECT (request already sent)`[^7].

## Coordination

| Situation             | Template                                                                                     |
| --------------------- | -------------------------------------------------------------------------------------------- |
| Handoff estimate      | `CALLSIGN, POSITION at ESTIMATE, LEVEL, MACH, route ROUTE, RVSM, RNP 10, ADS-C and CPDLC active, SELCAL ABCD` |
| Acceptance            | `CALLSIGN accepted at LEVEL.`                                                                |
| Renegotiation         | `CALLSIGN unable LEVEL due traffic. Available LEVEL or estimate TIME.`                        |
| Revised estimate      | `CALLSIGN revised estimate POSITION at ESTIMATE.`                                             |
| Deviation             | `CALLSIGN deviating right of track due weather, up to 30 miles, revised estimate POSITION at ESTIMATE.` |
| Conflicting traffic   | `Traffic CALLSIGN and CALLSIGN, same route, LEVEL, estimated POSITION at ESTIMATE and ESTIMATE.` |
| Communication failure | `CALLSIGN last contact TIME, last confirmed position POSITION, LEVEL, MACH, no contact since.` |

## What to avoid

| Avoid                                                        | Why                                                      |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| Treating the ADS-C display as radar contact                  | There is no radar surveillance, and it misleads the pilot |
| Heading instructions as vectoring                            | CPDLC is not used for vectoring[^8]                      |
| Translating standardized CPDLC elements                      | The message set is standardized[^4]                      |
| Using the published HF frequency as if it were tunable       | It is an aeronautical reference, not a network voice channel |
| SELCAL check on first contact with an aircraft on CPDLC      | It should not be done at that point unless requested[^9] |

[^1]: **AIP-Brasil, ENR 2.1**, and **MCA 100-16, Art. 37**.
[^2]: **MCA 100-16, Art. 27 and Table 6**.
[^3]: **AIP-Brasil, ENR 2.2, item 1.13**.
[^4]: **AIP-Brasil, ENR 3.5, item 9.1.1**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.4.1.2**.
[^6]: **MCA 100-16, Arts. 197 to 205**.
[^7]: **AIP-Brasil, ENR 3.5, item 9.4.1.11**.
[^8]: **AIP-Brasil, ENR 3.5, item 9.1.6**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.5.1.2**.
