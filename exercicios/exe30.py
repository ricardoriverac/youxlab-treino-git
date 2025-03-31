#Crie um programa que leia um número inteiro e mostre na tela se e par ou impar

n = int(input("Qual é o número? "))
resultado = n % 2

if resultado == 0:
    print("O número {} e par.".format(n))
else: print("O número {} e impar.".format(n))