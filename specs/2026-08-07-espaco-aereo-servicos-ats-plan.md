# Manual de Espaço Aéreo e Serviços ATS — Plano de Implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar no Portal ATC um manual de sete capítulos sobre estrutura do espaço aéreo brasileiro, classes ATS e serviços de tráfego aéreo, com eixo híbrido teoria + prática VATSIM.

**Architecture:** Site MkDocs Material estático. O manual é um diretório de arquivos Markdown em `docs/documentos/manuais/`, descoberto automaticamente pelo plugin `awesome-pages` e ordenado por um `.pages` local. Nenhum código de aplicação é escrito. O "teste" de cada tarefa é a combinação de build limpo do MkDocs, conferência de rastreabilidade das citações contra o texto oficial extraído, e inspeção visual nos temas claro e escuro.

**Tech Stack:** MkDocs 1.6.0, mkdocs-material 9.5.28, mkdocs-awesome-pages-plugin 2.9.2, mkdocs-static-i18n 1.2.3, pymdownx (superfences, snippets, tabbed, details), SVG inline.

**Spec:** `specs/2026-08-07-espaco-aereo-servicos-ats-design.md`

## Global Constraints

- **Branch:** `develop`. Não criar branch nova — os manuais anteriores foram commitados diretamente nela e integrados a `master` via pull request.
- **Idioma dos arquivos:** todos nascem com sufixo `.pt.md`. Nunca `.md` puro.
- **Idioma do conteúdo:** português brasileiro. Mensagens de commit em inglês.
- **Diretório do manual:** `docs/documentos/manuais/espaco-aereo-servicos-ats/`
- **Fontes normativas admitidas:** ICA 100-12 (ed. 28/11/2024), ICA 100-37 (ed. em vigor 27/11/2025), MCA 100-16, AIP Brasil. Nenhuma outra.
- **Regra dura:** nenhuma afirmação normativa entra sem estar respaldada por trecho extraído do documento oficial. Nada escrito de memória.
- **Toda tabela normativa** cita artigo, inciso ou anexo em footnote no formato `[^n]`, com link para `https://publicacoes.decea.mil.br/publicacao/<doc>`.
- **Valores locais nunca são fixados** no manual: limites de TMA, altitude de transição por aeródromo e afins apontam para AIP, carta e seção MOP.
- **Todo capítulo** começa com front matter (`title`, `icon`), a linha `--8<-- "includes/abreviacoes.md"`, a referência da imagem de cabeçalho e uma linha contendo apenas `#`.
- **Todo capítulo** tem ao menos um bloco `!!! tip "Na rede (Vatbrz)"`.
- **Nenhum PDF ou texto extraído é commitado.** Ficam em `.sources/`, que é gitignored.
- **Revisor nas tabelas de revisão:** `930847`.
- **Data de criação:** `07/08/2026`, revisão `08/2026`.

---

## Estrutura de arquivos

| Arquivo | Responsabilidade |
| --- | --- |
| `.gitignore` | Passa a ignorar `.sources/` |
| `includes/abreviacoes.md` | Ganha as siglas do domínio de espaço aéreo |
| `docs/documentos/manuais/espaco-aereo-servicos-ats/.pages` | Título e ordem do manual na navegação |
| `.../index.pt.md` | Apresentação, escopo, não-escopo, referências, revisão, links cruzados |
| `.../01-estrutura.pt.md` | ATZ, CTR, TMA, CTA, UTA, FIR + SVG-1 |
| `.../02-classes.pt.md` | Matriz das classes A–G + SVG-2 |
| `.../03-servicos.pt.md` | Controle, Informação de Voo, Alerta, Assessoramento |
| `.../04-orgaos.pt.md` | Órgãos ATS ↔ posições VATSIM + SVG-3 |
| `.../05-regras.pt.md` | Níveis de cruzeiro, VMC, transição, VFR especial |
| `.../06-checklist.pt.md` | Consulta rápida consolidada |
| `.../img/` | Imagens de cabeçalho (pendência do mantenedor) |

Não editar `docs/.pages` nem `docs/documentos/.pages`. O segundo usa `children: - ...` (auto-descoberta) e já resolve a inclusão do diretório novo.

---

### Task 1: Fontes normativas

Obter e extrair os dois documentos oficiais que sustentam o manual inteiro. Sem esta tarefa, nenhum capítulo pode ser escrito sem violar a regra dura.

**Files:**
- Create: `.sources/` (gitignored, não versionado)
- Modify: `.gitignore`

**Interfaces:**
- Produces: `.sources/ica-100-12.txt` e `.sources/ica-100-37.txt` — texto integral com marcadores `--- PAGE n ---`, consumidos por todas as tarefas seguintes para extrair citações verbatim.

- [ ] **Step 1: Ignorar o diretório de fontes**

Acrescentar ao final de `.gitignore`:

```
.sources
```

- [ ] **Step 2: Baixar os dois PDF**

```bash
mkdir -p .sources
curl -sL -o .sources/ica-100-12.pdf \
  "https://missaoeaof.com.br/downloads/ica/ICA%20100-12%2028.11.2024.pdf"
curl -sL -o .sources/ica-100-37.pdf \
  "https://missaoeaof.com.br/downloads/ica/ICA%20100-37%2027.11.2025.pdf"
file -b .sources/ica-100-12.pdf .sources/ica-100-37.pdf
```

Esperado: duas linhas começando com `PDF document`. A primeira com 84 páginas, a segunda com 302.

Estes são espelhos de terceiro. A fonte oficial é `https://publicacoes.decea.mil.br/publicacao/ica-100-12` e `.../ica-100-37`, que servem os arquivos por um botão "Visualizar" sem URL direta estável. O Step 4 valida que o espelho corresponde ao documento oficial.

- [ ] **Step 3: Extrair o texto**

```bash
uv run --quiet --with pypdf python -c "
from pypdf import PdfReader
for slug in ('ica-100-12', 'ica-100-37'):
    r = PdfReader(f'.sources/{slug}.pdf')
    txt = '\n'.join(f'--- PAGE {i+1} ---\n' + (p.extract_text() or '')
                    for i, p in enumerate(r.pages))
    open(f'.sources/{slug}.txt', 'w').write(txt)
    print(slug, len(r.pages), 'páginas,', len(txt), 'caracteres')
"
```

Esperado:
```
ica-100-12 84 páginas, ~167000 caracteres
ica-100-37 302 páginas, ~578000 caracteres
```

Se `uv` não estiver disponível, usar `venv/bin/pip install pypdf` e rodar com `venv/bin/python`.

- [ ] **Step 4: Validar a procedência dos arquivos**

```bash
grep -m1 "PORTARIA DECEA" .sources/ica-100-12.txt
grep -m1 "PORTARIA DECEA" .sources/ica-100-37.txt
grep -c "Art. 21" .sources/ica-100-37.txt
```

Esperado:
- ICA 100-12 → `PORTARIA DECEA/DNOR1 N° 1.536, DE 31 DE OUTUBRO DE 2024`
- ICA 100-37 → `PORTARIA DECEA/DNOR1 No 1.537, DE 4 DE NOVEMBRO DE 2024`
- terceiro comando retorna um número maior que zero (Art. 21 é a classificação dos espaços aéreos ATS)

Se qualquer portaria divergir, **parar**. O espelho está desatualizado e a fonte precisa ser obtida manualmente em `publicacoes.decea.mil.br`.

- [ ] **Step 5: Confirmar que os PDF não entram no git**

```bash
git status --short
```

Esperado: apenas ` M .gitignore`. Nenhuma menção a `.sources/`.

- [ ] **Step 6: Commit**

```bash
git add .gitignore
git commit -m "chore: ignore local normative source cache"
```

---

### Task 2: Siglas, esqueleto e introdução

Cria a espinha do manual: siglas globais, `.pages` e `index.pt.md`. Ao fim desta tarefa o manual já aparece na navegação do portal, mesmo com os capítulos ainda ausentes.

**Files:**
- Modify: `includes/abreviacoes.md`
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/.pages`
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/index.pt.md`

