---
  title: Monte sua Estação
  description: Trilha de instalação do EuroScope, do TrackAudio, do vATIS e do vacs, do download ao primeiro teste como observador
  icon: material/map-marker-path
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Monte sua Estação

Da instalação ao primeiro teste, em dez etapas. Cada uma resume o essencial e aponta para o guia completo do programa. Marque as etapas ao terminar: o portal guarda o seu progresso neste navegador.

!!! info "Quanto tempo leva?"
    Uma tarde basta. O que mais demora é o download dos arquivos de setor e o ajuste do áudio.

<div class="vb-trilha" data-chave="softwares" markdown>

<div class="vb-passo" markdown>

### Confira o que você precisa

- Um computador com **Windows**: o EuroScope não tem versão para macOS ou Linux.
- Fone de ouvido com microfone.
- Uma tecla ou botão livre para o *push-to-talk* (PTT).
- O seu **CID** e a sua **senha da VATSIM**. Todos os programas pedem os mesmos dados.

</div>

<div class="vb-passo" markdown>

### Instale o EuroScope

Baixe o instalador no [site do EuroScope](https://www.euroscope.hu), em `Installation`, e siga as etapas normalmente.

!!! danger "Versão recomendada"
    Instale a versão **3.2.3.2**, disponível [nesta página](https://www.euroscope.hu/wp/2024/06/09/v3-2-2-3-and-v3-2-3-2-with-token-authentication-update/).

[:octicons-arrow-right-24: Instalação do EuroScope](euroscope/instalacao.pt.md){ .md-button }

</div>

<div class="vb-passo" markdown>

### Instale os arquivos de setor

Os *sectorfiles* da Vatsim Brasil são instalados e atualizados com o **Sector File Manager**, que você instala pelo [Vectors ATC Hub](https://github.com/VectorsATCGroup/vectors-atc-releases/releases/latest/download/VectorsATCHub-Setup.exe). Entre com a sua conta do AeroNav e clique em **Install** nas FIRs em que vai controlar.

[:octicons-arrow-right-24: Arquivos de setor](euroscope/instalacao.pt.md#instale-o-sector-file-manager){ .md-button }

!!! warning "A caixa de perfis não apareceu?"
    Desmarque a opção `Auto load last profile on startup` e abra o EuroScope de novo.

</div>

<div class="vb-passo" markdown>

### Conheça os dois perfis

Cada FIR tem dois arquivos de perfil (`.prf`):

| Perfil | Posições | Plugin principal |
| --- | --- | --- |
| `solo` | `DEL`, `RMP`, `GND` e `TWR` | Ground Radar Plugin, que desenha o aeródromo e as etiquetas de solo |
| `radar` | `APP` e `CTR` | TopSky, que reproduz um sistema radar real |

Abra o perfil `solo` da FIR do seu aeródromo e explore a tela sem conectar: menus, listas, zoom com `F11` e `F12`.

[:octicons-arrow-right-24: A tela principal](euroscope/utilizacao.pt.md#a-tela-principal){ .md-button }

</div>

<div class="vb-passo" markdown>

### Instale o TrackAudio

Baixe a versão mais recente no [GitHub do TrackAudio](https://github.com/pierr3/TrackAudio/releases), na seção **Assets** do último *release*. No Windows, o arquivo termina em `.exe`.

[:octicons-arrow-right-24: Instalação do TrackAudio](trackaudio/instalacao.pt.md){ .md-button }

</div>

<div class="vb-passo" markdown>

### Configure o áudio e o PTT

Nas configurações do TrackAudio (a engrenagem no canto superior esquerdo):

- informe o CID e a senha da VATSIM;
- escolha a saída **primária** (o fone), a **secundária** (o alto-falante) e a **entrada** (o microfone);
- defina a tecla ou o botão de **PTT**.

!!! tip "Dica"
    Escolha um PTT que você alcance sem tirar a mão do mouse. Você vai apertá-lo centenas de vezes por sessão.

</div>

<div class="vb-passo" markdown>

### Instale o vATIS e importe os perfis

Baixe o vATIS no [site oficial](https://vatis.app). Ao abrir, clique em `Import` na janela de perfis e selecione o arquivo `.json` da sua FIR. A Vatsim Brasil mantém um perfil por FIR, já com estações, *presets* de pista e contrações.

[:octicons-arrow-right-24: Perfis da Vatsim Brasil](vatis/instalacao.pt.md#perfis-da-vatsim-brasil){ .md-button }

!!! warning "Não edite o perfil"
    Os perfis se atualizam sozinhos, e alterações locais são sobrescritas. Para corrigir algo, abra uma sugestão no repositório do portal.

</div>

<div class="vb-passo" markdown>

### Preencha seus dados no vATIS

Abra o perfil, clique em `User Settings` e preencha nome, CID, senha e rating. Clique em `Save`.

</div>

<div class="vb-passo" markdown>

### Instale o vacs

Baixe o vacs na [página de releases](https://github.com/vacs-project/vacs/releases/latest), instale e entre com **Login via VATSIM**. Em **Settings › Transmit**, escolha **Push-to-Talk** e ligue a integração com o **TrackAudio**: a mesma tecla vai servir ao rádio e à linha.

!!! warning "Uma tecla, um dono"
    Com a integração ligada, tire a tecla de PTT do TrackAudio e deixe-a só no vacs. Os dois programas não podem usar a mesma tecla ao mesmo tempo.

[:octicons-arrow-right-24: Instalação do vacs](vacs/instalacao.pt.md){ .md-button }

</div>

<div class="vb-passo" markdown>

### Faça um teste como observador

Antes da primeira sessão de verdade, confira que tudo conversa:

1. No EuroScope, conecte com um indicativo `_OBS` (por exemplo, `SBGR_OBS`).
2. Abra o TrackAudio: o indicativo aparece no topo e o botão `CONNECT` fica verde.
3. Conecte e adicione a frequência de uma posição on-line com o botão `+`. Marque só `RX` e escute.
4. Desconecte o TrackAudio e depois o EuroScope.

Se você ouviu a frequência, a sua estação está pronta.

[:octicons-arrow-right-24: Checklist de conexão](sessao.pt.md){ .md-button .md-button--primary }

</div>

</div>

## Ainda com dúvidas?

??? question "Posso usar macOS ou Linux?"
    O TrackAudio e o vATIS rodam nos três sistemas, mas o EuroScope é só para Windows. Em macOS ou Linux, ele precisa de uma máquina virtual ou de uma camada de compatibilidade, e este guia não cobre essas configurações.

??? question "Preciso do vATIS em toda sessão?"
    Só quando a sua posição for responsável pelo ATIS do aeródromo. Mesmo assim, vale instalá-lo desde o começo para conhecer o programa com calma.

??? question "E o AFV (Audio for VATSIM)?"
    O TrackAudio substitui o antigo cliente AFV para controladores. Use o TrackAudio.
