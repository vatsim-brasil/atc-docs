<p align="center">
  <img src=".github/docs/img/readme_banner.svg" alt="Portal ATC Banner" width="100%">
</p>

# Portal de Documentação ATC — VATSIM Brasil

Este é o repositório central do **Portal ATC da VATSIM Brasil** (disponível em [atc.vatsim.com.br](https://atc.vatsim.com.br)). O objetivo deste portal é fornecer aos controladores de tráfego aéreo virtuais da divisão brasileira um local unificado de referência com manuais, regulamentos, documentações técnicas e guias para softwares de simulação.

---

## 🚀 Como Começar

### Pré-requisitos
* **Python 3.8+** instalado em sua máquina.

### 📥 Instalação das Dependências

Instale os pacotes necessários especificados em [requirements.txt](./requirements.txt):

**Linux / macOS:**
```bash
pip install -r requirements.txt
```

**Windows:**
```bash
python -m pip install -r requirements.txt
```

---

## 💻 Desenvolvimento Local

Para rodar o portal localmente em modo de visualização em tempo real (live reload), você pode escolher uma das seguintes opções:

### Opção 1: Usando o script otimizado (Recomendado)
```bash
./dev.sh
```

### Opção 2: Comando MkDocs padrão
```bash
mkdocs serve
```
*No Windows, caso o comando acima não seja reconhecido diretamente:*
```bash
python -m mkdocs serve
```

### ⚡ Desenvolvimento Ágil (Fast Reload)
Para projetos com muitas páginas, o carregamento de mudanças pode se tornar lento. Use o parâmetro `--dirtyreload` para compilar apenas a página que foi modificada:
```bash
mkdocs serve --dirtyreload
```

### ⚙️ Opções Úteis de Execução
* **Abrir o navegador automaticamente**: `mkdocs serve --open`
* **Observar mudanças de arquivos de tema/estilo**: `mkdocs serve --watch-theme`
* **Definir porta e endereço personalizados**: `mkdocs serve --dev-addr 0.0.0.0:8080`
* **Limpar cache e reconstruir do zero**: `mkdocs serve --clean`

Após o servidor iniciar, acesse o endereço fornecido no terminal (geralmente [http://127.0.0.1:8000/](http://127.0.0.1:8000/)).

---

## 📂 Estrutura do Repositório

O projeto é organizado da seguinte forma:

* 📁 **[docs/](./docs)**: Contém todas as páginas de documentação escritas em Markdown.
  * 📁 `MOP/`: Manual de Operações Padrão.
  * 📁 `documentos/`: Tratados, regimentos e resoluções.
  * 📁 `fundamentos/`: Conceitos e guias de softwares (como o EuroScope).
* 📁 **[includes/](./includes)**: Snippets de texto reutilizáveis e lista global de abreviações.
* 📁 **[overrides/](./overrides)**: Customizações do tema MkDocs Material (HTML/JS/CSS adicionais).
* 📄 **[mkdocs.yml](./mkdocs.yml)**: Arquivo principal de configuração do site, definição de plugins e estrutura do menu de navegação.

---

## 🤝 Como Contribuir

Toda ajuda para manter nossos manuais e documentações atualizados é extremamente bem-vinda! Se você encontrou um erro de digitação, uma informação desatualizada ou quer propor um novo tutorial, siga o guia detalhado abaixo.

### 📝 Boas Práticas
* **Clareza e Tom**: Utilize uma linguagem formal, clara e objetiva. Lembre-se de que a documentação é voltada para a instrução de novos controladores.
* **Formatação**: Utilize os recursos do [MkDocs Material](https://squidfunk.github.io/mkdocs-material/reference/), como blocos de alerta (admonitions), tabelas e listas de tarefas para deixar o texto escaneável.
* **Links**: Sempre que linkar outros documentos internos do Portal, prefira caminhos relativos (ex: `../fundamentos/euroscope.md`) em vez de URLs completas.

### 🛠️ Passo a Passo Técnico

#### 1. Prepare o Ambiente
Primeiro, faça um **Fork** deste repositório para a sua conta do GitHub e clone-o localmente:
```bash
git clone https://github.com/seu-usuario/atc-docs.git
cd atc-docs
```

Instale as dependências necessárias:

**Linux / macOS:**
```bash
pip install -r requirements.txt
```

**Windows:**
```bash
python -m pip install -r requirements.txt
```

#### 2. Crie uma Branch para suas Alterações
Sempre crie uma nova branch a partir da branch principal (`main` ou `master`):
```bash
git checkout -b minha-melhoria
```
*Dica: Use nomes descritivos para a branch, como `docs/correcao-mop` ou `feature/guia-euroscope`.*

#### 3. Faça as Alterações e Teste Localmente
Edite os arquivos markdown desejados dentro da pasta `docs/`. Antes de submeter, inicie o servidor local para verificar a renderização e garantir que não há erros de compilação ou links quebrados:
```bash
mkdocs serve
```

#### 4. Commit e Push
Crie commits claros e objetivos sobre o que foi alterado. Por exemplo:
```bash
git add .
git commit -m "docs: corrige frequência da torre de Congonhas no MOP"
git push origin minha-melhoria
```

#### 5. Abra um Pull Request
Vá até a página do repositório original no GitHub (`vatsim-brasil/atc-docs`) e você verá uma sugestão para abrir um **Pull Request** a partir da sua branch. Descreva brevemente o que foi alterado e o motivo da modificação. Um dos revisores irá analisar e mesclar sua contribuição!

---

## 🔗 Links Úteis

* 📖 [Documentação do MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
* 🛠️ [Referência de Configuração e Extensões](https://squidfunk.github.io/mkdocs-material/reference/)
* 🌐 [Portal ATC da VATSIM Brasil](https://atc.vatsim.com.br)
