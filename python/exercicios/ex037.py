numero= int(input('Digite um número: '))
print('1 para binário \n 2 para octal \n 3 para hexadecimal')
conversao= int(input('Escolha uma base de conversão: '))

if conversao == 1:
    binario= bin(numero)
    print('O número {} convertido em binário é: {}'.format(numero, binario))
elif conversao == 2:
    octal= oct(numero)
    print('O número {} convertido em octal é: {}'.format(numero, octal))
elif conversao == 3:
    hexadecimal= hex(numero)
    print('O número {} convertido em hexadecimal é: {}'.format(numero, hexadecimal))