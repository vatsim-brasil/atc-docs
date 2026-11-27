---
  title: Visão Geral
  description: O Sector File Manager, o programa que instala e atualiza os arquivos de setor da Vatsim Brasil no EuroScope
  icon: material/folder-sync
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Sector File Manager

O [EuroScope Sector File Manager](https://github.com/VectorsATCGroup/euroscope-sector-file-manager) instala e atualiza os arquivos de setor da Vatsim Brasil no EuroScope com um clique. Ele baixa o pacote oficial de cada FIR no [AeroNav](https://files.aero-nav.com/SBXX), faz um backup, aplica a mudança e preserva as suas configurações.

É um programa gratuito e de código aberto (licença Apache 2.0), mantido pelo [Vectors ATC Group](https://github.com/VectorsATCGroup), um grupo independente de controladores da VATSIM. Roda só em Windows, como o EuroScope.

## Por que usar

Sem ele, atualizar o setor a cada AIRAC é trabalho manual: entrar no AeroNav, baixar o pacote de cada FIR, descompactar e copiar os arquivos para a pasta certa sem apagar os seus perfis e personalizações. Um arquivo copiado no lugar errado, ou uma cópia interrompida no meio, deixa o EuroScope com um setor quebrado.

O Sector File Manager faz tudo isso de uma vez e com segurança:

- **Baixa só do AeroNav oficial.** O programa não redistribui arquivos: o pacote vem da mesma fonte que você usaria à mão.
- **Faz backup antes de mudar.** A instalação é preparada numa área temporária e só é aplicada se tudo der certo. Se algo falhar, ele desfaz a operação.
- **Preserva o que é seu.** As personalizações da pasta `Settings`, os plugins e os arquivos que você criou ficam onde estão.
- **Mostra o AIRAC de cada FIR.** O painel compara o ciclo instalado com o disponível no AeroNav.
- **Fala português.** A interface tem português e inglês, com tema claro e escuro.

## As FIRs

O painel mostra as cinco FIRs da Vatsim Brasil:

| FIR | Nome |
| --- | --- |
| `SBAO` | Atlântico |
| `SBAZ` | Amazônica |
| `SBBS` | Brasília |
| `SBCW` | Curitiba |
| `SBRE` | Recife |

## O ciclo de uma atualização

Toque em cada ponto, ou use as setas do teclado, para acompanhar uma atualização do início ao fim.

<div class="vb-perfil" data-forma="voo" markdown>

<section data-sigla="AIRAC" data-nome="Novo ciclo" data-alt="0" markdown>

### Sai um novo AIRAC

A cada 28 dias começa um ciclo AIRAC, e a equipe da Vatsim Brasil publica no AeroNav os pacotes atualizados das FIRs.

Correções dentro do mesmo ciclo saem como uma nova edição do pacote. O painel mostra essas edições como `2608/2`; a primeira edição do ciclo aparece só como `2608`.

</section>

<section data-sigla="SFM" data-nome="Abra o programa" data-alt="1" markdown>

### Abra o Sector File Manager

Com o **EuroScope fechado**, abra o programa. Ele confere a sessão do AeroNav e lê o AIRAC instalado direto do arquivo `.sct` que o EuroScope carrega.

</section>

<section data-sigla="UPD" data-nome="Atualize" data-alt="2" markdown>

### Clique em Update

Se o pacote do AeroNav for mais novo que o instalado, a FIR mostra **Update**. Clique nele.

O programa baixa o pacote oficial, faz o backup e prepara a mudança numa área temporária.

</section>

<section data-sigla="OK" data-nome="Aplicado" data-alt="1" markdown>

### A mudança é aplicada

Só com tudo pronto, os arquivos novos substituem os antigos, de uma vez. Se o download ou a cópia falharem no meio, nada muda na sua instalação.

</section>

<section data-sigla="ES" data-nome="Abra o EuroScope" data-alt="0" markdown>

### Abra o EuroScope

Abra o EuroScope no perfil da FIR e confira o AIRAC do setor carregado. Pronto para a sessão.

</section>

</div>

## Guias

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } **Instalação**

    ---

    Trilha da instalação pelo Vectors ATC Hub, do login no AeroNav e da primeira instalação das FIRs.

    [:octicons-arrow-right-24: Instalação](instalacao.pt.md)

-   :material-folder-sync:{ .lg .middle } **Utilização**

    ---

    O painel, a atualização a cada AIRAC, o que é preservado, as configurações e a solução dos problemas comuns.

    [:octicons-arrow-right-24: Utilização](utilizacao.pt.md)

</div>

!!! info "Projeto independente"
    O Sector File Manager não é um programa da VATSIM, do AeroNav, da Navigraph ou do EuroScope. Dúvidas e problemas do programa vão para a página de [issues do projeto](https://github.com/VectorsATCGroup/euroscope-sector-file-manager/issues). Erros no conteúdo do setor, como uma frequência ou um procedimento errado, vão para a equipe da Vatsim Brasil.
