let numero = 0

while (numero < 10) {// O loop vai rodar enquanto o número for menor que 10
    console.log(numero) 
    numero++ // aui soma 1 em "numero" a cada volta do loop
}

// Fatorando um número:
let numero2 = 5
let fatorial = 1  // começando com 1 porque qualquer número multiplicado por 1 é ele mesmo

// O loop vai continuar enquanto "numero2" for maior ou igual a 1
while (numero2 >= 1) {
    fatorial *= numero2  // Multiplicando
    numero2--  // diminui 1 em "numero2" a cada loop
}

console.log(fatorial)