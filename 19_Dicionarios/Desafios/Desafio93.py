lista = []
dicionario = {}
dicionario['nome'] = str(input('Nome do jogador:'))

partidas = int(input('Quantas partidas ele jogou?'))

for c in range(1, partidas + 1):

    lista.append(int(input(f'Quantos gols ele fez na {c} partida ?')))

dicionario['gols'] = lista[:] 

dicionario['total'] = sum(dicionario['gols'])

print('-=' * 30)

for k, i in dicionario.items():

    print(f'O campo [{k}] tem valor {i}')

print('-=' * 30)

print(f'O jogador {dicionario["nome"]} jogou no total {partidas}')

for k, i  in enumerate(dicionario['gols']):

    print(f'    =>na partida {k + 1}, ele fez {i} gols')

print(f'O total de gols foi {sum(dicionario["gols"])}')