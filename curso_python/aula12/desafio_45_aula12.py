import random
print ('Bora jogar Jokempô!')
opçoes = ('Pedra', 'Papel', 'Tesoura')
print ("""Faça sua escolha:
          [ 0 ] - Pedra
          [ 1 ] - Papel
          [ 2 ] - Tesoura """)
computador = random.randint(0, 2)
jogador = int(input('O que você prefere? '))
if computador == jogador:
    print (f'O computador escolheu {computador} e o jogador também escolheu {jogador}. EMPATE ')
elif computador == 1 and jogador == 0 or computador == 2 and jogador == 1 or computador == 0 and jogador == 2:
    print (f'O computador jogou {computador} e o jogador jogou {jogador}. VOCÊ PERDEU! ')
elif computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0:
    print (f'O computador jogou {computador} e o jogador jogou {jogador}. VOCÊ GANHOU!')