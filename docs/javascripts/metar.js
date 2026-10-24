// Aba Meteorologia dos aeródromos: METAR e TAF decodificados, com componentes de vento por
// cabeceira, nível de transição e a linha do tempo hora a hora do TAF.
// O rumo verdadeiro das cabeceiras e a declinação magnética vêm de pistas.json, gerado a partir
// do OurAirports (rumos) e do WMM (declinação), com as cabeceiras da tabela de pistas de cada página.
const pistasUrl = document.currentScript ? new URL('pistas.json', document.currentScript.src).href : null;
let pistasPromise;
const carregarPistas = () => pistasPromise ??= (pistasUrl
    ? fetch(pistasUrl).then(r => (r.ok ? r.json() : {})).catch(() => ({}))
    : Promise.resolve({}));

document$.subscribe(({ body }) => {
    const container = body.querySelector('#metar-taf-container');
    if (!container) return;

    const metarEl = container.querySelector('#metar-content');
    const tafEl = container.querySelector('#taf-content');
    if (!metarEl || !tafEl) return;

    const airport = container.dataset.airport || 'SBCT';
    const en = (document.documentElement.lang || '').startsWith('en');
    const L = en ? TEXTOS.en : TEXTOS.pt;

    // Fontes com CORS liberado, sem proxy. O METAR vem de duas fontes em paralelo
    // (met.no e VATSIM): vale a observação mais recente, e uma cobre a falha da outra.
    // O met.no também traz os boletins das últimas 24 h, usados no histórico.
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
            .catch(() => {
                if (retries > 0) {
                    setTimeout(() => fetchWithRetry(url, parserFn, onError, retries - 1, delay), delay);
                } else {
                    onError();
                }
            });
    }

    const showMessage = (element, msg) => {
        element.innerHTML = `<span class="wx-msg">${msg}</span>`;
    };

    // Boletins de uma resposta em texto (o met.no lista as últimas 24 h, um por linha)
    const bulletins = (text) => text.split('\n').map(l => l.trim()).filter(Boolean)
        .map(l => l.replace(/=$/, '').replace(/^(METAR|SPECI)\s+/, ''));

    // Dados das cabeceiras (rumo verdadeiro) e altitude de transição da tabela da própria página
    const pistasDoAeroporto = carregarPistas().then(d => d[airport] || null);
    const altTransicao = (() => {
        for (const row of body.querySelectorAll('.md-typeset table tr')) {
            const cells = row.querySelectorAll('td');
            if (cells.length >= 2 && /altitude de transição|transition altitude/i.test(cells[0].textContent)) {
                const n = parseInt(cells[1].textContent.replace(/\D/g, ''), 10);
                if (n) return n;
            }
        }
        return null;
    })();

    // ---------- METAR ----------
    let shownMetar = '';
    let historico = [];
    let pending = metarSources.length;
    let failures = 0;
    const settleMetar = () => {
        if (--pending > 0 || shownMetar) return;
        showMessage(metarEl, failures === metarSources.length ? L.erroMetar : L.semMetar);
    };
    const desenharMetar = () => pistasDoAeroporto.then(pistas => {
        metarEl.innerHTML = renderMetar(decodeMetar(shownMetar), pistas, historico, altTransicao, L);
    });
    metarSources.forEach(url => fetchWithRetry(
        url,
        (text) => {
            const lista = bulletins(text);
            const raw = lista[lista.length - 1] || '';
            if (lista.length > historico.length) historico = lista;
            if (raw && (!shownMetar || isNewer(raw, shownMetar))) shownMetar = raw;
            if (shownMetar) desenharMetar();
            settleMetar();
        },
        () => { failures++; settleMetar(); }
    ));

    // ---------- TAF ----------
    fetchWithRetry(
        tafUrl,
        (text) => {
            // O met.no devolve os TAFs das últimas horas, um por linha; o último é o vigente
            const lista = bulletins(text);
            const rawTaf = (lista[lista.length - 1] || '').replace(/^TAF\s+/, '');
            if (!rawTaf) {
                showMessage(tafEl, L.semTaf);
                return;
            }
            pistasDoAeroporto.then(pistas => {
                const taf = decodeTaf(rawTaf);
                tafEl.innerHTML = taf ? renderTaf(taf, pistas, L) : renderTafBruto(rawTaf, L);
            });
        },
        () => showMessage(tafEl, L.erroTaf)
    );
});

