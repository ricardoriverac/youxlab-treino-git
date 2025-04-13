from random import randint
numero = (randint(1, 10)),(randint(1, 10)),(randint(1, 10)),(randint(1, 10)),(randint(1, 10)),
print('OS valores sorteados foram:', end=' ')
for n in numero:
    print(f'{n}', end=' ')
print(f'\nO maior valor foi {max(numero)}')
print(f'O menor valor foi {min(numero)}')