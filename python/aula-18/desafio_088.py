import random

for x in range(int(input('Número de jogos: '))):
    print(f'Jogo {x+1}: {random.sample(range(1, 60), 6)}')
