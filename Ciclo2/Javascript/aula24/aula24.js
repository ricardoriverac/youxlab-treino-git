//FUNÇÕES ANÔNIMAS --> não possuem um nome associado então não é chamada 

//é necessário associar uma função anônima a uma var
let funcao=function(valor1,valor2){ 
    return valor1+valor2
}
console.log(funcao(10,5))
console.log('\n')


// Com parâmetros indeterminados:
let funcao2=function(...valores){ 
    let resultado=0
    for(valor of valores){
        resultado+=valor
    }
    return resultado
}
console.log(funcao2(10,5,5))
console.log('\n')


//CONSTRUTOR dentro de uma função anônima

let funcao3=new Function('numero1','numero2', 'return numero1+numero2') // Função Conastrutor Anônima
// corpo da função SEMPRE SERÁ O ÚLTIMO PARÂMETRO dentro do parênteses

console.log(funcao3(10,5))