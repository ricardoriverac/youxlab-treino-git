const palavrasForca = [
  {
    palavra: "CACHORRO",
    dica: "Melhor amigo do homem.",
  },
  {
    palavra: "PRAIA",
    dica: "Lugar com areia e mar.",
  },
  {
    palavra: "PIPOCA",
    dica: "Boa para comer vendo filme.",
  },
  {
    palavra: "ESCOLA",
    dica: "Onde você vai para estudar.",
  },
  {
    palavra: "FUTEBOL",
    dica: "Esporte com bola muito popular no Brasil.",
  },
  {
    palavra: "BICICLETA",
    dica: "Meio de transporte com duas rodas.",
  },
  {
    palavra: "SORVETE",
    dica: "Doce gelado, bom no verão.",
  },
  {
    palavra: "LIVRO",
    dica: "Fonte de histórias e conhecimento.",
  },
  {
    palavra: "GUARDA-CHUVA",
    dica: "Protege da chuva.",
  },
  {
    palavra: "JANELA",
    dica: "Fica na parede e pode ser aberta para ver o lado de fora.",
  },
  {
    palavra: "RELOGIO",
    dica: "Usado para ver as horas.",
  },
  {
    palavra: "TRAVESSEIRO",
    dica: "Você apoia a cabeça nele para dormir.",
  },
];

const alfabeto = [
  "A",
  "B",
  "C",
  "Ç",
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
];

function IniciarJogo(palavra, dica) {
  imagemForca();
  criarTracinho(palavra);
  teclado(palavra);
  mostrarDica(dica);
}

const divTracinho = document.getElementById("divTracinho");
let divImagem = document.getElementById("divImagem");

function sorteia() {
  return Math.round(Math.random() * 11);
}

function mostrarDica(dica) {
  let divDica = document.getElementById("divDica");
  let dicaParagrafo = document.createElement("p");
  dicaParagrafo.setAttribute("class", "dica");
  dicaParagrafo.textContent = dica;
  divDica.appendChild(dicaParagrafo);
}

function imagemForca() {
  let imagem = document.createElement("img");
  imagem.src = "./imagens/hangman-0.svg";
  divImagem.appendChild(imagem);
}

function criarTracinho(palavraSorteada) {
  let palavraSeparada = [...palavraSorteada];
  palavraSeparada.map((letra) => {
    let tracinhos = document.createElement("div");
    tracinhos.setAttribute("class", "tracinho");
    tracinhos.textContent = "_";
    divTracinho.appendChild(tracinhos);
  });
}

function teclado(palavra) {
  let divTeclado = document.getElementById("divTeclado");
  let palavraSeparada = [...palavra];
  alfabeto.map((letra) => {
    let tecla = document.createElement("div");
    tecla.setAttribute("class", "teclas");
    tecla.textContent = letra;
    tecla.addEventListener("click", (evento) =>{
      marcarTecla(tecla.textContent, palavraSeparada)
    })
    divTeclado.appendChild(tecla);
  });
}

function marcarTecla(elemento, palavra){
  palavra.forEach((letra, index)=> {
    if (letra == elemento) {
      substituiTraco(letra, index)
    }
  })
}

function substituiTraco(letra, index) {
  let tracos = document.querySelectorAll(".tracinho")

  tracos.forEach((traco, i) => {
    if (i == index) {
      traco.textContent = letra
      return
    }
  })
}

let palavraSorteada=''

function iniciarJogo() {
  palavraSorteada = palavrasForca[sorteia()];
  let palavra = palavraSorteada.palavra;
  let dica = palavraSorteada.dica
  let tracinhosExistentes = document.querySelectorAll(".tracinho");
  tracinhosExistentes.forEach((traco) => {
    traco.remove();
  });
  IniciarJogo(palavra, dica);
}

// function reiniciarJogo(){
//   palavraSorteada=palavrasForca[sorteia()]
//   palavra= palavraSorteada.palavra
//   dica=palavraSorteada.dica
// }



