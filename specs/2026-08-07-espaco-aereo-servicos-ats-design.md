# Design — Manual de Espaço Aéreo Brasileiro e Serviços ATS

**Data:** 07/08/2026
**Status:** aprovado, pendente de implementação
**Repositório:** `atc-docs` (Portal ATC — VATSIM Brasil)

---

## 1. Contexto e motivação

O portfólio de manuais do Portal ATC hoje cobre cinco assuntos:

| Manual | Rating servido |
| --- | --- |
| Fraseologia Aeronáutica (IFR) | S1–S2 |
| Fraseologia para Voo Visual (VFR) | S2 |
| Circuito de Tráfego | S2 |
| Meteorologia Aeronáutica | S1+ |
| Plano de Voo (FPL) | S1 |

Duas lacunas saltam desse mapa:

1. **O portfólio para em S2 (TWR).** S3 (APP) e C1 (CTR) — os ratings com o treinamento mais longo, 10h e 15h de trainee — não têm material próprio.
2. **Falta a base conceitual que os manuais existentes já pressupõem.** O Manual de Circuito de Tráfego distingue "aeródromo controlado" de "não controlado"; o de Fraseologia VFR fala em "travessia de espaço aéreo controlado", em CONTROLE, INFORMAÇÃO e RÁDIO. Nenhum documento do portal define ATZ, CTR, TMA, CTA, UTA ou FIR, nem explica por que cada órgão presta um serviço diferente. Hoje o membro deduz.

Este manual fecha a lacuna nº 2 e serve de pré-requisito para o material radar que fecha a nº 1: não se ensina vetoração e separação sem antes fixar estrutura vertical e classes de espaço aéreo.

## 2. Objetivo

Produzir um manual didático, de leitura linear, que responda três perguntas para qualquer membro entre S1 e C1:

- **Onde estou?** Qual divisão do espaço aéreo, com quais limites.
- **O que vale aqui?** Qual classe, quais serviços prestados, quem separa quem.
- **O que eu faço?** Qual órgão presta o serviço e qual a minha jurisdição na rede.

### Não-objetivos

Declarados explicitamente no `index`, no mesmo formato que o Manual de Fraseologia VFR usa para delimitar escopo:

- emergências e contingências;
- falha de comunicação;
- interceptação de aeronaves;
- espaços aéreos condicionados (áreas proibidas, restritas e perigosas);
- rotas ATS e estrutura de aerovias;
- vetoração e separação radar.

Cada um desses é candidato a manual próprio no futuro.

## 3. Eixo editorial

**Híbrido: teoria + aplicação VATSIM.**

Cada conceito é apresentado primeiro na forma normativa (ICA/AIP) e recebe logo abaixo um bloco de tradução operacional para a rede:

```markdown
!!! tip "Na rede (Vatbrz)"
    Tradução prática: qual posição do EuroScope corresponde, o que você
    pode e não pode autorizar, onde isso aparece no sector file.
```

Alternativas consideradas e descartadas:

- **Teoria e prática em capítulos separados.** Mais limpo conceitualmente, mas obriga o leitor a pular para frente e voltar. Nenhum manual do portfólio faz isso.
- **Tabs `=== "Teoria"` / `=== "Na rede"`.** Compacto, mas as tabs já carregam significado fixo de idioma no portal (`:flag_br:` / `:flag_gb:` / `:flag_es:`). Reusar o componente para outra semântica confunde.

O bloco `!!! tip` foi escolhido porque mantém um único fio de leitura, casa com o uso de admonitions já consolidado no portfólio e permite que quem só quer a prática varra os blocos coloridos.

## 4. Arquitetura de arquivos

```
docs/documentos/manuais/espaco-aereo-servicos-ats/
├── .pages
├── index.pt.md
├── 01-estrutura.pt.md
├── 02-classes.pt.md
├── 03-servicos.pt.md
├── 04-orgaos.pt.md
├── 05-regras.pt.md
├── 06-checklist.pt.md
└── img/
```

### `.pages`

Segue o formato dos demais manuais — `title`, `collapse: false` e `nav` explícita:

