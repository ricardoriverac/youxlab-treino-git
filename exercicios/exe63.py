#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
#primeiros elementos de uma sequencia de fibonacci.

#ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

#Obs: a sequencia de leonardo fibonacci
#Cada número é a soma dos seus dois antecessores
# 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21
# 1 + 1 = 2, 1 + 2 = 3 e assim por diante.

n = int(input("Digite um número: "))
a, b = 0, 1
contador = 0

while contador < n:
    print(a, end=" - " if contador < n - 1 else "\n")
    a, b = b, a + b
    contador += 1