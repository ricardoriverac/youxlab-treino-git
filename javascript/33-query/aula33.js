const divTodas = [...document.getElementsByTagName("div")]
const cursosTodos = [...document.getElementsByClassName("curso")]
const cursosC1 = [...document.getElementsByClassName("c1")]
const cursosC2 = [...document.getElementsByClassName("c2")]
const cursoEspecial = document.getElementById("c1")
// getElementByClassName é uma função que retorna uma coleção de elementos HTML como mesmo nome de classe

// const query_divTodas = [...document.querySelectorAll("div[class]")]
const query_divTodas = [...document.querySelectorAll("div > p")]
const query_cursosTodos = [...document.querySelectorAll(".curso")]
const query_cursosC1 = [...document.querySelectorAll(".c1, p")]
const query_cursosC2 = [...document.querySelectorAll(".c2")]
const query_cursoEspecial = document.querySelectorAll("#c1") // # = ID

// QuerySelector() seleciona um único elemento da árvore DOM, com base em um seletor CSS e seleciona o primeiro elemento que corresponde ao seletor
// QuerySelectorAll() seleciona todos os elementos de um documento que correspondem a um seletor CSS especificado
//  Retorna todos os elementos que tem a classe "cursos"

console.log(query_divTodas)


// console.log(divTodas)
// console.log(cursosTodos)
// console.log(cursosC1)
// console.log(cursosC2)
// console.log(cursoEspecial)

// cursosC1.map((el)=>{
//     el.classList.add("destaque") // Adiciona uma classe nesse elemento
// })
