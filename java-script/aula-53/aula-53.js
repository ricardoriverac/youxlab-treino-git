const btn_soma = document.querySelector("#btn_soma")
const btn_subtracao = document.querySelector("#btn_subtracao")
const btn_multiplicacao = document.querySelector("#btn_multiplicacao")
const btn_divisao = document.querySelector("#btn_divisao")
const res = document.querySelector("#res")
const btn_limpar = document.querySelector("#btn_limpar")
const historico = document.querySelector("#historico")

function adicionarHistorico(operacao, valor1, valor2, resultado) {
    const item = document.createElement("li")
    item.textContent = `${valor1} ${operacao} ${valor2} = ${resultado}`
    historico.appendChild(item)
}

const op = [
    () => {
        const val = [Number(document.getElementById("valor1").value), Number(document.getElementById("valor2").value)]
        const resultado = val[0] + val[1]
        res.value = resultado
        adicionarHistorico("+", val[0], val[1], resultado)
    },
    () => {
        const val = [Number(document.getElementById("valor1").value), Number(document.getElementById("valor2").value)]
        const resultado = val[0] - val[1]
        res.value = resultado
        adicionarHistorico("-", val[0], val[1], resultado)
    },
    () => {
        const val = [Number(document.getElementById("valor1").value), Number(document.getElementById("valor2").value)]
        const resultado = val[0] * val[1]
        res.value = resultado
        adicionarHistorico("×", val[0], val[1], resultado)
    },
    () => {
        const val = [Number(document.getElementById("valor1").value), Number(document.getElementById("valor2").value)]
        const resultado = val[0] / val[1]
        res.value = resultado
        adicionarHistorico("÷", val[0], val[1], resultado)
    }
]

btn_soma.addEventListener("click", op[0])
btn_subtracao.addEventListener("click", op[1])
btn_multiplicacao.addEventListener("click", op[2])
btn_divisao.addEventListener("click", op[3])

btn_limpar.addEventListener("click", () => {
    valor1.value = ""
    valor2.value = ""
    res.value = ""
})
