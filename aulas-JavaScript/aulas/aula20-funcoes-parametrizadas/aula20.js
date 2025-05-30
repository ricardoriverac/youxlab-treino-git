const valorPadrao = 0

function soma(numero1, numero2){
    console.log(numero1 + numero2)
}

soma(10,5)

// passando valores padroes pros parametros
function soma(numero1=0, numero2=0){
    console.log(numero1 + numero2)
}

soma(10)

// retornando o valor
function soma(numero1, numero2){
    return numero1 + numero2
}

console.log(soma(10,10))

// dando o valor de uma variavel pro parametro
function soma(numero1 = valorPadrao, numero2 = valorPadrao){
    return numero1 + numero2
}

console.log(soma(10,32))

let valor = 0

console.log(valor)

function adicionar(v){
    return valor+v
}
valor = adicionar(10)
console.log(valor)