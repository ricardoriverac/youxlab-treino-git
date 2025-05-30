//MAP-->percorre arrays e devolve um array alterado

const cursos=['html','css','javascript','php','react']

cursos.map((elemento, indice)=>{
    console.log('Curso: '+elemento+' -Posição no array: '+indice)
})
// percorre por todos elementos e índices da array
console.log('\n')

let aulas=cursos.map((elemento)=>{
    return elemento
})
// percorre todos os elementos da array
// return de maneira simples (RETORNA UMA ARRAY)
console.log(aulas)
console.log('\n')

let aula=cursos.map((elemento)=>{
    return '<div> '+elemento+' </div>'
})
// percorre todos os elementos da array
// return de maneira separada (RETORNA OS ELEMENTOS SEPARADAMENTE COM COMANDO DIV)
console.log(aula)
console.log('\n')





// USANDO MAP PARA OPERAR A COLEÇÃO(id) NO HTML

let elementos=document.getElementsByTagName('div')// pegou todo os elementos que são do tipo 'div'
elementos=[...elementos] // separou os elementos
elementos.map((elemento,indice)=>{
    console.log(elemento.innerHTML) // retorna os conteúdos das divs com o .innerHTML 
    elemento.innerHTML='Curso de Javascript'// modifica os textos das divs
})
console.log('\n')

// De outra forma:
const element=document.getElementsByTagName('div')
const valores= Array.prototype.map.call(element,({innerHTML})=>innerHTML)
console.log(valores)
console.log('\n')


//CONVERTENDO COLEÇÃO COM TEXTOS PARA COLEÇÃO COM N° INTEIRO

const converterInt=(elemento)=>parseInt(elemento) // recebe um valor e retorna esse valor convertido para inteiro 
let numeros=['1','2','3','4','5'].map(converterInt) // coleção com textos convertida para n° inteiros
console.log(numeros) // retornou a coleção já convertida
console.log('\n')

//Dobrando os valores da lista
const dobrar=(elemento)=>elemento*2
numeros=['1','2','3','4','5'].map(dobrar) // converte os valores da coleção
console.log(numeros) // retornou a coleção com valores dobradas
console.log('\n')



