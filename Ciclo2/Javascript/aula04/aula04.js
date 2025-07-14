//OPERADOS E OPERAÇÕES ARITMÉTICAS

/*
OPERADORES:
soma: + , subtração:- , divisão:/ , multiplicação: * 
resto de divisão: % , incremento: ++/+= , decremento: --/-=
*/

let numero1= 0,numero2= 0,soma= 0,multiplicação= 0,divisão=0,resto=0
numero1=9 // atribuindo valor as variáveis
numero2=2
console.log('Núm1:' +numero1)// mostra valor das variáveis
console.log('Núm2:' +numero2)

soma=numero1+numero2 
console.log('Soma:' +soma) // resultado da soma

console.log(numero1-numero2) // subtração diretamente pelo console.log()

multiplicação=(numero1+numero2)*2 // multiplica a soma dos dois valores por 2
console.log('multiplicação:' +multiplicação) // resultado da multiplicação

divisão=(numero1-numero2)/2 // divide a subtração dos dois valores
console.log('divisão:' +divisão)

numero1=2
numero2=15
resto=numero2%numero1 // divide os dois valores
console.log('resto da divisão 15/2:' +resto) // retorna resto da divisão

numero1=9 
numero2=2
numero1++ // incremento: soma 1 ao valor da váriavel
console.log('incremento:'+numero1) //retorna numero1+1

numero1=9
numero2=2
numero1-- // decremento: subtrai 1 ao valor da váriavel
console.log('decremento:'+numero1) // retorna numero1-1

numero1=9
numero2=2
numero1+=1  // semelhante ao incremento. igual a: numero1= numero1+1
console.log('+=:' +numero1)

numero1=9
numero2=2
numero1-=1 // semelhante ao decremento. igual a: numero1= numero1-1
console.log('-=:' +numero1)

numero1=9
numero2=2
numero1*=2 //Também funciona com outros operadores 
console.log('*=:' +numero1)