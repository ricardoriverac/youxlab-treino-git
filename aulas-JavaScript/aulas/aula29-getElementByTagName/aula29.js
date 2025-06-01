const divC1 = document.getElementById('c1')
const divC2 = document.getElementById('c2')
const divC3 = document.getElementById('c3')
const divC4 = document.getElementById('c4')
const divC5 = document.getElementById('c5')
const divC6 = document.getElementById('c6')

const arrayElementos = [divC1, divC2, divC3, divC4, divC5, divC6]

//forma reduzida de tranformar um HTMLcollection em array
const colecaoHTML = [...document.getElementsByTagName('div')]

console.log(colecaoHTML)

colecaoHTML.map((elemeto)=>{
    console.log(elemeto)
})
