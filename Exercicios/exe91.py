#Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatorios.
#Guarde esses resultados em um dicionario. No final, coloque esse dicionario em ordem
#sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo =  {"Jogador1" : randint(1, 6),
         "Jogador2" : randint(1, 6),
         "Jogador3" : randint(1, 6),
         "Jogador4" : randint(1, 6)}

ranking = list()
print("Valores sorteados:")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("-=" * 10)
print(" == RAKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f"    {i+1} lugar: {v[0]} com {v[1]}.")
    sleep(1)