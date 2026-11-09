---
title: Fundamentos do AFIS
icon: material/information-outline
---

--8<-- "includes/abreviacoes.md"

# Fundamentos do AFIS

## O que é o AFIS

A ICA 100-37 define o Serviço de Informação de Voo de Aeródromo, o AFIS, como "um serviço que tem por finalidade proporcionar as informações que assegurem a condução eficiente do tráfego aéreo nos aeródromos que não disponham de órgão ATC ou este não esteja no seu horário de funcionamento" (Art. 782)[^1].

Ele é normalmente prestado por um órgão ATS identificado como **"RÁDIO"**, localizado no aeródromo ou remotamente (Art. 783). Esse órgão "presta o Serviço de Informação de Voo e, adicionalmente, o Serviço de Alerta a todo o tráfego em operação na área de movimento do aeródromo e a todas as aeronaves em voo no espaço aéreo Classe G nas imediações do mesmo" (Art. 783, parágrafo único)[^1].

São dois serviços, e nenhum deles é controle:

- **Informação de voo:** as informações de que o piloto precisa para operar no aeródromo. O vento, o ajuste de altímetro, a pista que os outros estão usando, o tráfego conhecido e as condições do aeródromo.
- **Alerta:** notificar os órgãos competentes quando uma aeronave precisa de busca e salvamento, e ajudar esses órgãos.

## Onde o AFIS é prestado

O AFIS é normalmente prestado dentro de uma **Zona de Informação de Voo (FIZ)**, divulgada na AIP-Brasil, com a configuração definida pelas características e necessidades da localidade (Art. 786)[^1]. Onde não houver FIZ publicada, o serviço é prestado, além da área de movimento, a todas as aeronaves em voo em Classe G abaixo do FL 145 e num raio de 27 NM (50 km) do aeródromo (Art. 787)[^1].

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

O caso normal é uma RÁDIO no aeródromo, mas a própria ICA 100-37 prevê outros arranjos. Num aeródromo não controlado que é sede de um APP, o AFIS é prestado por esse APP (Art. 784). Um APP pode também prestar AFIS em outro aeródromo, desde que o aeródromo fique numa CTR da jurisdição dele, a Organização Regional do DECEA concorde, um controlador fique responsável pelo AFIS de um único aeródromo e uma avaliação de risco mostre que a operação é viável (Art. 785)[^1]. O MCA 100-16 resume: os órgãos que prestam AFIS são **RDO, APP ou TWR** (Art. 153)[^3].

A AIP mostra todas essas formas:

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

## O que a RÁDIO informa

O Art. 788 da ICA 100-37 lista os elementos básicos de informação que o órgão do AFIS proporciona às aeronaves[^1]:

1. **Informações meteorológicas** para o pouso e a decolagem, incluindo SIGMET: vento na superfície e suas variações significativas, ajuste de altímetro (QNH) arredondado para o hectopascal inteiro inferior, temperatura do ar, visibilidade ou RVR quando menor que 10 km, condições meteorológicas significativas nos setores de decolagem e de aproximação e, para o IFR, a quantidade e a altura da base da camada de nuvens mais baixa.
2. **Informações para o piloto escolher a pista**, além do vento: a pista e o circuito de tráfego usados por outras aeronaves e, quando o piloto pedir, o comprimento da pista ou a distância de uma interseção ao fim dela.
3. **Aeronaves, veículos ou pessoas conhecidos** na área de manobras ou perto dela, e aeronaves operando nas proximidades que possam constituir risco.
4. **Condições do aeródromo**: obras, partes irregulares ou danificadas das pistas, água na pista, aeronaves estacionadas, outros perigos ocasionais como aves, e avarias na iluminação.
5. **Mudanças no estado operacional de auxílios** visuais e não visuais, quando não constarem das publicações.
6. **Informações de VHF-DF**, quando o órgão tiver o equipamento.
7. **Mensagens, incluindo autorizações, recebidas de outros órgãos ATS** para retransmissão à aeronave.
8. **Outras informações** que possam contribuir para a segurança.

A ICA 100-37 lembra o limite do que a RÁDIO sabe: o órgão do AFIS "apenas divulga informações conhecidas, algumas vezes reportadas pelos próprios pilotos que estão operando na localidade ou próximos dela" (Art. 786, § 2°)[^1].

## O que a RÁDIO não presta

A ICA 100-37 é direta: na FIZ "não há prestação de Serviço de Controle de Tráfego Aéreo e, por isso, não devem ser esperadas autorizações de controle de tráfego aéreo" (Art. 786, § 1°)[^1].

| A RÁDIO faz | A RÁDIO não faz |
| --- | --- |
| Informa o vento, o ajuste de altímetro, a temperatura e as condições do aeródromo | Autoriza pouso, decolagem, toque e arremetida ou táxi |
| Informa a pista e o circuito que os outros tráfegos estão usando | Escolhe a pista do piloto |
| Informa o tráfego conhecido: tipo, posição, altitude e intenção | Separa tráfego ou sequencia chegadas |
| Pede reportes: perna do vento, final, no solo, pista livre | Dá proas, níveis ou velocidades |
| Retransmite autorizações de outro órgão, dizendo quem autorizou | Emite autorização própria |
| Aciona o Serviço de Alerta | Transfere controle: não há controle a transferir |

