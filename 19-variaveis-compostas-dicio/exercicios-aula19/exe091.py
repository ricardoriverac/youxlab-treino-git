import random
from operator import itemgetter
import time
jogo = {
    'jogador1': random.randint(0,6),
    'jogador2' : random.randint(0,6),
    'jogador3' : random.randint(0,6),
    'jogador4' : random.randint(0,6)
}
ranking = list()
for k , v in jogo.items():
    print(f'O {k} tirou {v}')
    time.sleep(1)
print('Ranking dos jogadores')
ranking = sorted(jogo.items() , key=itemgetter(1) , reverse=True)
for i , v in enumerate(ranking):
    print(f'{i+1}° lugar é o {v[0]} com {v[1]} ')
    time.sleep(1)
