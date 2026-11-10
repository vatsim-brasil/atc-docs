---
title: APP e as REH
icon: material/map-marker-path
---

--8<-- "includes/abreviacoes.md"

# APP e as REH

## O que é uma REH

Nas terminais com muito movimento de helicópteros, o DECEA publica **Rotas Especiais de Helicópteros (REH)**. A ICA 100-4 diz que elas podem ser estabelecidas "em função do volume e da complexidade do tráfego aéreo, [...] a fim de ordenar a circulação de helicópteros dentro de uma CTR/TMA" (item 5.4.1)[^1].

As AIC de circulação VFR descrevem a REH como uma rota VFR em forma de corredor, apoiada em referências visuais no terreno (rodovias, rios, pontes, estádios), "disposta [...] de maneira a não interferir em procedimentos IFR" e no tráfego local dos aeródromos principais. O corredor costuma ter **1 NM de largura**, meio para cada lado do eixo[^2]. A REH é diferente da REA, a Rota Especial de Aeronaves, que serve a aviões e helicópteros e tem 3 NM de largura. O helicóptero pode usar uma REA se cumprir as exigências dela[^2].

## Onde a REH é publicada

Cada terminal com REH tem:

- uma **AIC** de circulação VFR, com as regras gerais, a descrição de cada rota e as coordenadas dos pontos;
- as cartas **CCV REH**, Cartas de Corredores Visuais, com o desenho das rotas;
- eventuais procedimentos na **AIP** e nas **VAC** dos aeródromos.

No portal, as REH de cada terminal ficam na página da [terminal](../../../MOP/terminais/index.pt.md): a camada de mapa REH e a caixa "Documentos de navegação visual", com os links para as AIC e as cartas. Antes de abrir um APP com REH, abra essa página.

## As regras do helicóptero na REH

As regras abaixo valem em qualquer REH. Os valores de cada rota (altitudes, pontos, frequências) estão na publicação da terminal.

| Regra | Fonte |
| --- | --- |
| Com REH implantada, o helicóptero voa, em princípio, dentro dela, nos níveis ou altitudes estabelecidos para o sentido de voo | ICA 100-4, item 5.4.2[^1] |
| O helicóptero mantém os pontos de referência da rota **à sua direita**, salvo outra previsão na AIP | ICA 100-4, item 5.4.3[^1] |
| Voo VFR, com contato visual com o solo o tempo todo | AIC de circulação VFR[^2] |
| As altitudes mínimas da REH não tiram do piloto a responsabilidade de manter separação dos obstáculos | AIC de circulação VFR[^2] |
| Sem condições visuais, o piloto volta, pousa em outro lugar ou pede ao ATC autorização para continuar, inclusive mudando para IFR | AIC de circulação VFR[^2] |
| O helicóptero não cruza o alinhamento de pista nem trajetórias IFR sem autorização do órgão ATC | AIC de circulação VFR[^2] |

Algumas REH são **compulsórias**: o helicóptero só sai delas em emergência ou com autorização do órgão ATS. Outras são **recomendadas**, em geral em classe G, e o ingresso no espaço controlado continua dependendo de autorização[^2].

## Controle ou informação?

A classe do espaço aéreo de cada trecho da REH está na publicação, e pode ser diferente da classe da terminal em volta[^2]. É ela que diz o que o APP presta:

| Classe do trecho | O que o APP faz |
| --- | --- |
| **C ou D** (espaço controlado) | Autoriza o ingresso, controla o helicóptero e presta a separação e a informação de tráfego da classe |
| **G** (não controlado) | Não há controle nem serviço de vigilância ATS. O helicóptero fala com a frequência de coordenação publicada e só recebe informação de voo e alerta, se pedir |

O que cada classe dá ao VFR está no [Manual de Espaço Aéreo e Serviços ATS](../espaco-aereo-servicos-ats/index.md). O que importa aqui é não "controlar" um helicóptero em classe G: lá ele decide por conta própria.

## As atividades do APP

### Antes de abrir a posição

- Saiba quais REH passam pela sua terminal, onde elas cruzam as finais e as saídas IFR, e em que pontos o helicóptero passa da sua frequência para a de uma torre.
- Saiba as altitudes por sentido de voo. São elas que separam dois helicópteros em sentidos opostos.

