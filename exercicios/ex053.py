print('=====ANALISADOR DE PALÍNDROMO=====')
frase= (input('Escreva uma frase: ')).strip().upper()
palavras= frase.split()
juntar= ''.join(palavras)
print('Você digitou a frase {}'.format(juntar))
inverso= ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
if inverso == juntar:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')