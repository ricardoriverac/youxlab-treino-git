const objs=document.getElementsByTagName("div")

let num=[10,20,30,40,50]

for(o in objs){
    console.log(o)
}

for(o of objs){
    console.log(o.innerHTML="Curso")
}

