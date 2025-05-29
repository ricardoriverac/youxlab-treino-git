const soma=(...valores)=>{
    const somar=val=>{
        let res = 0
        for(v of val)
            res+=v
        return res
}
   return somar(valores)
    
}
console.log(soma(3, 45, 2, 12, 8, 15, 14, 1))