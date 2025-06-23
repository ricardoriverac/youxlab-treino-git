//MÉTODO REDUCE --> verifica se pelo menos UM ITEM do array atende a uma condição

const p_array=document.getElementById('array') 
const btnReduzir=document.getElementById('btnReduzir') //input 
const resultado=document.getElementById('resultado')


const elemento_array=[1,2,3,4,5]
let ant=[]
let atu=[]
let dobro=[]

//adiciona os elementos do array na var p_array
p_array.innerHTML='[ '+elemento_array+' ]'         // mostra os elementos no site 


//BOTÃO REDUZIR--> verifica os números do array

btnReduzir.addEventListener("click",(evento)=>{
    dobro.push(elemento_array[0]*2) //Par apegar o 1° elemento
     resultado.innerHTML=elemento_array.reduce((anterior,atual,posicao)=>{
        ant.push(anterior) //Somente os números anteriores
        atu.push(atual) // Somente os números atuais
        dobro.push(atual*2) //Somente os números atuais multiplicado por 2
        return atual+anterior
    })
    resultado.innerHTML+="</br>Anterior:"+ant+"</br>Atual:"+atu+"</br>Dobro:"+dobro
})



