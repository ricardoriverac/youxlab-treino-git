// const cursos = ['HTML', 'CSS', 'Javascript', 'PHP', 'React']
// let c = cursos.map((el, indice)=>{ // MAP é o mais recomendado para percorrer valores
//     console.log("Curso: " + el + " -Posição do curso: " + indice)
//     return el
// })

// console.log(c)

// let el = document.getElementsByTagName("div")
// el = [...el]
// console.log(el)
// el.map((e, i) => {
//     e.innerHTML="Cursos  CFB"
//     console.log(e.innerHTML)
// })

// const el = document.getElementsByTagName("div") // Retorna uma coleção de todos os elementos <div> da página
// const val = Array.prototype.map.call(el,({innerHTML}) => innerHTML) // Estamos usando o método map do array em uma HTMLCollection, que não é um array, mas é "parecido"
// Usar .call() permite aplicar o .map() como se el fosse um array
// Para cada elemenyo do el ele extrai a propriedade innerHTML e retorna esse conteúdo
// console.log(val) 
// Val agora é um array contendo o conteúdo (innerHTML) de todas as <div> sa página

const converterInt = (e) => parseInt(e) // Criei uma função que converte uma string em um número inteiro
const dobrar = (e) => e * 2 // Crei uma função que dobra o valor recebido
let num = ['1', '2', '3', '4', '5'].map(dobrar) // Criei a lista e usei o map para percorrer a lista inteira e dobrar todos os números
console.log(num)