O elemento que mais confunde é a retransmissão (Art. 788, VII). A única autorização que passa pela frequência da RÁDIO é a de **outro** órgão, e a RÁDIO deixa claro de quem ela partiu. Nos exemplos do MCA 100-16, a RÁDIO diz "autorizado pelo Centro" antes da autorização (Art. 158)[^3].

!!! danger "Ciente, não autorizado"
    A resposta da RÁDIO a um reporte é **ciente**. "Autorizado pouso" ou "livre decolagem" na frequência da RÁDIO são erros: transmitem ao piloto uma autorização que ninguém tem autoridade para dar. Se o piloto pede autorização, a RÁDIO informa as condições e o tráfego conhecido, e a decisão fica com ele.

## A responsabilidade do piloto

Na FIZ, quem decide é o piloto. A ICA 100-37 dá a ele obrigações claras:

- **Escuta:** quem opera no espaço aéreo em que o AFIS é prestado mantém escuta na frequência do órgão (Art. 145)[^1].
- **Reportes:** na aproximação, no pouso, no movimento no solo e na saída, o piloto reporta à RÁDIO o procedimento IFR que vai executar e as fases e altitudes atingidas, a pista escolhida antes de entrar no circuito ou iniciar o táxi, as posições críticas no táxi e no circuito, as horas de pouso e decolagem e, na perna base ou na aproximação final IFR, o trem de pouso baixado e travado (Art. 791)[^1].
- **Escolha da pista:** espera-se que o piloto use a pista mais utilizada pelos outros tráfegos. Ele tem "autoridade final e responsabilidade pela operação segura da aeronave" e pode escolher outra pista, desde que reporte a intenção à RÁDIO antes de entrar no circuito ou iniciar o táxi (Art. 158)[^1].
- **Coordenação entre pilotos:** o piloto fica atento aos outros tráfegos VFR e IFR, informa suas intenções à RÁDIO e coordena suas manobras com os outros tráfegos, se for o caso (Art. 152)[^1].

Isso vale também para o IFR. Fora do espaço aéreo controlado, a aeronave IFR não recebe separação. A AIP deixa isso explícito para a FIZ Sorocaba, onde o procedimento IFR de SDCO fica todo em Classe G: as aeronaves que o executam "devem providenciar sua própria separação" em relação às demais aeronaves na FIZ[^2].

## O Serviço de Alerta

O Serviço de Alerta é prestado a toda aeronave que recebe Serviço de Controle de Tráfego Aéreo, que apresentou Plano de Voo e teve a decolagem notificada a um órgão ATS, ou que se sabe ou se suspeita estar sob interferência ilícita (Art. 795)[^1]. A responsabilidade de iniciar o serviço numa emergência é da "TWR, APP ou RDO (rádio) que tomar conhecimento de uma emergência em voo VFR ou IFR", que notifica imediatamente o ACC e o ARCC correspondentes (Art. 797)[^1].

Para a RÁDIO, isso significa acompanhar cada aeronave até o fim: quem reportou na final e não reportou no solo, ou quem decolou e não chamou o próximo órgão, é um caso para o Serviço de Alerta.

!!! note "Na rede"
    Na VATSIM não há ARCC. O equivalente prático é perguntar ao piloto, verificar se ele ainda está conectado e avisar o APP ou o centro que tem jurisdição em volta. Emergências na rede seguem o Código de Conduta: o piloto só declara emergência sob controle, e encerra a emergência se o controlador pedir[^4].

[^1]: [**ICA 100-37, Serviços de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/ica-100-37): Capítulo III, Seções XX e XXI (Arts. 140 a 164); Capítulo VIII, Seção V (AFIS, Arts. 782 a 791); Capítulo IX (Serviço de Alerta). Edição com a 2ª alteração (Portaria DECEA/DNOR1 nº 2.197, de 18/08/2026), em vigor em 26/11/2026.
[^2]: [**AIP-Brasil, ENR 2.2**](https://aisweb.decea.mil.br/?i=publicacoes&p=aip): tabela das FIZ, emenda de 01/10/2026.
[^3]: [**MCA 100-16, Fraseologia de Tráfego Aéreo**](https://publicacoes.decea.mil.br/publicacao/MCA-100-16): Seção VI, Serviço de Informação de Voo de Aeródromo – AFIS (Arts. 153 a 158). Edição com a alteração da Portaria DECEA/DNOR1 nº 2.193, de 11/08/2026, em vigor em 26/11/2026.
[^4]: [**VATSIM, Code of Conduct**](https://vatsim.net/docs/policy/code-of-conduct), item B6.
