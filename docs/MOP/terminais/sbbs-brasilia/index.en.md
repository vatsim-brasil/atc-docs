---
  title: Overview
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

The Brasília FIR has eight terminal control areas (TMA), each served by an approach control unit (APP). This page gathers, for each TMA, its limits, airspace class, ATS surveillance, VFR circulation and the top-down coverage order used on the network. Each TMA has its own page, with a map, volumes, ATC units, top-down coverage and VFR circulation.

!!! info "Map interactivity"

    Click a TMA or CTR to see a summary and a link to its page. Colors show the airspace class. Use the layer control in the top right corner to change the base map and toggle TMAs, CTRs and the FIR boundary.

<div class="fir-map-top">
    <div id="mapa-tmas" class="mapa"></div>
</div>

## Summary

| TMA | Position | Freq. | Limits | Class | Surveillance | Aerodromes |
| --- | --- | --- | --- | --- | --- | --- |
| [**SBWH** · Belo Horizonte](SBWH.en.md) | `SBWH_APP` | 129.100 | 4100 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBCF](../../aerodromos/sbbs-brasilia/twr/SBCF.en.md), [SBBH](../../aerodromos/sbbs-brasilia/twr/SBBH.en.md), [SBLS](../../aerodromos/sbbs-brasilia/afis/SBLS.en.md) |
| [**SBWR** · Brasília](SBWR.en.md) | `SBWR_APP` | 119.200 | FL065 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBBR](../../aerodromos/sbbs-brasilia/twr/SBBR.en.md) |
| [**SBWU** · Bauru](SBWU.en.md) | `SBWU_APP` | 121.300 | FL045 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> | Procedural | `SBBU`, [SBAE](../../aerodromos/sbbs-brasilia/afis/SBAE.en.md), [SBML](../../aerodromos/sbbs-brasilia/afis/SBML.en.md) |
| [**SBXD** · Palmas](SBXD.en.md) | `SBXD_APP` | 119.000 | 3500 FT – FL145 | <span class="classe-badge classe-d">D</span> | Procedural | [SBPJ](../../aerodromos/sbbs-brasilia/twr/SBPJ.en.md) |
| [**SBXN** · Anápolis](SBXN.en.md) | `SBXN_APP` | 129.450 | FL065 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | `SBAN`, [SBGO](../../aerodromos/sbbs-brasilia/twr/SBGO.en.md) |
| [**SBXQ** · Academia](SBXQ.en.md) | `SBXQ_APP` | 120.100 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | `SBYS`, `SBRP`, [SBAQ](../../aerodromos/sbbs-brasilia/afis/SBAQ.en.md), [SBGP](../../aerodromos/sbbs-brasilia/afis/SBGP.en.md) |
| [**SBXU** · Uberaba](SBXU.en.md) | `SBXU_APP` | 120.800 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> | Procedural | `SBUR` |
| [**SBXW** · Uberlândia](SBXW.en.md) | `SBXW_APP` | 122.850 | 5500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> | Procedural | `SBUL` |

## How to read this page

- **Airspace class.** In classes A and C all flights are controlled and separated. Class A only admits IFR. In class C, VFR is separated from IFR and receives traffic information on other VFR. In class D, IFR is only separated from IFR, and VFR only receives traffic information. All require a clearance to enter.
- **ATS surveillance.** Shows whether, in the real world, the TMA is listed in AIP ENR 1.6 as covered by radar. Academia, Anápolis, Belo Horizonte and Brasília TMAs are listed. In the others the real-world service is procedural: separation by time, DME distance, levels and position reports. On the network, the controller client shows all traffic; this information is a reference for realistic operations.
- **Top-down coverage.** When the APP is offline, the TMA is covered by the first online position in the listed order, as defined in the FIR sector package.
- **ATZ.** Aerodrome traffic zone around controlled aerodromes. The AIP publishes no class for ATZs.
- **VFR circulation.** Summarizes the rules published in the AIP (AD 2.22 and ENR 2.1) and highlights the official visual navigation documents: the VFR circulation circular (AIC) and the visual charts (REA, REH and REUL), when they exist. The charts are embedded in each TMA page; the AIC links to the official DECEA page.

