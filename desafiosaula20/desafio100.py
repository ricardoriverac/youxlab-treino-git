from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando \033[35m5 valores\033[m da lista... ')
    for c in range(0,5):
        num = randint(1,10)
        lista.append(num)
        print(f'{num}', end=' ', flush=True)
        sleep(0.5)
    print()
def somaPar (lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A \033[36mSOMA\033[m de todos os \033[36mNÚMEROS PARES\033[m é {soma}')
    
numeros = []
sorteia(numeros)
somaPar(numeros)


