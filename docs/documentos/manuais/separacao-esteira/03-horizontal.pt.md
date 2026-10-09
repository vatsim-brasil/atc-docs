---
title: Separação Horizontal
icon: material/arrow-left-right
---

--8<-- "includes/abreviacoes.md"

![Manual de Separação e Esteira de Turbulência - Separação Horizontal](img/manual-separacao-horizontal.png)

#

## Lateral e longitudinal

A separação horizontal mantém as aeronaves afastadas no plano horizontal, e tem duas formas[^1]:

- **Lateral**: as aeronaves estão em **rotas diferentes**, ou sobre **lugares geográficos diferentes**.
- **Longitudinal**: as aeronaves estão na mesma rota, em rotas opostas ou em rotas que se cruzam, com um **intervalo de tempo ou distância** entre elas.

Esta página trata primeiro da separação **convencional**, que se baseia em reportes de posição, estimados e distâncias informadas pelo piloto. A separação **com vigilância ATS**, que se mede na tela, está no fim da página e é a que você vai usar na maior parte do tempo na rede.

!!! info "Quando a separação convencional aparece na rede"
    A separação convencional quase não é usada nas posições continentais da Vatsim Brasil, porque elas têm vigilância. Ela aparece no controle oceânico, quando um alvo some da tela e nos mínimos de partida, que a torre e o APP usam mesmo com radar. Leia esta parte para entender a lógica, e use-a quando a vigilância não estiver disponível.

## Separação lateral

### Por lugares geográficos

O método mais simples: a aeronave reporta estar sobre um ponto e a outra, sobre outro ponto, e os dois lugares são claramente diferentes. A posição pode ser determinada visualmente ou por referência a um auxílio à navegação[^2].

### Por rotas divergentes

Duas aeronaves em rotas que partem de um mesmo auxílio ou ponto estão separadas lateralmente quando[^3]:

| Navegação | Condição |
| --- | --- |
| **VOR** | Radiais que divergem pelo menos **15°**, e pelo menos uma aeronave a **15 NM** ou mais do VOR |
| **NDB** | Rotas para ou do NDB que divergem pelo menos **30°**, e pelo menos uma aeronave a **15 NM** ou mais do NDB |
| **GNSS**, ou **VOR** e **GNSS** | Rotas que divergem de **15° a 135°**, e pelo menos uma aeronave a **15 NM** do ponto comum, do FL 010 ao FL 190, ou a **23 NM**, do FL 200 ao FL 600 |

Em rotas **opostas** ou que **se cruzam**, isso não basta. Estabeleça a separação vertical **antes** de as aeronaves chegarem a 15 NM do auxílio ou do ponto de cruzamento[^4].

Antes de usar a separação baseada em GNSS, confirme que a aeronave está navegando por GNSS e que não está voando com deslocamento lateral (SLOP)[^5]. Não use separação GNSS se o piloto reportar perda de RAIM[^6].

### Em procedimentos publicados

Aeronaves que saem ou chegam por procedimentos publicados (SID, STAR, IAC) estão separadas lateralmente quando a distância entre as rotas for de pelo menos[^7]:

| Combinação | Distância |
| --- | --- |
| RNAV 1 com RNAV 1, RNP 1, RNP APCH ou RNP AR APCH | **7 NM** |
| RNP 1, RNP APCH ou RNP AR APCH entre si | **5 NM** |

Elas também estão separadas quando as áreas de proteção das trajetórias não se sobrepõem.

### Em curvas

Se a rota de uma aeronave tiver uma curva que vai fazer a separação lateral deixar de existir, estabeleça **outra** separação antes de a aeronave iniciar a curva[^8]. Lembre-se de que uma curva **fly-by** pode começar até 20 NM antes do waypoint e passar por dentro dele. Já numa curva **flyover**, a aeronave sobrevoa o waypoint e só depois vira, ficando por fora da curva[^8].

## Separação longitudinal

### O que é "mesma rota"

Para a separação longitudinal, a diferença de ângulo entre as rotas define o caso[^9]:

| Caso | Diferença angular |
| --- | --- |
| **Mesma rota** | Menor que 45°, ou maior que 315° |
| **Rotas opostas** | Maior que 135° e menor que 225° |
| **Rotas que se cruzam** | Os demais casos: de 45° a 135°, e de 225° a 315° |

### Cuidado com a de trás mais rápida

