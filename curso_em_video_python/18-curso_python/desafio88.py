from random import sample
from time import sleep
print('-' *40)
sleep(0.5)
texto = ('\033[1;36mJOGO DA MEGA SENA\033[m')
print(texto.center(50))
sleep(0.5)
print('-' *40)
sleep(0.5)

jogos = int(input('\033[1mQuantos jogos você quer jogar?\033[m '))
sleep(1)
lista = [ ]
print('-' * 40)
print(f'\033[2;36mSORTEANDO {jogos} JOGOS...\033[m')
sleep(2)

for sorteio in range(1, jogos+1):
    sorteados = sample(range(1, 61), 6)
    lista.append(sorteados)
    print(f'\033[1;36mJogo {sorteio}:\033[m {sorteados}')
    sleep(1)