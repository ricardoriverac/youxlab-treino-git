let numero1=[10,20,30]
let numero2=[11,22,33,44,55]
let numero3=[...numero1,...numero2]

console.log('numero1: ' + numero1)
console.log('numero2: ' + numero2)
console.log('numero3: ' + numero3)
console.log('tipo de numero3: ' + typeof(numero3))

const jogador1 = {nome: 'Bruno', energia: 100, vidas: 3, nagia: 150}
const jogador2 = {nome: 'Bruce', energia: 100, vidas: 5, velocidade: 80}
const jogador3 = {...jogador1,...jogador2}

console.log(jogador3)

const soma=(valor1,valor2,valor3)=>{
    return valor1+valor2+valor3
}

let valores=[1,5,4]

console.log(soma(1,5,4)) // pode passar desse jeito
console.log(soma(...valores)) // assim tbm da

const objs1=document.getElementsByTagName('div')
const objs2=[...document.getElementsByTagName('div')]

objs2.forEach(element => {
    element.innerHTML='curso'
});

console.log(objs1)
console.log(objs2)