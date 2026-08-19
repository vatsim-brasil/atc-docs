---
title: Operação na FIR Atlântico
icon: material/airplane-takeoff
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

O que você precisa fazer para atravessar a FIR Atlântico colaborando com o serviço da posição `SBAO_FSS`.

## O que muda

Na FIR Atlântico **não há vigilância por radar**[^1]. O controlador não vê sua aeronave: ele sabe onde você está porque você informou. Três consequências:

1. **Você é a fonte da informação.** Reporte atrasado é lacuna na consciência situacional do controlador.
2. **As separações são muito maiores**, medidas em minutos e dezenas de milhas.
3. **Nada é imediato.** Um pedido de nível depende de cálculo sobre estimados, não de uma imagem na tela.

## Antes do voo

- Planeje pelas rotas ATS do corredor EUR/SAM, ou entre os portões da AORRA.
- Confira o nível na tabela aplicável, em [Estrutura e setorização](../atc/estrutura.pt.md#niveis-de-cruzeiro).
- **Planeje velocidade em número Mach**, no item 15, formato `M` mais três algarismos, por exemplo `M082`[^2]. O Mach é a base da separação nesta FIR.

### No plano de voo

Declare **apenas o que sua aeronave realmente faz**. Declarar o que você não vai usar é pior do que não declarar.

| Onde       | O quê                                            | Para quê                                    |
| ---------- | ------------------------------------------------ | ------------------------------------------- |
| Item 10    | `W` se aprovado RVSM                             | Permite 1.000 pés entre o FL 290 e o FL 410 |
| Item 10    | `R` se aprovado PBN, com `PBN/` no item 18       | Base da separação lateral de 50 NM          |
| Item 10    | `J5`, `J6` ou `J7` se tiver CPDLC por satélite   | Habilita o enlace de dados                  |
| Item 10b   | `D1` se tiver ADS-C                              | Habilita a posição automática               |
| Item 18    | `SEL/` e o código SELCAL                         | Permite chamada seletiva                    |
| Item 18    | `EET/SBAO` e o tempo até a FIR                   | Ajuda a calcular seu estimado de entrada    |

Sem RVSM, insira `STS/NONRVSM`. Sem RNP 10, `RMK/NONRNP10`. Nos dois casos a separação aplicada a você será maior.

!!! info "Na simulação"
    Nada na rede verifica certificação, por isso o controlador vai confirmar com você no primeiro contato. **Responda com honestidade.** Se o seu add-on não tem CPDLC, diga: ele apenas aplicará outra mínima, e ninguém sai prejudicado.

### Enlace de dados

Se tiver CPDLC, faça logon em **`SBAO`** entre **10 e 25 minutos antes** de entrar na FIR[^3]. Use exatamente o mesmo indicativo e matrícula do plano de voo, ou o logon é rejeitado[^4]. Vindo de FIR com enlace, a conexão costuma passar sozinha; confira ao cruzar o limite.

## Contato inicial

Chame na frequência de [Estrutura e setorização](../atc/estrutura.pt.md#posicoes-na-vatsim). O órgão é **ATLANTICO CENTER**, ou **CENTRO ATLÂNTICO**.

```text
ATLANTICO CENTER, CALLSIGN, POSITION at TIME, LEVEL, MACH
```

Mesmo em ADS-C, **envie uma mensagem de posição em CPDLC na entrada da FIR**[^5]. Usando CPDLC, **não** faça cheque de SELCAL no primeiro contato, salvo se o controlador pedir[^6].

## Reportes de posição

```text
CALLSIGN, POSITION at TIME, LEVEL, MACH,
estimating NEXT POSITION at ESTIMATE, next ENSUING POSITION
```

!!! example "Exemplo"
    *"Atlantico Center, EXEMPLO 123, position NIMAX at 1412, flight level 370, Mach decimal 82, estimating KOSAX at 1448, next TEBRO."*

**Quando reportar:** nos pontos de notificação compulsória, ao cruzar os limites da FIR, sempre que o controlador pedir, e na AORRA a cada 10° de longitude[^7]. Com ADS-C funcionando, o reporte por voz não é necessário, salvo solicitação[^8].

**Estimados:** avise sempre que mudar mais de **2 minutos**[^9], por vento, velocidade ou desvio.

```text
CALLSIGN, revised estimate NEXT POSITION at ESTIMATE
```

Se o controlador atribuiu um Mach, ele entra no reporte e também na primeira chamada após qualquer mudança de frequência[^10].

## Nível e Mach

- Peça com bastante antecedência: o controlador recalcula a separação com todos na sua rota.
- Com Mach atribuído, **peça aprovação antes de mudar**. Se for inevitável, por turbulência, avise assim que fizer[^11].
- Não conseguindo manter o Mach numa subida ou descida, informe ao solicitar[^12].
- Em espaço RVSM, reporte ao atingir o nível autorizado[^13].

## SLOP

Prática padrão nesta FIR[^14]: deslocamento **somente à direita**, no eixo, 1 NM ou 2 NM, **nunca** mais que 2 NM nem à esquerda. **Não precisa de autorização nem de aviso ao controlador.** Os reportes continuam baseados na autorização vigente, não no deslocamento.

## Desvios e falhas

Não conseguindo cumprir a autorização, ou manter a precisão de navegação exigida, **informe imediatamente**[^15]. Ao pedir desvio meteorológico, diga de uma vez o lado, a distância e o tempo previsto fora da rota. Ao voltar, reporte o retorno com estimado revisado.

| Falhou   | O que fazer                                                                     |
| -------- | -------------------------------------------------------------------------------- |
| CPDLC    | Reverta para voz iniciando com `CPDLC FAILURE`                                   |
| Logon    | Confira indicativo e matrícula, corrija, refaça; persistindo, avise por voz[^4]  |
| Voz      | Use a CPDLC até restabelecer                                                     |
| Tudo     | Aplique os procedimentos de falha de comunicação das Regras do Ar, mantenha escuta na frequência do setor e em 123.45 MHz, e transmita posição e intenções[^16] |

Turbulência impedindo manter o nível: `CALLSIGN, UNABLE RVSM DUE TURBULENCE`. Ao recuperar: `CALLSIGN, READY TO RESUME RVSM`.

## Transferência

- `CONTACT UNIT on FREQ`: mude de frequência **e faça** a chamada inicial.
- `MONITOR UNIT on FREQ`: mude de frequência **sem** chamada inicial[^17].
- Se o controlador informar que não há órgão à frente, mantenha o último nível e velocidade autorizados e prossiga conforme o plano.

## Resumo

1. Planeje com número Mach e confira o nível.
2. Declare só as capacidades que você vai usar de fato.
3. Logon em `SBAO` de 10 a 25 minutos antes de entrar, se tiver CPDLC.
4. Reporte com hora, nível, Mach, próximo ponto com estimado e ponto seguinte.
5. Avise qualquer mudança de estimado maior que 2 minutos.

[^1]: **AIP-Brasil, ENR 1.6**.
[^2]: **MCA 100-11, item 2.2.6.1**.
[^3]: **AIP-Brasil, ENR 3.5, itens 9.2.1 e 9.2.2**.
[^4]: **AIP-Brasil, ENR 3.5, itens 9.2.4 e 9.2.5**.
[^5]: **AIP-Brasil, ENR 3.5, item 9.5.2.1**.
[^6]: **AIP-Brasil, ENR 3.5, item 9.5.1.2**.
[^7]: **ICA 100-37, Art. 173**, e **AIP-Brasil, ENR 3.5, item 8.8.2**.
[^8]: **ICA 100-37, Art. 179**, e **AIP-Brasil, ENR 3.5, item 9.5.2.2**.
[^9]: **AIP-Brasil, ENR 3.5, item 9.5.2.5**.
[^10]: **ICA 100-37, Art. 180**.
[^11]: **ICA 100-37, Art. 375**.
[^12]: **ICA 100-37, Art. 376**.
[^13]: **AIP-Brasil, ENR 3.5, item 7.5.1**.
[^14]: **AIP-Brasil, ENR 3.5, item 7.9**.
[^15]: **AIP-Brasil, ENR 3.5, item 8.8.1**.
[^16]: **AIP-Brasil, ENR 1.1, item 4.1.1, e ENR 1.8, item 2.4.1**.
[^17]: **AIP-Brasil, ENR 3.5, itens 9.4.1.5 e 9.4.1.6**.
