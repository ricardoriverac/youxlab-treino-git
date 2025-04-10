#fazer
from random import randint
jokenpo= int (input('Pedra, Papel, Tesoura'))
computador= randint(1 , 3)
print('O computador escolheu {}'.format(computador))
if computador == 1:
    computador = 'Pedra'
elif computador == 2:
    computador = 'Papel'
elif computador == 3:
    computador = 'Tesoura'
if jokenpo == 1 and computador == 2 or 3:
    print('')
