//  ARRAY TRADICIONAL


//caixa
const caixa = document.getElementById("caixa")


// MATRIZES--> um array dentro de um array

//array cores como outro array dentro
let cores=["azul","verde","vermelho",["claro","escuro","médio"]]

//array cursos/cores 
let cursos = ["HTML", "CSS", "Javascript",cores]

//Seleciona a coleção que está na posição 3 e o elemento da coleção da posição 1 (verde)
console.log(cursos[3][1])

//Seleciona o array (cores) que está na posição 3, o outro array (dentro do array cores) também na posição 3 e por fim o a posição do elemento
console.log(cursos[3][3][1])


// altera o valor da posição 0
cursos[0]="C++" 


// adiciona um elemento no FINAL do array
cursos.push("Python") 
cursos.push("HTML")

// retira o ÚLTIMO elemento do array
cursos.pop()    // remove o HTML
cursos.pop()    // remove o Python


// adiciona o elemento no no COMEÇO do array
cursos.unshift("Python") 

// retita o 1° elemento do array
cursos.shift()


//indica o índice de um elemento específico 
console.log(cursos[0]) 


//adiciona os elementos na caixa
cursos.map((elemento) => {
  let p = document.createElement("p") // cria um parágrafo
  p.innerHTML = elemento // paragráfo recebe o elemento
  caixa.appendChild(p) // o paragráfo foi inserido na caixa
})
console.log(cursos)
