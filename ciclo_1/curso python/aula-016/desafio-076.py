
# produtos = ['Notebook', 1250.00', 'Caneta', 6.6, 'Caderno', 25.0, 'Carro', 200.000.00]
lista = ['Notebook', 1250.00, 'Carro de brinquedo', 300.0, 'Caneta', 5.0]
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end= '')
        # print(f'{lista[item]}')
    if item % 2 == 1:
        # print(f'{lista[item]:.>30}')
        print(f'{lista[item]:.>7}')