// ITERADORES

// *done--> a forma que a função utiliza para saber se chegou no final da coleção ou não

const valores=[10,8,9,2]

const iteradorValores=valores[Symbol.iterator]()
console.log(valores)

console.log(iteradorValores.next().value)

console.log("\n")



//Com string
const texto="Hello World!" 
const iteradorTexto=texto[Symbol.iterator]()
console.log(texto)

console.log(iteradorTexto.next()) //retor:(1° VALOR DO ARRAY), done: (false--> ñ chegou no final) }
console.log(iteradorTexto.next())
console.log(iteradorTexto.next()) //Já mostra os valores não mostrados automaticamente
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())
console.log(iteradorTexto.next())