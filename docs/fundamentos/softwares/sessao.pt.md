---
  title: Ligar e Desligar
  description: Checklist interativo para conectar e desconectar o EuroScope, o TrackAudio, o vacs e o vATIS, com soluções para os problemas mais comuns
  icon: material/clipboard-check-outline
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Ligar e Desligar

A ordem importa: o EuroScope conecta primeiro e desconecta por último. Use este checklist em cada sessão. As marcações ficam salvas neste navegador, e você pode limpá-las para a próxima vez.

<div class="vb-checklist" data-chave="softwares-sessao" markdown>

### Antes de conectar

- [ ] Conferi no Sector File Manager se os arquivos de setor estão no AIRAC atual.
- [ ] Abri o EuroScope no perfil da FIR certa: `solo` para aeródromo, `radar` para APP e CTR.
- [ ] Conferi o METAR (`F2`) e a pista em uso pelo MOP.
- [ ] Vi na lista de controladores quem já está on-line.
- [ ] Coloquei o fone e testei o PTT.

### EuroScope

- [ ] Conectei com o indicativo da posição, meu CID, *facility* e rating corretos.
- [ ] Marquei a frequência da posição como primária (`Prim`).
- [ ] Preenchi as linhas do *Controller ATIS*.

### TrackAudio

- [ ] O indicativo apareceu no topo e cliquei em `CONNECT`.
- [ ] Marquei `RX` e `TX` da minha frequência.
- [ ] Liguei o `XC` (clique direito no `XCA`), se a posição usa mais de um transceptor.

### vacs

- [ ] Cliquei em **Connect** e as teclas dos setores on-line acenderam.
- [ ] O ponto do **Endpoint** está verde, com a integração do TrackAudio ligada.

### vATIS (se a posição tiver ATIS)

- [ ] Escolhi a estação e o *preset* da pista em uso.
- [ ] Conferi as condições do aeródromo e os NOTAMs da sessão anterior.
- [ ] Cliquei em `CONNECT` e confirmei a letra.

### Ao encerrar

- [ ] Transferi os tráfegos ou orientei os pilotos a monitorar a UNICOM (122.800).
- [ ] Avisei no canal `ATC` que vou desconectar.
- [ ] Desconectei o ATIS no vATIS.
- [ ] Desconectei o vacs.
- [ ] Desconectei o TrackAudio.
- [ ] Desconectei o EuroScope (`Disconnect`).

</div>

## Quando algo dá errado

??? failure "O TrackAudio mostra *No VATSIM connection detected!*"
    O EuroScope não está conectado à rede, ou a conexão caiu. Conecte o EuroScope primeiro: o TrackAudio detecta a posição sozinho e o botão `CONNECT` fica verde.

??? failure "Não ouço nada na frequência"
    Confira se o `RX` da frequência está marcado. Depois, nas configurações do TrackAudio, confira se a saída primária é o seu fone. O botão `RX` fica laranja quando há alguém transmitindo: se ele acende e você não ouve, o problema é a saída de áudio.

??? failure "Os pilotos não me ouvem"
    O `TX` precisa estar marcado, e o botão fica laranja enquanto você aperta o PTT. Se ele não muda de cor, revise a tecla de PTT nas configurações. Se muda, revise a entrada de áudio (o microfone).

??? failure "Pilotos em lados opostos da área não se ouvem"
    Com vários transceptores na mesma frequência, cada piloto ouve só o mais próximo. Ligue o `XC`, com o clique direito no botão `XCA`, para acoplar os transceptores.

??? failure "A sessão de voz caiu com *Callsign changed during an active session*"
    O TrackAudio encerra a voz quando o indicativo muda no EuroScope ou quando a conexão cai. Reconecte o EuroScope, se preciso, e clique de novo em `CONNECT` no TrackAudio, marcando `RX` e `TX`.

??? failure "A rede recusou a conexão do EuroScope"
    Confira CID, senha, *facility* e rating. A rede não aceita uma posição acima do seu rating: com S1, só `_DEL`, `_GND` e `_OBS`.

??? failure "Troquei de FIR e o setor ficou estranho"
    Carregar outro setor com o EuroScope aberto não basta. Feche o programa e abra o perfil da nova FIR.

??? failure "Ninguém consegue me ligar pelo vacs"
    O vacs reconhece a posição pelo indicativo e pela frequência primária. Confira os dois no EuroScope, conforme o MOP. Veja mais soluções em [vacs: utilização](vacs/utilizacao.pt.md#quando-algo-da-errado).

??? failure "Apertei o PTT e saí na frequência em vez da linha"
    Com a mesma tecla para o rádio e o vacs, espere o indicador da chamada ficar verde antes de falar.

??? failure "A letra do ATIS está piscando"
    Saiu um METAR novo e o vATIS atualizou o ATIS. Clique uma vez na letra para confirmar que viu a atualização.

## Para ir além

- [Sua primeira sessão](../controlador/primeira-sessao.pt.md), o checklist do controlador para a primeira conexão;
- [EuroScope: utilização](euroscope/utilizacao.pt.md), com a rotina de controle passo a passo;
- [TrackAudio: utilização](trackaudio/utilizacao.pt.md), com todos os botões e indicadores;
- [vATIS: utilização](vatis/utilizacao.pt.md), com a preparação e a manutenção do ATIS;
- [vacs: utilização](vacs/utilizacao.pt.md), com as chamadas de coordenação.
