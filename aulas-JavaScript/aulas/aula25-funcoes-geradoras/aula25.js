function* cores(){
    yield 'Vermelho'
    yield 'Verde'
    yield 'Azul'
}

let itc = cores()
console.log(itc.next().value)
console.log(itc.next().value)
console.log(itc.next().value)
console.log(itc.next().value) // retorna undefined pq só tem 3 yield

function* perguntas(){
    const nome = yield 'Qual seu nome?'
    const esporte = yield 'Qual seu esporte favorito?'
    return 'Seu nome é ' + nome + ', seu esporte favorito é ' + esporte
}

const itp = perguntas()
console.log(itp.next().value)
console.log(itp.next('Tayla').value)
console.log(itp.next('Futebol').value)

// usando com um loop
function* contador(){
    let i=0
    while (true){
        yield i++    // loop infinito
        if (i>5){
            break
        }
    }
}
const iteradorC = contador()  // da pra fazer so com console.log normal
for (let i=0; i<10; i++){
    console.log(iteradorC.next().value)
}

// fazendo com for of tem q colocar o break dentro da função pra não ficar em um loop infinito
for (let c of iteradorC){
    console.log(c)
}