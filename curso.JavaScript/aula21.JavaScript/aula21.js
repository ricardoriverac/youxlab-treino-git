function parOuImpar(n1, n2){
    res = n1 * n2
    console.log(n1 + " X " + n2 + ' = ' + res)
    if (res%2 == 0){
        return console.log("PAR")
    }else{
        return console.log('ÍMPAR')
    }
}

parOuImpar(3, 9)
for (i = 1; i < 20; i++){
    parOuImpar(i, 3)
}