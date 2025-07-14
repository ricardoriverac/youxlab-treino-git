const caixaCursos=document.querySelector("#caixaCursos")
const btn_c=[...document.querySelectorAll(".curso")]
const c1_2=document.querySelector("#c1_2")
const cursos=["HTML","CSS","Javascript","PHP","React","MySQL","ReactNative"]
const botaoCursoSelecionado=document.getElementById("botaoCursoSelecionado")

cursos.map((elemento,chave)=>{
    const novoElemento=document.createElement("div")
    novoElemento.setAttribute("id","c"+chave)
    novoElemento.setAttribute("class","curso c1")
    novoElemento.innerHTML=elemento

    const comandos=document.createElement("div")
    comandos.setAttribute("class","comandos")
    
    const rb=document.createElement("input")
    rb.setAttribute("type","radio")
    rb.setAttribute("name","rb_curso")

    comandos.appendChild(rb)

    novoElemento.appendChild(comandos)

    caixaCursos.appendChild(novoElemento)
    
})

//BOTÃO CURSO SELECIONADO
botaoCursoSelecionado.addEventListener("click",(evento)=>{
    const todosRadios=[...document.querySelectorAll("input[type=radio]")] //Coloca em uma array TODOS elementos input qu eti ver o type=radio

    let radioSelecionado=todosRadios.filter((elemento)=>{ //pegando o objeto selecionado de uma coleção
        return elemento.checked //-->retorna somente os que estão selecionados
    })
    radioSelecionado=radioSelecionado[0]

// pega o texto que está ao lado (ou acima) do botão de rádio que foi selecionado.
// Ou seja, só mostra o nome do curso do botão marcado, ignorando os outros.

    //const cursoSelecionado=radioSelecionado.parentNode.parentNode.firstChild.textContent
    const cursoSelecionado=radioSelecionado.parentNode.previousSibling.textContent //.textContent-->conteúdo string
    alert("Curso selecionado: " + cursoSelecionado)
    // console.log(todosRadios)
    console.log(radioSelecionado)
    // console.log(cursoSelecionado)
})

// parentNode
// childNodes[nodenumber]
// firstChild -->aponta para o texto
// lastChild
// nextSibling
// previousSibling -->irmão anterior --> object text
