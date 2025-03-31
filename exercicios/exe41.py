#A confederação nacional de natação precisa de um programa que leia o ano de nascimento
#de um atleta e mostre sua categoria, de acordo com sua idade:

#ate 9 anos: mirim
#ate 14 anos: infantil
#ate 19 anos: junior
#ate 20 anos: senior
#acima: master

nascimento = int(input("Qual é o ano de nascimento? "))
anoAtual = 2025

idade = anoAtual - nascimento

if idade <= 9:
    print("Class: Mirim")
elif idade <= 14:
    print("Class: Infantil")
elif idade <= 19:
    print("Class: Junior")
elif idade <= 20:
    print("Class: Senior")
else: print("Class: Master")