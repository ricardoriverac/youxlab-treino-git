// querySelector/querySelectorAll-->Obtem o elemento que eu específicar para ele seja um id, tag ou class

//SINTAXE: 
//querySelector:
// const variável=[...document.querySelector('O QUE VOCÊ QUEIRA OBTER DO DOM')]
//querySelectorAll:
// const variável=[...document.querySelectorAll('O QUE VOCÊ QUEIRA OBTER DO DOM')]


const divTodas=[...document.getElementsByTagName('div')]//coleção de divs
const cursoTodos=[...document.getElementsByClassName('curso')]
const cursoC1=[...document.getElementsByClassName('c1')]
const cursoC2=[...document.getElementsByClassName('c2')]
const cursoEspecial=document.getElementById('c2')


//querySelector--> retorna somente o PRIMEIRO elemento que ele encontrar da chave do DOM que foi especificada 
//OBS: retorna um único elemento

const query_divTodas=document.querySelector('div') // seleciona a PRIMEIRA <div> encontrada no DOM
console.log(query_divTodas)


//querySelectorAll--> retorna uma COLEÇÃO da chave do DOM que foi especificada 

let queryAll_divTodas=document.querySelectorAll('div') // seleciona TODAS <div> encontrada no DOM
console.log(queryAll_divTodas)
//Trasformando em um array:
queryAll_divTodas=[...document.querySelectorAll('div')]
console.log(queryAll_divTodas)


// TODOS os elementos com class="curso" encontrados no DOM

const queryAll_cursoTodos=[...document.querySelectorAll('.curso')]
// Para selecionar uma classe com querySelectorAll, use um ponto (.) antes do nome da classe. Ex: '.curso'

console.log(queryAll_cursoTodos)


// TODOS os elementos com class="c1" encontrados no DOM

const queryAll_cursoC1=[...document.querySelectorAll('.c1')]

console.log(queryAll_cursoC1)


// TODOS os elemento com class="c2" encontrados no DOM

const queryAll_cursoC2=[...document.querySelectorAll('.c2')]

console.log(queryAll_cursoC2)


// elemento com id="c2" encontrado no DOM

const query_cursoEspecial=document.querySelector('#c2')
// Para selecionar um id com querySelector, use um "#" antes do nome do id. Ex: '#c2'

console.log(query_cursoEspecial)

// Com querySelectorAll :
const queryAll_cursoEspecial=document.querySelectorAll('#c2')[1]
// Com querySelectorAll retorna uma COLEÇÃO, por isso é PRECISO colocar a POCIÇÃO da div

console.log(query_cursoEspecial)


//ESPECIFICANDO DOIS (podendo ser mais) tipos de elementos com tags DIFERENTES 

//Selecionando TODOS os elementos de tag <div> e <p>
let queryAll_div_p=[...document.querySelectorAll('div,p')]

console.log(queryAll_div_p)

//Selecionando TODOS os elementos de class="c1" e tag <p>
let queryAll_c1_p=[...document.querySelectorAll('.c1,p')]

console.log(queryAll_c1_p)

//Selecionando TODAS as divs que POSSUEM o atriburo class
let queryAll_divTodas_class=[...document.querySelectorAll('div[class]')]
console.log(queryAll_divTodas_class)

//Selecionando TODOS elementos <p> que estão DENTRO de div
let queryAll_divTodas_p=[...document.querySelectorAll('div > p')]
console.log(queryAll_divTodas_p)

