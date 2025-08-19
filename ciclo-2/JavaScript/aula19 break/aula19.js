let numero = 0
let maximo = 1000

// usando break, ele para
while (numero < maximo) {
    console.log('curso de javascript ' + numero) // imprime o número atual
    if (numero > 10) { 
        break // quando o número for maior que 10, o loop vai ser interrompido
    }
    numero++  // soma 1 no número a cada iteração
}
console.log('fim do programa')
// usando continue, ele usado para pular a execução do código na interação atual do loop e continuar para a próxima interação. 
let pares = 0
for (let indice = numero; indice < maximo; indice++) {
    if (indice % 2 != 0) { // se o número for ímpar
        continue // vai pular essa interação do loop e continuar para a próxima
    }
    pares++  // conta os números pares
}
console.log('quantidade de números pares: ' + pares) // imprime a quantidade de números pares
console.log('fim do programa')
