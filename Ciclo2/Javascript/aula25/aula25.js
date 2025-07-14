// ARROW FUNCTION -->tipo de declaração de função anônima

// let soma=function(valor1,valor2){return valor1+valor2}

let soma=(valor1,valor2)=>{return valor1+valor2}
// troca a palavra 'function' por '=>' 
console.log(soma(10,5))
console.log('\n')


//REGRAS:

let apelido=sophia=>{return sophia}
//não precisa de parênteses caso for 1 PARÂMETRO DE ENTRADA

console.log(apelido('Sosô'))
console.log('\n')

//Sem RETURN
let adiciona=numero=>numero+10
//só é necessário as chaves se houver RETURN
//SOMENTE SE TIVER UMA LINHA NO CORPO DA FUNÇÃO

console.log(adiciona(10))
console.log('\n')

