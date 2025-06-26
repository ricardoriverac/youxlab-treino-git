const letrasDiv = document.querySelector(".letras")
const tecladoDiv = document.querySelector(".teclado")
const palavras = document.querySelector("#palavra")
const temas = document.querySelector(".temas")
const jogo = document.querySelector(".jogo")
const imagem = document.querySelector("#imagem")
const acertos = document.querySelector(".acertos")

console.log(acertos)
const palavrasForca = [
  {
    palavra: "CACHORRO",
    dica: "Melhor amigo do homem."
  },
  {
    palavra: "PRAIA",
    dica: "Lugar com areia e mar."
  },
  {
    palavra: "PIPOCA",
    dica: "Boa para comer vendo filme."
  },
  {
    palavra: "ESCOLA",
    dica: "Onde você vai para estudar."
  },
  {
    palavra: "FUTEBOL",
    dica: "Esporte com bola muito popular no Brasil."
  },
  {
    palavra: "BICICLETA",
    dica: "Meio de transporte com duas rodas."
  },
  {
    palavra: "SORVETE",
    dica: "Doce gelado, bom no verão."
  },
  {
    palavra: "LIVRO",
    dica: "Fonte de histórias e conhecimento."
  },
  {
    palavra: "GUARDA-CHUVA",
    dica: "Protege da chuva."
  },
  {
    palavra: "JANELA",
    dica: "Fica na parede e pode ser aberta para ver o lado de fora."
  },
  {
    palavra: "RELOGIO",
    dica: "Usado para ver as horas."
  },
  {
    palavra: "TRAVESSEIRO",
    dica: "Você apoia a cabeça nele para dormir."
  }
]; 

let arrayLetras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ç"]

for(letra of arrayLetras){
    const teclado = document.createElement("button")
    teclado.setAttribute("id", "btn_letra")
    teclado.textContent = letra
    letrasDiv.appendChild(teclado)
}

function sortearTema () {
    let sorteio = Math.floor(Math.random() * palavrasForca.length);
    return sorteio
}

let erro = 1

function resetar () {
  alfabeto.forEach((button) => {
    button.style.backgroundColor = "#F7B5CA";
  imagem.src = "paim_forca1.png"

  let sorteio = Math.floor(Math.random() * palavrasForca.length);
  dica.textContent = `DICA: ${palavrasForca[sorteio].dica}`

  const palavraSortedada = palavrasForca[sorteio].palavra
  sorteadaTamanho = palavraSortedada.length
  let tracinhos = Array(palavraSortedada.length).fill("_")
  console.log(sorteio)
  })
}

function erros () {
    erro++
    if(erro <= 8){
      imagem.src = `paim_forca${erro}.png`
    }else if(erro <= 9){
      alert("Você perdeu!")
    }else{
      imagem.src = "paim_forca1.png"
      erro = 1
    }
}

let numero = sortearTema()
const dica = document.createElement("label")
dica.setAttribute("id", "dica")
dica.textContent = `DICA: ${palavrasForca[numero].dica}`
temas.appendChild(dica)
console.log(palavrasForca[numero].dica)

const palavraSortedada = palavrasForca[numero].palavra
sorteadaTamanho = palavraSortedada.length
const resposta = document.createElement("label")
resposta.setAttribute("id", "resposta")
let tracinhos = Array(palavraSortedada.length).fill("_")
const tracinhosEspaco = tracinhos.join(" ")
resposta.textContent = tracinhosEspaco
acertos.appendChild(resposta)

const alfabeto = [...document.querySelectorAll("#btn_letra")]
console.log(alfabeto.textContent)

function vitória(){
  alert("Você ganhou!")
}

i = 0
alfabeto.forEach((LetrasPalavra) => {
    LetrasPalavra.addEventListener("click",() => {
        if(palavraSortedada.toLocaleUpperCase().includes(LetrasPalavra.textContent)){
          LetrasPalavra.style.backgroundColor = "#90D1CA";
          // const pos = palavraSortedada.indexOf(`${LetrasPalavra.textContent}`)
          for(i = 0; i  < palavraSortedada.length; i++ ){
            if(palavraSortedada[i] === LetrasPalavra.textContent){
              tracinhos[i] = LetrasPalavra.textContent
              resposta.textContent = tracinhos.join(" ")
            }
          }
        }else{
          LetrasPalavra.style.backgroundColor = "#FF3F33";
          erros()
        }
    })
})

// const btn_sortearOutro = document.createElement("button")
// btn_sortearOutro.setAttribute("id", "btn_sortearOutro")
// btn_sortearOutro.textContent = "Sortear outro"
// temas.appendChild(btn_sortearOutro)

// btn_sortearOutro.addEventListener("click", () => {
//   imagem.src = "paim_forca1.png"
  
//   let sorteio = Math.floor(Math.random() * palavrasForca.length);
//   dica.textContent = `DICA: ${palavrasForca[sorteio].dica}`
  
//   const palavraSort =  palavrasForca[sorteio].palavra
//   let tracinhosDois = Array(palavraSort.length).fill("_")
//   const tracinhosEsp = tracinhosDois.join(" ")
//   resposta.textContent = tracinhosEsp

//   alfabeto.forEach((LetrasPalavra) => {
//     LetrasPalavra.addEventListener("click",() => {
//         if(palavraSort.toLocaleUpperCase().includes(LetrasPalavra.textContent)){
//           LetrasPalavra.style.backgroundColor = "#90D1CA";
//           // const pos = palavraSortedada.indexOf(`${LetrasPalavra.textContent}`)
//           for(i = 0; i  < palavraSort.length; i++ ){
//             if(palavraSort[i] === LetrasPalavra.textContent){
//               tracinhosDois[i] = LetrasPalavra.textContent
//               resposta.textContent = tracinhosDois.join(" ")
//             }
//           }
//         }else{
//           LetrasPalavra.style.backgroundColor = "#FF3F33";
//           erros()
//         }
//     })
// })

//   alfabeto.forEach((button) => {
//     button.style.backgroundColor = "#F7B5CA";
//   imagem.src = "paim_forca1.png"
//   })
// })
