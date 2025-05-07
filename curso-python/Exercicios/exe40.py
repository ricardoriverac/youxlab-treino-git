#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
#mostrando uma mensagem no final, de acordo com a média atingida:

#media abaixo de 5.0: reprovado
#media entre 5.0 e 6.9: recuperação
#media 7.0 ou superior: aprovado

nome = input("Qual é o seu nome? ")

n1 = float(input("Qual é a 1° nota? "))
n2 = float(input("Qual é a 2° nota? "))

media = (n1 + n2) / 2

if media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno de recuperação.")
else:
    print("Aluno aprovado.")
    