---
title: Preenchimento do FPL (Campos principais)
icon: material/file-edit
---

![Manual de Plano de Voo (FPL) - Preenchimento do FPL](img/manual-plano-de-voo-preenchimento.png)

#

Esta seção cobre os campos que normalmente **sempre** aparecem em um FPL consistente.

> Convenção: sempre que houver campo “desconhecido” para o padrão OACI (sem designador), costuma-se usar **ZZZZ** e detalhar no **ITEM 18** com o indicador apropriado (ex.: `DEP/`, `DEST/`, `ALTN/`, `TYP/`).

## ITEM 7 — Identificação da aeronave

Regra de ouro: **até 7 caracteres**, alfanuméricos, sem hífen/símbolos.

| Situação | O que preencher | Exemplo |
|---|---|---|
| Voo comercial (companhia) | Designador telegráfico OACI + número do voo | `GLO1866`, `NGA213` |
| Aviação geral (matrícula) | Marca de nacionalidade/comum + matrícula | `PTRBA`, `PRERR`, `N256GA` |
| Outro designador oficial | Conforme registro aplicável | `FAB2506` |

**Exceção importante:** se o indicativo em radiotelefonia **exceder 7 caracteres**, preencha o ITEM 7 com a matrícula e use `RMK/` no ITEM 18 para informar o indicativo completo.

## ITEM 8 — Regras de voo e tipo de voo

### Regras de voo (1 letra)

| Código | Significado |
|---|---|
| `I` | IFR (todo o voo IFR) |
| `V` | VFR (todo o voo VFR) |
| `Y` | IFR inicialmente e depois muda para VFR |
| `Z` | VFR inicialmente e depois muda para IFR |

### Tipo de voo (1 letra)

O tipo de voo depende do contexto (ex.: aviação geral, comercial, militar). Em simulação, é comum ver:

| Código | Uso típico |
|---|---|
| `S` | Regular/“Scheduled” (linhas) |
| `N` | Não regular (charter/geral) |
| `G` | Aviação geral |
| `M` | Militar |
| `X` | Outro |

> Dica operacional: em VATSIM, **`G` (aviação geral)** e **`S` (linhas)** cobrem a maioria dos casos.

## ITEM 9 — Número, tipo de aeronave e esteira de turbulência

| Campo | Como preencher | Exemplo |
|---|---|---|
| Número | Quantidade, quando for **formação** | `2`, `4` |
| Tipo de aeronave | Designador OACI (Doc 8643) | `B738`, `A320`, `E110` |
| Sem designador / militar específico | Use `ZZZZ` e detalhe no ITEM 18 (`TYP/`) | `ZZZZ` + `TYP/KC130` |
| Esteira de turbulência | `J` SUPER, `H` PESADA, `M` MÉDIA, `L` LEVE | `M` |

## ITEM 10 — Equipamentos e capacidades

Este campo é dividido em dois blocos:

1) **COM/NAV/APP** (lado esquerdo)
2) **Vigilância / Transponder** (lado direito)

### Atalho seguro (para simulação)

- Se sua aeronave tem o “pacote padrão” de rádios/navegação para a rota: use **`S`**
- Se você quer indicar GNSS/RNAV de forma explícita para IFR: inclua **`G`**

> Em operação real, o ITEM 10 pode ficar longo. Em simulação, o importante é coerência: equipamento declarado deve refletir o que você pretende usar.

## ITEM 13 — Aeródromo de partida e hora

| Campo | Como preencher | Exemplo |
|---|---|---|
| Partida | ICAO (4 letras). Se não existir: `ZZZZ` + `DEP/` no ITEM 18 | `SBSP` |
| Hora | **EOBT** (calços fora) em UTC, 4 dígitos | `1435` |

## ITEM 15 — Velocidade, nível e rota

### Velocidade (até 5)

| Formato | Exemplo | Observação |
|---|---|---|
| `K####` | `K0650` | km/h |
| `N####` | `N0480` | nós |
| `M###` | `M082` | Mach |

### Nível

| Formato | Exemplo | Observação |
|---|---|---|
| `F###` | `F330` | nível de voo (FL) |
| `A###` | `A040` | altitude (centenas de pés) |
| `VFR` | `VFR` | quando o VFR não seguir a tabela e você detalha em `RMK/` |

### Rota

- Use **rotas ATS** (airways) quando aplicável.
- Use **`DCT`** para trechos diretos.
- Se usar `Y` ou `Z` (mudança IFR/VFR), a rota precisa indicar **ponto(s) de mudança**.

## ITEM 16 — Destino, EET total e alternados

| Campo | Como preencher | Exemplo |
|---|---|---|
| Destino | ICAO (4 letras) ou `ZZZZ` + `DEST/` no ITEM 18 | `SBBE` |
| EET total | Duração total estimada (HHMM), junto do destino | `0245` |
| Alternado 1/2 | ICAO (4 letras) ou `ZZZZ` + `ALTN/` no ITEM 18 | `SBSL` / `SBTE` |

---
