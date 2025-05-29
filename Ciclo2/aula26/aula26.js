// FUNÇÕES ANINHADAS 
const soma=(...valores)=>{ // Função que recebe um array com os valores
// a função soma chama a função somar 
    const somar=val=>{ // Função que FAZ a soma 
        let total=0
        for( let numero of val){ // Para cada número de valores
            total+=numero
        }
        return total //retorna/mostra o total apos o loop
    }
    return somar(valores) // Chama a função somar passando os valores recebidos pela função principa
}

console.log(soma(1,2,3)) 