**Interfaces:**
- Consumes: `.sources/*.txt` da Task 1.
- Produces: o `.pages` com as sete entradas de navegação, referenciado por todas as tarefas seguintes; o padrão de front matter e cabeçalho replicado nos capítulos 01 a 06.

- [ ] **Step 1: Acrescentar as siglas**

Ao final de `includes/abreviacoes.md`, mantendo o formato `*[SIGLA]: Português / English` já usado nas 72 linhas existentes:

```
*[ATZ]: Zona de Tráfego de Aeródromo / Aerodrome Traffic Zone
*[CTA]: Área de Controle / Control Area
*[UTA]: Área de Controle Superior / Upper Control Area
*[ACC]: Centro de Controle de Área / Area Control Centre
*[AIS]: Serviço de Informação Aeronáutica / Aeronautical Information Service
*[EAC]: Espaço Aéreo Condicionado / Conditional Airspace
*[AMSL]: Acima do Nível Médio do Mar / Above Mean Sea Level
*[QNH]: Ajuste de altímetro para indicar altitude / Altimeter setting to indicate altitude
*[QNE]: Ajuste de altímetro padrão, 1013,2 hPa / Standard altimeter setting, 1013.2 hPa
*[RVSM]: Separação Vertical Mínima Reduzida / Reduced Vertical Separation Minimum
*[IAS]: Velocidade Indicada / Indicated Airspeed
```

Não remover nem reordenar nada do que já existe. As siglas `ATC`, `ATS`, `TMA`, `FIR`, `CTR`, `VFR`, `IFR`, `VMC`, `IMC`, `AIP`, `SID`, `STAR`, `DEL`, `GND`, `TWR`, `APP`, `CTR`, `FSS`, `SSR` e `AFIS` já estão no arquivo — não duplicar.

- [ ] **Step 2: Verificar que não há sigla duplicada**

```bash
grep -oE '^\*\[[A-Z ]+\]' includes/abreviacoes.md | sort | uniq -d
```

Esperado: saída vazia.

- [ ] **Step 3: Criar o `.pages`**

`docs/documentos/manuais/espaco-aereo-servicos-ats/.pages`:

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

- [ ] **Step 4: Escrever o `index.pt.md`**

Front matter e cabeçalho exatos:

```markdown
---
title: Introdução
icon: material/map-marker-radius
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Introdução](img/manual-espaco-aereo-intro.png)

#

## Apresentação
```

O corpo cobre, nesta ordem:

1. **Apresentação** — o manual responde três perguntas: onde estou, o que vale aqui, o que eu faço. Explicar que os demais manuais do portal já pressupõem estes conceitos sem defini-los.
2. **Tabela de revisão**, exatamente:

```markdown
| Revisão | Data       | Descrição         | Revisor |
| ------- | ---------- | ----------------- | ------- |
| 08/2026 | 07/08/2026 | Criação do Manual | 930847  |
```

3. **Sobre este Manual** — construído sobre ICA 100-37[^1] e ICA 100-12[^2], com apoio do MCA 100-16[^3] e da AIP Brasil.
4. **Escopo** — o que o manual cobre.
5. **Fora do escopo** — lista explícita, no formato que o Manual de Fraseologia para Voo Visual usa: emergências e contingências, falha de comunicação, interceptação, espaços aéreos condicionados (áreas proibidas, restritas e perigosas), rotas ATS e aerovias, vetoração e separação radar.
6. **Aviso de simulação**:

```markdown
!!! warning "Importante"
    Conteúdo destinado ao ambiente de simulação de voo. Em operações reais, utilize sempre as publicações oficiais vigentes, as cartas aeronáuticas e os canais AIS e ATS.
```

7. **Como usar este manual** — lista numerada de 6 itens, um por capítulo.
8. **Leitura complementar**:

```markdown
!!! tip "Leitura complementar"
    Este manual é a base conceitual dos demais. O [Manual de Fraseologia para Voo Visual](../fraseologia-voo-visual/index.pt.md) e o [Manual de Fraseologia Aeronáutica](../fraseologia-aeronautica/index.pt.md) usam os órgãos e as classes definidos aqui. O [Manual de Circuito de Tráfego](../manual-circuito-trafego/index.md) depende da definição de ATZ e de aeródromo controlado. Os limites locais de cada TMA, CTR e ATZ estão na seção **Manuais Operacionais**.
```

Footnotes ao final:

```markdown
[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): regulamenta no Brasil os Serviços de Tráfego Aéreo previstos no Anexo 11 e no Doc 4444 da OACI. Edição em vigor em 27/11/2025.
[^2]: [**ICA 100-12, Regras do Ar**](https://publicacoes.decea.mil.br/publicacao/ica-100-12): estabelece as regras aplicáveis à operação de aeronaves no espaço aéreo brasileiro. Edição em vigor em 28/11/2024.
[^3]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): estabelece os padrões de fraseologia de tráfego aéreo, em complemento ao disposto na **ICA 100-12**.
```

- [ ] **Step 5: Build**

```bash
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | tee /tmp/atcdocs-build.log
grep -iE "warning|error" /tmp/atcdocs-build.log || echo "sem avisos"
```

Esperado: build conclui; nenhum aviso novo mencionando `espaco-aereo-servicos-ats`. Avisos preexistentes de outros diretórios podem aparecer e não são desta tarefa.

- [ ] **Step 6: Conferir a navegação**

```bash
ls /tmp/atcdocs-build/documentos/manuais/espaco-aereo-servicos-ats/
grep -o "Manual de Espaço Aéreo e Serviços ATS" /tmp/atcdocs-build/documentos/manuais/espaco-aereo-servicos-ats/index.html | head -1
```

Esperado: `index.html` existe e o título do manual aparece renderizado.

- [ ] **Step 7: Conferir que as footnotes fecham**

```bash
F=docs/documentos/manuais/espaco-aereo-servicos-ats/index.pt.md
diff <(grep -oE '\[\^[0-9]+\]' "$F" | grep -v ':' | sort -u) \
     <(grep -oE '^\[\^[0-9]+\]:' "$F" | tr -d ':' | sort -u)
```

Esperado: saída vazia — toda referência tem definição e vice-versa.

- [ ] **Step 8: Commit**

```bash
git add includes/abreviacoes.md docs/documentos/manuais/espaco-aereo-servicos-ats/
git commit -m "feat: add airspace and ATS services manual skeleton"
```

---

### Task 3: Capítulo 01 — Estrutura do Espaço Aéreo

**Files:**
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/01-estrutura.pt.md`

**Interfaces:**
- Consumes: `.sources/ica-100-37.txt` (Art. 15 a 20), `.sources/ica-100-12.txt` (Cap. II e Anexo VII); o padrão de front matter da Task 2.
- Produces: a definição de cada divisão do espaço aéreo, referenciada pelos capítulos 02 e 04; o bloco `<style>` do SVG, replicado nos SVG-2 e SVG-3.

- [ ] **Step 1: Extrair os trechos normativos**

```bash
sed -n '270,310p' .sources/ica-100-37.txt   # Art. 15 a 20: FIR, CTA, CTR, UTA, TMA, ATZ
grep -n "Altitude de Transição\|Nível de Transição" .sources/ica-100-12.txt | head
grep -n "^XI - ATZ\|^XVII - CTA\|^XVIII - CTR\|^L - TMA\|^XXIV - FIR" .sources/ica-100-12.txt
```

Copiar as definições verbatim para uso na redação. Não parafrasear sem conferir.

- [ ] **Step 2: Escrever o capítulo**

Cabeçalho:

```markdown
---
title: Estrutura do Espaço Aéreo
icon: material/layers-triple
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Estrutura](img/manual-espaco-aereo-estrutura.png)

#

