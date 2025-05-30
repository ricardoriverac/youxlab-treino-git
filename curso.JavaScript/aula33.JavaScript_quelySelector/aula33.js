const divsCursos = [...document.getElementsByTagName('div')]
const todosCursos = [...document.getElementsByClassName('curso')]
const cursosC1 = [...document.getElementsByClassName('c1')]
const cursosC2 = [...document.getElementsByClassName('c2')]
const cursoEspecial = document.getElementById('c1')

const query_divtodas =[...document.querySelectorAll('div')]
const query_todosCursos=[...document.querySelectorAll('.curso')]
const query_cursoc2 =[...document.querySelectorAll('c2')]
const query_cursoc1=[...document.querySelectorAll('c1')]

console.log(query_todosCursos)
console.log(divsCursos)
console.log(todosCursos)
console.log(cursosC1)
console.log(cursosC2)
console.log(cursoEspecial)

//cursosC2.map((el)=>{
   // el.classList.add('destaque')
//})