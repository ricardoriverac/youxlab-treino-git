jogador = dict()
golsporpartida = []
totalgols = 0

jogador['nome'] = str(input('Digite o nome do jogador: '))
numeropartidas = int(input('Quantas partidas o jogador jogou?: '))

for partida in range(numeropartidas):
    gols = int(input(f'Quantos gols na partida {partida + 1}?: '))
    golsporpartida.append(gols)
    totalgols += gols

jogador['gols'] = golsporpartida[:]
jogador['total'] = totalgols

print('_' * 40)
print(jogador)
print('_' * 40)

for chave, valor in jogador.items():
    print(f'O campo "{chave}" tem o valor {valor}')

print('_' * 40)
print(f'O jogador {jogador["nome"]} jogou {numeropartidas} partidas.')

for i, gols in enumerate(jogador['gols']):
    print(f'Na partida {i + 1}, fez {gols} gols.')

print(f'Ele fez um total de {jogador["total"]} gols.')
