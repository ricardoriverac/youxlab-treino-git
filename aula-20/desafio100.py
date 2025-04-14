from random import randint
def sorteio(lista):
    for i in range(5):
        lista.append(randint(0, 5))
    print(f'Lista com os números sorteados: {lista}')
def somapar(num):
    soma = 0
    for valor in num:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares é: {soma}')
numeros = []
sorteio(numeros)
somapar(numeros)