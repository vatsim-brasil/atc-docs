document$.subscribe(({ body }) => {
    const container = body.querySelector('#metar-taf-container');
    if (!container) return;

    const metarEl = container.querySelector('#metar-content');
    const tafEl = container.querySelector('#taf-content');
    if (!metarEl || !tafEl) return;

    const airport = container.dataset.airport || 'SBCT';

    const metarUrl = `https://aviationweather.gov/api/data/metar?ids=${airport}&format=json`;
    const tafUrl = `https://aviationweather.gov/api/data/taf?ids=${airport}&format=json`;

    const metarProxy = `https://api.allorigins.win/get?url=${encodeURIComponent(metarUrl)}`;
    const tafProxy = `https://api.allorigins.win/get?url=${encodeURIComponent(tafUrl)}`;

    // Função auxiliar para tentar a requisição novamente em caso de erro
    function fetchWithRetry(proxyUrl, element, parserFn, errorMsg, retries = 10, delay = 2000) {
        fetch(proxyUrl)
            .then(response => {
                if (!response.ok) throw new Error('Erro na resposta da rede');
                return response.json();
            })
            .then(data => {
                if (!data || !data.contents || data.contents.includes('Error code') || data.contents.includes('cloudflare') || data.contents.includes('522: Connection timed out')) {
                    throw new Error('Proxy retornou página de erro');
                }
                const parsed = JSON.parse(data.contents);
                parserFn(parsed);
            })
            .catch(err => {
                if (retries > 0) {
                    setTimeout(() => {
                        fetchWithRetry(proxyUrl, element, parserFn, errorMsg, retries - 1, delay);
                    }, delay);
                } else {
                    element.innerHTML = `<span style="opacity: 0.65; font-size: 0.8rem; padding: 20px; display: block; text-align: center;">${errorMsg}</span>`;
                }
            });
    }

    // Tradução de abreviações de nuvens
    const translateCover = (cover) => {
        const dict = {
            'FEW': 'Poucas',
            'SCT': 'Esparsas',
            'BKN': 'Nublado',
            'OVC': 'Encoberto',
            'CLR': 'Céu Claro',
            'SKC': 'Céu Limpo',
            'NSC': 'Sem Nuvens Sig.'
        };
        return dict[cover] || cover;
    };

    // 1. Busca e renderiza o Dashboard do METAR
    fetchWithRetry(
        metarProxy,
        metarEl,
        (parsed) => {
            const data = parsed[0];
            if (!data) {
                metarEl.innerHTML = '<span style="opacity: 0.65; font-size: 0.8rem; padding: 20px; display: block; text-align: center;">METAR não disponível.</span>';
                return;
            }

            const rawOb = data.rawOb || '';
            const fltCat = data.fltCat || 'VFR';
            const temp = data.temp !== undefined ? data.temp : '--';
            const dewp = data.dewp !== undefined ? data.dewp : '--';

            // Decodificação amigável do Vento
            let vento = 'Calmo';
            if (data.wspd) {
                const dir = data.wdir ? `${data.wdir}°` : 'Var';
                vento = `${dir} @ ${data.wspd} KT`;
                if (data.wgst) {
                    vento += ` (G ${data.wgst} KT)`;
                }
            }

            // Decodificação amigável da Visibilidade
            let visibilidade = 'Não disponível';
            if (data.visib) {
                if (data.visib === '9999' || data.visib === '10+' || data.visib === '6+') {
                    visibilidade = '>= 10 km';
                } else if (!isNaN(data.visib)) {
                    visibilidade = `${data.visib} m`;
                } else {
                    visibilidade = `${data.visib} SM`;
                }
            }

            // Pressão (QNH)
            const qnh = data.altim ? `${data.altim} hPa` : '-- hPa';

            // Cobertura de Nuvens / Teto (Corrigido para não multiplicar a base em ft por 100)
            let nuvens = 'Céu Claro (NSC)';
            if (data.clouds && data.clouds.length > 0) {
                nuvens = data.clouds.map(c => {
                    const cover = translateCover(c.cover);
                    const base = c.base ? `a ${c.base.toLocaleString('pt-BR')} ft` : '';
                    return `${cover} ${base}`.trim();
                }).join('<br>');
            }

            // Renderiza o Dashboard visual premium dentro do card do METAR
            metarEl.innerHTML = `
                <div class="weather-card-header">
                    <div class="weather-card-title">
                        <span class="pulse-dot"></span>
                        <span>METAR</span>
                    </div>
                    <span class="flight-category-badge ${fltCat.toLowerCase()}">${fltCat}</span>
                </div>
                <div class="metar-grid">
                    <!-- Vento -->
                    <div class="metar-grid-item">
                        <div class="metar-icon-wrapper wind-wrap">
                            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/></svg>
                        </div>
                        <div class="metar-details">
                            <span class="metar-label">Vento</span>
                            <span class="metar-value">${vento}</span>
                        </div>
                    </div>
                    
                    <!-- Visibilidade -->
                    <div class="metar-grid-item">
                        <div class="metar-icon-wrapper vis-wrap">
                            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                        </div>
                        <div class="metar-details">
                            <span class="metar-label">Visibilidade</span>
                            <span class="metar-value">${visibilidade}</span>
                        </div>
                    </div>

                    <!-- Pressão (QNH) -->
                    <div class="metar-grid-item">
                        <div class="metar-icon-wrapper press-wrap">
                            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6v6l4 2"/><circle cx="12" cy="12" r="10"/></svg>
                        </div>
                        <div class="metar-details">
                            <span class="metar-label">Pressão (QNH)</span>
                            <span class="metar-value">${qnh}</span>
                        </div>
                    </div>

                    <!-- Nuvens -->
                    <div class="metar-grid-item">
                        <div class="metar-icon-wrapper cloud-wrap">
                            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>
                        </div>
                        <div class="metar-details">
                            <span class="metar-label">Nuvens / Teto</span>
                            <span class="metar-value">${nuvens}</span>
                        </div>
                    </div>

                    <!-- Temperatura / Orvalho -->
                    <div class="metar-grid-item">
                        <div class="metar-icon-wrapper temp-wrap">
                            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/></svg>
                        </div>
                        <div class="metar-details">
                            <span class="metar-label">Temp / Orvalho</span>
                            <span class="metar-value">${temp}°C / ${dewp}°C</span>
                        </div>
                    </div>
                </div>
                <div class="metar-raw-box-premium">
                    <div class="metar-icon-wrapper raw-wrap">
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
                    </div>
                    <div class="metar-details" style="flex: 1;">
                        <span class="metar-label">METAR Codificado</span>
                        <code class="metar-raw-code">${rawOb}</code>
                    </div>
                </div>
            `;
        },
        'Erro ao carregar o METAR.'
    );

    // 2. Busca e renderiza o TAF formatado
    fetchWithRetry(
        tafProxy,
        tafEl,
        (parsed) => {
            const data = parsed[0];
            if (!data) {
                tafEl.innerHTML = '<span style="opacity: 0.65; font-size: 0.8rem; padding: 20px; display: block; text-align: center;">Previsão TAF não disponível.</span>';
                return;
            }

            const rawTaf = data.rawTAF || 'Não disponível';
            const formattedTaf = rawTaf.replace(/(FM|BECMG|TEMPO|PROB)/g, '\n  $1');

            tafEl.innerHTML = `
                <div class="weather-card-header">
                    <div class="weather-card-title">
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="opacity:0.8;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                        <span>Previsão de Aeródromo (TAF)</span>
                    </div>
                </div>
                <div class="metar-raw-box-premium">
                    <div class="metar-icon-wrapper raw-wrap">
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
                    </div>
                    <div class="metar-details" style="flex: 1;">
                        <span class="metar-label">TAF Codificado</span>
                        <code class="metar-raw-code" style="white-space: pre-wrap; line-height: 1.6;">${formattedTaf.trim()}</code>
                    </div>
                </div>
            `;
        },
        'Erro ao carregar o TAF.'
    );
});
