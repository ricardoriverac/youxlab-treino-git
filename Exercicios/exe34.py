#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#Para salarios superiores a R$1.250.00, calcule um aumento de 10%
#Para salarios inferiores ou iguais, o aumento é de 15%
#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o seu salário? "))

if salario >= 1250:
    aumento = 10 / 100
    salarioAumentado = salario + (salario * aumento)
    print("Seu salário atual com 10% de aumento e R${:.0f}.".format(salarioAumentado))
elif salario < 1250:
    aumento = 15 / 100
    salarioAumentado = salario + (salario * aumento)
    print("Seu salário atual com 15% de aumento e R${:.0f}.".format(salarioAumentado))