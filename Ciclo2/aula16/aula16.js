// LOOPS FOR IN E FOR OF --> melhor para percorrer coleções

const objetos= document.getElementsByTagName('div')

let numeros=[10,20,30,40]

//FOR IN
// para cada número em número 
for(objeto in objetos){
    console.log(objetos[objeto].innerHTML) // imprime as posições dos elementos

}


//FOR OF
// vai dentro do elemento da coleção que ele está interando
for(objeto of objetos){ 
    console.log(objeto.innerHTML='Curso') // imprime os valores diretamente
}


//USANDO O FOR 
/*for(let indice=0;indice<numeros.length; indice++){
    console.log(indice) // imprime as posições
    console.log(numeros[indice]) // imprime os valores em suas posições
}*/