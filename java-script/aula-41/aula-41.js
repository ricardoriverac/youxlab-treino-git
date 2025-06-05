const caixa1=document.querySelector("#caixa1")
const btn_c=[...document.querySelectorAll(".curso")]
const c1_2=document.querySelector("#c1_2")
const cursos=["HTML","CSS","Javascript","PH8","React","MySQL","ReactNative"]

cursos.map((el,chave)=>{
    const novoElemento=document.createElement("div")
    novoElemento.setAttribute("id","c"+chave)
    novoElemento.setAttribute("class","curso c1")
    novoElemento.innerHTML=el
    const btn_lixo=document.createElement("img")
    btn_lixo.setAttribute("scr","file:///home/youx/fotos/54324.png")
    btn_lixo.setAttribute("class","btn_lixo")
    btn_lixo.addEventListener("click",(evt)=>{
        console,console.log(evt.target);
        caixa1.removeChild(evt.target.parentNode)
    })
    novoElemento.appendChild(btn_lixo)
    caixa1.appendChild(novoElemento)
})