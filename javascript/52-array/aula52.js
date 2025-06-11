const caixa = document.querySelector("#caixa")

let cores = ["azul", "verde", "vermelho", ["claro", "escuro", "médio"]]
let cursos = ["HTML", "CSS", "JavaScript", cores]

// cursos[0] = "C++" // Altera o valor da posição 0

cursos.push("Python") // Cria um novo elemento no array
cursos.pop() // Pega o último elemento do array e remove
cursos.unshift("Python") // Cria um elemento no topo do array
cursos.shift() // Tira o primeiro elemento do array

console.log(cursos[0])
console.log(cursos [3][3][2])

cursos.map((el) => {
    let p = document.createElement("p")
    p.innerHTML = el
    caixa.appendChild(p)
})
