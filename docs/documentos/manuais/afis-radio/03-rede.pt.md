---
title: AFIS na Rede
icon: material/access-point-network
---

--8<-- "includes/abreviacoes.md"

# AFIS na Rede

## A posição RÁDIO

Na Vatsim Brasil, o AFIS é prestado pelas posições com o sufixo **`_R_TWR`**, como `SBBU_R_TWR` (Rádio Bauru) e `SBTT_R_TWR` (Rádio Tabatinga). O `_R_` marca a RÁDIO e é uma convenção da Vatsim Brasil. O `_TWR` é só o tipo de conexão: o Código de Conduta da VATSIM lista os sufixos aceitos na rede, e nenhum deles é de AFIS[^1].

Três consequências práticas:

- **Rating:** pela tabela da GCAP, as posições `_TWR` exigem o rating **S2** (Aerodrome Controller)[^2]. Abrir uma RÁDIO exige o mesmo rating de uma torre.
- **Posições aprovadas:** só podem ser abertas as posições e frequências aprovadas (item C6 do Código de Conduta)[^1]. Use o indicativo e a frequência da página do aeródromo no MOP.
- **Alcance:** o alcance máximo de uma posição de torre é de 50 NM (item C8)[^1]. É mais do que o raio de 27 NM do AFIS sem FIZ publicada.

!!! note "Não confunda"
    A RÁDIO brasileira não é nenhuma das duas posições da GCAP com nome parecido. O **Flight Service Station** (`_FSS`) presta informação e assessoramento em rota e exige C1[^2]. O **Radio Operator** (`_RDO`) trabalha junto com um controlador, recebendo reportes de posição e retransmitindo instruções dele, e só fica on-line com esse controlador associado[^2]. A RÁDIO de aeródromo presta AFIS por conta própria.

## Onde estão as RÁDIOS

As páginas dos aeródromos com AFIS ficam na pasta `afis` de cada FIR, na seção [Aeródromos](../../../MOP/aerodromos/index.pt.md), com a etiqueta **Não-Controlado**. A tabela "Órgãos ATC" de cada página traz a posição, a abreviatura, o indicativo de chamada e a frequência. A observação da tabela diz quando o AFIS é prestado por outro órgão, como em Bauru, onde o AFIS é prestado pelo APP Bauru (`SBWU_APP`) na mesma frequência.

As páginas das [terminais](../../../MOP/terminais/index.pt.md) listam os aeródromos de cada TMA e, no diagrama de cobertura top-down, mostram em que posição cada RÁDIO se apoia.

## Horários do mundo real

No mundo real, muitos órgãos mudam com o horário: a torre que vira AFIS de madrugada, o APP que fecha e deixa uma FIZ no lugar da TMA, a RÁDIO que só funciona em dias úteis. As páginas do MOP registram isso como "No mundo real".

Na rede, vale a posição do pacote de setores, a qualquer hora. Se o aeródromo tem torre no pacote, é torre. Se tem RÁDIO, é RÁDIO.

## Cobertura top-down

A GCAP estabelece que as posições da VATSIM cobrem o espaço aéreo e as posições abaixo delas quando essas não estão ocupadas. É o princípio top-down. Ele vale para as posições que prestam serviço de controle, e a divisão pode estendê-lo a outras posições (GCAP 4.6 e 4.6(a))[^2]. Na Vatsim Brasil, as RÁDIOS entram na cobertura: no diagrama de cada TMA, a `_R_TWR` fica abaixo do APP, e o APP fica abaixo do centro.

Com a RÁDIO desconectada, quem está acima presta o Serviço de Informação de Voo na FIZ[^3]. O arranjo tem paralelo no mundo real: num aeródromo não controlado que é sede de um APP, é o próprio APP que presta o AFIS (Art. 784 da ICA 100-37)[^4]. Isso tem um efeito que pega muita gente:

!!! warning "O top-down não transforma a FIZ em espaço controlado"
    O APP ou o centro que cobre um aeródromo com AFIS presta **informação** dentro da FIZ, não controle. Não há autorização de pouso nem de decolagem a dar. O controlador acima usa a fraseologia da RÁDIO no aeródromo, com o próprio indicativo, e volta a controlar quando a aeronave entra no espaço aéreo controlado.

Sem ninguém conectado, nem direto nem por top-down, os pilotos usam a frequência de tráfego da rede. O Código de Conduta manda monitorar a frequência designada no espaço aéreo sem controlador, e usar 122.800 onde não houver uma frequência própria[^1].

!!! note "Mundo real e rede"
    No mundo real, fora do horário do AFIS o piloto usa a frequência do próprio órgão como frequência de coordenação entre aeronaves (FCA), e em aeródromo sem órgão ATS usa a FCA da AIP ou, se não houver, 123,45 MHz (Arts. 147 e 148 da ICA 100-37)[^4]. Na VATSIM vale o Código de Conduta: a frequência de tráfego da rede é 122.800.

## Abrindo e fechando a posição

Ao abrir a RÁDIO, alguém provavelmente estava cobrindo o aeródromo por top-down. Avise o APP ou o centro, pergunte sobre o tráfego que já está na FIZ ou chegando, e só depois comece a responder chamadas.

Ao fechar, faça o inverso: avise quem vai cobrir e diga aos pilotos na frequência com quem eles vão falar a partir dali. Se ninguém vai cobrir, diga que o aeródromo fica sem órgão ATS e que a frequência de tráfego passa a ser a da rede.

Esses passos seguem o mesmo padrão da passagem de serviço entre quaisquer posições, tratado no [Manual de Coordenação e Transferência](../coordenacao-transferencia/04-rede.pt.md).

## Coordenação com o APP e o centro

A RÁDIO não recebe nem transfere controle, porque não há controle a transferir. Um voo que sai de um aeródromo com AFIS entra na cadeia de controle no órgão que tem jurisdição sobre o espaço aéreo à frente, e não na torre. O que a RÁDIO coordena com esse órgão é informação:

| Situação | O que a RÁDIO coordena |
| --- | --- |
| IFR vai decolar | Pede a autorização ao órgão de controle, retransmite ao piloto e avisa a decolagem |
| IFR vai chegar | Recebe o aviso do órgão de controle e informa o tráfego local que possa conflitar com a aproximação |
| VFR vai sair da FIZ para o espaço controlado | Dá ao piloto a frequência do órgão seguinte. Não precisa coordenar, porque o piloto vai pedir a autorização |
| Aeronave não reportou no solo, ou não chamou o próximo órgão | Avisa o órgão em volta, como faria no Serviço de Alerta |

!!! note "Boa prática"
    Se o APP ou o centro preferir falar direto com o IFR que vai decolar, combine isso ao abrir a posição e diga ao piloto em que frequência pegar a autorização. O que não pode acontecer é o piloto receber duas autorizações diferentes, uma de cada frequência.

## ATIS

O Código de Conduta só permite ATIS de voz nos aeródromos que têm ATIS no mundo real, sempre com uma versão em texto em inglês (item C7(a))[^1]. Alguns aeródromos com AFIS têm ATIS no pacote, como `SBBU_ATIS`. Se o aeródromo tem ATIS, a informação do aeródromo pode citar a letra da informação, mas o tráfego conhecido continua a ser dado na frequência.

[^1]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), itens B5, C4, C6, C7(a) e C8.
[^2]: [**VATSIM, Global Controller Administration Policy (GCAP)**](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf), versão 2.0, de 15/08/2026: itens 4.5(e), 4.5(j), 4.6, 6.3 e 6.6.
[^3]: Página da [TMA São Paulo](../../../MOP/terminais/sbcw-curitiba/SBXP.pt.md), na seção Terminais: "Com a posição da FIZ desconectada, o `SBXP_APP` (ou a posição que o cobre) presta o serviço de informação de voo nela."
[^4]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Capítulo III, Seção XXI. Edição com a 2ª alteração (Portaria DECEA/DNOR1 nº 2.197, de 18/08/2026), em vigor em 26/11/2026.