// =====================================================================
// Textos
// =====================================================================
const TEXTOS = {
    pt: {
        erroMetar: 'Erro ao carregar o METAR.', semMetar: 'METAR não disponível.',
        erroTaf: 'Erro ao carregar o TAF.', semTaf: 'Previsão TAF não disponível.',
        ha: (m) => m < 60 ? `há ${m} min` : `há ${Math.floor(m / 60)} h ${String(m % 60).padStart(2, '0')}`,
        desatualizado: 'Desatualizado', semFenomenos: 'Sem fenômenos significativos',
        vento: 'Vento', verdadeiro: 'verdadeiro', magnetico: 'magnético', calmo: 'Calmo', variavel: 'Variável',
        rajada: 'rajada', varEntre: 'variando entre',
        visibilidade: 'Visibilidade', visMin: 'mínima', rvr: 'RVR',
        teto: 'Teto', semTeto: 'Sem teto', nuvens: 'Nuvens', ceuClaro: 'Sem nuvens significativas',
        qnh: 'QNH', nt: 'Nível de transição', ntNota: (ta) => `TA ${ta.toLocaleString('pt-BR')} ft · ICA 100-37, Tab. 7`,
        temp: 'Temperatura', orvalho: 'orvalho', ur: 'UR',
        recente: 'Recente', windshear: 'Tesoura de vento',
        componentes: 'Componentes de vento', proa: 'proa', cauda: 'cauda', traves: 'través',
        esq: 'E', dir: 'D', favorecida: 'favorecida',
        semComponentes: 'Vento calmo ou variável: sem componentes por cabeceira.',
        notaPista: 'Cabeceira favorecida só pelo vento. A pista em uso segue as regras do aeródromo e o ATIS.',
        bruto: 'METAR codificado', historico: 'Últimos METAR',
        colHora: 'Hora', colVento: 'Vento', colVis: 'Vis', colTeto: 'Teto', colQnh: 'QNH', colCond: 'Cond.',
        alertaCb: 'CB/TCU', alertaTs: 'Trovoada', alertaRaj: (g) => `Rajada ${g} kt`,
        alertaTraves: (x) => `Través ${x} kt`,
        alertaWs: 'Tesoura de vento', alertaTeto: (t) => `Teto ${t} ft`, alertaVis: 'Visibilidade reduzida',
        taf: 'Previsão de Aeródromo (TAF)', emitido: 'emitido', validade: 'válido',
        tmax: 'Máx', tmin: 'Mín', as: 'às',
        horaria: 'Hora a hora', horariaNota: 'Horários em UTC. Condição prevalecente; TEMPO e PROB aparecem abaixo de cada hora.',
        agora: 'agora', decodificado: 'Decodificado', tafBruto: 'TAF codificado',
        base: 'Início', becmg: 'Tornando-se', tempo: 'Temporariamente', prob: (p) => `Probabilidade ${p}%`,
        fm: 'A partir de', das: (a, b) => `${a} → ${b}`,
        cavok: 'CAVOK', nsw: 'fim dos fenômenos', nsc: 'sem nuvens significativas',
        pista: 'RWY',
    },
    en: {
        erroMetar: 'Failed to load the METAR.', semMetar: 'METAR not available.',
        erroTaf: 'Failed to load the TAF.', semTaf: 'TAF not available.',
        ha: (m) => m < 60 ? `${m} min ago` : `${Math.floor(m / 60)} h ${String(m % 60).padStart(2, '0')} ago`,
        desatualizado: 'Outdated', semFenomenos: 'No significant weather',
        vento: 'Wind', verdadeiro: 'true', magnetico: 'magnetic', calmo: 'Calm', variavel: 'Variable',
        rajada: 'gust', varEntre: 'varying between',
        visibilidade: 'Visibility', visMin: 'minimum', rvr: 'RVR',
        teto: 'Ceiling', semTeto: 'No ceiling', nuvens: 'Clouds', ceuClaro: 'No significant cloud',
        qnh: 'QNH', nt: 'Transition level', ntNota: (ta) => `TA ${ta.toLocaleString('en-US')} ft · ICA 100-37, Table 7`,
        temp: 'Temperature', orvalho: 'dew point', ur: 'RH',
        recente: 'Recent', windshear: 'Wind shear',
        componentes: 'Wind components', proa: 'head', cauda: 'tail', traves: 'cross',
        esq: 'L', dir: 'R', favorecida: 'favoured',
        semComponentes: 'Calm or variable wind: no per-runway components.',
        notaPista: 'Runway favoured by wind only. The runway in use follows the aerodrome rules and the ATIS.',
        bruto: 'Raw METAR', historico: 'Recent METARs',
        colHora: 'Time', colVento: 'Wind', colVis: 'Vis', colTeto: 'Ceiling', colQnh: 'QNH', colCond: 'Cond.',
        alertaCb: 'CB/TCU', alertaTs: 'Thunderstorm', alertaRaj: (g) => `Gusts ${g} kt`,
        alertaTraves: (x) => `Crosswind ${x} kt`,
        alertaWs: 'Wind shear', alertaTeto: (t) => `Ceiling ${t} ft`, alertaVis: 'Reduced visibility',
        taf: 'Aerodrome Forecast (TAF)', emitido: 'issued', validade: 'valid',
        tmax: 'Max', tmin: 'Min', as: 'at',
        horaria: 'Hour by hour', horariaNota: 'Times in UTC. Prevailing conditions; TEMPO and PROB shown below each hour.',
        agora: 'now', decodificado: 'Decoded', tafBruto: 'Raw TAF',
        base: 'Initial', becmg: 'Becoming', tempo: 'Temporarily', prob: (p) => `Probability ${p}%`,
        fm: 'From', das: (a, b) => `${a} → ${b}`,
        cavok: 'CAVOK', nsw: 'no significant weather', nsc: 'no significant cloud',
        pista: 'RWY',
    }
};

const FENOMENOS = {
    DZ: ['chuvisco', 'drizzle'], RA: ['chuva', 'rain'], SN: ['neve', 'snow'], SG: ['grãos de neve', 'snow grains'],
    IC: ['cristais de gelo', 'ice crystals'], PL: ['pelotas de gelo', 'ice pellets'], GR: ['granizo', 'hail'],
    GS: ['granizo pequeno', 'small hail'], UP: ['precipitação desconhecida', 'unknown precipitation'],
    BR: ['névoa úmida', 'mist'], FG: ['nevoeiro', 'fog'], FU: ['fumaça', 'smoke'], VA: ['cinzas vulcânicas', 'volcanic ash'],
    DU: ['poeira', 'dust'], SA: ['areia', 'sand'], HZ: ['névoa seca', 'haze'], PY: ['borrifo', 'spray'],
    PO: ['redemoinhos de poeira', 'dust whirls'], SQ: ['tempestade (SQ)', 'squalls'], FC: ['nuvem funil', 'funnel cloud'],
    SS: ['tempestade de areia', 'sandstorm'], DS: ['tempestade de poeira', 'duststorm']
};
const COBERTURA = {
    FEW: ['Poucas', 'Few'], SCT: ['Esparsas', 'Scattered'], BKN: ['Nublado', 'Broken'], OVC: ['Encoberto', 'Overcast'],
    VV: ['Céu obscurecido', 'Sky obscured']
};

// =====================================================================
// Decodificação
// =====================================================================
const RE_WX = /^(-|\+|VC)?(MI|BC|PR|DR|BL|SH|TS|FZ)?((?:DZ|RA|SN|SG|IC|PL|GR|GS|UP|BR|FG|FU|VA|DU|SA|HZ|PY|PO|SQ|FC|SS|DS)*)$/;

