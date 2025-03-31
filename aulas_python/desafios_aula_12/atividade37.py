print('-=-=-=-=-Conversor de Bases Numéricas-=-=-=-=-')
numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

binario = bin(numero)[2:]
print(binario)