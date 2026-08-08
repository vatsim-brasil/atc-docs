# Manual de Espaço Aéreo e Serviços ATS — Handoff

**Data:** 08/08/2026
**Branch:** `develop` · 30 commits a partir de `5a7a852`
**Status:** pronto para revisão técnica por controlador. **Não pronto para publicar.**

---

## O que foi entregue

Sete capítulos em `docs/documentos/manuais/espaco-aereo-servicos-ats/`:

| Arquivo | Conteúdo |
| --- | --- |
| `index.pt.md` | Apresentação, escopo, não-escopo, referências, links cruzados |
| `01-estrutura.pt.md` | FIR, UTA, CTA, TMA, CTR, ATZ + corte vertical em SVG |
| `02-classes.pt.md` | Matriz das classes A–G, Anexo II reproduzido + matriz em SVG |
| `03-servicos.pt.md` | Controle, Informação de Voo, Alerta, Assessoramento |
| `04-orgaos.pt.md` | Órgãos ATS ↔ posições da rede, jurisdição + cadeia de transferência em SVG |
| `05-regras.pt.md` | Níveis de cruzeiro, RVSM, mínimos VMC, transição, VFR especial |
| `06-checklist.pt.md` | Consulta rápida antes de conectar |

O manual aparece sozinho na navegação — `docs/.pages` e `docs/documentos/.pages` não precisaram de edição. Build limpo: 0 erros.

Fontes normativas: **ICA 100-37** (em vigor 27/11/2025) e **ICA 100-12** (ed. 28/11/2024), com apoio do MCA 100-16 e da AIP Brasil. Toda afirmação normativa cita artigo, inciso ou anexo em footnote.

---

## Pendências antes do merge

### 1. As sete imagens de cabeçalho não existem

Não consigo reproduzir o template gráfico do portal. As referências já estão no lugar certo em cada capítulo — basta depositar os arquivos com estes nomes exatos em `docs/documentos/manuais/espaco-aereo-servicos-ats/img/`, sem editar Markdown:

```
manual-espaco-aereo-intro.png       manual-espaco-aereo-orgaos.png
manual-espaco-aereo-estrutura.png   manual-espaco-aereo-regras.png
manual-espaco-aereo-classes.png     manual-espaco-aereo-checklist.png
manual-espaco-aereo-servicos.png
```

Os 14 warnings de build (7 imagens × 2 locales) somem quando os arquivos entrarem.

### 2. Revisão técnica por controlador — obrigatória

O manual foi escrito inteiramente a partir das fontes oficiais, com verificação de citação artigo a artigo e revisão adversarial em cada capítulo. Ainda assim: **não sou autoridade aeronáutica.** Nada aqui deve ir ao ar sem um controlador ler.

### 3. Passe visual nos dois temas — nunca foi feito

Nenhum agente teve navegador. Os três SVG foram verificados **estruturalmente** (elementos dentro do `<svg>`, blocos de tema sobrevivendo ao build) e os contrastes foram **calculados** (todos acima do piso 3:1 da WCAG 1.4.11), mas ninguém olhou a página. Abra os capítulos 01, 02 e 04 e alterne o tema.

---

## Duas decisões que tomei sem poder perguntar

Ambas em conflitos internos do plano, onde o plano se contradizia. Nos dois casos a "regra dura" do próprio plano — nenhuma afirmação normativa sem citação — decidiu. **Ambas são reversíveis; se discordar, é só dizer.**

**1. Nota da FIR Atlântico (cap. 01).** O plano ditava o texto da admonition sem footnote, enquanto sua própria regra dura exige citação em toda afirmação normativa. Mandei citar. Respaldo: ICA 100-12 Art. 96 e Art. 97.

**2. Cabeçalho da tabela de órgãos (cap. 04).** O plano mandava uma tabela com coluna "Órgão ATS" listando Controle de Solo e Autorização de Tráfego como pares de ACC/APP/TWR. O Art. 509 da ICA 100-37 trata os dois como **posições internas da TWR**, não como órgãos. Mandei separar em "Órgão ATS" + "Posição interna", usando os três nomes do Art. 686. Todos os cinco mapeamentos de posição sobreviveram.

> O spec de design (`specs/2026-08-07-espaco-aereo-servicos-ats-design.md`) ainda mostra a tabela antiga de três colunas. O spec está desatualizado, não a entrega.

---

## Achados deixados em aberto

O processo permite uma única leva de correção após a revisão final. Estes dois entraram depois dela e são de baixo risco — correção de uma frase cada:

