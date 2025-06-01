const caixa1 = document.querySelector('#caixa1')
const curso = [...document.querySelectorAll('.curso')
]

// retorna todos os filhos ou so o da posicao q colocar
console.log(caixa1.children)

// retorna o primeiro filho
console.log(caixa1.firstElementChild)

// retorna o ultimo filho
console.log(caixa1.lastElementChild)

// retorma o nó raiz
console.log(document.getRootNode())
console.log(curso[0].ownerDocument) // é a msm coisa do de cima