import random
from time import sleep

vitorias = 0
derrotas = 0
chance = 5

while True:
    for t in range(5):
        numAleatorio = random.randint(1, 10)
        print(numAleatorio)
        tentativa = int(input("\nPalpite um número: "))

        if tentativa == numAleatorio:
            print(f"Parabens, você acertou o número aleatorio")
            vitorias += 1
            print(f"Vitorias: {vitorias}")
        else:
            chance -= 1
            print(f"Você errou. chance restante: {chance}\n")
            print(chance)
        
        if chance == 0:
            derrotas += 1
            print("Voce perdeu!")
            print(f"O número aleatorio era: {numAleatorio}")
            print(f"\nVitorias: {vitorias}")
            print(f"Derrotas: {derrotas}\n")

        