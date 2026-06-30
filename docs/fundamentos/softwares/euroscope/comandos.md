---
  title: Guia de Comandos
---

--8<-- "includes/abreviacoes.md"

#

![Fundamentos - Euroscope - Comandos](img/head-euroscope-comandos.png)

Este guia reúne os principais atalhos de teclado e comandos de linha do **EuroScope**.

## Atalhos principais

| Tecla | Parâmetros | Ação |
|---|---|---|
| `F2` | Código ICAO de quatro letras | Adiciona ou remove METARs. |
| `F3` | Clique na etiqueta da aeronave | Assume o rastreamento da aeronave ou aceita uma transferência. |
| `F4` | Clique na etiqueta da aeronave | Abandona o rastreamento, rejeita uma transferência ou inicia uma transferência. |
| `F5` | Altitude em centenas + clique na etiqueta | Altera a altitude final, conforme o plano de voo. |
| `F6` | Nenhum | Exibe a ficha de progresso de voo da aeronave atual. |
| `F7` | Nenhum | Alterna entre as visualizações de radar abertas. |
| `F8` | Altitude em centenas + clique na etiqueta | Altera a altitude temporariamente atribuída. |
| `F9` | Clique na etiqueta | Atribui automaticamente um código transponder. |
| `F9` | Código de quatro dígitos + clique na etiqueta | Atribui manualmente o código transponder informado. |
| `F9` | `V`, `R` ou `T` + clique na etiqueta | Define o tipo de comunicação: voz, somente recepção ou texto. |
| `F11` | Nenhum | Aproxima o radar. |
| `F12` | Nenhum | Afasta o radar. |

## Comandos acessados pela tecla `F1`

| Teclas | Comando | Parâmetros | Ação |
|---|---|---|---|
| `F1 + A` | `.am` | Clique na etiqueta da aeronave | Altera o plano de voo. |
| `F1 + C` | `.chat` | Clique na etiqueta da aeronave | Abre a janela de conversa. |
| `F1 + D` | `.distance` | Clique em uma aeronave e depois em outra aeronave ou ponto | Exibe continuamente a distância atualizada entre uma aeronave e outra aeronave ou ponto. |
| `F1 + F` | `.find` | Digite uma aeronave ou fixo | Exibe uma linha do centro da tela até o ponto informado. |
| `F1 + P` | `.point` | Identificador do controlador + clique na etiqueta da aeronave | Destaca a aeronave na tela do controlador especificado, realizando um *point out*. |
| `F1 + S` | `.sep` | Clique na etiqueta de duas aeronaves | Exibe continuamente a previsão do ponto de maior aproximação entre as aeronaves. |
| `F1 + 0` | - | Nenhum | Fecha a visualização ASR atual. |
| `F1 + 1` até `F1 + 9` | - | Nenhum | Abre as visualizações ASR predefinidas nas configurações gerais. |

## Comandos de linha

- `.break`

Altera a cor do seu indicativo, conforme exibido aos demais controladores, para indicar que você precisa de uma pausa ou substituição.

```text
.break
```

- `.center`

Centraliza a visualização atual do radar em um fixo ou aeronave.

```text
.center FIXO_OU_AERONAVE
```

- `.contactme`

Envia uma mensagem de texto ao piloto solicitando contato na frequência atual.

```text
.contactme
```

Atalho: `HOME`.

- `.nobreak`

Cancela o comando `.break` anterior.

```text
.nobreak
```

- `.qs`

Altera o conteúdo do *scratchpad* da aeronave.

```text
.qs CONTEUDO
```

Atalho: `INS`.

- `.rings`

Exibe anéis de distância em torno de um ponto central, informando o espaçamento em milhas e a quantidade de anéis.

```text
.rings CENTRO ESPACAMENTO QUANTIDADE
```

Executar o comando sem parâmetros remove os anéis:

```text
.rings
```

- `.showvis`

Exibe a área na qual as informações das aeronaves da VATSIM estão visíveis.

```text
.showvis
```

- `.vis`

Define até quatro centros para a área de visibilidade da VATSIM.

```text
.vis FIXO1 FIXO2 FIXO3 FIXO4
```

- `.vis1`, `.vis2`, `.vis3` e `.vis4`

Define individualmente cada centro da área de visibilidade da VATSIM.

```text
.vis1 FIXO
.vis2 FIXO
.vis3 FIXO
.vis4 FIXO
```

- `.wallop`

Envia uma mensagem para todos os supervisores conectados.

```text
.wallop MENSAGEM
```

## Referência

Para explicações completas, consulte a [referência de comandos do EuroScope](https://www.euroscope.hu/wp/command-line-reference/).
