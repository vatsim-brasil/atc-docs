---
  title: Visão Geral
  description: O vacs, a linha telefônica entre os controladores da VATSIM para a coordenação por voz
  icon: material/phone-classic
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# vacs

O [vacs](https://vacs.network) é a linha telefônica entre os controladores: um sistema de comunicação **solo-solo** (*ground-to-ground*, G2G) para a VATSIM. Com ele, você liga para o órgão vizinho e coordena por voz, como nos centros de controle reais, em vez de digitar no chat.

É um projeto aberto e gratuito, mantido pela equipe do [vacs-project](https://github.com/vacs-project/vacs), com versões para Windows, macOS e Linux.

## Como funciona

- **Você liga para um setor, não para uma pessoa.** Cada tecla da tela representa um setor. A chamada toca para quem estiver cobrindo aquele setor no momento, inclusive por [top-down](../../../documentos/manuais/coordenacao-transferencia/04-rede.pt.md#cobertura-top-down).
- **A sua posição é reconhecida pela conexão.** O vacs identifica a sua estação pelo indicativo, pela frequência primária e pelo tipo de órgão com que você conectou no EuroScope.
- **O login é pela VATSIM.** Você entra com o VATSIM Connect, e o vacs nunca vê a sua senha.
- **O áudio vai direto entre os controladores**, de ponto a ponto, sem servidor de voz no meio.
- **Ele conversa com o TrackAudio.** Com a integração de rádio, uma única tecla de PTT serve ao rádio e à linha, e o vacs mostra as suas frequências e grava o que você recebe para repetir depois.

## Na Vatsim Brasil

Os setores e as posições do Brasil estão cadastrados no repositório de dados do vacs, o [vacs-data](https://github.com/vacs-project/vacs-data/tree/main/dataset/SB), na pasta `SB`. Ela reúne as cinco FIRs: **Amazônica** (SBAZ), **Brasília** (SBBS), **Curitiba** (SBCW), **Recife** (SBRE) e **Atlântico** (SBAO), com os centros, as aproximações, as torres e as posições de solo.

!!! warning "Conecte com o indicativo e a frequência certos"
    Se o indicativo ou a frequência da sua conexão não baterem com o cadastro, o vacs não reconhece a sua posição, e os outros controladores não conseguem ligar para você. Use sempre os indicativos e as frequências do [MOP](../../../MOP/aerodromos/index.pt.md).

Encontrou um setor faltando ou uma frequência errada? Avise a equipe da Vatsim Brasil. As correções são feitas no repositório vacs-data.

## Uma chamada, passo a passo

Toque em cada ponto, ou use as setas do teclado, para acompanhar uma chamada do início ao fim.

<div class="vb-perfil" data-forma="voo" markdown>

<section data-sigla="1" data-nome="Escolha o setor" data-alt="0" markdown>

### Escolha o setor

Na tela do vacs, cada setor é uma **tecla de acesso direto**. Ela só fica clicável quando o setor está on-line, no vacs e na rede.

Antes de ligar, **prepare a mensagem**: indicativo da aeronave, ponto, hora, nível. A linha é para recados curtos.

</section>

<section data-sigla="2" data-nome="Ligue" data-alt="1" markdown>

### Ligue

Clique na tecla do setor. A chamada vai para quem cobre aquele setor agora: se a Torre não estiver on-line, toca no Controle que a cobre.

Para uma coordenação urgente, ative **PRIO** antes de clicar. O outro controlador vê uma borda amarela e ouve um toque diferente.

</section>

<section data-sigla="3" data-nome="Toca" data-alt="2" markdown>

### O outro lado atende

Do outro lado, a tecla do seu setor pisca em verde e o toque soa. Quem recebe atende clicando nela.

Se ninguém atender, a chamada termina sozinha e aparece **REMOTE TARGET DID NOT ANSWER** na barra superior.

</section>

<section data-sigla="4" data-nome="Coordene" data-alt="2" markdown>

### Coordene

Quando o indicador no canto superior esquerdo fica **verde**, a linha está aberta. Fale com o PTT da linha, de forma curta. Um estimado, no modelo do MCA 100-16:

> "Estimado do VRG 3256, de Cuiabá para Guarulhos, FL 330, estima VARGA aos 55."

Quem recebe confirma com "ciente" ou repete os dados.

</section>

<section data-sigla="5" data-nome="Desligue" data-alt="0" markdown>

### Desligue

Clique em **END**, na barra inferior. Depois, registre o que foi combinado na etiqueta do EuroScope, para que todos vejam a mesma informação.

</section>

</div>

## Guias

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Instalação**

    ---

    Trilha da instalação, do login e da configuração do áudio, do PTT e da integração com o TrackAudio.

    [:octicons-arrow-right-24: Instalação](instalacao.pt.md)

-   :material-phone-in-talk:{ .lg .middle } **Utilização**

    ---

    Fazer e receber chamadas, conferências, a página do telefone, o rádio e a solução dos problemas comuns.

    [:octicons-arrow-right-24: Utilização](utilizacao.pt.md)

</div>

## Linha, chat ou etiqueta?

| Ferramenta | Use para |
| --- | --- |
| Etiqueta do EuroScope (`F4` / `F3`) | A transferência de rotina, que não precisa de conversa |
| **vacs** | Coordenações que pedem resposta: pedido de nível, liberação, restrição, tráfego fora do padrão, emergência |
| Chat privado | Recados que podem esperar, ou quando o outro controlador não está no vacs |
| Canal `ATC` | Avisos para todos, como abertura e fechamento de posição |
