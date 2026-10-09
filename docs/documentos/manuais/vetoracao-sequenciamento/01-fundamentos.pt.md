---
title: Fundamentos da Vetoração
icon: material/compass-outline
---

--8<-- "includes/abreviacoes.md"

# Fundamentos da Vetoração

## Identificar antes de vetorar

Nenhuma vetoração começa sem identificação. Antes de prestar o Serviço de Vigilância ATS, o controlador precisa **estabelecer a identificação** da aeronave e **informar o piloto** disso. Essa identificação precisa ser mantida até o fim do serviço[^1]. Se ela se perder, o piloto também deve ser avisado[^2].

Os métodos mais usados com radar secundário (SSR) e ADS-B são[^3]:

| Método | Como fazer |
| --- | --- |
| Identificação na etiqueta | A etiqueta mostra o indicativo da aeronave, ou um código discreto já conferido. |
| Ajuste de código | Atribua um código ao piloto e observe a mudança na tela. |
| Acionamento de `IDENT` | Peça `IDENT` e observe a resposta. A função só deve ser acionada a pedido do controlador. |
| Transferência de identificação | O controlador anterior passa a aeronave já identificada. |

Um código discreto só pode servir de base para a identificação **depois de conferido**: confirme que o código selecionado pelo piloto é o atribuído[^4]. Na rede, isso significa confirmar que a etiqueta está correlacionada com o plano de voo certo, e não apenas que há uma etiqueta na tela.

Quando dois alvos estiverem muito próximos ou fizerem movimentos parecidos, use mais de um método até eliminar qualquer dúvida[^5].

### Informar a posição

Ao identificar a aeronave, informe sua posição. A exceção são as identificações feitas por transferência, pelo informe de posição do próprio piloto, por uma decolagem observada a menos de 1 NM do fim da pista ou pela etiqueta Modo S, ADS-B ou de código discreto, quando a posição na tela estiver de acordo com o plano de voo[^6]. A posição pode ser dada em relação a um ponto conhecido, por rumo e distância de um auxílio ou fixo, ou como distância do ponto de toque, quando a aeronave estiver na final[^7].

> **TAM 3501, contato radar, 40 milhas sul de Brasília, desça para FL 070, prevista aproximação ILS Z pista 29L.**

Com o Serviço de Vigilância ATS em curso, o piloto fica **dispensado de reportar posição** nos pontos compulsórios e só reporta onde o controle pedir[^8].

## O que é vetorar

Vetorar é dar à aeronave **proas e níveis** em lugar da rota que ela seguiria por conta própria. O Glossário ATM define a vetoração como a "provisão de orientação para navegação às aeronaves, em forma de **proas específicas** baseadas no uso de um Sistema de Vigilância ATS"[^glossario].

