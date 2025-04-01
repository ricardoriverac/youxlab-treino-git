num=int(input('Me fale um número inteiro qualquer '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao=int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido em binário é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
