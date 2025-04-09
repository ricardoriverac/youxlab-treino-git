time = list()
partidas = list()
jogador = {}
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas.clear()
    totpart = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for p in range(0,totpart):
        partidas.append(int(input(f'Quantos gols na {p}°: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        sair = str(input('Quer continuar [S/N] ')).upper().strip()
        if sair in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if sair == 'N':
        break
print('-='*30)
print('cod',  end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-='*30)
for k , v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values(): 
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Nao existe esse jogador')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i , g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
        print('-='*30)
print('VOLTE SEMPRE')
