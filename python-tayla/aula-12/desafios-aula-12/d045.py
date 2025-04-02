import random
inicio = print('Vamos jogar jokenpô?')
print("""
[1] pedra
[2] papel
[3] tesoura""")
jogadas = ['pedra' , 'papel' , 'tesoura']
computador = random.randint(1,3)
jogador = int(input('Escolha sua jogada: '))
jogou = jogadas[computador]

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
print(f'O computador jogou {jogou}')