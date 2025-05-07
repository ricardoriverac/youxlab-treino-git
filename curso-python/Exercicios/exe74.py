#Crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla
#Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que está na tupla

import random

tabelaDeNum = ()

for _ in range(5):
    randomNum = random.randint(1, 100)
    tabelaDeNum = tabelaDeNum + (randomNum,)

print(f"Os números da tupla são: {tabelaDeNum}")
print(f"O menor número da tabela é {min(tabelaDeNum)}")
print(f"O maior número da tabela é {max(tabelaDeNum)}")