const caixa1 = document.querySelector('#caixa1')
const caixa2 = document.querySelector('#caixa2')
const botaoTransferir = document.querySelector('#btn_transferir')
const todosCursos = [...document.querySelectorAll('.curso')]

todosCursos.map((elemento)=>{
    elemento.addEventListener('click', (evento)=>{
        const curso = evento.target
        curso.classList.toggle('selecionado')
    })
})

botaoTransferir.addEventListener('click', ()=>{
    const cursosSelecionados = [...document.querySelectorAll('.selecionado')]
    const cursosNaoSelecionados = [...document.querySelectorAll('.curso:not(.selecionado')]
    cursosSelecionados.map((elemento)=>{
        caixa2.appendChild(elemento)
    })
    cursosNaoSelecionados.map((elemento)=>{
        caixa1.appendChild(elemento)
    })
})