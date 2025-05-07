#Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores "M" ou "F".
#Caso esteja errado, peça a digitaçao novamente ate ter um valor correto.


nome = input("Qual é o seu nome: ")
sexo = str(input("Qual é o seu sexo: "))

while sexo != "M" and sexo != "F":
    print("Entrada inválida! Por favor, digite apenas 'M' ou 'F'.")
    sexo = str(input("Digite o sexo novamente: "))