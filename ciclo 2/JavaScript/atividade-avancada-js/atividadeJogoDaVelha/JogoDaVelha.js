// joguinho da velha que deu trabal
const btnIniciar = document.getElementById("btnIniciar");
const btnReiniciar = document.getElementById("btnReiniciar");
const btnZerarPlacar = document.getElementById("btnZerarPlacar");

const inputJog1 = document.getElementById("inputJog1");
const inputJog2 = document.getElementById("inputJog2");

const placar = document.getElementById("status");
const tabuleiroDiv = document.getElementById("tabuleiro");

const placarX = document.getElementById("placarX");
const placarO = document.getElementById("placarO");

// variáveis do jogo
let tabuleiro = [];
let jogadorAtual = "X"; // x começa
let jogando = false;
let nomeX = ""; // nome do jogador x
let nomeO = ""; // nome do jogador o
let vitoriasX = 0; // vitórias de x
let vitoriasO = 0; // vitórias de o
const tamanho = 9; // tamanho do tabuleiro (9 casas)

// evento para iniciar o jogo
btnIniciar.onclick = () => {
  nomeX = inputJog1.value; // pega o nome do jogador x
  nomeO = inputJog2.value; // pega o nome do jogador o

  // verifica se os dois jogadores preencheram o nome
  if (nomeX === "" || nomeO === "") {
    alert("preencha os nomes dos dois jogadores!"); // alerta se algum nome estiver vazio
    return;
  }

  // cria o tabuleiro
  tabuleiroDiv.innerHTML = "";
  tabuleiro = [];

  // cria as casas do tabuleiro
  for (let i = 0; i < tamanho; i++) {
    const casa = document.createElement("div");
    casa.className = "casa"; // classe para cada casa
    casa.id = i; // id da casa
    casa.onclick = jogar; // chama a função jogar quando clicar na casa
    tabuleiroDiv.appendChild(casa);
    tabuleiro[i] = ""; // inicializa as casas vazias
  }

  jogadorAtual = "X"; // começa com x
  jogando = true; // começa o jogo
  placar.textContent = `vez de ${nomeX} (X)`; // exibe a vez de x
  atualizarPlacar(); // atualiza o placar
};

// evento para reiniciar o jogo
btnReiniciar.onclick = () => {

  // reinicia as casas do tabuleiro
  for (let i = 0; i < tamanho; i++) {
    tabuleiro[i] = "";
    document.getElementById(i).textContent = "";
  }

  jogadorAtual = "X"; // começa com x
  jogando = true; // reinicia o jogo
  placar.textContent = `vez de ${nomeX} (X)`; // exibe a vez de x
};

// evento para zerar o placar
btnZerarPlacar.onclick = () => {
  vitoriasX = 0; // reinicia vitórias de x
  vitoriasO = 0; // reinicia vitórias de o
  atualizarPlacar(); // atualiza o placar
};

// função para realizar uma jogada
function jogar() {
  if (!jogando) return; // se não estiver jogando, não faz nada

  const indice = Number(this.id); // pega o índice da casa clicada
  console.log(indice)

  if (tabuleiro[indice] !== "") return; // se a casa já estiver ocupada, não faz nada
  console.log(tabuleiro[indice])

  tabuleiro[indice] = jogadorAtual; // marca a casa com o jogador atual
  this.textContent = jogadorAtual; // exibe o símbolo (X ou O) na casa
  console.log(this.textContent)
  console.log(jogadorAtual)

  // verifica se algum jogador venceu
  if (checarVitoria()) {
    console.log(checarVitoria())
    jogando = false; // jogo acabou

    if (jogadorAtual === "X") vitoriasX++; // se x venceu, aumenta vitórias de x
    else vitoriasO++; // se o venceu, aumenta vitórias de o

    placar.textContent = `parabéns! ${jogadorAtual === "X" ? nomeX : nomeO} venceu!`; // exibe mensagem de vitória
    atualizarPlacar(); // atualiza o placar
    return;
  }

  // verifica se houve empate
  if (checarEmpate()) {
    jogando = false; // jogo acabou
    placar.textContent = "empate!"; // exibe mensagem de empate
    return;
  }

  // muda o jogador para o próximo
  jogadorAtual = jogadorAtual === "X" ? "O" : "X";
  placar.textContent = `vez de ${jogadorAtual === "X" ? nomeX : nomeO} (${jogadorAtual})`; // exibe a vez do próximo jogador
}

// função para verificar se algum jogador venceu
function checarVitoria() {
  const combinacoes = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // linhas
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // colunas
    [0, 4, 8], [2, 4, 6] // diagonais
  ];

  // verifica se alguma combinação de 3 casas tem o mesmo símbolo
  return combinacoes.some(([a, b, c]) =>
    tabuleiro[a] && tabuleiro[a] === tabuleiro[b] && tabuleiro[a] === tabuleiro[c]
  ); //compara de acordo com a tabela, ex: a tabelaa e tabelaa comfere se é igual a b, e c
}

// função para verificar se houve empate
function checarEmpate() {
  return tabuleiro.every(c => c !== ""); // verifica se todas as casas estão ocupadas
}

// função para atualizar o placar
function atualizarPlacar() {
  placarX.textContent = `${nomeX} (X): ${vitoriasX}`; // exibe as vitórias de x
  placarO.textContent = `${nomeO} (O): ${vitoriasO}`; // exibe as vitórias de o
}
