---
  title: Instalação
  description: Trilha de instalação do vacs, do download à integração com o TrackAudio
  icon: material/download
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Instalação

Do download à primeira conexão, em oito etapas. Marque cada uma ao terminar: o portal guarda o seu progresso neste navegador.

<div class="vb-trilha" data-chave="vacs-instalacao" markdown>

<div class="vb-passo" markdown>

### Baixe a versão mais recente

Acesse a [página de releases do vacs](https://github.com/vacs-project/vacs/releases/latest) e, na seção **Assets** do release marcado como **Latest**, baixe o arquivo do seu sistema. Se a lista estiver recolhida, clique em **Show all assets**.

| Sistema | Arquivo |
| --- | --- |
| Windows | `..._x64-setup.exe` |
| macOS (Apple Silicon) | `..._aarch64.dmg` |
| macOS (Intel) | `..._x64.dmg` |
| Linux | `..._amd64.deb` (Debian e Ubuntu), `...x86_64.rpm` (Fedora, RHEL e openSUSE) ou `..._amd64.AppImage` |

O botão **Download latest** do [site do vacs](https://vacs.network) leva ao mesmo lugar.

</div>

<div class="vb-passo" markdown>

### Instale

=== "Windows"

    Execute o instalador e siga as etapas.

=== "macOS"

    Abra o `.dmg` e copie o vacs para a pasta **Aplicativos**, ou instale pelo Homebrew:

    ```text
    brew install --cask vacs-project/tap/vacs
    ```

    As versões para macOS ainda não são assinadas. Se o sistema disser que o aplicativo está danificado, rode no Terminal:

    ```text
    sudo xattr -rd com.apple.quarantine /Applications/vacs.app
    ```

    O macOS também pede as permissões de **Monitoramento de entrada** e **Acessibilidade** para os atalhos de teclado.

=== "Linux"

    Instale o pacote do seu sistema:

    ```text
    sudo apt install ./vacs_..._amd64.deb
    sudo dnf install ./vacs-...x86_64.rpm
    ```

    Para o AppImage, dê permissão de execução com `chmod +x`. No Wayland, os atalhos globais dependem do *portal* da área de trabalho.

O vacs se atualiza pelo próprio programa: quando há versão nova, aparece **UPDATE AVAILABLE** na barra superior.

</div>

<div class="vb-passo" markdown>

### Entre com a sua conta VATSIM

Na tela de login, clique em **Login via VATSIM** e entre com a sua conta. O vacs recebe só o seu CID, nunca a senha.

</div>

<div class="vb-passo" markdown>

### Escolha os dispositivos de áudio

Em **Settings › Audio**:

| Campo | O que escolher |
| --- | --- |
| **Headset / Output Device** | O fone de ouvido, o mesmo do TrackAudio |
| **Microphone / Input Device** | O microfone |
| **Speaker / Notification Device** | Opcional: um alto-falante para os toques e cliques, para ouvir a chamada mesmo sem o fone na cabeça |

Ajuste os volumes **Output**, **Input**, **Click Volume** e **Chime Volume**. O medidor do **Input** deve ficar no verde quando você fala.

!!! warning "Use fone de ouvido"
    O vacs não tem cancelamento de eco. Com alto-falante, o outro controlador ouve a própria voz de volta.

</div>

<div class="vb-passo" markdown>

### Configure o PTT e a integração com o TrackAudio

Abra **Settings › Transmit**. A configuração recomendada:

| Campo | Valor |
| --- | --- |
| **CALL MIC MODE** | **Push-to-Talk (PTT)**, com a tecla que você já usa no rádio |
| **RADIO INTEGRATION** | **TrackAudio** |
| **Radio PTT** | Deixe vazio para usar a mesma tecla da linha |

Assim, uma única tecla serve para o rádio e para a linha: durante uma chamada, ela fala com o outro controlador; fora dela, transmite na frequência pelo TrackAudio.

!!! danger "Tire a tecla do TrackAudio"
    Com a integração ligada, **não** deixe a mesma tecla configurada como PTT no TrackAudio. Os dois programas vão disputar a transmissão.

O ponto ao lado de **Endpoint** mostra o estado da integração:

| Cor | Significado |
| --- | --- |
| Verde | Conectado ao TrackAudio, pronto |
| Azul | Transmitindo no rádio |
| Amarelo | O TrackAudio está aberto, mas não conectado à voz da VATSIM |
| Cinza | Ainda não pronto |
| Vermelho | Erro de conexão |

Se você prefere teclas separadas para o rádio e para a linha, escolha uma **Radio PTT** diferente.

</div>

<div class="vb-passo" markdown>

### Configure os atalhos

Em **Settings › Hotkeys**, todos os atalhos são opcionais:

| Ação | Para que serve |
| --- | --- |
| **Accept first call** | Atende a primeira chamada que estiver tocando |
| **End active call** | Desliga a chamada em andamento |
| **Toggle RADIO PRIO** | Liga ou desliga a prioridade do rádio sobre a linha |
| **SAY AGAIN** | Repete a última transmissão recebida no rádio |

!!! tip "Dica"
    Use a **mesma tecla** para *Accept first call* e *End active call*: ela atende quando toca e desliga quando a chamada está em andamento.

!!! warning "Windows e modo administrador"
    Se o EuroScope ou o TrackAudio rodam como administrador, os atalhos do vacs não funcionam enquanto a janela deles está em foco. Rode os três do mesmo jeito: todos como administrador ou nenhum.

</div>

<div class="vb-passo" markdown>

### Revise as opções de chamada

Em **Settings › Call**, os padrões servem para a maioria. Vale conhecer:

- **Enable priority calls**: permite fazer e receber chamadas **PRIO**.
- **Use default call sources**: escolhe sozinho a estação de origem das suas chamadas.
- **End active call on accept**: ao atender uma segunda chamada, desliga a que está em andamento.
- **Always relay calls**: passa o áudio pelo servidor do vacs. Ligue se você usa VPN ou se as chamadas conectam e caem.
- **Ring sounds**: troca os toques por arquivos **WAV** de 0,1 a 30 segundos.

</div>

<div class="vb-passo" markdown>

### Conecte pela primeira vez

Na sua próxima sessão, com a posição conectada no EuroScope e a frequência primária marcada, clique em **Connect** no vacs. As teclas dos setores on-line ficam clicáveis, e você aparece para os outros controladores.

[:octicons-arrow-right-24: Utilização](utilizacao.pt.md){ .md-button .md-button--primary }

</div>

</div>

## Onde ficam os arquivos

As configurações ficam em arquivos `.toml`. O botão **Open Config**, em **Settings › Miscellaneous**, abre a pasta:

| Sistema | Pasta |
| --- | --- |
| Windows | `%APPDATA%\app.vacs.vacs-client\` |
| macOS | `~/Library/Application Support/app.vacs.vacs-client/` |
| Linux | `~/.config/app.vacs.vacs-client/` |

Feche o vacs antes de editar os arquivos à mão: o programa regrava `audio.toml` e `client.toml` e desfaz as suas alterações.
