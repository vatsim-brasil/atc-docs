---
title: Comunicações e Vigilância
icon: material/satellite-uplink
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Aqui comunicação e vigilância são o mesmo assunto: você sabe onde a aeronave está porque ela informou, pelo mesmo meio que você usa para responder. **Perder o meio de comunicação é perder a vigilância.**

## Hierarquia dos meios

| Ordem | Meio   | Função                                                   |
| ----- | ------ | -------------------------------------------------------- |
| 1     | ADS-C  | Posição automática e conformidade de rota                |
| 2     | CPDLC  | Autorizações, instruções e reportes por texto            |
| 3     | Voz    | Meio secundário, e primário para quem não tem enlace     |
| 4     | SELCAL | Chamada seletiva para recuperar aeronave silenciosa      |

ADS-C e CPDLC são o **meio primário** do ACC Atlântico, com HF como secundário[^1].

## ADS-C

!!! danger "ADS-C não é radar"
    O dado é **dependente** e **automático**: vem da própria aeronave, com a precisão do sistema dela, em intervalos discretos. Não há eco independente, não há atualização contínua, não há vetoração. Tratar como tela radar leva a decisões de separação que a fonte do dado não sustenta.

Contratos estabelecidos na FIR Atlântico[^2]:

| Tipo          | Gatilho                                                  |
| ------------- | -------------------------------------------------------- |
| **Periódico** | A cada 15 minutos                                        |
| **Por evento** | Pontos de notificação                                   |
| **Por evento** | Desvio lateral de 5 NM                                  |
| **Por evento** | Desvio de altitude de 200 pés                           |
| **Por evento** | Razão vertical de mais ou menos 2.000 pés por minuto    |
| **Por demanda** | Necessidade operacional                                 |

Os contratos por evento são o que transforma a ADS-C em ferramenta de conformidade: qualquer saída de rota, desvio de nível ou início de subida gera notificação sem você perguntar.

**Mesmo em ADS-C, o piloto deve enviar uma mensagem de posição em CPDLC na entrada da FIR**[^3]. Os estimados só precisam ser atualizados se variarem mais de 2 minutos[^4].

**Se a ADS-C falhar**, o piloto normalmente não é alertado pelo equipamento de bordo[^5]. Ao receber a notificação de falha: informe o piloto, exija reportes por CPDLC ou voz e restabeleça os mínimos aplicáveis[^6].

## CPDLC

### Logon

