//const c1=document.getElementById("c1")
//const c1=document.querySelector("#c1")

const cursos=[...document.querySelector("#c1")]


cursos.map((el)=>{
    el.addEventListener("click",(evt)=>{
        const el=evt.target
        el.classList.add("destaque")
        console.log(el.id + "foi clicado moço")
    })
})


//function msg(){ //pode usar const
  //  alert("oii,gracinha")
//}

//c1.addEventListener("click",(evt)=>{
  //  const el=evt.target
   // el.classList.add("destaque")
    //alert("ois,gracinha")
    //msg()
//})