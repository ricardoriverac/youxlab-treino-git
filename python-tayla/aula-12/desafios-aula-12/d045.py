from random import randint
inicio = print('Vamos jogar jokenpô?')
jogadas = ('Pedra', 'Papel', 'Tesoura')
print("""Suas opções:
[0] pedra
[1] papel
[2] tesoura""")
computador = randint(0,2)
jogou = jogadas[computador]
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;36m-=\033[m' * 12 )
print(f'O computador jogou {jogou}')
print(f'Jogador jogou {jogadas[jogador]}')
print('\033[1;36m-=\033[m' * 12)

if computador == 0:
    if jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Deu empate')

if computador == 1:
    if jogador == 2:
        print('Você venceu!')
    elif jogador == 0:
        print('Você perdeu!')
    else:
        print('Deu empate')

if computador == 2:
    if jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('Você perdeu!')
    else:
        print('Deu empate')