// Um grupo de condições (corpo do METAR, condição inicial do TAF ou grupo de mudança)
function parseCondicoes(tokens) {
    const g = { clouds: [], wx: [], rvr: [], recent: [], ws: [] };
    for (let i = 0; i < tokens.length; i++) {
        const tok = tokens[i];
        let m;
        if ((m = tok.match(/^(\d{3}|VRB|\/\/\/)(\d{2,3}|\/\/)(?:G(\d{2,3}))?(KT|MPS)$/))) {
            const f = m[4] === 'MPS' ? 1.944 : 1;
            g.wind = {
                dir: /^\d{3}$/.test(m[1]) ? parseInt(m[1], 10) : null,
                spd: m[2] === '//' ? null : Math.round(parseInt(m[2], 10) * f),
                gust: m[3] ? Math.round(parseInt(m[3], 10) * f) : null
            };
        } else if ((m = tok.match(/^(\d{3})V(\d{3})$/))) {
            g.windVar = [parseInt(m[1], 10), parseInt(m[2], 10)];
        } else if (tok === 'CAVOK') {
            g.cavok = true; g.vis = 9999;
        } else if ((m = tok.match(/^(\d{4})(NDV)?$/)) && g.vis === undefined) {
            g.vis = parseInt(m[1], 10);
        } else if ((m = tok.match(/^(\d{4})(N|NE|E|SE|S|SW|W|NW)$/)) && g.vis !== undefined) {
            g.visMin = { val: parseInt(m[1], 10), dir: m[2] };
        } else if ((m = tok.match(/^(\d+)SM$/)) && g.vis === undefined) {
            g.vis = Math.min(9999, Math.round(parseInt(m[1], 10) * 1609));
        } else if ((m = tok.match(/^R(\d{2}[LCR]?)\/([PM]?\d{4})(?:V([PM]?\d{4}))?(FT)?\/?([UDN])?$/))) {
            g.rvr.push({ rwy: m[1], val: m[2], max: m[3], tend: m[5] });
        } else if ((m = tok.match(/^(FEW|SCT|BKN|OVC|VV)(\d{3}|\/\/\/)(CB|TCU|\/\/\/)?$/))) {
            g.clouds.push({ cover: m[1], base: m[2] === '///' ? null : parseInt(m[2], 10) * 100, type: m[3] && m[3] !== '///' ? m[3] : null });
        } else if (/^(NSC|NCD|SKC|CLR)$/.test(tok)) {
            g.nsc = true;
        } else if (tok === 'NSW') {
            g.nsw = true;
        } else if ((m = tok.match(/^(M?\d{2})\/(M?\d{2})?$/))) {
            const n = (t) => parseInt(t.replace('M', '-'), 10);
            g.temp = n(m[1]);
            if (m[2]) g.dewp = n(m[2]);
        } else if ((m = tok.match(/^Q(\d{4})$/))) {
            g.qnh = parseInt(m[1], 10);
        } else if ((m = tok.match(/^A(\d{4})$/))) {
            g.qnh = Math.round(parseInt(m[1], 10) / 100 * 33.8639);
        } else if (tok === 'WS') {
            const alvo = tokens[i + 1] === 'ALL' ? 'ALL RWY' : (tokens[i + 1] || '').replace(/^R(WY)?/, '');
            g.ws.push(alvo);
            i += tokens[i + 1] === 'ALL' ? 2 : 1;
        } else if ((m = tok.match(/^RE(.+)$/)) && RE_WX.test(m[1])) {
            g.recent.push(m[1]);
        } else if (tok.length >= 2 && RE_WX.test(tok)) {
            g.wx.push(tok);
        }
    }
    return g;
}

function decodeMetar(raw) {
    const tokens = raw.split(/\s+/);
    const corpo = [];
    for (const tok of tokens.slice(1)) {
        if (/^(RMK|NOSIG|BECMG|TEMPO)$/.test(tok)) break;
        corpo.push(tok);
    }
    const d = parseCondicoes(corpo);
    d.raw = raw;
    d.icao = tokens[0];
    const t = raw.match(/\b(\d{2})(\d{2})(\d{2})Z\b/);
    if (t) d.obs = resolverData(+t[1], +t[2], +t[3]);
    return d;
}

// Dia do mês → data UTC completa, assumindo o mês corrente (ou o anterior/seguinte na virada)
function resolverData(dia, hora, min, ref = new Date()) {
    let d = new Date(Date.UTC(ref.getUTCFullYear(), ref.getUTCMonth(), dia, hora, min));
    if (d - ref > 15 * 86400e3) d = new Date(Date.UTC(ref.getUTCFullYear(), ref.getUTCMonth() - 1, dia, hora, min));
    else if (ref - d > 15 * 86400e3) d = new Date(Date.UTC(ref.getUTCFullYear(), ref.getUTCMonth() + 1, dia, hora, min));
    return d;
}

// true se o METAR a for mais recente que o b, pelo grupo DDHHMMZ
function isNewer(a, b) {
    const t = (raw) => {
        const m = raw.match(/\b(\d{2})(\d{2})(\d{2})Z\b/);
        return m ? resolverData(+m[1], +m[2], +m[3]).getTime() : 0;
    };
    return t(a) > t(b);
}

const tetoDe = (g) => {
    const bases = (g.clouds || []).filter(c => /BKN|OVC|VV/.test(c.cover) && c.base !== null).map(c => c.base);
    return bases.length ? Math.min(...bases) : null;
};

// Condição de aeródromo (ICA 100-12): VMC com teto ≥ 1500 ft e visibilidade ≥ 5000 m
function condicao(g) {
    const teto = tetoDe(g);
    const vis = g.vis ?? 9999;
    return (teto !== null && teto < 1500) || vis < 5000 ? 'IMC' : 'VMC';
}

// Nível de transição pela Tabela 7 do Art. 479 da ICA 100-37: cada faixa de QNH soma 500 ft
// à altitude de transição. Conferido com o ATIS de SBGR (TA 8000, QNH 1014 → FL085)
// e com o exemplo do manual (TA 3000, QNH 959,5–977,1 → FL050).
function nivelTransicao(ta, qnh) {
    if (!ta || !qnh) return null;
    const faixas = [[1031.7, 0], [1013.3, 5], [995.1, 10], [977.2, 15], [959.5, 20], [942.2, 25]];
    const faixa = faixas.find(([min]) => qnh >= min);
    return ta / 100 + (faixa ? faixa[1] : 30);
}

