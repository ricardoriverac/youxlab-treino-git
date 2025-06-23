const btnAdd = document.getElementById("jogador1");
const jogador1 = document.querySelector("#nome1");
const jogador2 = document.querySelector("#nome2");
const caixa = document.querySelector("#caixa1");
const jogadorX = document.querySelector("#x");
const jogadorO = document.querySelector("#o");
const pontoX = document.querySelector("#placar1");
const pontoO = document.querySelector("#placar2");
let contadorX = 0;
let contadorO = 0;

let jogadorA = "";
let jogadorB = "";
roda = false;

btnAdd.addEventListener("click", (evt) => {
  roda = true;

  jogadorA = jogador1.value;
  jogadorB = jogador2.value;
  jogadorX.innerHTML = jogadorA;
  jogadorO.innerHTML = jogadorB;
  const div = document.createElement("div");
  div.setAttribute("id", "jogadores");
  div.setAttribute("class", "caixa2");
  caixa.appendChild(div);
});

// ----------------------------------------------TABULEIRO-------------------------------------------------------------

let jogadorAtual = 0;

const tabuleiro = document.querySelector("#tabuleiro");
console.log(tabuleiro);

for (i = 0; i < 9; i++) {
  let coluna = document.createElement("div");
  coluna.setAttribute("id", "a" + i);
  coluna.setAttribute("class", "coluna");
  tabuleiro.appendChild(coluna);
}

const colunas = document.querySelectorAll(".coluna");

colunas.forEach((coluna) => {
  coluna.addEventListener("click", (evt) => {
    console.log(jogadorAtual);
    if (roda == false) {
      return;
    }
    if (jogadorAtual % 2 == 0) {
      coluna.textContent = "X";
    } else {
      coluna.textContent = "O";
    }
    let vitoria = verificarVitoria();
    console.log("jogador: ", jogadorAtual)
    if (vitoria) {

      if (jogadorAtual % 2 == 0) {
        console.log("X ganhou")
        contadorX++;
        pontoX.innerHTML = contadorX;
      } else {
        console.log("O ganhou")
        contadorO++;
        pontoO.innerHTML = contadorO;
      }
      jogadorAtual = 0;
    } else {
      jogadorAtual += 1;
    }
  });
});

const vitoria = [
  [colunas[0], colunas[1], colunas[2]],
  [colunas[3], colunas[4], colunas[5]],
  [colunas[6], colunas[7], colunas[8]],
  [colunas[0], colunas[3], colunas[6]],
  [colunas[1], colunas[4], colunas[7]],
  [colunas[2], colunas[5], colunas[8]],
  [colunas[0], colunas[4], colunas[8]],
  [colunas[2], colunas[4], colunas[6]],
];

console.log(vitoria);

const verificarVitoria = () => {
  let venceu = false;
  for (ele of vitoria) {
    let A = ele[0];
    let B = ele[1];
    let C = ele[2];
    if (
      A.textContent !== "" &&
      A.textContent == B.textContent &&
      A.textContent == C.textContent &&
      C.textContent == B.textContent
    ) {
      venceu = true;
      alert("vitoria");
      colunas.forEach((coluna) => {
        coluna.textContent = "";
      });
      roda = false;

      return true;
    }
  }
  let tudoPreenchido = true;

  colunas.forEach((coluna) => {
    if (coluna.textContent === "") {
      tudoPreenchido = false;
    }
  });

  if (tudoPreenchido && venceu == false) {
    alert("velha");
    colunas.forEach((coluna) => {
      coluna.textContent = "";
    });
    jogadorAtual = 0;
    roda = false;
  }
};
