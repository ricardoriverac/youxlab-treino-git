listagem = ('Lápis', 1.50, 
            'Caneta', 2.50, 
            'Borracha', 2.50, 
            'Lapiseira', 3.50, 
            'Caderno', 10.90, 
            'Mochila', 50.0, 
            'Lápis de cor', 7.90,
            'Corretivo', 7.50, 
            'Estojo', 15.90)
print ('-='*20)
print('{:^40}'.format('\033[1;35mLISTAGEM DE PREÇOS\033[m'))
# print(f'{"LISTAGEM DE PREÇO":^40}')
print ('-='*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='R$ ')
    if pos % 2 == 1:
        print(f'{listagem[pos]}')
print ('-='*20)