---

!!! warning "Precedence"
    Content for flight simulation. The following prevail, in this order: the current official aeronautical publication, the sector package distributed by VATSIM Brasil (callsigns, frequencies and logons) and the current VATSIM policy.

<!--
Daqui pra baixo, é o mapa. Contornos extraídos do pacote SBBS (setores TMA_* e CTR_*), em [longitude, latitude].
-->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
   integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
   crossorigin=""/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
   integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
   crossorigin=""></script>

<style>
    .mapa { height: 650px }
</style>

<script>
// Escopo isolado: com a navegação instantânea, o script é reexecutado a cada troca de página
(function () {

const cores = {"A": "#f87171", "C": "#fbbf24", "D": "#2dd4bf", "\u2014": "#94a3b8"};

const volumes = [
    {"tipo": "tma", "id": "SBXQ", "nome": "Academia TMA", "posicao": "SBXQ_APP", "freq": "120.100", "lim": "5500 FT – FL195", "classe": "A/C", "link": "SBXQ/", "contorno": [[-49.7337, -21.6635], [-49.589329, -21.528301], [-49.297551, -21.253685], [-48.938497, -20.913151], [-48.87602, -20.852815], [-48.7518, -20.7326], [-48.5967, -20.5822], [-48.170883, -20.560031], [-47.8574, -20.5437], [-47.382364, -20.583379], [-47.134915, -20.83935], [-47.027, -20.950333], [-47.001569, -21.051245], [-46.975358, -21.155012], [-46.775333, -21.875833], [-46.754667, -22.006333], [-46.756939, -22.097781], [-46.755, -22.186667], [-46.771069, -22.205839], [-46.820401, -22.26471], [-46.985278, -22.461389], [-47.440833, -22.646667], [-47.585, -22.704722], [-47.645833, -22.860278], [-47.726667, -23.067222], [-47.953, -23.0057], [-47.953, -22.9937], [-48.089207, -22.953543], [-48.861, -22.726], [-48.832226, -22.69952], [-48.7105, -22.5875], [-48.6833, -22.5508], [-48.642, -22.48], [-48.5486, -22.2114], [-48.6587, -22.083], [-49.7337, -21.6635]]},
    {"tipo": "tma", "id": "SBWR", "nome": "Brasília TMA", "posicao": "SBWR_APP", "freq": "119.200", "lim": "FL065 – FL195", "classe": "A/C", "link": "SBWR/", "contorno": [[-47.864047, -15.002428], [-47.764833, -15.015167], [-47.446, -15.162667], [-47.140167, -15.4365], [-47.063742, -16.008367], [-47.060556, -16.032222], [-47.242833, -16.388], [-47.325, -16.486667], [-47.339352, -16.499838], [-47.427097, -16.579906], [-47.442167, -16.593667], [-47.542167, -16.6595], [-47.694508, -16.708267], [-47.931333, -16.780833], [-48.084167, -16.7755], [-48.299, -16.742167], [-48.448333, -16.689667], [-48.477, -16.664667], [-48.644833, -16.548667], [-48.5995, -16.235667], [-48.541667, -16.099333], [-48.602333, -15.852833], [-48.775105, -15.785841], [-48.936167, -15.723167], [-48.946667, -15.671333], [-48.7775, -15.333333], [-48.674833, -15.243], [-48.401431, -15.049731], [-48.077167, -14.965], [-47.960556, -14.99], [-47.889153, -14.999181], [-47.864047, -15.002428]]},
    {"tipo": "tma", "id": "SBXU", "nome": "Uberaba TMA", "posicao": "SBXU_APP", "freq": "120.800", "lim": "5500 FT – FL195", "classe": "A/D", "link": "SBXU/", "contorno": [[-46.96583, -20.012953], [-46.935833, -19.684167], [-46.97, -19.538333], [-47.149, -19.1555], [-47.451035, -19.206406], [-48.0927, -19.3127], [-48.5242, -19.3761], [-48.599271, -19.385839], [-48.9061, -19.4251], [-48.892, -19.9802], [-48.5967, -20.5822], [-48.170883, -20.560031], [-47.8574, -20.5437], [-47.382364, -20.583379], [-47.21942, -20.430273], [-47.120658, -20.340369], [-46.984167, -20.213611], [-46.96583, -20.012953]]},
    {"tipo": "tma", "id": "SBXN", "nome": "Anápolis TMA", "posicao": "SBXN_APP", "freq": "129.450", "lim": "FL065 – FL195", "classe": "A/C", "link": "SBXN/", "contorno": [[-48.936167, -15.723167], [-48.775105, -15.785841], [-48.602333, -15.852833], [-48.541667, -16.099333], [-48.5995, -16.235667], [-48.644833, -16.548667], [-48.477, -16.664667], [-48.542662, -17.280069], [-48.559833, -17.440167], [-49.036514, -17.542154], [-49.318, -17.601833], [-49.737219, -17.352773], [-49.884167, -17.265167], [-49.972133, -16.953389], [-50.039162, -16.715102], [-50.054333, -16.661], [-49.748989, -16.294681], [-49.2915, -15.745833], [-49.00315, -15.727439], [-48.936167, -15.723167]]},
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 1", "posicao": "SBWH_APP", "freq": "129.100", "lim": "5500 FT – FL195", "classe": "A/C", "link": "SBWH/", "contorno": [[-43.266908, -20.206404], [-43.4576, -20.4966], [-43.9047, -20.5654], [-43.969076, -20.54265], [-44.4974, -20.3533], [-44.6949, -19.8], [-44.7775, -19.569], [-44.6146, -19.1277], [-44.353616, -18.988162], [-44.3214, -18.9709], [-43.951268, -18.949964], [-43.692, -18.9348], [-43.1142, -19.6081], [-43.1373, -20.0084], [-43.266908, -20.206404]]},
    {"tipo": "tma", "id": "SBXW", "nome": "Uberlândia TMA", "posicao": "SBXW_APP", "freq": "122.850", "lim": "5500 FT – FL195", "classe": "A/D", "link": "SBXW/", "contorno": [[-47.151491, -19.152226], [-47.149, -19.1555], [-47.451035, -19.206406], [-48.0927, -19.3127], [-48.5242, -19.3761], [-48.599271, -19.385839], [-48.9061, -19.4251], [-48.9198, -18.9543], [-48.913423, -18.920339], [-48.884639, -18.767298], [-48.8489, -18.5767], [-48.743696, -18.487564], [-48.4613, -18.2477], [-48.3419, -18.2199], [-48.2481, -18.2079], [-48.1278, -18.2133], [-47.8902, -18.2865], [-47.6971, -18.4316], [-47.545217, -18.632995], [-47.283397, -18.978726], [-47.151491, -19.152226]]},
    {"tipo": "tma", "id": "SBWU", "nome": "Bauru TMA", "posicao": "SBWU_APP", "freq": "121.300", "lim": "FL045 – FL195", "classe": "A/D", "link": "SBWU/", "contorno": [[-48.832226, -22.69952], [-48.7105, -22.5875], [-48.6833, -22.5508], [-48.642, -22.48], [-48.5486, -22.2114], [-48.6587, -22.083], [-49.7337, -21.6635], [-50.006, -21.7598], [-50.0593, -21.9363], [-50.105463, -22.08634], [-50.171111, -22.299444], [-50.224367, -22.498381], [-50.2487, -22.5827], [-49.1192, -22.9628], [-48.861, -22.726], [-48.832226, -22.69952]]},
    {"tipo": "tma", "id": "SBXD", "nome": "Palmas TMA", "posicao": "SBXD_APP", "freq": "119.000", "lim": "3500 FT – FL145", "classe": "D", "link": "SBXD/", "contorno": [[-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.695833, -10.428889], [-47.723056, -10.528889], [-47.767222, -10.621389], [-47.8125, -10.688889], [-47.863333, -10.748611], [-47.915278, -10.798889], [-47.9675, -10.835278], [-48.019444, -10.874722], [-48.090556, -10.904444], [-48.148333, -10.932778], [-48.233333, -10.949167], [-48.318056, -10.962778], [-48.397778, -10.964444], [-48.482778, -10.953611], [-48.584167, -10.926944], [-48.6775, -10.885], [-48.776389, -10.818889], [-48.913611, -10.676944], [-48.971111, -10.585278], [-49.008333, -10.485278], [-49.035833, -10.378611], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531]]},
    {"tipo": "tma", "id": "SBWH", "nome": "Belo Horizonte 2", "posicao": "SBWH_APP", "freq": "129.100", "lim": "4100 FT – 5500 FT", "classe": "C", "link": "SBWH/", "contorno": [[-44.3793, -19.2945], [-44.2396, -19.225], [-43.9432, -19.166], [-43.4868, -19.5018], [-43.5229, -19.9021], [-43.7936, -20.1036], [-43.9467, -20.0488], [-43.9806, -19.9293], [-44.3038, -19.9772], [-44.4276, -19.5236], [-44.3793, -19.2945]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "Brasília CTR", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – FL065", "classe": "C", "link": "SBWR/", "contorno": [[-48.4375, -15.645], [-48.393056, -16.179444], [-47.391389, -16.108333], [-47.432778, -15.573611], [-48.4375, -15.645]]},
    {"tipo": "ctr", "id": "SBWU", "nome": "Bauru CTR", "posicao": "SBBU_R_TWR", "freq": "121.300", "lim": "GND – FL045", "classe": "D", "link": "SBWU/", "contorno": [[-49.05, -21.9821], [-48.968, -21.9901], [-48.8971, -22.0107], [-48.8247, -22.0477], [-48.7679, -22.0923], [-48.721, -22.146], [-48.6826, -22.2141], [-48.6602, -22.2882], [-48.6545, -22.3572], [-48.6647, -22.4336], [-48.6883, -22.4993], [-48.7247, -22.5597], [-48.7787, -22.618], [-48.8446, -22.6646], [-48.9118, -22.6948], [-48.9839, -22.7128], [-49.0583, -22.7179], [-49.1325, -22.7099], [-49.2037, -22.6891], [-49.2762, -22.652], [-49.3331, -22.6072], [-49.3799, -22.5533], [-49.415, -22.4922], [-49.4371, -22.426], [-49.4455, -22.3495], [-49.4367, -22.273], [-49.4143, -22.207], [-49.379, -22.146], [-49.3321, -22.0923], [-49.2753, -22.0477], [-49.2029, -22.0107], [-49.132, -21.9901], [-49.05, -21.9821]]},
    {"tipo": "ctr", "id": "SBXQ", "nome": "Academia CTR (SBYS)", "posicao": "SBYS_TWR", "freq": "118.300", "lim": "GND – 5500 FT", "classe": "C", "link": "SBXQ/", "contorno": [[-47.34, -21.646667], [-47.402276, -21.651719], [-47.462673, -21.666724], [-47.519367, -21.691228], [-47.570644, -21.724491], [-47.614949, -21.765509], [-47.650938, -21.813041], [-47.677512, -21.865649], [-47.693855, -21.921738], [-47.69946, -21.979609], [-47.694144, -22.037503], [-47.678054, -22.09366], [-47.651669, -22.146372], [-47.61578, -22.194032], [-47.571475, -22.235186], [-47.520098, -22.268577], [-47.463216, -22.293185], [-47.402565, -22.308257], [-47.34, -22.313333], [-47.277435, -22.308257], [-47.216784, -22.293185], [-47.159902, -22.268577], [-47.108525, -22.235186], [-47.06422, -22.194032], [-47.028331, -22.146372], [-47.001946, -22.09366], [-46.985856, -22.037503], [-46.98054, -21.979609], [-46.986145, -21.921738], [-47.002488, -21.865649], [-47.029062, -21.813041], [-47.065051, -21.765509], [-47.109356, -21.724491], [-47.160633, -21.691228], [-47.217327, -21.666724], [-47.277724, -21.651719], [-47.34, -21.646667]]},
    {"tipo": "ctr", "id": "SBXN", "nome": "Anápolis 2 CTR (SBGO)", "posicao": "SBGO_TWR", "freq": "118.700", "lim": "GND – FL065", "classe": "C", "link": "SBXN/", "contorno": [[-49.098889, -16.4875], [-49.313056, -16.367222], [-49.411667, -16.3125], [-49.500278, -16.308056], [-49.709167, -16.65], [-48.998056, -17.046944], [-48.770833, -16.670278], [-49.098889, -16.4875]]},
    {"tipo": "ctr", "id": "SBXW", "nome": "Uberlândia CTR", "posicao": "SBUL_TWR", "freq": "118.800", "lim": "GND – FL055", "classe": "D", "link": "SBXW/", "contorno": [[-48.548311, -18.762206], [-48.488254, -18.665917], [-48.395638, -18.598614], [-48.304379, -18.566701], [-48.223232, -18.559057], [-48.149102, -18.565869], [-48.083629, -18.588802], [-48.028093, -18.618482], [-47.956776, -18.668832], [-47.901863, -18.747832], [-47.875748, -18.870728], [-47.895587, -18.992235], [-47.953546, -19.091064], [-48.0437, -19.161871], [-48.16468, -19.205267], [-48.284852, -19.205827], [-48.397743, -19.16565], [-48.490769, -19.087975], [-48.547968, -18.987952], [-48.567697, -18.875917], [-48.548311, -18.762206]]},
    {"tipo": "ctr", "id": "SBXU", "nome": "Uberaba CTR", "posicao": "SBUR_TWR", "freq": "118.500", "lim": "GND – FL055", "classe": "D", "link": "SBXU/", "contorno": [[-48.089312, -19.547577], [-48.006348, -19.520748], [-47.914897, -19.51932], [-47.830001, -19.548555], [-47.755764, -19.606613], [-47.714895, -19.678521], [-47.698639, -19.763401], [-47.713018, -19.851355], [-47.758858, -19.925215], [-47.826495, -19.98051], [-47.917755, -20.012422], [-48.004557, -20.011133], [-48.089453, -19.981899], [-48.161684, -19.923139], [-48.202646, -19.84799], [-48.219267, -19.762147], [-48.202059, -19.678659], [-48.160231, -19.606201], [-48.089312, -19.547577]]},
    {"tipo": "ctr", "id": "SBXD", "nome": "Palmas CTR", "posicao": "SBPJ_TWR", "freq": "118.000", "lim": "GND – 3500 FT", "classe": "D", "link": "SBXD/", "contorno": [[-48.3585, -10.038], [-48.402587, -10.041795], [-48.445338, -10.053065], [-48.485456, -10.071469], [-48.521724, -10.096448], [-48.553042, -10.127245], [-48.578457, -10.162926], [-48.597197, -10.202408], [-48.608691, -10.244492], [-48.612585, -10.287901], [-48.608759, -10.331316], [-48.597327, -10.373417], [-48.578632, -10.412926], [-48.55324, -10.448639], [-48.521923, -10.47947], [-48.48563, -10.504481], [-48.445467, -10.522911], [-48.402656, -10.534199], [-48.3585, -10.538], [-48.314344, -10.534199], [-48.271532, -10.522911], [-48.23137, -10.504481], [-48.195077, -10.47947], [-48.16376, -10.448639], [-48.138368, -10.412926], [-48.119673, -10.373417], [-48.108241, -10.331316], [-48.104415, -10.287901], [-48.108309, -10.244492], [-48.119803, -10.202408], [-48.138543, -10.162926], [-48.163958, -10.127245], [-48.195276, -10.096448], [-48.231544, -10.071469], [-48.271662, -10.053065], [-48.314413, -10.041795], [-48.3585, -10.038]]},
    {"tipo": "ctr", "id": "SBXQ", "nome": "Ribeirão CTR (SBRP)", "posicao": "SBRP_TWR", "freq": "118.000", "lim": "GND – 5500 FT", "classe": "C", "link": "SBXQ/", "contorno": [[-47.776, -20.909367], [-47.819375, -20.912906], [-47.861438, -20.923417], [-47.900917, -20.940582], [-47.936615, -20.963881], [-47.967451, -20.992609], [-47.992487, -21.025896], [-48.01096, -21.062733], [-48.022306, -21.102004], [-48.026174, -21.142516], [-48.02244, -21.183039], [-48.011213, -21.222342], [-47.992828, -21.259229], [-47.967839, -21.292576], [-47.937003, -21.321368], [-47.901258, -21.344726], [-47.861692, -21.36194], [-47.81951, -21.372483], [-47.776, -21.376033], [-47.73249, -21.372483], [-47.690308, -21.36194], [-47.650742, -21.344726], [-47.614997, -21.321368], [-47.584161, -21.292576], [-47.559172, -21.259229], [-47.540787, -21.222342], [-47.52956, -21.183039], [-47.525826, -21.142516], [-47.529694, -21.102004], [-47.54104, -21.062733], [-47.559513, -21.025896], [-47.584549, -20.992609], [-47.615385, -20.963881], [-47.651083, -20.940582], [-47.690562, -20.923417], [-47.732625, -20.912906], [-47.776, -20.909367]]},
    {"tipo": "ctr", "id": "SBXN", "nome": "Anápolis 1 CTR (SBAN)", "posicao": "SBAN_TWR", "freq": "118.300", "lim": "GND – FL065", "classe": "C", "link": "SBXN/", "contorno": [[-49.098889, -16.4875], [-49.313056, -16.367222], [-48.896111, -15.872222], [-48.643056, -16.071111], [-48.854722, -16.323056], [-48.916389, -16.275], [-49.015556, -16.378611], [-49.098889, -16.4875]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Confins CTR", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 5500 FT", "classe": "D", "link": "SBWH/", "contorno": [[-43.7636, -19.6104], [-43.8163, -19.7746], [-43.9881, -19.8107], [-44.1995, -19.5813], [-43.9659, -19.39], [-43.7636, -19.6104]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Belo Horizonte CTR", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 5500 FT", "classe": "C", "link": "SBWH/", "contorno": [[-43.7636, -19.6104], [-43.6578, -19.7253], [-43.7524, -19.9447], [-43.8544, -19.9932], [-43.9475, -19.9796], [-43.9592, -19.9384], [-44.1801, -19.8593], [-44.1995, -19.5813], [-43.9881, -19.8107], [-43.8163, -19.7746], [-43.7636, -19.6104]]},
    {"tipo": "ctr", "id": "SBWR", "nome": "Brasília ATZ", "posicao": "SBBR_TWR", "freq": "118.100", "lim": "GND – 5500 FT", "classe": "—", "link": "SBWR/", "contorno": [[-48.021944, -15.837778], [-47.988889, -15.806944], [-47.858333, -15.798056], [-47.823056, -15.826667], [-47.816667, -15.912778], [-47.849722, -15.943611], [-47.980278, -15.952778], [-48.015278, -15.924444], [-48.021944, -15.837778]]},
    {"tipo": "ctr", "id": "SBWU", "nome": "Arealva ATZ", "posicao": "SBAE_R_TWR", "freq": "126.600", "lim": "GND – 1500 FT AGL", "classe": "—", "link": "SBWU/", "contorno": [[-49.068333, -22.074501], [-49.040563, -22.078574], [-49.015506, -22.090397], [-48.995614, -22.108813], [-48.982832, -22.132021], [-48.978416, -22.157753], [-48.982801, -22.183489], [-48.995563, -22.206711], [-49.015456, -22.225142], [-49.040532, -22.236977], [-49.068333, -22.241055], [-49.096135, -22.236977], [-49.121211, -22.225142], [-49.141104, -22.206711], [-49.153866, -22.183489], [-49.158251, -22.157753], [-49.153834, -22.132021], [-49.141053, -22.108813], [-49.12116, -22.090397], [-49.096104, -22.078574], [-49.068333, -22.074501]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Confins ATZ", "posicao": "SBCF_TWR", "freq": "118.200", "lim": "GND – 4500 FT", "classe": "—", "link": "SBWH/", "contorno": [[-43.912222, -19.620833], [-43.935278, -19.64], [-43.939722, -19.652222], [-43.93, -19.662778], [-43.899167, -19.696389], [-43.951667, -19.738333], [-44.083056, -19.596389], [-43.973889, -19.509722], [-43.888889, -19.601667], [-43.912222, -19.620833]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Belo Horizonte ATZ (Pampulha)", "posicao": "SBBH_TWR", "freq": "118.000", "lim": "GND – 4500 FT", "classe": "—", "link": "SBWH/", "contorno": [[-43.891667, -19.813056], [-43.856944, -19.840833], [-43.881667, -19.911111], [-43.928056, -19.917778], [-44.009444, -19.892222], [-44.0425, -19.859722], [-44.017778, -19.789444], [-43.974722, -19.786944], [-43.891667, -19.813056]]},
    {"tipo": "ctr", "id": "SBWH", "nome": "Lagoa Santa ATZ", "posicao": "SBLS_R_TWR", "freq": "122.850", "lim": "GND – 4500 FT", "classe": "—", "link": "SBWH/", "contorno": [[-43.912222, -19.620833], [-43.863611, -19.632778], [-43.8575, -19.6625], [-43.863611, -19.679444], [-43.93, -19.662778], [-43.939722, -19.652222], [-43.935278, -19.64], [-43.912222, -19.620833]]}
];

const limiteFir = [[-50.105463, -22.08634], [-50.4579, -21.6254], [-51.3619, -20.4271], [-52.0114, -19.7046], [-52.7536, -18.9223], [-54.1235, -17.4059], [-53.1008, -16.7092], [-53.3203, -15.8089], [-53.3927, -15.4768], [-53.6267, -14.5625], [-53.5013, -12.96], [-53.051, -12.1836], [-51.672778, -11.0275], [-51.4728, -10.8474], [-51.0866, -10.5156], [-49.042249, -10.22507], [-48.991334, -10.040764], [-48.8754, -9.8531], [-48.6528, -9.6856], [-48.3677, -9.6214], [-48.1628, -9.6519], [-48.0051, -9.7238], [-47.8129, -9.9043], [-47.701, -10.1604], [-47.6882, -10.2861], [-47.3153, -10.3287], [-46.891, -12.0218], [-45.6083, -13.3218], [-45.278124, -13.796406], [-44.5772, -14.7847], [-44.3306, -15.2179], [-44.095833, -15.626499], [-42.6788, -16.4093], [-42.3377, -16.6247], [-41.8206, -16.9483], [-42.4482, -18.758], [-42.4406, -19.105], [-42.4795, -19.463], [-42.5269, -20.0033], [-42.7521, -20.4117], [-43.3928, -20.1562], [-43.965, -20.5375], [-44.7076, -21.4759], [-45.7749, -22.7993], [-45.8108, -23.0094], [-45.86, -23.2332], [-46.655, -23.6273], [-47.2173, -23.3154], [-47.573, -23.1164], [-47.726084, -23.065083], [-48.832226, -22.69952], [-49.9178, -22.3302]];

const elemento = document.getElementById('mapa-tmas');
if (!elemento || elemento._leaflet_id) return;

function paraLatLng(c) {
    return [c[1], c[0]];
}

var tileMapaClaro = camadaMapbox('claro', { minZoom: 3, maxZoom: 13 });
var tileMapaEscuro = camadaMapbox('escuro', { minZoom: 3, maxZoom: 13 });
var tileMapaSatelite = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    minZoom: 3,
    maxZoom: 13,
    attribution: '&copy; Esri'
});

var grupoFir = L.layerGroup([
    L.polygon(limiteFir.map(paraLatLng), { color: '#94a3b8', weight: 2, dashArray: '6 6', fill: false, interactive: false })
]);
var grupoTma = L.featureGroup();
var grupoCtr = L.featureGroup();

// Setores do APP (só nas TMAs setorizadas), agrupados por posição
const setores = [];
const paletaSetores = ['#60a5fa', '#f472b6', '#a3e635', '#fb923c', '#a78bfa', '#2dd4bf', '#fbbf24', '#f87171', '#34d399', '#e879f9', '#38bdf8', '#fda4af', '#818cf8'];
var grupoSetores = L.featureGroup();
setores.forEach(function (s, k) {
    var cor = paletaSetores[k % paletaSetores.length];
    L.polygon(s.contorno.map(paraLatLng), { color: cor, fillColor: cor, weight: 2, fillOpacity: 0.2 })
        .bindPopup('<b>' + s.posicao + '</b><br>' + s.freq + ' MHz<br>' + s.lim)
        .addTo(grupoSetores);
});

volumes.forEach(function (v) {
    // A cor segue a classe do volume inferior (ex.: A/C é desenhado como C)
    var cor = cores[v.classe.split('/').pop()];
    var ctr = v.tipo === 'ctr';
    var poligono = L.polygon(v.contorno.map(paraLatLng), {
        color: cor,
        fillColor: cor,
        weight: ctr ? 2 : 2.5,
        dashArray: ctr ? '4 4' : null,
        fillOpacity: ctr ? 0.3 : 0.12
    });
    poligono.bindPopup(
        '<b>' + v.nome + '</b><br>' +
        '<code>' + v.posicao + '</code> · ' + v.freq + ' MHz<br>' +
        v.lim + ' · Class ' + v.classe + '<br><a href="' + v.link + '">See details</a>'
    );
    poligono.on('mouseover', function () { this.setStyle({ weight: 4 }); });
    poligono.on('mouseout', function () { this.setStyle({ weight: ctr ? 2 : 2.5 }); });
    poligono.addTo(ctr ? grupoCtr : grupoTma);
});

var mapa = L.map('mapa-tmas', {
    minZoom: 3,
    maxZoom: 13,
    layers: [tileMapaClaro, grupoFir, grupoTma, grupoCtr]
});

mapa.fitBounds(L.polygon(limiteFir.map(paraLatLng)).getBounds(), { padding: [20, 20] });

// Rótulos com o designador de cada TMA
var rotulos = {};
volumes.forEach(function (v) {
    if (v.tipo !== 'tma' || rotulos[v.id]) return;
    rotulos[v.id] = true;
    var centro = L.polygon(v.contorno.map(paraLatLng)).getBounds().getCenter();
    L.marker(centro, {
        interactive: false,
        icon: L.divIcon({ className: 'fir-rotulo', html: v.id, iconSize: null })
    }).addTo(grupoTma);
});

L.control.layers({
    "Light": tileMapaClaro,
    "Dark": tileMapaEscuro,
    "Arcgis Satellite": tileMapaSatelite
}, {
    "TMAs": grupoTma,
    "CTRs": grupoCtr,
    "FIR boundary": grupoFir
}).addTo(mapa);

// Legenda das classes
var legenda = L.control({ position: 'bottomleft' });
legenda.onAdd = function () {
    var div = L.DomUtil.create('div', 'mapa-legenda');
    div.innerHTML = '<b>Class</b>' + ['A', 'C', 'D'].map(function (c) {
        return '<div><span style="background:' + cores[c] + '"></span>' + c + '</div>';
    }).join('');
    return div;
};
legenda.addTo(mapa);

})();
</script>
