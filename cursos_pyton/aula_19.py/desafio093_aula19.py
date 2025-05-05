gols = []
jogador = {}
soma = ''
jogador['Nome'] = str(input('Qual o nome do Jogador? ')).title().strip()
partidas = int(input(f'Quantas partidas {jogador["Nome"]} já jogou? '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c+1} ? ')))
    jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print()
print(f'O Jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'Na partida {k+1}, fez {v} gols')
print(f'Foi um total de {(jogador["total"])} gols nas partidas jogadas')