# Fiz da forma em que o computador que escolhe os números aleatórios"

from random import randint
numero1= randint(0,100)
numero2= randint(0,100)
numero3= randint(0,100)
numero4= randint(0,100)
numero5= randint(0,100)
lista = [numero1, numero2, numero3, numero4, numero5]
print(lista)
maior = max(lista)
menor = min(lista)
print(f'O maior número da lista é {maior} e o menor é {menor}.')

# Essa é a forma em que o usuário escolhe os números aleatórios:

lista2 = [ ]

for numeros in range(1,6):
    num1 = int(input('Escolha um número: '))
    lista2.append(num1)
    maiorNum = max(lista2)
    menorNum = min(lista2)
print(f'O maior número da lista é {maiorNum} e o menor é {menorNum}.')