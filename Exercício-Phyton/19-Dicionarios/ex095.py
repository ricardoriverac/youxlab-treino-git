gols = []
jogador = {}
time = []
soma = ''
while True:
    jogador['Nome'] = str(input('Qual o nome do Jogador? ')).title().strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na Partida {c+1} ? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    while True:
        perg = str(input('Quer continuar? (S/N) ')).upper()
        if perg in 'SN':
            break
        print('digite apenas N ou S.')
    if perg == 'N':
        break
print('-'*40)
print(f'{"cod ":<3}', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--'*40)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*40)
while True:
    resp = int(input('Qual jogador quer saber as informações? [999 para sair]: '))
    if resp == 999:
        break
    elif resp >= len(time):
        print(f'Nao existe jopgador com número {resp}.')
    else:
        print('Levantamento em andamento.....')
        print(f'O Jogador {time[resp]["Nome"]} fez {time[resp]["total"]} gols.')
        for k, v in enumerate(time[resp]['gols']):
            print(f' Na partida {k+1}, fez {v} gols.')