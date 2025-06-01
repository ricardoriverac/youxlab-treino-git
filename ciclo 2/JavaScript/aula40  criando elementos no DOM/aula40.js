const caixa1 = document.querySelector("#caixa1")
const btn_c = [...document.querySelectorAll(".curso")]
const c1_2 = document.querySelector("#c1_2")
const cursos=["HTML" ,"CSS", "Javascript", "PHP","React","MySQL"]

cursos.map((el,chave)=>{
    
    const NovoElemento=document.createElement("div")
    NovoElemento.setAttribute("id", "c"+chave+1)
    NovoElemento.setAttribute("class", "curso c1")
    
    NovoElemento.innerHTML="ReactNative"
    
    caixa1.appendChild(NovoElemento)

})