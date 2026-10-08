---
title: Coordenação na Rede
icon: material/lan-connect
---

--8<-- "includes/abreviacoes.md"

![Manual de Coordenação e Transferência - Coordenação na Rede](img/manual-coordenacao-rede.png)

#

## O que muda na VATSIM

No mundo real, cada órgão funciona no horário publicado e sempre há alguém do outro lado da fronteira. Na rede, as posições abrem e fecham conforme os controladores se conectam. O vizinho com quem você coordenava há uma hora pode ter saído, e o espaço aéreo dele pode ter passado para outro controlador, ou para ninguém. Três regras cobrem essa diferença: a cobertura top-down, a passagem de serviço ao abrir e fechar posições, e o tratamento do espaço aéreo sem controlador.

## Cobertura top-down

A GCAP estabelece que as posições da VATSIM **cobrem o espaço aéreo e as posições abaixo delas quando essas não estão ocupadas**. É o princípio top-down[^1]. Ele vale para as posições que prestam serviço de controle[^2].

| Posição online | Cobre, se estiverem desconectadas |
| --- | --- |
| `TWR` | `GND` e `DEL` do mesmo aeródromo |
| `APP` | `TWR`, `GND` e `DEL` dos aeródromos da TMA |
| `CTR` | `APP`, `TWR`, `GND` e `DEL` sob o setor |

Onde a cobertura for ambígua, como em espaços aéreos compartilhados ou sobrepostos, a divisão ou subdivisão decide quais posições estão "abaixo" de quais[^3]. Na Vatsim Brasil, a ordem de cobertura de cada TMA está na seção [Terminais](../../../MOP/terminais/index.pt.md), no diagrama "Cobertura top-down" de cada página.

Cobrir uma posição significa prestar o serviço dela. Um `APP` que cobre uma torre dá a autorização de tráfego, o táxi e as autorizações de pouso e decolagem daquele aeródromo, além do próprio trabalho de aproximação. O piloto chama a posição que está online, na frequência dela.

!!! info "Serviço reduzido"
    Um controlador sobrecarregado pode prestar um serviço reduzido, por exemplo **retirando a cobertura top-down de um aeródromo**. Nesse caso, a GCAP recomenda considerar se não seria melhor conectar numa posição menor ou num setor desmembrado[^4]. Se retirar a cobertura, avise os pilotos afetados e os controladores vizinhos.

### Posições que exigem endorsement

Enquanto um controlador com o endorsement necessário estiver na posição abaixo ou adjacente, quem está acima não precisa ter esse endorsement. Se esse controlador sair, quem está acima **deve desconectar imediatamente** caso não tenha o endorsement[^5]. Um exemplo é a FIR Atlântico, cujo MOP trata disso em [Abertura de posição](../../../MOP/oceanico/atc/abertura.pt.md).

## Abrir uma posição

Quando você abre uma posição, alguém provavelmente estava cobrindo aquele espaço aéreo por top-down. A passagem de serviço é uma coordenação como outra qualquer:

1. **Veja quem está online** acima, abaixo e ao lado da sua posição.
2. **Combine com quem estava cobrindo** o momento em que você assume. Pergunte sobre tráfego com restrição, espera, emergência ou coordenação pendente.
3. **Receba os tráfegos** que estão no seu espaço aéreo pela transferência da etiqueta. Quem cobria transfere com `F4`, você aceita com `F3`, e só então os pilotos mudam para a sua frequência.
4. **Coordene com os adjacentes** os pontos de transferência, se forem diferentes do padrão do manual operacional.

Se você cair e voltar em um tempo razoável, o controlador que assumiu sua posição nesse meio-tempo deve devolvê-la[^6].

## Fechar uma posição

Fechar é abrir ao contrário, com uma diferença: os pilotos vão perder a frequência em que estão.

!!! danger "Não desconecte com tráfego assumido"
    Antes de sair, **transfira cada tráfego** para quem vai cobrir o seu espaço aéreo, ou encerre o serviço de cada um e diga para onde ele deve chamar. Desconectar com etiquetas assumidas deixa aeronaves sem ninguém responsável por elas, que é exatamente o que a coordenação existe para evitar.

!!! note "Boa prática"
    1. Avise os vizinhos alguns minutos antes de fechar, para que se preparem para receber o tráfego.
    2. Pare de aceitar novos tráfegos se a posição de cima puder recebê-los diretamente.
    3. Transfira os tráfegos um a um, com a frequência certa de quem vai cobrir.
    4. Só desconecte depois que não houver mais nenhuma etiqueta assumida por você.

## Espaço aéreo sem controlador

Nem sempre há alguém para receber a aeronave. Quando o próximo espaço aéreo não tem controlador, nem direto nem por top-down, não existe com quem coordenar:

- **Aeronave saindo do seu espaço para um espaço sem controle:** encerre o serviço e oriente o piloto a monitorar a frequência de aconselhamento designada (UNICOM). A VATSIM exige que o piloto em espaço sem controlador monitore essa frequência até voltar a ter cobertura[^7].
- **Aeronave entrando no seu espaço vinda de um espaço sem controle:** ela chega sem coordenação. Identifique-a, confirme rota e nível, e dê a autorização como se fosse a chamada inicial de um voo no seu espaço.

## Ferramentas de coordenação

| Ferramenta | Use para |
| --- | --- |
| Transferência pela etiqueta (`F4` / `F3`) | A transferência de rotina, sem prévia coordenação. Veja [Transferência de Controle](02-transferencia.pt.md#no-euroscope) |
| *Point out* (`F1 + P`) | Avisar um vizinho de um tráfego que passa perto do limite sem entrar no espaço dele |
| Chat privado (`.chat` + indicativo do controlador) | Estimados, pedidos de nível, liberações, mudanças de plano, tudo o que a etiqueta não mostra |
| Canal `ATC` | Avisos para todos os controladores, como abertura e fechamento de posição |
| Canal de voz combinado entre os controladores | Coordenações longas ou urgentes, quando houver |

!!! tip "Mensagens curtas"
    Escreva no chat como se falasse na linha de coordenação: indicativo, ponto, hora e nível, nessa ordem. "VRG2320 ESTIMA VARGA 55 FL330" basta. Os modelos estão na [Fraseologia](05-fraseologia.pt.md#mensagens-entre-orgaos).

[^1]: **VATSIM, GCAP, item 4.6**. Ver [GCAP](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf).
[^2]: **VATSIM, GCAP, item 4.6(a)**.
[^3]: **VATSIM, GCAP, item 4.6(b)**.
[^4]: **VATSIM, GCAP, item 4.6(d)**.
[^5]: **VATSIM, GCAP, item 6.1(a)**.
[^6]: **VATSIM, Code of Conduct, item C5**. Ver [Code of Conduct](https://vatsim.net/docs/policy/code-of-conduct).
[^7]: **VATSIM, Code of Conduct, item B5**.
