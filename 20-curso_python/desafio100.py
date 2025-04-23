from random import randint
numeros = []
par = []

def sorteio(num):
    for i in range(5):
        resultado = randint(1, 101)
        if resultado %2 == 0:
            par.append(resultado)
        numeros.append(resultado)
    print(f'O resultado do sorteio foi {numeros}.')

sorteio(numeros)

def somaPar(num):
    soma = sum(par)
    print(f'Os números pares de {numeros} foram {par}, a soma dos números pares é {soma}')

somaPar(numeros)