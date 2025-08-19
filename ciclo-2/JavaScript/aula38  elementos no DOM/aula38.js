// pega a caixa1 da página (a div com id "caixa1")
const caixa1 = document.querySelector("#caixa1")

// pega TODOS os elementos que têm a classe "curso" e coloca numa lista
const btn_c = [...document.querySelectorAll(".curso")]

// mostra no console o PRIMEIRO item que tá dentro da caixa1
//console.log(caixa1.children[0])
console.log(btn_c[0].getRootNode())
console.log(btn_c[0].ownerDocument)

//console.log(caixa1.firstElementChild)
//console.log(caixa1.lastElementChild)

