from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print ('{}SUAS OPÇÕES:{}'.format('\033[36m', '\033[m'))
print ('[0]PEDRA')
print ('[1]PAPEL')
print ('[2]TESOURA')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('JOGADOR jogou {} '.format(itens[jogador]))
print('COMPUTADOR jogou {}'.format(itens[computador]))
if computador==0:
    if jogador==0:
        print('EMPATE! ')
    elif jogador==1:
        print('JOGADOR VENDEU! ')
    elif jogador==2:
        print('COMPUTADOR VENDEU! ')
if computador==1:
    if jogador==0:
        print('COMPUTADOR VENCEU! ')
    elif jogador==1:
        print('EMPATE! ')
    elif jogador==2:
        print('JOGADOR VENCEU! ')
if computador==2:
    if jogador==0:
        print('JOGADOR VENCEU! ')
    elif jogador==1:
        print('COMPUTADOR VENCEU! ')
    elif jogador==2:
        print('EMPATE! ')
