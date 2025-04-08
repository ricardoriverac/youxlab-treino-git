#Convertendo para Base
numero=int(input('Digite um número inteiro: '))
print('Qual base você quer?\n'
'1-Binàrio\n'
'2-Octal\n'
'3-Hexadecimal\n')
opcao=int(input('Qual opção você deseja: '))
if opcao== 1:
    binario=bin(numero)
    print(f'{numero} convertido para Binário é: {binario}')
elif opcao== 2:
    octal=oct(numero)
    print(f'{numero} convertido para Octal é: {octal}')
elif opcao== 3:
    hexadecimal=hex(numero)
    print(f'{numero} convertido para Hexadecimal: {hexadecimal}')


