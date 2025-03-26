#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o seu salário? "))

aumento = 15 / 100

salarioAumentado = salario + (salario * aumento)
print("Seu salário atual com 15% de aumento e R${}.".format(salarioAumentado))