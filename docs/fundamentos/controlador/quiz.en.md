---
  title: Controller Quiz
  description: Quick questions to check the basic concepts before the S1 course
  icon: material/head-question-outline
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Controller Quiz

Ten questions about what you saw on the path. There is no score: it is for you to find out what to review before the S1 course.

<div class="vb-quiz" markdown>

<div class="vb-pergunta" data-resposta="2" markdown>

You have just created your VATSIM account. What is your rating?

1. S1
2. OBS
3. None, until you take the exam

<div class="vb-explica" markdown>
Every account starts as **OBS** (observer): you can connect with an `_OBS` callsign to watch and listen, without transmitting. See the [rating ladder](ratings.en.md).
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Which positions does the S1 rating unlock?

1. Only `_DEL`
2. `_DEL`, `_GND` and `_TWR`
3. `_DEL` and `_GND`

<div class="vb-explica" markdown>
S1 unlocks **Delivery** and **Ground**. Tower requires S2.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Who issues the ATC clearance (route, level, departure and squawk code) when every position at the aerodrome is staffed?

1. Delivery (`_DEL`)
2. Ground (`_GND`)
3. Tower (`_TWR`)

<div class="vb-explica" markdown>
The clearance is **Delivery**'s job. Without it online, the clearance passes to the next position above, by top-down.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

Only `SBXP_APP` (São Paulo Control) is online. A pilot at Guarulhos wants an ATC clearance. Who handles it?

1. No one: without Delivery online, the pilot departs without a clearance
2. The pilot must wait for Delivery to connect
3. `SBXP_APP` itself, through top-down coverage

<div class="vb-explica" markdown>
Under **top-down coverage**, the online position covers the empty positions below it. APP acts as Tower, Ground and Delivery at the aerodromes it covers. See [Positions and units](posicoes.en.md#what-if-the-position-is-empty).
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

Which position clears the aircraft to enter the runway and take off?

1. Ground
2. Tower
3. Control

<div class="vb-explica" markdown>
**Tower** owns the runway. Ground takes the aircraft to the holding point, and Tower clears it to line up and take off.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

What is the Portuguese callsign of the `_APP` position?

1. Controle
2. Aproximação
3. Centro

<div class="vb-explica" markdown>
In Brazil, APP is called **Controle** (Control): *Controle São Paulo*, *Controle Brasília*. **Centro** (Center) is `_CTR`.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

What is the ATIS for?

1. For the controller to talk to other controllers
2. For the pilot to send the flight plan
3. To give the runway in use, wind, weather conditions and aerodrome notices

<div class="vb-explica" markdown>
The **ATIS** is a continuous recording with the aerodrome information. The pilot listens to it before the first call and reports the letter received. The controller maintains it with [vATIS](../softwares/vatis/index.en.md).
</div>

</div>

<div class="vb-pergunta" data-resposta="2" markdown>

You are about to close your session and no one is online above you. What do you tell the pilots on your frequency?

1. Nothing: they will notice when you disconnect
2. That the service is closing and they should monitor UNICOM, 122.800
3. To stand by on the frequency until another controller connects

<div class="vb-explica" markdown>
With no ATC online, pilots use the network's traffic frequency, **UNICOM 122.800**. Tell each one before you disconnect.
</div>

</div>

<div class="vb-pergunta" data-resposta="1" markdown>

Which of these requirements applies to S3 but not to S1?

1. Minimum hours connected on `_TWR` and as *solo trainee* on `_APP`
2. Passing a theory exam
3. Training with a mentor

<div class="vb-explica" markdown>
The theory exam and mentor apply to every rating. S3 adds **10 hours** on `_TWR` as S2 and **10 hours** of *solo trainee* time on `_APP`, plus the practical *check*.
</div>

</div>

<div class="vb-pergunta" data-resposta="3" markdown>

The pilot read back the wrong squawk code. What do you do?

1. Nothing, EuroScope corrects it automatically
2. Wait until they take off and let Control correct it
3. Correct it right away and ask for a new readback

<div class="vb-explica" markdown>
The readback is there precisely to catch errors. Correct it immediately: *"Negative, squawk FOUR ZERO THREE FIVE"*, and confirm they read it back correctly.
</div>

</div>

</div>

Want to see the other side of the frequency? Try the [pilot radio simulator](../piloto/radio.en.md) in *Practice as controller* mode.
