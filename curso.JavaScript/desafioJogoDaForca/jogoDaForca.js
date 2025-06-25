const teclado = document.querySelector("#teclado");
const letras = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
  "Ç",
];

const animais = [
  "Axolote",
  "Cachorro",
  "Baleia",
  "Jaguatirica",
  "Lacraia",
  "Coiote",
  "Onça",
  "Leopardo",
  "Renoceronte",
  "Macaco",
  "Cobra",
  "Piranha",
  "Veado",
  "Baiacu",
  "Esquilo",
  "Aranha",
  "Arara",
  "Jabuti",
];

const espacos = document.querySelector(".espaço");
const imagem = document.querySelector("#foto");
const palavras = document.querySelector("#palavra");
let certo = false;
let errado = false;
let tracos = "";
const enter = document.createElement("button");
enter.setAttribute("class", "enter");
enter.textContent = "Enter";
let animalAtual = "";
let palavraSeparada = []
let armazenarLetras = [];
let erro = 1;
const limiteErros = 8;

const mudarImagem = () => {
  erro++;
  imagem.src = `foto${erro}.png`;
};

const sortearAnimal = () => {
  let indiceSorteada = Math.floor(Math.random() * animais.length);
  animalAtual = animais[indiceSorteada];
  console.log(animalAtual);
  const tracinhos = animalAtual.split("");
  palavraSeparada = animalAtual.toLocaleUpperCase().split("");
  tracos = tracinhos.map((letra) => {
    if (letra === " " || letra === "-") {
      return letra;
    } else {
      return "_";
    }
  });

  // tracos = tracinhos.fill("_");
  palavras.innerHTML = `<div class="tracinhos"> ${tracos.join(" ")} </div>`;
};

sortearAnimal();

const resetarJogo = () => {
  erro = 1;
  imagem.src = "jogo1.png";
  armazenarLetras = [];
  const todosBotoes = document.querySelectorAll(".letra, .certo, .errado");
  todosBotoes.forEach((btn) => {
    btn.disabled = false;
    btn.setAttribute("class", "letra");
  });
};
letras.forEach((letra) => {
  const botao = document.createElement("button");
  botao.setAttribute("id", letra.toLowerCase());
  botao.setAttribute("class", "letra");
  botao.textContent = letra;
  teclado.appendChild(botao);
  botao.addEventListener("click", () => {
    botao.setAttribute("class", "letra");
    if (animalAtual.toLocaleUpperCase().includes(botao.textContent)) {
      certo = true;
      botao.setAttribute("class", "certo");
      botao.disabled = true;
      palavraSeparada.forEach((letra, index) => {
        if (letra.toLocaleUpperCase() == botao.textContent) {
          tracos[index] = letra;
          armazenarLetras.push(letra);
          palavras.innerHTML = `<div class="tracinhos"> ${tracos.join(
            " "
          )} </div>`;
        }
        if (tracos.join("").toUpperCase() === animalAtual.toUpperCase()) {
          imagem.src = "jogo1.png";
          resetarJogo();
          sortearAnimal();
        }
      });
    } else {
      errado = true;
      mudarImagem();
      botao.setAttribute("class", "errado");
      botao.disabled = true;
      if (erro >= limiteErros) {
        alert("Você perdeu! A palavra era " + animalAtual);
        resetarJogo();
        sortearAnimal();
      }
    }
  });
});
