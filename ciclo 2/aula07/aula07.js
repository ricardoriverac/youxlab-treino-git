// && --> and/e
// ||--> or/ou
// !! --> not/não
let num1=10,num2=5,num3=15,num4=20//dando valor aos numeros 
console.log("MOstrando numeros na tabela Verdade, Falsa:")
console.log((num1>num2)&&(num1>num3))//comparando os valores usando a tabela da verdade 
console.log((num1>num2)&&(num3<num4))//retornou true, seguidno a tabela
console.log((num1>num2)||(num1>num3))//tabela do or/ou,  de comparação
console.log(!(num1<num2)||(num1>num3))//inversão
if(num1>num2){
    console.log(num1 + "verdadeiro " +num2)//usando if fica assim:
    }else{
        console.log(num1 + "falso" + num2)
    }
