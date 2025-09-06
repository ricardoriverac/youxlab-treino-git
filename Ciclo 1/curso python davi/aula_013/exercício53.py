fr = input('escreva uma frase ').upper()
if fr == fr[::-1]:
    print('é um palíndromo')
else:
    print('não é um palíndromo')