from random import randint
from time import sleep
numero = int(input('Tente descobrir qual número escolhi, digite um número de a 0 a 5: '))
print('PROCESSANDO...')
numeroEscolhido = 3
if numero == 3:
    print('Parabéns, você adivinhou o número! ')
else:
    print('GANHEI MUHAHAHA! Eu pensei no número {} não no {}!'.format(numeroEscolhido, numero))

computador = randint(0, 5) #Faz o computador "PENSAR" 
print('-=-' * 20)
print('Escolhi um número de 0 a 5, tente adivinhar! ')
print('-=-' *20)
numero = int(input('Tente adinhar o número: ')) #Faz o jogador pensar em um número
print('PROCESSANDO...')
sleep(2)
if numero == computador:
    print('PARABÉNS! Você acertou!')
else:
    print('GANHEI! o número que pensei era {} e não {}! '.format(computador, numero))
