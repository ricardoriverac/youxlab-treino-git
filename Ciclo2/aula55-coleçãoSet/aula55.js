// COLEÇÃO SET--> não permite entrada duplicada de valor

const caixa=document.getElementById("caixa")

//Cria uma coleção set:
let musicas= new Set(["A flor", "2+2=5", "Arials"])

//adiciona um elemento:
musicas.add("Praga")

//NÃO ADICIONA:
musicas.add("A flor")    //não adiciona pois já tem um valor igual na coleção


console.log(musicas)


//percorre a coleção:
musicas.forEach(()=>{

})