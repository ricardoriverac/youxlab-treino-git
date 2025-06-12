const caixa = document.querySelector('#caixa')

let mapa = new Map()

// adicionando um elemento na coleção
mapa.set('curso', 'Javascript')
mapa.set(10, 'CFB Cursos')
mapa.set(1, 100)
mapa.set('canal',100)

// deletando um elemento
mapa.delete(1) // pega pela chave tbm

console.log(mapa)

// verificando se a chave existe na coleção
let pesquisa = 10
let resultado = ''

if (mapa.has(pesquisa)){ // has pesquisa pela chave
    resultado = `A chave existe na coleção com o valor: ${mapa.get(pesquisa)}` // pega um elemento
}else{
    resultado = 'A chave NÃO está na coleção'
}

resultado += `<br/> O tamanho da coleção é ${mapa.size}` // mostra o tamanho
caixa.innerHTML = resultado

mapa.forEach((elemento)=>{
    console.log(elemento)
})