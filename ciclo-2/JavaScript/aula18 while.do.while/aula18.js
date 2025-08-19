let numero = 10

// while: vai rodar enquanto a condição for verdadeira
while (numero < 10) { // a condição aqui é 'numero < 10', mas 'numero' já é 10, então a condição é falsa
    console.log('curso de javascript') 
    numero++ 
}
console.log('fim do programa \n') // n vai ser impresso porque o loop n começo

do {// do while: a diferença é que o loop vai rodar ao menos uma vez, mesmo que a condição seja falsa

    console.log('curso de javascript')
    numero++   // o número vai ser incrementado a cada iteração
} while (numero < 10)  // a condição vai ser checada depois do código rodar

console.log('fim do programa')
