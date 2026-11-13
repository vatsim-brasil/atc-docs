// Componentes interativos da seção Fundamentos: trilha de etapas, checklist com
// progresso, quiz, simulador de rádio e perfil de voo/escada de ratings.
// O markdown traz todo o conteúdo; sem JS ele continua legível, só sem a interação.
(function () {
    const TEXTOS = {
        pt: {
            etapas: (f, t) => `${f} de ${t} etapas concluídas`,
            itens: (f, t) => `${f} de ${t} itens marcados`,
            concluir: 'Marcar como concluída',
            desfazer: 'Desmarcar',
            concluida: 'Concluída',
            recomecar: 'Recomeçar',
            limpar: 'Limpar marcações',
            pergunta: (i, t) => `Pergunta ${i} de ${t}`,
            certo: 'Correto!',
            errado: 'Não é essa.',
            placar: (a, t) => `Você acertou ${a} de ${t}.`,
            placarParcial: (r, t) => `${r} de ${t} respondidas`,
            refazer: 'Refazer o quiz',
            ouvir: 'Acompanhar',
            comoPiloto: 'Praticar como piloto',
            comoAtc: 'Praticar como controlador',
            proxima: 'Próxima transmissão',
            conferir: 'Conferir minha resposta',
            tudo: 'Mostrar tudo',
            suaVez: 'Sua vez: fale a mensagem em voz alta e toque para conferir.',
            anterior: 'Anterior',
            seguinte: 'Próximo',
            modo: 'Modo do simulador',
        },
        en: {
            etapas: (f, t) => `${f} of ${t} steps completed`,
            itens: (f, t) => `${f} of ${t} items checked`,
            concluir: 'Mark as done',
            desfazer: 'Unmark',
            concluida: 'Done',
            recomecar: 'Start over',
            limpar: 'Clear checks',
            pergunta: (i, t) => `Question ${i} of ${t}`,
            certo: 'Correct!',
            errado: 'Not this one.',
            placar: (a, t) => `You got ${a} of ${t} right.`,
            placarParcial: (r, t) => `${r} of ${t} answered`,
            refazer: 'Retake the quiz',
            ouvir: 'Follow along',
            comoPiloto: 'Practice as pilot',
            comoAtc: 'Practice as controller',
            proxima: 'Next transmission',
            conferir: 'Check my answer',
            tudo: 'Show all',
            suaVez: 'Your turn: say the message out loud, then tap to check.',
            anterior: 'Previous',
            seguinte: 'Next',
            modo: 'Simulator mode',
        },
    };

    const lingua = () => ((document.documentElement.lang || 'pt').startsWith('en') ? 'en' : 'pt');

    // localStorage pode faltar (aba privada, bloqueio de cookies): o componente
    // funciona igual, só não lembra o progresso.
    const memoria = {
        ler(chave) {
            try { return JSON.parse(localStorage.getItem(chave)) || null; } catch (e) { return null; }
        },
        gravar(chave, valor) {
            try { localStorage.setItem(chave, JSON.stringify(valor)); } catch (e) { /* sem persistência */ }
        },
    };

    function el(tag, classe, texto) {
        const e = document.createElement(tag);
        if (classe) e.className = classe;
        if (texto != null) e.textContent = texto;
        return e;
    }

    function botao(classe, texto) {
        const b = el('button', classe, texto);
        b.type = 'button';
        return b;
    }

    function barra(rotulo) {
        const caixa = el('div', 'vb-progresso');
        const texto = el('span', 'vb-progresso-texto');
        const trilho = el('div', 'vb-progresso-trilho');
        const cheio = el('div', 'vb-progresso-cheio');
        trilho.setAttribute('role', 'progressbar');
        trilho.setAttribute('aria-label', rotulo);
        trilho.setAttribute('aria-valuemin', '0');
        trilho.append(cheio);
        caixa.append(texto, trilho);
        return {
            caixa,
            atualizar(feitos, total, frase) {
                texto.textContent = frase;
                trilho.setAttribute('aria-valuemax', String(total));
                trilho.setAttribute('aria-valuenow', String(feitos));
                cheio.style.width = total ? `${(feitos / total) * 100}%` : '0';
                caixa.classList.toggle('vb-progresso--completo', total > 0 && feitos === total);
            },
        };
    }

    // ---------------------------------------------------------------- Trilha
    // <div class="vb-trilha" data-chave="..."> com filhos .vb-passo, cada um
    // começando por um título (h3). As etapas viram um acordeão numerado.
    function trilha(raiz, t) {
        const passos = [...raiz.querySelectorAll(':scope > .vb-passo')];
        if (!passos.length) return;
        const chave = `vb-trilha-${raiz.dataset.chave || location.pathname}`;
        const feitos = new Set(memoria.ler(chave) || []);
        const prog = barra(raiz.dataset.titulo || 'Progresso');
        const zerar = botao('vb-link-botao', t.recomecar);
        const topo = el('div', 'vb-trilha-topo');
        topo.append(prog.caixa, zerar);
        raiz.prepend(topo);

        const cabs = passos.map((passo, i) => {
            const titulo = passo.querySelector('h2, h3, h4');
            const corpo = el('div', 'vb-passo-corpo');
            [...passo.childNodes].forEach((n) => { if (n !== titulo) corpo.append(n); });
            const id = titulo ? titulo.id : '';
            if (id) { titulo.removeAttribute('id'); passo.id = id; }
            corpo.id = `${chave}-${i}`;

            const cab = botao('vb-passo-cab');
            cab.setAttribute('aria-controls', corpo.id);
            const num = el('span', 'vb-passo-num', String(i + 1));
            const nome = el('span', 'vb-passo-nome', titulo ? titulo.textContent.replace(/¶$/, '').trim() : '');
            const estado = el('span', 'vb-passo-estado', t.concluida);
            cab.append(num, nome, estado);

            const marcar = botao('md-button vb-passo-marcar');
            marcar.addEventListener('click', () => {
                if (feitos.has(i)) feitos.delete(i); else feitos.add(i);
                memoria.gravar(chave, [...feitos]);
                const avancar = feitos.has(i);
                atualizar();
                if (avancar) {
                    abrir(i, false);
                    const prox = passos.findIndex((_, j) => j > i && !feitos.has(j));
                    if (prox >= 0) {
                        abrir(prox, true);
                        passos[prox].scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                    }
                }
            });
            corpo.append(marcar);
            cab.addEventListener('click', () => abrir(i, cab.getAttribute('aria-expanded') !== 'true'));

            passo.replaceChildren(cab, corpo);
            return { cab, corpo, marcar };
        });

        function abrir(i, sim) {
            cabs[i].cab.setAttribute('aria-expanded', sim ? 'true' : 'false');
            cabs[i].corpo.hidden = !sim;
        }

        function atualizar() {
            passos.forEach((p, i) => {
                const feito = feitos.has(i);
                p.classList.toggle('vb-passo--feito', feito);
                cabs[i].marcar.textContent = feito ? t.desfazer : t.concluir;
                cabs[i].marcar.classList.toggle('md-button--primary', !feito);
            });
            prog.atualizar(feitos.size, passos.length, t.etapas(feitos.size, passos.length));
        }

        zerar.addEventListener('click', () => {
            feitos.clear();
            memoria.gravar(chave, []);
            atualizar();
            passos.forEach((_, i) => abrir(i, i === 0));
        });

        atualizar();
        const alvo = location.hash ? passos.findIndex((p) => `#${p.id}` === location.hash) : -1;
        const primeiro = passos.findIndex((_, i) => !feitos.has(i));
        passos.forEach((_, i) => abrir(i, i === (alvo >= 0 ? alvo : primeiro)));
    }

    // ------------------------------------------------------------- Checklist
    // Lista de tarefas (pymdownx.tasklist) dentro de <div class="vb-checklist">.
    function checklist(raiz, t) {
        const caixas = [...raiz.querySelectorAll('input[type="checkbox"]')];
        if (!caixas.length) return;
        const chave = `vb-checklist-${raiz.dataset.chave || location.pathname}`;
        const salvo = memoria.ler(chave) || [];
        const prog = barra('Checklist');
        const limpar = botao('vb-link-botao', t.limpar);
        const topo = el('div', 'vb-trilha-topo');
        topo.append(prog.caixa, limpar);
        raiz.prepend(topo);

        const atualizar = () => {
            const n = caixas.filter((c) => c.checked).length;
            prog.atualizar(n, caixas.length, t.itens(n, caixas.length));
            caixas.forEach((c) => c.closest('li').classList.toggle('vb-item-feito', c.checked));
        };
        caixas.forEach((c, i) => {
            c.disabled = false;
            c.removeAttribute('disabled');
            c.checked = !!salvo[i];
            c.addEventListener('change', () => {
                memoria.gravar(chave, caixas.map((x) => x.checked));
                atualizar();
            });
        });
        limpar.addEventListener('click', () => {
            caixas.forEach((c) => { c.checked = false; });
            memoria.gravar(chave, []);
            atualizar();
        });
        atualizar();
    }

    // ------------------------------------------------------------------ Quiz
    // .vb-pergunta[data-resposta=N]: enunciado, lista numerada de opções e um
    // .vb-explica com o comentário. N começa em 1.
    function quiz(raiz, t) {
        const perguntas = [...raiz.querySelectorAll(':scope > .vb-pergunta')];
        if (!perguntas.length) return;
        const respostas = new Map();
        const placar = el('div', 'vb-quiz-placar');
        const texto = el('p', 'vb-quiz-placar-texto');
        const refazer = botao('md-button', t.refazer);
        placar.append(texto, refazer);
        raiz.append(placar);

        const estados = perguntas.map((p, i) => {
            const certa = Number(p.dataset.resposta) - 1;
            const lista = p.querySelector('ol, ul');
            const explica = p.querySelector('.vb-explica');
            const selo = el('p', 'vb-pergunta-selo', t.pergunta(i + 1, perguntas.length));
            p.prepend(selo);
            const veredito = el('p', 'vb-veredito');
            veredito.setAttribute('aria-live', 'polite');
            if (explica) explica.before(veredito); else p.append(veredito);

            const opcoes = el('div', 'vb-opcoes');
            const botoes = [...lista.children].map((li, j) => {
                const b = botao('vb-opcao');
                b.innerHTML = li.innerHTML;
                b.addEventListener('click', () => responder(i, j));
                opcoes.append(b);
                return b;
            });
            lista.replaceWith(opcoes);
            return { p, certa, botoes, explica, veredito };
        });

        function responder(i, j) {
            if (respostas.has(i)) return;
            const e = estados[i];
            respostas.set(i, j === e.certa);
            e.botoes.forEach((b, k) => {
                b.disabled = true;
                if (k === e.certa) b.classList.add('vb-opcao--certa');
                else if (k === j) b.classList.add('vb-opcao--errada');
            });
            e.p.classList.add(j === e.certa ? 'vb-pergunta--certa' : 'vb-pergunta--errada');
            e.veredito.textContent = j === e.certa ? t.certo : t.errado;
            if (e.explica) e.explica.hidden = false;
            atualizar();
        }

        function atualizar() {
            const acertos = [...respostas.values()].filter(Boolean).length;
            const fim = respostas.size === perguntas.length;
            texto.textContent = fim ? t.placar(acertos, perguntas.length) : t.placarParcial(respostas.size, perguntas.length);
            placar.classList.toggle('vb-quiz-placar--fim', fim);
            refazer.hidden = !respostas.size;
        }

        refazer.addEventListener('click', () => {
            respostas.clear();
            estados.forEach((e) => {
                e.p.classList.remove('vb-pergunta--certa', 'vb-pergunta--errada');
                e.veredito.textContent = '';
                if (e.explica) e.explica.hidden = true;
                e.botoes.forEach((b) => { b.disabled = false; b.classList.remove('vb-opcao--certa', 'vb-opcao--errada'); });
            });
            atualizar();
            raiz.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });

        estados.forEach((e) => { if (e.explica) e.explica.hidden = true; });
        atualizar();
    }

    // ----------------------------------------------------------------- Rádio
    // Diálogo com .comms-pilot, .comms-atc e .vb-cena (narração). As mensagens
    // aparecem uma a uma; no modo de prática, as falas do papel escolhido ficam
    // encobertas até o usuário conferir.
    function radio(raiz, t) {
        const itens = [...raiz.querySelectorAll(':scope > .comms-pilot, :scope > .comms-atc, :scope > .vb-cena')];
        if (!itens.length) return;
        let papel = '';
        let mostrados = 1;

        const modos = el('div', 'vb-radio-modos');
        modos.setAttribute('role', 'group');
        modos.setAttribute('aria-label', t.modo);
        const opcoesModo = [['', t.ouvir], ['comms-pilot', t.comoPiloto], ['comms-atc', t.comoAtc]].map(([valor, rot]) => {
            const b = botao('vb-segmento', rot);
            b.addEventListener('click', () => { papel = valor; reiniciar(); });
            modos.append(b);
            return [valor, b];
        });

        const controles = el('div', 'vb-radio-controles');
        const contador = el('span', 'vb-radio-contador');
        const proxima = botao('md-button md-button--primary', t.proxima);
        const tudo = botao('md-button', t.tudo);
        const zerar = botao('vb-link-botao', t.recomecar);
        controles.append(proxima, tudo, zerar, contador);
        raiz.prepend(modos);
        raiz.append(controles);

        itens.forEach((item) => {
            item.addEventListener('click', () => {
                if (item.classList.contains('vb-encoberta')) { item.classList.remove('vb-encoberta'); desenhar(); }
            });
            item.addEventListener('keydown', (ev) => {
                if ((ev.key === 'Enter' || ev.key === ' ') && item.classList.contains('vb-encoberta')) {
                    ev.preventDefault();
                    item.classList.remove('vb-encoberta');
                    desenhar();
                }
            });
        });

        const encobrir = (item) => {
            if (papel && item.classList.contains(papel)) {
                item.classList.add('vb-encoberta');
                item.dataset.dica = t.suaVez;
                item.tabIndex = 0;
            }
        };

        function desenhar() {
            itens.forEach((item, i) => {
                item.hidden = i >= mostrados;
                if (!item.classList.contains('vb-encoberta')) item.removeAttribute('tabindex');
            });
            const ultimo = itens[mostrados - 1];
            const pendente = ultimo && ultimo.classList.contains('vb-encoberta');
            proxima.textContent = pendente ? t.conferir : t.proxima;
            proxima.disabled = !pendente && mostrados >= itens.length;
            tudo.disabled = mostrados >= itens.length && !itens.some((x) => x.classList.contains('vb-encoberta'));
            contador.textContent = `${mostrados}/${itens.length}`;
            opcoesModo.forEach(([valor, b]) => b.setAttribute('aria-pressed', valor === papel ? 'true' : 'false'));
        }

        function reiniciar() {
            mostrados = 1;
            itens.forEach((item) => { item.classList.remove('vb-encoberta'); delete item.dataset.dica; });
            encobrir(itens[0]);
            desenhar();
        }

        proxima.addEventListener('click', () => {
            const ultimo = itens[mostrados - 1];
            if (ultimo.classList.contains('vb-encoberta')) {
                ultimo.classList.remove('vb-encoberta');
            } else if (mostrados < itens.length) {
                encobrir(itens[mostrados]);
                mostrados += 1;
                itens[mostrados - 1].hidden = false;
                itens[mostrados - 1].scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
            desenhar();
        });
        tudo.addEventListener('click', () => {
            mostrados = itens.length;
            itens.forEach((item) => item.classList.remove('vb-encoberta'));
            desenhar();
        });
        zerar.addEventListener('click', reiniciar);
        reiniciar();
    }

    // ---------------------------------------------------------------- Perfil
    // .vb-perfil[data-forma="voo"|"degraus"] com <section data-sigla data-alt
    // data-nome>. Desenha o perfil (voo) ou a escada (ratings) com um botão por
    // seção; o painel abaixo mostra uma seção por vez.
    function perfil(raiz, t) {
        const secoes = [...raiz.querySelectorAll(':scope > section')];
        if (!secoes.length) return;
        const degraus = raiz.dataset.forma === 'degraus';
        const n = secoes.length;
        const alts = secoes.map((s) => Number(s.dataset.alt || 0));
        const max = Math.max(1, ...alts);
        const pts = alts.map((a, i) => [((i + 0.5) / n) * 1000, 76 - (a / max) * 56]);

        let d = `M ${pts[0][0]} ${pts[0][1]}`;
        for (let i = 1; i < n; i += 1) {
            const [x0, y0] = pts[i - 1];
            const [x1, y1] = pts[i];
            if (degraus) {
                const meio = (x0 + x1) / 2;
                d += ` L ${meio} ${y0} L ${meio} ${y1} L ${x1} ${y1}`;
            } else {
                const meio = (x0 + x1) / 2;
                d += ` C ${meio} ${y0} ${meio} ${y1} ${x1} ${y1}`;
            }
        }

        const mapa = el('div', `vb-perfil-mapa${degraus ? ' vb-perfil-mapa--degraus' : ''}`);
        mapa.setAttribute('role', 'tablist');
        const svgNS = 'http://www.w3.org/2000/svg';
        const svg = document.createElementNS(svgNS, 'svg');
        svg.setAttribute('viewBox', '0 0 1000 100');
        svg.setAttribute('preserveAspectRatio', 'none');
        svg.setAttribute('aria-hidden', 'true');
        if (!degraus) {
            const chao = document.createElementNS(svgNS, 'line');
            chao.setAttribute('x1', '0'); chao.setAttribute('x2', '1000');
            chao.setAttribute('y1', '76'); chao.setAttribute('y2', '76');
            chao.setAttribute('class', 'vb-perfil-chao');
            svg.append(chao);
        }
        const linha = document.createElementNS(svgNS, 'path');
        linha.setAttribute('d', d);
        linha.setAttribute('class', 'vb-perfil-linha');
        svg.append(linha);
        mapa.append(svg);

        const painel = el('div', 'vb-perfil-painel');
        const nav = el('div', 'vb-perfil-nav');
        const ant = botao('vb-link-botao', `← ${t.anterior}`);
        const prox = botao('vb-link-botao', `${t.seguinte} →`);
        nav.append(ant, prox);

        const botoes = secoes.map((s, i) => {
            const b = botao('vb-perfil-ponto');
            b.setAttribute('role', 'tab');
            b.style.left = `${pts[i][0] / 10}%`;
            b.style.top = `${pts[i][1]}%`;
            b.append(el('span', 'vb-perfil-sigla', s.dataset.sigla || String(i + 1)));
            if (s.dataset.nome) b.append(el('span', 'vb-perfil-nome', s.dataset.nome));
            b.title = s.dataset.nome || s.dataset.sigla || '';
            b.addEventListener('click', () => selecionar(i));
            b.addEventListener('keydown', (ev) => {
                if (ev.key === 'ArrowRight') { ev.preventDefault(); selecionar(Math.min(n - 1, i + 1), true); }
                if (ev.key === 'ArrowLeft') { ev.preventDefault(); selecionar(Math.max(0, i - 1), true); }
            });
            mapa.append(b);
            s.setAttribute('role', 'tabpanel');
            painel.append(s);
            return b;
        });
        painel.append(nav);

        let atual = 0;
        function selecionar(i, focar) {
            atual = i;
            secoes.forEach((s, j) => { s.hidden = j !== i; });
            botoes.forEach((b, j) => {
                b.setAttribute('aria-selected', j === i ? 'true' : 'false');
                b.tabIndex = j === i ? 0 : -1;
                b.classList.toggle('vb-perfil-ponto--passado', j < i);
            });
            ant.disabled = i === 0;
            prox.disabled = i === n - 1;
            if (focar) botoes[i].focus();
        }
        ant.addEventListener('click', () => selecionar(Math.max(0, atual - 1)));
        prox.addEventListener('click', () => selecionar(Math.min(n - 1, atual + 1)));

        raiz.replaceChildren(mapa, painel);
        selecionar(0);
    }

    const COMPONENTES = [
        ['.vb-trilha', trilha],
        ['.vb-checklist', checklist],
        ['.vb-quiz', quiz],
        ['.vb-radio', radio],
        ['.vb-perfil', perfil],
    ];

    function iniciar(body) {
        const t = TEXTOS[lingua()];
        COMPONENTES.forEach(([seletor, montar]) => {
            body.querySelectorAll(seletor).forEach((raiz) => {
                if (raiz.dataset.pronto) return;
                raiz.dataset.pronto = '1';
                raiz.classList.add('vb-pronto');
                montar(raiz, t);
            });
        });
    }

    if (typeof document$ !== 'undefined') {
        document$.subscribe(({ body }) => iniciar(body));
    } else {
        document.addEventListener('DOMContentLoaded', () => iniciar(document.body));
    }
})();
