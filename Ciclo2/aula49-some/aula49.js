//MÉTODO SOME --> verifica se pelo menos UM item do array atende a uma condição

const p_array=document.getElementById('array') 
const btnVerificar=document.getElementById('btnVerificar') //input 
const resultado=document.getElementById('resultado')


const elemento_array=[16,12,10,17,15,23,11]

//adiciona os elementos do array na var p_array
p_array.innerHTML='[ '+elemento_array+' ]' // mostra os elementos no site 


//BOTÃO VERIFICAR--> verifica os números do array

btnVerificar.addEventListener("click",(evento)=>{
    const retorno= elemento_array.some((elemento,indice)=>{
        if(elemento<18){    //se algum elemento do array for menor que 18
            resultado.innerHTML="NÃO tem número maior que 18!"
        }
        return elemento>=18    // verifica se o array tem n° maior que 18
    })

    if(retorno){    // se o array tiver todos os n° maior que 18
        resultado.innerHTML="Tem número maior que 18!"
    }
    console.log(retorno)
})



