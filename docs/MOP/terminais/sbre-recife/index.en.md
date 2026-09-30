---
  title: Overview
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

The Recife FIR has ten terminal control areas (TMA), each served by an approach control unit (APP). This page gathers, for each TMA, its limits, airspace class, ATS surveillance, VFR circulation and the top-down coverage order used on the network. Each TMA has its own page, with a map, volumes, ATC units, top-down coverage and VFR circulation.

!!! info "Map interactivity"

    Click a TMA or CTR to see a summary and a link to its page. Colors show the airspace class. Use the layer control in the top right corner to change the base map and toggle TMAs, CTRs and the FIR boundary.

<div class="fir-map-top">
    <div id="mapa-tmas" class="mapa"></div>
</div>

## Summary

| TMA | Position | Freq. | Limits | Class | Surveillance | Aerodromes |
| --- | --- | --- | --- | --- | --- | --- |
| [**SBWF** · Recife](SBWF.en.md) | `SBWF_APP` | 120.400 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBRF](../../aerodromos/sbre-recife/twr/SBRF.en.md), [SBJP](../../aerodromos/sbre-recife/twr/SBJP.en.md) |
| [**SBWK** · Porto Seguro](SBWK.en.md) | `SBWK_APP` | 120.900 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBPS](../../aerodromos/sbre-recife/twr/SBPS.en.md) |
| [**SBWL** · Ilhéus](SBWL.en.md) | `SBWL_APP` | 120.100 | FL035 – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> | Procedural | [SBIL](../../aerodromos/sbre-recife/twr/SBIL.en.md) |
| [**SBWZ** · Fortaleza](SBWZ.en.md) | `SBWZ_APP` | 133.000 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBFZ](../../aerodromos/sbre-recife/twr/SBFZ.en.md) |
| [**SBXA** · Aracaju](SBXA.en.md) | `SBXA_APP` | 120.300 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> | Procedural | [SBAR](../../aerodromos/sbre-recife/twr/SBAR.en.md) |
| [**SBXE** · Teresina](SBXE.en.md) | `SBXE_APP` | 119.600 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-d">D</span> | Procedural | [SBTE](../../aerodromos/sbre-recife/twr/SBTE.en.md), `SNDR` |
| [**SBXM** · Maceió](SBXM.en.md) | `SBXM_APP` | 119.250 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBMO](../../aerodromos/sbre-recife/twr/SBMO.en.md) |
| [**SBXR** · Vitória](SBXR.en.md) | `SBXR_APP` | 119.850 | 4500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBVT](../../aerodromos/sbre-recife/twr/SBVT.en.md) |
| [**SBXS** · Salvador](SBXS.en.md) | `SBXS_APP` | 119.350 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBSV](../../aerodromos/sbre-recife/twr/SBSV.en.md) |
| [**SBXT** · Natal](SBXT.en.md) | `SBXT_APP` | 119.300 | 3500 FT – FL195 | <span class="classe-badge classe-a">A</span> <span class="classe-badge classe-c">C</span> | Radar | [SBSG](../../aerodromos/sbre-recife/twr/SBSG.en.md), `SBNT` |

## How to read this page

- **Airspace class.** In classes A and C all flights are controlled and separated. Class A only admits IFR. In class C, VFR is separated from IFR and receives traffic information on other VFR. In class D, IFR is only separated from IFR, and VFR only receives traffic information. All require a clearance to enter.
- **ATS surveillance.** Shows whether, in the real world, the TMA is listed in AIP ENR 1.6 as covered by radar. Fortaleza, Maceió, Natal, Porto Seguro, Recife, Salvador and Vitória TMAs are listed. In the others the real-world service is procedural: separation by time, DME distance, levels and position reports. On the network, the controller client shows all traffic; this information is a reference for realistic operations.
- **Top-down coverage.** When the APP is offline, the TMA is covered by the first online position in the listed order, as defined in the FIR sector package.
- **VFR circulation.** Summarizes the rules published in the AIP (AD 2.22 and ENR 2.1) and points to the special VFR routes chart (CCV REA), when one exists.

