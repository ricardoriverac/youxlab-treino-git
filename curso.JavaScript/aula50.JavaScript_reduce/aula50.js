const p_array = document.querySelector('#array')
const btnReduzir = document.querySelector('#btnReduzir')
const resultado = document.querySelector('#resultado')

const elementos = [1, 2, 3, 4, 5]
let ant = []
let atu = []
let dobro = []

p_array.innerHTML = elementos

btnReduzir.addEventListener('click', (evt)=>{
    resultado.innerHTML = elementos.reduce((anterior, atual, pos)=>{
        ant.push(anterior)
        atu.push(atual)
        dobro.push(atual*2)
        return atual + anterior
    })
    resultado.innerHTML += '<br/> Valor anterior: '+ant+'<br/> Valor atual: '+ atu + '<br/> Dobro:' + dobro
})