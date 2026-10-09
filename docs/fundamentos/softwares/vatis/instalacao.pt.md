---
  title: Instalação
---

--8<-- "includes/abreviacoes.md"

# Instalação

Esta página mostra como instalar o vATIS, importar os perfis da VATSIM Brasil e configurar seus dados de acesso. Para operar o programa durante a sessão, veja a página de [Utilização](utilizacao.pt.md).

## Download e instalação

Baixe o instalador no [site oficial do vATIS](https://vatis.app). Há versões para Windows, macOS e Linux.

| Sistema | Instalação |
|---|---|
| **Windows** | Execute o instalador. O vATIS é instalado em `%localappdata%\org.vatsim.vatis` e cria um atalho na área de trabalho. A pasta de instalação não pode ser alterada. |
| **macOS** | Copie o `vATIS.app` para a pasta **Aplicativos**. |
| **Linux** | Baixe o arquivo **AppImage** e salve-o na pasta que preferir. |

!!! info "Atualizações do programa"
    O vATIS se atualiza sozinho: quando há uma versão nova, ela é baixada e instalada ao abrir o programa.

## Perfis da VATSIM Brasil

No vATIS, um **perfil** reúne as estações ATIS de uma região. A VATSIM Brasil mantém **um perfil por FIR**, já configurado com:

- as estações ATIS dos aeródromos da FIR, com as frequências;
- **presets** para cada configuração de pista;
- o formato das mensagens em texto e voz, com o **nível de transição** calculado a partir do QNH;
- **contrações**, para que nomes e abreviaturas sejam lidos corretamente pela voz sintetizada;
- **NOTAMs** e **condições do aeródromo** pré-definidos para situações comuns, como pista fechada.

Os perfis estão disponíveis no pacote de *sectorfiles* de cada FIR e também podem ser baixados aqui:

| FIR | Arquivo | Estações |
|---|---|---|
| Amazônica (SBAZ) | [vATIS-Profile-SBAZ.json](https://atc.vatsim.com.br/files/vatis/vATIS-Profile-SBAZ.json) | SBEG, SBBE, SBCY, SBBV, SBRB, SBPV, SBSL |
| Brasília (SBBS) | [vATIS-Profile-SBBS.json](https://atc.vatsim.com.br/files/vatis/vATIS-Profile-SBBS.json) | SBBR, SBCF, SBGO, SBRP, SBYS, SBBU, SBBH |
| Curitiba (SBCW) | [vATIS-Profile-SBCW.json](https://atc.vatsim.com.br/files/vatis/vATIS-Profile-SBCW.json) | SBSP, SBPA, SBCT, SBFL, SBKP, SBGR, SBRJ, SBCG, SBGL, SBME, SBSJ, SDCO, SBMT, SBLO, SBBI, SBNF, SBSM |
| Recife (SBRE) | [vATIS-Profile-SBRE.json](https://atc.vatsim.com.br/files/vatis/vATIS-Profile-SBRE.json) | SBRF, SBTE, SBFZ, SBSG, SBNT, SBSV, SBPS, SBVT |

!!! tip "Dica"
    Para salvar o arquivo, clique no link com o botão direito e escolha **Salvar link como...**.

### Importando um perfil

Ao abrir o vATIS, aparece a janela de perfis.

<figure markdown>
![Janela de perfis do vATIS](https://vatis.app/assets/images/ProfileDialog.png){ : style="border:2px solid #999; max-width:340px" loading=lazy }
<figcaption>Janela de perfis. Imagem: <a href="https://vatis.app/docs/client/profiles.html">documentação oficial do vATIS</a>.</figcaption>
</figure>

1. Clique em `Import` e selecione o arquivo `.json` da FIR.
2. Repita para as outras FIRs em que você controla. Cada uma aparece como um perfil separado, por exemplo **FIR Curitiba (SBCW)**.
3. Para abrir um perfil, selecione-o e clique em `Open`, ou dê dois cliques no nome.

Os demais botões servem para criar (`New`), renomear (`Rename`), exportar (`Export`) e apagar (`Delete`) perfis. A exclusão não pode ser desfeita.

### Atualização automática dos perfis

Os perfis da VATSIM Brasil se atualizam sozinhos. Cada arquivo indica o endereço de onde é publicado e um número de versão, e o vATIS consulta esse endereço periodicamente. Quando há uma versão mais nova, ela é baixada e substitui a instalada.

!!! warning "Atenção!"
    Alterações feitas por você no perfil são **sobrescritas** na próxima atualização. Para corrigir ou melhorar um perfil (frequência, preset, contração, NOTAM), [abra uma sugestão no repositório do Portal ATC](https://github.com/vatsim-brasil/atc-docs). Os arquivos ficam em `docs/files/vatis/`.

## Configurações do usuário

Antes de conectar pela primeira vez, abra o perfil e clique em `User Settings`, no canto superior esquerdo da janela principal.

<figure markdown>
![Configurações do usuário do vATIS](https://vatis.app/assets/images/UserSettings.png){ : style="border:2px solid #999; max-width:300px" loading=lazy }
<figcaption>Configurações do usuário. Imagem: <a href="https://vatis.app/docs/client/user-settings.html">documentação oficial do vATIS</a>.</figcaption>
</figure>

| Campo | O que preencher |
|---|---|
| `Real Name` | Seu nome, como no EuroScope. |
| `VATSIM ID` | Seu CID. |
| `VATSIM Password` | Sua senha da VATSIM. |
| `Network Rating` | Seu rating de controlador. |
| `Mute own ATIS update sound` | Silencia o aviso sonoro das atualizações dos ATIS que você publica. |
| `Mute shared ATIS update sound` | Silencia o aviso sonoro das atualizações dos ATIS publicados por outros controladores. |
| `Automatically fetch ATIS letter` | Busca a letra do ATIS real (D-ATIS) ao conectar, nos aeródromos em que esse serviço existe. |

Clique em `Save` para gravar.

## Onde ficam os arquivos

Os perfis e as configurações ficam na pasta de dados do vATIS:

| Sistema | Pasta |
|---|---|
| Windows | `%localappdata%\org.vatsim.vatis` |
| macOS | `~/Library/Application Support/org.vatsim.vatis` |
| Linux | `~/.local/share/org.vatsim.vatis` (pasta oculta) |
