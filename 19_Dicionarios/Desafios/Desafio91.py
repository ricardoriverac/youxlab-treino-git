
import random

jogada = {}

final = []

for i in range(4):

    jogada['n_jogador'] = i+1

    jogada['n_dados'] = random.randint(1, 6)

    final.append(jogada.copy())

    print(f"jogador{jogada['n_jogador']} tirou {jogada['n_dados']} nos dados")

print(30 * '-')

print(' == RANKING DOS JOGADORES ==')

final = sorted(final, key=lambda k: (k['n_dados']), reverse=True)

for j in final:

    print(f" {final.index(j) + 1}º lugar: jogador {j['n_jogador']} com {j['n_dados']}")