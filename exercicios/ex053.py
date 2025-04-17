print('=====ANALISADOR DE PALÍNDROMO=====')
frase= str(input('Escreva uma frase: ')).strip().upper()
palavras= frase.split()
juntar= ''.join(palavras)
print('Você digitou a frase {}'.format(juntar))
inverso= ''
for letra in range(len(juntar - 1, -1, -1)):
    inverso += juntar[letra]
    print(juntar, inverso)
