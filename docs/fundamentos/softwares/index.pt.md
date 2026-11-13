---
  title: Visão Geral
  description: Os quatro programas da estação do controlador na Vatsim Brasil e a ordem em que eles se conectam
  icon: material/monitor-dashboard
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Softwares do Controlador

A estação de trabalho do controlador na Vatsim Brasil é formada por quatro programas. Cada um tem uma função, e eles dependem uns dos outros: o EuroScope conecta você à rede, e os outros três usam essa conexão.

<div class="grid cards" markdown>

-   :material-radar:{ .lg .middle } **EuroScope**

    ---

    A tela radar. Mostra o setor, os tráfegos e os planos de voo, e é por ele que você assume, autoriza e transfere cada aeronave.

    [:octicons-arrow-right-24: EuroScope](euroscope/index.pt.md)

-   :material-headset:{ .lg .middle } **TrackAudio**

    ---

    O rádio. Transmite e recebe nas frequências da sua posição, com o botão de *push-to-talk* (PTT).

    [:octicons-arrow-right-24: TrackAudio](trackaudio/index.pt.md)

-   :material-weather-windy:{ .lg .middle } **vATIS**

    ---

    O ATIS. Monta a informação do aeródromo a partir do METAR e da pista em uso e a transmite com voz sintetizada.

    [:octicons-arrow-right-24: vATIS](vatis/index.pt.md)

-   :material-phone-classic:{ .lg .middle } **vacs**

    ---

    A linha telefônica. Liga você aos outros controladores para coordenar por voz, sem precisar digitar no chat.

    [:octicons-arrow-right-24: vacs](vacs/index.pt.md)

</div>

## A ordem de conexão

Os programas sobem um de cada vez, sempre na mesma ordem. Toque em cada degrau, ou use as setas do teclado, para ver o que acontece nele.

<div class="vb-perfil" data-forma="degraus" markdown>

<section data-sigla="ES" data-nome="Abrir o perfil" data-alt="0" markdown>

### 1. Abra o EuroScope no perfil certo

Escolha o arquivo `.prf` da FIR em que vai controlar: **solo** para `DEL`, `GND` e `TWR`, **radar** para `APP` e `CTR`.

Para trocar de FIR, feche o programa e abra o perfil da nova FIR. Carregar outro setor com o EuroScope aberto não basta.

</section>

<section data-sigla="NET" data-nome="Conectar à rede" data-alt="1" markdown>

### 2. Conecte o EuroScope à VATSIM

No menu de conexão, escolha `Connect` e preencha o indicativo da posição (`SBCT_TWR`, por exemplo), seu nome, CID, senha, *facility* e rating. Use `Server` em `AUTOMATIC`.

A rede recusa a conexão numa posição acima do seu rating. Para só observar, use um indicativo terminado em `_OBS`.

</section>

<section data-sigla="FREQ" data-nome="Frequência primária" data-alt="2" markdown>

### 3. Marque a frequência primária

Em `OTHER SET` › *Voice Communications Setup*, marque a frequência da posição como **primária** (`Prim`). Na mesma janela ficam as linhas do *Controller ATIS*, que os pilotos leem ao consultar a sua posição.

Sem frequência primária, os pilotos veem a sua posição na rede, mas não sabem em que frequência chamar.

</section>

<section data-sigla="TA" data-nome="TrackAudio" data-alt="3" markdown>

### 4. Conecte o TrackAudio

Com o EuroScope conectado, o TrackAudio mostra o seu indicativo e o botão `CONNECT` fica verde. Clique nele e **marque à mão** `RX` e `TX` da sua frequência: o programa não faz isso sozinho.

Sem o EuroScope conectado, o TrackAudio mostra *"No VATSIM connection detected!"*.

</section>

<section data-sigla="G2G" data-nome="vacs" data-alt="4" markdown>

### 5. Conecte o vacs

Clique em **Connect** no vacs. Ele reconhece a sua posição pelo indicativo e pela frequência primária e acende as teclas dos setores on-line, para você ligar para eles.

Com a integração do TrackAudio, a mesma tecla de PTT serve ao rádio e à linha.

</section>

<section data-sigla="ATIS" data-nome="vATIS" data-alt="5" markdown>

### 6. Publique o ATIS, se for o caso

Se a posição for responsável pelo ATIS, abra o perfil da FIR no vATIS, escolha a estação e o *preset* da pista em uso, confira as condições e os NOTAMs e clique em `CONNECT`.

A pista do ATIS deve ser a mesma do EuroScope e a combinada com os demais órgãos.

</section>

<section data-sigla="ON" data-nome="Posição operacional" data-alt="6" markdown>

### 7. Posição operacional

Avise no canal `ATC` que abriu a posição e assuma os tráfegos que já estão na sua área.

Para encerrar, desça a escada na **ordem inversa**: transfira os tráfegos, desconecte o vATIS, o vacs, o TrackAudio e, por último, o EuroScope.

</section>

</div>

!!! tip "Dica"
    Siga a mesma ordem toda vez, como um checklist de cabine. O [checklist de conexão](sessao.pt.md) traz cada passo para marcar.

## O que você encontra aqui

| Página | O que tem |
| --- | --- |
| [Monte sua estação](preparacao.pt.md) | Trilha de instalação dos quatro programas, com marcação do seu progresso |
| [Ligar e desligar](sessao.pt.md) | Checklist da conexão e soluções para os problemas mais comuns |
| [EuroScope](euroscope/index.pt.md) | Instalação, utilização e guia de comandos |
| [TrackAudio](trackaudio/index.pt.md) | Instalação e utilização |
| [vATIS](vatis/index.pt.md) | Instalação, perfis da Vatsim Brasil e utilização |
| [vacs](vacs/index.pt.md) | Instalação, chamadas de coordenação e integração com o TrackAudio |
| [Quiz dos softwares](quiz.pt.md) | Perguntas rápidas para conferir o que você aprendeu |

## Do que você precisa

| Item | Observação |
| --- | --- |
| Computador com **Windows** | O EuroScope roda só em Windows. Os outros três também têm versões para macOS e Linux. |
| Fone de ouvido com microfone | Um *headset* evita que o áudio da frequência volte pelo microfone. |
| Uma tecla ou botão para o PTT | Pode ser do teclado, do mouse ou de um *joystick*. |
| CID e senha da VATSIM | Todos os programas pedem os mesmos dados de acesso. O vacs entra pelo login da VATSIM. |
| Conexão estável | Uma queda de internet derruba a sessão de voz e a conexão à rede. |
