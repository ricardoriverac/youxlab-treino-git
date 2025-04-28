from random import randint
from time import sleep
from operator import itemgetter
lista = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
print('VALORES SORTEADOS')
for k, v in lista.items():
    print(f'O {k}, tirou {v} no dado.')
    sleep(0.5)
print(f'--'*8, 'CAMPEÕES', '--'*8)
ganhador= sorted(lista.items(), reverse=True, key=itemgetter(1))
for k, v in enumerate(ganhador):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)