O identificador publicado é **`SBAO`**[^7]. Códigos dos desmembramentos em [Estrutura e setorização](estrutura.pt.md#posicoes-na-vatsim).

| Situação                          | Regra                                                                       |
| --------------------------------- | ---------------------------------------------------------------------------- |
| Quando fazer                      | **Entre 10 e 25 minutos** antes de ingressar na FIR[^8]                      |
| Decolando dentro do espaço aéreo  | Antes da decolagem[^8]                                                       |
| Vindo de FIR com enlace           | Transferência automática; a tripulação confere ao cruzar o limite[^9]        |
| Logon rejeitado                   | Indicativo e matrícula devem ser idênticos aos do plano de voo[^10]          |

### Regras de uso

| Regra                                                                    | Fonte  |
| ------------------------------------------------------------------------- | ------ |
| Quem fala por CPDLC recebe resposta por CPDLC; por voz, resposta por voz  | [^11]  |
| Todo diálogo deve ser fechado                                             | [^11]  |
| **Autorização por voz prevalece sobre a por CPDLC**                       | [^12]  |
| Texto livre só quando não houver mensagem padronizada; evite mensagens longas | [^13] |
| A CPDLC não é usada para vetorações                                       | [^14]  |
| `MONITOR`: muda de frequência **sem** chamada inicial                    | [^15]  |
| `CONTACT`: muda de frequência **e faz** chamada inicial                  | [^15]  |

**Se a CPDLC falhar**, reverta para voz iniciando com `CPDLC FAILURE`, ou `ALL STATIONS CPDLC FAILURE` se a falha for do sistema de solo. Mensagens pendentes são consideradas não encaminhadas e os diálogos recomeçam[^16]. Fraseologia completa em [Fraseologia e mensagens](fraseologia.pt.md#cpdlc).

## Voz

Na rede, a voz ocorre no canal VHF da posição, conforme [Estrutura e setorização](estrutura.pt.md#posicoes-na-vatsim). O contato inicial precisa estabelecer três coisas:

1. **Identificação**: indicativo da aeronave e do órgão.
2. **Situação**: posição, hora, nível e, se atribuída, a velocidade. A velocidade atribuída entra na chamada inicial após qualquer mudança de frequência[^17].
3. **Capacidade**: se há enlace ativo e se há SELCAL.

!!! info "Real e simulação"
    Este manual **não** afirma que o áudio da VATSIM reproduza propagação, cobertura ou degradação de HF. Trate o canal pelo que ele é: um canal de voz estável associado à posição.

## SELCAL

Código de quatro letras, obrigatório no item 18 precedido de `SEL/`[^18]. Duas regras práticas:

1. **Não faça cheque de SELCAL no primeiro contato de aeronave em CPDLC**, salvo se você solicitar[^19].
2. **Use o SELCAL para recuperar quem não responde**, ao lado de 121.5 MHz, frequência da empresa, frequência ar-ar e outras tripulações[^20].

!!! info "Real e simulação"
    Não há decodificador de bordo na rede: o cheque é convenção de fonia. Se o piloto não reconhecer o procedimento, não insista; combine escuta permanente na frequência e siga.

## Quando o meio primário falha

**A separação não pode depender de um meio que deixou de existir.**

| Perdeu  | O que fazer                                                                       |
| ------- | ---------------------------------------------------------------------------------- |
| ADS-C   | Exigir reportes por CPDLC ou voz e restabelecer os mínimos aplicáveis[^6]           |
| CPDLC   | Reverter para voz com `CPDLC FAILURE` e recomeçar os diálogos pendentes[^16]        |
| Voz     | Usar CPDLC para manter a segurança do voo até restabelecer[^21]                     |
| Ambos   | Aplicar o fluxo de [contingências](coordenacao.pt.md#perda-completa-de-comunicacao) |

[^1]: **AIP-Brasil, ENR 3.5, itens 8.3.1 e 9.5.1.3**.
[^2]: **AIP-Brasil, ENR 3.5, item 9.5.2.3**.
[^3]: **AIP-Brasil, ENR 3.5, item 9.5.2.1**.
[^4]: **AIP-Brasil, ENR 3.5, item 9.5.2.5**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.1**.
[^6]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.2**.
[^7]: **AIP-Brasil, ENR 3.5, item 9.2.1**.
[^8]: **AIP-Brasil, ENR 3.5, item 9.2.2**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.2.3**.
[^10]: **AIP-Brasil, ENR 3.5, itens 9.2.4 e 9.2.5**.
[^11]: **AIP-Brasil, ENR 3.5, item 9.4.1.3**.
[^12]: **AIP-Brasil, ENR 3.5, item 9.4.1.7**.
[^13]: **AIP-Brasil, ENR 3.5, itens 9.4.1.1 e 9.4.1.2**.
[^14]: **AIP-Brasil, ENR 3.5, item 9.1.6**.
[^15]: **AIP-Brasil, ENR 3.5, itens 9.4.1.5 e 9.4.1.6**.
[^16]: **AIP-Brasil, ENR 3.5, itens 9.4.4.2 a 9.4.4.5**.
[^17]: **ICA 100-37, Art. 180**.
[^18]: **MCA 100-11, item 2.2.8.1.12**, e **AIP-Brasil, ENR 3.5, item 9.4.3.2**.
[^19]: **AIP-Brasil, ENR 3.5, item 9.5.1.2**.
[^20]: **ICA 100-37, Art. 268**.
[^21]: **AIP-Brasil, ENR 3.5, item 9.1.4**.