```yaml
title: Manual de Espaço Aéreo e Serviços ATS
collapse: false
nav:
  - Introdução: index.pt.md
  - Estrutura do Espaço Aéreo: 01-estrutura.pt.md
  - Classes de Espaço Aéreo: 02-classes.pt.md
  - Serviços de Tráfego Aéreo: 03-servicos.pt.md
  - Órgãos ATS e Posições: 04-orgaos.pt.md
  - Regras de Voo e Níveis: 05-regras.pt.md
  - Checklist Rápido: 06-checklist.pt.md
```

### Integração com a navegação

`docs/documentos/.pages` usa `children: - ...` (auto-descoberta). O diretório novo aparece sozinho, sem edição. `docs/.pages` também permanece intocado.

### Internacionalização

Todos os arquivos nascem com sufixo `.pt.md`. O plugin `mkdocs-static-i18n` está configurado com `docs_structure: suffix` e `fallback_to_default: true`, então uma versão em inglês futura é apenas somar `.en.md` ao lado, sem renomear nem mover nada.

Observação: o `manual-circuito-trafego` usa `.md` puro e é a exceção do portfólio. Não replicar.

## 5. Convenções herdadas do portfólio

Levantadas por inspeção dos cinco manuais existentes. Todas obrigatórias:

| Convenção | Aplicação |
| --- | --- |
| Front matter | `title` + `icon` em todo arquivo |
| Ícone raiz | `material/map-marker-radius` no `index` |
| Snippet de abreviações | `--8<-- "includes/abreviacoes.md"` no topo de cada capítulo |
| Imagem de cabeçalho | `![Título - Capítulo](img/nome.png)` seguido de uma linha com `#` isolado |
| Tabela de revisão | colunas Revisão / Data / Descrição / Revisor, no `index` |
| Footnotes | `[^n]` linkando `publicacoes.decea.mil.br` |
| Aviso de simulação | `!!! warning "Importante"` no `index` |
| Links cruzados | `!!! tip "Leitura complementar"` apontando manuais irmãos |
| Admonitions | `!!! note` / `tip` / `warning` / `danger` conforme o peso da informação |

### Tabela de revisão inicial

```markdown
| Revisão | Data       | Descrição         | Revisor |
| ------- | ---------- | ----------------- | ------- |
| 08/2026 | 07/08/2026 | Criação do Manual | 930847  |
```

### Links cruzados a incluir no `index`

- Manual de Fraseologia para Voo Visual — usa os órgãos e classes definidos aqui.
- Manual de Fraseologia Aeronáutica — idem, na ponta IFR.
- Manual de Circuito de Tráfego — depende da definição de ATZ e de aeródromo controlado.
- Seção MOP — este manual dá a teoria, o MOP dá os limites locais.

## 6. Conteúdo por capítulo

### `index.pt.md` — Introdução

Apresentação, escopo e não-escopo, documentos de referência, tabela de revisão, aviso de simulação, roteiro de leitura ("Como usar este manual", no formato do Fraseologia VFR) e links cruzados.

### `01-estrutura.pt.md` — Estrutura do Espaço Aéreo

Definição, limites e responsável de cada divisão: **ATZ, CTR, TMA, CTA, UTA, FIR**. Diferença entre espaço aéreo controlado e não controlado. Projeções verticais e laterais.

Fonte: ICA 100-12, Cap. II (Art. 7º abreviaturas, Art. 8º definições) e Anexo VII; AIP Brasil ENR 2.

Diagrama: **SVG-1**, corte vertical.

Nota obrigatória: a FIR Atlântico tem procedimentos distintos das FIR continentais — a própria ICA 100-12 trata as duas separadamente (Art. 96 e Art. 97). Registrar a existência da distinção sem entrar no mérito de falha de comunicação, que está fora do escopo.

Bloco "Na rede": onde ler esses limites no sector file do EuroScope.

### `02-classes.pt.md` — Classes de Espaço Aéreo

Matriz das classes **A a G**: separação provida, serviços prestados, requisitos para VFR e IFR, comunicação obrigatória, necessidade de autorização, limite de velocidade.

Fonte: **ICA 100-37 (Serviços de Tráfego Aéreo)** e AIP Brasil ENR 1.4. A ICA 100-12 **não** contém a matriz — ela remete expressamente à ICA 100-37 ao tratar dos "espaços aéreos ATS classe A, B, C, D e E".

Ancoragens já verificadas na ICA 100-12, úteis como reforço:

- Art. 111 — requisitos para voos VFR nas Classes B, C e D;
- Art. 115 — voos VFR nas Classes E, F e G;
- Art. 113 — VFR dentro de TMA ou CTR.

