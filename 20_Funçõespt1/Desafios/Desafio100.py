import random

numeros = []

def sorteia():
    for i in range(5):
        n = random.randint(1,10)
        numeros.append(n)
    print('Números sorteados:', numeros)

def somaPar():
     soma = 0
     for num in numeros:
         if num % 2 == 0:
              soma = soma + num
     print('Soma dos pares:',soma)


sorteia()
somaPar()
