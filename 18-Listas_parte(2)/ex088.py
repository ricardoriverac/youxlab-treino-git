from random import randint
from time import sleep

mega=[]

numerosjogo = int(input('Quantos jogos vc deseja fazer:'))
for valores in range (numerosjogo):
    jogo=[]
    for valores1 in range(6):
        sorteio= randint
        sorteio = randint(1, 60)

        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)

    jogo.sort()
    mega.append(jogo[:])
    print(f'Jogo {valores + 1}: {mega[valores]}')
    sleep(0.5)
print()