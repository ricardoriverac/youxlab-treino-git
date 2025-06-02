const caixa1 =  document.querySelector("#caixa1")
const caixa2 =  document.querySelector("#caixa2")
const btn =  document.querySelector("#btn_transferir")
const todosCursos = [...document.querySelectorAll(".curso")]

todosCursos.map((el) =>{
    el.addEventListener("click", (evt) => {
        const curso = evt.target
        console.log(curso)
        curso.classList.toggle("selecionado") // Se o elemenro tiver a classe selecionado, ele remove, se não tiver ele adiciona
    })
})

btn.addEventListener("click", () =>{
    const cursosSelecionados = [...document.querySelectorAll(".selecionado")]
    const cursosNaoSelecionados = [...document.querySelectorAll(".curso:not(.selecionado)")]
    cursosSelecionados.map((el) => {
        caixa2.appendChild(el)
    cursosNaoSelecionados.map((el) => {
        caixa1.appendChild(el)
    })
})
})
