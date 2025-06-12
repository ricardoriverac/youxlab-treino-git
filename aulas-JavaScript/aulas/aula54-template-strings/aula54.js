const caixa = document.querySelector('#caixa')
const curso = 'Javascript'
const canal = 'CFB Cursos'
const frase = `Este é o<br/> curso de ${curso} do<br/> canal ${canal}`

caixa.innerHTML = frase


const caixa2 = document.querySelector('#caixa2')
const carros = ['Polo', 'Golf', 'T-Cross', 'HRV']

let ul = `<ul>`
carros.map((elemento)=>{
    ul += `<li>${elemento}</li>`
})
ul + `</ul>`

caixa2.innerHTML = ul