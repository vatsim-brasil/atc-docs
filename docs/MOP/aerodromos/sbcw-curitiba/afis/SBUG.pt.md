---
title: SBUG - Uruguaiana
tags:
  - Aeródromo
  - Não-Controlado
  - SBCW
---

--8<-- "includes/abreviacoes.md"

## :material-information-outline: Dados Gerais
|                              | Informações                                 |
|------------------------------|---------------------------------------------|
| **Nome do aeródromo**        | Uruguaiana - Rubem Berta |
| **Tipo de Operação**         | Internacional e Público |
| **Altitude de transição** | 3000 pés |
| **Elevação** | 256 pés (78 m) |

## :material-monitor-dashboard: Informações Úteis

=== ":material-monitor-dashboard: Painel"
    Selecione uma das ferramentas nas abas acima (Cartas, Meteorologia ou Tráfego) para acessar as informações do aeródromo.

=== ":material-file-document: Cartas Aeronáuticas"
    <iframe class="chart-iframe" src="https://api.chartfox.org/v2/interfaces/airport/SBUG?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5YjAzYTg5Yi0yZTY1LTQ1MzAtOTRhMi1iNTE1OWU1NzE3M2EiLCJqdGkiOiI4MDgyNjZhYWZhZDg1ZDJmNzZmODMwOTM0MTI1YTU3M2UyMjExMDU2MDI4ODJhNGQwMDdjMmNlNDRmNDRiNDcxOTVhNzYyMzg0YTFjYTc5MiIsImlhdCI6MTc4MjY4Mjk4OS40MjEzODIsIm5iZiI6MTc4MjY4Mjk4OS40MjEzODcsImV4cCI6MjQxMzgzNDk4OS40MTQ2MzgsInN1YiI6ImNhOWU2ODJmLTk3MmUtNDQwMC1hZTk0LTIwMTNjNTI1MWQ5NiIsInNjb3BlcyI6WyJpbnRlcmZhY2U6YWlycG9ydENoYXJ0cyJdfQ.fpe9LYMNVLeGlOP91pNic8qD0vluZyJdKIuQVnSwLBrGKxf8WtLWXN37D51AuR1qKMIghQDJ2rhf3NYiuYF9DeSTU84vjEjL8rlyMcRrsa8KJxRxlmGxQ5HWwMgFTLbEN61_ocfha66bXnHW-6dfhsJ0iC86PxAnYhFdggo2eUeExWQ_oZF2cTMg2x6xIm37cBcYL9LZN8T43NAu0wlN3qjyJUIUmPU1KD96FgohPJIn8AqI-h8CoCISnOfOITqhK4EgOIIV9viiXcBqv1CzSpYypOJcFFf2XQTDvfK93XnUBJPTo-Y_meB8XqFYfkwdQXgs6O-JCef9pojnNKRNGtgnVuiOXvI2RD7IAPPEJxv8yZ7W1BIciyMGHbHV8ZF959M4XL6n2oKD-vsE-tJe3JBsbP6MPc14gCmPw_zQ-nCK3kGS0rhoZHPcmRl0Gb-OYgn9HWybnI9m4-BOOoqtWkaqQt1nwhIFVTcwaBXy1jndU3I-0uyyBY88_GQQBSZ85sOgSmDVJOkHOrnDV6nxrLYRtUQigNfJ-m7IFfOQoRjFmtoHcswhjfrrHEI1laNSsZg6I_9eO-S6ccyxSS5QJtEaOM-wOlM6rDsswny2Q5QxCAL9VlZT3YMzz5ZCpprK_YpNmQoT-iGAdI0w2CJssDAGGreggc5t8XpwpdSUsfo"></iframe>

=== ":material-weather-partly-cloudy: Meteorologia"
    <div id="metar-taf-container" data-airport="SBUG" class="weather-card-container">
        <div class="weather-card metar" id="metar-content">
            Carregando o METAR<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
        <div class="weather-card taf" id="taf-content">
            Carregando o TAF<span class="loading-dots"><span>.</span><span>.</span><span>.</span></span>
        </div>
    </div>

=== ":material-radar: Tráfego VATSIM"
    [:material-radar: Tráfego](https://vatsim-radar.com/?airport=SBUG){ .md-button .btn-vatsim-custom target="_blank" style="flex: 1; min-width: 150px; text-align: center; margin: 0; display: inline-flex; align-items: center; justify-content: center; gap: 8px;align:center;" }

## :material-routes: Pistas
| Pista | Preferencial  | ILS                                         | Circuito   |
| :---: | :--- | :---: | :---: |
| **10** | -             | :fontawesome-solid-circle-xmark:{ .cornot } | Padrão     |
| **28** | -             | :fontawesome-solid-circle-xmark:{ .cornot } | Padrão     |

## :material-headset: Órgãos ATC
| Código     | Abrev. | Indicativo de Chamada | Frequência | Observações |
| ---------- | ------ | --------------------- | ---------- | ----------- |
| **SBUG_R_TWR** | `RUG` | Rádio Uruguaiana | **118.100** |  |

### DCL / CPDLC
- [ ] Não há disponível serviço de DCL no aeródromo.

## :material-airplane-takeoff: Operações

### Regulamentos do Aeródromo

- AFIS Uruguaiana operado remotamente a partir das dependências do ACC Curitiba (CINDACTA II). Área de responsabilidade correspondente ao espaço aéreo ATS classe G.
- PROC específicos para contingências de COM:
    1. Usar a FREQ da RDO como FCA e ajustar o código 7600 no transponder;
    2. Realizar IAC IFR se obtiver INFO MET do AD via ACC/AFIS; caso NEG, NO AUTH LDG IFR;
    3. Realizar SID se obtiver INFO MET do AD; caso NEG, NO AUTH DEP IFR;
    4. Atentar para as demais regras da ICA 100-12 para falha de COM.
- OPS fora do HR do AD restritas a aeromédico, segurança pública e operações especiais. ACFT da aviação geral não são autorizadas fora do HR publicado.
- OBS ACFT agrícola em voo próximo ao AD.
- ACFT no circuito de TFC e na RWY de LDG: OBS TFC em PROC IFR na APCH e DEP.

### Pátios e Pistas de Taxi

- RWY 10/28: giro de 180° de ACFT com PMD acima de 40T somente nas THR.
- O pátio não dispõe de pontos de amarração.

### Informação Adicional

- OBS concentração de pássaros (quero-quero, tapicuru, curicaca, maria-faceira) no circuito de TFC, SECT APCH RWY 10/28 e nos gramados laterais da RWY 10/28.

## :material-sign-direction: Posições de Parada
| Pátio     | Posições  | Classificação                         |
| :---: | :---: | :--- |
| **1** | ANY       | Doméstico / Internacional / Aviação Geral e Executiva |