// pega a caixa1 da página (a div com id "caixa1")
const caixa1 = document.querySelector("#caixa1")

// pega TODOS os elementos que têm a classe "curso" e coloca numa lista
const btn_c = [...document.querySelectorAll(".curso")]

const c1_2 = document.querySelector("#c1_2")

console.log(c1_2.parentNode.parentNode.children[4])
//console.log(caixa1.hasChildNodes())
//console.log(btn_c[0].hasChildNodes())
//console.log(btn_c[0].childNodes)

//console.log(caixa1.children.length> 0 ? "Possui fiote" : "Nao tem fiote")

//console.log(caixa1.children[1].innerHTML="Teste")


//console.log(caixa1.firstElementChild)

//console.log(caixa1.firstChild)

//if(btn_c[0].children.length> 0){
  //  console.log("Possui fiote" : "Nao tem fiote")
//}else{
  //  console.log("Nao tem fiote")
//}

// mostra no console o PRIMEIRO item que tá dentro da caixa1
//console.log(caixa1.children[0])
//console.log(btn_c[0].getRootNode())
//console.log(btn_c[0].ownerDocument)

//console.log(caixa1.firstElementChild)
//console.log(caixa1.lastElementChild)

