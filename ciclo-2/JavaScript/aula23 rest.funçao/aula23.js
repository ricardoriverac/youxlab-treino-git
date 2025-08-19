//uando for 
// função que soma vários valores (não importa quantos)
function soma(...numeros) {
    let resultado = 0
    let total = numeros.length // pega quantos números foram passados

    for (let i = 0; i < total; i++) {
        resultado += numeros[i] // vai somando um por um
    }

    return resultado
}

// testando com vários valores
console.log(soma(10, 5, 2, 8)) // 25
console.log(soma(1, 2, 3, 4, 5)) // 15
console.log('\n')

// usando for...of (mais limpo)
function soma(...numeros) {
    let resultado = 0

    for (let n of numeros) {
        resultado += n // soma direto cada número
    }

    return resultado
}

console.log(soma(10, 5, 2, 8)) // 25
console.log(soma(100, 200)) // 300
//o rest é útil quando você não sabe quantos valores vão ser passados pra função.