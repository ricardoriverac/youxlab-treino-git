from random import randint
from time import sleep
from operator import itemgetter

Jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranked = dict()

print('\033[33m=-=\033[m'*30,'\nValores sorteados:')

for jogador, valor in Jogo.items():
    print(f'O {jogador} tirou {valor} no DADO')
    sleep(1)
print('\033[33m=-=\033[m'*30)
ranked = sorted(Jogo.items(), key=itemgetter(1), reverse=True)

print('==========>>> Ranked dos Jogadores <<<==========')
for i, v in enumerate(ranked):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)    
print()






