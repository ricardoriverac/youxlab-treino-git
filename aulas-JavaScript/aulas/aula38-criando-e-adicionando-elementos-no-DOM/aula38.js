const caixa1 = document.querySelector('#caixa1')
const curso = [...document.querySelectorAll('.curso')
]
const c1_2 = document.querySelector('#c1_2')
const cursos = ['HTML', 'CSS', 'Javascript', 'PHP', 'React', 'MySQL', 'ReactNative']

// forma dinamica
cursos.map((elemento, chave)=>{
    const novoElemento = document.createElement('div')
    novoElemento.setAttribute('id', 'c'+chave)
    novoElemento.setAttribute('class', 'curso c1')
    novoElemento.innerHTML=elemento
    caixa1.appendChild(novoElemento)
})

// criando de forma manual um por um
const novoElemento = document.createElement('div')
novoElemento.setAttribute('id', 'c7')
novoElemento.setAttribute('class', 'curso c1')
novoElemento.innerHTML='ReactNative'

caixa1.appendChild(novoElemento)