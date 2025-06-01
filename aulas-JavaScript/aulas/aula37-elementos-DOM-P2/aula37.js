const caixa1 = document.querySelector('#caixa1')
const curso = [...document.querySelectorAll('.curso')
]
const c1_2 = document.querySelector('#c1_2')

console.log(c1_2.parentNode.parentNode) // mostra o avô
console.log(c1_2.parentNode.parentNode.children[3]) // pega um filho especifico

console.log(caixa1.hasChildNodes()) // ve se tem filho
console.log(curso[0].hasChildNodes())
console.log(curso[0].childNodes)

// verificando com IF
if (curso[0].children.length > 0){
    console.log('Possui filhos')
}else{
    console.log('NÃO possui filhos')
}

// verificando com condição ternaria
console.log(caixa1.children.length > 0 ? 'Possui filhos' : 'NÃO possui filhos')

// mudando o primeiro
console.log(caixa1.firstElementChild.innerHTML='TESTE')

// mudando o que eu escolher
console.log(caixa1.children[1].innerHTML='TESTE')