---

Sources: VATSIM Brasil SBRE sector package (lateral limits, positions, frequencies and top-down coverage) and AIP Brasil, AIRAC A 17/2026 (classes, vertical limits, ATS surveillance and VFR rules).

!!! warning "Precedence"
    Content for flight simulation. The following prevail, in this order: the current official aeronautical publication, the sector package distributed by VATSIM Brasil (callsigns, frequencies and logons) and the current VATSIM policy.

<!--
Daqui pra baixo, é o mapa. Contornos extraídos do pacote SBRE (setores TMA_* e CTR_*), em [longitude, latitude].
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
    {"tipo": "tma", "id": "SBXS", "nome": "Salvador TMA", "posicao": "SBXS_APP", "freq": "119.350", "lim": "3500 FT – FL195", "classe": "A/C", "link": "SBXS/", "contorno": [[-37.4625, -12.085167], [-37.9215, -11.7975], [-39.203333, -12.0], [-39.258611, -12.156111], [-39.278008, -12.70715], [-39.295833, -13.211389], [-39.132146, -13.456795], [-38.931389, -13.757778], [-38.416389, -13.941389], [-38.0775, -13.348056], [-37.841147, -13.005044], [-37.812686, -12.963647], [-37.4625, -12.085167]]},
    {"tipo": "tma", "id": "SBWZ", "nome": "Fortaleza TMA", "posicao": "SBWZ_APP", "freq": "133.000", "lim": "3500 FT – FL195", "classe": "A/C", "link": "SBWZ/", "contorno": [[-39.469444, -3.276667], [-39.043056, -2.967222], [-38.242222, -2.958611], [-37.822778, -3.203056], [-37.575833, -3.536111], [-37.524167, -4.006389], [-37.804167, -4.304444], [-37.968056, -4.474444], [-38.300833, -4.531667], [-38.767778, -4.526667], [-39.245833, -4.396667], [-39.595833, -3.837222], [-39.469444, -3.276667]]},
    {"tipo": "tma", "id": "SBWF", "nome": "Recife TMA", "posicao": "SBWF_APP", "freq": "120.400", "lim": "3500 FT – FL195", "classe": "A/C", "link": "SBWF/", "contorno": [[-34.774722, -6.844722], [-35.391111, -6.935], [-35.43, -6.940278], [-35.5175, -7.502778], [-35.709167, -7.841667], [-35.708748, -7.943557], [-35.707778, -8.18], [-35.706111, -8.609444], [-35.585, -8.705], [-35.127222, -8.987778], [-34.885833, -9.136111], [-34.240278, -8.348056], [-34.244286, -8.245169], [-34.289444, -7.086111], [-34.774722, -6.844722]]},
    {"tipo": "tma", "id": "SBXT", "nome": "Natal TMA", "posicao": "SBXT_APP", "freq": "119.300", "lim": "3500 FT – FL195", "classe": "A/C", "link": "SBXT/", "contorno": [[-36.209168, -5.327283], [-36.030556, -5.120556], [-35.086389, -5.422778], [-34.734444, -5.256667], [-34.463889, -5.668611], [-34.739722, -5.922222], [-34.774722, -6.844722], [-35.391111, -6.935], [-35.43, -6.940278], [-35.969444, -6.445833], [-36.3275, -5.9425], [-36.420556, -5.571944], [-36.209168, -5.327283]]},
    {"tipo": "tma", "id": "SBXA", "nome": "Aracaju TMA", "posicao": "SBXA_APP", "freq": "120.300", "lim": "3500 FT – FL195", "classe": "A/D", "link": "SBXA/", "contorno": [[-36.221667, -10.433611], [-36.448056, -10.694722], [-36.406111, -10.833333], [-36.3925, -10.965278], [-36.411614, -11.097711], [-36.415833, -11.126944], [-36.466944, -11.249444], [-36.531389, -11.351111], [-36.628889, -11.452778], [-36.736389, -11.521944], [-36.858611, -11.571667], [-37.001389, -11.594444], [-37.178611, -11.581111], [-37.4625, -12.085167], [-37.9215, -11.7975], [-37.6375, -11.380833], [-37.719444, -11.219722], [-37.7525, -11.078333], [-37.756389, -10.949444], [-37.738611, -10.822778], [-37.694167, -10.697222], [-37.67785, -10.67154], [-37.632222, -10.599722], [-37.5375, -10.491667], [-37.4175, -10.404167], [-37.266389, -10.339722], [-37.122222, -10.315278], [-36.991667, -10.318056], [-36.855556, -10.346389], [-36.631944, -10.091389], [-36.221667, -10.433611]]},
    {"tipo": "tma", "id": "SBWK", "nome": "Porto Seguro TMA", "posicao": "SBWK_APP", "freq": "120.900", "lim": "3500 FT – FL195", "classe": "A/C", "link": "SBWK/", "contorno": [[-38.823611, -15.649444], [-39.374722, -15.609722], [-39.3961, -15.8448], [-39.4531, -15.8761], [-39.5008, -15.908], [-39.5455, -15.9437], [-39.587, -15.9828], [-39.625, -16.0252], [-39.6592, -16.0704], [-39.6963, -16.1306], [-39.7211, -16.1813], [-39.7459, -16.2471], [-39.7605, -16.3014], [-39.7704, -16.3566], [-39.776, -16.4265], [-39.7739, -16.4965], [-39.7668, -16.5522], [-39.7549, -16.6071], [-39.735, -16.6697], [-39.9193, -17.0413], [-39.7218, -17.2358], [-39.3271, -17.4185], [-39.1216, -17.1104], [-39.0388, -17.1097], [-38.9664, -17.1017], [-38.8813, -17.0824], [-38.8128, -17.0586], [-38.7473, -17.028], [-38.6855, -16.991], [-38.6281, -16.9479], [-38.5658, -16.8889], [-38.5202, -16.8344], [-38.4807, -16.7755], [-38.4479, -16.713], [-38.4267, -16.6608], [-38.4066, -16.5934], [-38.3959, -16.5383], [-38.3901, -16.4826], [-38.3896, -16.4125], [-38.4016, -16.3151], [-38.4282, -16.2205], [-38.4687, -16.1306], [-38.5224, -16.0474], [-38.5881, -15.9727], [-38.6642, -15.908], [-38.7493, -15.8548], [-38.8381, -15.8153], [-38.823611, -15.649444]]},
    {"tipo": "tma", "id": "SBWL", "nome": "Ilhéus TMA", "posicao": "SBWL_APP", "freq": "120.100", "lim": "FL035 – FL195", "classe": "A/D", "link": "SBWL/", "contorno": [[-38.416389, -13.941389], [-38.556389, -14.320833], [-38.477222, -14.406111], [-38.41, -14.51], [-38.369167, -14.61], [-38.333611, -14.734167], [-38.330833, -14.869722], [-38.351944, -14.995], [-38.355215, -15.003454], [-38.396667, -15.110556], [-38.467222, -15.2225], [-38.546667, -15.308889], [-38.632222, -15.381667], [-38.709167, -15.421667], [-38.799722, -15.463333], [-38.823611, -15.649444], [-39.374722, -15.609722], [-39.350278, -15.422222], [-39.472778, -15.346389], [-39.565, -15.255278], [-39.580833, -15.234611], [-39.627778, -15.172778], [-39.675, -15.075], [-39.714722, -14.955556], [-39.728611, -14.822778], [-39.715278, -14.683889], [-39.691389, -14.579167], [-39.663583, -14.52576], [-39.642222, -14.484722], [-39.568611, -14.380556], [-39.448333, -14.271667], [-39.344722, -14.21], [-39.203056, -14.163333], [-39.07, -14.141111], [-38.931389, -13.757778], [-38.416389, -13.941389]]},
    {"tipo": "tma", "id": "SBXM", "nome": "Maceió TMA", "posicao": "SBXM_APP", "freq": "119.250", "lim": "3500 FT – FL195", "classe": "A/C", "link": "SBXM/", "contorno": [[-35.127222, -8.987778], [-35.226944, -9.141667], [-35.158056, -9.250278], [-35.116944, -9.384444], [-35.096667, -9.5075], [-35.111667, -9.656667], [-35.154167, -9.791111], [-35.218611, -9.912222], [-35.283889, -9.991667], [-35.373333, -10.071667], [-35.504444, -10.151111], [-35.651389, -10.196944], [-35.816111, -10.209167], [-35.998333, -10.175278], [-36.221667, -10.433611], [-36.631944, -10.091389], [-36.406111, -9.823889], [-36.445278, -9.718889], [-36.465833, -9.636389], [-36.471389, -9.513056], [-36.457778, -9.383056], [-36.406111, -9.234444], [-36.331111, -9.113889], [-36.229444, -9.009444], [-36.11, -8.928056], [-35.982222, -8.877778], [-35.833889, -8.849444], [-35.684444, -8.853889], [-35.585, -8.705], [-35.127222, -8.987778]]},
    {"tipo": "tma", "id": "SBXR", "nome": "Vitória TMA", "posicao": "SBXR_APP", "freq": "119.850", "lim": "4500 FT – FL195", "classe": "A/C", "link": "SBXR/", "contorno": [[-39.8122, -20.745], [-40.007222, -20.866389], [-40.251833, -20.947333], [-40.348833, -20.933333], [-40.409614, -20.924606], [-40.5675, -20.901667], [-40.674833, -20.807667], [-40.8205, -20.694833], [-40.975556, -20.406111], [-40.989444, -20.189167], [-40.906667, -19.929722], [-40.729444, -19.730833], [-40.606389, -19.644167], [-40.331389, -19.591111], [-40.0325, -19.623611], [-39.890667, -19.692667], [-39.779667, -19.779167], [-39.7295, -19.832333], [-39.663667, -19.925], [-39.611389, -20.038333], [-39.574444, -20.276389], [-39.678, -20.598], [-39.8122, -20.745]]},
    {"tipo": "tma", "id": "SBXE", "nome": "Teresina TMA", "posicao": "SBXE_APP", "freq": "119.600", "lim": "3500 FT – FL195", "classe": "A/D", "link": "SBXE/", "contorno": [[-42.983739, -4.4197], [-42.898206, -4.409887], [-42.782062, -4.400706], [-42.682754, -4.416889], [-42.587951, -4.44411], [-42.505085, -4.479395], [-42.416362, -4.542701], [-42.332144, -4.617044], [-42.282161, -4.690533], [-42.211457, -4.797989], [-42.190566, -4.889799], [-42.158675, -5.028807], [-42.168696, -5.127511], [-42.182115, -5.239836], [-42.239097, -5.358275], [-42.263344, -5.404994], [-42.299795, -5.475227], [-42.374101, -5.546079], [-42.444691, -5.618417], [-42.562091, -5.667753], [-42.639251, -5.703225], [-42.772549, -5.722663], [-42.913599, -5.724021], [-43.056395, -5.692583], [-43.132222, -5.666533], [-43.233915, -5.58734], [-43.318921, -5.525521], [-43.374441, -5.439118], [-43.439609, -5.344576], [-43.472362, -5.239461], [-43.492859, -5.141389], [-43.493592, -5.031963], [-43.480174, -4.919638], [-43.452359, -4.84089], [-43.424225, -4.777248], [-43.386389, -4.703611], [-43.182572, -4.510323], [-43.110165, -4.468477], [-42.997982, -4.421334], [-42.983739, -4.4197]]},
    {"tipo": "ctr", "id": "SBWZ", "nome": "Fortaleza CTR", "posicao": "SBFZ_TWR", "freq": "129.000", "lim": "GND – FL035", "classe": "C", "link": "SBWZ/", "contorno": [[-38.073889, -3.587778], [-38.851667, -3.379722], [-39.000556, -3.937222], [-38.221667, -4.146389], [-38.073889, -3.587778]]},
    {"tipo": "ctr", "id": "SBXS", "nome": "Salvador CTR", "posicao": "SBSV_TWR", "freq": "118.300", "lim": "GND – FL035", "classe": "C", "link": "SBXS/", "contorno": [[-38.321944, -12.571944], [-38.378889, -12.580278], [-38.446389, -12.600278], [-38.508056, -12.631111], [-38.568611, -12.683333], [-38.6125, -12.742222], [-38.646667, -12.825278], [-38.657778, -12.911389], [-38.648056, -13.001111], [-38.605556, -13.088056], [-38.546667, -13.159167], [-38.468333, -13.207222], [-38.395556, -13.235278], [-38.312778, -13.244444], [-38.237222, -13.238611], [-38.164444, -13.216111], [-38.095833, -13.175833], [-38.046667, -13.12], [-38.005278, -13.055833], [-37.979167, -12.983889], [-37.970833, -12.906111], [-37.977778, -12.833889], [-38.005833, -12.760833], [-38.051111, -12.695278], [-38.111667, -12.640278], [-38.187222, -12.5975], [-38.257222, -12.578611], [-38.321944, -12.571944]]},
    {"tipo": "ctr", "id": "SBXT", "nome": "Natal CTR", "posicao": "SBNT_TWR", "freq": "118.700", "lim": "GND – FL035", "classe": "C", "link": "SBXT/", "contorno": [[-35.218889, -5.571944], [-35.154722, -5.586944], [-35.083056, -5.612778], [-35.015833, -5.661944], [-34.962222, -5.7275], [-34.929444, -5.805556], [-34.912778, -5.884722], [-34.915556, -5.9575], [-34.940278, -6.046111], [-34.983056, -6.119167], [-35.035, -6.172222], [-35.101111, -6.211944], [-35.138056, -6.231111], [-35.206944, -6.246111], [-35.274167, -6.246111], [-35.334722, -6.237778], [-35.399167, -6.211944], [-35.458333, -6.175], [-35.510556, -6.121944], [-35.5475, -6.056389], [-35.568611, -5.993889], [-35.5825, -5.924167], [-35.574167, -5.849167], [-35.557778, -5.7825], [-35.523889, -5.720278], [-35.477222, -5.665556], [-35.427778, -5.624444], [-35.360556, -5.588889], [-35.284722, -5.573333], [-35.218889, -5.571944]]},
    {"tipo": "ctr", "id": "SBWF", "nome": "Recife CTR", "posicao": "SBRF_TWR", "freq": "118.350", "lim": "GND – FL035", "classe": "C", "link": "SBWF/", "contorno": [[-35.245278, -7.811111], [-34.858056, -7.682222], [-34.616667, -8.394722], [-35.014167, -8.528333], [-35.245278, -7.811111]]},
    {"tipo": "ctr", "id": "SBXR", "nome": "Vitória CTR", "posicao": "SBVT_TWR", "freq": "118.100", "lim": "GND – FL045", "classe": "C", "link": "SBXR/", "contorno": [[-40.305, -20.014722], [-40.376111, -20.031944], [-40.465278, -20.078333], [-40.520278, -20.149167], [-40.547778, -20.240833], [-40.536944, -20.337222], [-40.498333, -20.411944], [-40.426944, -20.475], [-40.339167, -20.511111], [-40.268333, -20.514167], [-40.186667, -20.499444], [-40.104722, -20.460278], [-40.048333, -20.395833], [-40.018611, -20.320833], [-40.011944, -20.238333], [-40.036667, -20.154722], [-40.090278, -20.081111], [-40.156111, -20.045], [-40.223889, -20.014722], [-40.305, -20.014722]]},
    {"tipo": "ctr", "id": "SBWK", "nome": "Porto Seguro CTR", "posicao": "SBPS_TWR", "freq": "118.850", "lim": "GND – FL035", "classe": "C", "link": "SBWK/", "contorno": [[-39.100556, -16.1925], [-39.173889, -16.211667], [-39.249444, -16.255278], [-39.304444, -16.3225], [-39.331944, -16.401389], [-39.331944, -16.4925], [-39.2975, -16.581944], [-39.233056, -16.650278], [-39.153333, -16.685833], [-39.062778, -16.697222], [-39.002222, -16.689722], [-38.930833, -16.658333], [-38.870556, -16.609444], [-38.825278, -16.533889], [-38.812778, -16.448333], [-38.825278, -16.365556], [-38.869167, -16.288889], [-38.935, -16.231111], [-39.018333, -16.201944], [-39.100556, -16.1925]]},
    {"tipo": "ctr", "id": "SBXA", "nome": "Aracaju CTR", "posicao": "SBAR_TWR", "freq": "118.800", "lim": "GND – FL035", "classe": "D", "link": "SBXA/", "contorno": [[-36.928333, -10.782222], [-36.871944, -10.829444], [-36.829444, -10.898056], [-36.808889, -10.978889], [-36.818333, -11.076111], [-36.855556, -11.142222], [-36.906389, -11.196111], [-36.968056, -11.229722], [-37.036667, -11.25], [-37.091667, -11.248611], [-37.156389, -11.231111], [-37.214722, -11.201667], [-37.264444, -11.153889], [-37.305833, -11.083889], [-37.322222, -11.009722], [-37.316667, -10.9475], [-37.292222, -10.881944], [-37.249722, -10.820556], [-37.196389, -10.778611], [-37.1275, -10.750278], [-37.045278, -10.745], [-36.986111, -10.756667], [-36.928333, -10.782222]]},
    {"tipo": "ctr", "id": "SBXM", "nome": "Maceió CTR", "posicao": "SBMO_TWR", "freq": "118.250", "lim": "GND – FL035", "classe": "D", "link": "SBXM/", "contorno": [[-35.625, -9.338333], [-35.579722, -9.381667], [-35.545556, -9.438611], [-35.531667, -9.509167], [-35.531667, -9.578056], [-35.549444, -9.648611], [-35.596389, -9.708056], [-35.648333, -9.7475], [-35.710278, -9.777222], [-35.778889, -9.786667], [-35.873611, -9.770278], [-35.951944, -9.725833], [-36.005556, -9.662222], [-36.034444, -9.580833], [-36.037222, -9.49], [-36.002778, -9.403333], [-35.942222, -9.334167], [-35.855833, -9.293611], [-35.771944, -9.282778], [-35.691111, -9.299167], [-35.625, -9.338333]]},
    {"tipo": "ctr", "id": "SBWL", "nome": "Ilhéus CTR", "posicao": "SBIL_R_TWR", "freq": "120.100", "lim": "GND – FL035", "classe": "D", "link": "SBWL/", "contorno": [[-39.033889, -14.555833], [-39.104722, -14.567778], [-39.166389, -14.591667], [-39.224167, -14.635556], [-39.270833, -14.704444], [-39.285833, -14.793611], [-39.266667, -14.893056], [-39.208889, -14.981944], [-39.121111, -15.036389], [-39.038889, -15.0525], [-38.952222, -15.041667], [-38.882222, -15.011111], [-38.820278, -14.956667], [-38.775278, -14.865556], [-38.768611, -14.771111], [-38.790556, -14.695556], [-38.845278, -14.631667], [-38.914167, -14.583889], [-38.977778, -14.561111], [-39.033889, -14.555833]]},
    {"tipo": "ctr", "id": "SBWF", "nome": "João Pessoa CTR", "posicao": "SBJP_TWR", "freq": "118.300", "lim": "GND – FL035", "classe": "D", "link": "SBWF/", "contorno": [[-34.864444, -6.911389], [-34.932778, -6.901389], [-34.976667, -6.9], [-35.033333, -6.913611], [-35.08, -6.938056], [-35.122778, -6.966667], [-35.161111, -7.015833], [-35.180278, -7.062222], [-35.199444, -7.119444], [-35.199444, -7.178056], [-35.185556, -7.240833], [-35.154167, -7.298056], [-35.119722, -7.340278], [-35.061944, -7.378333], [-35.003056, -7.398889], [-34.934444, -7.405833], [-34.876944, -7.393056], [-34.826111, -7.375556], [-34.7875, -7.346944], [-34.743611, -7.304722], [-34.7175, -7.25], [-34.701111, -7.200278], [-34.696944, -7.131667], [-34.709444, -7.072222], [-34.739444, -7.009444], [-34.791667, -6.956111], [-34.864444, -6.911389]]},
    {"tipo": "ctr", "id": "SBXE", "nome": "Teresina CTR", "posicao": "SBTE_TWR", "freq": "118.800", "lim": "GND – FL035", "classe": "D", "link": "SBXE/", "contorno": [[-42.806389, -4.814444], [-42.891944, -4.828333], [-42.9675, -4.870833], [-43.023889, -4.929722], [-43.052778, -5.005], [-43.059722, -5.101944], [-43.0375, -5.188333], [-42.982778, -5.255278], [-42.912778, -5.301667], [-42.820556, -5.320833], [-42.747778, -5.311389], [-42.664167, -5.275833], [-42.606389, -5.212778], [-42.569444, -5.144444], [-42.558333, -5.058333], [-42.576111, -4.983056], [-42.607778, -4.918611], [-42.669722, -4.861111], [-42.730833, -4.826667], [-42.806389, -4.814444]]}
];

