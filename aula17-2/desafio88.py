from random import randint
from random import shuffle
megasena = list(range(0,61))
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
pergunta = int(input('Quantos jogos quer que eu sorteie? '))
for aposta in range(1, pergunta+1):
    print(f'Jogo {aposta}: ', end='')
    shuffle(megasena)
    print(megasena[:6])
    del(megasena[:6])