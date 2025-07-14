// FUNÇÕES PARAMETRIZADAS  #P3 -->inserindo valores na função

function teste(parametro1){ //parametro1--> valor que entra dentro da função
    console.log(parametro1)//imprime o parametro1
}

teste('Sophia') // parametro1 foi substituido pelo valor dentro do parenteses, neste caso 'Sophia'

//podemos subistituí-lo por qualquer coisa:
teste(2025)
teste(5,2)
console.log('\n')


//Outro exemplo:
function soma(numero1,numero2){ // pode ser passado quantos parâmetros precisar
    console.log('n° 1: '+numero1)
    console.log('n° 2: '+numero2)
    resultado=numero1+numero2
    console.log('resultado: '+resultado)
}

soma(1,2) // temos que passar 2 valores
console.log('\n')


// parâmetro com valor padrão --> quando não for colocado valores ao chamar a função
function subtracao(Numero1=0,Numero2=0){ // parâmetros com valor padrão de 0
    console.log(Numero1-Numero2)
}

subtracao() // não foi passado valores
subtracao(10) // passando só um valor --> volta 10 --> 10-0=10
console.log('\n')


// COM RETURN
function divisao(Numero1=0,Numero2=0){ // parâmetros com valor padrão de 0
    return Numero1/Numero2
}

console.log(divisao(10,2)) // console.log()--> assumi o valor de retorno da função
console.log('\n')


//Outra forma de colocar parâmetros com valor padrão:
const valorPadrão=0

function multiplicacao(numero1=valorPadrão,numero2=valorPadrão){
    return numero1*numero2
}

console.log(multiplicacao())
console.log(multiplicacao(5))
console.log('\n')


//ALTERANDO VALOR DE VARIÁL:
let valor=0

console.log(valor)

function adiciona(numero){
    valor+=numero
}


//OPERANDO VARIÁVEL DENTRO DA FUNÇÃO
// variável recebe função com seu parâmetro
adiciona(10) //adicionou 10 a variável (somou 10)
console.log(valor)

adiciona(5) //adicionou mais 5 a variável (somou 5)
console.log(valor)