let numero=0
let max=1000
let pares=0

//testando o continue
while(numero<max){
    console.log('CFB Cursos - ' + numero)
    if(numero>10){
        break
    }
    numero++
}
console.log('Fim do programa')

// testando o break
for(let i=numero; i<max; i++){
    if(i%2!=0){
        continue
    }
    pares++
}

console.log('Quantidade de pares: ' + pares)
console.log('Fim ddo programa')