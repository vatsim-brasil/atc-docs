---
title: Quick Checklist
icon: material/checkbox-marked-circle-outline
---

--8<-- "includes/abreviacoes.md"

# Quick Checklist

## Before connecting

- [ ] I know which FIR, TMA, CTR or ATZ my position operates in
- [ ] I know the class of the airspace under my responsibility
- [ ] I know who is online above and below me
- [ ] I have confirmed the aerodrome's **transition altitude** on the chart (IAC or SID) — it is the reference for the **climb**
- [ ] I have determined the **transition level** with the current QNH — it is the reference for the **descent**
- [ ] I have read the local instructions in the [Operational Manuals](../../../MOP/aerodromos/index.en.md) section

## I am in this class — what do I owe?

Table derived from the class matrix in Art. 21 of ICA 100-37 and from Annex II, both already reproduced in the [Airspace Classes chapter](02-classes.en.md#tabela-consolidada-anexo-ii-da-ica-100-37).

| Class | Flights permitted | ATC clearance required | Radiocommunication required | Whom I separate | Information I provide |
| --- | --- | --- | --- | --- | --- |
| **A** | IFR only | Yes | Continuous two-way | All flights from each other | Not applicable — separation already covers all traffic |
| **B** | IFR and VFR | Yes, from IFR and VFR | Continuous two-way, from IFR and VFR | All flights from each other — IFR from IFR, IFR from VFR and VFR from VFR | Not applicable — separation already covers all traffic |
| **C** | IFR and VFR | Yes, from IFR and VFR | Continuous two-way, from IFR and VFR | IFR from IFR and from VFR — I do not separate VFR from VFR | VFR receives traffic information on other VFR, and traffic avoidance advice if requested by the pilot |
| **D** | IFR and VFR | Yes, from IFR and VFR | Continuous two-way, from IFR and VFR | Only IFR from IFR — VFR is not separated from anything | IFR receives traffic information on VFR flights; VFR, on all other flights. In both cases, traffic avoidance advice if requested by the pilot |
| **E** | IFR and VFR | Yes from IFR; **not** from VFR | Continuous two-way from IFR; **not** required from VFR | Only IFR from IFR — VFR is not separated | Everyone receives traffic information when possible; VFR also receives Flight Information Service |
| **F** | IFR and VFR | No, from neither | Continuous two-way from IFR; **not** required from VFR | IFR from IFR, when possible — this is advisory, not full separation | Flight Information Service: to IFR without waiting to be asked; to VFR, when requested* |
| **G** | IFR and VFR | No, from neither | Continuous two-way from IFR; **not** required from VFR | Not applicable — no separation | Flight Information Service, when possible and requested by the pilot |

The "ATC clearance required" and "Radiocommunication required" columns reproduce the last two columns of Annex II to ICA 100-37, condensing the IFR and VFR rows of each class into one. Where the two rows differ — in radiocommunication in Classes E, F and G, and in ATC clearance only in Class E —, the difference is spelled out in the cell. See the reading notes in the [Airspace Classes chapter](02-classes.en.md#tabela-consolidada-anexo-ii-da-ica-100-37), especially the one about the **D / VFR** row.

\* In Class F an IFR flight is required to maintain continuous two-way communication, and therefore receives Flight Information Service under item I of Art. 741 of ICA 100-37, **without having to request it**. A VFR flight has no such obligation and receives it under item II, on request. Art. 21, VI, *c*, of the same Instruction guarantees the floor: any flight in the class that requests it receives it. See the [Airspace Classes chapter, Class F section](02-classes.en.md#classe-f).

## Pocket VMC minima

Condensed version of Table 1 of Art. 104 of ICA 100-12, reproduced in the [Flight Rules and Levels chapter](05-regras.en.md#minimos-vmc).

| Altitude | Classes | Flight visibility | Distance from cloud |
| --- | --- | --- | --- |
| At or above 3,050 m (10,000 ft) AMSL | B, C, D, E, F, G | 8 km | 1,500 m horizontal / 300 m (1,000 ft) vertical |
| Below 3,050 m (10,000 ft) and above 900 m (3,000 ft) AMSL, or above 300 m (1,000 ft) above terrain — whichever is higher | B, C, D, E, F, G | 5 km | 1,500 m horizontal / 300 m (1,000 ft) vertical |
| At or below 900 m (3,000 ft) AMSL, or 300 m (1,000 ft) above terrain — whichever is higher | B, C, D, E | 5 km | 1,500 m horizontal / 300 m (1,000 ft) vertical |
| Same band as above | F, G | 5 km | Clear of cloud and in sight of the surface |

Class A does not appear in this table: it only admits IFR flights, so there is no VMC minimum to meet there. When the aerodrome's transition altitude is below 3,050 m (10,000 ft) AMSL, use FL 100 instead of 10,000 ft as the reference for the first band.

## Which unit does what

Condensed version of the correspondence table in the [ATS Units and Positions chapter](04-orgaos.en.md#tabela-de-correspondencia).

| ATS unit | Internal position | Network position | Typical airspace |
| --- | --- | --- | --- |
| Area Control Center (ACC) | — | `_CTR` | CTA, UTA and other portions of the FIR |
| Approach Control (APP) | — | `_APP` | TMA and Control Zone* |
| Aerodrome Control Tower (TWR) | Tower Control | `_TWR` | ATZ and Control Zone* |
| Aerodrome Control Tower (TWR) | Ground Control | `_GND` | Maneuvering area |
| Aerodrome Control Tower (TWR) | Clearance Delivery | `_DEL` | Apron |
| ATS unit identified as "RÁDIO" (AFIS) | — | `_R_TWR` | FIZ, or Class G in the vicinity of the aerodrome |

\* The Control Zone appears in two rows because jurisdiction over it **varies by location**: at one aerodrome it belongs to APP, at another to TWR, according to the delegation provided for in Art. 34 of ICA 100-37. In each specific CTR it belongs to only one of the two, as required by Art. 37 of the same Instruction. Which one, at that aerodrome, is in the AIP-Brasil and in the [**Operational Manuals**](../../../MOP/aerodromos/index.en.md) section.

Rows 3 to 5 are internal positions of a single unit — the TWR —, not three different units. The RÁDIO position **does not provide control**: it provides Flight Information Service and Alerting Service, and no control clearances are issued there. The `_CTR`, `_APP`, `_TWR`, `_GND` and `_DEL` suffixes are a convention across the whole VATSIM network; `_R_TWR` is specific to Vatsim Brasil. See the ATS Units and Positions chapter for details on the jurisdiction of each one.

## Where to find local data

!!! tip "On the network (Vatbrz)"
    This checklist does not replace the chart. Lateral and vertical limits, transition altitude and applied class change by aerodrome and by AIRAC cycle. The source is always the AIP, the chart and the portal's [**Operational Manuals**](../../../MOP/aerodromos/index.en.md) section.

---
