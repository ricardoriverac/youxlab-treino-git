from random import randint
computador = randint(0, 10)
jogador = 0
while jogador != computador:
    jogador = int(input('Escolha um número inteiro entre 0 e 10: '))
    if jogador == computador:
        print('Você \033[1;32mvenceu\033[m, parabéns!')
    else:
        print('Você \033[1;31mperdeu\033[m, tente de novo!')