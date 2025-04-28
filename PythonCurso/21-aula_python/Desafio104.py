def leiaInt(frase):
    print('-'*35)
    while True:
        num = str(input(frase)).strip()
        if num[0].isnumeric() or num[1].isnumeric():
            return int(num)
        else:
            print('! Digite um valor inteiro válido.')


n = leiaInt('Digite um número: ')
print(f'Você digitou o valor {n}.')