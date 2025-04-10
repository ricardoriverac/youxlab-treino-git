from random import randint
jokenpo= int ('Escolha um número de 1 a 3: \n 1 para pedra \n 2 para papel \n 3 para tesoura \n ')
computador= randint(1 , 3)
print('O computador escolheu {}'.format(computador))
if jokenpo == 1 and computador == 2 or 3:
    print('')
