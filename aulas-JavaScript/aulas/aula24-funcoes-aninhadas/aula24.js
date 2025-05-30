const soma = (...valores)=>{
    const somar = valor =>{
        let resultado = 0
        for (v of valor){
            resultado += v
        }
        return resultado
    }
    return somar(valores) // ta retornando o retorno da outra função
}

console.log(soma(10, 5, 15))