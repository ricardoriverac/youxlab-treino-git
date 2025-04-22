import random
from time import sleep
print('-='*20)
print('{:^40}'.format('\033[34mJOGUE NA MEGASENA\033[m'))
print('-='*20)
jogo = []
jogos = int(input('Quantos jogos você quer que eu sorteie?: '))
print('\033[36mSORTEANDO...\033[m')
sleep(3)
for c in range(1, jogos+1):
    numero = random.sample(range(0,60),6)
    jogo.append(numero)
    print(f'\033[35mJogo {c}:\033[m {jogo}')
    jogo.clear()
    sleep(1)
print('-='*20)   
print('{:^40}'.format('\033[32mBOA SORTE!\033[m '))
print('-='*20)
    
     