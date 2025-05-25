console.log('Início do programa')
//começando o loop, inicializando o contador com 0 e rodando até ser menor que 10
for (let contador = 0; contador < 10; contador++) { // A cada rodada, vai imprimir o valor do contador, o for é um loop usado quando sabemos o número de repetições que o loop vai fazer.
    console.log('alexia - valor do contador: ' + contador) // Vai repetir isso 10 vezes
}

console.log('Fim do programa')
//imprimir pares e impar
console.log('Início do programa')

// o loop vai de 0 até 99, somando 1 a cada rodada
for (let numero = 0; numero < 100; numero++) {
    // Se o número for par (resto da divisão por 2 é 0), vai imprimir que é par
    if (numero % 2 == 0) {
        console.log(numero + ' é par')
    } else {
        console.log(numero + ' é ímpar')
    }
}

console.log('Fim do programa')
