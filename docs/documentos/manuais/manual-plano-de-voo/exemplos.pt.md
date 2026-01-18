---
title: Exemplos práticos
icon: material/book-open-page-variant
---

![Manual de Plano de Voo (FPL) - Exemplos](img/manual-plano-de-voo-exemplos.png)

#

Os exemplos abaixo são pensados para **simulação** (VATSIM) e servem como referência de consistência.

## Exemplo 1 — VFR local (baixa altura)

| Item | Preenchimento | Comentário |
|---:|---|---|
| 7 | `PTABC` | Matrícula (até 7) |
| 8 | `V/G` | VFR / Aviação Geral |
| 9 | `1/C172/L` | 1 aeronave, tipo, esteira |
| 10 | `S/C` | Padrão + transponder conforme aplicável |
| 13 | `SBSP 1400` | Partida + EOBT (UTC) |
| 15 | `VFR` | Fora da tabela → detalhar em RMK |
| 16 | `SBSP 0045` | Local + duração total |
| 18 | `RMK/1500FT AGL LOCAL` | Ajuste de altura/localidade |
| 19 | (quando exigido) | Em simulação, normalmente omitido |

## Exemplo 2 — IFR doméstico (com aerovias)

| Item | Preenchimento | Comentário |
|---:|---|---|
| 7 | `GLO1866` | Companhia + número |
| 8 | `I/S` | IFR / Regular |
| 9 | `1/B738/M` | B738, esteira média |
| 10 | `SG/C` | S + GNSS (quando aplicável) |
| 13 | `SBGR 2230` | Partida + EOBT |
| 15 | `N0475 F350 DCT ...` | Velocidade, nível, rota |
| 16 | `SBRJ 0055 SBSP SBGL` | Destino+EET + alternados |
| 18 | `DOF/260117` | Data do voo |

> Na rota, substitua `...` pelos fixes/aerovias reais do seu planejamento (ex.: SimBrief/Navigraph).

## Template de “formulário” (para copiar)

Preencha e mantenha como checklist pessoal:

| Campo | Valor |
|---|---|
| Aeronave (ITEM 7) | `_______` |
| IFR/VFR + Tipo (ITEM 8) | `_______` |
| Tipo + WTC (ITEM 9) | `_______` |
| Equipamentos (ITEM 10) | `_______` |
| Partida + EOBT (ITEM 13) | `_______` |
| Vel/Nível/Rota (ITEM 15) | `_______` |
| Destino+EET+ALTN (ITEM 16) | `_______` |
| Outros dados (ITEM 18) | `_______` |

---
