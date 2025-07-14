// EVENTOS - addEventListener --> reage a ações do usuário

// SINTAXE: elemento.addEventListener("tipo de evento", função a executar)

// const c1 = document.getElementById("c1") // Seleciona a div com id="c1"

// function mensagem() {
//     alert('Clicou!')
// }

// Forma 1: chama uma função já existente ao clicar
// c1.addEventListener("click", mensagem)

// Forma 2: usa uma função anônima (arrow function)
// c1.addEventListener("click", () => {
//     mensagem() // Também é possível chamar a função aqui

//     // Ou executar um comando diretamente:
//     // alert("Clicou!")
// })

// Acessa o elemento que disparou o evento
// c1.addEventListener("click", (evento) => {
//     console.log(evento.target)
// })

// Adiciona a classe 'destaque' ao clicar na div c1
// c1.addEventListener("click", (evento) => {
//     const elemento = evento.target
//     elemento.classList.add("destaque")
// })



// Destaca todas as divs com a classe 'curso' ao clicar
const cursos = [...document.querySelectorAll(".curso")] // Seleciona todas as divs com a classe 'cursos'

cursos.map((elemento) => {  // Para cada div do array
    elemento.addEventListener("click", (evento) => {  // Adiciona evento de clique
        const elemento = evento.target  // Pega o elemento que foi clicado
        elemento.classList.add("destaque")  // Adiciona a classe 'destaque' ao elemento clicado
        console.log(elemento.id+" foi clicado")
        console.log(elemento.innerHTML+" foi clicado")
    })
})



