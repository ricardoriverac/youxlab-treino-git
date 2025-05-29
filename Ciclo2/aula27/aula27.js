//Funções Geradoras-->tem seu retorno ADIADO até que a gente precise desse retorno]

function* cores(){ //function*-->COMANDO de função geradora 
    yield 'Vermelho'
    yield 'Amarelo' // A função para e RETORNA O VALOR DIRETAMENTE SE TIVER O YIELD
    yield 'Azul'
}

const interator=cores() // iseriu a função em uma var
console.log(interator.next().value) 
// nesta chamada foi retornada VERMELHO pois é o VALOR do 1° YIELD

console.log(interator.next().value)
// nesta chamada foi retornada Amarelo pois a função RETORNA DE ONDE ELA PAROU (no caso, no 2° yield )


console.log(interator.next().value)
// nesta chamada foi retornada Azul pois a função RETORNA DE ONDE ELA PAROU (no caso, no 3° yield )
console.log('\n')



//Outro exemplo:
function* perguntas(){
    const nome=yield 'Qual seu nome? '  // yield--> ponto de parada
    const esporte=yield 'Qual seu esporte favorito? '
    return 'Seu nome é '+nome+', seu esporte favorito é '+esporte
}

const interador= perguntas()
console.log(interador.next().value)
console.log(interador.next('Sophia').value) 
// NO NEXT FOI INSERIDO O VALOR QUE VAI ENTRAR NA FUNÇÃO 
console.log(interador.next('Futsal').value) 
console.log('\n')



//Outro exemplo com LOOP:
function* contador(){
    let indice=0
    while (true){ // loop infinito 
        yield indice++ // todas as vezes que a função for chamada indice recebe +1 
        if(indice>=10){
            break
        }
    }
}

const intera=contador()
console.log(intera.next().value)
// retorna 0 pois foi camada 1 vez
console.log(intera.next().value)
// retorna 1 pois foi camada 2 vezes
console.log(intera.next().value)
// retorna 2 pois foi camada 3 vezes
console.log('Manual\n')


for (let i=0; i<10; i++){ // de i for menor que 10 i recebe +1
    console.log(intera.next().value)
}
//Começa de onde a função PAROU por isso da 3 valores indefinidos
console.log('Com o for\n')





