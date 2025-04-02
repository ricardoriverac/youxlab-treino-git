numero = int(input('Digite um valor: '))
print('[1] binário')
print('[2] octal')
print('[3] hexadecimal')
escolha = int(input('Qual opção você escolhe?: '))
binario = bin(numero) [2:] #esses '[2:] serve pra começar a resposta depois dos 2 primeiros números
octal = oct (numero) [2:]
hexadecimal = hex(numero) [2:]
if escolha == 1:
    print('O número que você escolheu convertido para {}BINÁRIO {}é {}'.format('\033[35m','\033[m', binario))
elif escolha == 2:
    print('O número que você escolheu convertido para {}OCTAL {}é {}'.format('\033[35m', '\033[m', octal))
elif escolha == 3:
    print('O número que você escolheu convertido para {}HEXADECIMAL {}é {}'.format('\033[35m', '\033[m', hexadecimal))
else:
    print('É pra você escolher umas das opções! Tente novamente!')
    