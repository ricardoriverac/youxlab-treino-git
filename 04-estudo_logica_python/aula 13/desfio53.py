frase=str(input(' Digite uma palavra :')).upper().split()
print('a palavra {} ao contrario é {} '.format(frase, frase[::-1]), end='')
if frase == frase[::-1]:
    print(' É uma POLÍNDROMO'.format(frase))
else:
    print('Nao é uma POLÍDROMO'.format(frase))    
