const divTodas = [...document.getElementsByTagName('div')]
const cursosTodos = [...document.getElementsByClassName('curso')]
const cursosC1 = [...document.getElementsByClassName('c1')]
const cursosC2 = [...document.getElementsByClassName('c2')]
const cursoEspecial = document.getElementById('c1')

console.log(divTodas)
console.log(cursosTodos)
console.log(cursosC1)
console.log(cursosC2)
console.log(cursoEspecial)

// usando query
const query_divTodas = document.querySelector('div') // pega só a primeira div que ele achar
const query_divTodasAll = [...document.querySelectorAll('div[class]')] // pega todas as divs e so as divs q tem class
const query_divTodasAllTagP = [...document.querySelectorAll('div > p')] // pega as divs q recebem o p
const query_cursosTodos = [...document.querySelectorAll('.curso')]
const query_cursosC1 = [...document.querySelectorAll('.c1')]
const query_cursosC2 = [...document.querySelectorAll('.c2')]
const query_cursoEspecial = document.querySelector('#c1')

console.log(query_divTodasAll)
console.log(query_divTodasAllTagP)
console.log(query_divTodas)
console.log(query_cursosTodos)
console.log(query_cursosC1)
console.log(query_cursosC2)
console.log(query_cursoEspecial)