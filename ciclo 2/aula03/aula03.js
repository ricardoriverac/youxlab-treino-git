"use strict"

function teste(){
if (true){
    var nome="Alexia" //mostrando a diferença de declarar variaveis com "var" e "let"
        console.log("dentro de if fica:" + nome)
    }
    console.log("isso é um teste:" + nome)
}
teste()

console.log("fora do teste:" + nome)