from random import randint
from time import sleep
print('Vamos jogar pedra, papel e tesoura?')
print('''Escolha uma jogada:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
itens = ('pedra', 'papel', 'tesoura')
j = int(input('Sua escolha: '))
c = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('')
print('='*15)
print('Você jogou: {}'.format(itens[j]))
print('Eu joguei: {}'.format(itens[c]))
if c == 0:
    if j == 0:
        print('Empate!')
    elif j == 1:
        print('Eu venci')
    elif j == 2:
        print('Você venceu!')
    else:
        print('Jogada inválida! Tente novamente.')
elif c == 1:
    if j == 0:
        print('Empate!')
    elif j == 1:
        print('Você perdeu!')
    elif j == 2:
        print('Você venceu!')
    else:
         print('Jogada inválida! Tente novamente.')
elif c == 2:
    if j == 0:
        print('Você ganhou!')
    elif j == 1:
        print('Você perdeu !')
    elif j == 2:
        print('Empatou!')
    else:
         print('Jogada inválida! Tente novamente.')