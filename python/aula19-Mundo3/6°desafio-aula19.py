jogador = {}
time = []
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    totalPartidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou?: '))
    partidas.clear()
    for contador in range(0, totalPartidas):
        partidas.append(int(input(f'    Quantos gols na {contador+1}° partida?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha not in 'SN':
        print('ERRO, você precisa digitar "S" ou "N" ')
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('\nCódigo', end=' ')
for indice in jogador.keys():
    print(f'{indice:<15}', end=' ')
print()
for key, value in enumerate(time):
    print(f'{key:>3} ', end=' ')
    for dado in value.values():
        print(f' {str(dado):>15} ', end=' ')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO, jogador não cadastrado com {busca}')
    else:
        print(f'JOGADOR {time[busca]["nome"]}: ')
        for indice, gols in enumerate(time[busca]['gols']):
            print(f'    No jogo {indice+1} fez {gols} gols')


