from random import randint
from time import sleep
from operator import itemgetter 
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6), 
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = []

print('-='*20)
print('{:^40}'.format('\033[1;35mVALORES SORTEADOS:\033[m '))
print('-='*20)
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado')
        sleep(1)
        
print('-='*20)
print('{:^40}'.format('\033[1;34mRANKING DOS JOGADORES\033[m'))
print('-='*20)        
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
        print(f'Em {i+1}º lugar: {v[0]} com {v[1]}')
        sleep(1)
        