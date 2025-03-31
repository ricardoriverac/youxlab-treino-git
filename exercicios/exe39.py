#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se a hora de se alistar ja chegou
#Se ja passou a hora
#Seu programa tambem devera mostrar o tempo que falta ou que passou o prazo

nome = input("Qual é o seu nome? ")
nascimento = int(input("Qual ano você nasceu? "))
anoAtual = 2025

idade = anoAtual - nascimento 

if idade == 18:
    print("Já chegou a hora de se alistar.")
elif idade > 18:
    passou = idade - 18
    print("Já passou da hora de se alistar! Você deveria ter se alistado há {} anos.".format(passou))
else:
    faltam = 18 - idade
    print("Você ainda terá que se alistar, faltam {} anos.".format(faltam))
