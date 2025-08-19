const caixa=document.querySelector("#caixa")

let cores=["azul","verde","vermelho"["claro", "escuro", "medio"]]
let cursos=["HTML","CSS","JavaScript", cores]
//cursos[0]="C++"

//cursos.push("c++")//push add
//cursos.unshift("pythonn")//unshift adiciona no inicio
//cursos.pop()//pop retira o ultimo elemento
//cursos.shift()//shift tita do inicio



console.log(cursos[3][1][4][5])
//console.log(cursos[0])


cursos.map((el)=>{
    let p=document.createElement("p")
    p.innerHTML=el
    caixa.appendChild(p)
})
