def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)

        else:
            print('\033[31mERRO! Digite um número inteiro!\033[m ')

num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')






def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print('ERRO! Digite um número inteiro! ')
        
        
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')
