// FUNÇÕES COM RETORNO  #P2
// *SEMPRE QUE É EXECUTADO O RETURN A FUNÇÃO PARA

function nome(){ // Função que retorna uma str
    return 'Sophia'
}

console.log(nome()) // retorno da função foi imprimido com console.log
console.log(nome())
console.log(nome())
console.log('\n')


//Outro exemplo:
function multiplicacao(){
    let numero1=10
    let numero2=20
    let resultado=numero1*numero2
    return resultado
}

console.log(multiplicacao())// retorno da função foi imprimido DIRETO com console.log

// podemos colocar o retorno da função em uma var
let numero=multiplicacao()
console.log(numero) 
console.log('\n')


//Retornando com situações diferentes:
//PAR OU IMPAR
function divisao(){
    let numero1=10
    let numero2=2
    let resultado=numero1/numero2
    if(resultado%2==0){
        return 'Par'
    }else{
        return 'Impar'
    }
}
let resultado=divisao()
console.log(resultado)


