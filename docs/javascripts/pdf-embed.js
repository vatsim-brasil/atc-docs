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
