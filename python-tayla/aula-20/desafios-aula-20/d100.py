from time import sleep
from random import randint

numeros = []
pares = []

def sorteio(numeros):
    for n in range(5):
        numeros.append(randint(0, 5))

    print('Sorteando 5 valores da lista: ', end='')
    for n in numeros:
        print(f'{n}', end=' ', flush = True)
        sleep(0.5)
    print('PRONTO!')

def somaPar(numeros):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
            pares.append(n)

    print(f'Somando os valores \033[1;34mpares\033[m de ', end='')
    for n in pares:
        print(f'{n}', end=' ', flush = True)
        sleep(0.5)
    print(f'temos {soma}')

sorteio(numeros)
somaPar(numeros)