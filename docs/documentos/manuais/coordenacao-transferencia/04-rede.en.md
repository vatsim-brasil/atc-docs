---
title: Coordination on the Network
icon: material/lan-connect
---

--8<-- "includes/abreviacoes.md"

# Coordination on the Network

## What changes on VATSIM

In the real world, each unit operates during its published hours and there is always someone on the other side of the boundary. On the network, positions open and close as controllers connect. The neighbour you were coordinating with an hour ago may have left, and their airspace may have passed to another controller, or to no one. Three rules cover this difference: top-down coverage, the handover when opening and closing positions, and the handling of unstaffed airspace.

## Top-down coverage

The GCAP establishes that VATSIM positions **cover the airspace and positions below them when those are not staffed**. This is the top-down principle[^1]. It applies to positions that provide a control service[^2].

| Position online | Covers, if they are disconnected |
| --- | --- |
| `TWR` | `GND` and `DEL` of the same aerodrome |
| `APP` | `TWR`, `GND` and `DEL` of the aerodromes in the TMA |
| `CTR` | `APP`, `TWR`, `GND` and `DEL` under the sector |

Where coverage is ambiguous, such as in shared or overlapping airspace, the division or subdivision decides which positions are "below" which[^3]. At Vatsim Brasil, the coverage order of each TMA is in the [Terminals](../../../MOP/terminais/index.en.md) section, in the "Top-down coverage" diagram on each page.

Covering a position means providing its service. An `APP` covering a tower gives the clearance, the taxi and the landing and take-off clearances for that aerodrome, as well as its own approach work. The pilot calls the position that is online, on its frequency.

!!! info "Reduced service"
    An overloaded controller may provide a reduced service, for example by **withdrawing top-down coverage from an aerodrome**. In that case, the GCAP recommends considering whether it would be better to connect to a smaller position or a split sector[^4]. If you withdraw coverage, tell the affected pilots and the neighbouring controllers.

### Positions that require an endorsement

While a controller with the required endorsement is on the position below or adjacent, the controller above does not need that endorsement. If that controller leaves, the controller above **must disconnect immediately** if they do not hold the endorsement[^5]. One example is the Atlântico FIR, whose MOP covers this in [Preparing and Opening the Position](../../../MOP/oceanico/atc/abertura.en.md).

## Opening a position

When you open a position, someone was probably covering that airspace top-down. The handover is a coordination like any other:

1. **See who is online** above, below and beside your position.
2. **Agree with whoever was covering** the moment you take over. Ask about traffic with restrictions, holds, emergencies or pending coordination.
3. **Receive the traffic** in your airspace through the tag transfer. Whoever was covering transfers with `F4`, you accept with `F3`, and only then do the pilots change to your frequency.
4. **Coordinate the transfer points with the adjacent positions**, if they differ from the operations manual's standard.

If you drop and come back within a reasonable time, the controller who took over your position in the meantime should give it back[^6].

## Closing a position

Closing is opening in reverse, with one difference: the pilots will lose the frequency they are on.

!!! danger "Do not disconnect with assumed traffic"
    Before leaving, **transfer each aircraft** to whoever will cover your airspace, or terminate the service of each one and tell it where to call. Disconnecting with assumed tags leaves aircraft with no one responsible for them, which is exactly what coordination exists to prevent.

!!! note "Good practice"
    1. Tell your neighbours a few minutes before closing, so they can prepare to receive the traffic.
    2. Stop accepting new traffic if the position above can receive it directly.
    3. Transfer the traffic one by one, with the correct frequency of whoever will cover.
    4. Only disconnect once there are no more tags assumed by you.

## Unstaffed airspace

There is not always someone to receive the aircraft. When the next airspace has no controller, either directly or top-down, there is no one to coordinate with:

- **Aircraft leaving your airspace for unstaffed airspace:** terminate the service and tell the pilot to monitor the designated advisory frequency (UNICOM). VATSIM requires pilots in unstaffed airspace to monitor that frequency until they are covered again[^7].
- **Aircraft entering your airspace from unstaffed airspace:** it arrives without coordination. Identify it, confirm route and level, and give the clearance as if it were the initial call of a flight in your airspace.

## Coordination tools

| Tool | Use for |
| --- | --- |
| Tag transfer (`F4` / `F3`) | Routine transfer, without prior coordination. See [Transfer of Control](02-transferencia.en.md#in-euroscope) |
| *Point out* (`F1 + P`) | Alerting a neighbour to traffic passing near the boundary without entering their airspace |
| Private chat (`.chat` + controller callsign) | Estimates, level requests, releases, flight plan changes, everything the tag does not show |
| `ATC` channel | Notices for all controllers, such as opening and closing a position |
| Voice channel agreed between the controllers | Long or urgent coordination, when available |

!!! tip "Short messages"
    Write in the chat as if you were speaking on the coordination line: callsign, point, time and level, in that order. "VRG2320 EST VARGA 55 FL330" is enough. The templates are in the [Phraseology](05-fraseologia.en.md#messages-between-units).

[^1]: **VATSIM, GCAP, item 4.6**. See [GCAP](https://cdn.vatsim.net/policy-documents/GCAP%20v2.0%20Release%2008152026r1.pdf).
[^2]: **VATSIM, GCAP, item 4.6(a)**.
[^3]: **VATSIM, GCAP, item 4.6(b)**.
[^4]: **VATSIM, GCAP, item 4.6(d)**.
[^5]: **VATSIM, GCAP, item 6.1(a)**.
[^6]: **VATSIM, Code of Conduct, item C5**. See [Code of Conduct](https://vatsim.net/docs/policy/code-of-conduct).
[^7]: **VATSIM, Code of Conduct, item B5**.
