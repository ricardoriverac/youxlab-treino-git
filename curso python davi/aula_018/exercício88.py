import random
from time import sleep
print("=" * 40)
print("       GERADOR DE JOGOS DA MEGA SENA       ")
print("=" * 40)
jogos = []
quant = int(input("Quantos jogos você quer que eu sorteie? "))
for i in range(quant):
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo)
print("\nSORTEANDO OS JOGOS...")
sleep(1)
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")
    sleep(0.5)
print("-" * 40)
print("Boa sorte!!")