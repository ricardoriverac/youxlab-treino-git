def leiaInt():
    while True:
        valor = input('Digite um número inteiro: ')
        if valor.isnumeric():
            valor = int(valor)
            print(f'{valor} é um número!')
            return valor
        else:
            print(f'Ocorreu um erro. "{valor.upper()}" não é um número!')

num = leiaInt()
print(f'Você digitou: {num}')