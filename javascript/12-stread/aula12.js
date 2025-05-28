const objs1 = document.getElementsByTagName("div")
const objs2 = [...document.getElementsByTagName("div")]
console.log(objs1)
console.log(objs2)

objs2.forEach(Element=>{
    console.log(Element)
})

// let n1 = [10, 20, 30]
// let n2 = [1, 22, 33, 44, 55]
// let n3 = [...n1, n2]
// const jogador1 = {nome: "Bruno", Energia: 100, vidas: 3, magia: 150}
// const jogador2 = {nome: "Nagi", Energia: 100, vidas: 5, velocidade: 80}
// const jogador3 = {...jogador1, ...jogador2}

// console.log("n1: " + n1)
// console.log("n2: " + n2)
// console.log("n3: " + n3)
// console.log(jogador3)

// const soma=(v1, v2, v3)=>{
//     return v1+v2+v3
// }
// let valores = [1, 5, 4]
// console.log(soma(...valores))
