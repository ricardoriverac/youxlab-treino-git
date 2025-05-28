palavras = ('python', 'programacao', 'desenvolvedor', 'teclado', 'monitor', 'computador', 'internet', 'software')
vogais = 'aeiou'
for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}" temos as vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
