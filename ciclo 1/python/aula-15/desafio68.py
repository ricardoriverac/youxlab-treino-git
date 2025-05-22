import random

print('--'*12)
print(' Jogo de PAR ou IMPAR!')
print('--'*12)

print('Vamos jogar PAR ou Impar!!!\n')

c_win = 0


while True:
    n_pc = random.randint(1,10)

    n_player = int(input('Jogue um número entre 1 e 10: '))
    r_player = str(input('Par ou Impar: ')).strip().lower()[0]
    total = (n_pc+n_player)%2

    print('')
    if r_player == 'p':
        r_player = int(0)
    elif r_player == 'i':
        r_player = int(1)
    else:
        print('Invalido!')

    print()
    print(f'O computador escolheu o número {n_pc}')

    if total == 0:
        print(f'O total foi de {n_pc+n_player}')
        print('O resultado é PAR\n')
        resp = 0
    else:
        print(f'O total foi de {n_pc + n_player}')
        print('O Resultado é IMPAR\n')
        resp = 1

    if r_player == resp:
        print('Jogador Pontuou!')
        c_win += 1
        print('=-'*15)
        print('')
    elif r_player != resp:
        print('Jogador Perdeu!')
        print('=-' * 15)
        print('')
        break

if c_win == 1:
    print(f'Jogador Ganhou {c_win} vez !')
elif c_win >1:
    print(f'O jogador GANHOU {c_win} vezes')
else:
    print('O jogador não ganhou nenhuma vez!')