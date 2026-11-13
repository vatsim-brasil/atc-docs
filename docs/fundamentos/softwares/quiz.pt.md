---
  title: Quiz dos Softwares
  description: Perguntas rápidas sobre o EuroScope, o TrackAudio, o vATIS e o vacs
  icon: material/head-question-outline
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Quiz dos Softwares

Doze perguntas sobre a estação do controlador. Não vale nota: é para você descobrir o que precisa revisar antes de conectar.

<div class="vb-quiz" markdown>

<div class="vb-pergunta" data-resposta="2" markdown>

Qual programa deve conectar à rede primeiro?

1. O TrackAudio
2. O EuroScope
3. O vATIS

<div class="vb-explica" markdown>
O **EuroScope** conecta primeiro. O TrackAudio e o vATIS dependem da conexão dele. Veja [a ordem de conexão](index.pt.md#a-ordem-de-conexao).
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Você vai controlar `SBCT_GND`. Qual perfil do EuroScope abre?

1. `radar`
2. Qualquer um, os dois têm as mesmas ferramentas
3. `solo`

<div class="vb-explica" markdown>
O perfil **solo** é feito para `DEL`, `RMP`, `GND` e `TWR`, com o Ground Radar Plugin. O **radar** é para `APP` e `CTR`, com o TopSky.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Você estava em `SBCT_TWR` e vai abrir uma posição em outra FIR. O que faz?

1. Fecha o EuroScope e abre o perfil da nova FIR
2. Carrega o novo setor pelo `OPEN SCT`
3. Só troca o indicativo na janela de conexão

<div class="vb-explica" markdown>
Carregar outro setor com o programa aberto **não basta**. É preciso reiniciar o EuroScope no perfil da nova FIR.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Você clicou em `CONNECT` no TrackAudio e a sua frequência apareceu. Os pilotos já ouvem você?

1. Sim, o TrackAudio habilita a frequência sozinho
2. Não, é preciso marcar `RX` e `TX` à mão
3. Só depois de publicar o ATIS

<div class="vb-explica" markdown>
O TrackAudio **não habilita** as frequências sozinho. Marque `RX` para ouvir e `TX` para transmitir.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

O botão `TX` fica laranja. O que isso indica?

1. Que há um piloto transmitindo
2. Que a frequência está com problema
3. Que você está transmitindo, com o PTT apertado

<div class="vb-explica" markdown>
`TX` laranja é **você** falando. Quando é outra estação transmitindo, quem fica laranja é o `RX`.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Você controla `SBBS_CTR` e dois pilotos em pontos distantes da FIR não se ouvem. O que liga no TrackAudio?

1. O `XC`, com o clique direito no botão `XCA`
2. O `SPK`
3. O `XCA`, com o clique esquerdo

<div class="vb-explica" markdown>
Com vários transceptores, cada piloto ouve só o mais próximo. O **XC** (clique direito) acopla os transceptores **da mesma frequência**. O **XCA** (clique esquerdo) junta frequências **diferentes** e deve ser usado com cautela.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Qual tecla assume um tráfego ou aceita uma transferência no EuroScope?

1. `F4`
2. `F3`
3. `F8`

<div class="vb-explica" markdown>
`F3` assume. `F4` inicia ou rejeita uma transferência, e `F8` altera o nível autorizado. Veja o [guia de comandos](euroscope/comandos.pt.md).
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Você quer corrigir uma frequência errada no perfil do vATIS da sua FIR. O que faz?

1. Edita o perfil no `ATIS Configuration`
2. Apaga o perfil e cria um novo
3. Abre uma sugestão no repositório do portal

<div class="vb-explica" markdown>
Os perfis da Vatsim Brasil **se atualizam sozinhos**, e alterações locais são sobrescritas na próxima atualização. A correção vai para o [repositório](https://github.com/vatsim-brasil/atc-docs).
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

A letra do ATIS começou a piscar no vATIS. O que aconteceu?

1. Saiu um METAR novo e o ATIS foi atualizado
2. O ATIS desconectou
3. Outro controlador assumiu a estação

<div class="vb-explica" markdown>
A letra pisca a cada **atualização** pelo METAR. Clique uma vez nela para confirmar que você viu.
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Em que ordem você encerra a sessão?

1. EuroScope, TrackAudio, vacs, vATIS
2. vATIS, vacs, TrackAudio, EuroScope
3. Tanto faz, desde que todos sejam desconectados

<div class="vb-explica" markdown>
Na **ordem inversa** da conexão: primeiro o ATIS, depois a linha e o rádio e, por último, o EuroScope. Antes de tudo, transfira os tráfegos.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Você clica na tecla `SBGR_TWR` no vacs, mas não há ninguém na Torre de Guarulhos. O `SBXP_APP` está on-line. O que acontece?

1. A chamada falha: a Torre está fechada
2. Toca para todos os controladores da FIR
3. Toca no `SBXP_APP`, que cobre a Torre por top-down

<div class="vb-explica" markdown>
O vacs liga para o **setor**, e a chamada vai para quem o cobre no momento. Veja [como funciona](vacs/index.pt.md#como-funciona).
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Você atendeu uma chamada no vacs e usa a mesma tecla para o rádio e a linha. Quando começa a falar?

1. Imediatamente, assim que clicar na tecla
2. Quando o indicador da chamada ficar verde
3. Depois de desligar o TrackAudio

<div class="vb-explica" markdown>
Antes do verde, o PTT ainda pode **sair na frequência**. Espere o indicador verde ou o som de início da chamada.
</div>

</div>

</div>

Quer revisar? Volte à [trilha de instalação](preparacao.pt.md) ou ao [checklist de conexão](sessao.pt.md).
