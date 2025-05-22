let numero = 0
let max = 1000

// while(numero<max){
//     console.log("CBF Cursos - " + numero)
//     if(numero>10){
//         break
//     }
//     numero++
// }

let pares = 0

for(let i=numero;i<max;i++){
    if(i%2!=0){
        continue
    }
    pares++
}

console.log("Quantidade de pares: " + pares)
console.log("Fim do programa")
