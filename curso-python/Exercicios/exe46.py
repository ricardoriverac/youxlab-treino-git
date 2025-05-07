#Faça um programa que mostre na tela uma contagem regressiva para o estouro
#de fogos de artificio, indo de 10 ate, com uma pausa de 1 segundo entre eles.

import time

for j in range(10, -1, -1):
    print("Falta {} segundos, para os fogos de artifício.".format(j))
    time.sleep(1)
print("BOOM!!, estorou os fogos de artifício. 🎉🎊")