from random import randint
from time import sleep
itens=('Pedra', 'Papel', 'Tesoura')
computador= randint(0, 2)
print("""Suas opções:
    [ 0 ]- Papel
    [ 1 ]- Tesoura
    [ 2 ]- Pedra
      """)
jogador=int(input('Qual a sua escolha?  '))
print('-=-' * 11)
print('JO')
print('-=-' *11)
sleep(1)
print('KEN')
print('-=-' *11)
sleep(1)
print('PO')
print('-=-' *11)
sleep(1)
print('-=-' * 11)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-=-' * 11)
if computador ==0:
    if jogador == 0:
        print('empate!')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Computadir Vence')
    else:
        print('Joagda invalida')
elif computador ==1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1 :
        print('empate')
    elif jogador== 2:
        print('Jogador vence')
    else:
        print('Invalida')
elif computador == 2:
    if jogador== 0:
        print('Jogador vence')
    elif jogador ==  1:
        print('computador vence')
    elif jogador == 2:
        print('empate')
    else:
        print('invalida')
        

    


       