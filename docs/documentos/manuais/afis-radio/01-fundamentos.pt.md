---
title: Fundamentos do AFIS
icon: material/information-outline
---

--8<-- "includes/abreviacoes.md"

# Fundamentos do AFIS

## O que é o AFIS

O Serviço de Informação de Voo de Aeródromo, o AFIS, é o Serviço de Informação de Voo prestado no próprio aeródromo. A ICA 100-37 diz que ele é normalmente prestado por um órgão ATS identificado como **"RÁDIO"** (Art. 783) e define o que esse órgão presta: "o Serviço de Informação de Voo e, adicionalmente, o Serviço de Alerta a todo o tráfego em operação na área de movimento do aeródromo e a todas as aeronaves em voo no espaço aéreo Classe G nas imediações do mesmo" (Art. 783, parágrafo único)[^1].

São dois serviços, e nenhum deles é controle:

- **Informação de voo:** avisos e informações úteis para que o voo seja seguro e eficiente. O vento, o ajuste de altímetro, as condições do aeródromo, os auxílios fora de serviço e o tráfego conhecido.
- **Alerta:** notificar os órgãos competentes quando uma aeronave precisa de busca e salvamento, e ajudar esses órgãos.

## Onde o AFIS é prestado

O AFIS é normalmente prestado dentro de uma **Zona de Informação de Voo (FIZ)**, publicada na AIP-Brasil (Art. 786)[^1]. Onde não houver FIZ publicada, o Art. 787 estende o serviço à área de movimento e a todas as aeronaves em voo em Classe G abaixo do FL 145, num raio de 27 NM (50 km) do aeródromo[^1].

As FIZ estão na ENR 2.2 da AIP[^2]. Todas são **Classe G**, mas variam muito de tamanho:

| FIZ | Limites laterais | Limites verticais | Indicativo |
| --- | --- | --- | --- |
| Araraquara | polígono | GND – 5000 FT | Rádio Araraquara |
| Bacacheri | polígono | GND – 4500 FT | Rádio Bacacheri |
| Caxias do Sul | polígono | GND – 5500 FT | Rádio Caxias |
| Gavião Peixoto | polígono com arcos de 27 NM | GND – 5500 FT | Rádio Gavião |
| Noronha | círculo de 27 NM | GND – FL 145 | Rádio Noronha |

Fonte: AIP-Brasil, ENR 2.2, emenda de 01/10/2026[^2].

Uma FIZ pode ficar **embaixo de uma TMA**. Nesse caso, o voo dentro da FIZ é Classe G, mas acima do teto dela começa o espaço aéreo controlado da TMA. A RÁDIO só presta serviço até o teto da FIZ.

## Quem presta o AFIS

O caso normal é uma RÁDIO no aeródromo. A AIP mostra outras formas, e todas aparecem na rede:

| Forma | Exemplo na AIP | O que muda |
| --- | --- | --- |
| RÁDIO no aeródromo | Caxias do Sul FIZ, "RÁDIO CAXIAS" | Nada: é o caso descrito neste manual |
| RÁDIO remota (R-AFIS) | Noronha FIZ, "RÁDIO NORONHA", marcada R-AFIS | O operador está em outro lugar. Para o piloto, a fonia é a mesma |
| APP que presta o AFIS | Bacacheri FIZ, prestada pelo APP Curitiba, com o indicativo "RÁDIO BACACHERI" | O mesmo órgão presta controle na TMA e informação na FIZ |
| TWR que presta o AFIS | Maringá FIZ, "AFIS MARINGÁ", prestada pela torre | A torre vira AFIS fora do horário dela |

Fonte: AIP-Brasil, ENR 2.2[^2].

A forma de prestar não muda o serviço. Se o APP ou a torre prestam AFIS numa FIZ, eles prestam **informação**, não controle, enquanto a aeronave estiver na FIZ.

!!! note "Na rede"
    Na Vatsim Brasil, todas essas formas viram a mesma coisa: uma posição `_R_TWR` com indicativo de RÁDIO, ou o APP cobrindo o aeródromo por top-down. Os horários do mundo real não se aplicam. Ver [AFIS na Rede](03-rede.pt.md).

