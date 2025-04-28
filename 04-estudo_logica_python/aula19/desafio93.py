gols = []
jogador = {}
soma = ''
jogador['Nome'] = str(input('Qual o nome do Jogador? ')).title().strip()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na Partida {c+1} ? ')))
    jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('--'*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O {k} tem o valor {v}.')
print('--'*30)
print(f'O Jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f' Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {(jogador["total"])} gols nas partidas.')