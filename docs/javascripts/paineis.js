// Painéis de duas partes: lista agrupada à esquerda, um item por vez à direita. Substituem
// abas com muitos itens (cartas visuais, setores do APP), que os usuários achavam confusas.
// O markdown traz o conteúdo completo; sem JS ele continua legível, só sem a lista.

// itens: [{ grupo, rotulo, titulo, nivel }]; mostrar(item) atualiza o painel à direita.
// Os grupos aparecem na ordem do primeiro item de cada um.
function montarPainel(raiz, { itens, titulosGrupo, rotuloNav, painel, topo, mostrar }) {
    const nav = document.createElement('nav');
    nav.className = 'lv-nav';
    nav.setAttribute('aria-label', rotuloNav);

    const botoes = [];
    const selecionar = (i) => {
        botoes.forEach((b, j) => b.setAttribute('aria-current', j === i ? 'true' : 'false'));
        mostrar(itens[i], i);
    };

    [...new Set(itens.map((c) => c.grupo))].forEach((grupo) => {
        const cab = document.createElement('p');
        cab.className = 'lv-grupo';
        cab.textContent = titulosGrupo[grupo] || grupo;
        const lista = document.createElement('div');
        lista.className = 'lv-lista';
        lista.dataset.grupo = grupo;
        nav.append(cab, lista);
        itens.forEach((c, i) => {
            if (c.grupo !== grupo) return;
            const b = document.createElement('button');
            b.type = 'button';
            b.className = 'lv-item';
            if (c.nivel) b.dataset.nivel = c.nivel;
            b.textContent = c.rotulo;
            b.title = c.titulo;
            b.addEventListener('click', () => selecionar(i));
            botoes[i] = b;
            lista.append(b);
        });
    });

    const lado = document.createElement('div');
    lado.className = 'lv-painel';
    lado.append(topo, ...painel);
    raiz.replaceChildren(nav, lado);
    raiz.classList.add('lv');
    selecionar(0);
}

function topoPainel(...filhos) {
    const topo = document.createElement('div');
    topo.className = 'lv-topo';
    topo.append(...filhos);
    return topo;
}

// Cartas visuais das TMAs com várias CCV. Em navegadores sem visualizador de PDF fica
// só a lista de links, com um aviso.
document$.subscribe(({ body }) => {
    body.querySelectorAll('.ccv-viewer').forEach((viewer) => {
        if (viewer.dataset.pronto) return;
        viewer.dataset.pronto = '1';

        const en = viewer.dataset.lang === 'en';
        const cartas = [...viewer.querySelectorAll('a')].map((a) => {
            const nome = a.textContent.trim();
            const m = nome.match(/^CCV (REA|REH)\s+(.*)$/);
            return { url: a.href, titulo: nome, grupo: m ? m[1] : '', rotulo: m ? m[2] : nome };
        });
        if (!cartas.length) return;

        if (navigator.pdfViewerEnabled === false) {
            const aviso = document.createElement('p');
            aviso.className = 'pdf-aviso';
            aviso.textContent = en
                ? 'This browser cannot display PDFs inside the page. Use the links above to open each chart.'
                : 'Este navegador não exibe PDF dentro da página. Use os links acima para abrir cada carta.';
            viewer.append(aviso);
            return;
        }

        const titulo = document.createElement('strong');
        titulo.className = 'lv-titulo';
        const abrir = document.createElement('a');
        abrir.className = 'md-button md-button--primary lv-abrir';
        abrir.target = '_blank';
        abrir.rel = 'noopener';
        abrir.textContent = en ? 'Open in new tab' : 'Abrir em nova aba';
        const iframe = document.createElement('iframe');
        iframe.className = 'pdf-iframe';
        iframe.title = 'PDF';

        montarPainel(viewer, {
            itens: cartas,
            rotuloNav: en ? 'Visual charts' : 'Cartas visuais',
            titulosGrupo: {
                REA: en ? 'REA · Aircraft' : 'REA · Aeronaves',
                REH: en ? 'REH · Helicopters' : 'REH · Helicópteros',
                '': en ? 'Charts' : 'Cartas',
            },
            topo: topoPainel(titulo, abrir),
            painel: [iframe],
            mostrar: (c) => {
                titulo.textContent = c.titulo;
                abrir.href = c.url;
                iframe.src = c.url + '#view=FitH';
            },
        });
    });
});

// Setorização do APP: setor total, posições combinadas e setores elementares num só painel.
// Cada <figure> traz data-grupo, data-titulo, data-info e, opcionalmente, data-nivel
// (posição combinada contida em outra).
document$.subscribe(({ body }) => {
    body.querySelectorAll('.setor-viewer').forEach((viewer) => {
        if (viewer.dataset.pronto) return;
        viewer.dataset.pronto = '1';

        const en = viewer.dataset.lang === 'en';
        const figuras = [...viewer.querySelectorAll(':scope > figure')];
        if (!figuras.length) return;
        const itens = figuras.map((f) => ({
            figura: f,
            grupo: f.dataset.grupo,
            rotulo: f.dataset.titulo,
            titulo: f.dataset.titulo,
            info: f.dataset.info || '',
            nivel: f.dataset.nivel,
        }));

        const titulo = document.createElement('strong');
        titulo.className = 'lv-titulo';
        const info = document.createElement('span');
        info.className = 'lv-info';
        const cabeca = document.createElement('div');
        cabeca.append(titulo, info);

        montarPainel(viewer, {
            itens,
            rotuloNav: en ? 'APP sectors' : 'Setores do APP',
            titulosGrupo: {
                total: en ? 'Whole TMA' : 'Setor total',
                comb: en ? 'Combined sectors' : 'Setores combinados',
                elem: en ? 'Sectors' : 'Setores',
            },
            topo: topoPainel(cabeca),
            painel: figuras,
            mostrar: (item) => {
                titulo.textContent = item.titulo;
                info.textContent = item.info;
                figuras.forEach((f) => { f.hidden = f !== item.figura; });
            },
        });
    });
});
