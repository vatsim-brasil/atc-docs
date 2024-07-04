---
  title: FIR Atlântico
  hide:
    - navigation
---

--8<-- "includes/abreviacoes.md"

## Apresentação

A FIR Atlântico abrange toda a região do Atlântico Sul, cobrindo quase 11 milhões de quilômetros quadrados. O órgão responsável por prover serviço de controle de tráfego aéreo e serviço de informação e alerta para voos transitando por essa região é o ACC Atlântico (`SBAO_CTR`). A FIR não dispõe de radar, seja ele primário ou secundário, sendo o monitoramento primariamente efetuado basicamente por reportes de posição nos fixos de notificação compulsória ou nas posições definidas por latitude e longitude. Outro sistema, chamado de Vigilância Automática Dependente – Contrato[^1], é utilizado para monitoramento das aeronaves.

[^1]:Tradução de *Automatic Dependent Surveillance - Contract*, ou ADS-C.

As comunicações entre as aeronaves e o ACC Atlântico são efetuados ou por rádio, utilizando frequências na banda HF (*High Frequency*, Frequência Alta), ou por enlace de dados, através de ferramentas próprias a bordo das aeronaves.

A FIR é dividida em dois setores: um mais ao norte, cobrindo os tráfegos que transitam entre o Brasil e a Europa ou norte da África, e um mais ao sul, cobrindo os tráfegos transitando entre o Brasil e a África Meridional.

Diante da ausência de cobertura radar e da falta de uma comunicação mais acessível e clara entre pilotos e controladores, a dinâmica de controle do ACC Atlântico é diferente se comparada em relação às outras FIR do País, todas com cobertura radar e VHF (*Very High Frequency*, ou Frequência Muito Alta). Além disso, outras rotinas específicas ao controle de regiões oceânicas[^2], como uso de SELCAL (*Selective Call*, Chamada Seletiva), domínio procedimentos alternativos de separação e gestão organizada das informações enviadas pelos pilotos são aplicadas ativamente durante o controle.

[^2]:Pelas regras da Organização da Aviação Civil Internacional (OACI), o disposto para controles oceânicos também pode ser aplicado em FIRs continentais remotas por possuírem as mesmas características de controles em áreas oceânicas: ausência de cobertura radar e dificuldades de comunicação VHF.

## Estruturação

O ACC Atlântico é a estação primária de controle, sendo responsável por todo o espaço aéreo da FIR[^3], seja provendo o serviço de controle de tráfego aéreo ou o serviço de informação e alerta, quando oportuno.

[^3]:MSL-UNL dentro do limite lateral.

Seguem algumas informações referentes ao ACC, aplicáveis à Vatsim:

- **Código de Conexão:** SBAO_FSS
- **Frequência:** 134.500 MHz (emulando a frequência 13450 kHz)
- **Qualificação Mínima:** Aprovação no Curso de Controle do Atlântico (CCA).

### Setorizações

Atualmente, a FIR é dividida em dois setores: Setor Norte e Setor Sul.

#### Setor Norte

É responsável pelo corredor EURSAM[^4], além das porções que estejam fora da AORRA[^5]. Controla especialmente os tráfegos voando entre o Brasil e a Europa ou Norte da África, além dos tráfegos cruzando o espaço aéreo voando entre o Caribe e a África Meridional.

[^4]:Corredor Europa-América do Sul. Maiores detalhes na seção EURSAM.
[^5]:Área de Rotas Aleatórias do Atlântico Sul. Maiores detalhes na seção AORRA.

- **Código de Conexão:** SBAO_N_FSS
- **Frequência:** 133.575 MHz (emulando a frequência 13350 kHz)
- **Qualificação Mínima:** Aprovação no Curso de Controle do Atlântico (CCA).

#### Setor Sul

É responsável exclusivamente pela AORRA, prestando controle para os tráfegos que cruzam o Atlântico Sul entre a América ou o Caribe e a África Meridional. Controla também voos entre a Ilha de Ascensão e as Ilhas Falklands (Malvinas), geralmente operados pela Força Aérea Real do Reino Unido (*Royal Air Force*).

- **Código de Conexão:** SBAO_S_FSS
- **Frequência:** 133.150 MHz (emulando a frequência 13315 kHz)
- **Qualificação Mínima:** Aprovação no Curso de Controle do Atlântico (CCA).

### FIRs Adjacentes

Ao longo do seu limite lateral, a FIR Atlântico é adjacente a outras 8 (oito) FIRs, a saber: Dacar Oceânico (GOOO), Luanda (FNAN), Joanesburgo Oceânico (FAJO), Montevidéu (SUEO), Curitiba (SBCW), Recife (SBRE), Amazônica (SBAZ) e Caiena (SOOO).

### Aeródromos

Há apenas um aeródromo localizado dentro dos limites laterais da FIR: a Base Aérea de Wideawake (FHAW/ASI), localizada na Ilha da Ascensão, a 865 nm da costa da África e 1215 nm da costa do Brasil.

A ilha é um Território Ultramarino Britânico, junto com Santa Helena (com um aeródromo dentro da FIR Luanda[^6], 695 nm a sudeste, e Tristão da Cunha (não há aeródromos), 2000 nm ao sul.

[^6]:Aeroporto Internacional de Santa Helena (FHSH/HLE). Inaugurado em 2016. Conta com um voo semanal com Joanesburgo, África do Sul, operado com o Embraer 190.

## Corredor EURSAM

## AORRA

A Área de Rotas RNAV Aleatórias do Oceano Atlântico[^7] é um volume de espaço aéreo entre o FL290 e o FL410, inclusive, 
The  is the volume of airspace between FL290 and FL410 inclusive within the Atlântico, Accra, Comodoro Rivadavia, Dakar, Dakar Oceanic, Ezeiza, Johannesburg Oceanic, Luanda and Montevideo FIRs. (See Enroute Chart).

[^7]:Atlantic Ocean Random Routing RNAV Area (AORRA).

Flights operating within the AORRA shall enter and exit AORRA via charted gates.

In cases where there is no fixed route structure, Standard Instrument Arrival (STAR) or Standard Instrument Departure (SID), soon after entering/leaving the AORRA that supports the origin/destination of a specific flight, aircraft may enter/leave the AORRA out of the gates established above.

Aircraft may indicate, by flight plan, the preferred trajectories between these gates. Before entering or after leaving AORRA by a certain gate, aircraft must:

- Comply with the structure of the ATS route associated to a certain entry or exit point; or
- When entering the Atlântico FIR, towards AORRA, via the ARUSI or UKEDI fix: indicate in the flight plan a trajectory composed of waypoints existing in the Brazilian airspace, following the flight level rules provided below. In this case, exceptionally, the ADS-C/CPDLC capability is mandatory, meeting the requirements set out below. The same applies to flights in the opposite direction.

ADS-C/CPDLC will be used within AORRA airspace by ACC Atlântico as the primary means of providing route compliance monitoring and communication for aircraft equipped with FANS 1/A data link systems, while HF communications will be employed as a secondary means.

No aircraft shall flight plan to operate in the AORRA airspace unless it is RNP10 certified to operate in this airspace by the State of Registry or the State of operator as the case may be, except in limited circumstances.