- **`04-orgaos.pt.md:81`** — "Um voo completo passa, tipicamente, por todas as posições da tabela" não foi atualizado quando as linhas RÁDIO e FIC entraram na tabela. A legenda do diagrama, na mesma seção, já diz que essas unidades ficam fora da cadeia. Sugestão: "todas as posições **de controle** da tabela".
- **`03-servicos.pt.md:99`** — estreita o Art. 29 para "apenas nas classes ali listadas", mas os incisos III e IV não são atrelados a classe, e uma ATZ não tem classe. Erra para o lado conservador: não autoriza instrução inválida.

**Correção a um relatório interno:** o relatório da leva de correção afirma que ARCC, AIRAC, SIGMET e AIRMET aparecem literalmente nas fontes. **AIRAC não aparece em nenhuma das duas.** A expansão está correta (terminologia AIP/OACI) e não é contradita pelo manual, mas a evidência citada está errada para essa sigla.

---

## Correções colaterais no portal

Três defeitos pré-existentes apareceram durante o trabalho e foram corrigidos:

1. **`<figure markdown>` quebrava SVG inline.** O atributo `markdown` faz o Python-Markdown envolver a tag de abertura do SVG num `<p>`, e o elemento fecha cedo — diagrama some. Confirmado com zero filhos de `<svg>` no Chromium. Corrigido nos capítulos 01 e 02, e o padrão foi removido do plano. **Se outros manuais usarem `<figure markdown>` com SVG inline, têm o mesmo problema.**
2. **Glossário definia TMA errado.** `includes/abreviacoes.md` expandia TMA como "Área de Manobras Terminais / Terminal Maneuvering Area" — a forma europeia. A ICA 100-12, Anexo VII, item L diz **"Área de Controle Terminal (Terminal Control Area)"**. O tooltip errado aparecia em toda página do portal que cita TMA. Corrigido.
3. **Siglas ausentes.** Acrescentadas ao glossário global: ATZ, CTA, ACC, EAC, AMSL, QNH, QNE, RVSM, IAS, OACI, IAC, ARCC, AIRAC, SIGMET, AIRMET. Beneficia os manuais existentes também.

Também notado, **não corrigido** (pré-existente, fora do escopo): `includes/abreviacoes.md` linha 47 lê `*[AUTH]: Autorizdo / Cleared` — provável erro de digitação de "Autorizado".

---

## Descobertas normativas que valem registro

- **O Anexo VII da ICA 100-37 foi revogado** (Portaria DECEA/DNOR1 nº 1.905, de 2025) e os Arts. 8º/9º remetem ao **MCA 100-27**, que não está entre as fontes admitidas. O manual usa o Anexo VII da ICA 100-12, que segue vigente, e nomeia a fonte em cada uso. Manuais futuros que precisem de definições enfrentam o mesmo.
- **Divergência real na Classe F**, documentada e **não resolvida** no manual: o Art. 21, VI, "c" condiciona o Serviço de Informação de Voo a pedido do piloto para todos os voos, enquanto a linha F/IFR do Anexo II omite a condição. O manual expõe as duas leituras. **Isto é uma pergunta para o revisor técnico.**
- **A numeração de artigos colide entre as duas ICAs.** Pelo menos Art. 21, 30, 32, 33, 34, 35, 38, 77, 93, 96, 97, 111, 114, 115, 116, 127 e 509 existem nas duas com significados diferentes. Toda citação do manual nomeia a ICA na própria frase por isso.
- **Regime transitório na ICA 100-12:** o Art. 96 vale até 31/12/2026 e o Art. 97 já vale na FIR Atlântico, passando a valer nas demais FIR em 1º/01/2027. Registrado no capítulo 01.
- **Qual classe se aplica a cada porção do espaço aéreo brasileiro** vem da AIP ENR 1.4 e muda por ciclo AIRAC. O manual não fixa esse dado — aponta para o AISWEB.

---

## Fora de escopo, por decisão

Declarado no `index.pt.md`: emergências e contingências, falha de comunicação, interceptação, espaços aéreos condicionados (áreas proibidas, restritas e perigosas), rotas ATS e aerovias, vetoração e separação radar.

Cada um é candidato a manual próprio. Na ordem que eu sugeriria: **vetoração e separação radar** (é a lacuna dos ratings S3 e C1, que hoje não têm material nenhum), depois **coordenação e transferência entre órgãos**, depois **contingências e emergências**.

---

## Documentos do projeto

- `specs/2026-08-07-espaco-aereo-servicos-ats-design.md` — spec de design
- `specs/2026-08-07-espaco-aereo-servicos-ats-plan.md` — plano de implementação em 9 tarefas
- `specs/2026-08-07-espaco-aereo-servicos-ats-imagens-pendentes.md` — registro das imagens pendentes
- Este handoff

Nenhum deles é servido pelo MkDocs: `specs/` está fora de `docs/`.
