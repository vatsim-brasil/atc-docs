---
title: Item 18 (Outros Dados)
icon: material/information-outline
---

# Item 18 (Outros Dados)

O ITEM 18 é onde você “fecha o contrato” do plano: detalhes de performance, RNAV/PBN, pontos especiais e observações.

**Regra de qualidade:** use **somente indicadores previstos** (ex.: `STS/`, `PBN/`, `DEP/`, `DEST/`, `ALTN/`, `REG/`, `DOF/`, `EET/`, `RMK/`). Indicadores inventados tendem a quebrar o processamento.

## Indicadores mais usados (práticos)

| Indicador | Para que serve | Exemplo |
|---|---|---|
| `DEP/` | Detalhar local de partida quando ITEM 13 = `ZZZZ` | `DEP/FAZENDA X 12NM N SBSP` |
| `DEST/` | Detalhar destino quando ITEM 16 = `ZZZZ` | `DEST/HELIPONTO Y` |
| `ALTN/` | Detalhar alternado quando alternado = `ZZZZ` | `ALTN/AERODROMO PRIVADO Z` |
| `TYP/` | Tipo de aeronave quando ITEM 9 = `ZZZZ` | `TYP/KC130` |
| `REG/` | Matrícula (quando necessário) | `REG/PTRBA` |
| `DOF/` | Data do voo (formato YYMMDD) | `DOF/260117` |
| `EET/` | Estimativas até FIR/pontos relevantes (quando aplicável) | `EET/SBAO0130` |
| `RMK/` | Observações em linguagem clara ou códigos exigidos | `RMK/500FT AGL` |

## STS/ (tratamento especial)

Use quando o voo requer tratamento especial por ATS (ex.: busca e salvamento, evacuação médica, calibração etc.).

Exemplos comuns:

- `STS/SAR`
- `STS/FLTCK`

> Quando o motivo não estiver na lista prevista, use `RMK/` para explicar.

## PBN/ (RNAV/RNP)

Indica especificações RNAV/RNP aplicáveis ao voo, por códigos (ex.: RNAV 1, RNAV 2, RNAV 5, etc.).

Em simulação, mantenha simples e coerente com a aeronave e a rota. Se você não domina PBN, prefira manter **o plano consistente com o que você realmente vai voar** (por exemplo, SID/STAR RNAV exige capacidade RNAV apropriada).

## Templates úteis (copiar e adaptar)

### VFR abaixo da tabela (exemplo de RMK)

| Campo | Valor |
|---|---|
| ITEM 15 | `VFR` |
| ITEM 18 | `RMK/500FT AGL` |

### Aeródromo sem ICAO (ZZZZ)

| Campo | Valor |
|---|---|
| ITEM 13 | `ZZZZ` |
| ITEM 18 | `DEP/LOCALIDADE OU COORDENADAS` |

---
