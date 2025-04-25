gols = {}
totalGols = []
time = []
while True:
    gols.clear()
    nomeJogador =gols['Nome do Jogador'] = str(input("Digite o nome do jogador: "))
    numPartidas = int(input(f"Digite quantas partidas {nomeJogador} jogou?: "))
    for c in range(numPartidas):
        golsNum = int(input(f'Quantos gols {nomeJogador} fez na {c}a partida'))
        totalGols.append(golsNum)
    gols['Gols:'] = totalGols
    somaGol = sum(totalGols)
    gols['Total'] = somaGol
    time.append(gols.copy())
    while True:
        continuar = str(input("Quer continuar? S/N")).upper()
        if continuar in 'SN':
            break
        print('ERRO')
    if continuar == 'N':
        break
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print(gols)