function umidade(t, td) {
    const a = 17.625, b = 243.04;
    return Math.round(100 * Math.exp((a * td) / (b + td)) / Math.exp((a * t) / (b + t)));
}

function decodeWx(code, L) {
    const lang = L === TEXTOS.en ? 1 : 0;
    const m = code.match(RE_WX);
    if (!m) return code;
    const [, intens, desc, fen] = m;
    const nomes = (fen.match(/../g) || []).map(f => FENOMENOS[f]?.[lang] || f);
    let base = nomes.join(lang ? ' and ' : ' e ');
    if (lang) {
        const adj = { MI: 'shallow', BC: 'patches of', PR: 'partial', DR: 'low drifting', BL: 'blowing', FZ: 'freezing' };
        if (desc === 'TS') base = base ? `thunderstorm with ${base}` : 'thunderstorm';
        else if (desc === 'SH') base = base ? `${base} showers` : 'showers';
        else if (desc) base = `${adj[desc]} ${base}`;
        if (intens === '-') base = `light ${base}`;
        if (intens === '+') base = `heavy ${base}`;
        if (intens === 'VC') base = `${base} in the vicinity`;
    } else {
        const adj = { MI: 'baixo', BC: 'em bancos', PR: 'parcial', DR: 'flutuante', BL: 'soprado', FZ: 'congelante' };
        const forca = intens === '-' ? ' leve' : intens === '+' ? ' forte' : '';
        if (desc === 'TS') base = base ? `trovoada com ${base}${forca}` : `trovoada${forca}`;
        else if (desc === 'SH') base = `pancadas de ${base || 'chuva'}${forca}`;
        else base = `${base}${desc ? ' ' + adj[desc] : ''}${forca}`;
        if (intens === 'VC') base = `${desc === 'SH' && !fen ? 'pancadas' : base} na vizinhança`;
    }
    return base.charAt(0).toUpperCase() + base.slice(1);
}

// ---------- TAF ----------
function decodeTaf(raw) {
    const tokens = raw.replace(/\s+RMK\s.*$/, '').split(/\s+/).filter(t => !/^(AMD|COR)$/.test(t));
    const icao = tokens.shift();
    const emis = (tokens[0] || '').match(/^(\d{2})(\d{2})(\d{2})Z$/);
    if (!emis) return null;
    tokens.shift();
    const ref = resolverData(+emis[1], +emis[2], +emis[3]);
    const periodo = (tok) => {
        const m = tok.match(/^(\d{2})(\d{2})\/(\d{2})(\d{2})$/);
        return m ? [resolverData(+m[1], +m[2], 0, ref), resolverData(+m[3], +m[4], 0, ref)] : null;
    };
    const val = periodo(tokens.shift() || '');
    if (!val) return null;

    const taf = { raw, icao, emitido: ref, de: val[0], ate: val[1], temps: [], grupos: [] };
    let atual = { tipo: 'BASE', de: val[0], ate: val[1], tokens: [] };
    const fechar = () => { atual.cond = parseCondicoes(atual.tokens); taf.grupos.push(atual); };
    for (let i = 0; i < tokens.length; i++) {
        const tok = tokens[i];
        let m;
        if ((m = tok.match(/^T([XN])(M?\d{2})\/(\d{2})(\d{2})Z$/))) {
            taf.temps.push({ tipo: m[1], val: parseInt(m[2].replace('M', '-'), 10), quando: resolverData(+m[3], +m[4], 0, ref) });
        } else if ((m = tok.match(/^FM(\d{2})(\d{2})(\d{2})$/))) {
            fechar();
            atual = { tipo: 'FM', de: resolverData(+m[1], +m[2], +m[3], ref), ate: val[1], tokens: [] };
        } else if (tok === 'BECMG' || tok === 'TEMPO' || /^PROB\d{2}$/.test(tok)) {
            fechar();
            let tipo = tok, prob = null;
            if (tok.startsWith('PROB')) {
                prob = parseInt(tok.slice(4), 10);
                if (tokens[i + 1] === 'TEMPO') { tipo = 'PROB TEMPO'; i++; } else tipo = 'PROB';
            }
            const p = periodo(tokens[i + 1] || '');
            if (p) i++;
            atual = { tipo, prob, de: p ? p[0] : val[0], ate: p ? p[1] : val[1], tokens: [] };
        } else {
            atual.tokens.push(tok);
        }
    }
    fechar();
    return taf;
}

// Aplica um grupo de mudança sobre o estado (só os elementos que o grupo informa)
function aplicar(estado, c) {
    const e = { ...estado, clouds: [...estado.clouds], wx: [...estado.wx] };
    if (c.wind) e.wind = c.wind;
    if (c.cavok) { e.vis = 9999; e.clouds = []; e.wx = []; e.cavok = true; }
    if (c.vis !== undefined && !c.cavok) { e.vis = c.vis; e.cavok = false; }
    if (c.wx.length) e.wx = c.wx;
    if (c.nsw) e.wx = [];
    if (c.clouds.length) { e.clouds = c.clouds; e.cavok = false; }
    if (c.nsc) e.clouds = [];
    return e;
}

// Linha do tempo: uma entrada por hora, da hora corrente até o fim da validade
function horasDoTaf(taf) {
    const agora = new Date();
    agora.setUTCMinutes(0, 0, 0);
    const inicio = new Date(Math.max(taf.de, agora));
    const base = taf.grupos[0];
    const horas = [];
    for (let t = inicio.getTime(); t < taf.ate.getTime() && horas.length < 36; t += 3600e3) {
        let estado = aplicar({ clouds: [], wx: [] }, base.cond);
        let transicao = null;
        const temporarios = [];
        for (const g of taf.grupos.slice(1)) {
            if (g.tipo === 'FM' && t >= g.de) estado = aplicar({ clouds: [], wx: [] }, g.cond);
            else if (g.tipo === 'BECMG' && t >= g.de) {
                estado = aplicar(estado, g.cond);
                if (t < g.ate) transicao = g;
            } else if (/TEMPO|PROB/.test(g.tipo) && t >= g.de && t < g.ate) temporarios.push(g);
        }
        horas.push({ t: new Date(t), estado, transicao, temporarios, agora: t === agora.getTime() });
    }
    return horas;
}

