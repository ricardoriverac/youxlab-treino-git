const caixa = document.querySelector("#caixa")

const carros = ["Polo", "Golf", "T-Cross", "HRV"]

let ol = `<ol>`

carros.map((el) => {
    ol += `<li>${el}</li>`
})
ol + `</ol>`

// const curso = "Javascript"
// const canal = "CFB Cursos"
// // const frase = "Este é o curso de " + curso + " do canal " + canal
// const frase = `Este é o curso de ${curso} do canal ${canal}` 
// // Pra quebrar linha na frase tem que usar <br/> pois está dentro do DOM

caixa.innerHTML = ol
