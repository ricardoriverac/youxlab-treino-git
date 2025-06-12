const caixa = document.querySelector('#caixa')

let musicas = new Set(['Seu astral', 'Duas metades', 'Yeshua', 'Paredes'])
musicas.add('Flor')
musicas.add('De tanto te querer')
musicas.add('Te vivo')

console.log(musicas)

musicas.forEach((el)=>{
    caixa.innerHTML+= el + '</br>'
})