// =====================================================================
// Vento × cabeceiras
// =====================================================================
function componentes(wind, pistas) {
    if (!pistas || !pistas.rwy.length || !wind || wind.dir === null || !wind.spd) return null;
    const porNumero = new Map();
    for (const [ident, hdg] of pistas.rwy) {
        const num = ident.slice(0, 2);
        if (!porNumero.has(num)) porNumero.set(num, { nome: [], hdg });
        porNumero.get(num).nome.push(ident);
    }
    const ordem = { L: 0, C: 1, '': 1, R: 2 };
    const linhas = [...porNumero.values()].map(p => {
        p.nome.sort((a, b) => ordem[a.slice(2)] - ordem[b.slice(2)]);
        const ang = (wind.dir - p.hdg) * Math.PI / 180;
        const calc = (v) => ({ proa: Math.round(v * Math.cos(ang)), traves: Math.round(v * Math.sin(ang)) });
        return { ...p, ...calc(wind.spd), raj: wind.gust ? calc(wind.gust) : null };
    }).sort((a, b) => b.proa - a.proa);
    // Só aponta cabeceira quando o vento de proa decide (≥ 3 kt); abaixo disso valem as regras do aeródromo
    if (linhas.length && linhas[0].proa >= 3) linhas[0].favorecida = true;
    return linhas;
}

const cabeceiraFavorecida = (wind, pistas) => {
    const c = componentes(wind, pistas);
    return c && c[0].favorecida ? c[0].nome.join('/') : null;
};

const pad3 = (n) => String(Math.round(n)).padStart(3, '0');
const magnetico = (dir, pistas) => pistas ? ((dir - pistas.dec) % 360 + 360) % 360 : null;
const arred10 = (d) => { const r = Math.round(d / 10) * 10 % 360; return r === 0 ? 360 : r; };

// =====================================================================
// Formatação
// =====================================================================
const esc = (s) => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
const hhmm = (d) => `${String(d.getUTCHours()).padStart(2, '0')}${String(d.getUTCMinutes()).padStart(2, '0')}Z`;
const ddhh = (d) => `${String(d.getUTCDate()).padStart(2, '0')}/${String(d.getUTCHours()).padStart(2, '0')}Z`;

const fmtVis = (v) => v === undefined ? '--' : v >= 9999 ? '≥ 10 km' : v >= 5000 ? `${Math.round(v / 1000)} km` : `${v} m`;
const fmtVento = (w, L) => {
    if (!w) return '--';
    if (!w.spd) return L.calmo;
    const dir = w.dir === null ? 'VRB' : `${pad3(w.dir)}°`;
    return `${dir} ${w.spd}${w.gust ? `G${w.gust}` : ''} kt`;
};
const fmtNuvem = (c) => `${c.cover}${c.base !== null ? String(c.base / 100).padStart(3, '0') : '///'}${c.type || ''}`;
const fmtFt = (n, L) => n.toLocaleString(L === TEXTOS.en ? 'en-US' : 'pt-BR');

const ICONES = {
    vento: '<path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>',
    vis: '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    nuvem: '<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/>',
    pressao: '<path d="M12 6v6l4 2"/><circle cx="12" cy="12" r="10"/>',
    temp: '<path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/>',
    sol: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
    parcial: '<path d="M12 2v2M4.93 4.93l1.41 1.41M20 12h2M19.07 4.93l-1.41 1.41M15.95 12.65A4 4 0 0 0 8.2 9.4"/><path d="M13 22H7a5 5 0 1 1 4.9-6H13a3 3 0 0 1 0 6z"/>',
    chuva: '<path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"/><path d="M8 19v2M8 13v2M16 19v2M16 13v2M12 21v2M12 15v2"/>',
    trovoada: '<path d="M19 16.9A5 5 0 0 0 18 7h-1.26a8 8 0 1 0-11.62 9"/><polyline points="13 11 9 17 15 17 11 23"/>',
    nevoa: '<path d="M4 9h16M3 13h18M5 17h14M8 21h8"/>',
    nivel: '<path d="M12 2l10 6-10 6L2 8z"/><path d="M2 16l10 6 10-6"/>',
    alerta: '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><path d="M12 9v4M12 17h.01"/>',
};
const icone = (nome, tam = 16) => `<svg viewBox="0 0 24 24" width="${tam}" height="${tam}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICONES[nome]}</svg>`;

function iconeTempo(g) {
    const wx = (g.wx || []).join(' ');
    if (/TS/.test(wx)) return 'trovoada';
    if (/RA|DZ|SH|SN|GR|GS|PL/.test(wx)) return 'chuva';
    if (/FG|BR|HZ|FU|DU|SA/.test(wx)) return 'nevoa';
    if ((g.clouds || []).some(c => /BKN|OVC|VV/.test(c.cover))) return 'nuvem';
    if ((g.clouds || []).length) return 'parcial';
    return 'sol';
}

const tile = (ic, cor, rotulo, valor, extra = '') => `
    <div class="wx-tile">
        <div class="wx-ic ${cor}">${icone(ic)}</div>
        <div class="wx-tile-body">
            <span class="wx-label">${rotulo}</span>
            <span class="wx-value">${valor}</span>
            ${extra ? `<span class="wx-sub">${extra}</span>` : ''}
        </div>
    </div>`;

