import random
def sorteia():
    numeros = [random.randint(1, 100) for _ in range(5)]
    print(f"Números sorteados: {numeros}")
    return numeros
def somapar(numeros):
    somapar = sum(num for num in numeros if num % 2 == 0)
    print(f"Soma dos números pares sorteados: {somapar}")
numeros_sorteados = sorteia()
somapar(numeros_sorteados)