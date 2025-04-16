from random import randint
from time import sleep

def sorteio():
    numeros = []
    print('sorteando 5 valores...', end='')
    for _ in range(5):
        numero = randint(0, 10)
        numeros.append(numero)
        print(f'{numero}', end='', flush=True)
        sleep(0.2)
    print('\nPronto! :D')
    return numeros

def somapar(numeros):
    sleep(0.3)
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'somando os valores pares de {numeros}, temos {soma}')

valores = sorteio()
somapar(valores)