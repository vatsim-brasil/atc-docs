---
title: Operações Especiais
icon: material/shield-star-outline
---

--8<-- "includes/abreviacoes.md"

# Operações Especiais

Duas especialidades aparecem com frequência entre os helicópteros da rede: a operação **offshore**, de apoio às plataformas de petróleo, e as operações de **segurança pública e aeromédicas**. Esta página mostra o que a norma diz sobre cada uma e o que a VATSIM permite.

## Operações offshore

### No mundo real

O **espaço aéreo offshore** é o espaço destinado às operações de apoio à exploração de petróleo nas bacias petrolíferas. Ele começa **12 NM** da costa e vai até os limites laterais da FIR. A classe e os procedimentos de cada bacia ficam em publicação própria (ICA 100-4, itens 1.3 e 6.2)[^1].

Os critérios gerais, válidos para todas as bacias, são da ICA 100-4 (capítulo 6)[^1]:

| Regra | Item |
| --- | --- |
| Plano de voo completo é obrigatório entre o continente e as plataformas | 6.1.1 |
| A mensagem de pouso na plataforma é obrigatória. Sem órgão ATS, o radioperador da plataforma a encaminha | 6.1.2 e 6.1.3 |
| O helicóptero mantém comunicação o tempo todo com o órgão ATS responsável | 6.1.4 |
| À noite, só se opera em plataforma para remover enfermos ou feridos graves, ou em urgência que ameace o meio ambiente, a plataforma, pessoas ou a navegação | 6.3 |
| O ajuste de altímetro é responsabilidade do piloto | 6.4 |
| Sobre o mar, só dentro da cobertura de auxílio homologado ou com RNAV | 6.5 |
| Transponder modo A/C obrigatório. Em algumas bacias, também ADS-B | 6.6 |
| As medidas de fluxo são aplicadas de preferência no solo, antes da decolagem | 6.7 |

O voo IFR para uma plataforma exige heliponto homologado IFR. Se o heliponto da plataforma não for IFR, o plano de voo pode ter como destino o próprio aeródromo de partida, com "RMK/LDG (nome da plataforma), CASO VFR" no item 18. Na volta, a alternativa deve ficar no continente (item 6.8)[^1].

### O que o controlador faz

Para o controlador do continente, o voo offshore é um voo comum até sair da terminal:

- **GND e TWR:** tratam a saída como a de qualquer helicóptero. Confira se o plano de voo está preenchido e se o destino é uma plataforma ou o próprio aeródromo, com a plataforma no item 18.
- **APP e centro:** acompanham o helicóptero até o limite da jurisdição. Depois das 12 NM, ele entra no espaço aéreo offshore, e o serviço depende da classe publicada para a bacia.
- **Na volta:** o helicóptero chega como um voo vindo do mar, pela rota ou pelo ponto que a publicação da bacia prever. Sequencie-o com o tráfego do aeródromo costeiro.

### Na rede

As regras da VATSIM não falam de plataformas de petróleo. Como a rede usa as regras e os procedimentos do local simulado[^2], vale a ICA 100-4, com duas adaptações práticas:

- **Não há radioperador de plataforma.** A mensagem de pouso vira o reporte do piloto: peça que ele informe o pouso antes de sair da frequência, ou que se despeça ao chegar à plataforma.
- **Não há órgão offshore no pacote.** Fora do alcance do APP, o helicóptero fica com o centro, se houver. Sem ninguém on-line, o piloto usa a frequência de tráfego da rede, 122.800 (item B5 do Código de Conduta)[^2].

A Política de Operações Especiais trata de navios e plataformas com ATC próprio, mas só para organizações de operações especiais, e exige um acordo com a divisão[^3]. Um helicóptero civil que voa para uma plataforma não precisa disso.

## Segurança pública e aeromédico

### No mundo real

A norma brasileira dá a esses voos **prioridade**. A sequência de decolagem da ICA 100-37 é (Art. 601)[^4]:

1. aeronave em missão de defesa aeroespacial;
2. aeronave em operação militar (missão de guerra ou de segurança interna);
3. aeronave transportando ou destinada a transportar enfermo ou lesionado em estado grave, órgão vital ou radiofármacos;
4. aeronave em operação SAR ou engajada em operações de segurança pública;
5. aeronave conduzindo o Presidente da República;
6. aeronave em manobra militar;
7. demais aeronaves.

