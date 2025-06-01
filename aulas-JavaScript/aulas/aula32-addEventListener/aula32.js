// pega todas as divs
const cursos = [...document.querySelectorAll('.curso')]
cursos.map((elementos)=>{
    elementos.addEventListener('click', (evento)=>{
        const elementos = evento.target
        elementos.classList.add('destaque')
        console.log(`${elementos.innerHTML} foi clicado`)
    })
})

// pega só a primeira div
const c1 = document.querySelector('#c1')
c1.addEventListener('click', (evento)=>{
    alert('clicou')
    const elemento = evento.target
    elemento.classList.add('destaque')
})