import random as rd
from time import sleep
numeros = []

def lin():
    print('-='*30)

def sorteia(numeros):
    lin()
    print('Sorteando 5 valores...')
    sleep(1)
    lin()
    for c in range(5):
        numeros.append(rd.randint(0,10))
    print(f'Valores sorteados: {numeros}')
    print()

sorteia(numeros)


def soma(numeros):
    lin()
    print('Somando os valores...')
    sleep(1)
    lin()
    print(f'A soma dos valores {numeros} é igual a : {sum(numeros)}')
    print()

soma(numeros)