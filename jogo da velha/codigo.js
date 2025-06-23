const caixas = document.querySelectorAll('.caixa');
const mensagem = document.getElementById('mensagem');
const botaoReiniciar = document.getElementById('reiniciar');

let jogadorAtual = 'X';
let jogoAtivo = true;


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


function verificarVitoria() {
    for (const combinacao of combinacoesVitoria) {
        const [a, b, c] = combinacao;
        if (
            