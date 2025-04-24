
from random import randint

from time import sleep





def sortear(n1, n2, n3, n4, n5):

    numeros = [n1, n2, n3, n4, n5]
    print(f'Sorteando 5 valores da lista: ', end='')

    for numero in numeros:
        print(numero, end=' ')
        sleep(0.3)
    print('PRONTO!')
    def soma_par():
        pares = 0
        for i in numeros:
            if i % 2 == 0:
                pares += i
        print(f'Somando os valores \033[33m pares \033[m de {numeros} temos {pares}!')
    soma_par()

# Main program

sortear(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))