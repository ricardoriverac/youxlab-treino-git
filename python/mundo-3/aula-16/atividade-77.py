palavras = ('python', 'programacao', 'computador', 'desenvolvimento', 'inteligencia', 'artificial', 'chatgpt')

for palavra in palavras:
    print(f'\nNa palavra "{palavra.upper()}" temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
