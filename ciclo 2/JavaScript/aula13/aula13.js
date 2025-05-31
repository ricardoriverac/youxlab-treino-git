let num = 10;  // Definindo o valor de como 100
if (num > 10) { 
  console.log('Número maior que 10'); 
  console.log('Verdadeiro');
}
console.log('Fim do programa \n');  
//agota com else 
if (num > 10) {  // se num for maior que 10...
  console.log('Número maior que 10'); 
  console.log('Verdadeiro');  // E isso também
} else {  // se num for 10 ou menor)...
  console.log('Número menor ou igual a 10')
  console.log('Falso'); 
}
console.log('Fim do programa \n');
//agora esle if
if (num > 10) {
  console.log('Número maior que 10');    
} else if (num > 5) {  // se num for maior que 5, mas não maior que 10
  console.log('Número está entre 6 e 10');
} else { 
  console.log('Número menor ou igual a 5');
}
console.log('Fim do programa \n');

if (num > 10) {  
  console.log('Número maior que 10');
  if (num > 50) { 
    console.log('Número maior que 50');
  }
} else if (num > 5) {  
  console.log('Número está entre 6 e 10');
} else { 
  console.log('Número menor ou igual a 5'); 
}
console.log('Fim do programa \n');
//expressão diferente:
let graus = 32;  // Definindo a temperatura
let clima = 'sol';
if (graus > 30 && clima === 'sol') {  // se estiver mais de 30 graus se tive sol
  console.log('Vou à praia');  
} else { 
  console.log('Vou ao cinema'); 
}
console.log('Fim do programa \n');
