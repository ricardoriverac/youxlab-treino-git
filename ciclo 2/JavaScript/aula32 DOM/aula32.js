// pega todos os elementos com a classe "curso"
const cursosTodos = [...document.getElementsByClassName("curso")]

// pega elementos com a classe "c1"
const cursosC1 = [...document.getElementsByClassName("c1")]

// pega elementos com a classe "c2"
const cursosC2 = [...document.getElementsByClassName("c2")]

// pega o 7º elemento com classe "curso"
const cursoEspecial = document.getElementsByClassName("curso")[6]

// mostra no console os arrays de cursos
console.log(cursosTodos)
console.log(cursosC1)
console.log(cursosC2)

// adiciona a classe "destaque" em cada elemento com classe "c1"
cursosC1.map((el) => {
    el.classList.add("destaque")
})
