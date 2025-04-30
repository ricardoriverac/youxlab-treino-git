pessoa = {}
totalGols = []
pessoa['nome'] = str(input('Nome do(a) jogador(a): '))
partidas = int(input(f'Quantas partidas {pessoa["nome"]} jogou? '))
for c in range(partidas):
    golsPartida = int(input(f'Quantos gols {pessoa["nome"]} fez na {c+1}ª partida? '))
    totalGols.append(golsPartida)
pessoa['gols'] = totalGols
soma = sum(totalGols)
pessoa['total gols'] = soma
print ()
print ('\033[35m-=\033[m' * 4, f'\033[35mDADOS\033[m','\033[35m-=\033[m' * 4 )
print ()
print (pessoa)
print('\n' + '\033[35m-\033[m'*40)
for campo, valor in pessoa.items():
    print()
    print(f'O campo {campo} tem o valor = {valor}') # pega a posição 0,0 depois 1,1 ....
print('\n' + '\033[35m-\033[m'*40)
print(f'Desempenho do(a) jogador(a): {pessoa["nome"]}')
print('\n' + '\033[35m-\033[m'*40)
for i, gols in enumerate(pessoa['gols']):
    print(f' {i+1}ª partida: {gols} gol(s)')
print('\n' + '\033[36m-\033[m'*40)
print(f' Soma total dos gols: {soma}')
print('\n' + '\033[35m-\033[m'*40)
