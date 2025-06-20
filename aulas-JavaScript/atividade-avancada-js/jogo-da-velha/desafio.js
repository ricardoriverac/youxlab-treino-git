const tabuleiro = document.querySelector(".tabuleiro");
const botaoJogar = document.querySelector("#btnJogar");
const botaoReiniciar = document.querySelector('#btnReiniciar')
const input1 = document.getElementById("jogador1");
const input2 = document.getElementById("jogador2");
const nomeJogadores = document.getElementById("nomeJogadores");
let jogada = 'X'
let marcacoesTabuleiro = ['', '', '', '', '', '', '', '', '']
let vitoriaJogador1 = 0
let vitoriaJogador2 = 0

botaoJogar.addEventListener("click", (evento) => {
  if (input1.value === "" || input2.value === ""){
    alert("Preencha o nome dos jogadores")
    return
  }

  for (let i = 0; i < 9; i++) {
    var quadrado = document.createElement("div");
    quadrado.setAttribute("class", "coluna");
    quadrado.setAttribute("id", i)
    quadrado.addEventListener('click', marcarQuadrado)
    tabuleiro.appendChild(quadrado);
  }

  atualizarPlacar()
});

function alternarJogador(){
  if (jogada == "X"){
    jogada = 'O'
  } else {
    jogada = 'X'
  }
}

function verificarVitoria(){
  const combinacoesVitorias = [[0,1,2], [3,4,5], [6,7,8],   // linhas
                              [0,3,6], [1,4,7], [2,5,8],  // colunas
                              [0,4,8], [2,4,6]]          // diagonais
                              
  const vitoria = combinacoesVitorias.some(([a,b,c])=>{
    return marcacoesTabuleiro[a] === jogada &&
    marcacoesTabuleiro[b] === jogada &&
    marcacoesTabuleiro[c] === jogada
  })
  
  if (vitoria){
    alert(`${jogada} ganhou`)
  }
  
  return vitoria
}

botaoReiniciar.addEventListener('click', (evento)=>{
  marcacoesTabuleiro = ['', '', '', '', '', '', '', '', '']
  const quadrados = document.querySelectorAll('.coluna ')
  quadrados.forEach((quadrado)=>{
    quadrado.textContent = ''
  })
})

function atualizarPlacar(){
  nomeJogadores.innerHTML = `<p>${input1.value} X: ${vitoriaJogador1}</p>
                             <p>${input2.value} O: ${vitoriaJogador2}</p>
                            `
}

function marcarQuadrado(evento){
  const quadrado = evento.target
  if (marcacoesTabuleiro[quadrado.id] !== ''){
    return
  }
  quadrado.textContent = jogada
  marcacoesTabuleiro[quadrado.id] = jogada
  
  if (verificarVitoria()){
    if (jogada == 'X'){
      vitoriaJogador1 += 1
    } else {
      vitoriaJogador2 += 1
    }

    atualizarPlacar()
    
    return
  }

  // verificando se deu velha
  const velha = marcacoesTabuleiro.every((resultado)=>{
    return resultado !== ''
  })
  if (velha){
    alert('velha')
    zerarTabuleiro()
    return
  }
  
  alternarJogador()
}