#Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5
#e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuario venceu ou perdeu

import random

n = random.randint(0, 5)
chance = 5

while chance > 0:
    chute = int(input("Qual é o número correto? "))

    if chute == n:
        print("Você acertou! Parabens, o número correto é {}".format(n))
        break
    else:
        print("Você errou!")
        chance -= 1

    if chance == 0:
        print("Acabaram suas chances! o número correto era {}".format(n))