// Rosa dos ventos em referência magnética, com as pistas desenhadas pelo designador
function rosaDosVentos(d, pistas) {
    const R = 70, C = 90;
    const pt = (graus, r) => {
        const a = (graus - 90) * Math.PI / 180;
        return [C + r * Math.cos(a), C + r * Math.sin(a)];
    };
    let svg = `<svg class="wx-rose" viewBox="0 0 180 180" role="img" aria-label="Wind rose">`;
    svg += `<circle cx="${C}" cy="${C}" r="${R}" class="wx-rose-ring"/>`;
    for (let g = 0; g < 360; g += 10) {
        const [x1, y1] = pt(g, R - (g % 30 ? 3 : 6));
        const [x2, y2] = pt(g, R);
        svg += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="wx-rose-tick"/>`;
    }
    for (const [g, s] of [[0, 'N'], [90, 'E'], [180, 'S'], [270, 'W']]) {
        const [x, y] = pt(g, R + 11);
        svg += `<text x="${x}" y="${y}" class="wx-rose-card">${s}</text>`;
    }
    // Pistas: uma faixa por par de cabeceiras; paralelas deslocadas para os lados
    if (pistas) {
        const pares = new Map();
        for (const [ident] of pistas.rwy) {
            const n = parseInt(ident, 10);
            if (n > 18 && pistas.rwy.some(([o]) => parseInt(o, 10) === n - 18)) continue;
            const k = n % 18 || 18;
            if (!pares.has(k)) pares.set(k, []);
            pares.get(k).push(ident);
        }
        const ordem = { L: 0, C: 1, '': 1, R: 2 };
        const oposto = { L: 'R', R: 'L', C: 'C', '': '' };
        for (const [k, idents] of pares) {
            idents.sort((a, b) => ordem[a.slice(2)] - ordem[b.slice(2)]);
            const hdg = k * 10;
            idents.forEach((ident, i) => {
                // L à esquerda e R à direita de quem segue o rumo k*10
                const off = (i - (idents.length - 1) / 2) * 10;
                const a = hdg * Math.PI / 180;
                const dx = Math.cos(a) * off, dy = Math.sin(a) * off;
                const [x1, y1] = pt(hdg, 46), [x2, y2] = pt(hdg + 180, 46);
                svg += `<line x1="${x1 + dx}" y1="${y1 + dy}" x2="${x2 + dx}" y2="${y2 + dy}" class="wx-rose-rwy"/>`;
                // Cada designador fica do lado da sua cabeceira (oposto ao rumo de pouso)
                const n = parseInt(ident, 10);
                const nOp = n > 18 ? n - 18 : n + 18;
                const op = pistas.rwy.find(([o]) => parseInt(o, 10) === nOp && o.slice(2) === oposto[ident.slice(2)]);
                for (const [nome, num] of [[ident, n], op ? [op[0], nOp] : null].filter(Boolean)) {
                    const [lx, ly] = pt(num * 10 + 180, 57);
                    svg += `<text x="${lx + dx * 2.2}" y="${ly + dy * 2.2}" class="wx-rose-lbl">${nome}</text>`;
                }
            });
        }
    }
    const w = d.wind;
    if (w && w.spd && w.dir !== null) {
        const mag = pistas ? magnetico(w.dir, pistas) : w.dir;
        if (d.windVar) {
            const [a, b] = d.windVar.map(v => pistas ? magnetico(v, pistas) : v);
            const [x1, y1] = pt(a, R - 1), [x2, y2] = pt(b, R - 1);
            const arco = ((b - a) % 360 + 360) % 360;
            svg += `<path d="M${C},${C} L${x1},${y1} A${R - 1},${R - 1} 0 ${arco > 180 ? 1 : 0} 1 ${x2},${y2} Z" class="wx-rose-var"/>`;
        }
        const [xa, ya] = pt(mag, R - 2), [xb, yb] = pt(mag, 18);
        svg += `<line x1="${xa}" y1="${ya}" x2="${xb}" y2="${yb}" class="wx-rose-arrow" marker-end="url(#wx-seta)"/>`;
        svg += `<defs><marker id="wx-seta" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" class="wx-rose-head"/></marker></defs>`;
    }
    svg += `<text x="${C}" y="${C + 4}" class="wx-rose-spd">${w && w.spd ? w.spd : '0'}</text>`;
    svg += `</svg>`;
    return svg;
}

