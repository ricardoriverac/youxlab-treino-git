import random
numeros = list()

def sorteia():
    numero = random.sample(range(0, 1000), 5)
    print(f'O número sorteado foi {numero}')
    numeros.append(numero.copy())
def somaPar():
    total = 0
    for lista in numeros:
        for n in lista:
            if n % 2 == 0:
                total += n
    return total
sorteia()
print(f'Lista de sorteios armazenados: {numeros}')
print(f'{somaPar()}')


