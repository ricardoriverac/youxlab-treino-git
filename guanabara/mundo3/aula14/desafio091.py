import random
from operator import itemgetter

jogadas = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6)
}

print("Resultados das jogadas:")
for jogador, valor in jogadas.items():
    print(f"{jogador} tirou {valor}")

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)


print("\nRanking dos jogadores:")
for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{i}º lugar: {jogador} com {valor}")