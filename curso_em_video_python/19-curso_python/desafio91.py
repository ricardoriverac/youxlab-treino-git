from random import randint
from time import sleep
from operator import itemgetter

print('-' *40)
sleep(0.5)
print('\033[1;35mJOGOS DE DADOS\033[m'.center(40))
sleep(0.5)
print('-' *40)
sleep(0.5)
print('\033[3;36mSORTEANDO...\033[m')
sleep(2)


jogo = {'jodador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
numeros = [ ]

for jogadores, num in jogo.items():
    print(f'O \033[1;35m{jogadores}\033[m tirou o número \033[1m{num}\033[m')
    sleep(1)
    numeros.append(num)

sleep(1)
print('\033[3;36mGERANDO RANKING...\033[m')
sleep(2)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for jogador, ranking in enumerate(ranking):
    print(f'\033[1;35m{jogador+1}° lugar\033[m - {ranking}')