Diagrama: **SVG-2**, matriz de classes.

Bloco "Na rede": qual classe você opera em cada posição da Vatbrz.

### `03-servicos.pt.md` — Serviços de Tráfego Aéreo

Os três serviços — **Controle de Tráfego Aéreo, Informação de Voo e Alerta** — com o que cada um pode e não pode fazer, e qual órgão presta cada um.

Fonte: ICA 100-37; ICA 100-12 Cap. IV Seção VI (Art. 77 a 98).

Reforça, agora com a base normativa, o que o Manual de Fraseologia VFR já afirma na prática: INFORMAÇÃO e RÁDIO não controlam e não usam verbos no imperativo que impliquem controle.

### `04-orgaos.pt.md` — Órgãos ATS e Posições

Correspondência entre órgão real e posição na rede:

| Órgão ATS | Posição VATSIM | Espaço aéreo típico |
| --- | --- | --- |
| Centro de Controle de Área (ACC) | `_CTR` | CTA / UTA / FIR |
| Controle de Aproximação (APP) | `_APP` | TMA / CTR |
| Torre de Controle (TWR) | `_TWR` | ATZ / CTR |
| Controle de Solo | `_GND` | área de manobras |
| Autorização de Tráfego | `_DEL` | pátio |

Inclui jurisdição, indicativos de chamada e o conceito de cobertura *top-down*.

Fonte: ICA 100-37; MCA 100-16 para os indicativos.

Diagrama: **SVG-3**, cadeia de transferência entre órgãos.

### `05-regras.pt.md` — Regras de Voo e Níveis

- **Níveis de cruzeiro semicirculares** — ICA 100-12 Art. 22, Art. 123/124 (VFR), Art. 142 (IFR) e Anexo IV. O Anexo IV traz a tabela geral, a tabela 8 para espaço aéreo RVSM e a tabela 9 para quando os procedimentos RVSM são suspensos.
- **Mínimos VMC** — ICA 100-12 Art. 104, Tabela 1: visibilidade em voo e distância de nuvens por classe e faixa de altitude. Inclui a regra do §1º: quando a altitude de transição for inferior a 10.000 pés AMSL, usa-se o FL100 no lugar de 10.000 pés.
- **Altitude e nível de transição** — ICA 100-12 Art. 22; QNH abaixo, QNE acima.
- **VFR especial** — ICA 100-12 Cap. V Seção VIII (Art. 128 a 135), aplicável em CTR e ATZ.

Bloco "Na rede": como identificar nível de cruzeiro incorreto no strip.

### `06-checklist.pt.md` — Checklist Rápido

Consulta rápida no padrão "estou nesta classe → separo quem, exijo o quê, presto qual serviço". Consolida os capítulos 02, 03 e 05. Sem conteúdo novo.

## 7. Diagramas

Três SVG inline, autorais. Não há dependência externa e o `attr_list` + `md_in_html` já habilitados no `mkdocs.yml` permitem SVG inline no Markdown.

| ID | Capítulo | Conteúdo |
| --- | --- | --- |
| SVG-1 | 01 | Corte vertical: solo → ATZ → CTR → TMA → CTA → UTA, com FIR envolvendo tudo |
| SVG-2 | 02 | Matriz visual das classes A–G contra separação, serviços e requisitos |
| SVG-3 | 04 | Cadeia DEL → GND → TWR → APP → CTR e o espaço aéreo de cada elo |

### Requisito de tema

O portal tem alternância clara/escura (`scheme: default` / `scheme: slate`). Cada SVG carrega `<style>` interno com:

1. `@media (prefers-color-scheme: dark)` como sinal padrão; e
2. seletor `[data-md-color-scheme="slate"]` para o toggle manual do Material, que precisa vencer sobre a preferência do sistema.

Sem isso, o diagrama fica ilegível para metade dos leitores.

### Imagens de cabeçalho

Os PNG de cabeçalho seguem um template gráfico autoral do portal que não é reproduzível aqui. Ficam como **pendência do mantenedor**. Os arquivos são escritos já com a referência `![...](img/...png)` no lugar certo, seguindo a convenção; a imagem entra depois sem edição de texto.

Nomes esperados em `img/`:

