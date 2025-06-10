const p_array = document.querySelector("#array")
const btnVerificar = document.querySelector("#btnVerificar")
const resultado = document.querySelector("#resultado")

const elementos_array = [21, 25, 19, 20, 18, 18, 22]
p_array.innerHTML = "[" + elementos_array + "]"

btnVerificar.addEventListener("click", (evt) => {
    const retorno = elementos_array.every((ele, ind) => { // O "every" compara todos os elementos e retorna um OK quando todos os elementos tiverem em conformidade com minha regra
        if(ele < 18){
            resultado.innerHTML = "Array não conforme na posição " + ind 
        }
        return ele >= 18
    })
    if(retorno){
        resultado.innerHTML = "OK"
    }
    console.log(retorno)
})
