// BREAK E CONTINUE

//break-->interrompe a execução
//continue--> só não executa a execução onde foi adicionado

let numero=0
let maximo=1000

//usando break
while(numero<maximo){
    console.log('Curso de Javascript '+numero)
    if(numero>10){
        break // para o loop se numero por maior que 10
    }
    numero++
}
console.log('Fim do programa')


//usando continue
let pares=0
for(let indice=numero; indice<maximo; indice++){
    if(indice%2!=0){ // se número for impar continue
      continue // pulou para próxima interação
    }
    pares++
}
console.log('Quantidade de números pares: '+pares)
console.log('Fim do programa')