## O que a RÁDIO não presta

A ICA 100-37 é direta: dentro da FIZ "não há prestação de Serviço de Controle de Tráfego Aéreo e, por isso, não devem ser esperadas autorizações de controle de tráfego aéreo" (Art. 786, § 1°)[^1].

| A RÁDIO faz | A RÁDIO não faz |
| --- | --- |
| Informa o vento, o ajuste de altímetro, a temperatura e as condições do aeródromo | Autoriza pouso, decolagem, toque e arremetida ou táxi |
| Informa a pista que os outros tráfegos estão usando | Escolhe a pista do piloto |
| Informa o tráfego conhecido: tipo, posição, altitude e intenção | Separa tráfego ou sequencia chegadas |
| Pede reportes: perna do vento, final, no solo, pista livre | Dá proas, níveis ou velocidades |
| Retransmite autorizações de outro órgão, dizendo quem autorizou | Emite autorização própria |
| Aciona o Serviço de Alerta | Transfere controle: não há controle a transferir |

O elemento que mais confunde é a retransmissão. Entre os elementos básicos de informação que a RÁDIO transmite estão as "mensagens, incluindo autorizações, recebidas de outros órgãos ATS para retransmissão à aeronave" (Art. 788, VII)[^1]. A única autorização que passa pela frequência da RÁDIO é a de **outro** órgão, e a RÁDIO deixa claro de quem ela partiu.

!!! danger "Ciente, não autorizado"
    A resposta da RÁDIO a um reporte é **ciente**. "Autorizado pouso" ou "livre decolagem" na frequência da RÁDIO são erros: transmitem ao piloto uma autorização que ninguém tem autoridade para dar. Se o piloto pede autorização, a RÁDIO informa as condições e o tráfego conhecido, e a decisão fica com ele.

## A responsabilidade do piloto

Na FIZ, quem evita colisão é o piloto. A ICA 100-37 dedica uma subseção do AFIS à responsabilidade do piloto em comando durante a aproximação, o pouso, a decolagem e o movimento no solo (Art. 791)[^1]. A RÁDIO ajuda com informação, mas não assume a separação.

Isso vale também para o IFR. Fora do espaço aéreo controlado, a aeronave IFR não recebe separação. A AIP deixa isso explícito para a FIZ Sorocaba, onde o procedimento IFR de SDCO fica todo em Classe G: as aeronaves que o executam "devem providenciar sua própria separação" em relação às demais aeronaves na FIZ[^2].

## O Serviço de Alerta

O Serviço de Alerta é acionado quando a aeronave recebe Serviço de Controle de Tráfego Aéreo, quando apresentou Plano de Voo e teve a decolagem notificada a um órgão ATS, ou quando se sabe ou se suspeita que está sob interferência ilícita (Art. 795)[^1]. A responsabilidade de iniciar o serviço numa emergência é da "TWR, APP ou RDO (rádio) que tomar conhecimento de uma emergência em voo VFR ou IFR", que notifica imediatamente o ACC e o ARCC correspondentes (Art. 797)[^1].

Para a RÁDIO, isso significa acompanhar cada aeronave até o fim: quem reportou na final e não reportou no solo, ou quem decolou e não chamou o próximo órgão, é um caso para o Serviço de Alerta.

!!! note "Na rede"
    Na VATSIM não há ARCC. O equivalente prático é perguntar ao piloto, verificar se ele ainda está conectado e avisar o APP ou o centro que tem jurisdição em volta. Emergências na rede seguem o Código de Conduta: o piloto só declara emergência sob controle, e encerra a emergência se o controlador pedir[^3].

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Seção V do capítulo do Serviço de Informação de Voo (AFIS) e capítulo do Serviço de Alerta. Edição em vigor em 27/11/2025.
[^2]: [**AIP-Brasil, ENR 2.2**](https://aisweb.decea.mil.br/?i=publicacoes&p=aip): tabela das FIZ, emenda de 01/10/2026.
[^3]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item B6.