## Espaço aéreo controlado e não controlado
```

Seções obrigatórias:

1. **Espaço aéreo controlado e não controlado** — o que muda na prática.
2. **FIR** — ICA 100-37 Art. 15: partes do espaço aéreo onde são providos os Serviços de Informação de Voo e de Alerta. Citar que CTA, CTR e ATZ dentro de uma FIR fazem parte dela (Art. 19, parágrafo único).
3. **Áreas de Controle: UTA, CTA e TMA** — ICA 100-37 Art. 16 e 17. UTA compreende aerovias superiores; CTA, aerovias inferiores; TMA, partes do espaço aéreo inferior, todas "assim definidas na AIP-Brasil".
4. **CTR** — zona de controle.
5. **ATZ** — ICA 100-37 Art. 19: partes do espaço aéreo em torno de um aeródromo com requisitos especiais para proteção do tráfego de aeródromo. Art. 20: aeródromo controlado é aquele onde há Serviço de Controle de Tráfego Aéreo para o tráfego de aeródromo.
6. **Justaposição vertical** — ICA 100-37 Art. 23: quando dois espaços ATS se sobrepõem, o voo no nível comum cumpre os requisitos da classe **menos restritiva**, sendo B menos restritiva que A, C que B, e assim por diante.
7. **Tabela-resumo** das divisões: sigla, nome, o que compreende, quem provê serviço.
8. **SVG-1** (Step 3).
9. **Nota sobre a FIR Atlântico**:

```markdown
!!! note "FIR Atlântico"
    Nem toda regra vale igual em todas as FIR. A ICA 100-12 trata a FIR Atlântico separadamente das FIR continentais em alguns procedimentos, e há dispositivos com vigência escalonada até 1º de janeiro de 2027. Ao operar em espaço oceânico, confira sempre a regra aplicável àquela FIR.
```

10. **Bloco "Na rede"**:

```markdown
!!! tip "Na rede (Vatbrz)"
    No EuroScope, os limites de FIR, TMA, CTR e ATZ vêm do sector file. Antes de conectar, abra o setor e localize visualmente o limite lateral e vertical da sua posição — é ele que define até onde vai a sua responsabilidade.
