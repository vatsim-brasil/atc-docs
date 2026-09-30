// Aba Meteorologia das TMAs: mapa Windy centrado na TMA, com as camadas de uso operacional.
// Cada camada declara a fonte; hoje só existe 'windy'. A REDEMET não pode ser embutida
// (frame-ancestors restrito ao decea.mil.br) e a API dela exige chave, então por ora fica como link.
document$.subscribe(({ body }) => {
    body.querySelectorAll('.tma-meteo').forEach((container) => {
        if (container.dataset.pronto) return;
        container.dataset.pronto = '1';

        const en = container.dataset.lang === 'en';
        const lat = container.dataset.lat;
        const lon = container.dataset.lon;
        const zoom = container.dataset.zoom || '8';

        const camadas = [
            { id: 'radar', fonte: 'windy', produto: 'radar', pt: 'Radar', en: 'Radar' },
            { id: 'satellite', fonte: 'windy', produto: 'satellite', pt: 'Satélite', en: 'Satellite' },
            { id: 'thunder', fonte: 'windy', pt: 'Trovoadas', en: 'Thunderstorms' },
            { id: 'wind', fonte: 'windy', niveis: true, pt: 'Vento', en: 'Wind' },
            { id: 'gust', fonte: 'windy', pt: 'Rajadas', en: 'Gusts' },
            { id: 'rain', fonte: 'windy', pt: 'Precipitação', en: 'Precipitation' },
            { id: 'lclouds', fonte: 'windy', pt: 'Nuvens baixas', en: 'Low clouds' },
            { id: 'cbase', fonte: 'windy', pt: 'Teto', en: 'Cloud base' },
            { id: 'visibility', fonte: 'windy', pt: 'Visibilidade', en: 'Visibility' },
            { id: 'cape', fonte: 'windy', pt: 'CAPE', en: 'CAPE' },
        ];

        const niveis = [
            ['surface', en ? 'Surface' : 'Superfície'],
            ['850h', 'FL050'],
            ['700h', 'FL100'],
            ['500h', 'FL180'],
            ['300h', 'FL300'],
            ['250h', 'FL340'],
            ['200h', 'FL390'],
        ];

        let atual = camadas[0];
        let nivel = 'surface';

        function urlWindy() {
            const p = new URLSearchParams({
                type: 'map',
                location: 'coordinates',
                lat, lon, zoom,
                overlay: atual.id,
                product: atual.produto || 'ecmwf',
                level: atual.niveis ? nivel : 'surface',
                metricWind: 'kt',
                metricTemp: '°C',
                metricRain: 'mm',
                calendar: 'now',
                pressure: 'true',
                message: 'true',
            });
            return 'https://embed.windy.com/embed.html?' + p.toString();
        }

        const barra = document.createElement('div');
        barra.className = 'tma-meteo-barra';

        const botoes = camadas.map((c) => {
            const b = document.createElement('button');
            b.type = 'button';
            b.className = 'tma-meteo-camada';
            b.textContent = en ? c.en : c.pt;
            b.addEventListener('click', () => {
                atual = c;
                atualizar();
            });
            barra.appendChild(b);
            return b;
        });

        const seletor = document.createElement('select');
        seletor.className = 'tma-meteo-nivel';
        seletor.setAttribute('aria-label', en ? 'Level' : 'Nível');
        niveis.forEach(([valor, rotulo]) => seletor.add(new Option(rotulo, valor)));
        seletor.addEventListener('change', () => {
            nivel = seletor.value;
            atualizar();
        });
        barra.appendChild(seletor);

        const moldura = document.createElement('div');
        moldura.className = 'tma-meteo-mapa';

        const rodape = document.createElement('div');
        rodape.className = 'tma-meteo-rodape';
        rodape.innerHTML = en
            ? 'Windy data (ECMWF model, radar and satellite composites). For official products, see <a href="https://redemet.decea.mil.br/" target="_blank" rel="noopener">REDEMET</a>.'
            : 'Dados do Windy (modelo ECMWF, mosaicos de radar e satélite). Para os produtos oficiais, consulte a <a href="https://redemet.decea.mil.br/" target="_blank" rel="noopener">REDEMET</a>.';

        container.append(barra, moldura, rodape);

        let iframe = null;

        function atualizar() {
            botoes.forEach((b, k) => b.classList.toggle('ativo', camadas[k] === atual));
            seletor.hidden = !atual.niveis;
            if (iframe) iframe.src = urlWindy();
        }

        // Só carrega o Windy quando a aba fica visível: dentro de uma aba oculta o iframe nasce com tamanho zero
        function montar() {
            if (iframe) return;
            iframe = document.createElement('iframe');
            iframe.title = en ? 'Weather map' : 'Mapa meteorológico';
            iframe.loading = 'lazy';
            iframe.src = urlWindy();
            moldura.appendChild(iframe);
        }

        atualizar();

        const observador = new IntersectionObserver((entradas) => {
            if (entradas.some((e) => e.isIntersecting)) {
                montar();
                observador.disconnect();
            }
        });
        observador.observe(moldura);
    });
});
