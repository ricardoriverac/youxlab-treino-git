const caixa=document.querySelector("#caixa")

const carros=["Polo","Golf","T-Cross","HRV"]

let ul=`<ul>`
carros.map((el)=>{
    ul+=`<li>${el}</li>`
})
ul+`</ul>`


caixa.innerHTML=ul
 //const canal  ="CBF Cursos"
 //const cursos ="JavaScript"
 //const frase ="Este é o curso de:" + cursos + "do canal" + canal   
//const frase= `este é o\n
//curso de ${curso} do \n canal ${canal}`

//console.log(frase)
//caixa.innerHTML=frase