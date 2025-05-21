"use strict"

function teste(){
    let nome="Bruno"
    if(true){
        console.log(`dentro do IF do teste: ${nome}`)
    }
    console.log("dentro do teste: " + nome)
}

teste() 

console.log("fora do teste: " + nome) // erro pq não pega a variavel nome pq ela ta declarada dentro da função

let nome='Bruno'
nome='CFB Cursos'
nome=10

console.log(nome)

const curso='Javascrispt'

curso='HTML' // erro pq não pode mudar quando declara a constante

console.log(curso) 