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

        // Camada base clara (Mapbox, ou Stadia sem token) — ver overrides/main.html
        camadaMapbox('claro', { maxZoom: 20 }).addTo(map);

        // Dados dos aeródromos formatados
        var airports = [
    {
        "icao": "SBAC",
        "name": "Aracati",
        "lat": -4.5686,
        "lon": -37.8047,
        "link": "sbre-recife/afis/SBAC/"
    },
    {
        "icao": "SBAE",
        "name": "Bauru / Arealva",
        "lat": -22.1578,
        "lon": -49.0683,
        "link": "sbbs-brasilia/afis/SBAE/"
    },
    {
        "icao": "SBAF",
        "name": "Afonsos",
        "lat": -22.8756,
        "lon": -43.3844,
        "link": "sbcw-curitiba/afis/SBAF/"
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
        "icao": "SBBG",
        "name": "Bagé",
        "lat": -31.3908,
        "lon": -54.1097,
        "link": "sbcw-curitiba/afis/SBBG/"
    },
    {
        "icao": "SBBH",
        "name": "Pampulha",
        "lat": -19.851,
        "lon": -43.951,
        "link": "sbbs-brasilia/twr/SBBH/"
    },
    {
        "icao": "SBBI",
        "name": "Bacacheri",
        "lat": -25.4033,
        "lon": -49.2336,
        "link": "sbcw-curitiba/twr/SBBI/"
    },
    {
        "icao": "SBBP",
        "name": "Bragança Paulista",
        "lat": -22.9789,
        "lon": -46.5372,
        "link": "sbcw-curitiba/afis/SBBP/"
    },
    {
        "icao": "SBBQ",
        "name": "Barbacena",
        "lat": -21.2672,
        "lon": -43.7606,
        "link": "sbcw-curitiba/afis/SBBQ/"
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
        "icao": "SBCA",
        "name": "Cascavel",
        "lat": -25.0022,
        "lon": -53.5019,
        "link": "sbcw-curitiba/afis/SBCA/"
    },
    {
        "icao": "SBCB",
        "name": "Cabo Frio",
        "lat": -22.9208,
        "lon": -42.0714,
        "link": "sbcw-curitiba/afis/SBCB/"
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
        "icao": "SBCG",
        "name": "Campo Grande",
        "lat": -20.4694,
        "lon": -54.6703,
        "link": "sbcw-curitiba/twr/SBCG/"
    },
    {
        "icao": "SBCH",
        "name": "Chapecó",
        "lat": -27.1339,
        "lon": -52.6589,
        "link": "sbcw-curitiba/afis/SBCH/"
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
        "icao": "SBCO",
        "name": "Canoas",
        "lat": -29.9456,
        "lon": -51.1436,
        "link": "sbcw-curitiba/twr/SBCO/"
    },
    {
        "icao": "SBCP",
        "name": "Campos",
        "lat": -21.7011,
        "lon": -41.3078,
        "link": "sbcw-curitiba/afis/SBCP/"
    },
    {
        "icao": "SBCR",
        "name": "Corumbá",
        "lat": -19.0119,
        "lon": -57.6714,
        "link": "sbcw-curitiba/afis/SBCR/"
    },
    {
        "icao": "SBCT",
        "name": "Curitiba",
        "lat": -25.5311,
        "lon": -49.1729,
        "link": "sbcw-curitiba/twr/SBCT/"
    },
    {
        "icao": "SBCX",
        "name": "Caxias do Sul",
        "lat": -29.1981,
        "lon": -51.1867,
        "link": "sbcw-curitiba/afis/SBCX/"
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
        "icao": "SBDB",
        "name": "Bonito",
        "lat": -21.2472,
        "lon": -56.4525,
        "link": "sbcw-curitiba/afis/SBDB/"
    },
    {
        "icao": "SBDN",
        "name": "Presidente Prudente",
        "lat": -22.175,
        "lon": -51.4244,
        "link": "sbcw-curitiba/twr/SBDN/"
    },
    {
        "icao": "SBDO",
        "name": "Dourados",
        "lat": -22.2006,
        "lon": -54.9256,
        "link": "sbcw-curitiba/afis/SBDO/"
    },
    {
        "icao": "SBEG",
        "name": "Eduardo Gomes",
        "lat": -3.0384,
        "lon": -60.047,
        "link": "sbaz-amazonica/twr/SBEG/"
    },
    {
        "icao": "SBES",
        "name": "São Pedro da Aldeia",
        "lat": -22.8167,
        "lon": -42.0925,
        "link": "sbcw-curitiba/twr/SBES/"
    },
    {
        "icao": "SBFI",
        "name": "Foz do Iguaçu",
        "lat": -25.6003,
        "lon": -54.485,
        "link": "sbcw-curitiba/twr/SBFI/"
    },
    {
        "icao": "SBFL",
        "name": "Florianópolis",
        "lat": -27.6703,
        "lon": -48.5525,
        "link": "sbcw-curitiba/twr/SBFL/"
    },
    {
        "icao": "SBFN",
        "name": "Fernando de Noronha",
        "lat": -3.8547,
        "lon": -32.4283,
        "link": "sbre-recife/afis/SBFN/"
    },
    {
        "icao": "SBFS",
        "name": "Farol de São Tomé",
        "lat": -22.0306,
        "lon": -41.0686,
        "link": "sbcw-curitiba/afis/SBFS/"
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
        "icao": "SBGV",
        "name": "Governador Valadares",
        "lat": -18.8961,
        "lon": -41.9833,
        "link": "sbre-recife/afis/SBGV/"
    },
    {
        "icao": "SBGW",
        "name": "Guaratinguetá",
        "lat": -22.7917,
        "lon": -45.2044,
        "link": "sbcw-curitiba/twr/SBGW/"
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
        "icao": "SBJA",
        "name": "Jaguaruna",
        "lat": -28.6753,
        "lon": -49.0603,
        "link": "sbcw-curitiba/afis/SBJA/"
    },
    {
        "icao": "SBJD",
        "name": "Jundiaí",
        "lat": -23.1817,
        "lon": -46.9436,
        "link": "sbcw-curitiba/twr/SBJD/"
    },
    {
        "icao": "SBJE",
        "name": "Jericoacoara",
        "lat": -2.9067,
        "lon": -40.3581,
        "link": "sbre-recife/afis/SBJE/"
    },
    {
        "icao": "SBJH",
        "name": "Catarina",
        "lat": -23.4269,
        "lon": -47.1658,
        "link": "sbcw-curitiba/afis/SBJH/"
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
        "icao": "SBJR",
        "name": "Jacarepaguá",
        "lat": -22.9875,
        "lon": -43.37,
        "link": "sbcw-curitiba/twr/SBJR/"
    },
    {
        "icao": "SBJU",
        "name": "Juazeiro do Norte",
        "lat": -7.2192,
        "lon": -39.2694,
        "link": "sbre-recife/afis/SBJU/"
    },
    {
        "icao": "SBJV",
        "name": "Joinville",
        "lat": -26.2231,
        "lon": -48.7978,
        "link": "sbcw-curitiba/afis/SBJV/"
    },
    {
        "icao": "SBKG",
        "name": "Campina Grande",
        "lat": -7.2692,
        "lon": -35.895,
        "link": "sbre-recife/afis/SBKG/"
    },
    {
        "icao": "SBKP",
        "name": "Viracopos",
        "lat": -23.0069,
        "lon": -47.1344,
        "link": "sbcw-curitiba/twr/SBKP/"
    },
    {
        "icao": "SBLO",
        "name": "Londrina",
        "lat": -23.3303,
        "lon": -51.1367,
        "link": "sbcw-curitiba/twr/SBLO/"
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
        "icao": "SBME",
        "name": "Macaé",
        "lat": -22.3417,
        "lon": -41.7661,
        "link": "sbcw-curitiba/twr/SBME/"
    },
    {
        "icao": "SBMG",
        "name": "Maringá",
        "lat": -23.4764,
        "lon": -52.0178,
        "link": "sbcw-curitiba/twr/SBMG/"
    },
    {
        "icao": "SBMI",
        "name": "Maricá",
        "lat": -22.9181,
        "lon": -42.8289,
        "link": "sbcw-curitiba/afis/SBMI/"
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
        "icao": "SBMS",
        "name": "Mossoró",
        "lat": -5.1958,
        "lon": -37.3617,
        "link": "sbre-recife/afis/SBMS/"
    },
    {
        "icao": "SBMT",
        "name": "Campo de Marte",
        "lat": -23.5092,
        "lon": -46.6375,
        "link": "sbcw-curitiba/twr/SBMT/"
    },
    {
        "icao": "SBNF",
        "name": "Navegantes",
        "lat": -26.8786,
        "lon": -48.6508,
        "link": "sbcw-curitiba/twr/SBNF/"
    },
    {
        "icao": "SBNM",
        "name": "Santo Ângelo",
        "lat": -28.2817,
        "lon": -54.1683,
        "link": "sbcw-curitiba/afis/SBNM/"
    },
    {
        "icao": "SBNT",
        "name": "Natal",
        "lat": -5.9083,
        "lon": -35.2492,
        "link": "sbre-recife/twr/SBNT/"
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
        "icao": "SBPA",
        "name": "Porto Alegre",
        "lat": -29.9947,
        "lon": -51.1711,
        "link": "sbcw-curitiba/twr/SBPA/"
    },
    {
        "icao": "SBPB",
        "name": "Parnaíba",
        "lat": -2.8933,
        "lon": -41.7303,
        "link": "sbre-recife/afis/SBPB/"
    },
    {
        "icao": "SBPF",
        "name": "Passo Fundo",
        "lat": -28.2442,
        "lon": -52.3283,
        "link": "sbcw-curitiba/afis/SBPF/"
    },
    {
        "icao": "SBPG",
        "name": "Ponta Grossa",
        "lat": -25.1844,
        "lon": -50.1439,
        "link": "sbcw-curitiba/afis/SBPG/"
    },
    {
        "icao": "SBPJ",
        "name": "Palmas",
        "lat": -10.2923,
        "lon": -48.3563,
        "link": "sbbs-brasilia/twr/SBPJ/"
    },
    {
        "icao": "SBPK",
        "name": "Pelotas",
        "lat": -31.7161,
        "lon": -52.3311,
        "link": "sbcw-curitiba/afis/SBPK/"
    },
    {
        "icao": "SBPL",
        "name": "Petrolina",
        "lat": -9.3675,
        "lon": -40.5636,
        "link": "sbre-recife/afis/SBPL/"
    },
    {
        "icao": "SBPO",
        "name": "Pato Branco",
        "lat": -26.2172,
        "lon": -52.6944,
        "link": "sbcw-curitiba/afis/SBPO/"
    },
    {
        "icao": "SBPP",
        "name": "Ponta Porã",
        "lat": -22.5497,
        "lon": -55.7031,
        "link": "sbcw-curitiba/afis/SBPP/"
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
        "icao": "SBPW",
        "name": "Porto do Açu",
        "lat": -21.8042,
        "lon": -41.1089,
        "link": "sbcw-curitiba/afis/SBPW/"
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
        "icao": "SBSC",
        "name": "Santa Cruz",
        "lat": -22.9328,
        "lon": -43.7194,
        "link": "sbcw-curitiba/twr/SBSC/"
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
        "icao": "SBSJ",
        "name": "São José dos Campos",
        "lat": -23.2289,
        "lon": -45.8711,
        "link": "sbcw-curitiba/twr/SBSJ/"
    },
    {
        "icao": "SBSL",
        "name": "São Luis",
        "lat": -2.5862,
        "lon": -44.2354,
        "link": "sbaz-amazonica/twr/SBSL/"
    },
    {
        "icao": "SBSM",
        "name": "Santa Maria",
        "lat": -29.7108,
        "lon": -53.6922,
        "link": "sbcw-curitiba/twr/SBSM/"
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
        "icao": "SBST",
        "name": "Santos",
        "lat": -23.9281,
        "lon": -46.2997,
        "link": "sbcw-curitiba/afis/SBST/"
    },
    {
        "icao": "SBSV",
        "name": "Salvador",
        "lat": -12.9097,
        "lon": -38.3278,
        "link": "sbre-recife/twr/SBSV/"
    },
    {
        "icao": "SBTA",
        "name": "Taubaté",
        "lat": -23.0389,
        "lon": -45.5158,
        "link": "sbcw-curitiba/twr/SBTA/"
    },
    {
        "icao": "SBTB",
        "name": "Trombetas",
        "lat": -2.5975,
        "lon": -56.1264,
        "link": "sbaz-amazonica/afis/SBTB/"
    },
    {
        "icao": "SBTC",
        "name": "Una / Comandatuba",
        "lat": -15.3533,
        "lon": -38.9972,
        "link": "sbre-recife/afis/SBTC/"
    },
    {
        "icao": "SBTD",
        "name": "Toledo",
        "lat": -24.6853,
        "lon": -53.6964,
        "link": "sbcw-curitiba/afis/SBTD/"
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
        "icao": "SBTG",
        "name": "Três Lagoas",
        "lat": -20.7514,
        "lon": -51.6803,
        "link": "sbcw-curitiba/afis/SBTG/"
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
        "icao": "SBTV",
        "name": "Terravista",
        "lat": -16.5414,
        "lon": -39.1081,
        "link": "sbre-recife/afis/SBTV/"
    },
    {
        "icao": "SBUA",
        "name": "São Gabriel da Cachoeira",
        "lat": -0.1509,
        "lon": -66.988,
        "link": "sbaz-amazonica/afis/SBUA/"
    },
    {
        "icao": "SBUF",
        "name": "Paulo Afonso",
        "lat": -9.4011,
        "lon": -38.2511,
        "link": "sbre-recife/afis/SBUF/"
    },
    {
        "icao": "SBUG",
        "name": "Uruguaiana",
        "lat": -29.7833,
        "lon": -57.0369,
        "link": "sbcw-curitiba/afis/SBUG/"
    },
    {
        "icao": "SBUY",
        "name": "Urucu",
        "lat": -4.8837,
        "lon": -65.3539,
        "link": "sbaz-amazonica/afis/SBUY/"
    },
    {
        "icao": "SBVC",
        "name": "Vitória da Conquista",
        "lat": -14.9078,
        "lon": -40.9147,
        "link": "sbre-recife/afis/SBVC/"
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
        "icao": "SBZM",
        "name": "Goianá",
        "lat": -21.5131,
        "lon": -43.1731,
        "link": "sbcw-curitiba/afis/SBZM/"
    },
    {
        "icao": "SDAM",
        "name": "Campos dos Amarais",
        "lat": -22.8592,
        "lon": -47.1081,
        "link": "sbcw-curitiba/afis/SDAM/"
    },
    {
        "icao": "SDCO",
        "name": "Sorocaba",
        "lat": -23.4778,
        "lon": -47.49,
        "link": "sbcw-curitiba/twr/SDCO/"
    },
    {
        "icao": "SIMK",
        "name": "Franca",
        "lat": -22.3789,
        "lon": -47.0136,
        "link": "sbbs-brasilia/afis/SIMK/"
    },
    {
        "icao": "SNCP",
        "name": "Correia Pinto",
        "lat": -27.6342,
        "lon": -50.3583,
        "link": "sbcw-curitiba/afis/SNCP/"
    },
    {
        "icao": "SSGG",
        "name": "Guarapuava",
        "lat": -25.3883,
        "lon": -51.5236,
        "link": "sbcw-curitiba/afis/SSGG/"
    },
    {
        "icao": "SSKW",
        "name": "Cacoal",
        "lat": -19.4633,
        "lon": -42.4839,
        "link": "sbaz-amazonica/afis/SSKW/"
    },
    {
        "icao": "SSVL",
        "name": "Telêmaco Borba",
        "lat": -24.3164,
        "lon": -50.6522,
        "link": "sbcw-curitiba/afis/SSVL/"
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
| [SBAT - Alta Floresta](sbaz-amazonica/afis/SBAT/) | [SBAE - Bauru / Arealva](sbbs-brasilia/afis/SBAE/) | [SBAF - Afonsos](sbcw-curitiba/afis/SBAF/) | [SBAC - Aracati](sbre-recife/afis/SBAC/) |
| [SBBE - Belém](sbaz-amazonica/twr/SBBE/) | [SBAQ - Araraquara](sbbs-brasilia/afis/SBAQ/) | [SBBG - Bagé](sbcw-curitiba/afis/SBBG/) | [SBAR - Aracaju](sbre-recife/twr/SBAR/) |
| [SBBV - Boa Vista](sbaz-amazonica/twr/SBBV/) | [SBAU - Araçatuba](sbbs-brasilia/afis/SBAU/) | [SBBI - Bacacheri](sbcw-curitiba/twr/SBBI/) | [SBFN - Fernando de Noronha](sbre-recife/afis/SBFN/) |
| [SBCC - Cachimbo](sbaz-amazonica/afis/SBCC/) | [SBAX - Araxá](sbbs-brasilia/afis/SBAX/) | [SBBP - Bragança Paulista](sbcw-curitiba/afis/SBBP/) | [SBFZ - Fortaleza](sbre-recife/twr/SBFZ/) |
| [SBCJ - Carajás](sbaz-amazonica/afis/SBCJ/) | [SBBH - Pampulha](sbbs-brasilia/twr/SBBH/) | [SBBQ - Barbacena](sbcw-curitiba/afis/SBBQ/) | [SBGV - Governador Valadares](sbre-recife/afis/SBGV/) |
| [SBCY - Cuiabá](sbaz-amazonica/twr/SBCY/) | [SBBR - Brasília](sbbs-brasilia/twr/SBBR/) | [SBCA - Cascavel](sbcw-curitiba/afis/SBCA/) | [SBIL - Ilhéus](sbre-recife/twr/SBIL/) |
| [SBCZ - Cruzeiro do Sul](sbaz-amazonica/afis/SBCZ/) | [SBBW - Barra do Garças](sbbs-brasilia/afis/SBBW/) | [SBCB - Cabo Frio](sbcw-curitiba/afis/SBCB/) | [SBJE - Jericoacoara](sbre-recife/afis/SBJE/) |
| [SBEG - Eduardo Gomes](sbaz-amazonica/twr/SBEG/) | [SBCF - Confins](sbbs-brasilia/twr/SBCF/) | [SBCG - Campo Grande](sbcw-curitiba/twr/SBCG/) | [SBJP - João Pessoa](sbre-recife/twr/SBJP/) |
| [SBGM - Guajará-Mirim](sbaz-amazonica/afis/SBGM/) | [SBCN - Caldas Novas](sbbs-brasilia/afis/SBCN/) | [SBCH - Chapecó](sbcw-curitiba/afis/SBCH/) | [SBJU - Juazeiro do Norte](sbre-recife/afis/SBJU/) |
| [SBHT - Altamira](sbaz-amazonica/afis/SBHT/) | [SBGO - Goiânia](sbbs-brasilia/twr/SBGO/) | [SBCO - Canoas](sbcw-curitiba/twr/SBCO/) | [SBKG - Campina Grande](sbre-recife/afis/SBKG/) |
| [SBIH - Itaituba](sbaz-amazonica/afis/SBIH/) | [SBGP - Gavião Peixoto](sbbs-brasilia/afis/SBGP/) | [SBCP - Campos](sbcw-curitiba/afis/SBCP/) | [SBMO - Maceió](sbre-recife/twr/SBMO/) |
| [SBIZ - Imperatriz](sbaz-amazonica/afis/SBIZ/) | [SBIP - Ipatinga](sbbs-brasilia/afis/SBIP/) | [SBCR - Corumbá](sbcw-curitiba/afis/SBCR/) | [SBMS - Mossoró](sbre-recife/afis/SBMS/) |
| [SBJI - Ji-Paraná](sbaz-amazonica/afis/SBJI/) | [SBIT - Itumbiara](sbbs-brasilia/afis/SBIT/) | [SBCT - Curitiba](sbcw-curitiba/twr/SBCT/) | [SBNT - Natal](sbre-recife/twr/SBNT/) |
| [SBMA - Marabá](sbaz-amazonica/afis/SBMA/) | [SBLS - Lagoa Santa](sbbs-brasilia/afis/SBLS/) | [SBCX - Caxias do Sul](sbcw-curitiba/afis/SBCX/) | [SBPB - Parnaíba](sbre-recife/afis/SBPB/) |
| [SBMN - Ponta Pelada](sbaz-amazonica/twr/SBMN/) | [SBMK - Montes Claros](sbbs-brasilia/afis/SBMK/) | [SBDB - Bonito](sbcw-curitiba/afis/SBDB/) | [SBPL - Petrolina](sbre-recife/afis/SBPL/) |
| [SBMQ - Macapá](sbaz-amazonica/twr/SBMQ/) | [SBML - Marília](sbbs-brasilia/afis/SBML/) | [SBDN - Presidente Prudente](sbcw-curitiba/twr/SBDN/) | [SBPS - Porto Seguro](sbre-recife/twr/SBPS/) |
| [SBOI - Oiapoque](sbaz-amazonica/afis/SBOI/) | [SBNV - A.N.A.](sbbs-brasilia/afis/SBNV/) | [SBDO - Dourados](sbcw-curitiba/afis/SBDO/) | [SBRF - Recife](sbre-recife/twr/SBRF/) |
| [SBPV - Porto Velho](sbaz-amazonica/twr/SBPV/) | [SBPJ - Palmas](sbbs-brasilia/twr/SBPJ/) | [SBES - São Pedro da Aldeia](sbcw-curitiba/twr/SBES/) | [SBSG - São Gonçalo do Amarante](sbre-recife/twr/SBSG/) |
| [SBRB - Rio Branco](sbaz-amazonica/twr/SBRB/) | [SBSR - Rio Preto](sbbs-brasilia/afis/SBSR/) | [SBFI - Foz do Iguaçu](sbcw-curitiba/twr/SBFI/) | [SBSV - Salvador](sbre-recife/twr/SBSV/) |
| [SBRD - Rondonópolis](sbaz-amazonica/afis/SBRD/) | [SBVG - Varginha](sbbs-brasilia/afis/SBVG/) | [SBFL - Florianópolis](sbcw-curitiba/twr/SBFL/) | [SBTC - Una / Comandatuba](sbre-recife/afis/SBTC/) |
| [SBSI - Sinop](sbaz-amazonica/afis/SBSI/) | [SIMK - Franca](sbbs-brasilia/afis/SIMK/) | [SBFS - Farol de São Tomé](sbcw-curitiba/afis/SBFS/) | [SBTE - Teresina](sbre-recife/twr/SBTE/) |
| [SBSL - São Luis](sbaz-amazonica/twr/SBSL/) |  | [SBGL - Galeão](sbcw-curitiba/twr/SBGL/) | [SBTV - Terravista](sbre-recife/afis/SBTV/) |
| [SBSN - Santarém](sbaz-amazonica/twr/SBSN/) |  | [SBGR - Guarulhos](sbcw-curitiba/twr/SBGR/) | [SBUF - Paulo Afonso](sbre-recife/afis/SBUF/) |
| [SBSO - Sorriso](sbaz-amazonica/afis/SBSO/) |  | [SBGW - Guaratinguetá](sbcw-curitiba/twr/SBGW/) | [SBVC - Vitória da Conquista](sbre-recife/afis/SBVC/) |
| [SBTB - Trombetas](sbaz-amazonica/afis/SBTB/) |  | [SBJA - Jaguaruna](sbcw-curitiba/afis/SBJA/) | [SBVT - Vitória](sbre-recife/twr/SBVT/) |
| [SBTF - Tefé](sbaz-amazonica/afis/SBTF/) |  | [SBJD - Jundiaí](sbcw-curitiba/twr/SBJD/) |  |
| [SBTS - Tiriós](sbaz-amazonica/afis/SBTS/) |  | [SBJH - Catarina](sbcw-curitiba/afis/SBJH/) |  |
| [SBTT - Tabatinga](sbaz-amazonica/afis/SBTT/) |  | [SBJR - Jacarepaguá](sbcw-curitiba/twr/SBJR/) |  |
| [SBUA - São Gabriel da Cachoeira](sbaz-amazonica/afis/SBUA/) |  | [SBJV - Joinville](sbcw-curitiba/afis/SBJV/) |  |
| [SBUY - Urucu](sbaz-amazonica/afis/SBUY/) |  | [SBKP - Viracopos](sbcw-curitiba/twr/SBKP/) |  |
| [SBVH - Vilhena](sbaz-amazonica/afis/SBVH/) |  | [SBLO - Londrina](sbcw-curitiba/twr/SBLO/) |  |
| [SSKW - Cacoal](sbaz-amazonica/afis/SSKW/) |  | [SBME - Macaé](sbcw-curitiba/twr/SBME/) |  |
|  |  | [SBMG - Maringá](sbcw-curitiba/twr/SBMG/) |  |
|  |  | [SBMI - Maricá](sbcw-curitiba/afis/SBMI/) |  |
|  |  | [SBMT - Campo de Marte](sbcw-curitiba/twr/SBMT/) |  |
|  |  | [SBNF - Navegantes](sbcw-curitiba/twr/SBNF/) |  |
|  |  | [SBNM - Santo Ângelo](sbcw-curitiba/afis/SBNM/) |  |
|  |  | [SBPA - Porto Alegre](sbcw-curitiba/twr/SBPA/) |  |
|  |  | [SBPF - Passo Fundo](sbcw-curitiba/afis/SBPF/) |  |
|  |  | [SBPG - Ponta Grossa](sbcw-curitiba/afis/SBPG/) |  |
|  |  | [SBPK - Pelotas](sbcw-curitiba/afis/SBPK/) |  |
|  |  | [SBPO - Pato Branco](sbcw-curitiba/afis/SBPO/) |  |
|  |  | [SBPP - Ponta Porã](sbcw-curitiba/afis/SBPP/) |  |
|  |  | [SBPW - Porto do Açu](sbcw-curitiba/afis/SBPW/) |  |
|  |  | [SBRJ - Rio / Santos-Dumont](sbcw-curitiba/twr/SBRJ/) |  |
|  |  | [SBSC - Santa Cruz](sbcw-curitiba/twr/SBSC/) |  |
|  |  | [SBSJ - São José dos Campos](sbcw-curitiba/twr/SBSJ/) |  |
|  |  | [SBSM - Santa Maria](sbcw-curitiba/twr/SBSM/) |  |
|  |  | [SBSP - São Paulo / Congonhas](sbcw-curitiba/twr/SBSP/) |  |
|  |  | [SBST - Santos](sbcw-curitiba/afis/SBST/) |  |
|  |  | [SBTA - Taubaté](sbcw-curitiba/twr/SBTA/) |  |
|  |  | [SBTD - Toledo](sbcw-curitiba/afis/SBTD/) |  |
|  |  | [SBTG - Três Lagoas](sbcw-curitiba/afis/SBTG/) |  |
|  |  | [SBUG - Uruguaiana](sbcw-curitiba/afis/SBUG/) |  |
|  |  | [SBZM - Goianá](sbcw-curitiba/afis/SBZM/) |  |
|  |  | [SDAM - Campos dos Amarais](sbcw-curitiba/afis/SDAM/) |  |
|  |  | [SDCO - Sorocaba](sbcw-curitiba/twr/SDCO/) |  |
|  |  | [SNCP - Correia Pinto](sbcw-curitiba/afis/SNCP/) |  |
|  |  | [SSGG - Guarapuava](sbcw-curitiba/afis/SSGG/) |  |
|  |  | [SSVL - Telêmaco Borba](sbcw-curitiba/afis/SSVL/) |  |
