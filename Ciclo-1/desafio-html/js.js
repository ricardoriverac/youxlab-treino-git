const caixas = document.querySelectorAll('.caixa');//onde colocar o X ou O
const mensagem = document.getElementById('mensagem');
const botaoReiniciar = document.getElementById('reiniciar');//reinicia a partida

// musica do jogo
const seletorMusica = document.getElementById('seletorMusica');
const audio = document.getElementById('audioFundo');

let jogadorAtual = 'X';//analiza aqual o jogador atual
let jogoAtivo = true;//define qual jogador ira jogar

//variacoes de possiçoes disponiveis para ganhar
const combinacoesVitoria = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8], 
    [0, 3, 6], 
    [1, 4, 7],
    [2, 5, 8], 
    [0, 4, 8], 
    [2, 4, 6]  
];

//verifica se teve uma vitoria apos ler as variaçoes de vitoria 
function verificarVitoria() {
    for (const combinacao of combinacoesVitoria) {
        const [a, b, c] = combinacao;
        if (
            caixas[a].textContent &&
            caixas[a].textContent === caixas[b].textContent &&
            caixas[a].textContent === caixas[c].textContent
        ) {
            return true;
        }
    }
    return false;
}

//verifica para ver se teve um empate
function verificarEmpate() {
    return [...caixas].every(caixa => caixa.textContent);
}

function cliqueCaixa(event) {
    const caixa = event.target;

    if (!jogoAtivo || caixa.textContent) {
        return;
    }

    caixa.textContent = jogadorAtual;

    //verifica quem ganhou apos ver quem esta nas determinada posiçoes para vitoria baseado em que jogador selecionou as determinadas posições
    if (verificarVitoria()) {
        const nome = jogadorAtual === 'X' ? document.getElementById('nome1').value || 'Jogador 1' 
                                          : document.getElementById('nome2').value || 'Jogador 2';
        mensagem.textContent = `${nome} venceu! 🎉`;
        jogoAtivo = false;
        return;
    }
    //termina a partida quando tiver um empate
    if (verificarEmpate()) {
        mensagem.textContent = 'Deu velha! 😐';
        jogoAtivo = false;
        return;
    }

    jogadorAtual = jogadorAtual === 'X' ? 'O' : 'X';// separa a condição do que acontece se ela for verdadeira
}

caixas.forEach(caixa => {
    caixa.addEventListener('click', cliqueCaixa);
});

//botão de reiniciar
botaoReiniciar.addEventListener('click', () => {
    caixas.forEach(caixa => caixa.textContent = '');
    jogadorAtual = 'X';
    jogoAtivo = true;
    mensagem.textContent = '';
});

//troca de musica
seletorMusica.addEventListener('change', function () {
    const musicaSelecionada = this.value;
    audio.src = musicaSelecionada;
    audio.play();
});