```
manual-espaco-aereo-intro.png
manual-espaco-aereo-estrutura.png
manual-espaco-aereo-classes.png
manual-espaco-aereo-servicos.png
manual-espaco-aereo-orgaos.png
manual-espaco-aereo-regras.png
manual-espaco-aereo-checklist.png
```

## 8. Abreviações

`includes/abreviacoes.md` é anexado automaticamente a todas as páginas via `pymdownx.snippets.auto_append`. Faltam termos centrais deste manual. Acrescentar ao arquivo global, no formato existente `*[SIGLA]: Português / English`:

`ATZ`, `CTA`, `UTA`, `ACC`, `AFIS`, `AIS`, `EAC`, `AMSL`, `QNH`, `QNE`, `RVSM`, `ALT TRANS`, `NVL TRANS`.

Ganho colateral: os manuais existentes passam a exibir tooltip para essas siglas também.

Observação sobre redundância: os capítulos importam `--8<-- "includes/abreviacoes.md"` manualmente **e** o `auto_append` do `mkdocs.yml` já faz isso. Manter a importação manual por consistência com o portfólio; não é o escopo deste trabalho corrigir a duplicação.

## 9. Verificação factual

Regra dura. Conteúdo aeronáutico errado em material didático é pior que material ausente.

1. **Nenhuma afirmação normativa entra sem fonte extraída do documento oficial.** Nada escrito de memória.
2. **ICA 100-12** já foi obtida e extraída: edição de 28/11/2024, aprovada pela Portaria DECEA/DNOR1 nº 1.536, de 31/10/2024, que revogou a edição de 2016 e as modificações de 2018. 84 páginas.
3. **ICA 100-37 e AIP Brasil ENR 1.4 precisam ser baixadas e extraídas antes de escrever os capítulos 02, 03 e 04.** Sem elas, a matriz de classes não pode ser redigida.
4. **Toda tabela normativa cita artigo, seção ou parágrafo** em footnote.
5. **Valores locais ou variáveis não são fixados no manual.** Limites de TMA, altitude de transição por aeródromo e afins apontam para AIP, carta e MOP.
6. **Revisão técnica por controlador antes do merge.** Este documento sai como rascunho revisável, não como fonte de autoridade.

### Armadilha de data identificada

A ICA 100-12 tem regime transitório: o Art. 96 vigora até 31/12/2026 e o Art. 97 já vale na FIR Atlântico, passando a valer nas demais FIR em 1º/01/2027. O assunto (falha de comunicação) está fora do escopo, mas a existência de dois regimes por FIR precisa ser sinalizada no capítulo 01.

## 10. Critérios de aceite

- [ ] Sete arquivos `.pt.md` criados, com front matter, snippet de abreviações e referência de imagem de cabeçalho.
- [ ] `.pages` com `title`, `collapse: false` e `nav` explícita nas sete entradas.
- [ ] Manual aparece na navegação do portal sem alteração em `docs/.pages` ou `docs/documentos/.pages`.
- [ ] Toda afirmação normativa referenciada em footnote para ICA 100-12, ICA 100-37, AIP ou MCA 100-16.
- [ ] Matriz de classes A–G redigida a partir da ICA 100-37 e da AIP ENR 1.4, nunca de memória.
- [ ] Três SVG inline legíveis nos temas claro e escuro.
- [ ] Novas siglas adicionadas a `includes/abreviacoes.md`.
- [ ] Cada capítulo tem ao menos um bloco `!!! tip "Na rede (Vatbrz)"`.
- [ ] Escopo e não-escopo declarados no `index`.
- [ ] `dev.sh` builda sem warning novo; navegação, i18n e SVG conferidos nos dois temas.

## 11. Riscos e pendências

| Item | Situação |
| --- | --- |
| PNG de cabeçalho | Pendência do mantenedor — template gráfico não reproduzível aqui |
| ICA 100-37 e AIP ENR 1.4 | A obter antes dos capítulos 02–04 |
| Revisão técnica | Obrigatória antes do merge; o autor não é autoridade aeronáutica |
| Versão em inglês | Fora da v1; estrutura `.pt.md` já a viabiliza sem refatoração |

## 12. Entrega

Trabalho na branch `develop`, seguindo a convenção do repositório (os manuais anteriores foram commitados diretamente nela e integrados a `master` via pull request). Mensagens de commit em inglês, no padrão do histórico:

```
feat: add airspace and ATS services manual
```

Build local de verificação via `dev.sh`.
