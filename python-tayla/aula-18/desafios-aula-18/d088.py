from random import sample
from time import sleep

valores = []

print('\033[1m-\033[m' * 27)
print('\033[1;36m     JOGA NA MEGA SENA\033[m')
print('\033[1m-\033[m' * 27)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print('')
print(f'-=-=-=-=-= SORTEANDO {quantidade} JOGOS -=-=-=-=-=')

for c in range(quantidade):
    numeros = sample(range(1, 60),6)
    valores.append(numeros)

for n, v in enumerate(valores):
    print(f'Jogo {n+1}: {v} ')
    sleep(1)

print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')