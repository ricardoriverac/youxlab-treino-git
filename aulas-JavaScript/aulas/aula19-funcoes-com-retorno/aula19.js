function canal(){
    let numero1 = 10
    let numero2 = 2
    let resultado = numero1 * numero2
    if (resultado%2 == 0){
        return 'Par'
    }else{
        return 'Ímpar'  // a partir do momento que o programa encontra um return ele interrompe
    }
}

let resposta = canal()

console.log(resposta)