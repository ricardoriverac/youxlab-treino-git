//OPERADORES LÓGICOS

/*
OPERADORES LÓGICOS:
&&: and,  ||: or,  !: not
*/

let numero1=2,numero2=1,numero3=7,numero4=4

console.log((numero1>numero2)&&(numero1>numero3))// &&--> true + false = false
// o comando a cima resultará false de acordo com o comando &&

console.log((numero1<numero2)&&(numero1>numero3))// &&--> false + false = false
// o comando a cima resultará false de acordo com o comando &&

console.log((numero1>numero2)&&(numero1<numero3))// &&--> true + true = true
// o comando a cima resultará true de acordo com o comando &&


console.log((numero1>numero2)||(numero1<numero3))// ||--> true + true = true
// o comando a cima resultará true de acordo com o comando ||

console.log((numero1>numero2)||(numero1<numero3))// ||--> true + false = true
// o comando a cima resultará true de acordo com o comando ||

console.log((numero1<numero2)||(numero1>numero3))// ||--> false + false = false
// este comando a cima resultará false de acordo com o comando ||


console.log(!((numero1>numero2)||(numero1<numero3)))// !--> true + true = false
// o comando a cima resultará false de acordo com o comando !


// se núm1 maior que núm2
if(numero1>numero2){
    console.log(numero1+' MAIOR que '+numero2)
}else{
    console.log(numero1+' MENOR que '+numero2)
}

// se núm1 menor que núm2
if(numero1<numero2){
    console.log(numero1+' MAIOR que '+numero2)
}else{
    console.log(numero1+' MENOR que '+numero2)
}


// COM OPERADORES LÓGICOS
// se núm1 for MAIOR que núm2 e(&&) se núm3 for MAIOR que núm4 
if((numero1>numero2)&&(numero3>numero4)){
    console.log('VERDADEIRO')
}else{
    console.log('FALSO')
}

// se núm1 for MAIOR que núm2 ou(||) se núm3 for MAIOR que núm4 
if((numero1>numero2)||(numero3>numero4)){
    console.log('VERDADEIRO')
}else{
    console.log('FALSO')
}

// se não(!) núm1 for MAIOR que núm2 ou(||) se núm3 for MAIOR que núm4 
// negação em somente uma das operações 
// ||--> false + true = true
if(!(numero1>numero2)||(numero3>numero4)){
    console.log('VERDADEIRO')
}else{
    console.log('FALSO')
}

// negação em somente uma das operações 
// &&--> false + true = false
if(!(numero1>numero2)||(numero3>numero4)){
    console.log('VERDADEIRO')
}else{
    console.log('FALSO')
}