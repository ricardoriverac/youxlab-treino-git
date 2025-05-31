// usando o operador spread quebrando um conjunto de elementos e devolve elemento a elemento

let num1=[10,20,30]
let num2=[11,22,33,44,55]
let num3=[...num1] // passando um arrey para outro

num3=[num1,num2] // a , junta os dois
console.log('numero 3: '+ num3)

num3=[...num1,...num2] // junta as variáveis porém com o spread
console.log('numero 3: '+ num3)

console.log('numero 1: '+num1,1)
console.log('numero 2: '+num2)
console.log('numero 3: '+num3)

const jogador1={nome:'claudinete', energia:100, vidas:6, velocidade:100 }
const jogador2={nome:'clebin', energia:150, vidas:8, velocidade:69}
const jogador3={...jogador1,...jogador2}//juntando os jogadores 
console.log(jogador3)

const soma=(v1,v2,v3)=>{ //função
    return v1+v2+v3
}
let valores=[1,2,3]

console.log(soma(...valores)) //passa os valores do array como parâmetros individuais
const objeto1=document.getElementsByTagName('div') // coleta todas as <div> da página em uma coleção de elementos HTML (HTMLCollection)
console.log(objeto1)

const objeto2=[...document.getElementsByTagName('div')] // usando o spread para transformar a HTMLCollection em um array real
console.log(objeto2) //exibe um array com <div>
// percorre cada <div> e altera seu conteúdo interno para 'Curso'
objeto2.forEach(element =>{
    element.innerHTML='Curso'
});