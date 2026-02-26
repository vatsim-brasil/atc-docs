![Header Image](.github/docs/img/readme_banner.svg)

# Instalação

Após instalar o python, execute o comando a seguir para instalar as dependências:

```bash
pip install -r requirements.txt
```

No windows, talvez seja necessário utilizar:

```bash
python -m pip install -r requirements.txt
```

## Desenvolvimento Local

Para desenvolvimento local e testes, utilize:

```bash
mkdocs serve
```

Ou use o script de desenvolvimento otimizado (recomendado):

```bash
./dev.sh
```

No windows, talvez seja necessário utilizar:

```bash
python -m mkdocs serve
```

### Fast Reload (Recomendado para projetos grandes)

Para um reload mais rápido durante o desenvolvimento, especialmente em projetos grandes, utilize a flag `--dirtyreload`:

```bash
mkdocs serve --dirtyreload
```

Esta opção recompila apenas a página atual quando há mudanças, tornando o rebuild muito mais rápido.

### Outras opções úteis

- **Observar arquivos do tema**: `mkdocs serve --watch-theme`
- **Abrir navegador automaticamente**: `mkdocs serve --open`
- **Servir em endereço/porta customizada**: `mkdocs serve --dev-addr 0.0.0.0:8080`
- **Modo limpo (rebuild completo)**: `mkdocs serve --clean`

Após executar, será exibida a url de acesso local (geralmente `http://127.0.0.1:8000/`).

O servidor observa automaticamente mudanças em:

- Arquivos em `docs/`
- Arquivo `mkdocs.yml`
- Diretório `includes/` (abreviações e snippets)
- Diretório `overrides/` (customizações do tema)

## Links úteis

- [Documentação do mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
- [Referência rápida](https://squidfunk.github.io/mkdocs-material/reference/)
