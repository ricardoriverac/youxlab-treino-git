const caixa = document.querySelector('#caixa')

let musicas = new Set(['musica1', 'musica boa', 'musica10'])

// adicionando elementos (não duplica chave)
musicas.add('musica muito legal')
musicas.add('musica1')
musicas.add('musica10')

// deletando um elemento
musicas.delete('musica1')

// limpando a coleção por completo
musicas.clear()

console.log(musicas)

musicas.forEach((elemento)=>{
    caixa.innerHTML += `${elemento} <br/>`
})