---
  title: Utilização
  description: Como fazer e receber chamadas de coordenação no vacs, com conferências, a página do telefone e o rádio
  icon: material/phone-in-talk
---

--8<-- "includes/abreviacoes.md"

# Utilização

Esta página mostra o vacs numa sessão de controle: conectar, ligar, atender, fazer conferências e encerrar. Ela parte do ponto em que a [instalação](instalacao.pt.md) já foi feita.

## Conectando

``` mermaid
flowchart LR
    A[EuroScope conectado<br/>e frequência primária] --> B[TrackAudio<br/>conectado]
    B --> C[Connect<br/>no vacs]
    C --> D[Teclas dos setores<br/>on-line ativas]
```

1. Conecte a posição no [EuroScope](../euroscope/utilizacao.pt.md#conectando-a-rede) e marque a frequência primária. Sem isso, o vacs não reconhece a sua estação.
2. Conecte o [TrackAudio](../trackaudio/utilizacao.pt.md), se usa a integração de rádio.
3. No vacs, clique em **Connect**.

## A tela

A tela principal é formada por **teclas de acesso direto**, uma por setor. A disposição vem do cadastro da Vatsim Brasil: em abas, na barra inferior, ou num mapa (*GEO*). Uma tecla fica **clicável** quando o setor está on-line no vacs e na rede.

Além das teclas, você vai usar:

| Botão | O que faz |
| --- | --- |
| **PRIO** | Torna a próxima chamada prioritária |
| **CONF** | Convida mais um setor para a chamada em andamento |
| **PLAY BACK** e **SAY AGAIN** | Repetem as transmissões recebidas no rádio |
| **RADIO PRIO** | Dá prioridade ao rádio e silencia o microfone da linha |
| **END** | Desliga a chamada, na barra inferior |
| Telefone | Abre a lista telefônica, as últimas chamadas e o teclado, no lado direito |

O indicador no canto superior esquerdo mostra o estado da linha: **laranja** chamando ou tocando, **verde** conectado.

## Fazendo uma chamada

1. **Prepare a mensagem** antes de ligar.
2. Clique na tecla do setor. A chamada toca para quem cobre aquele setor agora, inclusive por top-down.
3. Espere o indicador ficar **verde** (ou o som de início da chamada) e fale.
4. Ao terminar, clique em **END**.

!!! warning "Não fale antes do verde"
    Com a mesma tecla para o rádio e a linha, apertar o PTT logo depois que a chamada conecta pode **transmitir na frequência**. Espere o indicador verde.

Se ninguém atender, a tecla pisca em vermelho e a barra superior mostra **REMOTE TARGET DID NOT ANSWER**. A chamada sem resposta é encerrada sozinha depois de 60 segundos.

### De qual estação você está ligando

Se você cobre mais de um setor, como um APP que cobre as torres da TMA, o vacs escolhe sozinho a estação de origem da chamada. Para escolher outra:

- **um clique** num dos seus setores define a origem só para a **próxima** chamada (laranja-claro);
- **dois cliques** fixam a origem (laranja-escuro) até você clicar de novo.

### Chamada prioritária

Para uma coordenação urgente, clique em **PRIO** e depois na tecla do setor. Do outro lado, a chamada aparece com borda amarela e um toque diferente. Use só quando a coordenação não pode esperar.

## Recebendo uma chamada

Quando alguém liga, a tecla do setor que chama **pisca em verde-escuro** e o toque soa. Clique nela para atender, ou use o atalho **Accept first call**.

- Se houver mais de uma chamada tocando, escolha qual atender.
- Uma conferência aparece como **CONF** na tecla.
- Não há botão de recusar: se você não puder atender, deixe tocar, e quem ligou recebe o aviso de que você não atendeu.
- Atender uma segunda chamada desliga a que está em andamento. Isso pode ser mudado em **Settings › Call**, na opção **End active call on accept**.

## Conferência

Para juntar um terceiro setor a uma chamada em andamento:

1. Clique em **CONF**. Ele pisca em azul-escuro.
2. Clique na tecla do setor que quer convidar.

Quem adicionou o terceiro participante é o **líder**. Só ele convida e remove participantes, e se ele sair, a conferência termina para todos. Os outros participantes saem com **END** sem derrubar a chamada. A conferência comporta até oito controladores.

## A página do telefone

O botão de telefone, à direita, abre quatro seções:

| Seção | Para que serve |
| --- | --- |
| **Dir.** | Lista telefônica: todos os controladores conectados ao vacs, inclusive os que não têm tecla na sua tela. Pesquise e clique em **Call**. |
| **Call List** | As últimas chamadas: verde as recebidas, azul as feitas, com X vermelho as que não completaram. |
| **Dial Pad** | Liga para um controlador pelo CID. |
| **Ign.** | Lista de CIDs ignorados, que não tocam para você. |

## Rádio e repetição

Com a integração do TrackAudio, a página **Radio** do vacs mostra as suas frequências, com `Rx` e `Tx` e os acoplamentos **CPL** e **FAST CPL**. Ela é um atalho para o TrackAudio, que continua sendo o seu rádio.

- **RADIO PRIO**: enquanto ligado, o microfone da linha fica mudo, e você pode falar no rádio sem que a chamada ouça. Desliga sozinho no fim de cada chamada.
- **PLAY BACK**: lista as transmissões recebidas no rádio para ouvir de novo. Ative antes em **Enable radio playback**, nas configurações avançadas. Funciona no Windows e no Linux; no macOS, não.
- **SAY AGAIN**: repete a última transmissão recebida. Útil quando o piloto falou junto com a linha.

As chamadas da linha não são gravadas.

## Como falar na linha

As mensagens entre órgãos seguem o Anexo II do MCA 100-16:

- ao atender, diga o nome do seu órgão e "prossiga" ou "aguarde";
- prepare a mensagem antes de ligar e confira se está falando com o órgão certo;
- quando não houver cotejamento, confirme com "ciente" ou "entendido".

| Quem | Mensagem |
| --- | --- |
| SETOR 1 | "Transferência do BRA 4177, passando FL 160, sul de Campinas, solicita direto Bonsucesso." |
| SETOR 2 | "Autorizado Bonsucesso, contato em 129,75." |
| SETOR 1 | "Ciente, chamará em 129,75." |

Mais modelos de estimados, pedidos e transferências estão na [Fraseologia do Manual de Coordenação e Transferência](../../../documentos/manuais/coordenacao-transferencia/05-fraseologia.pt.md#mensagens-entre-orgaos).

## Encerrando

1. Termine as chamadas em andamento com **END**.
2. Desconecte o vacs antes de desconectar o TrackAudio e o EuroScope.

## Quando algo dá errado

??? failure "A tecla do setor está cinza"
    O setor não está on-line, ou o controlador dele não está conectado ao vacs. Procure-o na lista telefônica (**Dir.**). Se não estiver lá, coordene pelo chat.

??? failure "Os outros controladores não conseguem me ligar"
    O vacs não reconheceu a sua posição. Confira se você conectou com o indicativo e a frequência primária do MOP. Se estiverem certos, a posição pode estar faltando no cadastro: avise a equipe da Vatsim Brasil.

??? failure "A chamada conecta e cai, ou nunca conecta"
    Firewall, antivírus ou VPN podem bloquear a conexão direta. Ligue **Always relay calls** em **Settings › Call**.

??? failure "Os atalhos não funcionam com o EuroScope em foco"
    No Windows, se o EuroScope ou o TrackAudio rodam como administrador, rode o vacs como administrador também, ou nenhum deles.

??? failure "O ponto do Endpoint está amarelo"
    O TrackAudio está aberto, mas não conectado à voz. Clique em `CONNECT` no TrackAudio.

??? failure "O outro controlador ouve eco"
    O vacs não tem cancelamento de eco. Use fone de ouvido em vez de alto-falante.

## Para saber mais

- [Documentação oficial do vacs](https://docs.vacs.network) (em inglês);
- [Estado dos servidores](https://status.vacs.network);
- [Cadastro dos setores do Brasil](https://github.com/vacs-project/vacs-data/tree/main/dataset/SB), no repositório vacs-data.
