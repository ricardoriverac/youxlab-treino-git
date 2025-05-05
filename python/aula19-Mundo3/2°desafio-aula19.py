#JOGO E DADOS
from random import randint
from time import sleep
from operator import itemgetter
jogadores={'jogador1': randint(0,6),
           'jogador2': randint(0,6),
           'jogagor3': randint(0,6),
           'jogador4': randint(0,6)}
ranking=[]
for key, value in jogadores.items():
    print(f'O {key} tirou {value}')
    sleep(1)
ranking=sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for indice, value in enumerate(ranking):
    print(f'{indice+1}° lugar: {value[0]} com {value[1]}')
    sleep(1)