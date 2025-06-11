const caixa = document.querySelector('#caixa')

let nomes = ['Jotape', 'Brennuz', 'Barreto', 'Kroy']
let cursos = ['HTML', 'CSS', 'JavaScript', nomes]

cursos.push('C++')
cursos.unshift('Python')

cursos.map((elemento)=>{
    const paragrafo = document.createElement('p')
    paragrafo.innerHTML = elemento
    caixa.appendChild(paragrafo)
})