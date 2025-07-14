// MÉTODO getElementByTagName--> neste comando conseguimos obter uma coleção de elementos

//usando getElementById(RETORNA SOMENTE 1 ELEMNTO DIRETAMENTE):
const divCurso1=document.getElementById('curso1')
const divCurso2=document.getElementById('curso2')
const divCurso3=document.getElementById('curso3')
const divCurso4=document.getElementById('curso4')
const divCurso5=document.getElementById('curso5')
const divCurso6=document.getElementById('curso6')

const arrayElementos=[divCurso1,divCurso2,divCurso3,divCurso4,divCurso5,divCurso6]

console.log(arrayElementos)//retorna uma array

//usando getElementByTagName(RETORNA UMA COLEÇÃO DE ELEMENTOS):
let colecaoHTML=document.getElementsByTagName('div') // pegou TODOS os elementos div

console.log(colecaoHTML)//retorna um HTMLCollection



// com o HTMLCollection NÃO podemos utilizar uma grande parte de funções/comados que poderiamos utilizar em um array
// para utilizarmos essas funções/comando é necessário trasformar esse HTMLCollection em um array
// para isso temos que utilizar um spreed(...)

colecaoHTML=[...document.getElementsByTagName('div')]

console.log(colecaoHTML) // retorna um array diretamente

// De outra forma

colecaoHTML=[document.getElementsByTagName('div')]

colecaoHTML=[...colecaoHTML]

console.log(colecaoHTML)// retorna um array do HTMLCollection

// com isso podemos utilizar as outras fuções/comandos como o map

colecaoHTML.map((elemento)=>{
    console.log(elemento) //retorna os elementos
})

