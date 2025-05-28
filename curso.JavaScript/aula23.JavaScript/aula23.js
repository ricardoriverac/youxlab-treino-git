function valores (...valores){
    let tam = valores.length
    let res = 0
    for(let i=0; i <tam; i++){
        res += valores[i]
    }
    return res
}

console.log(valores(5, 6, 8, 2))