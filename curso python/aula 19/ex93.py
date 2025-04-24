pessoa = {}
totalGols = []
pessoa['nome'] = str(input('Nome do(a) jogador(a): '))
partidas = int(input(f'Quantas partidas {pessoa["nome"]} jogou? '))
for c in range(partidas):
    golsPartida = int(input(f'Quantos gols {pessoa["nome"]} fez na {c+1}ª partida? '))
    totalGols.append(golsPartida)
pessoa['gols'] = totalGols
soma = sum(totalGols)
print ()
print ('-=' * 4, f'\033[35mDADOS\033[m','-=' * 4 )
print('\n' + '-'*40)
print(f'Desempenho do(a) jogador(a): {pessoa["nome"]}')
print('-'*40)
for i, gols in enumerate(pessoa['gols']):
    print(f' {i+1}ª partida: {gols} gol(s)')
print('-'*40)
print(f' Soma total dos gols: {soma}')
print('-'*40)
