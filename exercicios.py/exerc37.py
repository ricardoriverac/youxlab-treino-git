from time import sleep
numero = int(input('Escolha um número: '))
binario = bin(numero) [2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]
print ('Escolha a base que você quer converter:')
print('[1] Binário')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input('Qual das opçoẽs? '))
print('CONVERTENDO...')
sleep(2)
if opcao == 1:
    print('O número {} em binário é:\033[1;35m{}.'.format(numero, binario))
elif opcao == 2:
    print ('O número {} em octal é:\033[1;35m{}.'.format(numero, octal ))
elif opcao == 3:
    print('O número {} em hexadecimal é\033[1;35m{}.'.format(numero, hexadecimal))
else :
    print('Eu te dei três opçoẽs, faça o favor de escolher certo!')