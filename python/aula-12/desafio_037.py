print('Digite uma numeração para escolher a conversão.')
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')

# Solicitar um número para o usuário
num = int(input('Digite o número para conversão: '))

conversao = int(input('Escolha a opção desejada: '))

if conversao == 1:
    binario = format(num, 'b')
    print(f'Número em binário: {binario}')
elif conversao == 2:
    octal = format(num, 'o')
    print(f'Número em octal: {octal}')
elif conversao == 3:
    hexadecimal = format(num, 'x')
    print(f'Número em hexadecimal: {hexadecimal.upper()}')
else:
    print('\033[1:31mVocê não digitou nenhuma das opções válidas!\033[m')
