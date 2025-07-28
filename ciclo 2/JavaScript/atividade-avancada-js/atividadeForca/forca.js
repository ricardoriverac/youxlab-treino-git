const palavras = [
  { id: 1, palavra: "CENOURA", dica: "vegetal" },
  { id: 2, palavra: "TIJOLO", dica: "material de construcao" },
  { id: 3, palavra: "CACHORRO", dica: "animal de estimacao" },
  { id: 4, palavra: "OCULOS", dica: "ajuda a enxergar" },
  { id: 5, palavra: "BOLA", dica: "usado em esportes" },
  { id: 6, palavra: "CHUVEIRO", dica: "banho" },
  { id: 7, palavra: "ESPELHO", dica: "reflete imagem" },
  { id: 8, palavra: "CADEIRA", dica: "movel para sentar" },
  { id: 9, palavra: "PANELA", dica: "usado para cozinhar" },
  { id: 10, palavra: "GUARDA-CHUVA", dica: "protege da chuva" },
  { id: 11, palavra: "TREM", dica: "meio de transporte sobre trilhos" },
  { id: 12, palavra: "SABAO", dica: "usado na limpeza" },
  { id: 13, palavra: "CADERNO", dica: "usado para escrever" },
  { id: 14, palavra: "ABACAXI", dica: "fruta tropical" },
  { id: 15, palavra: "TRAVESSEIRO", dica: "usado para dormir" },
  { id: 16, palavra: "VENTILADOR", dica: "gera vento" },
  { id: 17, palavra: "ESCADA", dica: "ajuda a subir" },
  { id: 18, palavra: "TIGRE", dica: "animal selvagem" },
  { id: 19, palavra: "CAMISA", dica: "peca de roupa" },
  { id: 20, palavra: "GELADEIRA", dica: "eletrodomestico" },
  { id: 21, palavra: "JARDIM", dica: "tem flores e plantas" },
  { id: 22, palavra: "PRANCHA", dica: "usada para surfar" },
  { id: 23, palavra: "DRAGAO", dica: "criatura mitologica" },
  { id: 24, palavra: "DINHEIRO", dica: "meio de pagamento" },
  { id: 25, palavra: "TEATRO", dica: "local de apresentacoes" }
];

const alfabeto = ["A", "B", "C", "Ç", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

let palavraAtual = "";
let dicaAtual = "";
let tracinhos = [];
let letrasUsadas = [];
let tentativasErradas = 0;
let maxTentativas = 8;
let letraCorreta = [];
let letraErrada = [];
let mostrarTeclado = true;

function iniciarJogo() {
  tentativasErradas = 0;
  letrasUsadas = [];
  tracinhos = [];
  sortearPalavra();

  if (mostrarTeclado) {
    criarBotoes();
  } else {
    document.querySelector("#teclado").innerHTML = "";
  }
  btnIniciar.disabled = true;
}
console.log(palavraAtual);

document.querySelector("#btnIniciar").addEventListener("click", iniciarJogo);
document.querySelector("#btnIniciar").addEventListener("click", iniciarJogo);

function sortearPalavra() {
  const indice = Math.floor(Math.random() * palavras.length);
  palavraAtual = palavras[indice].palavra;
  dicaAtual = palavras[indice].dica;

  tracinhos = palavraAtual.split("").map(letra => (letra === " " ? " " : "_"));

  letrasUsadas = [];
  tentativasErradas = 0;

  document.querySelector("#dica").textContent = `Dica: ${dicaAtual}`;
  document.querySelector("#palavra").textContent = tracinhos.join(" ");
  document.querySelector("#tentativas").textContent = `Tentativas restantes: ${maxTentativas - tentativasErradas}`;
  document.querySelector("#letras-usadas").textContent = `Letras usadas: ${letrasUsadas.join(", ")}`;
  atualizarVidas();
}

function verificarLetra(letra) {
  if (letrasUsadas.includes(letra)) return;

  letrasUsadas.push(letra);

  if (palavraAtual.includes(letra)) {
    palavraAtual.split("").forEach((l, i) => {
      if (l === letra) tracinhos[i] = letra;
    });
    document.querySelector("#palavra").textContent = tracinhos.join(" ");
  } else {
    tentativasErradas++;
    atualizarVidas();
  }

  document.querySelector("#tentativas").textContent = `Tentativas restantes: ${maxTentativas - tentativasErradas}`;
  document.querySelector("#letras-usadas").textContent = `Letras usadas: ${letrasUsadas.join(", ")}`;

  if (tracinhos.join("") === palavraAtual) {
    alert("Você ganhou, jiló");
    // sortearPalavra();
    iniciarJogo();
  } else if (tentativasErradas >= maxTentativas) {
    alert(`Você perdeu bobo! A palavra era: ${palavraAtual}`);
    // sortearPalavra();
    iniciarJogo();
  }
}

function atualizarVidas() {
  const coracoes = document.querySelectorAll(".vida");
  for (let i = 0; i < coracoes.length; i++) {
    if (i < 8 - tentativasErradas) {
      coracoes[i].style.display = "inline";
    } else {
      coracoes[i].style.display = "none";
    }
  }
}

function criarBotoes() {
  const teclado = document.querySelector("#teclado");
  teclado.innerHTML = ""; 
  alfabeto.forEach(letra => {
    const botao = document.createElement("button");
    botao.textContent = letra;

    botao.addEventListener("click", () => {
      verificarLetra(letra);

      if (palavraAtual.includes(letra)) {
        botao.classList.add("acerto"); 
      } else {
        botao.classList.add("erro");  
      }

      botao.disabled = true;
    });

    teclado.appendChild(botao);
  });
}

const botaoReiniciar = document.querySelector('#btnReiniciar');

btnReiniciar.addEventListener('click', () => {
  document.querySelector('#dica').textContent = '';
  document.querySelector('#teclado').innerHTML = '';
  letrasUsadas = [];
  tentativasErradas = 8;
  tracinhos = [];
  iniciarJogo();
});
