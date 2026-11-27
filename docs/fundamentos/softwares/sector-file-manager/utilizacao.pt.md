---
  title: Utilização
  description: Como manter os arquivos de setor da Vatsim Brasil em dia com o Sector File Manager, a cada AIRAC
  icon: material/folder-sync
---

--8<-- "includes/abreviacoes.md"

# Utilização

Esta página mostra o Sector File Manager no dia a dia: conferir o AIRAC, atualizar as FIRs e resolver os problemas comuns. Ela parte do ponto em que a [instalação](instalacao.pt.md) já foi feita.

## A rotina antes de cada sessão

``` mermaid
flowchart LR
    A[EuroScope<br/>fechado] --> B[Abra o<br/>Sector File Manager]
    B --> C{Alguma FIR<br/>com Update?}
    C -- Sim --> D[Clique em<br/>Update]
    C -- Não --> E[Abra o EuroScope]
    D --> E
```

1. **Feche o EuroScope.** O programa não deve substituir arquivos que o EuroScope está usando.
2. Abra o Sector File Manager e espere a conferência da sessão (**Checking saved session…**).
3. Se alguma FIR mostrar **Update**, clique nele.
4. Abra o EuroScope no perfil da FIR.

## O painel

Cada FIR aparece numa linha, com:

| Informação | O que significa |
| --- | --- |
| AIRAC instalado | O ciclo do setor que está na sua máquina, lido do arquivo `.sct` que o EuroScope carrega |
| AIRAC disponível | O pacote mais novo publicado no AeroNav |
| **Install** | A FIR ainda não está instalada |
| **Update** | Há um pacote mais novo que o instalado |

O painel mostra o que está instalado mesmo antes do login no AeroNav. Para ver o que há de novo e baixar, é preciso estar autenticado.

### As edições dentro do ciclo

Quando a equipe corrige um pacote dentro do mesmo AIRAC, ele sai como uma nova edição. O painel mostra a primeira edição como `2608` e as seguintes como `2608/2`, `2608/3`. Uma edição nova também aparece como **Update**: instale-a, mesmo que o ciclo seja o mesmo.

## O que a atualização muda

| A atualização substitui | A atualização preserva |
| --- | --- |
| Setor (`.sct` e `.ese`), ASR, NavData, alias e as configurações do vATIS do pacote | Os perfis `solo` e `radar` (`.prf`) e as suas personalizações das pastas `Settings/SOLO` e `Settings/RADAR` |
| `login_profiles.txt`, `VoiceChannels.txt` e `AircraftPerformance.txt` | Os plugins e os arquivos que você criou e que não fazem parte do pacote |

!!! warning "Editou um desses três arquivos?"
    As alterações feitas à mão em `login_profiles.txt`, `VoiceChannels.txt` e `AircraftPerformance.txt` se perdem na atualização. O backup automático guarda a versão anterior.

## A sessão do AeroNav

- O login fica guardado por até **30 dias**, num perfil de navegador isolado.
- Se o AeroNav encerrar a sessão antes disso, o painel pede um novo login. Clique em **Authenticate**, entre de novo, e a operação continua.
- **Logout** apaga a sessão guardada. Use num computador compartilhado.

## Configurações

Em **Settings**:

| Opção | Para que serve |
| --- | --- |
| Idioma | Português ou inglês. A troca vale na hora. |
| Tema | Claro ou escuro |
| **Updates** | Liga ou desliga a busca por versão nova do programa ao abrir, e tem o botão **Check now** |

Quando há uma versão nova do programa, ele mostra as novidades e o botão **Update now**, e uma faixa fica sob a barra de título até você atualizar. A atualização é baixada, conferida e instalada sozinha, e o programa reabre. O [Vectors ATC Hub](instalacao.pt.md#instale-o-vectors-atc-hub) também mantém o programa em dia.

O Sector File Manager abre uma janela só: abrir o programa de novo traz para a frente a janela que já está aberta. Fechar a janela principal encerra o programa.

## Quando algo dá errado

??? failure "O painel diz que a sessão expirou"
    O AeroNav encerrou a sessão. Clique em **Authenticate** e entre de novo.

??? failure "O EuroScope continua mostrando o AIRAC antigo"
    O EuroScope estava aberto durante a atualização, ou você abriu um perfil de outra pasta. Feche o EuroScope, confira no painel se a FIR está no AIRAC novo e abra o perfil da pasta que o programa usa.

??? failure "A atualização foi interrompida no meio"
    Nada muda na sua instalação: a mudança só é aplicada com tudo pronto. Abra o programa e clique em **Update** de novo.

??? failure "Perdi uma alteração num arquivo do pacote"
    Os arquivos do pacote são substituídos na atualização. A versão anterior está no backup, na pasta do programa (`%LOCALAPPDATA%\VectorsATCGroup\EuroScopeSectorFileManager`).

??? failure "Outro problema"
    Os logs ficam em `logs\app-*.log`, na pasta do programa. Eles não guardam endereços, cookies nem senhas, e podem ser enviados junto com o relato na página de [issues do projeto](https://github.com/VectorsATCGroup/euroscope-sector-file-manager/issues).

## Para saber mais

- [Repositório do Sector File Manager](https://github.com/VectorsATCGroup/euroscope-sector-file-manager), com o histórico de versões no `CHANGELOG.md` (em inglês);
- [Vectors ATC Hub e catálogo de versões](https://github.com/VectorsATCGroup/vectors-atc-releases);
- [Pacotes das FIRs no AeroNav](https://files.aero-nav.com/SBXX).