### Identificação e transponder

As AIC das terminais com REH costumam tornar o transponder obrigatório em toda a área, inclusive em classe G, e definir um código para helicópteros que voam entre localidades sem órgão ATS[^2]. Quando o helicóptero entra no espaço controlado, dê a ele um código próprio e identifique-o como qualquer outro tráfego.

### O reporte padrão

Para não congestionar a frequência, as AIC pedem um primeiro contato curto, com destinatário, matrícula, rota, posição, altitude e sentido do deslocamento[^2]. Um reporte típico é:

> "Controle, PR-HEL, REH ALFA, vertical da PONTE, 1.500 pés, para o norte."

Se o piloto chamar com menos que isso, pergunte o que falta antes de autorizar.

### Ingresso e cruzamento

O ingresso de um helicóptero no espaço controlado pela REH depende de autorização. A autorização dá a rota, a altitude e o próximo ponto de reporte. Nos pontos em que a REH cruza uma final ou uma trajetória de saída IFR, o helicóptero precisa de autorização para cruzar.

!!! note "Boa prática"
    Se a final está ocupada, mande o helicóptero aguardar sobre o último ponto visual antes do cruzamento, e libere o cruzamento logo depois do pouso ou da decolagem. É mais rápido que desviá-lo da rota.

### Informação de tráfego

Dois helicópteros em sentidos opostos na mesma REH ficam em altitudes diferentes e cada um à direita do eixo. Mesmo assim, informe um ao outro. Informe também o helicóptero que vai passar perto de uma final sobre o tráfego que está nela, e o avião VFR que cruza uma REH sobre os helicópteros nela.

### Coordenação com a torre

A REH que entra numa CTR ou ATZ passa para a frequência da torre num ponto definido. Coordene com a torre antes de transferir, como faria com qualquer chegada VFR. A transferência é no ponto publicado, não no meio do corredor.

## Na rede

O APP é uma posição **S3** na GCAP, com alcance máximo de 150 NM[^3]. Com a torre e o solo fora do ar, o APP cobre os dois pelo princípio top-down (GCAP 4.6)[^3], inclusive os pousos e decolagens de helicópteros nos aeródromos da terminal.

Muitos pilotos de helicóptero na rede não conhecem as REH. Algumas regras práticas:

- se o piloto não tem a carta, indique a página da terminal no portal, que mostra as REH no mapa;
- se ele não consegue seguir a REH, autorize uma rota direta a um ponto visual, longe das finais e das saídas IFR, numa altitude que não conflite com elas;
- em classe G sem nenhum controlador, a frequência de coordenação publicada vira a frequência de tráfego da rede: o Código de Conduta manda usar a frequência designada ou, se não houver, 122.800 (item B5)[^4].

!!! warning "Sobrecarga"
    A GCAP permite ao controlador sobrecarregado reduzir o serviço, por exemplo deixando de cobrir um aeródromo por top-down (item 4.6(d))[^3]. Não permite ignorar os helicópteros que já estão na frequência. A política da Vatsim Brasil cita "recusar atendimento a tráfegos presentes" como conduta que prejudica a reputação da divisão[^5].

[^1]: [**ICA 100-4, Regras e Procedimentos Especiais de Tráfego Aéreo para Helicópteros**](https://publicacoes.decea.mil.br/publicacao/ica-100-4): item 5.4 (REH). Portaria DECEA nº 109/DGCEA, de 21/07/2021.
[^2]: AIC de circulação VFR das terminais com REH, como a [**AIC N 29/26**](https://publicacoes.decea.mil.br/publicacao/aic-n-2926) (itens 2.1, 3 e 4): definições de REH, REA, rotas compulsórias e recomendadas, classes do espaço aéreo, transponder e fonia. Os valores de cada terminal estão na AIC dela.
[^3]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), versão 2.0, de 15/08/2026: itens 4.6 e 4.6(d). Alcances máximos: [**Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item C8.
[^4]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item B5.
[^5]: [**Vatsim Brasil, Política de Divisão**](https://vatsim.com.br/documentos), item 3.6.
