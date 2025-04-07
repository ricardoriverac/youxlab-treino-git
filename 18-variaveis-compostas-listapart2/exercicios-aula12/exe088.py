lista60 = []
import random
for c in range(1 , 61):
    lista60.append(c)
jogos = int(input('Quantos jogos quer que eu sorteie? : '))
for c in range(1,jogos+1):
    print(f'Jogo {c}: {random.sample(lista60, 6)}')
print('-='*10 , end='')
print('Boa sorte', end='')
print('-='*10)
    