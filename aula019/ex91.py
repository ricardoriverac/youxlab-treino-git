
from random import randint
#from time import sleep
from operator import itemgetter

resultados = {'play1':randint(1,6),
             'play2':randint(1,6),
             'play3':randint(1,6),
             'play4':randint(1,6)}

ranking = {}

for chave, valor in resultados.items():
    print(f'O jogador {chave}, tirou o número: {valor} ')
    #sleep(1)

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print(ranking)


for contador ,valor in enumerate(ranking):
    print(f'{contador +1} lugar: {valor[0]} com {valor[1]} ')

    