```

Cada afirmação normativa recebe footnote `[^1]` para ICA 100-37 e `[^2]` para ICA 100-12, com o mesmo texto de definição usado no `index.pt.md`.

- [ ] **Step 3: Inserir o SVG-1, corte vertical**

Colar no ponto indicado da seção. Renderiza em ambos os temas:

```html
<figure markdown>
<svg viewBox="0 0 640 380" role="img" aria-label="Corte vertical do espaço aéreo: solo, ATZ, CTR, TMA, CTA e UTA dentro de uma FIR" style="max-width:100%;height:auto">
  <style>
    .ea-bg   { fill: #ffffff; }
    .ea-band { stroke: #546e7a; stroke-width: 1.5; }
    .ea-fir  { fill: none; stroke: #37474f; stroke-width: 2; stroke-dasharray: 6 4; }
    .ea-lbl  { fill: #263238; font: 500 13px "Ubuntu Sans", sans-serif; }
    .ea-sub  { fill: #546e7a; font: 400 11px "Ubuntu Sans", sans-serif; }
    .ea-uta  { fill: #b3e5fc; }
    .ea-cta  { fill: #c8e6c9; }
    .ea-tma  { fill: #fff9c4; }
    .ea-ctr  { fill: #ffe0b2; }
    .ea-atz  { fill: #ffccbc; }
    .ea-gnd  { fill: #bdbdbd; }
    @media (prefers-color-scheme: dark) {
      .ea-bg  { fill: #1e2129; }
      .ea-lbl { fill: #eceff1; }
      .ea-sub { fill: #b0bec5; }
      .ea-fir { stroke: #cfd8dc; }
      .ea-band{ stroke: #90a4ae; }
      .ea-uta { fill: #01579b; } .ea-cta { fill: #1b5e20; }
      .ea-tma { fill: #827717; } .ea-ctr { fill: #e65100; }
      .ea-atz { fill: #bf360c; } .ea-gnd { fill: #424242; }
    }
    [data-md-color-scheme="slate"] .ea-bg  { fill: #1e2129; }
    [data-md-color-scheme="slate"] .ea-lbl { fill: #eceff1; }
    [data-md-color-scheme="slate"] .ea-sub { fill: #b0bec5; }
    [data-md-color-scheme="slate"] .ea-fir { stroke: #cfd8dc; }
    [data-md-color-scheme="slate"] .ea-band{ stroke: #90a4ae; }
    [data-md-color-scheme="slate"] .ea-uta { fill: #01579b; }
    [data-md-color-scheme="slate"] .ea-cta { fill: #1b5e20; }
    [data-md-color-scheme="slate"] .ea-tma { fill: #827717; }
    [data-md-color-scheme="slate"] .ea-ctr { fill: #e65100; }
    [data-md-color-scheme="slate"] .ea-atz { fill: #bf360c; }
    [data-md-color-scheme="slate"] .ea-gnd { fill: #424242; }
    [data-md-color-scheme="default"] .ea-bg  { fill: #ffffff; }
    [data-md-color-scheme="default"] .ea-lbl { fill: #263238; }
    [data-md-color-scheme="default"] .ea-sub { fill: #546e7a; }
    [data-md-color-scheme="default"] .ea-fir { stroke: #37474f; }
    [data-md-color-scheme="default"] .ea-band{ stroke: #546e7a; }
    [data-md-color-scheme="default"] .ea-uta { fill: #b3e5fc; }
    [data-md-color-scheme="default"] .ea-cta { fill: #c8e6c9; }
    [data-md-color-scheme="default"] .ea-tma { fill: #fff9c4; }
    [data-md-color-scheme="default"] .ea-ctr { fill: #ffe0b2; }
    [data-md-color-scheme="default"] .ea-atz { fill: #ffccbc; }
    [data-md-color-scheme="default"] .ea-gnd { fill: #424242; }
  </style>

  <rect class="ea-bg" x="0" y="0" width="640" height="380"/>
  <rect class="ea-fir" x="12" y="12" width="616" height="356" rx="6"/>
  <text class="ea-lbl" x="24" y="32">FIR — Região de Informação de Voo</text>
  <text class="ea-sub" x="24" y="48">Serviço de Informação de Voo e Serviço de Alerta</text>

  <rect class="ea-uta ea-band" x="40" y="62" width="560" height="52"/>
  <text class="ea-lbl" x="52" y="84">UTA</text>
  <text class="ea-sub" x="52" y="102">Aerovias superiores e demais partes do espaço aéreo superior</text>

  <rect class="ea-cta ea-band" x="40" y="118" width="560" height="52"/>
  <text class="ea-lbl" x="52" y="140">CTA</text>
  <text class="ea-sub" x="52" y="158">Aerovias inferiores e demais partes do espaço aéreo inferior</text>

  <rect class="ea-tma ea-band" x="120" y="174" width="400" height="70"/>
  <text class="ea-lbl" x="132" y="198">TMA</text>
  <text class="ea-sub" x="132" y="216">Partes do espaço aéreo inferior em torno de um ou mais aeródromos</text>

  <rect class="ea-ctr ea-band" x="200" y="248" width="240" height="66"/>
  <text class="ea-lbl" x="212" y="272">CTR</text>
  <text class="ea-sub" x="212" y="290">Zona de Controle, do solo até um limite superior definido</text>

  <rect class="ea-atz ea-band" x="262" y="318" width="116" height="34"/>
  <text class="ea-lbl" x="274" y="340">ATZ</text>

  <rect class="ea-gnd" x="40" y="352" width="560" height="10"/>
  <text class="ea-sub" x="404" y="340">Superfície</text>
</svg>
<figcaption>Corte vertical esquemático. Limites laterais e verticais reais de cada divisão são publicados na AIP-Brasil e nas cartas.</figcaption>
</figure>
```

- [ ] **Step 4: Conferir citações contra a fonte**

Para cada artigo citado no capítulo, confirmar que existe no texto oficial:

```bash
F=docs/documentos/manuais/espaco-aereo-servicos-ats/01-estrutura.pt.md
for art in $(grep -oE 'Art\. [0-9]+' "$F" | sort -u | grep -oE '[0-9]+'); do
  printf "Art. %s -> " "$art"
  grep -c "Art. $art\." .sources/ica-100-37.txt
done
```

Esperado: contagem maior que zero para todo artigo citado. Zero significa citação inventada — corrigir antes de seguir.

- [ ] **Step 5: Build e conferência de footnotes**

```bash
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | grep -iE "warning|error" || echo "sem avisos"
F=docs/documentos/manuais/espaco-aereo-servicos-ats/01-estrutura.pt.md
diff <(grep -oE '\[\^[0-9]+\]' "$F" | grep -v ':' | sort -u) \
     <(grep -oE '^\[\^[0-9]+\]:' "$F" | tr -d ':' | sort -u)
```

Esperado: sem avisos e diff vazio.

- [ ] **Step 6: Conferência visual nos dois temas**

```bash
venv/bin/python -m mkdocs serve --dirtyreload
```

Abrir `http://127.0.0.1:8000/documentos/manuais/espaco-aereo-servicos-ats/01-estrutura/`, alternar o tema pelo botão do cabeçalho e confirmar que rótulos e faixas do SVG permanecem legíveis nos dois. Encerrar com `Ctrl+C`.

- [ ] **Step 7: Commit**

```bash
git add docs/documentos/manuais/espaco-aereo-servicos-ats/01-estrutura.pt.md
git commit -m "feat: add airspace structure chapter"
```

---

### Task 4: Capítulo 02 — Classes de Espaço Aéreo

O capítulo mais sensível do manual. A matriz é normativa e não admite paráfrase livre.

**Files:**
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/02-classes.pt.md`

**Interfaces:**
- Consumes: `.sources/ica-100-37.txt` (Art. 21 a 24 e Anexo II), `.sources/ica-100-12.txt` (Art. 111, 113, 115); as definições de divisão do capítulo 01.
- Produces: a matriz de classes A–G, consumida pelo capítulo 06 (checklist) e referenciada pelo capítulo 03.

- [ ] **Step 1: Extrair a classificação e a tabela de requisitos**

```bash
sed -n '310,372p' .sources/ica-100-37.txt      # Art. 21 a 24
sed -n '10548,10710p' .sources/ica-100-37.txt  # Anexo II, tabela de requisitos
grep -n "Art. 111\.\|Art. 113\.\|Art. 115\." .sources/ica-100-12.txt
```

O Anexo II traz, por classe e tipo de voo: separação provida, serviços e informações prestados, limite de velocidade, requisitos de radiocomunicação e sujeição a autorização ATC. A extração do PDF quebra as colunas — reconstruir a tabela conferindo linha a linha contra o texto do Art. 21.

- [ ] **Step 2: Escrever o capítulo**

Cabeçalho:

```markdown
---
title: Classes de Espaço Aéreo
icon: material/format-list-group
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Classes](img/manual-espaco-aereo-classes.png)

#

## Por que existem classes
```

Seções obrigatórias:

1. **Por que existem classes** — a classe define três coisas: quem pode voar ali, quem separa quem, e o que o órgão presta.
2. **As sete classes** — uma subseção por classe, com o conteúdo do Art. 21 da ICA 100-37:
   - **A**: somente IFR; ATC a todos; todos separados entre si.
   - **B**: IFR e VFR; ATC a todos; todos separados entre si.
   - **C**: IFR e VFR; ATC a todos; IFR separado de IFR e de VFR; VFR separado apenas de IFR, e recebe informação de tráfego sobre outros VFR mais aviso para evitar tráfego quando solicitado.
   - **D**: IFR e VFR; ATC a todos; IFR separado de IFR e recebe informação de tráfego sobre VFR; VFR recebe apenas informação de tráfego sobre todos os voos, mais aviso para evitar tráfego quando solicitado.
   - **E**: IFR e VFR; ATC somente aos IFR, separados entre si; todos recebem informação de tráfego quando possível.
   - **F**: IFR e VFR; Serviço de Assessoramento de Tráfego Aéreo somente aos IFR; todos recebem Serviço de Informação de Voo quando solicitado.
   - **G**: IFR e VFR permitidos, recebendo somente Serviço de Informação de Voo, quando possível e solicitado pelo piloto.
3. **Tabela consolidada** reproduzindo o Anexo II: classe, tipo de voo, separação provida, serviços prestados, limite de velocidade, radiocomunicação, sujeição a autorização ATC. Valores verificados que devem constar: Classe B VFR — 380 kt IAS; Classe C VFR — 250 kt IAS abaixo de 10.000 pés AMSL.
4. **Duas regras que pegam o iniciante**, ambas do Art. 21 e 23:

```markdown
!!! warning "Zona de Controle não é Classe E"
    O § 1° do Art. 21 da ICA 100-37 veda a classificação de Zonas de Controle como Classe E.[^1]

!!! note "Espaços justapostos verticalmente"
    Quando dois espaços aéreos ATS estão um acima do outro, o voo no nível comum cumpre os requisitos e dispõe dos serviços da classe **menos restritiva**. Para esse efeito, a Classe B é menos restritiva que a A, a C menos que a B, e assim por diante.[^1]
```

5. **Responsabilidade do piloto** — Art. 24: em classe onde o ATC não tem responsabilidade de prover separação, cabe ao piloto em comando prover a própria separação. Conecta com o que o Manual de Fraseologia para Voo Visual já afirma.
6. **Assessoramento é medida temporária** — § 2° do Art. 21.
7. **SVG-2** (Step 3).
8. **Bloco "Na rede"**:

```markdown
!!! tip "Na rede (Vatbrz)"
    A classe do espaço aéreo muda o que você deve ao piloto. Em Classe C você separa IFR de VFR; em Classe D você não separa VFR de ninguém, apenas informa tráfego. Antes de aceitar uma posição, saiba em qual classe ela opera — a informação está na AIP e na seção **Manuais Operacionais** do portal.
```

9. **Nota sobre a classificação aplicada no Brasil**:

```markdown
!!! note "Qual classe vale onde"
    A ICA 100-37 define o que cada classe significa. **Qual** classe se aplica a cada porção do espaço aéreo brasileiro é publicado na AIP-Brasil, seção ENR 1.4, e pode mudar por AIRAC. Consulte sempre o [AISWEB](https://aisweb.decea.mil.br/) para o dado vigente.
```

Este bloco é obrigatório: fecha a lacuna entre a norma, que está em mãos, e a aplicação local, que muda por ciclo AIRAC e não é fixada no manual.

- [ ] **Step 3: Inserir o SVG-2, matriz de classes**

Mesma estratégia de tema do SVG-1. Sete colunas (A–G) contra quatro linhas (voos permitidos, ATC prestado a, separação entre, informação de tráfego), com célula preenchida indicando presença:

```html
<figure markdown>
<svg viewBox="0 0 700 300" role="img" aria-label="Matriz das classes de espaço aéreo A a G contra voos permitidos, serviço de controle, separação e informação de tráfego" style="max-width:100%;height:auto">
  <style>
    .cl-bg   { fill: #ffffff; }
    .cl-hd   { fill: #263238; font: 600 14px "Ubuntu Sans", sans-serif; text-anchor: middle; }
    .cl-rw   { fill: #263238; font: 400 12px "Ubuntu Sans", sans-serif; }
    .cl-cell { fill: #eceff1; stroke: #90a4ae; stroke-width: 1; }
    .cl-on   { fill: #2e7d32; }
    .cl-part { fill: #f9a825; }
    .cl-off  { fill: #cfd8dc; }
    .cl-key  { fill: #546e7a; font: 400 11px "Ubuntu Sans", sans-serif; }
    @media (prefers-color-scheme: dark) {
      .cl-bg { fill: #1e2129; } .cl-hd { fill: #eceff1; } .cl-rw { fill: #eceff1; }
      .cl-cell { fill: #2b303b; stroke: #546e7a; } .cl-off { fill: #37474f; }
      .cl-on { fill: #66bb6a; } .cl-part { fill: #ffca28; } .cl-key { fill: #b0bec5; }
    }
    [data-md-color-scheme="slate"] .cl-bg { fill: #1e2129; }
    [data-md-color-scheme="slate"] .cl-hd { fill: #eceff1; }
    [data-md-color-scheme="slate"] .cl-rw { fill: #eceff1; }
    [data-md-color-scheme="slate"] .cl-cell { fill: #2b303b; stroke: #546e7a; }
    [data-md-color-scheme="slate"] .cl-off { fill: #37474f; }
    [data-md-color-scheme="slate"] .cl-on { fill: #66bb6a; }
    [data-md-color-scheme="slate"] .cl-part { fill: #ffca28; }
    [data-md-color-scheme="slate"] .cl-key { fill: #b0bec5; }
    [data-md-color-scheme="default"] .cl-bg { fill: #ffffff; }
    [data-md-color-scheme="default"] .cl-hd { fill: #263238; }
    [data-md-color-scheme="default"] .cl-rw { fill: #263238; }
    [data-md-color-scheme="default"] .cl-cell { fill: #eceff1; stroke: #90a4ae; }
    [data-md-color-scheme="default"] .cl-off { fill: #cfd8dc; }
    [data-md-color-scheme="default"] .cl-on { fill: #2e7d32; }
    [data-md-color-scheme="default"] .cl-part { fill: #f9a825; }
    [data-md-color-scheme="default"] .cl-key { fill: #546e7a; }
  </style>
  <rect class="cl-bg" x="0" y="0" width="700" height="300"/>
</svg>
<figcaption>Verde: aplica-se integralmente. Âmbar: aplica-se parcialmente ou sob condição. Cinza: não se aplica. A redação normativa completa está no Art. 21 da ICA 100-37.</figcaption>
</figure>
```

Completar o corpo do SVG com as células, seguindo a matriz do Step 2: cabeçalho com as sete letras em `x` de 260 a 660, espaçamento de 60; rótulos de linha em `x=20`; células de 34×34. Verde para presença integral, âmbar para condicional (por exemplo, informação de tráfego "quando possível" na Classe E, ou "quando solicitado" na F e G), cinza para ausência.

- [ ] **Step 4: Conferir a matriz contra o Art. 21, célula a célula**

Reler o Step 1 lado a lado com o capítulo escrito. Conferir explicitamente, por classe: voos permitidos, a quem se presta ATC, quem é separado de quem, que informação de tráfego é prestada e sob qual condição.

Erros nesta matriz se propagam para o checklist do capítulo 06 e para a formação de todos os membros. Se houver qualquer dúvida de interpretação, marcar o ponto com um comentário HTML `<!-- REVISAR: ... -->` e levantar na revisão técnica em vez de arbitrar.

- [ ] **Step 5: Conferir citações contra a fonte**

```bash
F=docs/documentos/manuais/espaco-aereo-servicos-ats/02-classes.pt.md
for art in $(grep -oE 'Art\. [0-9]+' "$F" | sort -u | grep -oE '[0-9]+'); do
  printf "Art. %s -> ica-100-37: " "$art"
  grep -c "Art. $art\." .sources/ica-100-37.txt
done
grep -c "380 kt\|250 kt" .sources/ica-100-37.txt
```

Esperado: contagens maiores que zero. Os limites de velocidade devem aparecer no Anexo II.

- [ ] **Step 6: Build e conferência de footnotes**

```bash
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | grep -iE "warning|error" || echo "sem avisos"
F=docs/documentos/manuais/espaco-aereo-servicos-ats/02-classes.pt.md
diff <(grep -oE '\[\^[0-9]+\]' "$F" | grep -v ':' | sort -u) \
     <(grep -oE '^\[\^[0-9]+\]:' "$F" | tr -d ':' | sort -u)
grep -c "REVISAR" "$F" || true
```

Esperado: sem avisos, diff vazio. Se houver marcações `REVISAR`, listá-las no relatório final da tarefa.

- [ ] **Step 7: Conferência visual nos dois temas**

```bash
venv/bin/python -m mkdocs serve --dirtyreload
```

Abrir `http://127.0.0.1:8000/documentos/manuais/espaco-aereo-servicos-ats/02-classes/`, alternar tema, conferir SVG-2 e a tabela consolidada. A tabela é larga — confirmar que não estoura no viewport estreito. Encerrar com `Ctrl+C`.

- [ ] **Step 8: Commit**

```bash
git add docs/documentos/manuais/espaco-aereo-servicos-ats/02-classes.pt.md
git commit -m "feat: add airspace classes chapter"
```

---

### Task 5: Capítulo 03 — Serviços de Tráfego Aéreo

**Files:**
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/03-servicos.pt.md`

**Interfaces:**
- Consumes: `.sources/ica-100-37.txt` (objetivos e divisão dos Serviços de Tráfego Aéreo), `.sources/ica-100-12.txt` (Cap. IV Seção VI, Art. 77 a 98); a matriz de classes do capítulo 02.
- Produces: a distinção entre os quatro serviços, consumida pelo capítulo 04 ao mapear órgãos.

- [ ] **Step 1: Extrair os trechos normativos**

```bash
grep -n "Serviço de Informação de Voo\|Serviço de Alerta\|Serviço de Assessoramento\|Serviço de Controle de Tráfego Aéreo" .sources/ica-100-37.txt | head -40
sed -n '/Seção VI/,/Seção VII/p' .sources/ica-100-12.txt | head -80
```

- [ ] **Step 2: Escrever o capítulo**

Cabeçalho:

```markdown
---
title: Serviços de Tráfego Aéreo
icon: material/headset
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Serviços](img/manual-espaco-aereo-servicos.png)

#

## Os serviços de tráfego aéreo
```

Seções obrigatórias:

1. **Os serviços de tráfego aéreo** — visão geral: o termo é genérico e abrange serviços distintos, prestados conforme a classe do espaço aéreo.
2. **Serviço de Controle de Tráfego Aéreo** — objetivo, subdivisões (controle de área, de aproximação e de aeródromo).
3. **Serviço de Informação de Voo** — o que inclui, a quem se presta.
4. **Serviço de Alerta** — quando é acionado.
5. **Serviço de Assessoramento de Tráfego Aéreo** — Classe F, medida temporária (§ 2° do Art. 21 da ICA 100-37).
6. **Tabela: qual serviço em qual classe** — cruzamento direto com o capítulo 02.
7. **O que informar não é controlar**:

```markdown
!!! danger "Informar não é controlar"
    O Serviço de Informação de Voo **não** separa aeronaves e **não** emite autorizações. Quem presta apenas informação de voo não usa verbos que impliquem controle — "suba", "desça", "mantenha", "autorizado". Ele informa, transmite condições e responde com **CIENTE**.

    Quando retransmite uma autorização emitida por um órgão ATC, deve deixar claro de quem partiu a autorização.
```

Este bloco reforça, com a base normativa, o que o [Manual de Fraseologia para Voo Visual](../fraseologia-voo-visual/conceitos.pt.md) já pratica na fonia. Linkar explicitamente.

8. **Bloco "Na rede"**:

```markdown
!!! tip "Na rede (Vatbrz)"
    Toda posição conectada na rede presta Serviço de Controle de Tráfego Aéreo dentro do seu espaço aéreo. O que muda é o alcance: fora do espaço controlado, o que você presta ao piloto é informação, não controle. Reconhecer essa fronteira é o que separa uma instrução válida de uma instrução que você não tinha autoridade para emitir.
```

- [ ] **Step 3: Conferir citações contra a fonte**

```bash
F=docs/documentos/manuais/espaco-aereo-servicos-ats/03-servicos.pt.md
for art in $(grep -oE 'Art\. [0-9]+' "$F" | sort -u | grep -oE '[0-9]+'); do
  printf "Art. %s -> 100-37: %s | 100-12: %s\n" "$art" \
    "$(grep -c "Art. $art\." .sources/ica-100-37.txt)" \
    "$(grep -c "Art. $art\." .sources/ica-100-12.txt)"
done
```

Esperado: cada artigo citado aparece em ao menos uma das duas fontes, e a footnote correspondente aponta para a fonte certa.

- [ ] **Step 4: Build e conferência de footnotes**

```bash
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | grep -iE "warning|error" || echo "sem avisos"
F=docs/documentos/manuais/espaco-aereo-servicos-ats/03-servicos.pt.md
diff <(grep -oE '\[\^[0-9]+\]' "$F" | grep -v ':' | sort -u) \
     <(grep -oE '^\[\^[0-9]+\]:' "$F" | tr -d ':' | sort -u)
```

Esperado: sem avisos e diff vazio.

- [ ] **Step 5: Conferir o link cruzado**

```bash
ls docs/documentos/manuais/fraseologia-voo-visual/conceitos.pt.md
```

Esperado: arquivo existe. O `mkdocs.yml` tem `validation: unrecognized_links: ignore`, então um link quebrado **não** gera aviso de build — a conferência tem que ser manual.

- [ ] **Step 6: Commit**

```bash
git add docs/documentos/manuais/espaco-aereo-servicos-ats/03-servicos.pt.md
git commit -m "feat: add ATS services chapter"
```

---

### Task 6: Capítulo 04 — Órgãos ATS e Posições

**Files:**
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/04-orgaos.pt.md`

**Interfaces:**
- Consumes: `.sources/ica-100-37.txt` (órgãos ATS), a tabela de órgãos do Manual de Fraseologia para Voo Visual, os capítulos 01 e 03.
- Produces: o mapeamento órgão ↔ posição VATSIM, consumido pelo capítulo 06.

- [ ] **Step 1: Extrair os trechos normativos e conferir a tabela existente**

```bash
grep -n "Centro de Controle de Área\|Controle de Aproximação\|Torre de Controle\|órgão ATS" .sources/ica-100-37.txt | head -30
sed -n '/Órgãos que você encontra/,/Indicativo de chamada/p' docs/documentos/manuais/fraseologia-voo-visual/conceitos.pt.md
```

A tabela de órgãos do Fraseologia VFR já existe e usa colunas PT/EN/ES. **Não duplicar** aquele conteúdo: este capítulo trata de jurisdição e espaço aéreo, não de fonia. Linkar para lá quanto aos indicativos.

- [ ] **Step 2: Escrever o capítulo**

Cabeçalho:

```markdown
---
title: Órgãos ATS e Posições
icon: material/account-tie-hat
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Órgãos](img/manual-espaco-aereo-orgaos.png)

#

## Órgão ATS e posição na rede
```

Seções obrigatórias:

1. **Órgão ATS e posição na rede** — a distinção entre o órgão real e a posição conectada.
2. **Tabela de correspondência**, exatamente com estas linhas:

```markdown
| Órgão ATS | Posição VATSIM | Espaço aéreo típico | Serviço prestado |
| --- | --- | --- | --- |
| Centro de Controle de Área (ACC) | `_CTR` | CTA, UTA e demais porções da FIR | Controle de área |
| Controle de Aproximação (APP) | `_APP` | TMA e CTR | Controle de aproximação |
| Torre de Controle (TWR) | `_TWR` | ATZ e CTR | Controle de aeródromo |
| Controle de Solo | `_GND` | Área de manobras | Controle de aeródromo |
| Autorização de Tráfego | `_DEL` | Pátio | Controle de aeródromo |
```

3. **Jurisdição** — até onde vai cada posição, lateral e verticalmente.
4. **Cobertura top-down** — quando a posição superior está conectada e a inferior não, a superior responde pelo espaço aéreo da inferior. Explicar a consequência prática: o piloto chama uma frequência só.
5. **Transferência entre órgãos** — o encadeamento normal de um voo completo.
6. **SVG-3** (Step 3).
7. **Bloco "Na rede"**:

```markdown
!!! tip "Na rede (Vatbrz)"
    Antes de conectar, confira quem já está online. Se o CTR está conectado e você assume o APP, parte do espaço aéreo que estava sob cobertura *top-down* passa a ser sua — e a transferência dos tráfegos já em frequência precisa ser coordenada, não presumida.
```

8. **Link cruzado** para o Manual de Fraseologia Aeronáutica e para o de Fraseologia para Voo Visual, quanto aos indicativos de chamada de cada órgão.

- [ ] **Step 3: Inserir o SVG-3, cadeia de transferência**

Cinco nós encadeados da esquerda para a direita — DEL, GND, TWR, APP, CTR — cada um rotulado com o espaço aéreo correspondente, ligados por setas, e uma faixa acima indicando a cobertura top-down no sentido inverso. Mesmo tratamento de tema dos SVG anteriores:

```html
<figure markdown>
<svg viewBox="0 0 720 240" role="img" aria-label="Cadeia de órgãos ATS de DEL a CTR com o espaço aéreo de cada elo e o sentido da cobertura top-down" style="max-width:100%;height:auto">
  <style>
    .or-bg  { fill: #ffffff; }
    .or-box { fill: #e3f2fd; stroke: #1565c0; stroke-width: 1.5; }
    .or-ttl { fill: #0d47a1; font: 600 14px "Ubuntu Sans", sans-serif; text-anchor: middle; }
    .or-sub { fill: #37474f; font: 400 11px "Ubuntu Sans", sans-serif; text-anchor: middle; }
    .or-arw { stroke: #546e7a; stroke-width: 2; fill: none; marker-end: url(#or-head); }
    .or-td  { fill: #546e7a; font: 400 11px "Ubuntu Sans", sans-serif; }
    .or-hd  { fill: #546e7a; }
    @media (prefers-color-scheme: dark) {
      .or-bg { fill: #1e2129; } .or-box { fill: #102a43; stroke: #64b5f6; }
      .or-ttl { fill: #90caf9; } .or-sub { fill: #cfd8dc; }
      .or-arw { stroke: #b0bec5; } .or-td { fill: #b0bec5; } .or-hd { fill: #b0bec5; }
    }
    [data-md-color-scheme="slate"] .or-bg  { fill: #1e2129; }
    [data-md-color-scheme="slate"] .or-box { fill: #102a43; stroke: #64b5f6; }
    [data-md-color-scheme="slate"] .or-ttl { fill: #90caf9; }
    [data-md-color-scheme="slate"] .or-sub { fill: #cfd8dc; }
    [data-md-color-scheme="slate"] .or-arw { stroke: #b0bec5; }
    [data-md-color-scheme="slate"] .or-td  { fill: #b0bec5; }
    [data-md-color-scheme="slate"] .or-hd  { fill: #b0bec5; }
    [data-md-color-scheme="default"] .or-bg  { fill: #ffffff; }
    [data-md-color-scheme="default"] .or-box { fill: #e3f2fd; stroke: #1565c0; }
    [data-md-color-scheme="default"] .or-ttl { fill: #0d47a1; }
    [data-md-color-scheme="default"] .or-sub { fill: #37474f; }
    [data-md-color-scheme="default"] .or-arw { stroke: #546e7a; }
    [data-md-color-scheme="default"] .or-td  { fill: #546e7a; }
    [data-md-color-scheme="default"] .or-hd  { fill: #546e7a; }
  </style>
  <defs>
    <marker id="or-head" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path class="or-hd" d="M 0 0 L 10 5 L 0 10 z"/>
    </marker>
  </defs>
  <rect class="or-bg" x="0" y="0" width="720" height="240"/>
</svg>
<figcaption>Encadeamento normal de um voo. A cobertura <em>top-down</em> percorre o sentido inverso: a posição superior responde pelo espaço aéreo das inferiores que não estiverem conectadas.</figcaption>
</figure>
```

Completar o corpo com cinco `<rect class="or-box">` de 120×64 em `y=88`, com `x` em 20, 160, 300, 440 e 580; título e subtítulo centralizados em cada um; setas `<path class="or-arw">` ligando as bordas; e a faixa top-down em `y=40` com seta apontando da direita para a esquerda.

- [ ] **Step 4: Conferir citações contra a fonte**

```bash
F=docs/documentos/manuais/espaco-aereo-servicos-ats/04-orgaos.pt.md
for art in $(grep -oE 'Art\. [0-9]+' "$F" | sort -u | grep -oE '[0-9]+'); do
  printf "Art. %s -> " "$art"; grep -c "Art. $art\." .sources/ica-100-37.txt
done
```

Esperado: contagens maiores que zero.

Atenção: cobertura *top-down* é convenção da rede VATSIM, **não** norma DECEA. Ela vive no bloco "Na rede" e não recebe footnote normativa.

- [ ] **Step 5: Build, footnotes e links**

```bash
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | grep -iE "warning|error" || echo "sem avisos"
F=docs/documentos/manuais/espaco-aereo-servicos-ats/04-orgaos.pt.md
diff <(grep -oE '\[\^[0-9]+\]' "$F" | grep -v ':' | sort -u) \
     <(grep -oE '^\[\^[0-9]+\]:' "$F" | tr -d ':' | sort -u)
for l in $(grep -oE '\]\(\.\./[^)]+\)' "$F" | sed 's/](//;s/)//'); do
  p="docs/documentos/manuais/$(echo "$l" | sed 's|\.\./||')"
  [ -f "$p" ] && echo "ok $l" || echo "QUEBRADO $l"
done
```

Esperado: sem avisos, diff vazio, nenhum `QUEBRADO`.

- [ ] **Step 6: Conferência visual nos dois temas**

```bash
venv/bin/python -m mkdocs serve --dirtyreload
```

Abrir `http://127.0.0.1:8000/documentos/manuais/espaco-aereo-servicos-ats/04-orgaos/`, alternar tema, conferir que as setas e o marcador do SVG-3 aparecem nos dois. Encerrar com `Ctrl+C`.

- [ ] **Step 7: Commit**

```bash
git add docs/documentos/manuais/espaco-aereo-servicos-ats/04-orgaos.pt.md
git commit -m "feat: add ATS units and positions chapter"
```

---

### Task 7: Capítulo 05 — Regras de Voo e Níveis

**Files:**
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/05-regras.pt.md`

**Interfaces:**
- Consumes: `.sources/ica-100-12.txt` (Art. 22, 104, 123/124, 128 a 135, 142, Anexo IV); as classes do capítulo 02.
- Produces: os mínimos VMC e a regra de níveis, consumidos pelo capítulo 06.

- [ ] **Step 1: Extrair os trechos normativos**

```bash
sed -n '1196,1232p' .sources/ica-100-12.txt   # Art. 104, Tabela 1 (mínimos VMC)
sed -n '380,395p'   .sources/ica-100-12.txt   # Art. 22, níveis de cruzeiro
sed -n '2584,2640p' .sources/ica-100-12.txt   # Anexo IV, tabelas de níveis
grep -n "Art. 123\.\|Art. 124\.\|Art. 142\.\|Voo VFR Especial" .sources/ica-100-12.txt
```

- [ ] **Step 2: Escrever o capítulo**

Cabeçalho:

```markdown
---
title: Regras de Voo e Níveis
icon: material/altimeter
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Regras](img/manual-espaco-aereo-regras.png)

#

## Níveis de cruzeiro
```

Seções obrigatórias:

1. **Níveis de cruzeiro** — Art. 22 da ICA 100-12: os níveis são expressos em nível de voo acima da altitude de transição, e em altitude na altitude de transição ou abaixo. A tabela por rumo magnético está no Anexo IV.
2. **Espaço aéreo RVSM** — o Anexo IV traz a tabela 8 para RVSM e a tabela 9 para quando os procedimentos RVSM são suspensos.
3. **Níveis VFR** — Art. 123 e 124.
4. **Níveis IFR em espaço aéreo controlado** — Art. 142.
5. **Altitude e nível de transição** — QNH abaixo, QNE acima; a altitude de transição é publicada por aeródromo. **Não fixar valores** — apontar para AIP, carta e MOP.
6. **Mínimos VMC** — reproduzir a Tabela 1 do Art. 104, com as três faixas de altitude e as classes correspondentes:

| Faixa | Classes | Visibilidade em voo | Distância de nuvens |
| --- | --- | --- | --- |
| 10.000 pés AMSL ou acima | B C D E F G | 8 km | 1.500 m horizontal, 300 m (1.000 pés) vertical |
| Abaixo de 10.000 pés AMSL e acima de 3.000 pés AMSL, ou 1.000 pés sobre o terreno, o que for maior | B C D E F G | 5 km | 1.500 m horizontal, 300 m (1.000 pés) vertical |
| 3.000 pés AMSL ou abaixo, ou 1.000 pés sobre o terreno, o que for maior | B C D E | 5 km | 1.500 m horizontal, 300 m (1.000 pés) vertical |
| idem | F G | 5 km | Livre de nuvens e avistando o solo |

Incluir a regra do § 1°: quando a altitude de transição for inferior a 10.000 pés AMSL, usa-se o FL100 no lugar de 10.000 pés.

7. **VFR especial** — Cap. V Seção VIII, Art. 128 a 135; aplicável em CTR e ATZ.
8. **Bloco "Na rede"**:

```markdown
!!! tip "Na rede (Vatbrz)"
    Nível de cruzeiro incompatível com o rumo magnético é dos erros mais comuns na rede. Ao receber um plano, confira rumo contra nível antes de autorizar — corrigir na autorização inicial é mais barato do que resolver o conflito depois.
```

9. **Nota sobre helicópteros**:

```markdown
!!! note "Helicópteros"
    Os mínimos de visibilidade em voo e distância de nuvens para helicópteros são tratados em publicação própria, a ICA 100-4 (Regras e Procedimentos Especiais de Tráfego Aéreo para Helicópteros), e não constam da tabela acima.[^2]
```

- [ ] **Step 3: Conferir a tabela VMC contra a fonte, linha a linha**

Reler a saída do Step 1 lado a lado com a tabela escrita. Conferir explicitamente: as três faixas de altitude, quais classes constam em cada faixa, os valores de visibilidade (8 km e 5 km) e as distâncias de nuvens. A Classe A não aparece na tabela de mínimos VMC porque nela só são permitidos voos IFR — confirmar que a tabela escrita reflete isso.

- [ ] **Step 4: Conferir citações contra a fonte**

```bash
F=docs/documentos/manuais/espaco-aereo-servicos-ats/05-regras.pt.md
for art in $(grep -oE 'Art\. [0-9]+' "$F" | sort -u | grep -oE '[0-9]+'); do
  printf "Art. %s -> " "$art"; grep -c "Art. $art\." .sources/ica-100-12.txt
done
grep -c "1.500 m\|8 km\|5 km" .sources/ica-100-12.txt
```

Esperado: contagens maiores que zero.

- [ ] **Step 5: Build e conferência de footnotes**

```bash
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | grep -iE "warning|error" || echo "sem avisos"
F=docs/documentos/manuais/espaco-aereo-servicos-ats/05-regras.pt.md
diff <(grep -oE '\[\^[0-9]+\]' "$F" | grep -v ':' | sort -u) \
     <(grep -oE '^\[\^[0-9]+\]:' "$F" | tr -d ':' | sort -u)
```

Esperado: sem avisos e diff vazio.

- [ ] **Step 6: Commit**

```bash
git add docs/documentos/manuais/espaco-aereo-servicos-ats/05-regras.pt.md
git commit -m "feat: add flight rules and cruising levels chapter"
```

---

### Task 8: Capítulo 06 — Checklist Rápido

**Files:**
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/06-checklist.pt.md`

**Interfaces:**
- Consumes: capítulos 02, 03, 04 e 05. **Nenhum conteúdo novo.** Toda linha do checklist tem que existir em um capítulo anterior.
- Produces: nada. É folha da árvore.

- [ ] **Step 1: Escrever o capítulo**

Cabeçalho:

```markdown
---
title: Checklist Rápido
icon: material/checkbox-marked-circle-outline
---

--8<-- "includes/abreviacoes.md"

![Manual de Espaço Aéreo e Serviços ATS - Checklist](img/manual-espaco-aereo-checklist.png)

#

## Antes de conectar
```

Seções obrigatórias:

1. **Antes de conectar** — lista de tarefas em `pymdownx.tasklist`:

```markdown
- [ ] Sei em qual FIR, TMA, CTR ou ATZ minha posição opera
- [ ] Sei qual a classe do espaço aéreo sob minha responsabilidade
- [ ] Sei quem está online acima e abaixo de mim
- [ ] Confirmei a altitude de transição do aeródromo na carta
- [ ] Li as instruções locais na seção Manuais Operacionais
```

2. **Estou nesta classe — o que devo?** — tabela de consulta rápida derivada do capítulo 02, com colunas: classe, voos permitidos, quem separo, o que informo.
3. **Mínimos VMC de bolso** — versão condensada da tabela do capítulo 05.
4. **Qual órgão faz o quê** — versão condensada da tabela do capítulo 04.
5. **Onde buscar o dado local**:

```markdown
!!! tip "Na rede (Vatbrz)"
    Este checklist não substitui a carta. Limites laterais e verticais, altitude de transição e classe aplicada mudam por aeródromo e por ciclo AIRAC. A fonte é sempre a AIP, a carta e a seção **Manuais Operacionais** do portal.
```

Sem footnotes próprias: o capítulo não afirma nada de novo, apenas consolida. Cada tabela referencia o capítulo de origem por link relativo, por exemplo `[capítulo de Classes](02-classes.pt.md)`.

- [ ] **Step 2: Verificar que não há conteúdo novo**

Para cada linha das tabelas do checklist, localizar a afirmação equivalente no capítulo de origem. Qualquer linha sem origem ou é erro de consolidação, ou revela uma lacuna no capítulo anterior — nesse caso, corrigir o capítulo anterior, não o checklist.

- [ ] **Step 3: Build e conferência de links internos**

```bash
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | grep -iE "warning|error" || echo "sem avisos"
D=docs/documentos/manuais/espaco-aereo-servicos-ats
for l in $(grep -oE '\]\(0[0-9]-[a-z]+\.pt\.md\)' "$D/06-checklist.pt.md" | sed 's/](//;s/)//'); do
  [ -f "$D/$l" ] && echo "ok $l" || echo "QUEBRADO $l"
done
```

Esperado: sem avisos, nenhum `QUEBRADO`.

- [ ] **Step 4: Commit**

```bash
git add docs/documentos/manuais/espaco-aereo-servicos-ats/06-checklist.pt.md
git commit -m "feat: add airspace manual quick checklist"
```

---

### Task 9: Fechamento e verificação integral

Fecha o manual como um todo: confere os critérios de aceite do spec, registra as pendências e deixa o material pronto para a revisão técnica.

**Files:**
- Create: `docs/documentos/manuais/espaco-aereo-servicos-ats/img/README.md`
- Modify: `docs/documentos/manuais/espaco-aereo-servicos-ats/index.pt.md` (apenas se a conferência apontar ajuste)

**Interfaces:**
- Consumes: todas as tarefas anteriores.
- Produces: manual completo e verificado na branch `develop`.

- [ ] **Step 1: Registrar a pendência das imagens de cabeçalho**

Criar `docs/documentos/manuais/espaco-aereo-servicos-ats/img/README.md`:

```markdown
# Imagens de cabeçalho — pendência

Este manual referencia sete imagens de cabeçalho que ainda não foram
produzidas. Elas seguem o mesmo template gráfico dos demais manuais do
portal e devem ser geradas pelo mantenedor.

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
arquivos aqui com estes nomes exatos — nenhuma edição de Markdown é
necessária.
```

- [ ] **Step 2: Conferir os critérios de aceite do spec**

```bash
D=docs/documentos/manuais/espaco-aereo-servicos-ats
echo "== arquivos =="; ls "$D"
echo "== nenhum .md puro =="; ls "$D" | grep -E '^[0-9a-z-]+\.md$' && echo FALHA || echo ok
echo "== snippet de abreviações =="
for f in "$D"/*.pt.md; do grep -q 'includes/abreviacoes.md' "$f" || echo "FALTA em $f"; done
echo "== bloco Na rede =="
for f in "$D"/*.pt.md; do
  case "$f" in *index.pt.md) continue;; esac
  grep -q 'Na rede (Vatbrz)' "$f" || echo "FALTA em $f"
done
echo "== imagem de cabeçalho =="
for f in "$D"/*.pt.md; do grep -q '^!\[' "$f" || echo "FALTA em $f"; done
```

Esperado: sete `.pt.md` mais `.pages` e `img/`; nenhum `FALHA`; nenhum `FALTA`.

- [ ] **Step 3: Build integral e conferência de navegação**

```bash
rm -rf /tmp/atcdocs-build
venv/bin/python -m mkdocs build -d /tmp/atcdocs-build 2>&1 | tee /tmp/atcdocs-final.log
grep -iE "warning|error" /tmp/atcdocs-final.log || echo "sem avisos"
ls /tmp/atcdocs-build/documentos/manuais/espaco-aereo-servicos-ats/
```

Esperado: sete diretórios de página renderizados, nenhum aviso referente ao manual.

- [ ] **Step 4: Conferir a versão em inglês**

```bash
ls /tmp/atcdocs-build/en/documentos/manuais/espaco-aereo-servicos-ats/ 2>/dev/null | head
```

Esperado: as páginas aparecem também sob `/en/`, servidas em português por `fallback_to_default: true`. É o comportamento correto — o manual ainda não tem tradução, e a estrutura `.pt.md` permite acrescentá-la depois sem renomear nada.

- [ ] **Step 5: Conferência visual final nos dois temas**

```bash
venv/bin/python -m mkdocs serve --dirtyreload
```

Percorrer os sete capítulos em `http://127.0.0.1:8000/documentos/manuais/espaco-aereo-servicos-ats/`, alternando o tema em cada um. Conferir: os três SVG legíveis nos dois temas; as tabelas largas sem estouro horizontal; a navegação lateral na ordem do `.pages`; os tooltips das siglas novas funcionando. Encerrar com `Ctrl+C`.

- [ ] **Step 6: Levantar as marcações de revisão**

```bash
grep -rn "REVISAR" docs/documentos/manuais/espaco-aereo-servicos-ats/ || echo "nenhuma"
```

Toda marcação encontrada entra no relatório final como ponto a resolver na revisão técnica por controlador. Não arbitrar sozinho pontos de interpretação normativa.

- [ ] **Step 7: Commit**

```bash
git add docs/documentos/manuais/espaco-aereo-servicos-ats/img/README.md
git add -u docs/documentos/manuais/espaco-aereo-servicos-ats/
git commit -m "docs: document pending header images for airspace manual"
```

- [ ] **Step 8: Relatório final**

Reportar ao mantenedor:

1. Sete capítulos criados e o caminho do manual.
2. As sete imagens de cabeçalho pendentes.
3. Toda marcação `REVISAR` encontrada no Step 6.
4. Lembrete de que a **revisão técnica por controlador é obrigatória antes do merge** — o manual foi redigido a partir das fontes oficiais, mas o autor não é autoridade aeronáutica.
5. Que a classificação aplicada a cada porção do espaço aéreo brasileiro vem da AIP-Brasil ENR 1.4 e muda por AIRAC; o manual aponta para o AISWEB em vez de fixar o dado.

---

## Notas de execução

**Sobre a AIP ENR 1.4.** O spec previa usá-la como fonte secundária no capítulo 02. Ela não é obtível por URL direta estável: o AISWEB serve a AIP por um portal dinâmico sem link permanente para as seções. O plano resolve isso mantendo a **ICA 100-37 como única fonte normativa da matriz de classes** — que é onde a norma efetivamente está — e tratando a classificação aplicada por região como dado local, que o manual não fixa e para o qual aponta o AISWEB. Nenhum capítulo fica bloqueado.

**Sobre `mkdocs build` e links.** O `mkdocs.yml` define `validation: unrecognized_links: ignore`. Links internos quebrados **não** falham o build. Por isso cada tarefa que cria link relativo tem um passo explícito de conferência por `ls`/`test -f`.

**Sobre o ambiente Python.** O repositório tem `venv/` com o MkDocs instalado. Os comandos usam `venv/bin/python -m mkdocs` diretamente para não depender de ativação de shell — o `dev.sh` assume bash e o shell da sessão é fish.
