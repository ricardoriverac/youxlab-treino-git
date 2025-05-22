entrada = str(input('Digite uma frase: ')).upper().replace(" ", '')
total = len(entrada)
resul = ''
for c in range(total, 0, -1):
    resul += entrada[c - 1]
print('O inverso de {} é {}'.format(entrada, resul))

if resul == entrada:
    print('Sua frase é considerada um palíndromo !')
else:
    print('Sua frase NÃO é considerada um palíndromo')
