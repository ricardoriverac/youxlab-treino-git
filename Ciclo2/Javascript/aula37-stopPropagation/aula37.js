//stopPropagation--> Para a propagação de uma elemento

// Seleciona a div com id "caixa1"
const caixa1 = document.querySelector('#caixa1')

// Seleciona todos os elementos com a classe "curso"
const cursos = [...document.querySelectorAll('.curso')]

// Adiciona evento de clique na div "caixa1"
caixa1.addEventListener("click", (evento) => { 
    console.log(evento.target) // Mostra o elemento que disparou o evento
    console.log('Clicou na caixa1!')
})

//IMPEDINDO QUE OS ELEMENTOS POSSAM SER CLICADOS:
// Adiciona evento de clique em cada elemento com a classe "c1"
cursos.map((elemento) => {
    elemento.addEventListener("click", (evento) => { 
        evento.stopPropagation() // Impede que o clique se propague para a caixa1
    })
})
