---
title: NOTAM
icon: material/alert-circle
---

--8<-- "includes/abreviacoes.md"

# NOTAM (AISWEB) — leitura e interpretação

## O que é (operacional)

NOTAM é um aviso oficial para informar **mudanças temporárias** ou **informações críticas** que afetem a operação, como:

- pista/interseções fechadas,
- auxílios à navegação indisponíveis,
- procedimentos alterados,
- restrições no espaço aéreo,
- obstáculos e balizamento,
- operações especiais (eventos, fluxo, etc.).

!!! tip "Operacional"
    NOTAM é parte do "risco operacional não-meteorológico", mas frequentemente **interage** com meteorologia:
    - baixa visibilidade + pista contaminada/obras
    - teto baixo + auxílio indisponível
    - CB/TS + procedimento RNAV/ILS restrito

---

## Estrutura (mapa mental)

Campos mais comuns:

- **Q)**: classificação/escopo (código Q), FIR, limites verticais e área
- **A)**: localidade (aeródromo/área)
- **B)**: início (UTC)
- **C)**: fim (UTC) (ou `PERM`)
- **D)**: horários (quando aplicável)
- **E)**: texto principal (o que muda / o que está indisponível)
- **F)/G)**: níveis (quando aplicável)

> Abreviaturas aeronáuticas variam; use AIP/GEN e listas oficiais. Veja [Referências](referencias.pt.md).

---

## Consulta (AISWEB)

- Página de NOTAM (AISWEB): consultas básicas e "últimos NOTAM emitidos".
- NOTAM por aeródromo também aparece na página do aeródromo (AISWEB).

---

## Exemplos reais (AISWEB e documentos DECEA)

### Lista de "últimos NOTAM emitidos" (amostra)

> Exemplo de como o AISWEB lista número, local e data/hora (formato resumido).

```text
E7505/25 SBRJ E 29/12/25 12:29
E7504/25 SBRJ E 29/12/25 12:28
E7503/25 SBRJ E 29/12/25 12:28
E7502/25 SBRJ E 29/12/25 11:31
E7501/25 SBRJ E 29/12/25 11:30
E7500/25 SBRJ E 29/12/25 11:30
B2878/25 SBRJ B 29/12/25 08:49
```

### NOTAM com "Q) / A) / B) / C) / E)" (exemplo em relatório DECEA)

```text
SBRJ B3118/24 NOTAMN
Q) SBRE/QPFCA/IV/NBO/AE/000/999/1632S03906W005
A) SBTV - PORTO SEGURO/TERRAVISTA,BA
B) 21/12/24 00:00 - C) 06/01/25 23:59 UTC
E) PROC CTL FLUXO ACT ACFT TKOF DE SBTV COM DEST A SBXP (TMA-SP) ...
```

**Leitura operacional:**

Identifique rapidamente: o que, onde, quando, como impacta.

O campo E) é o "coração" (restrição/procedimento).

---

## Padrão de leitura (check rápido)

1. **Validade (B/C)**: está vigente para seu horário?
2. **Local (A)**: afeta seu aeródromo/rota/área?
3. **Texto (E)**: afeta pista, aproximação, mínimo, taxi, saída, SID/STAR?
4. **Mitigação**: alternar procedimento, mudar janela, selecionar alternado, rebrief.

---

## Erros comuns

- Ignorar horário (UTC) e aplicar NOTAM fora da validade.
- Ler "por cima" e perder detalhe (interseção fechada, restrição parcial, janela diária DLY).
- Não cruzar NOTAM com METAR/TAF: clima degradado + restrição operacional amplifica risco.
