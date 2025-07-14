//PARÂMETROS REST  #P4 --> função sem n° determinado de valores 

function soma(...valores){
    let tamanhoLista=valores.length // length--> qunatidade de valores em uma lista
    let resultado=0
    for(let indice=0;indice<tamanhoLista;indice++){
        resultado+=valores[indice]
        // soma resultado mais o valor na posição do índice
    }
    return resultado
}

console.log(soma(10,5,2,8)) //--> pode adicionar uma quantidade indeterminada de valores 
console.log('\n')


//Outro exemplo FOR OF:
function soma(...valores){
    resultado=0
    for(let valor of valores){
    // Para cada valor de valores 
        resultado+=valor
    }
    return resultado
}

console.log(soma(10,5,2,8))