---
title: Transferência de Controle
icon: material/transfer-right
---

--8<-- "includes/abreviacoes.md"

![Manual de Coordenação e Transferência - Transferência de Controle](img/manual-coordenacao-transferencia.png)

#

## Com vigilância ATS

Onde há vigilância ATS, a transferência de controle deve ser feita sempre que a aeronave passar de um órgão ou setor para outro que também a preste, **para que o serviço não seja interrompido**[^1]. A ICA 100-37 prevê duas formas de fazer isso.

### Transferência sem prévia coordenação

Quando o radar secundário ou o ADS-B mostram as aeronaves com etiquetas, a transferência entre posições ou órgãos adjacentes pode ser feita **sem prévia coordenação**, desde que[^2]:

1. o plano de voo atualizado da aeronave, inclusive o código transponder, seja comunicado ao aceitante **antes** da transferência;
2. a aeronave apareça na tela do aceitante antes da transferência e seja identificada, de preferência antes da chamada inicial;
3. os controladores tenham como falar entre si **instantaneamente**, a qualquer momento;
4. os pontos de transferência e as demais condições estejam fixados em instruções específicas ou numa carta de acordo operacional;
5. essas instruções prevejam que o aceitante pode encerrar esse tipo de transferência a qualquer momento, normalmente com coordenação prévia;
6. o aceitante seja informado de **qualquer instrução de nível, velocidade ou vetor** que modifique o progresso previsto do voo no ponto de transferência.

É o que a rede faz com a transferência pela etiqueta no EuroScope. O plano de voo e o código já circulam pela rede, a aeronave aparece na tela de quem vai recebê-la, e o chat está sempre disponível. A condição 6 é a que mais falha: **o que não está na etiqueta precisa ser dito**. Se você deu uma proa, uma velocidade ou um nível diferente do esperado no ponto de transferência, lance na etiqueta e, se não couber, avise pelo chat.

A separação entre aeronaves prestes a ser transferidas dessa forma deve levar em conta todas as circunstâncias técnicas e operacionais. Se as condições deixarem de ser atendidas, volte à transferência com coordenação até a situação se resolver[^3].

### Transferência com coordenação

Quando as condições acima não se aplicam, a transferência pode ser feita desde que[^4]:

1. a identificação tenha sido transferida ao aceitante, ou estabelecida diretamente por ele;
2. os controladores possam falar entre si instantaneamente;
3. a separação com os outros voos controlados atenda às mínimas previstas para a transferência entre aqueles setores ou órgãos;
4. o aceitante seja informado das instruções de nível, velocidade ou vetor aplicáveis no ponto de transferência;
5. **o transferidor mantenha a comunicação com a aeronave até o aceitante concordar** em assumir o Serviço de Vigilância ATS.

Depois disso, a aeronave é instruída a mudar de frequência, e a responsabilidade passa a ser do aceitante[^4].

### Transferir a identificação

A transferência de identificação só deve começar quando a aeronave já estiver dentro da cobertura de vigilância do aceitante[^5]. Na rede, a etiqueta correlacionada resolve isso. Sem ela, o transferidor pode indicar o código transponder, a posição em relação a um ponto que os dois vejam na tela, ou pedir ao piloto um `IDENT` ou uma mudança de código para o aceitante observar. Essas duas últimas formas exigem combinar antes, porque a indicação na tela é curta[^6].

### O aceitante confirma

Depois de identificar a aeronave, o aceitante informa ao transferidor que **completou o contato e mantém a identificação**. Se necessário, informa também a frequência e o código transponder[^7]. Sem vigilância, a regra é a mesma: o aceitante notifica que estabeleceu contato e assumiu o controle, salvo acordo em contrário[^8].

## Transferência de comunicações

| Situação | Quando mandar o piloto trocar de frequência |
| --- | --- |
| Separação com vigilância ATS | **Imediatamente depois** que o aceitante concordar em assumir o controle[^9] |
| Separação convencional | **5 minutos antes** da hora prevista no limite comum das áreas[^10] |

!!! warning "Nunca antes do aceite"
    Com vigilância, a troca de frequência vem **depois** do aceite, não antes. Um piloto que chama uma posição que ainda não aceitou a transferência fica numa frequência onde ninguém responde por ele. Se o aceite não vier, coordene pelo chat e, enquanto isso, mantenha a aeronave na sua frequência e longe do limite.

O aviso de que a aeronave foi instruída a chamar o aceitante só é exigido quando houver acordo entre os órgãos nesse sentido[^11].

## Passando para um órgão sem vigilância

Se o próximo setor ou órgão vai prestar **separação convencional**, você precisa entregar a aeronave já separada por esse método. Estabeleça a separação convencional **antes** que a aeronave chegue ao limite da sua área ou saia da cobertura de vigilância[^12]. Não basta estar a 5 NM do outro tráfego: o próximo controlador não vê a tela e precisa de níveis, tempos ou distâncias DME que consiga aplicar.

