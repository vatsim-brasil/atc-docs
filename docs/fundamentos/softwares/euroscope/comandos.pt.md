---
  title: Guia de Comandos
  description: Os atalhos de teclado e os comandos de linha do EuroScope, com um quiz dos principais
  icon: material/keyboard-outline
---

--8<-- "includes/abreviacoes.md"

# Guia de Comandos

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

## Treine os atalhos

Seis situações do dia a dia. Escolha o atalho certo para cada uma.

<div class="vb-quiz" markdown>

<div class="vb-pergunta" data-resposta="2" markdown>

O piloto chamou na sua frequência e o tráfego está branco (relacionado). Qual tecla você usa para assumi-lo?

1. `F4`
2. `F3`
3. `F9`

<div class="vb-explica" markdown>
`F3` assume o tráfego ou aceita a transferência. `F4` faz o caminho contrário: inicia ou rejeita uma transferência.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Você autorizou a subida para o FL150. Como registra isso na etiqueta?

1. `F5` + `150` + clique na etiqueta
2. `.qs 150`
3. `F8` + `150` + clique na etiqueta

<div class="vb-explica" markdown>
`F8` altera o **nível autorizado** (CFL). `F5` muda o nível final do plano de voo, que é outra coisa.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Quer acompanhar a distância entre dois tráfegos que vão se cruzar. Qual comando prevê o ponto de maior aproximação?

1. `F1 + S` (`.sep`)
2. `F1 + D` (`.distance`)
3. `F1 + F` (`.find`)

<div class="vb-explica" markdown>
`.sep` prevê a menor distância entre duas aeronaves. `.distance` mostra a distância atual até outra aeronave ou ponto.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Um tráfego chamou em outra frequência por engano e você quer que ele chame na sua. O que usa?

1. `.wallop`
2. `.contactme`, atalho `HOME`
3. `.break`

<div class="vb-explica" markdown>
`.contactme` manda ao piloto uma mensagem de texto pedindo contato na sua frequência. `.wallop` chama os supervisores.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Como adicionar o METAR de SBKP à tela?

1. `.metar SBKP`
2. `F1 + M` e clique no aeródromo
3. `F2` + `SBKP`

<div class="vb-explica" markdown>
`F2` seguido do código ICAO adiciona ou remove METARs.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Precisa de alguém para render você daqui a pouco. Como avisar os outros controladores sem escrever no chat?

1. `.break`
2. `.nobreak`
3. `.showvis`

<div class="vb-explica" markdown>
`.break` muda a cor do seu indicativo para os outros controladores. `.nobreak` desfaz o aviso.
</div>

</div>

</div>

## Referência

Para explicações completas, consulte a [referência de comandos do EuroScope](https://www.euroscope.hu/wp/command-line-reference/).
