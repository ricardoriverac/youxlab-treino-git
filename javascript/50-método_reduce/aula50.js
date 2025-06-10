const p_array = document.querySelector("#array")
const btnReduzir = document.querySelector("#btnReduzir")
const resultado = document.querySelector("#resultado")

const elementos_array = [1, 2, 3, 4, 5]
let ant = []
let atu = []
let dobro = []

p_array.innerHTML = "[" + elementos_array + "]"

btnReduzir.addEventListener("click", (evt) => {
    dobro.push(elementos_array[0] * 2)
    resultado.innerHTML = elementos_array.reduce((anterior, atual, posição) => { // O método "reduce" permite operar todos os elementos do array e obter um resultado com esses elementos
        ant.push(anterior)
        atu.push(atual)
        dobro.push(atual*2)
        return atual + anterior
    })
    resultado.innerHTML += "<br/>Valor anterior: " + ant + "<br/>Valor atual: " + atu + "<br/>Dobro: " + dobro
})
