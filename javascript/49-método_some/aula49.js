const p_array = document.querySelector("#array")
const btnVerificar = document.querySelector("#btnVerificar")
const resultado = document.querySelector("#resultado")

const elementos_array = [10, 12, 10, 17, 15, 13, 11, 19]
p_array.innerHTML = "[" + elementos_array + "]"

btnVerificar.addEventListener("click", (evt) => {
    const retorno = elementos_array.some((ele, ind) => { // O "some" compara todos os elementos e retorna um OK se pelo meno UM desses elementos tiverem em conformidade com minha regra
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
