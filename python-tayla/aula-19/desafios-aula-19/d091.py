from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
cont = 1

print('Valores sorteados: ')

for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)

print('-=' * 20)

print('  == RANKING DOS JOGADORES ==')

for i in sorted(jogadores, key = jogadores.get, reverse = True):
    print(f'    {cont}ª lugar: {i} com {jogadores[i]}')
    cont += 1
    sleep(1)