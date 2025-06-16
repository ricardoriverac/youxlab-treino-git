const caixa = document.querySelector('#caixa')

const curso = 'JavaScript'
const canal = 'CFB cursos'

const carros = ['BMW', 'Audi', 'Volkswagen', 'Chevrolet']

let ol = '<ol>'
carros.map((el)=>{
    ol+= `<li> ${el}</li>`
})
ol + '</ol>'




// const frase = 'Este é o curso de ' + curso + ' do canal ' + canal
const frase = `Este é o curso de ${curso} do canal ${canal}`

caixa.innerHTML = ol