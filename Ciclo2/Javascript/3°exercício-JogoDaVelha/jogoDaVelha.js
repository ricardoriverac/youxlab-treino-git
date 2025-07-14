const jogadorX = document.getElementById("jogadorX");
const jogadorO = document.getElementById("jogadorO");

let jogadorAtual = "X";

let jogoAtivo = false;

let contador = 0;

let contadorPlacarX = 0;
let contadorPlacarO = 0;

function iniciarJogo() {
  jogoAtivo = true;
  let tabuleiro = document.getElementById("tabuleiro");
  tabuleiro.innerHTML = "";
  for (let i = 0; i < 9; i++) {
    const caixa = document.createElement("div");
    caixa.setAttribute("id", i);
    caixa.setAttribute("class", "caixa");
    caixa.addEventListener("click", marcarCaixa);
    tabuleiro.appendChild(caixa);
  }

}

function marcarCaixa(elemento) {
  const caixaMarcada = elemento.target;
  if (caixaMarcada.textContent !== "") {
    return;
  }
  if (caixaMarcada) {
    var status = document.getElementById("status");
    contador++;

    if (contador % 2 == 0) {
      caixaMarcada.textContent = "O";
      jogadorAtual = "O";
      if (jogadorX.value == "") {
        status.innerHTML = "Vez do jogador X";
      } else {
        status.innerHTML = `Vez de ${jogadorX.value}`;
      }
    } else {
      caixaMarcada.textContent = "X";
      jogadorAtual = "X";
      if (jogadorO.value == "") {
        status.innerHTML = "Vez do jogador O";
      } else {
        status.innerHTML = `Vez de ${jogadorO.value}`;
      }
    }
  }
  verificarVitoria();
  empate();
}

function empate() {
  const caixas= document.querySelectorAll(".caixa")
  console.log('caixas :>> ', caixas);
  if(Array.from(caixas).every(c => c.textContent !== '')){
    alert("Velha")
  }
}

function verificarVitoria() {
  const caixas = document.querySelectorAll(".caixa");
  const combinacoesVencedoras = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8], // Linhas
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8], // Colunas
    [0, 4, 8],
    [2, 4, 6], // Diagonais
  ];
  combinacoesVencedoras.forEach(([i, j, k]) => {
    const a = caixas[i].textContent;
    const b = caixas[j].textContent;
    const c = caixas[k].textContent;
    if (a && a == b && a == c) {
      jogoAtivo = false;
      if (a == "X") {
        contadorPlacarX++;
        document.getElementById("jogadorPlacarX").innerText = contadorPlacarX;
        if (jogadorX.value == "") {
          alert("Jogador 'X' GANHOU!!");
        } else {
          alert(`O jogador ${jogadorX.value} GANHOU!`);
        }
      } else if (a == "O") {
        contadorPlacarO++;
        document.getElementById("jogadorPlacarO").innerText = contadorPlacarO;
        if (jogadorO.value == "") {
          alert("Jogador 'O' GANHOU!!");
        } else {
          alert(`O jogador ${jogadorO.value} GANHOU!`);
        }
      }
      reiniciarJogo();
    }
  });
}

function reiniciarJogo() {
  contador = 0;
  jogadorAtual = "X";
  let status = document.getElementById("status");
  status.innerHTML = "";
  iniciarJogo();
}

function zerarPlacar() {
  contadorPlacarX = 0;
  document.getElementById("jogadorPlacarX").innerText = contadorPlacarX;
  contadorPlacarO = 0;
  document.getElementById("jogadorPlacarO").innerText = contadorPlacarO;
  reiniciarJogo();
}
