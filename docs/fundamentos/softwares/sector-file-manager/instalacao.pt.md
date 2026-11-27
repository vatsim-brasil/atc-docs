---
  title: Instalação
  description: Trilha de instalação do Sector File Manager, do Vectors ATC Hub às FIRs instaladas no EuroScope
  icon: material/download
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Instalação

Do download às FIRs instaladas, em cinco etapas. Marque cada uma ao terminar: o portal guarda o seu progresso neste navegador.

!!! info "Do que você precisa"
    - Windows 10 ou mais novo, 64 bits.
    - O [EuroScope instalado](../euroscope/instalacao.pt.md).
    - Uma conta no [AeroNav](https://files.aero-nav.com/SBXX), a mesma que você usaria para baixar os pacotes à mão.

<div class="vb-trilha" data-chave="sfm-instalacao" markdown>

<div class="vb-passo" markdown>

### Instale o Vectors ATC Hub

O Sector File Manager é distribuído pelo **Vectors ATC Hub**, o programa que instala, atualiza, repara e remove os programas do Vectors ATC Group.

Baixe o **[VectorsATCHub-Setup.exe](https://github.com/VectorsATCGroup/vectors-atc-releases/releases/latest/download/VectorsATCHub-Setup.exe)** e execute.

A instalação é por usuário e **não pede permissão de administrador**. Se o Windows ainda não tiver o Microsoft WebView2, o instalador o instala junto.

!!! warning "Não use a página de releases antiga"
    O repositório original do Sector File Manager parou na versão 1.2.0. As versões novas saem só pelo Hub e pelo catálogo [vectors-atc-releases](https://github.com/VectorsATCGroup/vectors-atc-releases).

</div>

<div class="vb-passo" markdown>

### Instale o Sector File Manager pelo Hub

Abra o Hub e instale o **EuroScope Sector File Manager**. A partir daí, o Hub mantém o programa atualizado, e o próprio Hub se atualiza sozinho.

</div>

<div class="vb-passo" markdown>

### Abra o programa pela primeira vez

Na primeira vez, um assistente encontra sozinho a **instalação do EuroScope** e a **pasta dos arquivos de setor**. Confira os caminhos que ele mostrar antes de seguir.

!!! tip "Dica"
    Escolha o idioma e o tema em **Settings**. A troca para português vale na hora, sem reiniciar.

</div>

<div class="vb-passo" markdown>

### Entre na sua conta do AeroNav

Clique em **Authenticate**. Abre uma janela com a página oficial do AeroNav, separada do resto do programa. Entre com a sua conta, pela VATSIM ou pela Navigraph, como no site.

A janela fecha sozinha quando a lista de pacotes aparece. O programa **nunca vê a sua senha**: ele só guarda a sessão do AeroNav, por até 30 dias.

</div>

<div class="vb-passo" markdown>

### Instale as FIRs

O painel mostra as cinco FIRs da Vatsim Brasil, com o AIRAC disponível de cada uma. Clique em **Install** nas FIRs em que você vai controlar.

O programa baixa o pacote, faz um backup e aplica a instalação. Se algo falhar no meio, ele desfaz a operação.

!!! tip "Instale todas as FIRs"
    Com as cinco instaladas, você está pronto para controlar em qualquer FIR, e uma troca de última hora não pega você sem o setor.

[:octicons-arrow-right-24: Utilização](utilizacao.pt.md){ .md-button .md-button--primary }

</div>

</div>

## Onde ficam os arquivos do programa

As configurações, o registro do que está instalado, os backups e os logs ficam em:

```text
%LOCALAPPDATA%\VectorsATCGroup\EuroScopeSectorFileManager
```

O programa guarda só dados técnicos: os caminhos de instalação, as versões instaladas, o tema e o idioma. A sessão do AeroNav fica num perfil de navegador isolado, na mesma pasta.

## Desinstalando

Desinstale pelo Hub, ou rode o instalador de novo e escolha **Uninstall**. A desinstalação apaga **toda** a pasta acima, inclusive os backups e a sessão do AeroNav. Os arquivos de setor instalados no EuroScope continuam onde estão.

Numa nova instalação, o programa começa do zero e mostra o assistente da primeira vez.
