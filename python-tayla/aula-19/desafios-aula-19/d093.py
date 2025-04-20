dados = {}
gol = []

nome = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {nome} jogou? '))
dados['nome'] = nome

for c in range(partidas):
    gols = int(input(f'Quantos gols na paartida {c+1}: '))
    gol.append(gols)
    dados['gols'] = gol
    dados['total'] = sum(gol)

print('-=' * 30)
print(dados)
print('-=' * 30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor de {v}')
print('-=' * 30)

print(f'O jogador {nome} jogou {partidas} partidas')
for i in range(partidas):
    print(f'    => Na partida {i+1}, fez {gol[i]} gols')
print(f'Foi um total de {sum(gol)} gols')