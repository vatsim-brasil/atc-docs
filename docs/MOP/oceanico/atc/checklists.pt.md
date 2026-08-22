---
title: Checklists
icon: material/format-list-checks
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

Listas de verificação para uso durante a sessão. Cada item remete ao capítulo em que o assunto está tratado por extenso.

## Abertura da posição

### Autorização

- [ ] Constar do ATC Roster da VATSIM Brasil
- [ ] Possuir rating **C1** ou superior
- [ ] Possuir o endorsement **Tier 2 "Oceanic Positions"**

Detalhes em [Preparação e abertura, Autorização](abertura.pt.md#autorizacao).

### Cliente e setor

- [ ] Pacote de setor **SBAO** instalado e no ciclo AIRAC vigente
- [ ] Perfil **radar** carregado, e não o perfil solo
- [ ] EuroScope reiniciado, se a posição anterior era de outra FIR
- [ ] Pontos de visibilidade distribuídos pela extensão do setor
- [ ] Alcance de tela mostrando o ponto de entrada e o de saída da rota principal

### Conexão e áudio

- [ ] Indicativo correto da posição, conforme [a tabela de posições](estrutura.pt.md#posicoes-na-vatsim)
- [ ] Frequência primária correspondente à posição
- [ ] TrackAudio conectado **depois** do EuroScope
- [ ] `RX` e `TX` habilitados manualmente na frequência da posição
- [ ] `XCA` ativado na frequência da posição
- [ ] Frequências não utilizadas removidas da interface

### Enlace de dados

- [ ] Código de logon conferido: `SBAO` para a posição geral
- [ ] Integração de enlace conectada e janela de mensagens visível
- [ ] Se indisponível, decidido que a sessão será conduzida por voz e reportes

### Publicação da posição

- [ ] *Controller information* preenchido, no máximo quatro linhas de 76 caracteres, em inglês
- [ ] Horário previsto de desconexão informado
- [ ] Indicação de controle procedural sem vigilância radar
- [ ] Situação do enlace de dados informada

### Antes de anunciar

- [ ] Adjacentes online identificados
- [ ] Abertura coordenada com cada adjacente conectado
- [ ] Tráfegos já dentro da FIR levantados
- [ ] Reporte de posição obtido de cada aeronave sem registro
- [ ] Plano de desmembramento definido, se houver outro controlador habilitado

## Recebimento de cada aeronave

- [ ] **Identificação** confirmada
- [ ] **Rota** conferida contra o setor, com pontos de notificação reconhecidos
- [ ] **Nível** compatível com a tabela aplicável
- [ ] **Número Mach** declarado ou obtido do piloto
- [ ] **Capacidades** conferidas: `W` para RVSM, `R` para PBN, `D1` para ADS-C, `SEL/` para SELCAL
- [ ] **Estimado** de entrada confirmado, por coordenação, por `EET/` ou pelo piloto
- [ ] **Comunicação** estabelecida, com o meio em uso identificado
- [ ] **Conflitos** avaliados contra todo o quadro antes de aceitar
- [ ] **Registro** aberto com estimado para o próximo ponto

Detalhes em [Plano de voo e capacidades](plano-de-voo.pt.md) e [Fluxo operacional](fluxo.pt.md).

## Acompanhamento

A cada reporte recebido, ou a cada 15 minutos:

- [ ] **Posição** atualizada, com hora exata
- [ ] **Estimado** do próximo ponto revisado
- [ ] **Separação** recalculada para todos os pares afetados
- [ ] **Solicitações** pendentes respondidas
- [ ] **Coordenação** feita, se algo já informado ao adjacente mudou
- [ ] **Registro** atualizado

Sinais de alerta que exigem ação imediata:

- [ ] Reporte esperado que não chegou
- [ ] Estimado revisado em mais de 2 minutos
- [ ] Notificação de evento ADS-C por desvio lateral, desvio de altitude ou razão vertical
- [ ] Aeronave informando incapacidade de manter nível, Mach ou precisão de navegação

## Transferência

- [ ] **Estimado** do ponto de transferência calculado e atualizado
- [ ] **Coordenação** enviada com antecedência suficiente
- [ ] **Aceitação** do próximo órgão obtida, ou condições renegociadas
- [ ] **Informações atualizadas** confirmadas: nível, Mach, rota e capacidades
- [ ] **Instrução ao piloto** emitida, com `CONTACT` ou `MONITOR` conforme o caso
- [ ] **Enlace de dados** transferido, ou logon refeito, ou conexão encerrada
- [ ] **Registro** encerrado com a hora sobre o ponto de transferência

Se o próximo órgão não estiver online:

- [ ] Piloto informado de que não há órgão ATS conectado à frente
- [ ] Informações para apresentação adiante fornecidas
- [ ] Última posição, nível e Mach registrados
- [ ] Serviço encerrado de forma explícita

## Fechamento da posição

- [ ] **Aviso antecipado** aos adjacentes e às aeronaves em frequência
- [ ] **Coordenação** de encerramento com cada adjacente conectado
- [ ] **Transferência** de todos os tráfegos que ainda podem ser entregues
- [ ] **Verificação** de aeronaves que ficarão sem atendimento, com orientação explícita a cada uma
- [ ] **Se houver outra posição da FIR online**, entrega da lista completa de tráfegos, com posição, nível, Mach, estimado e situação de comunicação
- [ ] **Encerramento das conexões**: enlace de dados, TrackAudio e cliente ATC, nesta ordem
- [ ] **Desconexão** somente após confirmar que nenhuma aeronave ficou aguardando resposta

!!! tip "Na rede (Vatbrz)"
    Anuncie o fechamento com pelo menos 15 minutos de antecedência. Em uma FIR onde o tempo de travessia é medido em horas, um piloto que perde o órgão sem aviso pode ficar sem referência por muito tempo.
