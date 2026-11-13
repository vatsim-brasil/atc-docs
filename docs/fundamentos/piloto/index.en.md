---
  title: Your First Flight
  description: Step by step to flying on VATSIM with air traffic control in Brazil
  icon: material/airplane-takeoff
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

# Your First Flight

Flying on VATSIM means flying with real people: other pilots in the same sky and controllers who answer on the radio. You don't need any training to start, just to know the network rules and to prepare.

Follow the steps and tick each one when you finish. Your progress is saved in this browser.

<div class="vb-trilha" data-chave="piloto" markdown>

<div class="vb-passo" markdown>

### Create your VATSIM account

Registration is free, at [vatsim.net](https://vatsim.net). You get a **CID**, the number you will connect with.

- Use your **real name**, as the network requires.
- One account per person.

!!! info "Pilots don't need a transfer"
    To fly in Brazil, you don't need to be a VATSIM Brasil member. All airspace on the network is open to all pilots.

</div>

<div class="vb-passo" markdown>

### Learn the network rules

The [VATSIM Code of Conduct](https://vatsim.net/docs/policy/code-of-conduct) applies to everyone. The essentials for your first flight:

- **Connect at the gate or on the apron**, never on the runway or in the air.
- **Follow ATC instructions.** If you can't comply with one, say *"unable"* and explain.
- **Don't speed up simulator time** while connected.
- **With no ATC, monitor UNICOM** (122.800) and announce your intentions.
- **Never leave the aircraft unattended** in controlled airspace. If you need to leave, disconnect.
- **Be courteous** on frequency and in chat.

</div>

<div class="vb-passo" markdown>

### Install the pilot client

The client connects your simulator to the network and has built-in voice radio.

| Simulator | Client |
| --- | --- |
| Microsoft Flight Simulator, Prepar3D | [vPilot](https://vpilot.rosscarlson.dev) |
| X-Plane 11 and 12 | [xPilot](https://xpilot-project.org) |
| Several simulators | [swift](https://swift-project.org) |

Set up the client with your **CID** and password and choose a **callsign**: the airline code and flight number (`GLO1419`, `AZU4031`) or the aircraft registration (`PRABC`).

</div>

<div class="vb-passo" markdown>

### Choose your flight

For your first flight, prefer:

- a **short route** you know, 30 to 60 minutes;
- an **aircraft you have mastered**: this is not the time to try a new one;
- **aerodromes with ATC online**, for the full experience.

To see who is online, use a network map such as [VATSIM Radar](https://vatsim-radar.com). VATSIM Brasil events, announced at [vatsim.com.br](https://vatsim.com.br), guarantee ATC and traffic.

</div>

<div class="vb-passo" markdown>

### File your flight plan

Every IFR flight needs a flight plan. You can file it:

- through **myVATSIM**, at [my.vatsim.net](https://my.vatsim.net), before connecting;
- through **SimBrief**, which builds the plan and lets you send it to VATSIM;
- through the pilot client itself, after connecting.

Check the route, cruising level and aircraft type. The [Flight Plan Manual](../../documentos/manuais/manual-plano-de-voo/index.en.md) explains each field.

!!! tip "Not ready to talk?"
    Write `/T/` in the flight plan remarks (item 18, `RMK/`) to operate by text only, or `/R/` to receive by voice and reply by text. The controller will adapt.

</div>

<div class="vb-passo" markdown>

### Connect and listen before you talk

At the gate, with the simulator ready, connect the client.

1. **Tune the ATIS** of the aerodrome, if available, and note the information letter.
2. **Find out who is online** and who to call first: see [Who to talk to](orgaos.en.md).
3. **Listen to the frequency** for a few seconds before calling, so you don't interrupt anyone.
4. **Plan your message**, and only then press the transmit button.

</div>

<div class="vb-passo" markdown>

### Practise the phraseology

Before your first call, train with the radio simulator: it shows a complete departure from Brasília and hides your lines so you can practise.

[:octicons-arrow-right-24: On frequency](radio.en.md){ .md-button .md-button--primary }

</div>

<div class="vb-passo" markdown>

### Fly, land and disconnect at the gate

- Follow the sequence of ATC units: each controller gives you the next frequency.
- Read back clearances, levels, headings, frequencies and the squawk code.
- After landing, vacate the runway, call Ground (if online) and taxi to the gate.
- **Disconnect only at the gate**, with the aircraft stopped.

Then check that you learned the basics in the [pilot quiz](quiz.en.md).

</div>

</div>

## Still have questions?

??? question "Can I fly in Portuguese?"
    English is the network's standard language, and every controller will work you in English. Between a Brazilian pilot and a Brazilian controller, Portuguese can also be used. Choose the language on first contact and stick with it.

??? question "What if I make a mistake on frequency?"
    It happens to everyone. Ask the controller to repeat (*"say again"*) when you don't understand, and correct yourself when you get it wrong. The controller is there to help.

??? question "Do I need a payware aircraft or a specific simulator?"
    No. Any simulator with a compatible client and any aircraft will do. What matters is knowing how to operate the aircraft you choose.

??? question "I want to be a controller too. Where do I start?"
    With the [controller path](../controlador/index.en.md).