// =====================================================================
// Renderização do METAR
// =====================================================================
function renderMetar(d, pistas, historico, ta, L) {
    const cond = condicao(d);
    const teto = tetoDe(d);
    const idadeMin = d.obs ? Math.max(0, Math.round((Date.now() - d.obs) / 60000)) : null;
    const velho = idadeMin !== null && idadeMin > 75;
    const comps = componentes(d.wind, pistas);

    // Alertas operacionais
    const alertas = [];
    if (d.clouds.some(c => c.type)) alertas.push(['red', L.alertaCb]);
    if (d.wx.some(w => /TS/.test(w))) alertas.push(['red', L.alertaTs]);
    if (d.ws.length) alertas.push(['red', `${L.alertaWs} ${d.ws.join(' ')}`]);
    if (d.wind?.gust) alertas.push(['amber', L.alertaRaj(d.wind.gust)]);
    if (comps) {
        const menorTraves = Math.min(...comps.map(c => Math.abs(c.raj ? c.raj.traves : c.traves)));
        if (menorTraves >= 15) alertas.push(['amber', L.alertaTraves(menorTraves)]);
    }
    if (teto !== null && teto < 1500) alertas.push(['red', L.alertaTeto(fmtFt(teto, L))]);
    if ((d.vis ?? 9999) < 5000) alertas.push(['red', L.alertaVis]);

    // Vento
    let ventoValor = L.calmo, ventoExtra = '';
    if (d.wind && d.wind.spd) {
        ventoValor = fmtVento(d.wind, L);
        const partes = [];
        if (d.wind.dir !== null && pistas) partes.push(`${L.magnetico}: <b>${pad3(arred10(magnetico(d.wind.dir, pistas)))}/${String(d.wind.spd).padStart(2, '0')}${d.wind.gust ? `G${d.wind.gust}` : ''} kt</b>`);
        if (d.windVar) partes.push(`${L.varEntre} ${pad3(d.windVar[0])}° – ${pad3(d.windVar[1])}°`);
        ventoExtra = partes.join(' · ');
        if (d.wind.dir !== null) ventoValor += ` <small>${L.verdadeiro}</small>`;
    } else if (d.wind && d.wind.spd === null) ventoValor = '--';

    // Visibilidade
    let visExtra = [];
    if (d.visMin) visExtra.push(`${L.visMin} ${fmtVis(d.visMin.val)} ${d.visMin.dir}`);
    for (const r of d.rvr) visExtra.push(`${L.rvr} ${r.rwy}: ${r.val}${r.max ? `–${r.max}` : ''} m${r.tend ? ` ${r.tend}` : ''}`);
    const visValor = d.cavok ? 'CAVOK' : fmtVis(d.vis);

    // Teto e nuvens
    const tetoValor = d.cavok ? L.semTeto : teto !== null ? `${fmtFt(teto, L)} ft` : L.semTeto;
    const nuvensTxt = d.clouds.length
        ? d.clouds.map(c => `${COBERTURA[c.cover]?.[L === TEXTOS.en ? 1 : 0] || c.cover} ${c.base !== null ? fmtFt(c.base, L) + ' ft' : ''}${c.type ? ` <b class="wx-cb">${c.type}</b>` : ''}`).join('<br>')
        : L.ceuClaro;

    // Pressão e nível de transição
    const nt = nivelTransicao(ta, d.qnh);
    const qnhValor = d.qnh ? `${d.qnh} hPa` : '--';
    const qnhExtra = d.qnh ? `${(d.qnh / 33.8639).toFixed(2)} inHg` : '';

    // Temperatura
    const tempValor = d.temp !== undefined ? `${d.temp}° / ${d.dewp ?? '--'}°C` : '--';
    const tempExtra = d.temp !== undefined && d.dewp !== undefined ? `${L.ur} ${umidade(d.temp, d.dewp)}%` : '';

    // Tempo presente
    const tempoPresente = d.wx.length ? d.wx.map(w => decodeWx(w, L)).join(', ') : (d.cavok ? 'CAVOK' : L.semFenomenos);
    const recente = d.recent.length ? ` · ${L.recente}: ${d.recent.map(w => decodeWx(w, L).toLowerCase()).join(', ')}` : '';

    // Componentes por cabeceira
    let blocoComp = `<p class="wx-note">${L.semComponentes}</p>`;
    if (comps) {
        blocoComp = `<div class="wx-comp">` + comps.map(c => {
            const fmt = (v) => {
                const lado = v.traves === 0 ? '' : v.traves > 0 ? L.dir : L.esq;
                return { proa: v.proa, traves: Math.abs(v.traves), lado };
            };
            const s = fmt(c), r = c.raj ? fmt(c.raj) : null;
            const proaTxt = c.proa >= 0 ? `${L.proa} ${s.proa}` : `${L.cauda} ${-s.proa}`;
            return `
                <div class="wx-comp-row${c.favorecida ? ' fav' : ''}${c.proa < 0 ? ' tail' : ''}">
                    <div class="wx-comp-top">
                        <span class="wx-comp-rwy">${c.nome.join(' · ')}</span>
                        ${c.favorecida ? `<span class="wx-tag">${L.favorecida}</span>` : ''}
                    </div>
                    <div class="wx-comp-vals">
                        <span class="wx-comp-val">${proaTxt}${r ? ` <small>(${r.proa >= 0 ? r.proa : -r.proa})</small>` : ''} kt</span>
                        <span class="wx-comp-val">${L.traves} ${s.traves}${r ? ` <small>(${r.traves})</small>` : ''} kt ${s.lado}</span>
                    </div>
                </div>`;
        }).join('') + `</div><p class="wx-note">${L.notaPista}</p>`;
    }

    // Histórico (met.no traz as últimas 24 h)
    let blocoHist = '';
    if (historico.length > 1) {
        const linhas = historico.slice(-8).reverse().map(raw => {
            const h = decodeMetar(raw);
            const tt = tetoDe(h);
            const c = condicao(h);
            return `<tr><td>${h.obs ? hhmm(h.obs) : '--'}</td><td>${fmtVento(h.wind, L)}</td><td>${h.cavok ? 'CAVOK' : fmtVis(h.vis)}</td>
                <td>${tt !== null ? fmtFt(tt, L) : '—'}</td><td>${h.qnh || '--'}</td><td><span class="wx-badge sm ${c.toLowerCase()}">${c}</span></td></tr>`;
        }).join('');
        blocoHist = `
            <details class="wx-details">
                <summary>${L.historico}</summary>
                <div class="wx-table-wrap"><table class="wx-table">
                    <thead><tr><th>${L.colHora}</th><th>${L.colVento}</th><th>${L.colVis}</th><th>${L.colTeto}</th><th>${L.colQnh}</th><th>${L.colCond}</th></tr></thead>
                    <tbody>${linhas}</tbody>
                </table></div>
            </details>`;
    }

    return `
        <div class="wx-head">
            <div class="wx-title">
                <span class="pulse-dot${velho ? ' stale' : ''}"></span>
                <span>METAR ${esc(d.icao)}</span>
                ${d.obs ? `<span class="wx-time">${hhmm(d.obs)} · ${L.ha(idadeMin)}${velho ? ` · <b>${L.desatualizado}</b>` : ''}</span>` : ''}
            </div>
            <span class="wx-badge ${cond.toLowerCase()}">${cond}</span>
        </div>
        <div class="wx-summary">
            <span class="wx-summary-ic">${icone(iconeTempo(d), 22)}</span>
            <span>${tempoPresente}${recente}</span>
        </div>
        ${alertas.length ? `<div class="wx-alerts">${alertas.map(([cor, txt]) => `<span class="wx-chip ${cor}">${icone('alerta', 12)} ${txt}</span>`).join('')}</div>` : ''}
        <div class="wx-main">
            <div class="wx-wind-panel">
                ${rosaDosVentos(d, pistas)}
                <div class="wx-wind-side">
                    <span class="wx-label">${L.componentes}</span>
                    ${blocoComp}
                </div>
            </div>
            <div class="wx-tiles">
                ${tile('vento', 'c-blue', L.vento, ventoValor, ventoExtra)}
                ${tile('vis', 'c-green', L.visibilidade, visValor, visExtra.join('<br>'))}
                ${tile('nuvem', 'c-purple', L.teto, tetoValor, d.cavok ? '' : nuvensTxt)}
                ${tile('pressao', 'c-orange', L.qnh, qnhValor, qnhExtra)}
                ${nt ? tile('nivel', 'c-teal', L.nt, `FL${pad3(nt)}`, L.ntNota(ta)) : ''}
                ${tile('temp', 'c-red', L.temp, tempValor, tempExtra)}
            </div>
        </div>
        <div class="wx-raw">
            <span class="wx-label">${L.bruto}</span>
            <code>${esc(d.raw)}</code>
        </div>
        ${blocoHist}
    `;
}

