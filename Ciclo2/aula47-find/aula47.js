//MÉTODO FIND -->pesquisa um elemento de um array

const p_array=document.getElementById('array') 
const txt_pesquisar=document.getElementById('txt_pesquisar') //input 
const btnPesquisar=document.getElementById('btnPesquisar')
const resultado=document.getElementById('resultado')


// const elemento_array=[10,5,8,2,9,15,20] -->podendo ser também um array numérico

const elemento_array=["html","css","javascript"]
//adiciona os elementos do array na var p_array
p_array.innerHTML='[ '+elemento_array+' ]' // mostra os elementos no site 


//BOTÃO PESQUISAR
btnPesquisar.addEventListener("click",(evento)=>{
    resultado.innerHTML="Valor não encontrado" //define a mensagem padrão
    //função para pesquisar no array
    const retorno=elemento_array.find((elemento,indice)=>{
        if (elemento.toUpperCase()==txt_pesquisar.value.toUpperCase()){ //toUperCase-->trasforma os valores em maiúscula
            resultado.innerHTML="Valor encontrado "+elemento+" na posição "+indice //redefine a mensagem caso tenha o elemento no array
            return elemento
        }
    })
    console.log(retorno)
})