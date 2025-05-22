const objs= document.getElementsByTagName("div")

const jogador1 = {nome: "Kaio Jorge", energia: 120, vidas: 3, magia: "raio"}
const jogador2 = {nome: "Ronaldin", energia: 67, vidas: 2, velocidade: 45}
const jogador3 = {...jogador1, ...jogador2}
console.log(jogador3)


let n1 = [20, 22, 14]
let n2 = [11, 16, 21, 25, 2]
let n3 = [...n1, ...n2]
console.log("n1 = " + n1)
console.log("n2 = " + n2)
console.log("n3 = " + n3)

const soma = (v1, v2, v3)=>{
    return v1+v2+v3
}
const valores=[2, 6, 2]
console.log(soma(...valores))

