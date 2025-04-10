palavras=('pedra', 'janela', 'livro', 'carro', 'rio' ,'tempo', 'casa', 'flor', 'papel', 'sapato')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end =' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end = ' ')

