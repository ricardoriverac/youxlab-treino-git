from random import randint
print('\033[1;34m=-=-=-=-=- Eai, bora jogar jokenpo? -=-=-=-=-=\033[m')
jogadas = ('Pedra', 'Papel', 'Tesoura')
print("""Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura""")
computador = randint(0,2)
jogou = jogadas[computador]
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;34m-=\033[m' * 12 )
print('JO\nKEN\nPO!!!')
print('\033[1;34m-=\033[m' * 12 )
print(f'O computador jogou {jogou}')
print(f'Jogador jogou {jogadas[jogador]}')
print('\033[1;34m-=\033[m' * 12)

if computador == 0:
    if jogador == 1:
        print('\033[1;32mVocê venceu!\033[m')
    elif jogador == 2:
        print('\033[1;31mVocê perdeu!\033')
    else:
        print('\033[1;36mDeu empate\033[m')

if computador == 1:
    if jogador == 2:
         print('\033[1;32mVocê venceu!\033[m')
    elif jogador == 0:
        print('\033[1;31mVocê perdeu!\033m')
    else:
        print('\033[1;36mDeu empate\033[m')

if computador == 2:
    if jogador == 0:
        print('\033[1;32mVocê venceu!\033[m')
    elif jogador == 1:
        print('\033[1;31mVocê perdeu!\033')
    else:
        print('\033[1;36mDeu empate\033[m')