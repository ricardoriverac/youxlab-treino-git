const palavras = [
  { id: 1, palavra: "banana", dica: "alimento" },
  { id: 2, palavra: "sabonete", dica: "objeto" },
  { id: 3, palavra: "computador", dica: "tecnologia" },
  { id: 4, palavra: "aviao", dica: "meio de transporte" },
  { id: 5, palavra: "violao", dica: "instrumento musical" },
  { id: 6, palavra: "girassol", dica: "planta" },
  { id: 7, palavra: "astronauta", dica: "profissão" },
  { id: 8, palavra: "pinguim", dica: "animal" },
  { id: 9, palavra: "caneta", dica: "material escolar" },
  { id: 10, palavra: "montanha", dica: "formação geográfica" },
  { id: 11, palavra: "telescopio", dica: "equipamento de observação" },
  { id: 12, palavra: "bicicleta", dica: "meio de transporte" },
  { id: 13, palavra: "microfone", dica: "equipamento de áudio" },
  { id: 14, palavra: "pipoca", dica: "lanche" },
  { id: 15, palavra: "jacare", dica: "animal" },
  { id: 16, palavra: "hospital", dica: "lugar" },
  { id: 17, palavra: "escola", dica: "lugar" },
  { id: 18, palavra: "livro", dica: "objeto" },
  { id: 19, palavra: "mochila", dica: "acessório" },
  { id: 20, palavra: "chave", dica: "objeto" },
  { id: 21, palavra: "tartaruga", dica: "animal" },
  { id: 22, palavra: "planeta", dica: "corpo celeste" },
  { id: 23, palavra: "janela", dica: "parte da casa" },
  { id: 24, palavra: "teclado", dica: "acessório de computador" },
  { id: 25, palavra: "relogio", dica: "marca o tempo" },
];
const alfabeto = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Ç","Z","X","C","V","B","N","M"];

let letrasUsadas = "";
let tracinhos = [];

const teclado = document.getElementById("teclado");
const botaoJogar = document.querySelector(".btnJogar");
const linha = document.getElementById("linha");
const dica = document.getElementById("id_dica");
const imagem = document.getElementById("imagem_coracao");

function montarTeclado() {
  botaoJogar.style.display = "none";

  alfabeto.forEach((letra) => {
    const botoesLetras = document.createElement("button");
    botoesLetras.setAttribute("class", "letra");
    botoesLetras.textContent = letra;
    teclado.appendChild(botoesLetras);
    // console.log(letra)
  });
}

function iniciarJogo() {
  criarCoracao()
  montarTeclado();
  mostrarDica();
  montarTraco();

  const letraTeclado = document.querySelectorAll(".letra");
  letraTeclado.forEach((letra) => {
    // console.log(letra.textContent)
    letra.addEventListener("click", (evento) => {
      if (imagem.childNodes.length === 0) {
        alert("Já perdeu louco, para de tentar");
        return;
      }
      letra.disabled = true;
      letrasUsadas = letra.textContent;

      let verificacaoLetra = palavraSorteadaDividida.includes(letrasUsadas);

      if (verificacaoLetra) {
        evento.target.classList.toggle("letraCerta");
        marcarTracinho(letrasUsadas);

        let venceu = tracinhos.every(
          (traco, i) => traco.textContent === palavraSorteadaDividida[i]
        );
        if (venceu) {
          alert("Parabéns, você venceu!");
          letraTeclado.forEach((letra) => {
            letra.disabled = true;
          });
        }
      } else {
        evento.target.classList.toggle("letraErrada");
        imagem.removeChild(imagem.lastElementChild);
      }

      if (imagem.childNodes.length === 0) {
        alert("Você perdeu, melhore na próxima!");
      }
    });
  });
}

function sortearPalavra(max) {
  return Math.floor(Math.random() * max);
}
const palavraSorteada = palavras[sortearPalavra(palavras.length)];
// console.log(palavraSorteada.palavra)

let palavraSorteadaDividida = palavraSorteada.palavra.toUpperCase().split("");
console.log(palavraSorteadaDividida);

function montarTraco() {
  let traco = "_";
  tracinhos = [];
  let novoArrayTraco = palavraSorteadaDividida.map((elemento) => {
    return traco;
  });
  // console.log(palavraSorteadaDividida)
  // console.log(novoArrayTraco)

  for (let linhas of novoArrayTraco) {
    linhas = document.createElement("div");
    linhas.setAttribute("class", "linha");
    linhas.textContent = "_";
    linha.appendChild(linhas);
    tracinhos.push(linhas);
    // console.log(linhas)
  }
  console.log(tracinhos);
}

function mostrarDica() {
  let dicaSorteada = palavraSorteada.dica;
  let dicaNaTela = document.createElement("h2");
  dicaNaTela.setAttribute("class", "dicaNaTela");
  dicaNaTela.textContent = `Dica: ${dicaSorteada}`;
  dica.appendChild(dicaNaTela);
}

function marcarTracinho(letra) {
  palavraSorteadaDividida.map((escolha, i) => {
    if (escolha === letra) {
      tracinhos[i].textContent = letra;
    }
  });
}

function criarCoracao(){
  for (let i = 0; i < 6; i++) {
    var imagemCoracao = document.createElement("img");
    imagemCoracao.src = "coracao-mine-removebg-preview.png";
    imagemCoracao.alt = "imagem coração para contar vidas";
    imagemCoracao.style.width = "3em";
    imagemCoracao.setAttribute("id", i);
    imagem.appendChild(imagemCoracao);
  }
  imagem.classList.add('ativo')
}