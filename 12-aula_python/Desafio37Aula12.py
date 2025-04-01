numero = int(input('Digite um número: '))
print('''Escolha uma das bases para conersão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')

opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero) ))

