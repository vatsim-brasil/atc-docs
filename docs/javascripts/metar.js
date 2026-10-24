document$.subscribe(({ body }) => {
    const container = body.querySelector('#metar-taf-container');
    if (!container) return;

    const metarEl = container.querySelector('#metar-content');
    const tafEl = container.querySelector('#taf-content');
    if (!metarEl || !tafEl) return;

    const airport = container.dataset.airport || 'SBCT';

    // Fontes com CORS liberado, sem proxy. O METAR vem de duas fontes em paralelo
    // (met.no e VATSIM): vale a observação mais recente, e uma cobre a falha da outra.
    const metarSources = [
        `https://api.met.no/weatherapi/tafmetar/1.0/metar.txt?icao=${airport}`,
        `https://metar.vatsim.net/${airport}`
    ];
    const tafUrl = `https://api.met.no/weatherapi/tafmetar/1.0/taf.txt?icao=${airport}`;

    // Função auxiliar para tentar a requisição novamente em caso de erro
    function fetchWithRetry(url, parserFn, onError, retries = 2, delay = 1000) {
        fetch(url, { signal: AbortSignal.timeout(8000) })
            .then(response => {
                if (!response.ok) throw new Error('Erro na resposta da rede');
                return response.text();
            })
            .then(text => parserFn(text.trim()))
            .catch(err => {
                if (retries > 0) {
                    setTimeout(() => {
                        fetchWithRetry(url, parserFn, onError, retries - 1, delay);
                    }, delay);
                } else {
                    onError();
                }
            });
    }

    const showMessage = (element, msg) => {
        element.innerHTML = `<span style="opacity: 0.65; font-size: 0.8rem; padding: 20px; display: block; text-align: center;">${msg}</span>`;
    };

    // Último boletim de uma resposta em texto (o met.no lista as últimas 24 h, um por linha)
    const lastBulletin = (text) => {
        const lines = text.split('\n').map(l => l.trim()).filter(Boolean);
        return lines.length ? lines[lines.length - 1].replace(/=$/, '').replace(/^(METAR|SPECI)\s+/, '') : '';
    };

    // true se o METAR a for mais recente que o b, pelo grupo DDHHMMZ (tratando a virada do mês)
    function isNewer(a, b) {
        const minutes = (raw) => {
            const m = raw.match(/\b(\d{2})(\d{2})(\d{2})Z\b/);
            return m ? (+m[1]) * 1440 + (+m[2]) * 60 + (+m[3]) : 0;
        };
        let diff = minutes(a) - minutes(b);
        if (diff > 20 * 1440) diff -= 31 * 1440;
        if (diff < -20 * 1440) diff += 31 * 1440;
        return diff > 0;
    }

    // Decodifica o METAR bruto nos campos usados pelo dashboard
    function decodeMetar(rawOb) {
        const data = { rawOb, clouds: [] };
        const tokens = rawOb.split(/\s+/);

        for (const tok of tokens.slice(1)) {
            if (/^(RMK|NOSIG|BECMG|TEMPO)$/.test(tok)) break;

            let m;
            if ((m = tok.match(/^(\d{3}|VRB)(\d{2,3})(?:G(\d{2,3}))?(KT|MPS)$/))) {
                const factor = m[4] === 'MPS' ? 1.944 : 1;
                data.wdir = m[1] === 'VRB' ? null : parseInt(m[1], 10);
                data.wspd = Math.round(parseInt(m[2], 10) * factor);
                if (m[3]) data.wgst = Math.round(parseInt(m[3], 10) * factor);
            } else if (tok === 'CAVOK') {
                data.visib = 9999;
            } else if (/^\d{4}$/.test(tok) && data.visib === undefined) {
                data.visib = parseInt(tok, 10);
            } else if ((m = tok.match(/^(FEW|SCT|BKN|OVC|VV)(\d{3})(CB|TCU)?$/))) {
                data.clouds.push({ cover: m[1], base: parseInt(m[2], 10) * 100, type: m[3] });
            } else if ((m = tok.match(/^(M?\d{2})\/(M?\d{2})?$/))) {
                const toNum = (t) => parseInt(t.replace('M', '-'), 10);
                data.temp = toNum(m[1]);
                if (m[2]) data.dewp = toNum(m[2]);
            } else if ((m = tok.match(/^Q(\d{4})$/))) {
                data.altim = parseInt(m[1], 10);
            } else if ((m = tok.match(/^A(\d{4})$/))) {
                data.altim = Math.round(parseInt(m[1], 10) / 100 * 33.8639);
            }
        }

        // Categoria de voo pelo teto (BKN/OVC/VV) e visibilidade
        const ceiling = Math.min(...data.clouds.filter(c => /BKN|OVC|VV/.test(c.cover)).map(c => c.base), Infinity);
        const vis = data.visib ?? 9999;
        if (ceiling < 500 || vis < 1600) data.fltCat = 'LIFR';
        else if (ceiling < 1000 || vis < 4800) data.fltCat = 'IFR';
        else if (ceiling <= 3000 || vis <= 8000) data.fltCat = 'MVFR';
        else data.fltCat = 'VFR';

        return data;
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
            'NSC': 'Sem Nuvens Sig.',
            'VV': 'Céu Obscurecido'
        };
        return dict[cover] || cover;
    };

    // 1. Busca e renderiza o Dashboard do METAR
    function renderMetar(text) {
        const data = decodeMetar(text);
        const rawOb = data.rawOb;
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
        if (data.visib !== undefined) {
            visibilidade = data.visib >= 9999 ? '>= 10 km' : `${data.visib} m`;
        }

        // Pressão (QNH)
        const qnh = data.altim ? `${data.altim} hPa` : '-- hPa';

        // Cobertura de Nuvens / Teto (Corrigido para não multiplicar a base em ft por 100)
        let nuvens = 'Céu Claro (NSC)';
        if (data.clouds && data.clouds.length > 0) {
            nuvens = data.clouds.map(c => {
                const cover = translateCover(c.cover);
                const base = c.base ? `a ${c.base.toLocaleString('pt-BR')} ft` : '';
                return `${cover} ${base} ${c.type || ''}`.trim();
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
    }

    // Mostra a primeira resposta que chegar e troca se a outra fonte trouxer um METAR mais novo
    let shownMetar = '';
    let pending = metarSources.length;
    let failures = 0;
    const settleMetar = () => {
        if (--pending > 0 || shownMetar) return;
        showMessage(metarEl, failures === metarSources.length ? 'Erro ao carregar o METAR.' : 'METAR não disponível.');
    };
    metarSources.forEach(url => fetchWithRetry(
        url,
        (text) => {
            const raw = lastBulletin(text);
            if (raw && (!shownMetar || isNewer(raw, shownMetar))) {
                shownMetar = raw;
                renderMetar(raw);
            }
            settleMetar();
        },
        () => { failures++; settleMetar(); }
    ));

    // 2. Busca e renderiza o TAF formatado
    fetchWithRetry(
        tafUrl,
        (text) => {
            // O met.no devolve os TAFs das últimas horas, um por linha; o último é o vigente
            const rawTaf = lastBulletin(text);
            if (!rawTaf) {
                showMessage(tafEl, 'Previsão TAF não disponível.');
                return;
            }

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
        () => showMessage(tafEl, 'Erro ao carregar o TAF.')
    );
});
