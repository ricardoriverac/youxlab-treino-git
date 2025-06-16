//INSERIR ELEMENTOS NO DOM EM POSIÇÕES ESPECÍFICAS

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

// FUNÇÃO PARA CRIAR UM NOVO CURSO
let indice=0 // --> irá dar a posição dos elementos (para NÃO ter id repetidos)

const criarNovoCurso=(curso)=>{   //curso--> nome do curso
    const novoElemento=document.createElement("div")
    novoElemento.setAttribute("id","c"+indice)
    novoElemento.setAttribute("class","curso c1")
    novoElemento.innerHTML=curso

    const comandos=document.createElement("div")
    comandos.setAttribute("class","comandos")
    
    const rb=document.createElement("input")
    rb.setAttribute("type","radio")
    rb.setAttribute("name","rb_curso")

    comandos.appendChild(rb)

    novoElemento.appendChild(comandos)

    return novoElemento
}

cursos.map((elemento,chave)=>{
    const novoElemento=criarNovoCurso(elemento)
    caixaCursos.appendChild(novoElemento)
    indice++ // --> atuializa o índice
})

//BOTÃO CURSO SELECIONADO
botaoCursoSelecionado.addEventListener("click",(evento)=>{
    const radioSelecionado=CursoSelecionado() // var recebe o contúdo dessa função (pega o elemento selecionado) 
    if(radioSelecionado!=undefined){ // Caso botão for selecionado
        const cursoSelecionado=radioSelecionado.parentNode.previousSibling.textContent //.textContent-->conteúdo string
        alert('Curso selecionado: '+cursoSelecionado)//comando para quando botão for clicado aparecer uma mensagem na tela
    }else{ // se NENHUM cursofor selecionado
        alert('SELECIONE UM CURSO')
    }
    })


//BOTÃO REMOVER CURSO
botaoRemoveCurso.addEventListener("click",(evento)=>{
    const selecionado=CursoSelecionado() // pega o curso selecionado
    try{ // utilizando o try
        const removeSelecionado=selecionado.parentNode.parentNode // pega todo conteúdo do curso selecionado
        // .parentNode.parentNode --> pega todo conteúdo 
        removeSelecionado.remove()
    }catch(indefinido){ // SE CURSO NÃO FOR SELECIONADO
        alert('SELECIONE UM CURSO')
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
        const cursoSelecionado=selecionado.parentNode.parentNode
        const novoCurso=criarNovoCurso(nomeCurso.value)
        caixaCursos.insertBefore(novoCurso,cursoSelecionado) //-->inseri o elemento antes do elemento selecionado
        }else{ // se não ALERTE
            alert("Digite um curso")
        }
    }catch(ex){
        alert("Selecione um curso")
    }
})

btnAdicionarNovoCursoDepois.addEventListener("click",(evento)=>{
    const selecionado=CursoSelecionado()
    try{
        if(nomeCurso.value!=""){
        const cursoSelecionado=selecionado.parentNode.parentNode
        const novoCurso=criarNovoCurso(nomeCurso.value)
        caixaCursos.insertBefore(novoCurso,cursoSelecionado.nextSibling) //-->inseri o elemento antes do elemento selecionado
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


