frase = str(input('Digite uma frase: '))
inverso = frase[::-1]
espaco = inverso.replace(' ','')
espacoFrase = frase.replace(' ','')
if espaco == espacoFrase:
    print ('Esta frase é um palíndromo! ')
else:
    print ('Esta frase não é um palíndromo. ')