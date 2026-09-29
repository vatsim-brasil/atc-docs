---
title: Visão Geral Operacional
icon: material/eye
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

## A posição

`SBAO_FSS` representa o ACC Atlântico. O sufixo `_FSS` identifica posição oceânica na convenção da rede e exige rating mínimo **C1**[^1].

| Porção do espaço aéreo          | Classe | Serviço                                               |
| ------------------------------- | ------ | ----------------------------------------------------- |
| Acima do FL 245 (Atlântico UIR) | `A`    | Controle de tráfego aéreo, informação de voo e alerta |
| Abaixo do FL 145                | `G`    | Informação de voo e alerta, sem controle              |

Na prática, o tráfego é quase todo IFR de longo curso em nível de cruzeiro, portanto em Classe `A`, onde todos os voos são separados entre si.

## O que muda em relação a um ACC continental

| Recurso continental      | Na FIR Atlântico                                                        |
| ------------------------ | ------------------------------------------------------------------------ |
| Vigilância radar         | **Não existe.** A FIR não consta da cobertura publicada[^2]              |
| VHF direta em toda a área | **Não existe.** As frequências publicadas do órgão são HF[^3]           |
| Voz como meio primário   | **Invertido.** ADS-C e CPDLC são o meio primário, HF é o secundário[^4]  |
| Vetoração                | **Não se aplica.** A CPDLC não é usada para vetorações[^5]               |
| Separação de 5 NM        | **Não se aplica.** As mínimas são procedurais, em minutos e dezenas de NM |

A FIR Atlântico é expressamente excetuada das duas regras que valem nas demais FIR brasileiras: aqui a CPDLC não é meio adicional à voz, e é empregada mesmo sem serviço de vigilância ATS[^6].

## As três perguntas

Tudo o que o controlador faz responde a uma destas:

1. **Onde está a aeronave?** ADS-C quando disponível, reporte de posição quando não. Ver [Comunicações](controle.pt.md) e [Fluxo operacional](fluxo.pt.md).
2. **Como falo com ela?** CPDLC primário, voz secundária, SELCAL para recuperar quem sumiu. Ver [Comunicações](controle.pt.md).
3. **Ela está separada?** Cálculo sobre estimados, níveis e número Mach. Ver [Separação](separacao.pt.md).

!!! danger "O erro não aparece sozinho"
    Em espaço radar, um conflito que se forma fica visível na tela. Aqui, um estimado desatualizado produz uma imagem mental errada que permanece errada até o próximo reporte. Manter o registro em dia não é burocracia, é o instrumento de vigilância.

## O ciclo da sessão

| Etapa                                 | Página                                             |
| ------------------------------------- | -------------------------------------------------- |
| Consultar limites, setores e frequências | [Estrutura e setorização](estrutura.pt.md)       |
| Preparar, conectar e abrir            | [Preparação e abertura](abertura.pt.md)             |
| Receber a aeronave e conferir o plano | [Plano de voo](plano-de-voo.pt.md)                  |
| Estabelecer comunicação               | [Comunicações e vigilância](controle.pt.md)         |
| Acompanhar e registrar a progressão   | [Fluxo operacional](fluxo.pt.md)                    |
| Separar, tratar solicitações e desvios | [Separação, rotas e desvios](separacao.pt.md)      |
| Coordenar, transferir e tratar falhas | [Coordenação e contingências](coordenacao.pt.md)    |

!!! tip "Na rede (Vatbrz)"
    Poucos tráfegos, cada um por muito tempo. Um voo Europa/Sudeste ocupa a posição por mais de duas horas. Planeje a sessão pensando em duração, não em volume, e informe o horário previsto de desconexão no *controller information*.

[^1]: **VATSIM, GCAP v2.0, item 6.3**.
[^2]: **AIP-Brasil, ENR 1.6, itens 3 e 4**.
[^3]: **AIP-Brasil, ENR 2.1**.
[^4]: **AIP-Brasil, ENR 3.5, itens 8.3.1 e 9.5.1.3**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.1.6**.
[^6]: **AIP-Brasil, ENR 3.5, itens 9.1.3 e 9.1.5**.
