const caixa1=document.querySelector("#caixa1")
const btn_c1=document.querySelector("#c1")
const cursos=[...document.querySelectorAll(".curso")]


caixa1.addEventListener("click",(evt)=>{
    console.log("clicou ai rpz")
        console.log(evt)

})
 cursos.map((el)=>{
     btn_c1.addEventListener("click",()=>{
        evt.stopPropagation()
     })

 })
//caixa1.addEventListener("click",(evt)=>{
  //  console.log(evt)



