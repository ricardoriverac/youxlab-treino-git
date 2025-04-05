#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 a 60 para cada jogo, cadastrado tudo em uma lista composta.

from random import sample
from time import sleep

jogos = []

quantidade = int(input("Quantos jogos você quer: "))

for j in range(quantidade):
    randomNum = sample(range(1, 61), 6)
    randomNum.sort()
    jogos.append(randomNum)

print("\nGerando seus palpites...\n")
print("Seus palpites para MEGA SENA:")
for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")
    sleep(0.7)

print("\nBoa sorte! Que você fique rico... e lembre de mim 😎💸")
