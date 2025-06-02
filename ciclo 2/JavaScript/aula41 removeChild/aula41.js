const caixaCursos = document.querySelector("#caixaCursos")

const btn_c = [...document.querySelectorAll(".curso")]

const c1_2 = document.querySelector("#c1_2")

const cursos = ["HTML", "CSS", "Javascript", "PHP", "React", "MySQL", "ReactNative"]

// botão para exibir o curso selecionado
const btnCursoSelecionado = document.getElementById("btnCursoSelecionado")

// cria dinamicamente os elementos na tela
cursos.map((elemento, chave) => {
    const novoElemento = document.createElement("div")
    novoElemento.setAttribute("id", "c" + chave)
    novoElemento.setAttribute("class", "curso c1")
    novoElemento.innerHTML = elemento

    // cria container para comandos (radio button)
    const comandos = document.createElement("div")
    comandos.setAttribute("class", "comandos")
    
    // botão de seleção do curso
    const rb = document.createElement("input")
    rb.setAttribute("type", "radio")
    rb.setAttribute("name", "rb_curso")

    comandos.appendChild(rb)
    novoElemento.appendChild(comandos)
    caixaCursos.appendChild(novoElemento)
})

// botão que mostra o curso selecionado
btnCursoSelecionado.addEventListener('click', (evento) => {
    // seleciona todos os radios da página
    const todosRadios = [...document.querySelectorAll('input[type=radio]')]

    // filtra para pegar apenas o que estiver marcado
    let radioSelecionado = todosRadios.filter((elemento) => {
        return elemento.checked
    })
    radioSelecionado = radioSelecionado[0]

    // pega o nome do curso a partir da estrutura html
    const cursoSelecionado = radioSelecionado.parentNode.previousSibling.textContent

    alert(`Curso selecionado ${cursoSelecionado}`)
    console.log(cursoSelecionado)
    console.log(todosRadios)
    console.log(radioSelecionado)
})

/*
parentNode          // nó pai do elemento
childNodes[n]       // lista de filhos (n é o índice)
firstChild          // primeiro nó filho
lastChild           // último nó filho
nextSibling         // próximo nó irmão
previousSibling     // nó irmão anterior
*/
