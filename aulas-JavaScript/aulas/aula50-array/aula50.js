const caixa = document.querySelector('#caixa')
let cores = ['azul', 'verde', 'vermelho', ['claro', 'escuro', 'médio']]
let cursos = ['HTML', 'CSS', 'Javascript',cores]

//cursos[0] = 'C++'

cursos.push

// adicionando elementos
cursos.push('C++')
cursos.unshift('Python') // adiciona no inicio do array

// apagando elementos
cursos.pop() // apaga o último item
cursos.shift() // apaga o primeiro item 

console.log(cursos[3][3][2]) // indice pra localizar um elemento dentro de um array q ta dentro de outro array

console.log(cursos[0])

cursos.map((elemento)=>{
    let paragrafo = document.createElement('p')
    paragrafo.innerHTML = elemento
    caixa.appendChild(paragrafo)
})