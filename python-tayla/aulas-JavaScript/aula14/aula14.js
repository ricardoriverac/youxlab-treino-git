let numeros=[10,20,30,40,50]

for(numero in numeros){ // o FOR in pega o indice
    console.log(numeros[numero])
}

for(numero of numeros){ // o FOR of pega os números 
    console.log(numero)
}

const objetos=document.getElementsByTagName('div')

for(objeto of objetos){
    console.log(objeto.innerHTML='Curso')
}

for(objeto in objetos){
    console.log(objeto)
}