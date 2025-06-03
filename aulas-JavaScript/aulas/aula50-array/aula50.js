const caixa = document.querySelector('#caixa')
let cursos = ['HTML', 'CSS', 'Javascript']

//cursos[0] = 'C++'

cursos.push

console.log(cursos[0])

cursos.map((elemento)=>{
    let p = document.createElement('p')
    p.innerHTML = elemento
    caixa.appendChild(p)
})