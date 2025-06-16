import random
import time
from operator import itemgetter
jogadore = {}
jogador1 = jogadore['Jogador 1'] = random.randint(1, 6)
jogador2 = jogadore['Jogador 2'] = random.randint(1, 6)
jogador3 = jogadore['Jogador 3'] = random.randint(1, 6)
jogador4 = jogadore['Jogador 4'] = random.randint(1, 6)
for c, l in jogadore.items():
    print(f'O {c} tirou {l}')
    time.sleep(1)
ranking = []
ranking = sorted(jogadore.items(), key =itemgetter(1), reverse= True)
for j, o in enumerate(ranking):
    print(f'{j} lugar com {o[0]} que tirou: {o[1]}')
