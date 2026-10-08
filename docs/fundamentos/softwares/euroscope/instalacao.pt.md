---
  title: Instalação
---

--8<-- "includes/abreviacoes.md"

![Fundamentos - Euroscope - Instalação](img/head-euroscope-instalacao.png)

## Download

!!! info "Informação"
    O Euroscope está disponível apenas para *Microsoft Windows*.

1. Acesse o [site do Euroscope](https://www.euroscope.hu) e acesse a página de downloads clicando em `Installation` na barra superior.

![](img/es1.png){ : style="border:2px solid #999" }

2. Clique no link disponível na seção "Download" para baixar o EuroScope. Após o download, siga as etapas do instalador normalmente.

![](img/es2.png){ : style="border:2px solid #999" }

!!! danger "Atenção!"
    Recomendamos que seja instalada a versão **3.2.3.2** que pode ser encontrada [nesse link](https://www.euroscope.hu/wp/2024/06/09/v3-2-2-3-and-v3-2-3-2-with-token-authentication-update/).

!!! warning "Uma dica!"
    Recomendamos fortemente a leitura do manual do Euroscope, que pode ser facilmente encontrado no site em `Documentation` > `Download User's Guide`.

## *Sectorfiles* e Arquivos de Configuração

Os *sectorfiles* e perfis da VATSIM Brasil são publicados no **[Aeronav GNG](https://files.aero-nav.com/SBXX)**. A divisão recomenda instalá-los e atualizá-los com o **[EuroScope Sector File Manager](https://github.com/VectorsATCGroup/euroscope-sector-file-manager)**, ferramenta gratuita desenvolvida pelo **[Vectors ATC Group](https://vectorsatcgroup.com)**.

<figure markdown>
[![Vectors ATC Group](https://raw.githubusercontent.com/VectorsATCGroup/euroscope-sector-file-manager/main/assets/vectors-logo-dark.png#only-light){ width="240" }![Vectors ATC Group](https://raw.githubusercontent.com/VectorsATCGroup/euroscope-sector-file-manager/main/assets/vectors-logo-white.png#only-dark){ width="240" }](https://vectorsatcgroup.com)
</figure>

O aplicativo baixa o pacote de cada FIR direto do Aeronav, faz um backup e aplica a atualização sem apagar sua pasta `Settings` nem seus arquivos personalizados. Se algo falhar, a instalação é revertida.

!!! info "Requisitos"
    Windows 10 ou superior (64 bits), EuroScope instalado e uma conta no Aeronav.

1. Baixe o arquivo `VectorsEuroScopeSectorFileManager-Setup.exe` na [página de *releases*](https://github.com/VectorsATCGroup/euroscope-sector-file-manager/releases/latest) e execute-o. A instalação é feita só para o seu usuário e não pede permissão de administrador.
2. Ao abrir pela primeira vez, o aplicativo localiza a instalação do EuroScope e a pasta de *sectorfiles*.
3. Entre na sua conta do Aeronav na janela que se abre. O login acontece na página oficial do Aeronav e fica salvo para as próximas vezes.
4. O painel lista cada FIR (SBAO, SBAZ, SBBS, SBCW e SBRE) com o AIRAC instalado e o disponível. Clique em `Install` ou `Update` nas FIRs em que você controla.

!!! tip "Dica"
    Abra o aplicativo a cada novo ciclo AIRAC para manter os *sectorfiles* em dia. Ele também avisa quando há uma versão nova do próprio programa.

??? question "O aplicativo tem acesso à minha senha?"
    Não. O login é feito nas páginas oficiais do Aeronav, VATSIM e Navigraph, em uma janela de navegador isolada. O aplicativo não lê nem guarda sua senha e não envia dados a nenhum servidor. Os detalhes estão no [repositório do projeto](https://github.com/VectorsATCGroup/euroscope-sector-file-manager#privacidade-em-primeiro-lugar).

??? question "Posso instalar sem o aplicativo?"
    Sim. Baixe o pacote da FIR no [Aeronav GNG](https://files.aero-nav.com/SBXX), descompacte-o e copie os arquivos para a pasta de *sectorfiles* do EuroScope, tomando cuidado para não sobrescrever sua pasta `Settings`.

### Abrindo o perfil

Ao abrir o EuroScope, escolha o perfil (`.prf`) da FIR e da posição em que vai controlar.

!!! warning "Atenção!"
    Se a caixa de diálogo de perfis não aparecer, a opção `Auto load last profile on startup` está marcada. Desmarque a opção, e abra novamente o Euroscope.

??? question "Qual a diferença do perfil `radar` para o perfil `solo`?"
    O perfil `solo` contém um esquema de cores e tags otimizado para o controle nas posições `DEL`, `RMP`, `GND` e `TWR`.

    Já o perfil `radar` está otimizado para as posições `APP` e `CTR`.

!!! info "Uma informação importante"
    Se desejar mudar de posição e esta se encontrar em uma FIR diferente, você deverá reiniciar o Euroscope e abrir o perfil correto para a nova posição. Simplesmente carregar o novo setor/ASR não é suficiente.
