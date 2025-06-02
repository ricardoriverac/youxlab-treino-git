// ENTENDENDO A RELAÇÃO DOS ELEMENTOS NO DOM #P2

// Seleciona a div com id "caixa1"
const caixa1 = document.querySelector('#caixa1')

// Seleciona todos os elementos com a classe "curso" e converte em array
const botaoC1 = [...document.querySelectorAll(".curso")]

// Seleciona a div com id "curso1_2"
const curso1_2 = document.querySelector('#curso1_2')

console.log(curso1_2) // Exibe a div com id "curso1_2"

// Retorna o elemento pai da div "curso1_2"
console.log(curso1_2.parentNode)

// Retorna o quinto filho (índice 4) do elemento avô de "curso1_2"
console.log(curso1_2.parentNode.parentNode.children[4])

// Verifica se os elementos possuem filhos (nós filhos)
// Retorna true se houver pelo menos um nó (inclusive texto)
console.log(caixa1.hasChildNodes())         // true
console.log(botaoC1[0].hasChildNodes())     // true (texto dentro da div conta como filho)
console.log(botaoC1[0].childNodes)          // Lista de todos os nós filhos (inclui texto, comentários, etc.)

// Verifica se há elementos HTML como filhos
//de botaoC1
if (botaoC1[0].children.length > 0) {
    console.log('Possui filho')
} else {
    console.log('Não possui filho')
}

//de caixa1
if (caixa1.children.length > 0) {
    console.log('Possui filho')
} else {
    console.log('Não possui filho')
}

// Versão com operador ternário
console.log(botaoC1[0].children.length > 0 ? 'Possui filho' : 'Não possui filho') // false

// OPERANDO SOBRE OS ELEMENTOS

// Modifica o conteúdo do primeiro filho da caixa1
caixa1.firstElementChild.innerHTML = 'TESTE'

// Modifica o conteúdo do segundo filho da caixa1
caixa1.children[1].innerHTML = 'TESTE2'
