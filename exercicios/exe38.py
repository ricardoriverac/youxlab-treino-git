#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela
#O primeiro valor e maior
#O segundo valor e maior
#Não existe valor maior, os dois são iguais

n1 = int(input("Digite o número 1°: "))
n2 = int(input("Digite o número 2°: "))

if n1 > n2:
    print("O primeiro valor é maior.")
elif n2 > n1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