O mínimo longitudinal vale o tempo todo, e não só no momento em que você o confere. Se a aeronave de trás for **mais rápida** que a da frente, a distância entre elas diminui. Quando a separação for chegar ao mínimo, ajuste a velocidade para mantê-la[^10].

### Por tempo

A separação por tempo usa reportes de posição e estimados, e é o que se usa sem vigilância e sem DME.

| Situação | Mínimo | Fonte |
| --- | --- | --- |
| Mesmo nível, mesma rota | **15 min** | [^11] |
| Mesmo nível, mesma rota, com auxílios que permitem determinar posição e velocidade continuamente | **10 min** | [^11] |
| Mesmo nível, mesma rota, da frente **20 kt** ou mais rápida (TAS) | **5 min** | [^11] |
| Mesmo nível, mesma rota, da frente **40 kt** ou mais rápida (TAS) | **3 min** | [^11] |
| Mesmo nível, rotas que se cruzam, no ponto de cruzamento | **15 min**, ou **10 min** com auxílios | [^12] |
| Rotas opostas, sem separação lateral | Vertical de **10 min antes** até **10 min depois** do cruzamento estimado | [^13] |

Os mínimos de 5 e 3 minutos só valem entre aeronaves que decolaram do mesmo aeródromo, entre aeronaves em rota que reportaram o mesmo ponto, ou entre uma partida e uma aeronave em rota que já reportou um ponto que garante a separação onde a partida vai entrar na rota[^11].

Em rotas opostas, se for possível ter **certeza** de que as aeronaves já se cruzaram, os 10 minutos depois do cruzamento deixam de ser necessários[^13].

### Subindo ou descendo

Quando uma aeronave sobe ou desce **através** do nível de outra, sem separação vertical:

| Situação | Mínimo | Fonte |
| --- | --- | --- |
| Mesma rota | **15 min** | [^14] |
| Mesma rota, com auxílios que permitem determinar posição e velocidade com frequência | **10 min** | [^14] |
| Mesma rota, com a mudança de nível iniciada até 10 min depois de a segunda aeronave reportar um ponto de notificação | **5 min** | [^14] |
| Rotas que se cruzam | **15 min**, ou **10 min** com auxílios | [^15] |

### Por distância DME ou GNSS

Com DME ou GNSS, as distâncias informadas pelos pilotos substituem o tempo. As duas aeronaves devem estar usando a **mesma estação DME**, um DME e um waypoint no mesmo local, ou o **mesmo waypoint**, e voando direto para ele ou se afastando dele[^16]. Mantenha comunicação direta em VHF com as duas enquanto aplicar essa separação[^17]. Se ambas tiverem navegação de área, peça especificamente a **distância GNSS**[^18].

| Situação | Mínimo | Fonte |
| --- | --- | --- |
| Mesmo nível, mesma rota | **20 NM** | [^19] |
| Mesmo nível, mesma rota, da frente **20 kt** ou mais rápida (TAS) | **10 NM** | [^20] |
| Mesmo nível, rotas que se cruzam em menos de 90°, com distâncias do mesmo ponto no cruzamento | **20 NM**, ou **10 NM** com 20 kt | [^21] |
| Subindo ou descendo, mesma rota, **uma delas mantendo nível** | **10 NM** | [^22] |
| Rotas opostas, depois de **confirmado** o cruzamento | **10 NM** para subir ou descer através do nível da outra | [^23] |

A distância deve ser conferida com leituras **simultâneas** das duas aeronaves, a intervalos frequentes[^19].

## Partidas

Os mínimos de partida da ICA 100-37 completam os anteriores e são aplicados entre aeronaves que acabaram de decolar[^24]:

| Situação | Mínimo | Fonte |
| --- | --- | --- |
| Rotas que divergem pelo menos **45°** logo após a decolagem, de modo que haja separação lateral | **1 min** | [^25] |
| Mesma rota, com a da frente **40 kt** ou mais rápida | **2 min** | [^26] |
| Mesma rota, a de trás cruzando o nível da da frente sem separação vertical | **5 min** | [^27] |

No mínimo de 2 minutos, a diferença de velocidade na subida pode ser mais bem estimada pela IAS do que pela TAS[^26].

