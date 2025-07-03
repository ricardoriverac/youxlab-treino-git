const mensagem = document.getElementById('mensagem');
const botaoReiniciar = document.getElementById('reiniciar');

let jogadorAtual = 'X';
let jogoAtivo = false;

function iniciar(){
    const tabuleiro = document.getElementById('jogo');
    const nome1 = document.getElementById('nome1')
    const nome2 = document.getElementById('nome2')
    const start = document.getElementById('Jogar')
    tabuleiro.innerHTML="";
    for (let i=0; i<9; i++) {
        const quadrado = document.createElement('div')
        quadrado.setAttribute('id', 'caixa')
        quadrado.setAttribute('data-index', i)
        tabuleiro.appendChild(quadrado)
        }
    jogoAtivo = true   
    }


