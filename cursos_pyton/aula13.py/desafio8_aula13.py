frase = str(input('Digite uma palavra: ')).upper()
frase = ''.join(frase.split(' '))
print('A palavra {} ao contrário é {} logo, ela  '.format(frase, frase[::-1]), end='')
if frase == frase[::-1]:
    print('é um palíndromo.' .format(frase))
else:
    print('não é um palíndromo.' .format(frase))