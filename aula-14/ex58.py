from random import randint

computador = randint(0,10)
print('Vamos jogar um jogo. Irei pensar em um número entre 0 e 10, e você terá que tentar acertar')
acertou = False 
tentativas = 0

while not acertou:
    jogador = int(input('Digite seu palpite: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('Acertou com {} tentativas.'.format(tentativas))