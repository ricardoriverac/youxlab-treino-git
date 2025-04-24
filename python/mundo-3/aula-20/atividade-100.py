import random

numeros = []

def sorteia():
    print("Sorteando 5 números: ", end='')
    for _ in range(5):
        n = random.randint(1, 100)
        numeros.append(n)
        print(n, end=' ')
    print()


def somaPar():
    soma = sum(num for num in numeros if num % 2 == 0)
    print(f"Somando os valores pares de {numeros}, temos: {soma}")

sorteia()
somaPar()
