const caixa1 = document.querySelector('#caixa1')
const caixa2 = document.querySelector('#caixa2')
const botao = document.querySelector('#btn_copiar')
const todosCursos = [...document.querySelectorAll('.curso')]

todosCursos.map((elemento)=>{
    elemento.addEventListener('click', (evento)=>{
        const curso = evento.target
        curso.classList.toggle('selecionado')
    })
})

botao.addEventListener('click', ()=>{
    const cursosSelecionados = [...document.querySelectorAll('.selecionado')]
    cursosSelecionados.map((elemento)=>{
        caixa2.appendChild(elemento)
    })
})