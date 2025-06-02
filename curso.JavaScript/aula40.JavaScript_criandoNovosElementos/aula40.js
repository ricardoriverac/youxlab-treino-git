const caixa1 = document.querySelector('#caixa1')
const btn_c= [...document.querySelectorAll('.curso')]
const c1_22 = document.querySelector('#c1_2')
const cursos = ['PHP', 'JavaScript', 'Python', 'Frontend', 'CSS', 'React']

cursos.map((el, chave)=>{
    const novoElemento = document.createElement('div')
    caixa1.appendChild(novoElemento)
    novoElemento.setAttribute('id', 'c' + chave)
    novoElemento.setAttribute('class', 'curso c1')
    novoElemento.innerHTML = el
})

const novoElemento = document.createElement('div')
caixa1.appendChild(novoElemento)

novoElemento.setAttribute('id', 'c7')
novoElemento.setAttribute('class', 'curso c1')
novoElemento.innerHTML = 'React'

console.log()