const limiteFir = [[-35.4608, -1.7439], [-36.2217, -1.3619], [-37.9531, -0.4917], [-39, 0], [-39.9331, 0.5036], [-40.7822, 0.9303], [-41.7, -1.7569], [-41.8556, -2.1744], [-42.086944, -2.855278], [-42.1475, -3.03], [-42.368056, -3.686111], [-42.523889, -4.176944], [-42.979444, -4.398611], [-43.157778, -4.485278], [-43.182573, -4.510323], [-43.386389, -4.703611], [-44.201389, -6.094444], [-44.796667, -6.304444], [-45.780278, -8.143611], [-46.672222, -8.86], [-47.150833, -9.530556], [-47.315278, -10.328611], [-46.934722, -11.848889], [-46.891111, -12.021944], [-45.62204, -13.306131], [-45.278124, -13.796406], [-45.010227, -14.217837], [-44.580004, -14.779477], [-44.251448, -15.354465], [-44.095833, -15.626499], [-42.819853, -16.378574], [-42.337778, -16.624722], [-41.820556, -16.948333], [-42.448056, -18.758056], [-42.440556, -19.105], [-42.479444, -19.463056], [-42.526944, -20.003333], [-42.752222, -20.411667], [-42.594444, -20.460833], [-42.316668, -20.533343], [-42.000004, -20.61667], [-41.400004, -20.48334], [-40.975556, -20.406111], [-40.8205, -20.694833], [-40.674833, -20.807667], [-40.5675, -20.901667], [-40.409614, -20.924606], [-40.348833, -20.933333], [-40.251833, -20.947333], [-40.007222, -20.866389], [-39.8122, -20.745], [-39.678, -20.598], [-39.6257, -20.5074], [-38.3444, -19.7896], [-37.6728, -18.8625], [-38.2428, -18.6793], [-37.6216, -17.4696], [-37.0281, -16.2961], [-35.8551, -14.6957], [-35.0828, -13.6253], [-34.4171, -12.7023], [-33.7561, -11.7775], [-32.9956, -10.7084], [-31.8644, -9.1011], [-30.1192, -6.5894], [-28.3914, -4.0714], [-29.2432, -3.6192], [-31.2094, -3.3882], [-32.1211, -3.2717], [-33.5089, -2.6381], [-34.8803, -2.0189]];

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
