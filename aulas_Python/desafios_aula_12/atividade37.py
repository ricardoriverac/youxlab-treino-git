print('-=-=-=-=-Conversor de Bases Numéricas-=-=-=-=-')
numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

binario = bin(numero)[2:]

octal = oct(numero)[2:]

hexa = hex(numero)[2:]

if opcao == 1: 
    print('O número {} em BINARIO é: {}'.format(numero, binario))
    
elif opcao == 2 :
    print('O número {} em OCTAL é: {}'.format(numero, octal))
    

elif opcao == 3 :
    print('O numero {} em HEXADECIMAL é: {}'.format(numero, hexa))

