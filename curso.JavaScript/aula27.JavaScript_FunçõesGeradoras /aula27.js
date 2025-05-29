function* cores(){
    yield 'Rosa'
    yield 'Roxo'
    yield 'Branco'
}

const itc = cores()
console.log(itc.next().value)
console.log(itc.next().value)
console.log(itc.next().value)

function* perguntas (){
   const nome = yield 'Qual o seu nome?'
   const esporte = yield 'Qual esporte você mais gosta?'
   return 'Seu nome é ' + nome + ' e seu esporte favorito é ' + esporte
    }

const p = perguntas()
console.log(p.next().value)
console.log(p.next('Ana Clara').value)
console.log(p.next('vôlei.').value)

function* contador(){
    let i = 0
    while(true){
        yield i++
        if (i>25)
            break
        }
    }

let c = contador()

for (i = 0; i < 26; i++){
    console.log(c.next().value)
}
