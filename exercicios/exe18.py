#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, consseno e tangente desse angulo

from math import radians, sin, cos, tan

angulo = float(input("Digite o angulo que voce deseja: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O angulo de {} tem o Seno de {:.2f}".format(angulo, seno))
print("O angulo de {} tem o Cosseno de {:.2f}".format(angulo, cosseno))
print("O angulo de {} tem o Tangente de {:.2f}".format(angulo, tangente))
