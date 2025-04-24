from random import randint
from time import sleep
adivinhaMega = []
numerojogos = int(input('Quantos jogos você quer gerar? '))
for contagem in range(numerojogos):
    jogo = []
    for qtdValores in range(6):
        sorteio = randint(1, 60)
        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)
    jogo.sort()
    adivinhaMega.append(jogo[:])
    print(f'Jogo {contagem + 1}: {adivinhaMega[contagem]}')
    sleep(0.5)
print()
print(f'\033[38;5;198m★ Boa sorte!')