!!! info "Um direto não é vetoração"
    "Autorizado direto LOMEN" não é uma proa: o piloto navega por conta própria até o fixo. Por isso, um direto não é vetoração, mesmo quando tira a aeronave da trajetória publicada de uma STAR. O MCA 100-16 trata os dois casos separadamente, como "vetoração ou voo direto"[^diretos]. A diferença muda quem responde pela separação de obstáculos. Veja [E no direto?](#e-no-direto).

A ICA 100-37 é direta sobre o que a vetoração implica[^9]:

!!! danger "Sob vetoração, a navegação é sua"
    "Sempre que uma aeronave estiver sob vetoração, será proporcionado o Serviço de Controle de Tráfego Aéreo e **o controlador será o responsável pela navegação da aeronave**, devendo transmitir para a mesma as orientações de proa e as mudanças de nível que se tornarem necessárias."

A consequência mais séria está na separação de obstáculos. Fora da vetoração, o Serviço de Controle de Tráfego Aéreo não inclui a prevenção de colisão com o solo, e o piloto precisa verificar se a autorização é segura nesse aspecto. **Sob vetoração, essa verificação deixa de ser do piloto**[^10]. O piloto vetorado pode nem saber a posição exata em que está e, por isso, não tem como conferir a altitude segura. Cabe ao controlador emitir autorizações que garantam a separação de obstáculos **a todo momento**, até o ponto em que o piloto volta a navegar por conta própria[^11].

### Quando vetorar

A vetoração serve a seis objetivos[^12]:

1. estabelecer separação;
2. orientar a aeronave na execução de procedimentos especiais;
3. obter vantagem operacional para o controle ou para a aeronave, como uma sequência mais eficiente ou uma trajetória mais curta;
4. desviar a aeronave de formações meteorológicas ou de esteira de turbulência;
5. corrigir desvios de rota significativos;
6. atender a uma solicitação do piloto, quando possível.

Vetorar por vetorar não é um deles. Sempre que a rota publicada (SID, STAR, aerovia) resolver o problema, prefira-a. A carga de trabalho é menor para os dois lados, e uma falha de comunicação não deixa a aeronave sem rumo.

## Altitude mínima de vetoração

Como a separação de obstáculos passa a ser sua, toda proa precisa vir acompanhada de uma altitude segura **para o trecho que a aeronave vai sobrevoar**. A ICA 100-37 exige que o controlador tenha sempre informações completas e atualizadas sobre as altitudes mínimas de voo da área, os níveis mais baixos utilizáveis e as altitudes mínimas dos procedimentos baseados em vetoração[^13].

Nas TMAs que têm a carta, essa informação está na **ATCSMAC** (Carta de Altitude Mínima de Vigilância ATC), publicada pelo DECEA no AISWEB. Ela divide a TMA em setores com a altitude mínima de vetoração de cada um. Onde não houver ATCSMAC, use a referência mais conservadora entre a MSA da IAC e as altitudes mínimas das cartas de rota e de área.

!!! warning "Abaixo da MSA, só com a carta certa"
    A MSA da IAC é uma altitude de **segurança** num raio de 25 NM do auxílio. Ela não é a altitude mínima de vetoração. Vetorar abaixo da MSA só é seguro com a ATCSMAC (ou equivalente) na mão. Sem ela, mantenha a aeronave na MSA, ou acima dela, até que esteja estabilizada num procedimento publicado.

Quando o piloto pede para desviar de uma formação abaixo da altitude mínima de segurança publicada, a responsabilidade pela separação de obstáculos **volta para ele**. A fraseologia deixa isso explícito: o controlador informa a altitude mínima e aprova o desvio[^14].

### E no direto?

Num direto dado a uma aeronave em navegação própria, a regra da vetoração não se aplica em sentido estrito:

- **O piloto continua responsável pelo terreno.** Fora da vetoração, cabe ao piloto assegurar que a autorização é segura em relação ao solo[^10]. O voo IFR mantém o nível mínimo da rota e, fora de rota, voa pelo menos 1.000 pés (2.000 pés em área montanhosa) acima do obstáculo mais alto num raio de 8 km. O cálculo desse nível é do piloto[^regras-do-ar].
- **O controlador não autoriza abaixo do mínimo publicado.** As altitudes de uma STAR protegem só os segmentos publicados. No trecho direto, a referência é a altitude mínima da área: MSA ou TAA da IAC, AMA ou ATCSMAC[^mca-desvio]. O controlador precisa ter essas altitudes à mão[^13] e não pode emitir autorização abaixo delas[^altitudes-minimas].
- **Sob vetoração, o direto continua sendo vetoração.** Se a aeronave já estiver sendo vetorada e receber uma trajetória direta que a desvie da rota ATS, a separação de obstáculos continua com o controlador até o ponto em que o piloto reassume a navegação[^11]. É por isso que a fraseologia encerra a vetoração com "reassuma navegação, autorizado direto…".

!!! tip "Na prática"
    No direto a partir da navegação própria, autorize um nível igual ou acima da MSA (ou TAA/AMA) do trecho. Para autorizar abaixo da MSA, use a ATCSMAC, que é publicada para uso com vigilância. Esta é uma leitura combinada das normas citadas: nenhuma delas diz, literalmente, que o direto exige a ATCSMAC.

## Início, limites e término

### Início

O início da vetoração é marcado por uma informação do controlador de que a aeronave está **sob vetoração**[^15]. Se o primeiro vetor tirar a aeronave de uma rota estabelecida, informe também **o objetivo** do vetor. Quando a proa dada puder criar risco caso a comunicação seja perdida, especifique ainda **o limite** do vetor[^16].

> **TAM 3205, vetoração para final ILS pista 29L, curva à esquerda proa 240.**
>
> **TAM 3456, vetoração para sequenciamento, curva à esquerda proa 285, limite três minutos para reassumir a navegação direto NIMTO.**

### Métodos

Existem seis formas de dar um vetor[^17]:

| Método | Exemplo |
| --- | --- |
| Sentido da curva e proa final | "curva à direita proa 070" |
| Proa a voar | "voe proa 150" |
| Manter a proa atual | "mantenha presente proa" |
| Sentido e número de graus, quando a proa da aeronave não é conhecida e não há tempo para obtê-la | "curva 30 graus à esquerda" |
| Proa para abandonar um auxílio sobre o qual a aeronave está | "abandone BUENO na proa 240" |
| Curva e parada da curva, quando os instrumentos de orientação da aeronave não são confiáveis | "curva à direita... pare a curva" |

No método de número de graus, antes das manobras peça ao piloto que faça **todas as curvas à razão padrão** e cumpra as instruções **imediatamente** ao recebê-las[^17].

### Limites geográficos

- Fora de uma transferência de controle, **não vetore a menos de 2,5 NM do limite** do seu espaço aéreo. Se a separação mínima aplicável for maior que 5 NM, a distância mínima passa a ser **metade dessa separação**[^18].
- **Não vetore voos controlados para fora do espaço aéreo controlado**, exceto em emergência, para desviar de meteorologia (com aviso ao piloto) ou a pedido do piloto[^19].
- Sempre que possível, vetore por trajetórias em que o piloto consiga acompanhar a própria posição pelos auxílios à navegação. Isso reduz a assistência necessária e atenua uma eventual falha do sistema de vigilância[^20].

### Durante a vetoração

Enquanto a aeronave estiver sob vetoração, você deve[^21]:

1. atribuir uma altitude a manter, respeitando todas as restrições;
2. reconduzir a aeronave a um espaço aéreo controlado compatível com o destino;
3. dar uma proa que intercepte a radial ou o curso desejado **a uma distância que garanta a interceptação**;
4. avisar com antecedência se, por alguma razão, a aeronave precisar sair da cobertura radar e o piloto tiver de reassumir a navegação a partir de um ponto;
5. manter o piloto informado de sua posição.

### Término

Ao terminar a vetoração, instrua o piloto a **reassumir a navegação**. Se os vetores tiverem afastado a aeronave da rota atribuída, informe também a posição e dê as instruções necessárias[^22].

> **TAM 3702, 50 milhas sudeste do VOR Campo Grande, reassuma navegação na proa do VOR Urubupungá.**

Na aproximação, não é preciso informar o término do Serviço de Vigilância ATS quando a aeronave faz uma **aproximação visual** ou é vetorada **para o rumo de aproximação final**[^23]. A vetoração de um ILS termina quando a aeronave intercepta o curso de aproximação final e a trajetória de planeio[^24].

## Separação com vigilância ATS

### Mínimos

| Situação | Mínima | Fonte |
| --- | --- | --- |
| Separação horizontal com PSR, SSR, ADS-B ou MLAT | **5 NM** | [^25] |
| Somente radar de rota disponível na TMA ou CTR | **10 NM** | [^25] |
| Separação vertical aplicada por um APP | **1.000 pés** | [^26] |
| Aeronaves em espera sobre o mesmo fixo | **Não se aplica a mínima radar**: separe verticalmente | [^27] |

A distância é medida **entre os centros dos alvos**. Em nenhuma circunstância as bordas dos alvos podem se tocar ou se sobrepor sem separação vertical[^28]. Os mínimos radar só valem entre aeronaves **identificadas** cuja identificação provavelmente será mantida[^29]. Uma partida pode ser separada por radar desde a decolagem, desde que seja provável identificá-la a menos de 1 NM do fim da pista[^30].

!!! info "Mínimas reduzidas"
    A redução abaixo de 5 NM só é permitida conforme publicação específica do DECEA[^31], e no mundo real existe apenas em áreas determinadas. Na rede, aplique 5 NM, a menos que o MOP da TMA autorize outro valor.

### Níveis na tela

Pela altitude-pressão, uma aeronave é considerada[^32]:

| Situação | Critério (espaço aéreo RVSM) |
| --- | --- |
| **Mantendo** o nível | Dentro de ±200 pés do nível atribuído |
| **Livrando** o nível | Variou mais de 300 pés na direção prevista |
| **Cruzando** um nível na subida ou descida | Passou mais de 300 pés além dele, na direção prevista |
| **Atingindo** o nível autorizado | Está dentro de ±200 pés há três renovações ou 15 segundos, o que for maior |

Fora do espaço aéreo RVSM, a tolerância de **mantendo** e **atingindo** passa a ser de ±300 pés. Os critérios de **livrando** e **cruzando** não mudam.

Uma aeronave só pode ser autorizada a um nível ocupado por outra **depois que esta informar que o livrou**. Com turbulência forte, só depois de informar que já está no novo nível[^33].

### Esteira de turbulência

Nas fases de aproximação e decolagem, e em rota abaixo do FL 240, aplique os mínimos de esteira **quando forem maiores que os 5 NM**[^34]:

| À frente | Atrás | Mínima |
| --- | --- | --- |
| SUPER (`J`) | PESADA (`H`) | **6 NM** |
| SUPER (`J`) | MÉDIA (`M`) | **7 NM** |
| SUPER (`J`) | LEVE (`L`) | **8 NM** |
| PESADA (`H`) | PESADA (`H`) | **4 NM** |
| PESADA (`H`) | MÉDIA (`M`) | **5 NM** |
| PESADA (`H`) | LEVE (`L`) | **6 NM** |
| MÉDIA (`M`) | LEVE (`L`) | **5 NM** |

Esses mínimos valem quando a aeronave de trás segue a rota da da frente, ou a cruza, **na mesma altitude ou menos de 1.000 pés abaixo**, e quando as duas usam a mesma pista ou pistas paralelas a menos de 760 m[^35]. A categoria de cada tipo está no Doc 8643 da OACI e aparece no plano de voo (`A320/M`, `B77W/H`, `A388/J`). As categorias SUPER e PESADA devem se anunciar como "super" ou "pesada" no contato inicial[^36].

!!! tip "Na prática"
    A mínima que vale é sempre **a maior** entre a mínima radar e a de esteira. Um `B77W` seguido de um `A320` na final pede 5 NM pela esteira. Isso coincide com a mínima radar, e mesmo assim não há margem para compressão. Um `A320` seguido de um `C172` pede 5 NM pela esteira, e um `B77W` seguido de um `C172`, 6 NM.

[^1]: **ICA 100-37, Art. 906**. Ver [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 907**.
[^3]: **ICA 100-37, Arts. 909 e 910**.
[^4]: **ICA 100-37, Art. 911**.
[^5]: **ICA 100-37, Art. 914**.
[^6]: **ICA 100-37, Art. 917, inciso I**.
[^7]: **ICA 100-37, Art. 918**.
[^8]: **ICA 100-37, Art. 920**.
[^9]: **ICA 100-37, Art. 921**.
[^10]: **ICA 100-37, Art. 93, parágrafo único**.
[^11]: **ICA 100-37, Art. 922 e seu § 2°**.
[^12]: **ICA 100-37, Art. 924**.
[^13]: **ICA 100-37, Art. 934**.
[^14]: **MCA 100-16, Art. 117**. Ver [MCA 100-16](https://publicacoes.decea.mil.br/publicacao/MCA-100-16).
[^15]: **ICA 100-37, Art. 923**.
[^16]: **ICA 100-37, Art. 927**.
[^17]: **ICA 100-37, Art. 925 e parágrafo único**.
[^18]: **ICA 100-37, Art. 928**.
[^19]: **ICA 100-37, Art. 929**.
[^20]: **ICA 100-37, Art. 926**.
[^21]: **ICA 100-37, Art. 930**.
[^22]: **ICA 100-37, Art. 933**.
[^23]: **ICA 100-37, Art. 940**.
[^24]: **ICA 100-37, Art. 1008**.
[^25]: **ICA 100-37, Art. 953 e seu § 2°**.
[^26]: **ICA 100-37, Art. 432**.
[^27]: **ICA 100-37, Art. 952**.
[^28]: **ICA 100-37, Arts. 948 e 949**.
[^29]: **ICA 100-37, Art. 946**.
[^30]: **ICA 100-37, Art. 951**.
[^31]: **ICA 100-37, Art. 954**.
[^32]: **ICA 100-37, Arts. 897 a 901**.
[^33]: **ICA 100-37, Art. 433**.
[^34]: **ICA 100-37, Arts. 956 e 959, Tabela 11**.
[^35]: **ICA 100-37, Art. 960**.
[^36]: **ICA 100-37, Arts. 206 e 208**.
[^glossario]: **MCA 100-27, Glossário ATM, item 595**. A ICA 100-37 remete a esse glossário para as definições (Art. 9°). Ver [MCA 100-27](https://publicacoes.decea.mil.br/publicacao/MCA-100-27).
[^diretos]: **MCA 100-16, Art. 115, incisos VI, VIII e IX**.
[^regras-do-ar]: **ICA 100-12, Art. 137 e § 1°**. Ver [ICA 100-12](https://publicacoes.decea.mil.br/publicacao/ica-100-12).
[^mca-desvio]: **MCA 100-16, Art. 117**, que relaciona AMA, MSA, TAA e ATCSMAC como altitudes mínimas de segurança publicadas.
[^altitudes-minimas]: **ICA 100-37, Art. 302**.
