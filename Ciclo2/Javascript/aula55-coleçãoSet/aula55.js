// COLEÇÃO SET--> não permite elementos duplicados

const caixa=document.getElementById("caixa")

//Cria uma coleção set:
let musicas= new Set(["A flor", "2+2=5", "Arials"])

//adiciona um elemento:
musicas.add("Praga")

//NÃO ADICIONA:
musicas.add("A flor")    //não adiciona pois já tem um valor igual na coleção
//deleta um elemento:
musicas.delete("Praga")

//limpar toda a coleção:
// console.clear()

console.log(musicas)


//percorre a coleção:
musicas.forEach((elemento)=>{
    caixa.innerHTML+=elemento+"<br/>" //Adiciona os elementos na caixa
})

// //de outra forma 
// for(let music of musicas){
//     caixa.innerHTML+=music+"<br/>"
// }
