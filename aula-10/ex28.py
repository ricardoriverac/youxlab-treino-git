from random import randint
computador=randint(0, 5)
print('-'*70)
print('Vou pensar em um número entre 0 e 5, tente adivinhar... ')
print('-'*70)
jogador=int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabéns! Você venceu!!')
else:
    print('Eu ganhei. Eu pensei no número {} e não no {}'.format(computador,jogador))
