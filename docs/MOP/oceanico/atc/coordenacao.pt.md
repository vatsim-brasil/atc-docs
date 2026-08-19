---
title: Coordenação e Contingências
icon: material/swap-horizontal
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Em espaço procedural a coordenação pesa mais do que em espaço radar, porque o órgão aceitante não tem como conferir sozinho o que recebeu.

## Formato de coordenação

Use sempre a mesma sequência. Ela cobre o exigido[^1] e cabe em uma linha.

```text
CALLSIGN | POINT | ESTIMATE | LEVEL | MACH | ROUTE | CAPABILITIES | COMMS
```

!!! example "Exemplo"
    **Saída:** *"EXEMPLO 123, KOSAX at 1448, flight level 370, Mach decimal 82, route direct TEBRO, RVSM and RNP 10, ADS-C and CPDLC active, SELCAL AB-CD."*

    **Aceitação:** *"EXEMPLO 123 accepted at flight level 370."*

    **Renegociação:** *"EXEMPLO 123 unable flight level 370 due traffic. Available flight level 350 or estimate KOSAX 1500."*

## Quando coordenar

Sempre que algo já informado ao adjacente mudar:

| Gatilho                            | O que informar                                    |
| ---------------------------------- | ------------------------------------------------- |
| Estimado revisado                  | Novo estimado e motivo                            |
| Mudança de nível                   | Novo nível e ponto em que estará nivelada         |
| Mudança de Mach                    | Novo Mach e efeito sobre o estimado               |
| Rota alterada                      | Nova rota, novo ponto de saída, novos estimados   |
| Desvio meteorológico               | Lado, extensão, duração e estimado revisado       |
| Emergência                         | Natureza, intenções e assistência necessária      |
| Falha de comunicação               | Último contato, última posição confirmada, nível e Mach |
| Tráfego conflitante                | Identificação, posição, nível e trajetória        |
| Mudança de posição na rede         | Quem assume, a partir de quando, e cada tráfego   |

Uma aeronave não deve adentrar espaço aéreo de outro órgão sem coordenação concluída[^2].

## Entre posições da FIR

Quando a FIR opera desmembrada, as posições trocam informações de plano de voo e controle de tudo que é transferido e de tudo que evolui perto do limite interno[^3]. Trate a fronteira interna como fronteira de FIR.

- **Ao abrir** um desmembramento: quem chega recebe a lista completa dos tráfegos que passam para a sua área.
- **Ao fechar**: quem sai entrega a mesma lista e confirma que a outra posição recebeu cada um.

## Contingências

### A sequência, sempre a mesma

**Identificar → Confirmar → Proteger a separação → Estabelecer meio alternativo → Coordenar → Registrar → Normalizar ou transferir.**

Proteger a separação vem **antes** de restabelecer a comunicação. Não depende dela.

### Tabela de ação

| Situação                         | Ação imediata                                                                | Efeito na separação                          |
| -------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------- |
| **Perda de CPDLC**               | Reverter para voz com `CPDLC FAILURE`; diálogos pendentes recomeçam[^4]       | Mínimas dependentes de enlace deixam de valer |
| **Perda de ADS-C**               | Informar o piloto (o equipamento dele não avisa) e exigir reportes[^5]        | Restabelecer mínimos sem ADS-C               |
| **Falha de voz**                 | Tentar frequências secundárias e 121.5 MHz[^6]; usar CPDLC no interim[^7]     | Ampliar separação com os afetados            |
| **Falha de SELCAL**              | Combinar escuta permanente na frequência e seguir                             | Nenhum: é recurso de chamada                 |
| **Perda total de comunicação**   | Esgotar 121.5 MHz, SELCAL, frequência da empresa, ar-ar 123.45 MHz e outras tripulações[^6] [^8] | Ver abaixo             |
| **Degradação de navegação**      | Aumentar frequência dos reportes                                              | Outro tipo ou mínimo; RNAV deixa de valer[^9] |
| **Não mantém nível ou Mach**     | Obter o que ela consegue manter e por quanto tempo                            | Vertical volta a 2.000 pés; Mach deixa de reduzir[^10] |
| **Desvio meteorológico urgente** | Informar tráfego conflitante, oferecer nível livre, depois tratar do lateral  | Ver [Separação](separacao.pt.md#desvios)     |
| **Emergência declarada**         | Confirmar intenções, limpar níveis e rota, prestar toda assistência[^11]      | Separação de emergência se necessário[^12]   |
| **Sem capacidades declaradas**   | Confirmar o que ela faz de fato e exigir reporte em todos os pontos           | Mínimas maiores: 2.000 pés, 100 NM, sem redução por Mach |
| **Piloto desconecta**            | Registrar hora e última posição; avisar quem o aguardava                      | Liberar o espaço protegido                   |
| **Controlador reconecta**        | Não presumir o quadro anterior: refazer o levantamento e pedir reporte a todos | Reconfirmar coordenações pendentes          |
| **Sobrecarga**                   | Desmembrar, ou coordenar espaçamento maior na entrega                         | **Nunca improvisar mínimas menores**         |
| **Adjacente sai sem coordenar**  | Assumir até o limite da jurisdição e tratar cada saída como órgão offline      | Resolver conflitos dentro da FIR             |
| **Conflito detectado tarde**     | **Verticalizar primeiro**, informar tráfego às duas, depois velocidade ou rota | Emergência se nada resolver[^12]            |

### Perda completa de comunicação

Além da tabela acima:

1. **Trate a aeronave como podendo estar em qualquer ponto** entre a última posição confirmada e a projetada, e afaste todos os demais tráfegos dessa faixa e do nível.
2. Oriente as outras aeronaves a tentarem contato na frequência ar-ar **123.45 MHz**, prevista para voo em zonas remotas e oceânicas fora do alcance de estações VHF[^8].
3. Informe todos os adjacentes e o próximo órgão da rota.

!!! warning "Fases de emergência"
    A **Fase de Incerteza (INCERFA)** começa 30 minutos após a hora em que a comunicação era esperada, ou da primeira tentativa infrutífera, o que ocorrer primeiro[^13]. Cai para 15 minutos em voos de até 1 hora[^14]. Seguem-se **ALERFA** e **DETRESFA** se as tentativas continuarem infrutíferas[^15].

### Emergência com ADS-C

Aeronave equipada pode ativar o modo de emergência do ADS-C. Recebido o reporte, **acuse o recebimento pelo meio mais apropriado** e preste toda a assistência possível[^11].

[^1]: **ICA 100-37, Arts. 814, 818 e 824**.
[^2]: **ICA 100-37, Art. 822**.
[^3]: **ICA 100-37, Art. 852**.
[^4]: **AIP-Brasil, ENR 3.5, itens 9.4.4.2 a 9.4.4.5**.
[^5]: **AIP-Brasil, ENR 3.5, itens 9.5.2.6.1 e 9.5.2.6.2**.
[^6]: **ICA 100-37, Arts. 267 e 268**.
[^7]: **AIP-Brasil, ENR 3.5, item 9.1.4**.
[^8]: **AIP-Brasil, ENR 1.1, item 4.1.1**.
[^9]: **ICA 100-37, Arts. 337 e 382**.
[^10]: **AIP-Brasil, ENR 2.2, itens 1.6 e 1.13**.
[^11]: **ICA 100-37, Arts. 1088 a 1090**.
[^12]: **ICA 100-37, Arts. 270 e 271**.
[^13]: **ICA 100-37, Art. 804**.
[^14]: **ICA 100-37, Art. 805**.
[^15]: **ICA 100-37, Arts. 807 e 808**.
