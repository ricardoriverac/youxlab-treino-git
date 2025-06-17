const caixa=document.querySelector("#caixa")//usando metodo de coleçao do map
let mapa=new Map()

mapa.set("curso","JavaScript")//add elemntos
mapa.set(10,"CFB Cursos")//add elemntos
mapa.set(1,100)//add elemntos
mapa.set("canal",100)//add elemntos

mapa.delete(1)
console.log(mapa)

let pes="teste"
let res=""
if(mapa.has(pes)){
    caixa.innerHTML="A chave existe na coleção com o valor:" + mapa.get(pes)
} else{
    res="A chave NÂO está na coleção"
}
res+="<br> O tamanho da coleção é" + mapa.size
caixa.innerHTML=res
