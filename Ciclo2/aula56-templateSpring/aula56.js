// TEMPLATE STRINGS

const caixa=document.getElementById("caixa")

const curso="Javascript"
const canal="CFB Cursos"

//modo comun:
// const frase="Este é o curso de "+curso+" do canal "+canal

//usando o template strings:
const frase=`Este é o curso de ${curso} do canal ${canal}`

caixa.innerHTML=frase


//outro exemplo:

const carros=["Polo","Gol","T-Cros","HIV",]

//lista dos elemento:
let ul=`<ul>`

carros.map((elemento)=>{
    ul+=`<li>${elemento}</li>`
})

ul+=`</ul>`

caixa.innerHTML=ul

