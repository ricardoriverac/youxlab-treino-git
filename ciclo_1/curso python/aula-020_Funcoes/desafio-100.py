import random
numeros = []
valorPar = []
def sorteia():
    for c in range (5):
        sort = random.randint(1, 60)
        numeros.append(sort)
    print(f'Os números sorteados foram {numeros}')


sorteia()

def somaPar():
    for valor in numeros:
        if valor % 2 == 0:
            valorPar.append(valor)
    somaP = sum(valorPar)
    print(f'A soma dos pares de {numeros} é {somaP}')
    print(f'Os valores pares são {valorPar}')


somaPar()