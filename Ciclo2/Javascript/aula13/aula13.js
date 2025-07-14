// IF e IF ELSE

//false
let numero=10
if(numero>10)
    console.log('número maior que 10')

console.log('Fim do programa \n')

//true
numero=100
if(numero>10)
    console.log('número maior que 10')

console.log('Fim do programa \n')

// se o if tiver 1 COMANDO NÃO É NECESSÁRIO USAR CHAVES 
//MAIS DE 1 COMANDO É NECESSÁRIO:
numero=100
if(numero>10){
      console.log('número maior que 10')
      console.log('verdadeiro')
}

console.log('Fim do programa \n')



// com 2 blocos de comando:
numero=10
if(numero>10){ // se for true
    console.log('número maior que 10')
    console.log('verdadeiro')
}else{ // se for false
    console.log('número menor ou igual a 10')
    console.log('falso')
}

console.log('Fim do programa \n')

// com 3 blocos de comando
numero=10
if(numero>10){ // SE
    console.log('número maior que 10')
}else if(numero>5){ // SE NÃO SE 
    console.log('número está entre 6 ou 10')
}else{ // SE NÃO
    console.log('número menor ou igual a 5')
}

console.log('Fim do programa \n')

//com 4 blocos de comando
numero=100
if(numero>10){ // SE
    console.log('número maior que 10')
    if(numero>50){
         console.log('número maior que 50')
    }
}else if(numero>5){ // SE NÃO SE 
    console.log('número está entre 6 ou 10')
}else{ // SE NÃO
    console.log('número menor ou igual a 5')
}

console.log('Fim do programa \n')

//com outras EXPRESSÕES
let graus=32
let clima='sol'

if(graus>30 && clima=='sol'){ // SE
    console.log('vou a praia')
}else{ // SE NÃO
    console.log('vou ao cinema')
}

console.log('Fim do programa \n')