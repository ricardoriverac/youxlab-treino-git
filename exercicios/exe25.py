#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input("Qual é o seu nome completo? ")).lower()

if "silva" in nome:
    print("O seu nome contem o sobrenome silva!")
else: print("O seu nome não contem o sobrenome silva!")