const elementos = document.getElementsByTagName('div')  // Pegando todos os 'divs' do HTML

let valores = [10, 20, 30, 40]  // Uma lista

// FOR IN, percorrendo os índices dos elementos dentro do 'elementos'
for (indice in elementos) {
    console.log(elementos[indice].innerHTML) // Mostra o conteúdo dentro dos divs, usando a posição do índice
}

// FOR OF, pqrq percorrer diretamente os elementos da coleção
for (elemento of elementos) { 
    console.log(elemento.innerHTML = 'Curso') // Troca o conteúdo de cada div para "Curso"
}

// Outra forma de usar o FOR:
for (let i = 0; i < valores.length; i++) {
    console.log(i) // Imprime a posição do índice
    console.log(valores[i]) // Imprime o valor na posição
}
