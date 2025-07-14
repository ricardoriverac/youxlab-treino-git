// DIFERENÇA DE PRÉ INCREMENTO E PÓS INCREMENTO

let numero=10

// PÓS INCREMENTO--> adiciona o incremento após a var 
numero++ // adicionando 1 no valor da var
console.log(numero)

numero=10
console.log(numero++)


//PRÉ INCREMENTRO--> adiciona o incremrnto antes da var
numero=10
console.log(++numero)

// OS DOIS COMANDOS MODIFICAM O VALOR DA VAR 
numero=10
console.log(numero++)
console.log(numero)


numero=10
numero+=10 // soma 10 ao valor da var 
console.log(numero)

numero=-10 // OPERADOR DE INVERSÃO
let exemplo=-numero // converte o valor negativo para positivo 
console.log(exemplo)

let numero1=10
let numero2=20
// quando tem uma str no meio das variáveis o valor irá concatenar (JUNTAR)
console.log(numero1+''+numero2)
