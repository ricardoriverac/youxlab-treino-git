const caixa1 = document.querySelector('#caixa1')
const curso = [...document.querySelectorAll('.curso')
]
const c1_2 = document.querySelector('#c1_2')
const cursos = ['HTML', 'CSS', 'Javascript', 'PHP', 'React', 'MySQL', 'ReactNative']

cursos.map((elemento, chave)=>{
    const novoElemento = document.createElement('div')
    novoElemento.setAttribute('id', 'c'+chave)
    novoElemento.setAttribute('class', 'curso c1')
    novoElemento.innerHTML=elemento

    const botaoLixeira = document.createElement('img')
    botaoLixeira.setAttribute('src', './lixeira.png')
    botaoLixeira.setAttribute('class', 'btn_lixeira')
    botaoLixeira.addEventListener('click', (evento)=>{
        caixa1.removeChild(evento.target.parentNode)
    })

    novoElemento.appendChild(botaoLixeira)
    caixa1.appendChild(novoElemento)
})
