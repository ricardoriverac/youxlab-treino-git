from random import randint
from time import sleep

lista = list()
print('='*40)
print('JOGO DA MEGA SENA')
print('='*40)

jogos = int(input('quantos jogos você quer que eu sorteie? '))

for c in range(1,jogos+1):
    print(f'JOGO {c}:',end='')
    for n in range(0,6):
        lista.append(randint(0,60))
    print(sorted(lista))
    lista.clear()
    sleep(1)

print('='*40)
print('obrigado por jogar! Boa sorte.')