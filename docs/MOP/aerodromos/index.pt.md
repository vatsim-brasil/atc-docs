---
  title: Visão Geral
  hide:
    - toc
---

--8<-- "includes/abreviacoes.md"

Aqui você encontra instruções locais para todos os aeródromos controlados do Brasil. Apenas para fins de simulação de voo.

Clique em qualquer ponto azul no mapa abaixo para abrir diretamente o manual do aeródromo desejado.

<div id="map" style="height: 750px; width: 100%; border-radius: 12px; border: 1px solid rgba(0,0,0,0.1); margin: 20px 0; z-index: 1;"></div>

<script>
(function() {
    function initMap() {
        var mapContainer = document.getElementById('map');
        if (!mapContainer) return;
        
        // Impede reinicialização se o mapa já estiver anexado a esta div
        if (mapContainer._leaflet_id) return;

        // Inicializa o mapa focado no centro do Brasil
        var map = L.map('map').setView([-14.235, -51.9253], 4);

        // Adiciona camada de mapa (carto light para visual limpo)
        L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
            subdomains: 'abcd',
            maxZoom: 20
        }).addTo(map);

        // Dados dos aeródromos formatados
        var airports = [
    {
        "icao": "SBAE",
        "name": "Bauru / Arealva",
        "lat": -22.1578,
        "lon": -49.0683,
        "link": "sbbs-brasilia/afis/SBAE/"
    },
    {
        "icao": "SBAQ",
        "name": "Araraquara",
        "lat": -21.8081,
        "lon": -48.1347,
        "link": "sbbs-brasilia/afis/SBAQ/"
    },
    {
        "icao": "SBAR",
        "name": "Aracaju",
        "lat": -10.9839,
        "lon": -37.0709,
        "link": "sbre-recife/twr/SBAR/"
    },
    {
        "icao": "SBAT",
        "name": "Alta Floresta",
        "lat": -9.8697,
        "lon": -56.1073,
        "link": "sbaz-amazonica/afis/SBAT/"
    },
    {
        "icao": "SBAU",
        "name": "Araçatuba",
        "lat": -21.1983,
        "lon": -50.4283,
        "link": "sbbs-brasilia/afis/SBAU/"
    },
    {
        "icao": "SBAX",
        "name": "Araxá",
        "lat": -19.563,
        "lon": -46.96,
        "link": "sbbs-brasilia/afis/SBAX/"
    },
    {
        "icao": "SBBE",
        "name": "Belém",
        "lat": -1.3785,
        "lon": -48.4764,
        "link": "sbaz-amazonica/twr/SBBE/"
    },
    {
        "icao": "SBBH",
        "name": "Pampulha",
        "lat": -19.851,
        "lon": -43.951,
        "link": "sbbs-brasilia/twr/SBBH/"
    },
    {
        "icao": "SBBR",
        "name": "Brasília",
        "lat": -15.8705,
        "lon": -47.9171,
        "link": "sbbs-brasilia/twr/SBBR/"
    },
    {
        "icao": "SBBV",
        "name": "Boa Vista",
        "lat": 2.8451,
        "lon": -60.6921,
        "link": "sbaz-amazonica/twr/SBBV/"
    },
    {
        "icao": "SBBW",
        "name": "Barra do Garças",
        "lat": -15.8615,
        "lon": -52.3892,
        "link": "sbbs-brasilia/afis/SBBW/"
    },
    {
        "icao": "SBCC",
        "name": "Cachimbo",
        "lat": -9.3331,
        "lon": -54.968,
        "link": "sbaz-amazonica/afis/SBCC/"
    },
    {
        "icao": "SBCF",
        "name": "Confins",
        "lat": -19.6361,
        "lon": -43.9659,
        "link": "sbbs-brasilia/twr/SBCF/"
    },
    {
        "icao": "SBCJ",
        "name": "Carajás",
        "lat": -6.1176,
        "lon": -50.0032,
        "link": "sbaz-amazonica/afis/SBCJ/"
    },
    {
        "icao": "SBCN",
        "name": "Caldas Novas",
        "lat": -17.7431,
        "lon": -48.2831,
        "link": "sbbs-brasilia/afis/SBCN/"
    },
    {
        "icao": "SBCT",
        "name": "Curitiba",
        "lat": -25.5311,
        "lon": -49.1729,
        "link": "sbcw-curitiba/twr/SBCT/"
    },
    {
        "icao": "SBCY",
        "name": "Cuiabá",
        "lat": -15.6537,
        "lon": -56.1166,
        "link": "sbaz-amazonica/twr/SBCY/"
    },
    {
        "icao": "SBCZ",
        "name": "Cruzeiro do Sul",
        "lat": -7.5999,
        "lon": -72.7708,
        "link": "sbaz-amazonica/afis/SBCZ/"
    },
    {
        "icao": "SBEG",
        "name": "Eduardo Gomes",
        "lat": -3.0384,
        "lon": -60.047,
        "link": "sbaz-amazonica/twr/SBEG/"
    },
    {
        "icao": "SBFZ",
        "name": "Fortaleza",
        "lat": -3.7775,
        "lon": -38.5355,
        "link": "sbre-recife/twr/SBFZ/"
    },
    {
        "icao": "SBGL",
        "name": "Galeão",
        "lat": -22.8132,
        "lon": -43.2489,
        "link": "sbcw-curitiba/twr/SBGL/"
    },
    {
        "icao": "SBGM",
        "name": "Guajará-Mirim",
        "lat": -15.8611,
        "lon": -57.5758,
        "link": "sbaz-amazonica/afis/SBGM/"
    },
    {
        "icao": "SBGO",
        "name": "Goiânia",
        "lat": -16.6329,
        "lon": -49.2187,
        "link": "sbbs-brasilia/twr/SBGO/"
    },
    {
        "icao": "SBGP",
        "name": "Gavião Peixoto",
        "lat": -23.0081,
        "lon": -47.1347,
        "link": "sbbs-brasilia/afis/SBGP/"
    },
    {
        "icao": "SBGR",
        "name": "Guarulhos",
        "lat": -23.4315,
        "lon": -46.4713,
        "link": "sbcw-curitiba/twr/SBGR/"
    },
    {
        "icao": "SBHT",
        "name": "Altamira",
        "lat": -3.2506,
        "lon": -52.254,
        "link": "sbaz-amazonica/afis/SBHT/"
    },
    {
        "icao": "SBIH",
        "name": "Itaituba",
        "lat": -4.2441,
        "lon": -56.0022,
        "link": "sbaz-amazonica/afis/SBIH/"
    },
    {
        "icao": "SBIL",
        "name": "Ilhéus",
        "lat": -14.8157,
        "lon": -39.0318,
        "link": "sbre-recife/twr/SBIL/"
    },
    {
        "icao": "SBIP",
        "name": "Ipatinga",
        "lat": -19.4728,
        "lon": -42.4888,
        "link": "sbbs-brasilia/afis/SBIP/"
    },
    {
        "icao": "SBIT",
        "name": "Itumbiara",
        "lat": -21.1364,
        "lon": -48.2411,
        "link": "sbbs-brasilia/afis/SBIT/"
    },
    {
        "icao": "SBIZ",
        "name": "Imperatriz",
        "lat": -5.5302,
        "lon": -47.4587,
        "link": "sbaz-amazonica/afis/SBIZ/"
    },
    {
        "icao": "SBJI",
        "name": "Ji-Paraná",
        "lat": -10.8706,
        "lon": -61.8483,
        "link": "sbaz-amazonica/afis/SBJI/"
    },
    {
        "icao": "SBJP",
        "name": "João Pessoa",
        "lat": -7.1484,
        "lon": -34.9507,
        "link": "sbre-recife/twr/SBJP/"
    },
    {
        "icao": "SBLS",
        "name": "Lagoa Santa",
        "lat": -19.662,
        "lon": -43.896,
        "link": "sbbs-brasilia/afis/SBLS/"
    },
    {
        "icao": "SBMA",
        "name": "Marabá",
        "lat": -5.3689,
        "lon": -49.1384,
        "link": "sbaz-amazonica/afis/SBMA/"
    },
    {
        "icao": "SBMK",
        "name": "Montes Claros",
        "lat": -16.7067,
        "lon": -43.8199,
        "link": "sbbs-brasilia/afis/SBMK/"
    },
    {
        "icao": "SBML",
        "name": "Marília",
        "lat": -15.78,
        "lon": -47.93,
        "link": "sbbs-brasilia/afis/SBML/"
    },
    {
        "icao": "SBMN",
        "name": "Ponta Pelada",
        "lat": -3.146,
        "lon": -59.986,
        "link": "sbaz-amazonica/twr/SBMN/"
    },
    {
        "icao": "SBMO",
        "name": "Maceió",
        "lat": -9.5118,
        "lon": -35.7919,
        "link": "sbre-recife/twr/SBMO/"
    },
    {
        "icao": "SBMQ",
        "name": "Macapá",
        "lat": 0.0514,
        "lon": -51.0702,
        "link": "sbaz-amazonica/twr/SBMQ/"
    },
    {
        "icao": "SBNV",
        "name": "A.N.A.",
        "lat": -26.2239,
        "lon": -48.7981,
        "link": "sbbs-brasilia/afis/SBNV/"
    },
    {
        "icao": "SBOI",
        "name": "Oiapoque",
        "lat": 3.8554,
        "lon": -51.797,
        "link": "sbaz-amazonica/afis/SBOI/"
    },
    {
        "icao": "SBPJ",
        "name": "Palmas",
        "lat": -10.2923,
        "lon": -48.3563,
        "link": "sbbs-brasilia/twr/SBPJ/"
    },
    {
        "icao": "SBPS",
        "name": "Porto Seguro",
        "lat": -16.4388,
        "lon": -39.0824,
        "link": "sbre-recife/twr/SBPS/"
    },
    {
        "icao": "SBPV",
        "name": "Porto Velho",
        "lat": -8.7122,
        "lon": -63.9019,
        "link": "sbaz-amazonica/twr/SBPV/"
    },
    {
        "icao": "SBRB",
        "name": "Rio Branco",
        "lat": -9.8704,
        "lon": -67.8966,
        "link": "sbaz-amazonica/twr/SBRB/"
    },
    {
        "icao": "SBRD",
        "name": "Rondonópolis",
        "lat": -16.5028,
        "lon": -54.5822,
        "link": "sbaz-amazonica/afis/SBRD/"
    },
    {
        "icao": "SBRF",
        "name": "Recife",
        "lat": -8.1296,
        "lon": -34.9218,
        "link": "sbre-recife/twr/SBRF/"
    },
    {
        "icao": "SBRJ",
        "name": "Rio / Santos-Dumont",
        "lat": -22.91,
        "lon": -43.1625,
        "link": "sbcw-curitiba/twr/SBRJ/"
    },
    {
        "icao": "SBSG",
        "name": "São Gonçalo do Amarante",
        "lat": -5.768,
        "lon": -35.3664,
        "link": "sbre-recife/twr/SBSG/"
    },
    {
        "icao": "SBSI",
        "name": "Sinop",
        "lat": -11.8486,
        "lon": -55.4858,
        "link": "sbaz-amazonica/afis/SBSI/"
    },
    {
        "icao": "SBSL",
        "name": "São Luis",
        "lat": -2.5862,
        "lon": -44.2354,
        "link": "sbaz-amazonica/twr/SBSL/"
    },
    {
        "icao": "SBSN",
        "name": "Santarém",
        "lat": -2.4219,
        "lon": -54.7886,
        "link": "sbaz-amazonica/twr/SBSN/"
    },
    {
        "icao": "SBSO",
        "name": "Sorriso",
        "lat": -14.6536,
        "lon": -39.2789,
        "link": "sbaz-amazonica/afis/SBSO/"
    },
    {
        "icao": "SBSP",
        "name": "São Paulo / Congonhas",
        "lat": -23.6285,
        "lon": -46.6549,
        "link": "sbcw-curitiba/twr/SBSP/"
    },
    {
        "icao": "SBSR",
        "name": "Rio Preto",
        "lat": -20.8164,
        "lon": -49.4067,
        "link": "sbbs-brasilia/afis/SBSR/"
    },
    {
        "icao": "SBSV",
        "name": "Salvador",
        "lat": -12.9097,
        "lon": -38.3278,
        "link": "sbre-recife/twr/SBSV/"
    },
    {
        "icao": "SBTB",
        "name": "Trombetas",
        "lat": -2.5975,
        "lon": -56.1264,
        "link": "sbaz-amazonica/afis/SBTB/"
    },
    {
        "icao": "SBTE",
        "name": "Teresina",
        "lat": -5.0625,
        "lon": -42.8232,
        "link": "sbre-recife/twr/SBTE/"
    },
    {
        "icao": "SBTF",
        "name": "Tefé",
        "lat": -3.383,
        "lon": -64.7236,
        "link": "sbaz-amazonica/afis/SBTF/"
    },
    {
        "icao": "SBTS",
        "name": "Tiriós",
        "lat": -4.2483,
        "lon": -55.9928,
        "link": "sbaz-amazonica/afis/SBTS/"
    },
    {
        "icao": "SBTT",
        "name": "Tabatinga",
        "lat": -4.2546,
        "lon": -69.9376,
        "link": "sbaz-amazonica/afis/SBTT/"
    },
    {
        "icao": "SBUA",
        "name": "São Gabriel da Cachoeira",
        "lat": -0.1509,
        "lon": -66.988,
        "link": "sbaz-amazonica/afis/SBUA/"
    },
    {
        "icao": "SBUY",
        "name": "Urucu",
        "lat": -4.8837,
        "lon": -65.3539,
        "link": "sbaz-amazonica/afis/SBUY/"
    },
    {
        "icao": "SBVG",
        "name": "Varginha",
        "lat": -21.5647,
        "lon": -45.4578,
        "link": "sbbs-brasilia/afis/SBVG/"
    },
    {
        "icao": "SBVH",
        "name": "Vilhena",
        "lat": -12.6917,
        "lon": -60.0976,
        "link": "sbaz-amazonica/afis/SBVH/"
    },
    {
        "icao": "SBVT",
        "name": "Vitória",
        "lat": -20.258,
        "lon": -40.2818,
        "link": "sbre-recife/twr/SBVT/"
    },
    {
        "icao": "SIMK",
        "name": "Franca",
        "lat": -22.3789,
        "lon": -47.0136,
        "link": "sbbs-brasilia/afis/SIMK/"
    },
    {
        "icao": "SSKW",
        "name": "Cacoal",
        "lat": -19.4633,
        "lon": -42.4839,
        "link": "sbaz-amazonica/afis/SSKW/"
    }
];

        airports.forEach(function(ap) {
            // Marcador círculo azul na cor da VATSIM (#2483c5)
            var marker = L.circleMarker([ap.lat, ap.lon], {
                color: '#2483c5',
                fillColor: '#2483c5',
                fillOpacity: 0.85,
                radius: 7,
                weight: 2
            }).addTo(map);

            // Tooltip amigável ao passar o mouse
            marker.bindTooltip("<b>" + ap.icao + "</b> - " + ap.name, {
                direction: 'top',
                offset: [0, -5]
            });

            // Efeito de hover (aumenta o marcador)
            marker.on('mouseover', function(e) {
                this.setRadius(9);
                this.setStyle({ color: '#182061', fillColor: '#182061' });
            });
            marker.on('mouseout', function(e) {
                this.setRadius(7);
                this.setStyle({ color: '#2483c5', fillColor: '#2483c5' });
            });

            // Carrega diretamente o manual correspondente ao clicar
            marker.on('click', function() {
                window.location.href = ap.link;
            });
        });
    }

    // Gerencia o ciclo de vida tanto para SPA quanto para recarregamento total (F5)
    if (typeof document$ !== 'undefined') {
        document$.subscribe(initMap);
    } else {
        document.addEventListener("DOMContentLoaded", function() {
            if (typeof document$ !== 'undefined') {
                document$.subscribe(initMap);
            } else {
                initMap();
            }
        });
    }
})();
</script>


