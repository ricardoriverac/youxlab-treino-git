#Melhore o jogo do desafio 028 onde vai "pensar" em um número de 0 a 10
#So que agora o jogador vai tentar advinhar ate acertar, mostrando no final
#quantos palpites necessarios para vencer

import random

n = random.randint(0, 5)
chance = 5

while chance > 0:
    palpite = int(input("Qual é o número correto? "))

    if palpite == n:
        print("Você acertou! Parabens, o número correto é {}".format(n))
        break
    else:
        print("\nVocê errou!")
        chance -= 1
        print(f"Você tem {chance} chances ainda.\n")

    if chance == 0:
        print("Acabaram suas chances! o número correto era {}".format(n))
print("Acabou")