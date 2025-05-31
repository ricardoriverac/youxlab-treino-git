//funçao geradora vc pode ir retornado durante a execuçao
//é o pilar do js

function* perguntas(){
    const nome=yield'Qual é o seu nome?'
    const idade= yield'Qual é a sua idade?'
    const altura = yield 'Qual é sua altura?'
    return "Seu nome é" + nome + ", sua idade é" + idade + ", sua altura é" +altura
}

const itp=perguntas()
console.log(itp.next("").value)//o "." puxa
console.log(itp.next("16").value)//o "." puxa
console.log(itp.next('').value)//o "." puxa

//contador
function * contador(){
    let i=0
    while(true){
        yield i++
         if(i>6)
            break
    }
}

const itc=contador()
for (let c of itc){
    console.log(c)
}
