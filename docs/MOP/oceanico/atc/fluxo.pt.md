---
title: Fluxo Operacional e Reportes
icon: material/airplane
tags:
  - Centro
  - SBAO
---

--8<-- "includes/abreviacoes.md"

O que acontece com uma aeronave da entrada à transferência, e como manter o registro que substitui a tela de radar.

## Entrada por transferência

É o caso normal: o órgão anterior está online e coordena a entrega.

### O que a coordenação precisa trazer

| Elemento               | Para quê                              |
| ---------------------- | ------------------------------------- |
| Identificação          | Base do registro                      |
| Ponto de entrada       | Por onde cruza o limite               |
| **Estimado sobre o ponto** | Base do cálculo de separação      |
| Nível                  | Separação vertical                    |
| **Número Mach**        | Técnica do número Mach                |
| Rota após a entrada    | Pontos seguintes e adjacente de saída |
| Capacidades            | RVSM, RNP 10, ADS-C, CPDLC e SELCAL   |
| Meio de comunicação    | Por onde a aeronave está sendo tratada |

### Fluxo

1. **Confira** cada elemento da tabela acima.
2. **Analise o plano de voo** conforme [Plano de voo e capacidades](plano-de-voo.pt.md).
3. **Procure conflito** com quem já está na FIR, **antes** de aceitar.
4. **Aceite ou renegocie.** Não poder aceitar nas condições propostas é normal: peça outro nível, outro Mach ou outro horário sobre o ponto de entrada[^1].
5. **Confirme o enlace.** Vindo de FIR com enlace, a conexão passa sozinha; se não passou, o piloto refaz o logon com `SBAO`[^2].
6. **Estabeleça a comunicação** e confirme identificação, posição, hora, nível e Mach.
7. **Abra o registro** com o estimado do próximo ponto.

!!! warning "Não aceite sem coordenação completa"
    Uma aeronave não deve adentrar espaço aéreo de outro órgão sem coordenação concluída[^3]. Quem cruza a fronteira sem isso fica, por alguns minutos, sob responsabilidade de ninguém.

## Entrada sem ATC online

O caso mais frequente na rede: a aeronave voou horas sem nenhum órgão conectado e não existe registro.

1. **Identifique** pelo indicativo e pelo plano arquivado.
2. **Não presuma nada** a partir do plano de voo.
3. **Peça um reporte de posição completo.**
4. **Confirme** rota, nível e Mach que ela está realmente cumprindo.
5. **Confirme as capacidades** e peça o logon, se aplicável.
6. **Avalie conflitos** agora com dados reais.
7. **Estabeleça o serviço**: identifique o órgão, confirme nível e Mach a manter e defina o próximo ponto de reporte.

!!! tip "Na rede (Vatbrz)"
    Ao abrir a posição, faça isso com **todas** as aeronaves já dentro da FIR, uma a uma, antes de emitir qualquer autorização.

## Reportes de posição

O reporte é o que substitui a tela. A responsabilidade de confeccionar e transmitir é do piloto[^4].

### Formato

```text
CALLSIGN, POSITION, TIME, LEVEL, MACH, NEXT POSITION and ESTIMATE, ENSUING POSITION
```

Os seis elementos normativos são identificação, posição, hora, nível (incluindo o que está cruzando e o autorizado, se diferentes), próxima posição com hora, e ponto significativo seguinte[^5]. **O número Mach entra sempre que tiver sido atribuído**[^6].

!!! example "Exemplo"
    Indicativo e fixos fictícios.

    *"Atlantico Center, EXEMPLO 123, position NIMAX at 1412, flight level 370, Mach decimal 82, estimating KOSAX at 1448, next TEBRO."*

    Registre: `NIMAX` às `1412`, FL 370, Mach 0.82, `KOSAX` às `1448`, depois `TEBRO`. O estimado de `1448` passa a ser a base de separação com quem mais cruzar `KOSAX`.

### Quando é exigido

| Situação                                                                    |
| ---------------------------------------------------------------------------- |
| Sobre os pontos de notificação compulsória, ou logo após passá-los[^7]      |
| No cruzamento dos limites laterais da FIR[^7]                               |
| Por solicitação do órgão ATS[^7]                                            |
| Em rota sem pontos compulsórios: após os primeiros 30 minutos, depois de hora em hora[^7] |
| Na entrada da FIR, por CPDLC, mesmo em ADS-C[^8]                            |
| Na AORRA, a cada 10° de longitude[^9]                                       |