A separação entre uma partida e uma chegada no mesmo aeródromo está em [Separação no Aeródromo](05-aerodromo.pt.md#partidas-e-chegadas).

## Com vigilância ATS

Com vigilância ATS, a separação horizontal deixa de depender de reportes e passa a ser medida na tela.

| Situação | Mínimo | Fonte |
| --- | --- | --- |
| Separação com PSR, SSR, ADS-B ou MLAT | **5 NM** | [^28] |
| Na TMA ou CTR, se só houver radar de rota | **10 NM** | [^28] |
| Esteira de turbulência, se for maior que o mínimo radar | Ver [Esteira de Turbulência](04-esteira.pt.md#com-vigilancia-ats) | [^29] |

As regras de aplicação são:

- A distância é medida entre os **centros dos alvos**. As bordas nunca podem se tocar ou se sobrepor sem separação vertical[^30].
- Os mínimos só valem entre aeronaves **identificadas**, quando for provável que a identificação vai ser mantida[^31].
- Uma partida pode ser separada pelos mínimos de vigilância desde a decolagem, se for provável que ela seja identificada a até **1 NM** do fim da pista[^32].
- Os mínimos de vigilância **não** valem entre aeronaves na **mesma espera**. Separe-as verticalmente[^33].
- Se um voo controlado ainda não identificado entrar no seu espaço aéreo, mantenha as aeronaves identificadas separadas de **todos** os alvos que aparecem na tela, até identificá-lo ou estabelecer a separação convencional[^34].
- Se o controle vai passar para um setor ou órgão que só presta separação **convencional**, estabeleça essa separação **antes** de a aeronave chegar ao limite do seu espaço aéreo ou sair da cobertura de vigilância[^35].

Como medir e manter os 5 NM com vetores e velocidade está no [Manual de Vetoração e Sequenciamento](../vetoracao-sequenciamento/01-fundamentos.pt.md#separacao-com-vigilancia-ats).

!!! tip "No EuroScope"
    `F1 + D` (`.distance`) mostra a distância atualizada entre uma aeronave e outra aeronave ou ponto. `F1 + S` (`.sep`) prevê o ponto de maior aproximação entre duas aeronaves. Use a segunda **antes** de autorizar uma subida ou descida através do nível de outro tráfego. Veja [Comandos](../../../fundamentos/softwares/euroscope/comandos.pt.md).

[^1]: **ICA 100-37, Art. 334**, e **Art. 39, § 2°, inciso II**. Ver [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 341**.
[^3]: **ICA 100-37, Art. 342, § 1°, e Tabela 2**.
[^4]: **ICA 100-37, Art. 343**.
[^5]: **ICA 100-37, Art. 344**.
[^6]: **ICA 100-37, Art. 346**.
[^7]: **ICA 100-37, Art. 349**.
[^8]: **ICA 100-37, Art. 338 e §§ 1° e 2°**.
[^9]: **ICA 100-37, Art. 360**.
[^10]: **ICA 100-37, Art. 357 e parágrafo único**.
[^11]: **ICA 100-37, Art. 362**.
[^12]: **ICA 100-37, Art. 363**.
[^13]: **ICA 100-37, Art. 366**.
[^14]: **ICA 100-37, Art. 364, § 1°**.
[^15]: **ICA 100-37, Art. 365**.
[^16]: **ICA 100-37, Arts. 367 e 368, caput e § 1°**.
[^17]: **ICA 100-37, Art. 368, § 2°**.
[^18]: **ICA 100-37, Art. 369**.
[^19]: **ICA 100-37, Art. 370**.
[^20]: **ICA 100-37, Art. 371**.
[^21]: **ICA 100-37, Art. 372**.
[^22]: **ICA 100-37, Art. 373**.
[^23]: **ICA 100-37, Art. 374**.
[^24]: **ICA 100-37, Art. 434**.
[^25]: **ICA 100-37, Art. 435**.
[^26]: **ICA 100-37, Art. 436 e parágrafo único**.
[^27]: **ICA 100-37, Art. 437 e parágrafo único**.
[^28]: **ICA 100-37, Art. 953 e §§ 1° e 2°**.
[^29]: **ICA 100-37, Art. 956**.
[^30]: **ICA 100-37, Arts. 948 e 949**.
[^31]: **ICA 100-37, Art. 946**.
[^32]: **ICA 100-37, Art. 951**.
[^33]: **ICA 100-37, Art. 952**.
[^34]: **ICA 100-37, Art. 950**.
[^35]: **ICA 100-37, Art. 947**.
