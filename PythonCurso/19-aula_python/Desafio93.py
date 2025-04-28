jogador = dict()
partidas = list()
jogador ['nome'] = str(input('Qual o nome do jogador? '))
total = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'     Quantos gols na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['totals'] = sum(partidas)
print('=' * 36)
print(jogador)
print('=' * 36)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 36)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas. ')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["totals"]} gols.')
