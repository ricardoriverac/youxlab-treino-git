numero= int(input('Digite um numero:'))
base= int(input('digite {1} para transformar esse numero em binario\n''Digite {2} para tranformar esse numemero em octal\n Digite {3} para transformar em um hexadecimsal\n'))
if base == 1:
    conversao= bin(numero)[2:]
    print('Binario: ', conversao)
elif base== 2:
    conversao= oct(numero)
    print('oct: ', conversao)
elif base ==3 :
    conversao= hex(numero)
    print('hex: ', conversao)
else :
    print('O seu numero é invalido')