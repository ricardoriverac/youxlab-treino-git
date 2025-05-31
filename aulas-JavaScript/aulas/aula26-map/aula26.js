const cursos = ['HTML', 'CSS', 'Javascript', 'PHP', 'React']

// usar o map pra percorrer a coleção toda sem interrupção
cursos.map((elemento, i)=>{  // pra executar alguma coisa dentro do map tem q ter =>
    console.log(`Curso: ${elemento} - Posição do curso: ${i}`)
})

// usando return
let c = cursos.map((elementos, i)=>{
    return '<div>' + elementos + '</div>'
})

console.log(c)

// alterando no browser
let elemento = document.getElementsByTagName('div')

elemento = [...elemento]

console.log(elemento)

elemento.map((e, i)=>{
    e.innerHTML='Youx Lab'
    console.log(e.innerHTML)
})

// mostrando os valores
const elemento2 = document.getElementsByTagName('div')
const valores = Array.prototype.map.call(elemento2,({innerHTML})=>innerHTML)
console.log(valores)

// fazendo operações
const converterInt = (elemento) => parseInt(elemento)
let numero = ['1', '2', '3', '4', '5'].map(converterInt)
console.log(numero)

const dobrar = (elemento) => elemento*2
let numero2 = ['1', '2', '3', '4', '5'].map(dobrar)
console.log(numero2)