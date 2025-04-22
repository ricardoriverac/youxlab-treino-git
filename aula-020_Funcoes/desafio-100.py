import random
def sorteio():
    for c in range (5):
        sort = random.randint(1, 60)
        lista.append(sort)
    print(lista)


lista = []
numPar = []

def somaPar():
    for numero in lista:
        if numero % 2 == 0:
            numPar.append(numero)
    soma = sum(numPar)
    print(f'A soma dos numeros pares é {soma} os numeros pares são {numPar}')



somaPar()


sorteio()