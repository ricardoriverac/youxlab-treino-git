// função parametrizada com 1 valor
function mostrar(dado) {
    console.log(dado)
}

// chamando com diferentes tipos de valores
mostrar('alexia')
mostrar(2008)
mostrar(10, 20) // só o primeiro é usado
console.log('\n')

// função que mostra 2 números e soma eles
function somar(a, b) {
    console.log('valor 1: ' + a)
    console.log('valor 2: ' + b)

    let resultado = a + b
    console.log('soma: ' + resultado)
}

// testando a função
somar(3, 7)
console.log('\n')

//com 0 como valor padrao
// se não passar valor, vai usar 0 como padrão
function subtrair(x = 0, y = 0) {
    console.log(x - y)
}

// diferentes combinações
subtrair()         // 0 - 0
subtrair(8)        // 8 - 0
subtrair(10, 3)    // 10 - 3
console.log('\n')

//agr com return
// função que divide dois números e retorna o resultado
function dividir(x = 0, y = 1) {
    return x / y
}

// testando usando console.log pra mostrar o retorno
console.log(dividir(10, 2))
console.log(dividir(9, 3))
console.log('\n')

//usando uma variavel externa
const padrao = 1

// se não passar valor, usa a constante "padrao"
function multiplicar(a = padrao, b = padrao) {
    return a * b
}

// testando
console.log(multiplicar())       // 1 * 1
console.log(multiplicar(5))      // 5 * 1
console.log(multiplicar(4, 2))   // 4 * 2
console.log('\n')

//fora da funçao mod.
let total = 0
console.log('total atual: ' + total)

//sma um valor na variável externa
function somarAoTotal(valor) {
    total += valor
}

// testando a modificação da variável
somarAoTotal(10)  // vira 10
console.log('depois de somar 10: ' + total)

somarAoTotal(5)   // vira 15
console.log('depois de somar 5: ' + total)
