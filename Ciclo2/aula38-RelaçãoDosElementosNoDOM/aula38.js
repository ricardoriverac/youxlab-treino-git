//ENTENDENDO A RELAÇÃO DOS ELEMENTOS NO DOM

// Seleciona a div com id "caixa1"
const caixa1 = document.querySelector('#caixa1')

// Seleciona todos os elementos com a classe "curso" dentro do documento e transforma em array
const botaoC1 = [...document.querySelectorAll(".curso")]

console.log(botaoC1) // Exibe array com 6 divs com a classe "curso"
console.log(caixa1)  // Exibe o elemento com id "caixa1"

console.log(document.getRootNode()) // Exibe o nó raiz do documento (geralmente o <html>)
console.log(caixa1.children) // Lista todos os elementos filhos diretos de "caixa1"
console.log(caixa1.children[4]) // Exibe o 5º filho (índice 4) da "caixa1"
console.log(caixa1.firstElementChild) // Exibe o primeiro filho elemento de "caixa1"
console.log(caixa1.lastElementChild) // Exibe o último filho elemento de "caixa1"

// O DOM representa a estrutura HTML como uma árvore de elementos, onde cada tag
// é um nó que pode conter filhos, pais e irmãos. No código, são selecionados elementos como a 
// div #caixa1 (pai) e seus filhos com a classe .curso. Com comandos como children, firstElementChild e 
// lastElementChild, é possível acessar diretamente os elementos filhos dessa div. Além disso, document.getRootNode() 
// retorna o nó raiz do documento. Essa manipulação permite interagir com partes específicas da página 