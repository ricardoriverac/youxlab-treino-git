gols = {}
totalGols = []
nomeJogador =gols['Nome do Jogador'] = str(input("Digite o nome do jogador: "))
numPartidas = int(input(f"Digite quantas partidas {nomeJogador} jogou?: "))
for c in range(numPartidas):
    golsNum = int(input(f'Quantos gols {nomeJogador} fez na {c}a partida'))
    totalGols.append(golsNum)
    gols['Gols:'] = totalGols
somaGol = sum(totalGols)
gols['Total'] = somaGol
print(gols)
