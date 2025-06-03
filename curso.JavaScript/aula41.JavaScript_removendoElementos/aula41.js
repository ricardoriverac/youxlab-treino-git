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

    const btn_lixeira = document.createElement('img')
    btn_lixeira.setAttribute('src', './icone_lixeira.png')
    btn_lixeira.setAttribute('class', 'lixeira')
    novoElemento.appendChild(btn_lixeira)
    
    btn_lixeira.addEventListener('click',(evt)=>{
        caixa1.removeChild(evt.target.parentNode)
    })
})

console.log()