Na chegada, a ordem muda pouco: primeiro os planadores, depois o aeromédico e em seguida SAR e segurança pública (Art. 608)[^4]. As aeronaves de segurança pública são as definidas pela ANAC no RBAC 90, e a prioridade vale **só** quando elas estão engajadas em operação de segurança pública (Art. 3º, XXXI, e parágrafo único do Art. 601)[^4]. Um helicóptero da polícia em voo de traslado não tem prioridade.

A ICA 100-4 também prevê que esses helicópteros usem **áreas de pouso eventual**, sempre em VMC e em contato rádio bilateral com o órgão ATC, se o voo estiver sob controle (item 2.4.6)[^1].

### Na rede

Aqui está a maior diferença entre o mundo real e a VATSIM.

**Polícia, segurança pública, SAR e combate a incêndio** são operações restritas. O Código de Conduta diz que operações militares, paramilitares ou de agências governamentais civis "devem ser autorizadas e conduzidas por uma Virtual Special Operations Association (VSOA) aprovada" (item A13(b))[^2]. A lista de atividades restritas inclui busca e salvamento e combate a incêndio, de asa fixa ou rotativa[^3]. Um piloto que não pertence a uma VSOA não pode simular uma operação policial, nem uma busca e salvamento.

**Aeromédico comum** não está na lista. A Política de Operações Especiais só restringe os voos médicos em desastres e operações humanitárias, a partir de embarcações, depois de uma operação SAR e para aeroportos que só aceitam voos de socorro[^3]. Uma remoção de paciente entre hospitais pode ser voada por qualquer piloto.

**Ninguém pode exigir prioridade.** O Código de Conduta diz que nenhum voo pode se declarar prioritário sobre outro, e que o piloto só declara emergência sob controle, encerrando-a imediatamente se o controlador pedir (item B6)[^2]. Também proíbe simular sequestro, inclusive com o código 7500, e recriar desastres reais (itens B6 e A17)[^2].

O que isso significa para o controlador:

| Situação | O que fazer |
| --- | --- |
| Voo de uma VSOA, com o site da organização nas observações do plano de voo | É legítimo. Atenda como operação especial e acomode o voo sempre que der[^3] |
| Helicóptero "policial" sem VSOA | Atenda como um helicóptero civil comum. Não aplique a prioridade de segurança pública |
| Aeromédico comum | Atenda normalmente. A prioridade do Art. 601 pode ser dada a critério do controlador, se a carga de trabalho permitir. O piloto não pode exigi-la |
| Emergência declarada | Atenda como emergência. Se ela atrapalhar a operação, peça ao piloto que a encerre |
| Piloto insiste em operação restrita | Explique a regra com cortesia. Se ele continuar, chame um supervisor da rede |

!!! note "Como reconhecer um voo de VSOA"
    A Política de Operações Especiais manda os voos de VSOA colocarem o site da organização nas observações do plano de voo, justamente para que o ATC e a VATSIM possam identificá-los (item 8.5)[^3]. Sem isso, trate o voo como civil.

[^1]: [**ICA 100-4, Regras e Procedimentos Especiais de Tráfego Aéreo para Helicópteros**](https://publicacoes.decea.mil.br/publicacao/ica-100-4): item 1.3 (definições), item 2.4.6 (área de pouso eventual) e capítulo 6 (offshore). Portaria DECEA nº 109/DGCEA, de 21/07/2021.
[^2]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct): Propósito (regras do local simulado), itens A13(b), A17, B5 e B6. Revisão 2026.2.
[^3]: [**VATSIM, Special Operations Policy**](https://cdn.vatsim.net/policy-documents/VATSIM-POL-Special_Operations_v5.0.pdf), versão 5.0, de 14/05/2026: itens 4 (definições), 6 (atividades restritas), 8.5 (identificação no plano de voo), 9.3 (acomodação pelo ATC) e 10 (navios e plataformas).
[^4]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Art. 3º, XXXI, e Arts. 601 e 608 (prioridades). Edição com a 2ª alteração (Portaria DECEA/DNOR1 nº 2.197, de 18/08/2026), em vigor em 26/11/2026.
