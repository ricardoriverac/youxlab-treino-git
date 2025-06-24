//COLEÇÃO MAP

const caixa=document.getElementById("caixa")


//cria uma coleção map:
let mapa=new Map()       // foi inserida a uma variável

//adiciona elementos na coleção:
//sintaxe--> mapa.set("CHAVE","VALOR") 
mapa.set("curso","Javascript")

//adiona outro elemento: 
mapa.set(10,"CFB Cursoso") // a chave e o valor pode ser de qualquer valor
mapa.set(1,100)
mapa.set("HTML",20)

// *NÃO PODE TER CHAVES IGUAIS 


//deleta um elemento:
mapa.delete(1)


console.log(mapa)

// verifica se tem tal chave na coleção:
let pesquisa=10
let resultado=""
if(mapa.has(pesquisa)){
    resultado="A chave existe na coleção com o valor: "+ mapa.get(pesquisa) 
}else{
    resultado="A chave NÃO existe na coleção"
}
resultado+="<br/> O tamanho da coleção é: "+mapa.size 
caixa.innerHTML=resultado


// Para cada elemento
mapa.forEach((elemento)=>{
    console.log(elemento)
})



//adiociona na caixa o valor da chave curso:
//caixa.innerHTML=mapa.get("curso")  // .get-->obtem um valor da coleção map 


