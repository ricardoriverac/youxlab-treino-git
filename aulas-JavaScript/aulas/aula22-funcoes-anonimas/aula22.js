let funcao = function (valor1, valor2){
    return valor1 + valor2
}

console.log(funcao(10,5))

// usando o ...
const funcao2 = function(...valores){
    let resultado = 0
    for (let valor of valores){
        resultado+=valor
    }
    return resultado
}
console.log(funcao2(10,5))

// funcao construto anonimo
const funcao3 = new Function('valor1', 'valor2', 'return valor1+valor2')
console.log(funcao3(10,9))