import time
jogador = dict()

grupo = list()

qjogador = 0

while True:

    nome = str(input('Digite o nome do jogador: '))

    partidas = int(input('Digite quantas partidas ele jogou: '))

    tot = 0

    gol = list()

    for n in range(1, partidas+1):

        gols = int(input(f'Quantos gols ele fez na partida {n}? '))

        gol.append(gols)

        tot += gols

    jogador = {'Nome': nome, 'Gols': gol, 'Total': tot}

    grupo.append(jogador.copy())

    qjogador += 1

    esc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    while esc not in 'SN':

        esc = str(input('Opção inválida! Quer continuar? [S/N]: ')).strip().upper()[0]

    if esc == 'N':

        break

print('-='*19)

print(f'cod. nome        gols          total')

print('-'*36)

for pos, j in enumerate(grupo):

    print(f'{pos:<5}{grupo[pos]["Nome"]:<12}{grupo[pos]["Gols"].__str__():<15}{grupo[pos]["Total"]:>5}')

print('-='*19)

escolhaj = int(input('Mostrar dados de qual jogador? (999 para parar): '))

while escolhaj != 999:

    while escolhaj >= qjogador:

        escolhaj = str(input('Jogador inexistente! Mostrar dados de qual jogador? '))

    print(f'--Levantamento do jogador {grupo[escolhaj]["Nome"]}--')

    for pos in range(1, len(grupo[escolhaj]["Gols"])+1):

        print(f'No jogo {pos} fez {grupo[escolhaj]["Gols"][pos-1]} gols.')

        time.sleep(1)

    escolhaj = int(input('Mostrar dados de qual jogador? (999 para parar): '))

print('Volte sempre')