// função arrow que soma dois valores (forma mais simples)
const soma = (v1, v2) => {
    return v1 + v2 // retorna a soma de v1 e v2
}

console.log(soma(10, 5)) 

// função que recebe um nome e retorna ele mesmo
const nome = n => {
    return n // só devolve o nome que foi passado
}

console.log(nome("alexia"))


// função que soma 10 ao valor passado
const add = n => n + 10 // quando só tem 1 linha, não precisa de chaves nem return

console.log(add(10)) 
