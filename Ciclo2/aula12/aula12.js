// OPERADOR SPREAD // quebra um conjunto de elementos e devolve elemento a elemento

let lista1=[10,20,30]
let lista2=[11,22,33,44,55]
let lista3=[...lista1] // copiamou um arrey para outro

lista3=[lista1,lista2] // junta as duas variáveis
console.log('LIsta 3: '+lista3)

lista3=[...lista1,...lista2] // Também junta as duas variáveis porém usando o SPREAD
console.log('LIsta 3: '+lista3)

console.log('LIsta 1: '+lista1)
console.log('LIsta 2: '+lista2)
console.log('LIsta 3: '+lista3)



const jogador1={nome:'Sophia', energia:100, vidas:3, poder:150 }
const jogador2={nome:'Sarah', energia:100, vidas:5, velocidade:80}
const jogador3={...jogador1,...jogador2} // junta jodador1 e jogador2
console.log(jogador3)



const soma=(valo1,valo2,valo3)=>{   // Abriu uma função
    return valo1+valo2+valo3
}

let valores=[1,2,3]

console.log(soma(...valores)) // com o spread cada valor dessa var será espalhada para uma das variáveis da função



const objeto1=document.getElementsByTagName('div') // html colection (SÓ RECEBE ELEMENTOS HTML)
// dentro de objetos tem uma coleção de objetos div
console.log(objeto1)

const objeto2=[...document.getElementsByTagName('div')] // usando o spread (PODE ADICIONAR OUTROS TIPOS DE ELEMENTOS)
console.log(objeto2) // aparecera um arrey/lista com os elentos

objeto2.forEach(element =>{
    element.innerHTML='Curso'
});