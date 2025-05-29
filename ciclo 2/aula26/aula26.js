const soma = (...valores)=>{//função arrow 
    const somar = val=>{ //funçao somar
        let res=0
        for(v of val)//o valor da arrya foi para o "V" vindo do val
            res+=v
        return res// retorno da soma 
    }
    return somar (valores)
}
console.log(soma(10,5,15))
valor=[10,15,20]
console.log(soma(...valor))