### Quando é dispensado

Com ADS-C ativa e funcionando, o reporte por voz não é necessário, salvo solicitação[^10]. **A dispensa vale enquanto o dado chega:** no instante em que a ADS-C falha, os reportes voltam a ser exigidos e cabe a você informar isso ao piloto[^11].

!!! info "Vento e temperatura não fazem parte"
    Eles aparecem no bloco meteorológico de um informe ADS-C e em um AIREP Especial, não no reporte de posição de rotina. Não peça.

### Estimados

Uma **revisão superior a 2 minutos** exige ação[^12]. Ao recebê-la, recalcule imediatamente todos os pares que dependiam do estimado anterior.

!!! example "Exemplo"
    `EXEMPLO 123` havia informado `KOSAX` às `1448` e agora informa `1455`. São 7 minutos. Se havia outra aeronave planejada para `KOSAX` às `1500` com 10 minutos de separação, a mínima foi comprometida e exige ação imediata.

### Reporte que não chegou

O controle **não** deve ser baseado no pressuposto de que o estimado foi cumprido. Tome ação imediata para obter o reporte se houver qualquer influência sobre outra aeronave[^13].

1. Marque a hora em que o reporte era esperado.
2. Chame a aeronave; sem resposta, tente SELCAL e os demais meios.
3. **Trate a aeronave como podendo estar em qualquer ponto** entre o último reporte confirmado e a posição projetada, e afaste os demais tráfegos dessa faixa.
4. Solicite contrato ADS-C por demanda ou mensagem CPDLC.
5. Avise o adjacente de que o estimado está incerto.

## Registro da progressão

Mantenha, por aeronave:

- [ ] último ponto reportado, com hora exata;
- [ ] nível atual e nível autorizado, se diferentes;
- [ ] número Mach atribuído;
- [ ] próximo ponto e estimado vigente;
- [ ] ponto subsequente;
- [ ] meio de comunicação e capacidades confirmadas.

!!! tip "Na rede (Vatbrz)"
    Use os campos de tag e as listas do perfil distribuído no pacote de setor. O que está na tela sobrevive a uma reconexão; o que está no papel não.

## Saída da FIR

1. **Calcule o estimado** do ponto de transferência e revise-o quando o quadro mudar.
2. **Coordene** com antecedência suficiente para a análise do adjacente[^14].
3. **Aguarde a aceitação**, ajustando antes da fronteira se ele indicar outras condições[^1].
4. **Instrua a aeronave** com `CONTACT` ou `MONITOR`, conforme o caso[^15].
5. **Trate o enlace**: transferência automática se o próximo órgão também usa, senão encerre a conexão[^2].
6. **Encerre o registro** com a hora sobre o ponto de transferência.

### Quando o próximo órgão não está online

1. Informe ao piloto que não há órgão ATS conectado à frente.
2. Oriente-o a tentar contato com o órgão seguinte com pelo menos 5 minutos de antecedência do estimado sobre o fixo, transmitindo identificação, procedência, destino, rota, nível, código transponder, estado RVSM e estimado[^16].
3. Registre a última posição, nível e Mach.
4. **Encerre o serviço de forma explícita.** O piloto precisa saber que deixou de ter órgão responsável.

[^1]: **ICA 100-37, Art. 825**.
[^2]: **AIP-Brasil, ENR 3.5, item 9.2.3**.
[^3]: **ICA 100-37, Art. 822**.
[^4]: **ICA 100-37, Arts. 171 e 172**.
[^5]: **ICA 100-37, Art. 178**.
[^6]: **ICA 100-37, Art. 180**.
[^7]: **ICA 100-37, Art. 173**.
[^8]: **AIP-Brasil, ENR 3.5, item 9.5.2.1**.
[^9]: **AIP-Brasil, ENR 3.5, item 8.8.2**.
[^10]: **ICA 100-37, Art. 179**, e **AIP-Brasil, ENR 3.5, item 9.5.2.2**.
[^11]: **AIP-Brasil, ENR 3.5, item 9.5.2.6.2**.
[^12]: **AIP-Brasil, ENR 3.5, item 9.5.2.5**.
[^13]: **ICA 100-37, Art. 174**.
[^14]: **ICA 100-37, Art. 824**.
[^15]: **AIP-Brasil, ENR 3.5, itens 9.4.1.5 e 9.4.1.6**.
[^16]: **AIP-Brasil, ENR 1.8, item 2.3.3.1.2**.
