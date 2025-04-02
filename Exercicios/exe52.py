#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

numero = int(input("Digite um número: "))

if numero <= 1:
    print(f"O Número {numero} não é primo.")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"O Número {numero} é primo.")
else:
    print(f"O Número {numero} não é primo.")
