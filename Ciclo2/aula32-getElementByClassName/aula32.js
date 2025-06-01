// MÉTODO getElementByClassName-->permite que a gente obtenha os elementos do DOM que utiliza  uma classe específica

//SINTAXE: let variável=document.getElementByClassName('NOME DA CLASS')

// Obtém todos os elementos com a classe 'curso' (HTMLCollection)
const cursoTodos=document.getElementsByClassName('curso')

console.log(cursoTodos)


// Converte a coleção em um array
const cursoTodosArray=[...document.getElementsByClassName('curso')]

console.log(cursoTodosArray)

// Separa os elementos com as classes 'c1' e 'c2'
const cursoC1=[...document.getElementsByClassName('c1')]
const cursoC2=[...document.getElementsByClassName('c2')]

console.log(cursoC1)
console.log(cursoC2)


// Adicionando a classe 'destaque' a todos os elementos
// cursoTodosArray.map((elemento)=>{
//     elemento.classList.add('destaque') 
// })

//Inspecionando cada elemento percebe-se que todos eles receberam a classe destaque

// Adicionando a classe 'destaque' a todos os elementos de classe c1
cursoC1.map((elemento)=>{
    elemento.classList.add('destaque') 
})

//Inspecionando cada elemento de classe c1 percebe-se que todos eles receberam a classe destaque

//OBTENDO 1 ELEMENTO ESPECÍFICO
const cursoEspecial=document.getElementsByClassName('curso')[2] // Pegue o elemento com classe 'curso' da 2° posição

console.log(cursoEspecial)