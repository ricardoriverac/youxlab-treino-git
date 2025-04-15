import random
from time import sleep
from operator import itemgetter

valores = {'jogador1' : random.randint(1,6),
'jogador2' : random.randint(1,6),
'jogador3' : random.randint(1,6),
'jogador4' : random.randint(1,6)}

ranking = {}

print('VALORES SORTEADOS')
for k,v in valores.items():
    print(f'{k} tirou {v} ')
    sleep(0.8)
ranking = sorted(valores.items(),key=itemgetter(1),reverse=True)
print('--'*35)

for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.8)