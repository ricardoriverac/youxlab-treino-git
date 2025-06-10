const p_array = document.querySelector('#array')
const botaoReduzir = document.querySelector('#botaoReduzir')
const resultado = document.querySelector('#resultado')

const botaoAdicionar = document.querySelector('#botaoAdicionar')

let elementosArray = []

let ant = []
let atu = []
let dobro = []

const adicionarNumeros = (evento)=>{
    const input = document.querySelector('#numerosArray')
    const valorInput = Number(input.value)
    elementosArray.push(valorInput)
    console.log(elementosArray)
    p_array.innerHTML = `[ ${elementosArray} ]`
}

botaoReduzir.addEventListener('click',(evento)=>{
    dobro.push(elementosArray[0]*2)
    resultado.innerHTML=elementosArray.reduce((anterior,atual,posicao)=>{

        ant.push(anterior)
        atu.push(atual)
        dobro.push(atual*2)

        return atual+anterior
    })
    resultado.innerHTML+=`<br/>V.anterior: ${ant} <br/>V.atual: ${atu} <br/>Dobro: ${dobro}`
})

// reduce permite operar os elementos do array e obter resultados com eles