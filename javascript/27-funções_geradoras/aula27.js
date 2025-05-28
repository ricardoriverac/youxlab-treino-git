function* cores(){ // Funcão geradora
    yield 'Vermelho' // Yield retorna o conteúdo
    yield 'Verde'
    yield 'Azul'
}

let itc = cores()
console.log(itc.next().value)
console.log(itc.next().value)
console.log(itc.next().value)

function* perguntas(){
    const nome = yield 'Qual seu nome?'
    const esporte = yield 'Qual seu esporte favorito?'
    return 'Seu nome é ' + nome + ', seu esporte favorito é ' + esporte

}

const itp = perguntas()
console.log(itp.next().value)
console.log(itp.next('Nagi').value)
console.log(itp.next('Futebol').value)

function* contador (){
    let i = 0
    while(true){
        yield i++
        if(i>5){
            break
        }
    }
}
const contagem = contador()
for(let c of contagem)
    console.log(c)
