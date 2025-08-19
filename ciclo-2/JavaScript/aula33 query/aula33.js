// seleciona todos os elementos <div> e os converte em um array
const divTodas = [...document.getElementsByTagName("div")]

// seleciona todos os elementos com a classe "curso" e os converte em um array
const cursosTodos = [...document.getElementsByClassName("curso")]

// seleciona todos os elementos com a classe "c1" e os converte em um array
const cursosC1 = [...document.getElementsByClassName("c1")]

// seleciona todos os elementos com a classe "c2" e os converte em um array
const cursosC2 = [...document.getElementsByClassName("c2")]

// seleciona o elemento com o id "c1"
const cursoEspecial = document.getElementById("c1")

// seleciona todos os elementos <p> que são filhos diretos de <div> e os converte em um array
// const query_divTodas = [...document.querySelectorAll("div[class]")]
const query_divTodas = [...document.querySelectorAll("div > p")] //query jseleciona o primeiro elemento que corresponde ao seletor CSS fornecido


// seleciona todos os elementos com a classe "curso" e os converte em um array
const query_cursosTodos = [...document.querySelectorAll(".curso")]

// seleciona todos os elementos com a classe "c1" ou <p> e os converte em um array
const query_cursosC1 = [...document.querySelectorAll(".c1, p")]

// seleciona todos os elementos com a classe "c2" e os converte em um array
const query_cursosC2 = [...document.querySelectorAll(".c2")]

// seleciona todos os elementos com o id "c1" e os converte em um array
const query_cursoEspecial = document.querySelectorAll("#c1")

// exibe no console os elementos selecionados com a consulta "div > p"
console.log(query_divTodas)


// console.log(divTodas)
// console.log(cursosTodos)
// console.log(cursosC1)
// console.log(cursosC2)
// console.log(cursoEspecial)

// cursosC1.map((el)=>{
//     el.classList.add("destaque") // adiciona uma classe nesse elemento
// })