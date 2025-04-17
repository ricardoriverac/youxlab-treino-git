print(f'{" Banco":^40}')
valor = int(input('Qual o valor você gostaria de sacar hoje? R$: '))
total = valor
cedulas = 50
qntdCedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        qntdCedulas += 1
    else:
        print(f'Total de {qntdCedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        qntdCedulas = 0
        if total == 0:
            break
