# Manual de Espaço Aéreo e Serviços ATS — imagens de cabeçalho pendentes

Este manual referencia sete imagens de cabeçalho que ainda não foram
produzidas. Elas seguem o mesmo template gráfico dos demais manuais do
portal e devem ser geradas pelo mantenedor.

Diretório de destino:

```
docs/documentos/manuais/espaco-aereo-servicos-ats/img/
```

| Arquivo | Capítulo |
| --- | --- |
| `manual-espaco-aereo-intro.png` | Introdução |
| `manual-espaco-aereo-estrutura.png` | Estrutura do Espaço Aéreo |
| `manual-espaco-aereo-classes.png` | Classes de Espaço Aéreo |
| `manual-espaco-aereo-servicos.png` | Serviços de Tráfego Aéreo |
| `manual-espaco-aereo-orgaos.png` | Órgãos ATS e Posições |
| `manual-espaco-aereo-regras.png` | Regras de Voo e Níveis |
| `manual-espaco-aereo-checklist.png` | Checklist Rápido |

As referências já estão no lugar certo em cada capítulo. Basta depositar os
arquivos no diretório acima com estes nomes exatos — nenhuma edição de
Markdown é necessária.

Enquanto os arquivos não existirem, o `mkdocs build` emite um aviso por
imagem e por idioma (14 avisos no total). São avisos esperados e
documentados por esta pendência, não regressões.

> Este arquivo vive em `specs/`, fora de `docs/`, de propósito: dentro de
> `docs/` ele seria construído e publicado como uma página do portal,
> indexada pela busca nos dois idiomas.