// =====================================================================
// Renderização do TAF
// =====================================================================
function resumoCondicoes(c, L) {
    const partes = [];
    if (c.wind) partes.push(fmtVento(c.wind, L));
    if (c.cavok) partes.push('CAVOK');
    else if (c.vis !== undefined) partes.push(fmtVis(c.vis));
    if (c.wx.length) partes.push(c.wx.map(w => decodeWx(w, L)).join(', '));
    if (c.nsw) partes.push(L.nsw);
    if (c.clouds.length) partes.push(c.clouds.map(fmtNuvem).join(' '));
    if (c.nsc) partes.push(L.nsc);
    return partes.join(' · ') || '—';
}

function rotuloGrupo(g, L) {
    if (g.tipo === 'BASE') return L.base;
    if (g.tipo === 'FM') return `${L.fm} ${ddhh(g.de)}`;
    if (g.tipo === 'BECMG') return L.becmg;
    if (g.tipo === 'TEMPO') return L.tempo;
    if (g.tipo === 'PROB TEMPO') return `${L.prob(g.prob)} · ${L.tempo.toLowerCase()}`;
    return L.prob(g.prob);
}

function renderTaf(taf, pistas, L) {
    const horas = horasDoTaf(taf);
    const temps = taf.temps.map(t => `<span class="wx-chip ${t.tipo === 'X' ? 'red' : 'blue'}">${t.tipo === 'X' ? L.tmax : L.tmin} ${t.val}°C ${L.as} ${ddhh(t.quando)}</span>`).join('');

    const cards = horas.map(h => {
        const e = h.estado;
        const cond = condicao(e);
        const piores = h.temporarios.map(g => condicao(aplicar(e, g.cond)));
        const pior = piores.includes('IMC') ? 'IMC' : cond;
        const teto = tetoDe(e);
        const rwy = cabeceiraFavorecida(e.wind, pistas);
        const tags = [];
        if (h.transicao) tags.push(`<span class="wx-tag becmg">BECMG</span>`);
        for (const g of h.temporarios) tags.push(`<span class="wx-tag ${g.tipo === 'TEMPO' ? 'tempo' : 'prob'}">${g.tipo === 'PROB TEMPO' ? `PROB${g.prob} TEMPO` : g.tipo === 'PROB' ? `PROB${g.prob}` : 'TEMPO'}</span>`);
        const extras = h.temporarios.map(g => `<div class="wx-hr-temp ${condicao(aplicar(e, g.cond)).toLowerCase()}">${esc(g.tokens.join(' '))}</div>`).join('');
        return `
            <div class="wx-hr ${pior.toLowerCase()}${h.agora ? ' now' : ''}">
                <div class="wx-hr-tags">${tags.join('')}</div>
                <div class="wx-hr-time">${String(h.t.getUTCHours()).padStart(2, '0')}Z${h.agora ? ` <small>${L.agora}</small>` : ''}</div>
                <div class="wx-hr-day">${String(h.t.getUTCDate()).padStart(2, '0')}</div>
                <div class="wx-hr-ic">${icone(iconeTempo(e), 24)}</div>
                <span class="wx-badge sm ${cond.toLowerCase()}">${cond}</span>
                <div class="wx-hr-line"><b>${e.wind ? fmtVento(e.wind, L).replace(' kt', '') : '--'}</b></div>
                ${rwy ? `<div class="wx-hr-rwy">${L.pista} ${rwy}</div>` : ''}
                <div class="wx-hr-line">${e.cavok ? 'CAVOK' : fmtVis(e.vis)}</div>
                <div class="wx-hr-line">${teto !== null ? `${L.teto} ${fmtFt(teto, L)}` : (e.clouds.length ? e.clouds.map(fmtNuvem).join(' ') : (e.cavok ? '' : 'NSC'))}</div>
                ${e.wx.length ? `<div class="wx-hr-line wx-hr-wx">${e.wx.map(w => decodeWx(w, L)).join(', ')}</div>` : ''}
                ${extras}
            </div>`;
    }).join('');

    const decod = taf.grupos.map(g => `
        <div class="wx-grp ${g.tipo.split(' ')[0].toLowerCase()}">
            <div class="wx-grp-head">
                <span class="wx-grp-type">${rotuloGrupo(g, L)}</span>
                <span class="wx-grp-time">${g.tipo === 'FM' ? '' : L.das(ddhh(g.de), ddhh(g.ate))}</span>
            </div>
            <div class="wx-grp-body">${resumoCondicoes(g.cond, L)}</div>
        </div>`).join('');

    const formatado = taf.raw.replace(/\s(FM\d{6}|BECMG|TEMPO|PROB\d{2}(?:\sTEMPO)?)(?=\s)/g, '\n  $1').replace(/\s(RMK)\s/, '\n  $1 ');

    return `
        <div class="wx-head">
            <div class="wx-title">
                ${icone('pressao')}
                <span>${L.taf}</span>
                <span class="wx-time">${L.emitido} ${ddhh(taf.emitido).replace('Z', '')}${String(taf.emitido.getUTCMinutes()).padStart(2, '0')}Z · ${L.validade} ${ddhh(taf.de)} – ${ddhh(taf.ate)}</span>
            </div>
        </div>
        ${temps ? `<div class="wx-alerts">${temps}</div>` : ''}
        ${horas.length ? `
            <div class="wx-section-title">${L.horaria} <small>${L.horariaNota}</small></div>
            <div class="wx-timeline">${cards}</div>` : ''}
        <details class="wx-details" open>
            <summary>${L.decodificado}</summary>
            <div class="wx-groups">${decod}</div>
        </details>
        <div class="wx-raw">
            <span class="wx-label">${L.tafBruto}</span>
            <code>${esc(formatado)}</code>
        </div>
    `;
}

function renderTafBruto(raw, L) {
    return `
        <div class="wx-head"><div class="wx-title">${icone('pressao')}<span>${L.taf}</span></div></div>
        <div class="wx-raw"><span class="wx-label">${L.tafBruto}</span><code>${esc(raw)}</code></div>`;
}
