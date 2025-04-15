import random
from time import sleep

print("-" * 40)
print("        GERADOR DE PALPITES MEGA SENA")
print("-" * 40)

jogos = []
quantidade = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(quantidade):
    jogo = sorted(random.sample(range(1, 61), 6))
    jogos.append(jogo)

print("\nSORTEANDO OS JOGOS...")
sleep(1)

for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")
    sleep(0.5)

print("-" * 40)
print("BOA SORTE!")
