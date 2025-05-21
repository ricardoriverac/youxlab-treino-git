/* && and ou e
|| or ou
! not ou não*/

let num1, num2, num3, num4

num1 = 2
num2 = 7
num3 = 10
num4 = 1
console.log((num1>num4)&&(num2<num1))
console.log((num1==num3)||(num2>=num1))
console.log(!(num1==num3)||(num2>=num1))

if(num1>num2){
    console.log(num1 + " maior que " + num2)
}else{
    console.log(num1 + " menor que " + num2)
}

if((num1>num2) && (num4>num3)){
    console.log('falso')
}else{
    console.log('verdadeiro')
}

if((num1>num2) || (num4>num3)){
    console.log('falso')
}else{
    console.log('verdadeiro')
}