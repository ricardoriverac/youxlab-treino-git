//MÉTODO EVERY -->verifica e procura equivalências

const p_array=document.getElementById('array') 
const btnVerificar=document.getElementById('btnVerificar') //input 
const resultado=document.getElementById('resultado')


// const elemento_array=["html","css","javascript"] -->podendo ser também um array com strings

const elemento_array=[0,25,20,22,29,25,20]

//adiciona os elementos do array na var p_array
p_array.innerHTML='[ '+elemento_array+' ]' // mostra os elementos no site 


//BOTÃO VERIFICAR--> verifica os números do array

btnVerificar.addEventListener("click",(evento)=>{
    const retorno= elemento_array.every((elemento,indice)=>{
        if(elemento<18){    //se algum elemento do array for menor que 18
            resultado.innerHTML="Número menor que 18 na posição "+indice+"!"
        }
        return elemento>=18    // verifica se o array tem n° maior que 18
    })

    if(retorno){    // se o array tiver todos os n° maior que 18
        resultado.innerHTML="Todos maior de 18!"
    }
    console.log(retorno)
})