## Quem entrega a quem, e quando

### ACC e APP

| Fluxo | A transferência ocorre | Fonte |
| --- | --- | --- |
| Chegadas | Ao cruzar o limite lateral da TMA nos pontos de notificação, ao cruzar o limite vertical, ou num ponto acordado a partir do qual o APP possa assumir | [^13] |
| Saídas | Ao cruzar o limite lateral da TMA nos pontos de notificação, ao cruzar o limite vertical, ou num ponto acordado a partir do qual o ACC possa assumir | [^14] |
| Voos visuais chegando | Podem ser transferidos direto do ACC para a TWR, em coordenação com o APP | [^15] |

O APP pode emitir autorizações a qualquer aeronave que lhe tenha sido transferida pelo ACC, **sem notificá-lo**[^16].

### APP e TWR

| Fluxo | A transferência ocorre | Fonte |
| --- | --- | --- |
| Chegadas | Quando a aeronave estiver nas vizinhanças do aeródromo e a aproximação e o pouso puderem ser completados com referência visual, ou quando tiver pousado | [^17] |
| Saídas | Imediatamente após a decolagem, ou antes de a aeronave entrar em condições de voo por instrumentos | [^18] |

O APP mantém o controle das chegadas **até que sejam transferidas e estejam em comunicação com a TWR**[^19]. Com vigilância, ele continua responsável pela separação entre aeronaves sucessivas na final, a menos que o procedimento local transfira essa responsabilidade à torre[^20]. Mande a aeronave para a torre num ponto em que a autorização de pouso ainda possa ser dada a tempo[^21]. Veja também [Sequenciamento, Na final](../vetoracao-sequenciamento/04-sequenciamento.pt.md#na-final).

### TWR e solo

| Fluxo | A transferência ocorre | Fonte |
| --- | --- | --- |
| Chegadas | Depois que a torre passa a hora de pouso e a autorização para livrar a pista e trocar para o solo, ou em outra posição combinada na área de manobras. O piloto só troca de frequência depois de livrar a pista | [^22] |
| Saídas | Na posição 2 (ponto de espera), ou em outra posição combinada na área de manobras | [^23] |

## No EuroScope

| Ação | Como |
| --- | --- |
| Iniciar a transferência | `F4` sobre a etiqueta e escolha do próximo controlador |
| Aceitar uma transferência | `F3` sobre a etiqueta |
| Rejeitar uma transferência recebida | `F4` sobre a etiqueta |
| Avisar um vizinho sem transferir (*point out*) | `F1 + P` (`.point`) com o identificador do controlador |
| Registrar nível, proa e velocidade | Campos da etiqueta, ou `F8` para o nível |

A rotina de cada transferência:

1. **Antes do limite**, confira se o que está na etiqueta é o que você autorizou.
2. **Transfira** com `F4`, com antecedência suficiente para o aceitante analisar.
3. **Espere o aceite.** Sem resposta, chame pelo chat.
4. **Mande o piloto trocar** de frequência só depois do aceite.
5. Se o aceitante pedir uma modificação, **aplique-a antes** de entregar o tráfego.

Veja os atalhos completos em [Comandos do EuroScope](../../../fundamentos/softwares/euroscope/comandos.pt.md).

[^1]: **ICA 100-37, Art. 969**. Ver [ICA 100-37](https://publicacoes.decea.mil.br/publicacao/ica-100-37).
[^2]: **ICA 100-37, Art. 970**.
[^3]: **ICA 100-37, Art. 971 e parágrafo único**.
[^4]: **ICA 100-37, Art. 972 e parágrafo único**.
[^5]: **ICA 100-37, Art. 915**.
[^6]: **ICA 100-37, Art. 916, incisos II, VI, VII e VIII, e § 5°**.
[^7]: **ICA 100-37, Art. 974 e parágrafo único**.
[^8]: **ICA 100-37, Art. 835**.
[^9]: **ICA 100-37, Art. 833**.
[^10]: **ICA 100-37, Art. 832**.
[^11]: **ICA 100-37, Art. 834**.
[^12]: **ICA 100-37, Arts. 939 e 947**.
[^13]: **ICA 100-37, Art. 839**.
[^14]: **ICA 100-37, Art. 840**.
[^15]: **ICA 100-37, Art. 839, parágrafo único**.
[^16]: **ICA 100-37, Art. 838, inciso I**.
[^17]: **ICA 100-37, Art. 848**.
[^18]: **ICA 100-37, Art. 849**.
[^19]: **ICA 100-37, Art. 844**.
[^20]: **ICA 100-37, Art. 1005**.
[^21]: **ICA 100-37, Art. 1007**.
[^22]: **ICA 100-37, Art. 853 e parágrafo único**.
[^23]: **ICA 100-37, Art. 854**.
