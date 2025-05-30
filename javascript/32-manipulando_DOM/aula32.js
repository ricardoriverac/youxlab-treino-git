const cursosTodos = [...document.getElementsByClassName("curso")]
const cursosC1 = [...document.getElementsByClassName("c1")]
const cursosC2 = [...document.getElementsByClassName("c2")]
const cursoEspecial = document.getElementsByClassName("curso")[6]
// getElementByClassName é uma função que retorna uma coleção de elementos HTML como mesmo nome de classe

console.log(cursosTodos)
console.log(cursosC1)
console.log(cursosC2)

cursosC1.map((el)=>{
    el.classList.add("destaque") // Adiciona uma classe nesse elemento
})
