// usando o for normal
function soma(...valores){
    let tamanho = valores.length
    let resultado = 0
    for (let i=0; i<tamanho; i++){
        resultado += valores[i]
    }
    return resultado
}

console.log(soma(10,5,2,8))

// usando for or
function soma(...valores){
    let resultado = 0
    for (let valor of valores){
        resultado += valor
    }
    return resultado
}

console.log(soma(10,5,2,8))