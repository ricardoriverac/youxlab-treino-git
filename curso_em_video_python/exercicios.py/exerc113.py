def leiaFloat():
    while True:
        try:
            valor = input('Digite um número inteiro: ')
        except:
            print('Algo deu errado.')
        if valor.isnumeric():
            valor = int(valor)
            print(f'{valor} é um número inteiro!')
            return valor
        else:
            print(f'Ocorreu um erro. "{valor.upper()}" não é um número!')


num = leiaFloat()
print(f'Você digitou: {num}')