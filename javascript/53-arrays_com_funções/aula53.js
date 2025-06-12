const btn_soma = document.querySelector("#btn_soma")
const btn_subtracao = document.querySelector("#btn_subtracao")
const btn_multiplicacao = document.querySelector("#btn_multiplicacao")
const btn_divisao = document.querySelector("#btn_divisao")
const resultado = document.querySelector("#res")
const btn_resetar = document.querySelector("#btn_resetar")
const res = document.querySelector("#resultados")
const btn_apagar = document.querySelector("#btn_apagar")

const op = [
    () => {
        const val = [document.getElementById("valor1").value, document.getElementById("valor2").value]
        resultado.value = Number(val[0])+Number(val[1])
        const resSoma = resultado.value = Number(val[0])+Number(val[1])
        res.innerHTML += ` </p> ${Number(val[0])} + ${Number(val[1])} = ${resSoma}`
    },
    () => {
        const val = [document.getElementById("valor1").value, document.getElementById("valor2").value]
        resultado.value = Number(val[0])-Number(val[1])
        const resSub = resultado.value = Number(val[0])-Number(val[1])
        res.innerHTML += ` </p> ${Number(val[0])} - ${Number(val[1])} = ${resSub}`
    },
    () => {
        const val = [document.getElementById("valor1").value, document.getElementById("valor2").value]
        resultado.value = Number(val[0])*Number(val[1])
        const resMultiplicacao = resultado.value = Number(val[0])*Number(val[1])
        res.innerHTML += ` </p> ${Number(val[0])} x ${Number(val[1])} = ${resMultiplicacao}`
    },
    () => {
        const val = [document.getElementById("valor1").value, document.getElementById("valor2").value]
        resultado.value = Number(val[0])/Number(val[1])
        const resDiv = resultado.value = Number(val[0])/Number(val[1])
        res.innerHTML += ` </p> ${Number(val[0])} / ${Number(val[1])} = ${resDiv}`
    },
    () => {
        document.getElementById("valor1").value = "" 
        document.getElementById("valor2").value = ""
        resultado.value = ""
    },
    () => {
        res.innerHTML = ""
    }
]

btn_soma.addEventListener("click", op[0])
btn_subtracao.addEventListener("click", op[1])
btn_multiplicacao.addEventListener("click", op[2])
btn_divisao.addEventListener("click", op[3])
btn_resetar.addEventListener("click", op[4])

// let valores = [1, 2, 3, 4, 5]
// const op = [
//     (val) =>{
//         let res = 0
//         for(v of val){
//             res += v
//         }
//         return res
//     },
//     (val) => {
//         let res = 1
//         for(v of val){
//             res *= v
//         }
//         return res
//     },
//     (val) =>{
//         for(v of val){
//             console.log(v)
//         }
//     }
// ]

// console.log(op[1](valores))
