---
  title: Quiz do Controlador
  description: Perguntas rápidas para conferir os conceitos básicos antes do curso de S1
  icon: material/head-question-outline
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Quiz do Controlador

Dez perguntas sobre o que você viu na trilha. Não vale nota: é para você descobrir o que precisa revisar antes do curso de S1.

<div class="vb-quiz" markdown>

<div class="vb-pergunta" data-resposta="2" markdown>

Você acabou de criar sua conta na VATSIM. Qual é o seu rating?

1. S1
2. OBS
3. Nenhum, até fazer a prova

<div class="vb-explica" markdown>
Toda conta começa como **OBS** (observador): você pode conectar com um indicativo `_OBS` para ver e ouvir, sem transmitir. Veja a [escada de ratings](ratings.pt.md).
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Quais posições o rating S1 libera?

1. Só `_DEL`
2. `_DEL`, `_GND` e `_TWR`
3. `_DEL` e `_GND`

<div class="vb-explica" markdown>
O S1 libera **Tráfego** e **Solo**. A Torre exige o S2.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Quem emite a autorização de tráfego (rota, nível, saída e código transponder) quando todas as posições do aeródromo estão ocupadas?

1. O Tráfego (`_DEL`)
2. O Solo (`_GND`)
3. A Torre (`_TWR`)

<div class="vb-explica" markdown>
A autorização é o trabalho do **Tráfego**. Sem ele on-line, a autorização passa para a próxima posição acima, por top-down.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Só o `SBXP_APP` (Controle São Paulo) está on-line. Um piloto em Guarulhos quer a autorização de tráfego. Quem atende?

1. Ninguém: sem Tráfego on-line, o piloto decola sem autorização
2. O piloto deve esperar o Tráfego conectar
3. O próprio `SBXP_APP`, pela cobertura top-down

<div class="vb-explica" markdown>
Pela **cobertura top-down**, a posição on-line cobre as posições vazias abaixo dela. O APP faz o papel de Torre, Solo e Tráfego nos aeródromos que cobre. Veja [Posições e órgãos](posicoes.pt.md#e-se-a-posicao-estiver-vazia).
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Qual posição autoriza a aeronave a entrar na pista e decolar?

1. O Solo
2. A Torre
3. O Controle

<div class="vb-explica" markdown>
A **Torre** é a dona da pista. O Solo leva a aeronave até o ponto de espera, e a Torre autoriza o alinhamento e a decolagem.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Qual é o indicativo em português da posição `_APP`?

1. Controle
2. Aproximação
3. Centro

<div class="vb-explica" markdown>
No Brasil, o APP é chamado de **Controle**: *Controle São Paulo*, *Controle Brasília*. **Centro** é o `_CTR`.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Para que serve o ATIS?

1. Para o controlador conversar com os outros controladores
2. Para o piloto enviar o plano de voo
3. Para informar pista em uso, vento, condições meteorológicas e avisos do aeródromo

<div class="vb-explica" markdown>
O **ATIS** é uma gravação contínua com as informações do aeródromo. O piloto escuta antes da primeira chamada e informa a letra que recebeu. O controlador a mantém com o [vATIS](../softwares/vatis/index.pt.md).
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Você vai encerrar a sessão e não há ninguém on-line acima de você. O que diz aos pilotos na sua frequência?

1. Nada: ao desconectar, eles percebem
2. Que o serviço está encerrado e que monitorem a UNICOM, 122.800
3. Que aguardem na frequência até outro controlador conectar

<div class="vb-explica" markdown>
Sem ATC on-line, o piloto usa a frequência de tráfego da rede, a **UNICOM 122.800**. Oriente cada um antes de desconectar.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Qual destes requisitos vale para o S3, mas não para o S1?

1. Horas mínimas de conexão em `_TWR` e de *solo trainee* em `_APP`
2. Aprovação em prova teórica
3. Treinamento com mentor

<div class="vb-explica" markdown>
Prova teórica e mentor valem para todos os ratings. O S3 soma **10 horas** em `_TWR` como S2 e **10 horas** de *solo trainee* como `_APP`, além do *check* prático.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

O piloto cotejou o código transponder errado. O que você faz?

1. Nada, o EuroScope corrige sozinho
2. Espera ele decolar para corrigir com o Controle
3. Corrige na hora e pede novo cotejamento

<div class="vb-explica" markdown>
O cotejamento serve justamente para pegar erros. Corrija imediatamente: *"Negativo, transponder QUATRO ZERO TRÊS CINCO"*, e confirme que ele repetiu certo.
</div>

</div>

</div>

Quer ver o outro lado da frequência? Experimente o [simulador de rádio do piloto](../piloto/radio.pt.md) no modo *Praticar como controlador*.
