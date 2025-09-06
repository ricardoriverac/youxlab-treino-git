import random
from time import sleep
jogadores = {
    'Jogador 1': random.randint(1, 6),
    'Jogador 2': random.randint(1, 6),
    'Jogador 3': random.randint(1, 6),
    'Jogador 4': random.randint(1, 6),
}
print("Valores sorteados:")
for jogador, valor in jogadores.items():
    print(f"{jogador} tirou {valor} no dado.")
    sleep(0.5)
ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
print("Ranking dos jogadores:")
for i, (jogador, valor) in enumerate(ranking, 1):
    print(f"{i}º lugar: {jogador} com {valor}")
    sleep(0.5)
