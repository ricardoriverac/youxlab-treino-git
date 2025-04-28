lista=( 'Bolo' , 1.50,
        'Café' , 90.0,
        'Doce' , 0.50,
        'Coca' , 8.0,
        'Wisky' , 0.1,
        'pepsi' , 98.0,
        'Seabra' , 0.0)
print('__' *12)
print('|LISTAGEM|DOS|PRODUTOS|')
print('¨' *24)
for pos in  range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end ='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-' * 41)