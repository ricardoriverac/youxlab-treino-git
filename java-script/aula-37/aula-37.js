const caixa1=document.querySelector("#caixa1")
const btn_c1=document.querySelector("#c1")
const curso=[...document.querySelectorAll(".curso")]
caixa1.addEventListener("click",(evt)=>{
    console.log("foi")
    console.log(evt)
})
curso.map((el)=>{
    el.addEventListener("click",(evt)=>{
        evt.stopPropagation()
    })
})