## Aeródromos por FIR

| SBAZ (Amazônica) | SBBS (Brasília) | SBCW (Curitiba) | SBRE (Recife) |
| :--- | :--- | :--- | :--- |
| [SBAT - Alta Floresta](sbaz-amazonica/afis/SBAT/) | [SBAE - Bauru / Arealva](sbbs-brasilia/afis/SBAE/) | [SBCT - Curitiba](sbcw-curitiba/twr/SBCT/) | [SBAR - Aracaju](sbre-recife/twr/SBAR/) |
| [SBBE - Belém](sbaz-amazonica/twr/SBBE/) | [SBAQ - Araraquara](sbbs-brasilia/afis/SBAQ/) | [SBGL - Galeão](sbcw-curitiba/twr/SBGL/) | [SBFZ - Fortaleza](sbre-recife/twr/SBFZ/) |
| [SBBV - Boa Vista](sbaz-amazonica/twr/SBBV/) | [SBAU - Araçatuba](sbbs-brasilia/afis/SBAU/) | [SBGR - Guarulhos](sbcw-curitiba/twr/SBGR/) | [SBIL - Ilhéus](sbre-recife/twr/SBIL/) |
| [SBCC - Cachimbo](sbaz-amazonica/afis/SBCC/) | [SBAX - Araxá](sbbs-brasilia/afis/SBAX/) | [SBRJ - Rio / Santos-Dumont](sbcw-curitiba/twr/SBRJ/) | [SBJP - João Pessoa](sbre-recife/twr/SBJP/) |
| [SBCJ - Carajás](sbaz-amazonica/afis/SBCJ/) | [SBBH - Pampulha](sbbs-brasilia/twr/SBBH/) | [SBSP - São Paulo / Congonhas](sbcw-curitiba/twr/SBSP/) | [SBMO - Maceió](sbre-recife/twr/SBMO/) |
| [SBCY - Cuiabá](sbaz-amazonica/twr/SBCY/) | [SBBR - Brasília](sbbs-brasilia/twr/SBBR/) |  | [SBPS - Porto Seguro](sbre-recife/twr/SBPS/) |
| [SBCZ - Cruzeiro do Sul](sbaz-amazonica/afis/SBCZ/) | [SBBW - Barra do Garças](sbbs-brasilia/afis/SBBW/) |  | [SBRF - Recife](sbre-recife/twr/SBRF/) |
| [SBEG - Eduardo Gomes](sbaz-amazonica/twr/SBEG/) | [SBCF - Confins](sbbs-brasilia/twr/SBCF/) |  | [SBSG - São Gonçalo do Amarante](sbre-recife/twr/SBSG/) |
| [SBGM - Guajará-Mirim](sbaz-amazonica/afis/SBGM/) | [SBCN - Caldas Novas](sbbs-brasilia/afis/SBCN/) |  | [SBSV - Salvador](sbre-recife/twr/SBSV/) |
| [SBHT - Altamira](sbaz-amazonica/afis/SBHT/) | [SBGO - Goiânia](sbbs-brasilia/twr/SBGO/) |  | [SBTE - Teresina](sbre-recife/twr/SBTE/) |
| [SBIH - Itaituba](sbaz-amazonica/afis/SBIH/) | [SBGP - Gavião Peixoto](sbbs-brasilia/afis/SBGP/) |  | [SBVT - Vitória](sbre-recife/twr/SBVT/) |
| [SBIZ - Imperatriz](sbaz-amazonica/afis/SBIZ/) | [SBIP - Ipatinga](sbbs-brasilia/afis/SBIP/) |  |  |
| [SBJI - Ji-Paraná](sbaz-amazonica/afis/SBJI/) | [SBIT - Itumbiara](sbbs-brasilia/afis/SBIT/) |  |  |
| [SBMA - Marabá](sbaz-amazonica/afis/SBMA/) | [SBLS - Lagoa Santa](sbbs-brasilia/afis/SBLS/) |  |  |
| [SBMN - Ponta Pelada](sbaz-amazonica/twr/SBMN/) | [SBMK - Montes Claros](sbbs-brasilia/afis/SBMK/) |  |  |
| [SBMQ - Macapá](sbaz-amazonica/twr/SBMQ/) | [SBML - Marília](sbbs-brasilia/afis/SBML/) |  |  |
| [SBOI - Oiapoque](sbaz-amazonica/afis/SBOI/) | [SBNV - A.N.A.](sbbs-brasilia/afis/SBNV/) |  |  |
| [SBPV - Porto Velho](sbaz-amazonica/twr/SBPV/) | [SBPJ - Palmas](sbbs-brasilia/twr/SBPJ/) |  |  |
| [SBRB - Rio Branco](sbaz-amazonica/twr/SBRB/) | [SBSR - Rio Preto](sbbs-brasilia/afis/SBSR/) |  |  |
| [SBRD - Rondonópolis](sbaz-amazonica/afis/SBRD/) | [SBVG - Varginha](sbbs-brasilia/afis/SBVG/) |  |  |
| [SBSI - Sinop](sbaz-amazonica/afis/SBSI/) | [SIMK - Franca](sbbs-brasilia/afis/SIMK/) |  |  |
| [SBSL - São Luis](sbaz-amazonica/twr/SBSL/) |  |  |  |
| [SBSN - Santarém](sbaz-amazonica/twr/SBSN/) |  |  |  |
| [SBSO - Sorriso](sbaz-amazonica/afis/SBSO/) |  |  |  |
| [SBTB - Trombetas](sbaz-amazonica/afis/SBTB/) |  |  |  |
| [SBTF - Tefé](sbaz-amazonica/afis/SBTF/) |  |  |  |
| [SBTS - Tiriós](sbaz-amazonica/afis/SBTS/) |  |  |  |
| [SBTT - Tabatinga](sbaz-amazonica/afis/SBTT/) |  |  |  |
| [SBUA - São Gabriel da Cachoeira](sbaz-amazonica/afis/SBUA/) |  |  |  |
| [SBUY - Urucu](sbaz-amazonica/afis/SBUY/) |  |  |  |
| [SBVH - Vilhena](sbaz-amazonica/afis/SBVH/) |  |  |  |
| [SSKW - Cacoal](sbaz-amazonica/afis/SSKW/) |  |  |  |
