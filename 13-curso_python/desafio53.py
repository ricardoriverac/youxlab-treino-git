frase = (input('Escreva uma frase: ')).upper()
palavras = frase.split()
junto = ' '.join(frase)
inverso = junto[::-1]
if inverso ==junto :
    print('A frase {} é um palíndromo.'.format(frase))
else :
    print('A frase {} não é um palíndromo.'.format(frase))
