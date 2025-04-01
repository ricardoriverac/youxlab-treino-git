import random

print('=-=-=-=-=- Eai, bora jogar jokenpo? -=-=-=-=-=')
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA ')
jogada = int(input('Qual sua jogada? '))
print('JO\nKEN\nPO!!!')


numeros = [0, 1, 2]
escolha = e = random.choice(numeros)


if jogada == 0:
    print('-=-=-=-=-=-=-=-=-=-=-=\nComputador jogou {}\nJogador jogou Pedra\n-=-=-=-=-=-=-=-=-=-=-='.format(escolha))
    
    
    #USA CHOICE