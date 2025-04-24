armazem = {}
listaDeGol = []
soma = 0

armazem['Nome'] = str(input('Qual o nome do jogador?: '))
partidas = int(input(f'Quantas partidas {armazem["Nome"]} jogou?: '))

for v in range(+1, partidas +1):
    Gols = int(input(f'Quantos gols {armazem["Nome"]} fez na partida {v}: '))
    listaDeGol.append(Gols)


armazem['Gols Feitos'] = listaDeGol
armazem['Total de gols'] = sum(listaDeGol)


print('\033[33m=-=\033[m'*15,f'\nO nome do jogador é: {armazem["Nome"]}')
print(f'O jogador {armazem["Nome"]} fez {armazem["Gols Feitos"]} essa sequencia de gols.')
print(f'A soma de todos os gols é: {armazem["Total de gols"]}.')

print('\033[33m=-=\033[m'*15)
print(f'O jogador {armazem["Nome"]} jogou {partidas} partidas')
for i, v in enumerate(armazem["Gols Feitos"]):
    print(f'       => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {armazem["Total de gols"]} gols')
print('\033[33m=-=\033[m'*15)