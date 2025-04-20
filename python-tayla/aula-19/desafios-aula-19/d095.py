from time import sleep
partidas = []
jogadores = {}
time = []

while True:
    jogadores.clear()
    jogadores['nome'] = input('Nome do jogador: ')
    total = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    partidas.clear()

    for c in range(total):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogadores['gols'] = partidas[:]
    jogadores['total'] = sum(partidas)
    time.append(jogadores.copy())

    pergunta = input('Quer continuar? [S/N] ').upper()
    while pergunta not in 'SN':
        pergunta = input('Quer continuar? [S/N] ').upper()
    if pergunta == 'N':
        break

print('-=' * 30)
print('\033[1;36mcod \033[m', end='')
for i in jogadores.keys():
    print(f'\033[1;36m{i:<15}\033[m', end='')
print()

print('—' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('—' * 40)

while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if escolha == 999:
        break
    if escolha >= len(time):
        print(f'\033[1;31mERRO!\033[m Não existe jogador com código {escolha}')
    else:
        print(f'\033[1;33m—— LEVANTAMENTO DO JOGADOR {time[escolha]["nome"]}: \033[m')
        for i, g in enumerate(time[escolha]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print('—' * 40)
sleep(0.5)
print('\033[1mFINALIZANDO...')
print('<< VOLTE SEMPRE >>\033[m')