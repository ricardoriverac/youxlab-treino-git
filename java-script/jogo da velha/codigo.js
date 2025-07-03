const mensagem = document.getElementById('mensagem');
const botaoReiniciar = document.getElementById('reiniciar');
const nome1 = document.getElementById('nome1');
const nome2 = document.getElementById('nome2');
const placarX = document.getElementById('placarX');
const placarO = document.getElementById('placarO');

let jogadorAtual = 'X';
let jogoAtivo = false;
let jogoIniciado = false;

let nomesJogadores = { X: 'X', O: 'O' };
let pontuacao = { X: 0, O: 0 };

function iniciar() {
    if (!jogoIniciado) {
        const nomeX = nome1.value.trim() || 'Jogador X';
        const nomeO = nome2.value.trim() || 'Jogador O';
        nomesJogadores = { X: nomeX, O: nomeO };
        jogoIniciado = true;
    }

    criarTabuleiro();
}



function reiniciarJogo() {
    criarTabuleiro();
}

function criarTabuleiro() {
    const tabuleiro = document.getElementById('jogo');
    tabuleiro.innerHTML = "";

    for (let i = 0; i < 9; i++) {
        const quadrado = document.createElement('div');
        quadrado.classList.add('caixa');
        quadrado.setAttribute('data-index', i);
        quadrado.addEventListener('click', cliqueQuadrado);
        tabuleiro.appendChild(quadrado);
    }

    jogadorAtual = 'X';
    jogoAtivo = true;
    mensagem.textContent = `Vez de ${nomesJogadores[jogadorAtual]}`;
    botaoReiniciar.style.display = 'none';
}

function cliqueQuadrado(event) {
    const quadrado = event.target;
    if (!jogoAtivo || quadrado.textContent !== '') return;

    quadrado.textContent = jogadorAtual;

    if (verificarVitoria()) return;

    if (verificarEmpate()) {
        mensagem.textContent = 'Empate!';
        jogoAtivo = false;
        botaoReiniciar.style.display = 'block';
        return;
    }

    jogadorAtual = jogadorAtual === 'X' ? 'O' : 'X';
    mensagem.textContent = `Vez de ${nomesJogadores[jogadorAtual]}`;
}

function verificarVitoria() {
    const quadrados = document.querySelectorAll('.caixa');
    const combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ];

    for (let [a,b,c] of combinacoes) {
        const valorA = quadrados[a].textContent;
        const valorB = quadrados[b].textContent;
        const valorC = quadrados[c].textContent;

        if (valorA && valorA === valorB && valorA === valorC) {
            jogoAtivo = false;
            mensagem.textContent = `${nomesJogadores[valorA]} venceu!`;
            pontuacao[valorA]++;
            atualizarPlacar();
            botaoReiniciar.style.display = 'block';
            return true;
        }
    }

    return false;
}

function verificarEmpate() {
    const quadrados = document.querySelectorAll('.caixa');
    return [...quadrados].every(q => q.textContent !== '');
}

function atualizarPlacar() {
    placarX.textContent = `${nomesJogadores.X}: ${pontuacao.X}`;
    placarO.textContent = `${nomesJogadores.O}: ${pontuacao.O}`;
}
