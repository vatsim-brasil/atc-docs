---
title: METAR e SPECI
icon: material/weather-sunny
---

--8<-- "includes/abreviacoes.md"

# METAR e SPECI (leitura operacional)

## Estrutura (mapa mental)

Um METAR/SPECI normalmente segue esta ordem:

1. **Tipo**: `METAR` ou `SPECI`
2. **Localidade ICAO**: ex. `SBGR`
3. **Data/hora (UTC)**: ex. `291200Z`
4. **Vento**: direção/velocidade, variação, rajadas
5. **Visibilidade**: em metros (`9999` = ≥ 10 km)
6. **Fenômenos**: `-RA`, `TS`, `BR`, `FG`, etc.
7. **Nuvens**: `FEW/SCT/BKN/OVC` + altura (centenas de pés) + `CB/TCU`
8. **Temperatura/Ponto de orvalho**: `TT/TD`
9. **Pressão**: `QNH` (`Q1016`)
10. **Complementos**: `RE...`, `WS RWY..`, `NOSIG`, correções, observações

!!! tip "Operacional"
    Leia primeiro: **vento + visibilidade + fenômenos + teto (BKN/OVC mais baixo) + QNH**.  
    O restante confirma nuance e tendência.

---

## Vento (interpretação rápida)

| Grupo | Exemplo | Interpretação |
| :--- | :------ | :------------ |
| Direção/vel | `31005KT` | 310° / 5 kt |
| Calmo | `00000KT` | sem vento significativo |
| Variável (sem direção) | `VRB03KT` | direção variável / 3 kt |
| Variação direcional | `220V010` | variando entre 220° e 010° |
| Rajadas | `03012G24KT` | 12 kt com rajadas até 24 kt |

**Pontos de atenção**

- `G` (rajadas) + `TS` / `SH` → risco de rajada e mudança de performance.
- `xxxVyyy` grande → componente cruzado pode variar rápido.

---

## Visibilidade e fenômenos

- `9999` = **visibilidade ≥ 10 km**
- `BR` = névoa úmida (reduz visibilidade)
- `FG` = nevoeiro (geralmente mais crítico)
- `-RA / RA / +RA` = chuva fraca / moderada / forte
- `TS` = trovoada (pode aparecer com `CB`)
- `DZ` = garoa/chuvisco

---

## Nuvens e teto (o que importa)

- `FEW` e `SCT` normalmente **não definem teto**.
- `BKN` ou `OVC` **definem teto** (use o menor BKN/OVC).
- Altura é em centenas de pés:
  - `BKN015` → **1500 ft**
  - `OVC002` → **200 ft**

---

## Biblioteca de exemplos reais (REDEMET)

> Abaixo há exemplos reais, obtidos de consultas automáticas da REDEMET (vários aeródromos/datas).  
> A finalidade aqui é **reconhecer padrões** rapidamente.

### METAR (CAVOK / bom tempo)

```text
METAR SBGR 291200Z 31005KT CAVOK 26/20 Q1016=
METAR SBBR 291200Z VRB03KT CAVOK 26/20 Q1018=
METAR SBMG 290200Z 00000KT CAVOK 25/21 Q1013=
METAR SBMT 040000Z VRB02KT CAVOK 22/18 Q1016=
METAR SBSP 040800Z AUTO 36006KT 330V030 CAVOK 21/19 Q1015=
```

### METAR (chuva e teto)

```text
METAR SBSP 040400Z AUTO 34010KT 9999 -RA FEW012 BKN024 21/20 Q1017=
METAR SBSP 042000Z 31011KT 8000 -RA SCT015 OVC080 23/21 Q1016=
METAR SBMT 042100Z 14003KT 110V170 7000 -RA SCT017 FEW035TCU OVC080 21/20 Q1016=
METAR SBPV 291200Z 32002KT 9999 OVC002 23/22 Q1013=
METAR SBVH 291200Z 29007KT 5000 BR SCT011 OVC055 21/20 Q1017=
```

### SPECI (mudança significativa / convectivo)

```text
SPECI SBSP 040201Z 36005KT CAVOK 23/20 Q1017=
SPECI SBMT 041936Z 03012G24KT 340V070 1000 -TSRA BR BKN015 FEW035CB 21/19 Q1016=
SPECI SBPV 291223Z 17002KT 9999 OVC005 24/22 Q1013=
```

### METAR COR (correção)

```text
METAR COR SBMT 042000Z 04007KT 360V090 3000 -RA BR BKN015 FEW035TCU 20/19 Q1015 RETS=
```

---

## Interpretações guiadas (operacionais) — exemplos selecionados

### 1) Convectivo com redução severa de visibilidade (SPECI)

```text
SPECI SBMT 041936Z 03012G24KT 340V070 1000 -TSRA BR BKN015 FEW035CB 21/19 Q1016=
```

**Análise:**

- **SPECI**: mudança relevante (não esperar o próximo METAR).
- **03012G24KT**: rajadas fortes (instabilidade).
- **1000**: visibilidade 1 km (impacto direto em mínimos).
- **-TSRA BR**: trovoada com chuva e névoa úmida.
- **BKN015**: teto 1500 ft (IFR mais restritivo).
- **FEW035CB**: presença de CB (risco de turbulência, granizo, cisalhamento, microburst).

!!! warning "Leitura operacional"
    Cenário típico de "janela fechando"; alternado/holding e espera por melhora podem ser necessários.

### 2) Teto extremamente baixo (OVC002)

```text
METAR SBPV 291200Z 32002KT 9999 OVC002 23/22 Q1013=
```

**Análise:**

- **OVC002**: céu encoberto a 200 ft → teto crítico.
- Visibilidade boa não "salva" teto para operação IFR (aproximação depende de mínimos).

### 3) Chuva fraca persistente com OVC alto

```text
METAR SBSP 042000Z 31011KT 8000 -RA SCT015 OVC080 23/21 Q1016=
```

**Análise:**

- **-RA** + vis 8 km: degradação moderada
- **SCT015** (não teto) e **OVC080** (teto 8000 ft): teto não é o fator limitante, mas pista molhada e vento podem ser.

---

## Erros comuns (que geram decisões ruins)

- Tratar **SCT** como teto: teto é **BKN/OVC**.
- Ignorar **xxxVyyy**: direção variável pode elevar componente cruzado real.
- "CAVOK = sempre bom": pode haver vento forte (no TAF) e NOTAM limitando operação.
- Não confrontar METAR com TAF recente (ou com SPECI): tendência pode ter mudado.
