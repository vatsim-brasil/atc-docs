// PDFs embutidos (cartas visuais das TMAs). Navegadores sem visualizador de PDF
// embutido (a maioria dos celulares) mostram o iframe vazio; nesses, troca por um aviso
// apontando para o botão de abrir, que fica sempre visível acima.
document$.subscribe(({ body }) => {
    if (navigator.pdfViewerEnabled !== false) return;
    const en = document.documentElement.lang === 'en';
    body.querySelectorAll('.pdf-embed').forEach((caixa) => {
        if (caixa.dataset.pronto) return;
        caixa.dataset.pronto = '1';
        const aviso = document.createElement('p');
        aviso.className = 'pdf-aviso';
        aviso.textContent = en
            ? 'This browser cannot display PDFs inside the page. Use the button above to open the document.'
            : 'Este navegador não exibe PDF dentro da página. Use o botão acima para abrir o documento.';
        caixa.replaceChildren(aviso);
    });
});

// Visualizador das cartas visuais das TMAs com várias CCV: lista agrupada (REA/REH) à
// esquerda e um único PDF à direita. O markdown traz só a lista de links, que continua
// funcionando sem JS e em navegadores sem visualizador de PDF.
document$.subscribe(({ body }) => {
    body.querySelectorAll('.ccv-viewer').forEach((viewer) => {
        if (viewer.dataset.pronto) return;
        viewer.dataset.pronto = '1';

        const en = viewer.dataset.lang === 'en';
        const cartas = [...viewer.querySelectorAll('a')].map((a) => {
            const nome = a.textContent.trim();
            const m = nome.match(/^CCV (REA|REH)\s+(.*)$/);
            return { url: a.href, nome, grupo: m ? m[1] : '', rotulo: m ? m[2] : nome };
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

        const titulosGrupo = {
            REA: en ? 'REA · Aircraft' : 'REA · Aeronaves',
            REH: en ? 'REH · Helicopters' : 'REH · Helicópteros',
            '': en ? 'Charts' : 'Cartas',
        };

        const nav = document.createElement('nav');
        nav.className = 'ccv-nav';
        nav.setAttribute('aria-label', en ? 'Visual charts' : 'Cartas visuais');

        const painel = document.createElement('div');
        painel.className = 'ccv-painel';
        const topo = document.createElement('div');
        topo.className = 'ccv-topo';
        const titulo = document.createElement('strong');
        titulo.className = 'ccv-titulo';
        const abrir = document.createElement('a');
        abrir.className = 'md-button md-button--primary ccv-abrir';
        abrir.target = '_blank';
        abrir.rel = 'noopener';
        abrir.textContent = en ? 'Open in new tab' : 'Abrir em nova aba';
        topo.append(titulo, abrir);
        const iframe = document.createElement('iframe');
        iframe.className = 'pdf-iframe';
        iframe.title = 'PDF';
        painel.append(topo, iframe);

        const botoes = [];
        const selecionar = (i) => {
            const c = cartas[i];
            botoes.forEach((b, j) => b.setAttribute('aria-current', j === i ? 'true' : 'false'));
            titulo.textContent = c.nome;
            abrir.href = c.url;
            iframe.src = c.url + '#view=FitH';
        };

        [...new Set(cartas.map((c) => c.grupo))].forEach((grupo) => {
            const cab = document.createElement('p');
            cab.className = 'ccv-grupo';
            cab.textContent = titulosGrupo[grupo] || grupo;
            nav.append(cab);
            cartas.forEach((c, i) => {
                if (c.grupo !== grupo) return;
                const b = document.createElement('button');
                b.type = 'button';
                b.className = 'ccv-item';
                b.textContent = c.rotulo;
                b.title = c.nome;
                b.addEventListener('click', () => selecionar(i));
                botoes[i] = b;
                nav.append(b);
            });
        });

        viewer.replaceChildren(nav, painel);
        viewer.classList.add('ccv-viewer--ativo');
        selecionar(0);
    });
});
