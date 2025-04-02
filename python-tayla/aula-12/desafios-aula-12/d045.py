from random import randint
inicio = print('Vamos jogar jokenpô?')
jogadas = ('Pedra', 'Papel', 'Tesoura')
print("""Suas opções:
[1] pedra
[2] papel
[3] tesoura""")
computador = randint(1,3)
jogou = jogadas[computador]
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;36m-=\033[m' * 12 )
print(f'O computador jogou {jogou}')
print(f'Jogador jogou {jogadas[jogador]}')
print('\033[1;36m-=\033[m' * 12)

if computador == 1:
    if jogador == 2:
        print('Você venceu!')
    elif jogador == 3:
        print('Você perdeu!')
    else:
        print('Deu empate')

if computador == 2:
    if jogador == 2:
        print('Você venceu!')
    elif jogador == 1:
        print('Você perdeu!')
    else:
        print('Deu empate')

if computador == 3:
    if jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Deu empate')