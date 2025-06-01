const caixa1 = document.querySelector('#caixa1')
const divC1 = document.querySelector('#c1')
const cursos = [...document.querySelectorAll('.curso')]

caixa1.addEventListener('click', (evento)=>{
    console.log(evento)
    console.log('clicou')

})

cursos.map((elemento)=>{
    elemento.addEventListener('click', (evento)=>{
        evento.stopPropagation()
    })
})