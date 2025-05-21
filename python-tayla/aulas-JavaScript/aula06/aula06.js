/*
&& -> and
|| -> or
! -> not
*/

let numero1, numero2, numero3, numero4
numero1=10, numero2=5, numero3=15, numero4=2

console.log((numero1>numero2)&&(numero1>numero3)) // -> and
console.log((numero1>numero2)||(numero1>numero3)) // -> or
console.log(!(numero1>numero2)||(numero1>numero3)) // -> not

if(numero1>numero2){
    console.log(numero1 + ' maior que ' + numero2)
}else{
    console.log(numero1 + ' menor que ' + numero2)
}

if((numero1>numero2) && (numero3>numero4)){
    console.log('verdadeiro')
}else{
    console.log('falso')
}