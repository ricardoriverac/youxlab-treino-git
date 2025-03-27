#Crie um programa que leia o nome completo de uma pessoa e mostre:

#O nome com todas as letras maiusculas

#O nome com todas as letras minusculas

#Quantas letras ao todo (sem considerar espaços).

#Quantas letras tem o primeiro nome

nome = str(input("Qual é o seu nome? "))
letrasNoNome = len(nome)
#primeiroNome = 
min = nome.lower()
mai = nome.upper()

print("Seu nome em maiúsculo: {}.".format(mai)) 

print("Seu nome em minúsculo: {}.".format(min))

print("Seu primeiro nome contem {} letras.".format(nome.find(" ")))

print("Seu nome contem {} números.".format(letrasNoNome))

removerEspaco = len(nome.replace(" ", ""))
print("Seu nome contem {} letras ao todo, sem considerar os espaços.".format(removerEspaco))
