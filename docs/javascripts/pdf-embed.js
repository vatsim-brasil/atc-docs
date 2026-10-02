// PDFs embutidos (cartas visuais e AIC das TMAs). Navegadores sem visualizador de PDF
// embutido (a maioria dos celulares) mostram o iframe vazio; nesses, troca por um aviso
// apontando para os botões de abrir/baixar, que ficam sempre visíveis acima.
document$.subscribe(({ body }) => {
    if (navigator.pdfViewerEnabled !== false) return;
    const en = document.documentElement.lang === 'en';
    body.querySelectorAll('.pdf-embed').forEach((caixa) => {
        if (caixa.dataset.pronto) return;
        caixa.dataset.pronto = '1';
        const aviso = document.createElement('p');
        aviso.className = 'pdf-aviso';
        aviso.textContent = en
            ? 'This browser cannot display PDFs inside the page. Use the buttons above to open or download the document.'
            : 'Este navegador não exibe PDF dentro da página. Use os botões acima para abrir ou baixar o documento.';
        caixa.replaceChildren(aviso);
    });
});
