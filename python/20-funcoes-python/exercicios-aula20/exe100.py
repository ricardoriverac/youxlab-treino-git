from random import randint
def sorteia(numeros):
    for c in range(5):
        numeros.append(randint(0,100))

def somaPar(numeros):
    par = list()
    for num in numeros:
        if num % 2 == 0:
            par.append(num)
    somap = sum(par)
    print(f'Os valores pares {par} somados foram {somap}')

            


#programa principal
numeros = []
sorteia(numeros)
print(f'Os valores sorteados foram {numeros}')
somaPar(numeros)