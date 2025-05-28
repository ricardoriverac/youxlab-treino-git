num =int(input('escreva um número inteiro: '))
print(''' escolha uma das 3 opções:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opcao =int(input('sua opção '))
if opcao == 1:
    print('{} binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} seu número convertido para octal é {}' .format(num, oct (num) [2:]))
elif opcao == 3:
    print('{} sendo covertido para hexadecimal é {}' .format(num, hex (num) [2:]))
else:
    print('opção inválida. ')
