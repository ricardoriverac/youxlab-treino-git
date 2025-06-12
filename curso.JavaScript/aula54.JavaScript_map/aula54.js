const caixa = document.querySelector('#caixa')

let mapa = new Map()

mapa.set('livro', 'Era uma vez um coração partido')
mapa.set('ele', 'Jacks')
mapa.set('ela', 'evangeline')
mapa.delete('livro')



if (mapa.has('ela')){
    res = ('A chave está na coleção com o valor ' + mapa.get('ela'))
}else{
    res = ('A chave NÃO está na coleção')
}
caixa.innerHTML = res