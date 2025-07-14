//OPERADORES RELACIONAIS --> comparação 

/*
OPERADORES:
>:maior, >=:maior ou igual, <:menor, <=:menor ou igual
==:igual, !=:diferente
*/

let numero1=10,numero2=5,numero3=10

console.log(numero1 > numero2) // > maior.  retorna true

console.log(numero1 < numero2) // < menor.  retorna false

console.log(numero1 >= numero2) // >= maior ou igual. retorna true (numero1 é MAIOR que 5)
console.log(numero1 >= numero3) // >= maior ou igual. retorna true (numero1 é IGUAL a 10)

console.log(numero1 <= numero2) // <= menor ou igual. retorna false (numero2 é MENOR que 10)
console.log(numero1 <= numero3) // >= maior ou igual. retorna true (numero1 é IGUAL a 10)

console.log(numero1 == numero3) // == igual. retorna true (numero1 é IGUAL a 10)
console.log(numero2 == numero3) // == igual. retorna false (numero2 é DIFERENTE de 10)

console.log(!(numero1==numero3)) // ! negação. retorna false (Valores do numero1 e numero3 NÃO podem ser iguais)
console.log(!(numero1==numero2)) // ! negação. retorna true (Valores do numero1 e numero2 NÃO podem ser iguais)

console.log(numero1!=numero3) // != diferente. retorna false (numero1 é IGUAL a 10)
console.log(numero1!=numero2) // != diferente. retorna true (numero1 é DIFERNTE de 5)

