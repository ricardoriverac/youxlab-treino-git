entrada = str(input('Digite uma frase: ')).upper().replace(" ", '')
total = len(entrada)
resultado = ''
for c in range(total, 0, -1):
    resultado += entrada[c - 1]
print(f'O inverso de {entrada} é {resultado}')

if resultado == entrada:
    print('Sua frase é um palíndromo !')
else:
    print('Sua frase não é um palíndromo')