//MÉTODO TOGGLE

//Delclarando elementos em variáveis 
const caixaCursos=document.querySelector("#caixaCursos")
const btn_c=[...document.querySelectorAll(".curso")]
const c1_2=document.querySelector("#c1_2")
const cursos=["HTML","CSS","Javascript","PHP","React","MySQL","ReactNative"]
const botaoCursoSelecionado=document.getElementById("botaoCursoSelecionado")
const botaoRemoveCurso=document.getElementById("botaoRemoveCurso")


//Declarando o curso DIGITADO:
const nomeCurso=document.getElementById("nomeCurso")
 
//FUNÇÃO QUE RECEBE O CURSO SELECIONADO
const CursoSelecionado=()=>{ 
    const todosRadios=[...document.querySelectorAll("input[type=radio]")] //Coloca em uma array TODOS elementos input que tiver o type=radio

    let radioSelecionado=todosRadios.filter((elemento)=>{ //pegando o objeto selecionado de uma coleção
        return elemento.checked //-->retorna somente os que estão selecionados
    })
    return radioSelecionado=radioSelecionado[0]
}


let indice=0 // --> irá dar a posição dos elementos (para NÃO ter id repetidos)

//FUNÇÃO PARA SELECIONAR SOMENTE UM CURUSO
const tirarSelecao=()=>{
    const cursosSelecionados=[...document.querySelectorAll(".selecionado")]
    cursosSelecionados.map((elemento)=>{
        elemento.classList.remove("selecionado") // retira a seleção do que ja foi clicado
    })
}

// FUNÇÃO PARA CRIAR UM NOVO CURSO
const criarNovoCurso=(curso)=>{   //curso--> nome do curso
    const novoElemento=document.createElement("div")
    novoElemento.setAttribute("id","c"+indice)
    novoElemento.setAttribute("class","curso c1")
    novoElemento.innerHTML=curso
    novoElemento.addEventListener("click",(evento)=>{
        tirarSelecao()
        evento.target.classList.toggle("selecionado")
    })
    return novoElemento
    //FOI RETIRADO OS RADIOS (bolinhas)
}

cursos.map((elemento,chave)=>{
    const novoElemento=criarNovoCurso(elemento)
    caixaCursos.appendChild(novoElemento)
    indice++ // --> atuializa o índice
})

//FUNÇÃO DE CURSO SELECIONADO
const cursoSelecionado = () => {
    const cursoSelecionado=[...document.querySelectorAll(".selecionado")] // elemento com classe selecionado
    return cursoSelecionado[0] // retorna DIRETAMENTE o curso selecinado 
}



//BOTÃO CURSO SELECIONADO
botaoCursoSelecionado.addEventListener("click",(evento)=>{
    try{
        alert("Curso selecionado: "+ cursoSelecionado().innerHTML) // mostar o TEXTO do selecionado
    }catch(ex){
        alert("Selecione um curso")
    }
})

//BOTÃO REMOVER CURSO
botaoRemoveCurso.addEventListener("click",(evento)=>{
    const cs=cursoSelecionado() // var recebe o curso selecionado
    if(cs!=undefined){ // se var for diferente de indefinido
        cs.remove()
    }else{
        alert("Selecione um curso")
    }
})




//Declarando os novos botoẽs:
const btnAdicionarNovoCursoAntes=document.getElementById("btnAdicionarNovoCursoAntes")
const btnAdicionarNovoCursoDepois=document.getElementById("btnAdicionarNovoCursoDepois")

//BOTÃO Adiciononar Novo Curso Antes
btnAdicionarNovoCursoAntes.addEventListener("click",(evento)=>{
    const selecionado=CursoSelecionado()
    try{
        if (nomeCurso.value!=""){ // se a var nomeCurso NÃO estiver vazia
        const novoCurso=criarNovoCurso(nomeCurso.value)
        caixaCursos.insertBefore(novoCurso,cursoSelecionado()) //-->inseri o elemento antes do elemento selecionado
        }else{ // se não ALERTE
            alert("Digite um curso")
        }
    }catch(ex){
        alert("Selecione um curso")
    }
})

btnAdicionarNovoCursoDepois.addEventListener("click",(evento)=>{
    try{
        if(nomeCurso.value!=""){
        const novoCurso=criarNovoCurso(nomeCurso.value)
        caixaCursos.insertBefore(novoCurso,cursoSelecionado().nextSibling) //-->inseri o elemento antes do elemento selecionado
        }else{
            alert("Digite um curso")
        }
    }catch(ex){
        alert("Selecione um curso")
    }
})

// parentNode
// childNodes[nodenumber]
// firstChild -->aponta para o texto
// lastChild
// nextSibling
// previousSibling -->irmão anterior --> object text


