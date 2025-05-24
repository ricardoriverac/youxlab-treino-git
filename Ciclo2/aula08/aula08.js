// OPERADORES BITWISE

let numero1=10
let numero2=11
let resultado= numero1&numero2
//OPERADOR &: vai retornar onde tiver equivalência 
console.log(resultado)

numero1=14
resultado= numero1&numero2
console.log(resultado)


numero1=10
numero2=11
//OPERADOR |: realizará a operação bit a bit dos elementos
resultado= numero1|numero2
console.log(resultado)


// OPERADOR ^: retorna um quando tiver o n° 1 sem equivalência na operação de um bit
resultado=numero1^numero2
console.log(resultado)


// >> 1(n° de deslocamento): desloca 1 bit para direita
// << 1(n° de deslocamento): desloca 1 bit para esquerda 
resultado= numero1 << 1 // quando é feita uma operaçãpo pata a direita o resultado do bit dobra
console.log(resultado)
resultado= numero1 >> 1 // reduz o valor do bit pela metade
console.log(resultado)

resultado= numero1 << 2 //dois bits para a esquerda e dobra 2x o resultado do bit
console.log(resultado)

resultado= numero1 >> 2 //dois bits para a direita e divide 2x pela metade do resultado do bit
console.log(resultado)