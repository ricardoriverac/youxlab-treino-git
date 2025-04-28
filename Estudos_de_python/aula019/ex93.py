jogador={}
contador = 0
gols = []
soma = 0

jogador['nome'] = str(input('Digite o nome do jogador: '))

total = int(input('Quantas partidas o jogador jogou?: '))

while contador != total:
    contador += 1

    gols.append(int(input(f'Digite squando gols fez no {contador} jogo: ')))

    jogador['soma'] = sum(gols)

    jogador['gols'] = gols

print(jogador)

for contador2,pontos in  enumerate(jogador['gols']):

    print(f'---Na partida {contador2} fez {pontos} gols ')
    




