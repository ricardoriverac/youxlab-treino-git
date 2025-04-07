import random
num = random.randint(0, 10)
jogador = int(input("Digite um número:"))
while jogador != num:
    print('Você errou tente de novo:')
    jogador = int(input("Digite um número:"))
else:
    print('Você acertou!')