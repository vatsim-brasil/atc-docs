---
title: TAF
icon: material/weather-rainy
---

--8<-- "includes/abreviacoes.md"

![Manual de Meteorologia - TAF](img/manual-meteorologia-taf.png)

#

## Estrutura (essência)

TAF normalmente contém:

- **Localidade**
- **Emissão (UTC)**
- **Validade** (janela)
- **Condição base**
- **Grupos de mudança**: `BECMG`, `TEMPO`, `PROBxx`, `FM` (quando aplicável)
- **Temperaturas**: `TX..` / `TN..` (quando fornecidas)
- **RMK**: observações

!!! warning "Operacional"
    Para decisão, foque no **pior caso dentro da janela relevante** (especialmente `TEMPO` e `PROB`).

---

## Grupos (como pensar)

| Grupo | Ideia operacional | Risco típico |
| :--- | :---------------- | :----------- |
| `BECMG` | muda gradualmente para nova condição | janela de transição |
| `TEMPO` | flutuação temporária | "piora intermitente" |
| `PROB30/40` | probabilidade | planejamento conservador |
| `FM` | mudança "a partir de" | quebra de cenário |

---

## Biblioteca de exemplos reais (REDEMET)

### TAF SBSP (Congonhas) — com TS/CB em janela TEMPO

```text
TAF SBSP 290900Z 2912/2924 05002KT CAVOK TX34/2918Z TN23/2924Z
BECMG 2912/2914 36005KT
BECMG 2915/2917 25004KT
TEMPO 2919/2921 TS SCT035 FEW050CB
BECMG 2921/2923 17004KT CAVOK
RMK PHG=
```

**Leitura operacional:**

Base CAVOK, mas existe uma janela TEMPO com TS e CB (2919–2921Z).

Planeje chegada/saída evitando a janela, ou com alternado/margens.

### TAF SBGR (Guarulhos) — PROB/TEMPO TSRA

```text
TAF SBGR 290900Z 2912/3018 35005KT CAVOK TN21/3008Z TX36/3018Z
BECMG 2915/2917 32005KT FEW035
PROB40 TEMPO 2917/2920 TSRA SCT025 FEW045CB
BECMG 2920/2922 10005KT
BECMG 3006/3008 08002KT
BECMG 3008/3010 08002KT SCT015
...
RMK PHG=
```

**Leitura operacional:**

O risco aqui está concentrado na janela PROB40 TEMPO TSRA (2917–2920Z).

Em operação conservadora, trate PROB40 como risco "real" para planejamento.

### TAF SBBP (com mudanças graduais)

```text
TAF SBBP 180800Z 1812/1824 14010KT 9999 SCT030 TN18/1812Z TX24/1818Z
BECMG 1812/1814 13008KT FEW025
RMK PGE=
```

### TAF SBSC (simples / melhora para CAVOK)

```text
TAF SBSC 092100Z 1000/1012 VRB03KT 9999 SCT020 TN24/1007Z TX30/1012Z
BECMG 1009/1011 CAVOK
RMK PFP=
```

---

## Interpretações guiadas — exemplos selecionados

### 1) Janela curta, alto impacto (TS + CB)

Se houver:

```text
TEMPO .... TS ... FEW...CB
```

**Operacionalmente:**

A janela TEMPO pode coincidir com aproximação final.

Considere: atraso tático, alternado com melhor estabilidade, combustível para holding.

### 2) BECMG + vento

Quando o BECMG muda vento significativamente, avalie:

- componente cruzado,
- pista em uso,
- impacto de rajadas e variação.

---

## Erros comuns em TAF

- Ler apenas a condição base e ignorar TEMPO/PROB.
- Não alinhar janela TAF com seu ETA real (UTC).
- Assumir que "CAVOK no TAF" elimina risco: TS pode aparecer como TEMPO/PROB.
